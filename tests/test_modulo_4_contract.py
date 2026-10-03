"""Contrato de conteudo da Aula 4, que o validador generico nao cobre."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MODULE = DOCS / "modulo-4-dominios-da-solucao"
OLD_MODULE = DOCS / "modulo-4-protocolos-e-representacao"
IMAGES = DOCS / "assets" / "images"

B1 = "bloco-1-arquitetura-de-negocio.md"
B2 = "bloco-2-arquitetura-de-dados.md"
B3 = "bloco-3-arquitetura-de-aplicacoes-e-integracao.md"
B4 = "bloco-4-arquitetura-de-infraestrutura.md"

BLOCKS = {
    B1: ("modulo-4-modelos-de-negocio.svg", 13, ("2.3",)),
    B2: ("modulo-4-grade-dado-aplicacao.svg", 14, ("2.5",)),
    B3: ("modulo-4-servicos-e-contrato.svg", 15, ("2.6", "3.6.4", "4.3.1")),
    B4: ("modulo-4-solucao-como-grafo.svg", 16, ("2.7", "7.5")),
}

INTERFACE_ATTRIBUTES = (
    "Origem", "Destino", "Gatilho", "Itens trocados", "Sequência",
    "Pré e pós-condições",
)

FORBIDDEN_IN_VISUALS = ("ACME", "COBOL", "CICS", "matrícula", "Matrícula")
CONSTRUCTION_VERBS = ("Desenhe", "Monte", "Construa", "Modele", "Mapeie")


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


def without_sources(text: str) -> str:
    fontes = re.search(r"^## Fontes\s*$", text, re.MULTILINE)
    return text[: fontes.start()] if fontes else text


class ModuleFourStructureTest(unittest.TestCase):
    def test_old_folder_is_gone(self):
        self.assertFalse(OLD_MODULE.exists())

    def test_all_pages_exist_and_are_in_nav(self):
        nav = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        for name in ("index.md", *BLOCKS, "sintese.md"):
            with self.subTest(page=name):
                self.assertTrue((MODULE / name).is_file())
                self.assertIn(f"modulo-4-dominios-da-solucao/{name}", nav)

    def test_old_urls_redirect_to_the_new_folder(self):
        config = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        self.assertIn(
            "modulo-4-protocolos-e-representacao/index.md: "
            "modulo-4-dominios-da-solucao/index.md",
            config,
        )
        self.assertIn(
            "modulo-4-protocolos-e-representacao/bloco-4-representacao-de-modelos-e-c4.md: "
            f"modulo-4-dominios-da-solucao/{B3}",
            config,
        )
        self.assertNotRegex(config, r":\s*modulo-4-protocolos-e-representacao/")

    def test_each_block_has_its_numbered_exercise(self):
        for name, (_, number, _) in BLOCKS.items():
            with self.subTest(page=name):
                self.assertRegex(read(name), rf"(?m)^## Exercício {number}\s*$")

    def test_each_block_has_an_accessible_local_visual(self):
        for name, (image, _, _) in BLOCKS.items():
            with self.subTest(page=name):
                self.assertRegex(
                    read(name),
                    rf"!\[[^\]]{{40,}}\]\(\.\./assets/images/{re.escape(image)}\)"
                    r"\{ \.module-diagram \}",
                )
                svg = (IMAGES / image).read_text(encoding="utf-8")
                self.assertRegex(svg, r"<title[^>]*>[^<]{5,}</title>")
                self.assertRegex(svg, r"<desc[^>]*>[^<]{20,}</desc>")

    def test_visuals_do_not_carry_case_data_and_are_legible(self):
        for image, _, _ in BLOCKS.values():
            svg = (IMAGES / image).read_text(encoding="utf-8")
            sizes = [int(size) for size in re.findall(r"font-size:(\d+)px", svg)]
            with self.subTest(image=image):
                self.assertTrue(sizes)
                self.assertGreaterEqual(min(sizes), 16)
            for term in FORBIDDEN_IN_VISUALS:
                with self.subTest(image=image, term=term):
                    self.assertNotIn(term, svg)

    def test_each_block_cites_lovatt_with_its_sections(self):
        for name, (_, _, sections) in BLOCKS.items():
            fontes = section(read(name), "Fontes")
            with self.subTest(page=name):
                self.assertIn("Lovatt, M. (2021)", fontes)
            for number in sections:
                with self.subTest(page=name, section=number):
                    self.assertIn(number, fontes)

    def test_no_page_keeps_the_old_framing(self):
        for page in MODULE.glob("*.md"):
            text = page.read_text(encoding="utf-8")
            for phrase in ("estilo e plataforma", "fecha a aula", "abre a aula"):
                with self.subTest(page=page.name, phrase=phrase):
                    self.assertNotIn(phrase, text)

    def test_case_names_are_in_portuguese(self):
        for name in (B1, B2, B3):
            with self.subTest(page=name):
                self.assertIn("Hospital Vale do Pousio", read(name))
        for page in MODULE.glob("*.md"):
            with self.subTest(page=page.name):
                self.assertNotIn("Fallowdale", without_sources(page.read_text(encoding="utf-8")))


class ExerciseRuleTest(unittest.TestCase):
    def test_exercises_do_not_ask_the_student_to_build_models(self):
        for name, (_, number, _) in BLOCKS.items():
            ex = section(read(name), f"Exercício {number}")
            for verb in CONSTRUCTION_VERBS:
                with self.subTest(page=name, verb=verb):
                    self.assertNotIn(verb, ex)

    def test_exercise_13_consumes_scope_and_requirements(self):
        ex = section(read(B1), "Exercício 13")
        self.assertIn("bloco-4-partes-interessadas-e-pontos-de-vista.md#exercicio-8", ex)
        for code in ("R1", "R7", "R13"):
            with self.subTest(code=code):
                self.assertIn(code, ex)
        for label in ("estratégica", "operacional", "de apoio"):
            with self.subTest(label=label):
                self.assertIn(label, ex)

    def test_exercise_14_consumes_exercise_13(self):
        ex = section(read(B2), "Exercício 14")
        self.assertIn(f"{B1}#exercicio-13", ex)
        self.assertIn("2.300", ex)
        for entity in ("aluno", "matrícula", "nota", "lançamento financeiro", "turma"):
            with self.subTest(entity=entity):
                self.assertIn(entity, ex.lower())

    def test_exercise_15_consumes_exercise_14_and_reproduces_the_cost(self):
        ex = section(read(B3), "Exercício 15")
        self.assertIn(f"{B2}#exercicio-14", ex)
        for fact in ("38%", "05h10", "R7", "vermelho", "âmbar", "verde"):
            with self.subTest(fact=fact):
                self.assertIn(fact, ex)
        for attribute in INTERFACE_ATTRIBUTES:
            with self.subTest(attribute=attribute):
                self.assertIn(attribute, ex)

    def test_exercise_16_consumes_exercise_15(self):
        ex = section(read(B4), "Exercício 16")
        self.assertIn(f"{B3}#exercicio-15", ex)
        self.assertIn("tecnologia a definir na Aula 5", ex)


class ReviewFindingsTest(unittest.TestCase):
    """Achados da revisao final da branch, fixados para nao regredirem."""

    def test_exercise_13_value_stream_does_not_name_the_requirement(self):
        ex = section(read(B1), "Exercício 13")
        rows = re.findall(r"(?m)^\| [1-6]\. .*$", ex)
        stream = [row for row in rows if "Situação" not in row and "Responsável" not in row]
        self.assertTrue(stream)
        for row in stream:
            for code in ("R1", "R7", "R13"):
                with self.subTest(row=row[:40], code=code):
                    self.assertNotIn(code, row)

    def test_exercise_14_grid_does_not_invent_access_per_entity(self):
        ex = section(read(B2), "Exercício 14")
        self.assertNotIn("| Lê, por conector", ex)
        self.assertNotIn("| Lê e grava, por conector", ex)

    def test_exercises_14_and_15_consume_module_3_products(self):
        ex14 = section(read(B2), "Exercício 14")
        ex15 = section(read(B3), "Exercício 15")
        self.assertIn("../modulo-3-design-e-padroes/bloco-1-principios-de-design.md#exercicio-9", ex14)
        self.assertIn("../modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md#exercicio-11", ex15)

    def test_nfe_example_keeps_ws_i_out_of_the_protocols(self):
        text = read(B3)
        protocols = re.search(r"Os protocolos são.*?\.(?= [A-Z])", text)
        self.assertIsNotNone(protocols)
        self.assertNotIn("WS-I", protocols.group(0))

class BlockContentTest(unittest.TestCase):
    def test_block_1_presents_the_four_business_models(self):
        text = read(B1)
        for model in ("Mapa de capacidades", "Fluxo de valor",
                      "Decomposição funcional", "Modelo de processo"):
            with self.subTest(model=model):
                self.assertIn(model, text)
        self.assertIn("bloco-2-a-solucao-como-sistema.md", text)

    def test_block_2_covers_ownership_and_consistency(self):
        text = read(B2).lower()
        for term in ("dado, informação e metadado", "fonte de verdade",
                     "regime de consistência", "propriedade do dado"):
            with self.subTest(term=term):
                self.assertIn(term, text)

    def test_block_3_disambiguates_standard_and_lists_interface_attributes(self):
        text = read(B3)
        for term in ("padrão técnico", "*standard*", "*pattern*", "protocolo",
                     "especificação", "contrato de integração", "Diagrama de contexto"):
            with self.subTest(term=term):
                self.assertIn(term, text)
        concept = without_sources(text)
        for attribute in INTERFACE_ATTRIBUTES:
            with self.subTest(attribute=attribute):
                self.assertIn(attribute, concept)

    def test_block_4_treats_the_solution_as_a_graph_and_keeps_containers(self):
        text = read(B4)
        for term in ("grafo", "Diagrama de contêineres", "tecnologia a definir na Aula 5"):
            with self.subTest(term=term):
                self.assertIn(term, text)


class CourseIntegrationTest(unittest.TestCase):
    def test_schedule_moves_security_to_class_5(self):
        text = (DOCS / "cronograma.md").read_text(encoding="utf-8")
        aula4 = re.search(r"### Aula 4.*?(?=### Aula 5)", text, re.DOTALL).group(0)
        aula5 = re.search(r"### Aula 5.*?(?=### Aula 6)", text, re.DOTALL).group(0)
        self.assertNotIn("segurança", aula4.lower())
        for domain in ("negócio", "dados", "aplicações", "infraestrutura"):
            with self.subTest(domain=domain):
                self.assertIn(domain, aula4.lower())
        self.assertIn("Segurança fim a fim", aula5)
        self.assertIn("modelo técnico de referência", aula5)

    def test_module_5_index_lists_the_security_block(self):
        text = (DOCS / "modulo-5-frameworks-e-tecnologias" / "index.md").read_text(encoding="utf-8")
        self.assertIn("Segurança fim a fim", text)

    def test_module_3_prepares_for_the_domains(self):
        text = (DOCS / "modulo-3-design-e-padroes" / "index.md").read_text(encoding="utf-8")
        prep = section(text, "Preparação para a Aula 4")
        self.assertIn("domínios", prep)
        self.assertNotIn("protocolos", prep)

    def test_index_has_objectives_schedule_inputs_route_and_bridge(self):
        text = read("index.md")
        for heading in ("Objetivos de aprendizagem", "Grade de tempo",
                        "Entrada recebida das Aulas 2 e 3", "Roteiro da aula",
                        "Preparação para a Aula 5"):
            with self.subTest(heading=heading):
                self.assertRegex(text, rf"(?m)^## {heading}\s*$")

    def test_synthesis_has_checklist_chain_self_assessment_and_sources(self):
        text = read("sintese.md")
        for heading in ("Checklist do que precisa permanecer", "Cadeia dos domínios",
                        "Autoavaliação", "Fontes da aula"):
            with self.subTest(heading=heading):
                self.assertRegex(text, rf"(?m)^## {heading}\s*$")

    def test_glossary_defines_the_new_terms(self):
        text = (DOCS / "referencia" / "glossario.md").read_text(encoding="utf-8")
        for heading in ("Arquitetura de negócio", "Capacidade", "Fluxo de valor",
                        "Arquitetura de dados", "Propriedade do dado", "Fonte de verdade",
                        "Regime de consistência", "Arquitetura de aplicações",
                        "Padrão técnico", "Protocolo", "Especificação de interface",
                        "Contrato de integração", "Arquitetura de infraestrutura"):
            with self.subTest(heading=heading):
                self.assertRegex(text, rf"(?m)^## {heading}\s*$")

    def test_bibliography_lists_the_verified_sources(self):
        text = (DOCS / "referencia" / "bibliografia.md").read_text(encoding="utf-8")
        for source in ("Kleppmann, M.", "Dehghani, Z.", "RFC 9110", "OpenAPI", "AsyncAPI"):
            with self.subTest(source=source):
                self.assertIn(source, text)


if __name__ == "__main__":
    unittest.main()
