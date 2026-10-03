"""Contrato de conteudo da Aula 3, que o validador generico nao cobre."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MODULE = DOCS / "modulo-3-design-e-padroes"
IMAGES = DOCS / "assets" / "images"
STYLESHEET = DOCS / "assets" / "stylesheets" / "extra.css"

BLOCKS = {
    "bloco-1-principios-de-design.md": ("modulo-3-principios-ao-desenho-logico.svg", 9),
    "bloco-2-estilos-arquiteturais.md": ("modulo-3-estilos-forcas-compromissos.svg", 10),
    "bloco-3-padroes-arquiteturais-e-de-design.md": ("modulo-3-niveis-de-padrao.svg", 11),
    "bloco-4-registro-de-decisao-arquitetural.md": ("modulo-3-ciclo-de-vida-adr.svg", 12),
}

PRINCIPLES = (
    "Simplicidade", "Separação de responsabilidades", "Baixo acoplamento",
    "Alta coesão", "Encapsulamento", "Desenho para falha", "Observabilidade",
    "Segurança por desenho", "Evolução incremental",
)

STYLES = (
    "Arquitetura em camadas", "Arquitetura de microsserviços",
    "Arquitetura orientada a eventos", "Arquitetura microkernel",
    "Arquitetura hexagonal", "Pipes and filters", "Arquitetura orientada a APIs",
)

STYLE_ASPECTS = (
    "Forma estrutural", "Componentes e comunicação", "Favorece", "Prejudica",
    "Quando usar", "Quando evitar", "Anti-padrão",
)

PATTERNS = (
    "Strangler Fig", "Anti-Corruption Layer", "Adapter", "API Gateway",
    "Timeout", "Retry com limite", "Circuit Breaker", "Bulkhead",
    "Transactional Outbox", "Saga",
)

PATTERN_ASPECTS = (
    "Problema", "Contexto e forças", "Estrutura mínima",
    "Consequência favorável", "Custo", "Sinal de uso inadequado",
)

FORBIDDEN_IN_VISUALS = ("ACME", "COBOL", "CICS", "matrícula", "Matrícula")


def read(name: str) -> str:
    return (MODULE / name).read_text(encoding="utf-8")


def section(text: str, heading_regex: str) -> str:
    """Devolve o trecho entre o cabecalho de nivel 2 indicado e o seguinte."""
    match = re.search(rf"^##\s+{heading_regex}\s*$", text, re.MULTILINE)
    if match is None:
        return ""
    rest = text[match.end():]
    end = re.search(r"^##\s", rest, re.MULTILINE)
    return rest[: end.start()] if end else rest


class ModuleThreeStructureTest(unittest.TestCase):
    def test_custom_stylesheet_url_is_versioned_to_avoid_stale_layout(self):
        config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        self.assertRegex(
            config,
            r"(?m)^\s+- assets/stylesheets/extra\.css\?v=\d{8}-\d+$",
        )

    def test_module_diagrams_stay_inside_the_content_column(self):
        css = STYLESHEET.read_text(encoding="utf-8")
        rule = re.search(
            r"\.md-typeset img\.module-diagram\s*\{(?P<body>.*?)\n\}",
            css,
            re.DOTALL,
        ).group("body")

        self.assertRegex(rule, r"width:\s*100%")
        for overflow_technique in ("100vw", "translateX", "margin-left"):
            self.assertNotIn(overflow_technique, css)

    def test_figure_wrapping_a_module_diagram_takes_the_column_width(self):
        # Material define figure com width: fit-content, e um SVG so com viewBox
        # encolhe a figura para cerca de 300 px.
        css = STYLESHEET.read_text(encoding="utf-8")
        rule = re.search(
            r"\.md-typeset figure:has\(> img\.module-diagram\)\s*\{(?P<body>[^}]*)\}",
            css,
        )
        self.assertIsNotNone(rule)
        self.assertRegex(rule.group("body"), r"width:\s*100%")

    def test_module_diagrams_use_legible_internal_type(self):
        for image, _ in BLOCKS.values():
            svg = (IMAGES / image).read_text(encoding="utf-8")
            sizes = [int(size) for size in re.findall(r"font-size:(\d+)px", svg)]
            with self.subTest(image=image):
                self.assertTrue(sizes)
                self.assertGreaterEqual(min(sizes), 16)

    def test_all_pages_exist_and_are_in_nav(self):
        nav = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        for name in ("index.md", *BLOCKS, "sintese.md"):
            with self.subTest(page=name):
                self.assertTrue((MODULE / name).is_file())
                self.assertIn(f"modulo-3-design-e-padroes/{name}", nav)

    def test_each_block_has_its_numbered_exercise(self):
        for name, (_, number) in BLOCKS.items():
            with self.subTest(page=name):
                self.assertRegex(read(name), rf"(?m)^## Exercício {number}\s*$")

    def test_each_block_has_an_accessible_local_visual(self):
        for name, (image, _) in BLOCKS.items():
            with self.subTest(page=name):
                self.assertRegex(
                    read(name),
                    rf"!\[[^\]]{{40,}}\]\(\.\./assets/images/{re.escape(image)}\)"
                    r"\{ \.module-diagram \}",
                )
                svg = (IMAGES / image).read_text(encoding="utf-8")
                self.assertRegex(svg, r"<title[^>]*>[^<]{5,}</title>")
                self.assertRegex(svg, r"<desc[^>]*>[^<]{20,}</desc>")

    def test_visuals_do_not_carry_case_data(self):
        for image, _ in BLOCKS.values():
            svg = (IMAGES / image).read_text(encoding="utf-8")
            for term in FORBIDDEN_IN_VISUALS:
                with self.subTest(image=image, term=term):
                    self.assertNotIn(term, svg)

    def test_no_page_keeps_the_old_framing_line(self):
        for page in MODULE.glob("*.md"):
            text = page.read_text(encoding="utf-8")
            for phrase in ("fecha a aula", "abre a aula"):
                with self.subTest(page=page.name, phrase=phrase):
                    self.assertNotIn(phrase, text)


class ExerciseChainTest(unittest.TestCase):
    def test_exercise_10_consumes_exercise_9(self):
        ex = section(read("bloco-2-estilos-arquiteturais.md"), "Exercício 10")
        self.assertIn("bloco-1-principios-de-design.md#exercicio-9", ex)
        for term in ("adequação", "risco introduzido", "mecanismo compensatório"):
            self.assertIn(term, ex)

    def test_exercise_11_consumes_exercise_10(self):
        ex = section(read("bloco-3-padroes-arquiteturais-e-de-design.md"), "Exercício 11")
        self.assertIn("bloco-2-estilos-arquiteturais.md#exercicio-10", ex)
        for term in ("coexistência", "falha de integração", "publicação confiável",
                     "elemento afetado", "consequência favorável", "custo aceito"):
            self.assertIn(term, ex)

    def test_exercise_12_consumes_the_three_previous_products(self):
        ex = section(read("bloco-4-registro-de-decisao-arquitetural.md"), "Exercício 12")
        for anchor in (
            "bloco-1-principios-de-design.md#exercicio-9",
            "bloco-2-estilos-arquiteturais.md#exercicio-10",
            "bloco-3-padroes-arquiteturais-e-de-design.md#exercicio-11",
        ):
            with self.subTest(anchor=anchor):
                self.assertIn(anchor, ex)
        self.assertIn("gatilho", ex)

    def test_exercise_9_lists_the_four_case_inputs(self):
        ex = section(read("bloco-1-principios-de-design.md"), "Exercício 9")
        for term in ("período letivo", "território nacional", "30/09/2027", "10 minutos"):
            with self.subTest(term=term):
                self.assertIn(term, ex)
        for field in ("nome", "motivação", "implicação", "evidência"):
            self.assertIn(field, ex)


class RepertoireTest(unittest.TestCase):
    def test_block_1_covers_concepts_principles_and_transformation(self):
        text = read("bloco-1-principios-de-design.md")
        for term in ("Objetivo", "Requisito", "Princípio", "Decisão", "Elemento lógico",
                     *PRINCIPLES, "desenho conceitual", "desenho lógico"):
            with self.subTest(term=term):
                self.assertIn(term, text)

    def test_block_2_standardizes_the_seven_styles(self):
        text = read("bloco-2-estilos-arquiteturais.md")
        for style in STYLES:
            with self.subTest(style=style):
                match = re.search(rf"^### {re.escape(style)}\s*$", text, re.MULTILINE)
                self.assertIsNotNone(match)
                rest = text[match.end():]
                end = re.search(r"^##", rest, re.MULTILINE)
                body = rest[: end.start()] if end else rest
                for aspect in STYLE_ASPECTS:
                    self.assertIn(aspect, body, f"{style}: {aspect}")

    def test_block_2_links_styles_to_block_1_principles(self):
        text = read("bloco-2-estilos-arquiteturais.md")
        self.assertIn("bloco-1-principios-de-design.md", text)
        self.assertLessEqual(text.count("Lei de Conway"), 2)

    def test_block_3_uses_the_three_level_taxonomy(self):
        text = read("bloco-3-padroes-arquiteturais-e-de-design.md")
        for level in ("Estilo arquitetural", "Padrão arquitetural", "Padrão de design"):
            self.assertIn(level, text)

    def test_block_3_describes_each_pattern_with_the_six_aspects(self):
        text = read("bloco-3-padroes-arquiteturais-e-de-design.md")
        for pattern in PATTERNS:
            with self.subTest(pattern=pattern):
                match = re.search(rf"^#### {re.escape(pattern)}\s*$", text, re.MULTILINE)
                self.assertIsNotNone(match)
                rest = text[match.end():]
                end = re.search(r"^#{2,4}\s", rest, re.MULTILINE)
                body = rest[: end.start()] if end else rest
                for aspect in PATTERN_ASPECTS:
                    self.assertIn(aspect, body, f"{pattern}: {aspect}")

    def test_strangler_fig_is_never_called_a_style(self):
        for name in ("bloco-2-estilos-arquiteturais.md",
                     "bloco-3-padroes-arquiteturais-e-de-design.md"):
            text = read(name).lower()
            for phrase in ("estilo strangler", "estilo estrangulador"):
                with self.subTest(page=name, phrase=phrase):
                    self.assertNotIn(phrase, text)

    def test_block_4_template_fields_have_quality_criterion_and_frequent_error(self):
        text = read("bloco-4-registro-de-decisao-arquitetural.md")
        self.assertIn("Critério de qualidade", text)
        self.assertIn("Erro frequente", text)


class IndexSynthesisAndReferenceTest(unittest.TestCase):
    def test_index_has_objectives_schedule_route_and_bridges(self):
        text = read("index.md")
        for heading in ("Objetivos de aprendizagem", "Grade de tempo",
                        "Roteiro da aula", "Entrada recebida da Aula 2",
                        "Preparação para a Aula 4"):
            with self.subTest(heading=heading):
                self.assertRegex(text, rf"(?m)^## {heading}\s*$")
        for name in (*BLOCKS, "sintese.md"):
            self.assertIn(f"({name})", text)

    def test_synthesis_has_checklist_chain_self_assessment_and_sources(self):
        text = read("sintese.md")
        for heading in ("Checklist do que precisa permanecer",
                        "Cadeia da decisão", "Autoavaliação", "Fontes da aula"):
            with self.subTest(heading=heading):
                self.assertRegex(text, rf"(?m)^## {heading}\s*$")
        chain = section(text, "Cadeia da decisão")
        for term in ("objetivo", "requisito", "princípio", "estilo", "padrão", "decisão"):
            self.assertIn(term, chain.lower())

    def test_glossary_defines_the_new_terms(self):
        text = (DOCS / "referencia" / "glossario.md").read_text(encoding="utf-8")
        for heading in ("Princípio de design", "Desenho conceitual", "Desenho lógico",
                        "Padrão arquitetural", "Padrão de design"):
            with self.subTest(heading=heading):
                self.assertRegex(text, rf"(?m)^## {heading}\s*$")

    def test_bibliography_lists_the_new_sources(self):
        text = (DOCS / "referencia" / "bibliografia.md").read_text(encoding="utf-8")
        for author in ("Gamma, E.", "Evans, E.", "Fowler, M.", "Richardson, C.",
                       "Nygard, M. (2018)"):
            with self.subTest(author=author):
                self.assertIn(author, text)


class ReviewFindingsTest(unittest.TestCase):
    """Achados da revisao final da branch, fixados para nao regredirem."""

    def test_block_2_quotes_the_maxim_in_the_right_order(self):
        text = read("bloco-2-estilos-arquiteturais.md")
        self.assertIn("a forma segue a função", text)
        self.assertNotIn("a função segue a forma", text)

    def test_retry_is_not_attributed_to_nygard(self):
        text = read("bloco-3-padroes-arquiteturais-e-de-design.md")
        self.assertNotIn("os quatro padrões abaixo pertencem a esse grupo", text)
        match = re.search(r"^#### Retry com limite\s*$", text, re.MULTILINE)
        rest = text[match.end():]
        body = rest[: re.search(r"^#{2,4}\s", rest, re.MULTILINE).start()]
        self.assertNotIn("Nygard", body)

    def test_exercise_11_reproduces_the_virtual_learning_contract_cost(self):
        ex = section(read("bloco-3-padroes-arquiteturais-e-de-design.md"), "Exercício 11")
        self.assertIn("38%", ex)

    def test_exercise_11_points_to_the_logical_sketch_of_exercise_9(self):
        ex = section(read("bloco-3-padroes-arquiteturais-e-de-design.md"), "Exercício 11")
        self.assertIn("bloco-1-principios-de-design.md#exercicio-9", ex)


if __name__ == "__main__":
    unittest.main()
