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

B0 = "bloco-0-espinha-dorsal-dos-dominios.md"

ROTEIRO = {
    B1: "Que capacidades, etapas do fluxo de valor e atividades a solução altera, segundo os modelos que a arquitetura de negócio já mantém?",
    B2: "Que entidades sustentam as capacidades afetadas, quem é o dono de cada uma, onde fica a fonte de verdade, com que regime cada cópia a reflete e que obrigações o dado carrega?",
    B3: "Que aplicações mudam, por quais interfaces trocam essas entidades, que contrato governa cada interface e onde passa a fronteira da solução?",
    B4: "Em que nó cada contêiner executa, com que modo, volume e latência cada relação opera e o que fica como exigência para a definição tecnológica?",
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
    fontes = re.search(r"^## Fontes( da aula)?\s*$", text, re.MULTILINE)
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
                self.assertIn("Hospital ACME", read(name))
        for page in MODULE.glob("*.md"):
            with self.subTest(page=page.name):
                self.assertNotIn("Fallowdale", without_sources(page.read_text(encoding="utf-8")))


class SelfContainedTextTest(unittest.TestCase):
    """Revisao de 03/10/2026: texto autocontido, autor so na referencia."""

    def test_block_bodies_do_not_narrate_the_textbook(self):
        for page in sorted(DOCS.glob("modulo-*/*.md")):
            body = without_sources(page.read_text(encoding="utf-8"))
            prose = "\n".join(line for line in body.splitlines()
                              if not line.startswith("*Figura"))
            with self.subTest(page=page.name):
                self.assertNotIn("Lovatt", prose)
                self.assertNotIn("livro-texto", prose)

    def test_cases_are_named_acme_and_drop_the_old_names(self):
        for page in sorted(DOCS.rglob("*.md")):
            if "superpowers" in page.parts:
                continue
            text = page.read_text(encoding="utf-8")
            with self.subTest(page=page.name):
                self.assertNotIn("Vale do Pousio", text)
                self.assertNotIn("produtora de vídeo", text)

    def test_archimate_is_presented_in_version_4(self):
        self.assertIn("ArchiMate 4", read(B1))

    def test_hospital_case_is_the_laboratory_change_without_letters(self):
        text = without_sources(read(B1))
        self.assertIn("laboratório", text)
        self.assertNotIn("carta", text)
        self.assertIn("modulo-4-b1-mapa-de-capacidades-afetadas.svg", text)


class DataArchitectureDepthTest(unittest.TestCase):
    """Revisao de 03/10/2026: arquitetura de dados com base no DMBOK."""

    def test_block_2_is_grounded_in_dmbok_and_lgpd(self):
        body = concept(read(B2))
        for term in ("DMBOK", "modelo de dados corporativo", "Dados mestres", "linhagem de dados",
                     "contrato de dados", "LGPD", "lakehouse", "medallion"):
            with self.subTest(term=term):
                self.assertIn(term.lower(), body.lower())

    def test_block_2_drops_the_introductory_sections(self):
        text = read(B2)
        for heading in ("### Dado, informação e metadado", "### Entidade, generalização e especialização"):
            with self.subTest(heading=heading):
                self.assertNotIn(heading, text)
        self.assertNotIn("ISO/IEC 2382", text)

    def test_exercise_14_asks_for_master_data_and_personal_data_decisions(self):
        ex = section(read(B2), "Exercício 14")
        for term in ("dado mestre", "LGPD", "R9", "R14", "ADR"):
            with self.subTest(term=term):
                self.assertIn(term, ex)


class BlockZeroTest(unittest.TestCase):
    """Bloco 0 de 03/10/2026: o trabalho do arquiteto nos quatro dominios."""

    def test_page_exists_and_is_in_nav(self):
        self.assertTrue((MODULE / B0).is_file())
        nav = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        self.assertIn(f"modulo-4-dominios-da-solucao/{B0}", nav)
        self.assertLess(nav.index(f"modulo-4-dominios-da-solucao/{B0}"),
                        nav.index(f"modulo-4-dominios-da-solucao/{B1}"))

    def test_page_is_conceptual_and_has_no_exercise(self):
        text = read(B0)
        self.assertNotRegex(text, r"(?m)^## Exerc[ií]cio")
        for term in ("ACME", "Hospital", "Clínica", "COBOL", "matrícula"):
            with self.subTest(term=term):
                self.assertNotIn(term, text)

    def test_page_covers_the_four_domains_and_the_three_columns(self):
        body = without_sources(read(B0)).lower()
        for term in ("negócio", "dados", "aplicações", "infraestrutura", "recebe", "decide", "entrega"):
            with self.subTest(term=term):
                self.assertIn(term, body)

    def test_page_shows_the_central_figure(self):
        self.assertRegex(
            read(B0),
            r"!\[[^\]]{40,}\]\(\.\./assets/images/modulo-4-b0-espinha-dorsal\.svg\)\{ \.module-diagram \}",
        )

    def test_page_lists_the_four_questions(self):
        uso = section(read(B0), "Uso pelo arquiteto")
        for name, question in ROTEIRO.items():
            with self.subTest(block=name):
                self.assertIn(question, uso)

    MAPAS = {B1: "negocio", B2: "dados", B3: "aplicacoes", B4: "infraestrutura"}

    def test_each_block_opens_with_its_own_map(self):
        for name, key in self.MAPAS.items():
            body = concept(read(name))
            with self.subTest(page=name):
                self.assertIn(B0, body)
                self.assertRegex(
                    body,
                    rf"!\[[^\]]{{40,}}\]\(\.\./assets/images/modulo-4-b0-mapa-{key}\.svg\)\{{ \.module-diagram \}}",
                )
                for other in set(self.MAPAS.values()) - {key}:
                    self.assertNotIn(f"modulo-4-b0-mapa-{other}.svg", body)

    def test_each_block_repeats_its_question_verbatim(self):
        for name, question in ROTEIRO.items():
            with self.subTest(page=name):
                self.assertIn(question, section(read(name), "Uso pelo arquiteto"))

    def test_block_3_hierarchy_points_back_to_block_0(self):
        text = read(B3)
        start = text.index("### Hierarquia de serviços")
        self.assertIn(B0, text[start:start + 1500])

    def test_synthesis_chain_points_to_block_0(self):
        self.assertIn(B0, section(read("sintese.md"), "Cadeia dos domínios"))

    def test_index_schedule_and_route_include_block_0(self):
        text = read("index.md")
        self.assertRegex(text, r"(?m)^\| 19h25–19h35 \| Bloco 0, os quatro domínios numa só solução \| 10 \|\s*$")
        self.assertIn(B0, section(text, "Roteiro da aula"))

    def test_schedule_page_lists_block_0(self):
        text = (DOCS / "cronograma.md").read_text(encoding="utf-8")
        aula4 = re.search(r"### Aula 4.*?(?=### Aula 5)", text, re.DOTALL).group(0)
        self.assertRegex(aula4, r"(?m)^\| 0 \| ")

    def test_glossary_defines_the_backbone(self):
        text = (DOCS / "referencia" / "glossario.md").read_text(encoding="utf-8")
        self.assertRegex(text, r"(?m)^## Espinha dorsal dos domínios\s*$")

class BlockZeroReviewTest(unittest.TestCase):
    """Achados da revisao final da branch do bloco 0."""

    def test_execution_layer_is_a_requirement_not_a_choice(self):
        svg = (IMAGES / "modulo-4-b0-espinha-dorsal.svg").read_text(encoding="utf-8")
        self.assertIn("compatível", svg)
        self.assertIn("camada de execução compatível", read(B0))
        opening = concept(read(B4))[:1500]
        self.assertIn("camada de execução compatível", opening)

    def test_course_pages_mention_the_block_0_opening(self):
        cronograma = (DOCS / "cronograma.md").read_text(encoding="utf-8").split("\n\n")[1]
        self.assertIn("bloco 0", cronograma)
        home = (DOCS / "index.md").read_text(encoding="utf-8")
        self.assertIn("bloco 0", home)

    def test_figure_questions_are_declared_short_forms(self):
        self.assertIn("forma curta da pergunta", read(B0))

    def test_table_third_column_matches_the_figure(self):
        text = read(B0)
        self.assertIn("| Domínio | Recebe, e de quem | Decide | Entrega |", text)
        row = next(l for l in text.splitlines() if l.startswith("| Negócio |"))
        self.assertIn("Capacidades, etapas e atividades afetadas", row)

    def test_side_axis_boxes_fit_their_labels(self):
        svg = (IMAGES / "modulo-4-b0-espinha-dorsal.svg").read_text(encoding="utf-8")
        widths = [int(w) for w in re.findall(r'<rect x="\d+" y="\d+" width="(\d+)" height="90"', svg)]
        self.assertEqual(4, len(widths))
        self.assertGreaterEqual(min(widths), 160)


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


def concept(text: str) -> str:
    """Trecho entre Antes de comecar e Uso pelo arquiteto."""
    start = re.search(r"^## Antes de começar\s*$", text, re.MULTILINE)
    end = re.search(r"^## Uso pelo arquiteto\s*$", text, re.MULTILINE)
    return text[start.end(): end.start()] if start and end else ""


class RevisionFiguresAndTechnologyTest(unittest.TestCase):
    """Revisao de 03/10/2026: mais figuras, tecnologia e C4 como notacao."""

    MIN_VISUALS = {B1: 3, B2: 4, B3: 5, B4: 3}

    TECHNOLOGY = {
        B1: ("BPMN", "ArchiMate"),
        B2: ("PostgreSQL", "Redis", "Debezium", "Kafka", "data warehouse"),
        B3: ("gRPC", "GraphQL", "RabbitMQ", "JSON Schema", "Idempotency-Key", "gateway de API"),
        B4: ("Kubernetes", "zonas de disponibilidade", "balanceador de carga", "máquina virtual"),
    }

    def test_each_block_explains_concepts_with_several_visuals(self):
        for name, minimum in self.MIN_VISUALS.items():
            body = concept(read(name))
            count = body.count("{ .module-diagram }") + body.count("```mermaid")
            with self.subTest(page=name):
                self.assertGreaterEqual(count, minimum)

    def test_blocks_ground_concepts_in_technology(self):
        for name, terms in self.TECHNOLOGY.items():
            body = concept(read(name))
            for term in terms:
                with self.subTest(page=name, term=term):
                    self.assertIn(term, body)

    def test_c4_is_explained_once_in_block_3(self):
        b3, b4 = read(B3), read(B4)
        for heading in ("### Modelo C4", "### Diagrama de contexto", "### Diagrama de contêineres"):
            with self.subTest(heading=heading):
                self.assertIn(heading, b3)
                self.assertNotIn(heading, b4)
        self.assertNotIn("| Contexto | O que o sistema faz?", b4)
        self.assertIn("diagrama de implantação", b4.lower())

    def test_all_module_4_visuals_are_accessible_legible_and_generic(self):
        for svg_path in sorted(IMAGES.glob("modulo-4-*.svg")):
            svg = svg_path.read_text(encoding="utf-8")
            sizes = [int(size) for size in re.findall(r"font-size:(\d+)px", svg)]
            with self.subTest(image=svg_path.name):
                self.assertRegex(svg, r"<title[^>]*>[^<]{5,}</title>")
                self.assertRegex(svg, r"<desc[^>]*>[^<]{20,}</desc>")
                self.assertTrue(sizes)
                self.assertGreaterEqual(min(sizes), 16)
                for term in FORBIDDEN_IN_VISUALS:
                    self.assertNotIn(term, svg)

    def test_every_module_4_visual_is_used_by_a_page(self):
        pages = "".join(page.read_text(encoding="utf-8") for page in MODULE.glob("*.md"))
        for svg_path in sorted(IMAGES.glob("modulo-4-*.svg")):
            with self.subTest(image=svg_path.name):
                self.assertIn(svg_path.name, pages)

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
        for term in ("grafo", "diagrama de contêineres", "tecnologia a definir na Aula 5"):
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
