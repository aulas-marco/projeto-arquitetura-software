"""Contrato de conteudo da Aula 5, que o validador generico nao cobre."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MODULE = DOCS / "modulo-5-frameworks-e-tecnologias"
IMAGES = DOCS / "assets" / "images"

B1 = "bloco-1-definicao-tecnologica-e-trm.md"
B2 = "bloco-2-plataforma-arquitetural.md"
B3 = "bloco-3-seguranca-fim-a-fim.md"
B4 = "bloco-4-adr-de-plataforma.md"

BLOCKS = {
    B1: (("modulo-5-bloco-ao-componente.svg", "modulo-5-trm-cinco-colunas-v3.svg"),
         17, ("2.7.2", "7.1", "7.4")),
    B2: (("modulo-5-pilares-zona-de-pouso.svg",), 18, ("7.5",)),
    B3: (("modulo-5-fronteira-de-confianca-stride.svg",
          "modulo-5-grade-de-permissoes.svg"), 19, ("2.9", "4.6.7", "7.7")),
    B4: (("modulo-5-tipos-de-lacuna.svg",), 20, ("7.8", "7.9")),
}

CRITERIA = ("aderência ao requisito", "maturidade", "suporte",
            "custo total de propriedade", "competência", "portabilidade")

STRIDE = ("falsificação de identidade", "adulteração", "repúdio",
          "divulgação de informação", "negação de serviço", "elevação de privilégio")

GAP_TYPES = ("nova", "substituição", "modificação", "remoção")

FORBIDDEN_IN_VISUALS = ("ACME", "COBOL", "CICS", "Oracle", "matrícula", "Matrícula")
CONSTRUCTION_VERBS = ("Desenhe", "Monte", "Construa", "Modele", "Mapeie")
FIRST_PERSON = ("Em sala", "percorremos", "ficam para leitura posterior")

# Fontes complementares que a Task 2 confere na origem. Fonte nao conferida sai daqui.
VERIFIED_SOURCES = (
    "Lei nº 13.709",
    "Shostack, A.",
    "OWASP",
    "CWE",
    "ISO/IEC 27001",
    "AWS Control Tower",
    "Azure landing zone",
)

GLOSSARY_HEADINGS = (
    "Modelo técnico de referência", "Definição tecnológica da solução",
    "Lacuna de provisão", "Zona de pouso", "Infraestrutura como código",
    "Grade de permissões", "Menor privilégio", "Fronteira de confiança",
    "STRIDE", "Autoridade de design de segurança", "Dado pessoal sensível",
)


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


def item(text: str, number: int) -> str:
    """Devolve o trecho do item indicado, ate o proximo cabecalho de nivel 2 ou 3."""
    match = re.search(rf"(?m)^### Item {number}: .*$", text)
    if match is None:
        return ""
    rest = text[match.end():]
    end = re.search(r"(?m)^#{2,3} ", rest)
    return rest[: end.start()] if end else rest


def without_sources(text: str) -> str:
    fontes = re.search(r"^## Fontes( da aula)?\s*$", text, re.MULTILINE)
    return text[: fontes.start()] if fontes else text


def concept(text: str) -> str:
    """Trecho entre Antes de comecar e Uso pelo arquiteto."""
    start = re.search(r"^## Antes de começar\s*$", text, re.MULTILINE)
    end = re.search(r"^## Uso pelo arquiteto\s*$", text, re.MULTILINE)
    return text[start.end(): end.start()] if start and end else ""


class ModuleFiveStructureTest(unittest.TestCase):
    def test_all_pages_exist_and_are_in_nav(self):
        config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        nav = config[config.index("\nnav:"):]
        for name in ("index.md", *BLOCKS, "sintese.md"):
            with self.subTest(page=name):
                self.assertTrue((MODULE / name).is_file())
                self.assertIn(f"modulo-5-frameworks-e-tecnologias/{name}", nav)

    def test_nav_orders_blocks_one_to_four(self):
        config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        nav = config[config.index("\nnav:"):]
        positions = [nav.index(f"modulo-5-frameworks-e-tecnologias/{name}") for name in BLOCKS]
        self.assertEqual(positions, sorted(positions))

    def test_each_block_has_its_numbered_exercise(self):
        for name, (_, number, _) in BLOCKS.items():
            with self.subTest(page=name):
                self.assertRegex(read(name), rf"(?m)^## Exercício {number}\s*$")

    def test_each_block_places_its_visuals(self):
        for name, (images, _, _) in BLOCKS.items():
            for image in images:
                with self.subTest(page=name, image=image):
                    self.assertRegex(
                        read(name),
                        rf"!\[[^\]]{{40,}}\]\(\.\./assets/images/{re.escape(image)}\)"
                        r"\{ \.module-diagram \}",
                    )

    def test_visuals_are_accessible_legible_and_generic(self):
        svgs = sorted(IMAGES.glob("modulo-5-*.svg"))
        self.assertEqual(6, len(svgs))
        for svg_path in svgs:
            svg = svg_path.read_text(encoding="utf-8")
            sizes = [int(size) for size in re.findall(r"font-size:(\d+)px", svg)]
            with self.subTest(image=svg_path.name):
                self.assertRegex(svg, r"<title[^>]*>[^<]{5,}</title>")
                self.assertRegex(svg, r"<desc[^>]*>[^<]{20,}</desc>")
                self.assertTrue(sizes)
                self.assertGreaterEqual(min(sizes), 16)
                for term in FORBIDDEN_IN_VISUALS:
                    self.assertNotIn(term, svg)

    def test_every_module_5_visual_is_used_by_a_page(self):
        pages = "".join(page.read_text(encoding="utf-8") for page in MODULE.glob("*.md"))
        for svg_path in sorted(IMAGES.glob("modulo-5-*.svg")):
            with self.subTest(image=svg_path.name):
                self.assertIn(svg_path.name, pages)

    def test_each_block_cites_lovatt_with_its_sections(self):
        for name, (_, _, sections) in BLOCKS.items():
            fontes = section(read(name), "Fontes")
            with self.subTest(page=name):
                self.assertIn("Lovatt, M. (2021)", fontes)
            for number in sections:
                with self.subTest(page=name, section=number):
                    self.assertIn(number, fontes)

    def test_pages_do_not_use_first_person_or_the_old_framing(self):
        for page in MODULE.glob("*.md"):
            text = page.read_text(encoding="utf-8")
            for phrase in (*FIRST_PERSON, "já estão publicados", "publicados antes da aula"):
                with self.subTest(page=page.name, phrase=phrase):
                    self.assertNotIn(phrase, text)

    def test_seven_factors_survive_only_as_the_block_1_correspondence(self):
        self.assertEqual(1, read(B1).count("sete fatores"))
        for name in (B2, B3, B4, "index.md", "sintese.md"):
            with self.subTest(page=name):
                text = read(name)
                self.assertNotIn("sete fatores", text)
                self.assertNotIn("fatores de adaptação", text)

    def test_case_names_are_in_portuguese(self):
        for name in (B1, B3):
            with self.subTest(page=name):
                self.assertIn("Hospital ACME", read(name))
        for page in MODULE.glob("*.md"):
            with self.subTest(page=page.name):
                self.assertNotIn("Fallowdale", without_sources(page.read_text(encoding="utf-8")))


class BlockOneTest(unittest.TestCase):
    def test_block_1_explains_the_mapping_and_the_trm(self):
        body = concept(read(B1)).lower()
        for term in ("definição tecnológica", "requisito de serviço", "nível de serviço",
                     "lacuna", "modelo técnico de referência", "blueprint",
                     "exemplos aprovados", "exemplos não aprovados", "tecnologias descontinuadas",
                     "verde", "âmbar", "vermelho", "terraform", "dependência de fornecedor"):
            with self.subTest(term=term):
                self.assertIn(term, body)

    def test_block_1_presents_the_six_criteria(self):
        body = concept(read(B1)).lower()
        for criterion in CRITERIA:
            with self.subTest(criterion=criterion):
                self.assertIn(criterion, body)
        self.assertIn("matriz de avaliação", body)

    def test_block_1_links_back_to_earlier_lessons(self):
        body = concept(read(B1))
        self.assertIn("../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md", body)
        self.assertIn("../modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md", body)

    def test_exercise_17_consumes_exercise_16_and_keeps_the_baseline_facts(self):
        ex = section(read(B1), "Exercício 17")
        self.assertIn("bloco-4-arquitetura-de-infraestrutura.md#exercicio-16", ex)
        for fact in ("JSF 1.2", "Oracle 12c", "2.300", "LDAP", "61.400", "OpenID Connect"):
            with self.subTest(fact=fact):
                self.assertIn(fact, ex)
        self.assertNotIn("SOAP", ex)

    def test_exercise_17_items_do_not_hand_over_the_answer(self):
        item2 = item(section(read(B1), "Exercício 17"), 2)
        rows = [line for line in item2.splitlines() if line.startswith("|")]
        self.assertTrue(rows)
        for row in rows:
            for word in ("verde", "âmbar", "vermelho"):
                with self.subTest(row=row[:40], word=word):
                    self.assertNotIn(word, row.lower())


class BlockTwoTest(unittest.TestCase):
    def test_block_2_keeps_the_definition_and_orders_style_before_platform(self):
        body = concept(read(B2)).lower()
        for term in ("plataforma arquitetural", "instanciação de estilos",
                     "composição multidimensional", "adaptação ao contexto"):
            with self.subTest(term=term):
                self.assertIn(term, body)

    def test_block_2_is_trimmed_to_three_or_four_platform_examples(self):
        count = len(re.findall(r"(?m)^#### Plataforma", read(B2)))
        self.assertGreaterEqual(count, 3)
        self.assertLessEqual(count, 4)

    def test_block_2_describes_the_landing_zone(self):
        body = concept(read(B2)).lower()
        for term in ("zona de pouso", "conta", "hub-spoke", "identidade centralizada",
                     "políticas", "monitoramento", "infraestrutura como código",
                     "etiqueta", "opentelemetry"):
            with self.subTest(term=term):
                self.assertIn(term, body)
        for tag in ("projeto", "ambiente", "time", "centro de custo"):
            with self.subTest(tag=tag):
                self.assertIn(tag, body)

    def test_block_2_uses_the_six_criteria_by_link_and_defers_to_aula_4(self):
        body = concept(read(B2))
        self.assertIn(B1, body)
        self.assertIn("seis critérios", body)
        self.assertIn("../modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md", body)

    def test_exercise_18_uses_criteria_and_has_the_landing_zone_item(self):
        ex = section(read(B2), "Exercício 18")
        self.assertIn("Critério", ex)
        self.assertNotIn("| Fator |", ex)
        item3 = item(ex, 3)
        self.assertTrue(item3)
        for fact in ("R4", "R14", "etiqueta"):
            with self.subTest(fact=fact):
                self.assertIn(fact, item3)


class BlockThreeTest(unittest.TestCase):
    def test_block_3_covers_the_security_concepts(self):
        body = concept(read(B3)).lower()
        for term in ("segurança da informação", "cibersegurança", "arquitetura de segurança",
                     "confidencialidade", "integridade", "disponibilidade",
                     "lei geral de proteção de dados", "dado pessoal sensível",
                     "base legal", "transferência internacional", "menor privilégio",
                     "grade de permissões", "fronteira de confiança", "stride",
                     "autoridade de design de segurança", "iso/iec 27001", "owasp", "cwe", "raci"):
            with self.subTest(term=term):
                self.assertIn(term, body)

    def test_block_3_names_the_six_stride_categories(self):
        body = concept(read(B3)).lower()
        for category in STRIDE:
            with self.subTest(category=category):
                self.assertIn(category, body)

    def test_block_3_links_controls_to_block_2_and_to_earlier_lessons(self):
        body = concept(read(B3))
        self.assertIn(B2, body)
        self.assertIn("../modulo-2-requisitos-e-partes-interessadas/bloco-2-qualidade-e-tipos-de-requisito.md", body)
        self.assertIn("../modulo-4-dominios-da-solucao/bloco-3-arquitetura-de-aplicacoes-e-integracao.md", body)

    def test_exercise_19_consumes_exercises_16_and_18_and_the_dossier(self):
        ex = section(read(B3), "Exercício 19")
        self.assertIn("bloco-4-arquitetura-de-infraestrutura.md#exercicio-16", ex)
        self.assertIn(f"{B2}#exercicio-18", ex)
        for fact in ("R9", "R14", "LGPD", "STRIDE"):
            with self.subTest(fact=fact):
                self.assertIn(fact, ex)
        for number in (1, 2, 3):
            with self.subTest(item=number):
                self.assertTrue(item(ex, number))

    def test_exercise_19_stride_artifact_does_not_name_the_category(self):
        item3 = item(section(read(B3), "Exercício 19"), 3)
        rows = [line for line in item3.splitlines() if line.startswith("| ")]
        self.assertTrue(rows)
        for row in rows:
            for category in STRIDE:
                with self.subTest(row=row[:40], category=category):
                    self.assertNotIn(category, row.lower())


class BlockFourTest(unittest.TestCase):
    def test_block_4_keeps_the_adr_content_and_links_the_criteria(self):
        body = concept(read(B4))
        self.assertIn(B1, body)
        self.assertIn(f"{B2}#exercicio-18", read(B4))
        self.assertIn("../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md", body)
        self.assertIn("dependência de fornecedor", body.lower())

    def test_block_4_classifies_infrastructure_service_gaps(self):
        body = concept(read(B4)).lower()
        for term in ("lacuna de provisão", "catálogo de infraestrutura", "validação",
                     *GAP_TYPES):
            with self.subTest(term=term):
                self.assertIn(term, body)
        self.assertIn("../modulo-6-lacunas-e-governanca/index.md", concept(read(B4)))

    def test_exercise_20_keeps_items_1_to_3_and_adds_item_4(self):
        ex = section(read(B4), "Exercício 20")
        for number in (1, 2, 3, 4):
            with self.subTest(item=number):
                self.assertTrue(item(ex, number))
        item4 = item(ex, 4)
        for fact in ("diretório corporativo", "extração noturna", "integração por arquivos"):
            with self.subTest(fact=fact):
                self.assertIn(fact, item4)
        for gap in GAP_TYPES:
            with self.subTest(gap=gap):
                rows = [l for l in item4.splitlines() if l.startswith("| ")]
                self.assertFalse(any(gap in row.lower() for row in rows[2:]))


class ExerciseRuleTest(unittest.TestCase):
    def test_exercises_do_not_ask_the_student_to_build_models(self):
        for name, (_, number, _) in BLOCKS.items():
            ex = section(read(name), f"Exercício {number}")
            for verb in CONSTRUCTION_VERBS:
                with self.subTest(page=name, verb=verb):
                    self.assertNotIn(verb, ex)

    def test_exercise_chain_links_are_present(self):
        self.assertIn(f"{B1}#exercicio-17", read(B2))
        self.assertIn(f"{B1}#exercicio-17", section(read(B4), "Exercício 20"))
        self.assertIn(f"{B3}#exercicio-19", section(read(B4), "Exercício 20"))


class CourseIntegrationTest(unittest.TestCase):
    def test_index_has_objectives_schedule_inputs_route_and_bridge(self):
        text = read("index.md")
        for heading in ("Objetivos de aprendizagem", "Grade de tempo",
                        "Entrada recebida da Aula 4", "Roteiro da aula",
                        "Preparação para a Aula 6"):
            with self.subTest(heading=heading):
                self.assertRegex(text, rf"(?m)^## {heading}\s*$")
        self.assertRegex(text, r"(?m)^\| 19h25–19h58 \| Bloco 1, .*\| 33 \|\s*$")
        self.assertNotRegex(text, r"(?m)^\| [\dh–]+ \| Bloco 0,")

    def test_synthesis_has_checklist_chain_self_assessment_and_sources(self):
        text = read("sintese.md")
        for heading in ("Checklist do que precisa permanecer", "Cadeia da definição tecnológica",
                        "Autoavaliação", "Fontes da aula"):
            with self.subTest(heading=heading):
                self.assertRegex(text, rf"(?m)^## {heading}\s*$")
        chain = section(text, "Cadeia da definição tecnológica")
        for number in (16, 17, 18, 19, 20):
            with self.subTest(exercise=number):
                self.assertIn(f"exercício {number}", chain.lower())

    def test_schedule_describes_the_four_blocks_of_class_5(self):
        text = (DOCS / "cronograma.md").read_text(encoding="utf-8")
        aula5 = re.search(r"### Aula 5.*?(?=### Aula 6)", text, re.DOTALL).group(0)
        for term in ("modelo técnico de referência", "zona de pouso", "Segurança fim a fim",
                     "lacunas na provisão"):
            with self.subTest(term=term):
                self.assertIn(term, aula5)

    def test_artifacts_page_lists_the_class_5_products(self):
        text = (DOCS / "caso-acme" / "artefatos.md").read_text(encoding="utf-8")
        for term in ("zona de pouso", "STRIDE", "lacunas de provisão classificadas"):
            with self.subTest(term=term):
                self.assertIn(term, text)

    def test_glossary_defines_the_new_terms(self):
        text = (DOCS / "referencia" / "glossario.md").read_text(encoding="utf-8")
        for heading in GLOSSARY_HEADINGS:
            with self.subTest(heading=heading):
                self.assertRegex(text, rf"(?m)^## {heading}\s*$")

    def test_bibliography_lists_the_verified_sources(self):
        text = (DOCS / "referencia" / "bibliografia.md").read_text(encoding="utf-8")
        for source in VERIFIED_SOURCES:
            with self.subTest(source=source):
                self.assertIn(source, text)


if __name__ == "__main__":
    unittest.main()
