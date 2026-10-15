# Aula 5, frameworks e tecnologias

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produzir a Aula 5 do site, com os blocos 1 e 3 novos, os blocos 2 e 4 revisados, índice, síntese, seis visuais novos, a cadeia de exercícios 17 a 20 e as atualizações de cronograma, glossário, bibliografia e dossiê.

**Architecture:** Um teste novo, `tests/test_modulo_5_contract.py`, fixa antes da escrita os contratos que o validador genérico não cobre, no modelo de `tests/test_modulo_4_contract.py`. Os blocos 1 e 3 entram como páginas novas na pasta existente `docs/modulo-5-frameworks-e-tecnologias/`, e os blocos 2 e 4 são editados no lugar, sem renomear arquivo, para que as âncoras `#exercicio-18` e `#exercicio-20` e os redirecionamentos atuais continuem válidos. Os visuais são SVG escritos à mão no padrão de `docs/assets/images/modulo-4-b4-camadas-de-execucao.svg`.

**Tech Stack:** Python 3, unittest, MkDocs Material em `.venv` com o plugin `redirects`, SVG estático, Mermaid nos enunciados, Markdown com `attr_list` e `md_in_html`, Playwright para a conferência visual.

**Spec:** `docs/superpowers/specs/2026-10-15-modulo-5-frameworks-e-tecnologias-design.md`

## Global Constraints

- Anatomia de página de bloco, na ordem: título funcional, linha de enquadramento, `## Antes de começar`, seção de conceito com título livre, `## Uso pelo arquiteto`, `## Exercício N`, `## Fontes`.
- Exercícios numerados 17, 18, 19 e 20, um por bloco, na ordem dos blocos, cada um dividido em itens com subtítulo `### Item N: assunto`, cada item com o próprio artefato seguido das suas perguntas, e ao menos um visual em Mermaid no enunciado.
- Regra dos exercícios: o enunciado fornece o artefato já montado e o aluno classifica, marca, rotula, corrige, associa ou responde perguntas curtas. Nenhum enunciado usa os verbos desenhe, monte, construa, modele ou mapeie como tarefa do aluno. O artefato fornecido não traz a resposta.
- O enunciado do exercício não repete a frase "Este exercício é realizado fora do horário de aula". A regra fica só no índice da aula.
- Lovatt (2021) é a base de cada bloco e aparece apenas em `## Fontes` e na legenda de figura. O corpo do texto expõe o conceito de forma direta e impessoal, sem "Lovatt diz" nem "livro-texto". O texto integral está em `/Volumes/Marco-Dev/dev/projeto-arquitetura-solucao/docs/superpowers/plans/livro-lovatt.md`.
- O aluno não lê o livro. Conceito já visto em outra aula é ligado por link ao bloco de origem, em frase curta, sem repetir a definição.
- Termos do glossário do curso: modelo técnico de referência, definição tecnológica da solução, lacuna de provisão, zona de pouso, infraestrutura como código, menor privilégio, fronteira de confiança, autoridade de design de segurança, dependência de fornecedor.
- Organizações fictícias se chamam ACME com qualificador de setor. O exemplo conceitual dos blocos 1 e 3 é o Hospital ACME, adaptado do caso do livro-texto, com a origem declarada apenas em `## Fontes`. A palavra Fallowdale só aparece em `## Fontes`.
- Os critérios de seleção são seis: aderência ao requisito, maturidade, suporte, custo total de propriedade, competência da equipe e portabilidade. A expressão "sete fatores" aparece somente no bloco 1, na frase de correspondência. Os blocos 2 e 4 não mantêm lista própria de fatores.
- Segurança fim a fim é tema do bloco 3. Região, zonas de disponibilidade e camadas de execução entram apenas por link ao bloco 4 da Aula 4. IA no processo de arquitetura, roteiro e governança ficam fora da aula.
- Zero ponto e vírgula em texto corrido, no máximo um travessão por parágrafo fora de `## Fontes`, nenhum título abrindo com "Por que", nenhum título com subtítulo após travessão, nenhuma ocorrência da palavra "prosa".
- Negrito entre três e cinco ocorrências por página, só na seção de conceito, no primeiro uso do termo.
- Registro sóbrio e impessoal, português brasileiro com acentuação completa, sem metáfora, sem frase de efeito no fim de parágrafo, média de pelo menos 14 palavras por frase, sem primeira pessoa e sem "em sala" no corpo.
- Fonte complementar entra no texto e na bibliografia somente depois de conferida na origem. Fonte não conferida sai do texto, da bibliografia e do teste.
- Visuais conceituais com nome `modulo-5-*.svg`, `<title>` e `<desc>` preenchidos, fonte interna de pelo menos 16 px declarada como `font-size:NNpx`, marcados com `{ .module-diagram }`, sem os termos "ACME", "COBOL", "CICS", "Oracle" ou "matrícula". Figura de exercício com dado da ACME é Mermaid no enunciado, ou SVG com prefixo `acme-`.
- Figura com conteúdo alterado recebe nome de arquivo novo, porque o GitHub Pages serve imagem com cache de 600 s.
- Nenhum gabarito no site. Gabaritos vão para `~/pka/projects/aulas/PRJ-aulas-iec-projeto-e-inovacao-em-arquitetura-de-solucoes.md`, seção `## Gabaritos dos exercícios da Aula 5`.
- Cada commit termina com a linha `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`. O trabalho ocorre na branch `modulo-5-frameworks-e-tecnologias`.

## Review Focus

- Divergência entre o EAD e o site quanto ao diretório corporativo: o roteiro M-U3V2 diz SOAP, e `docs/caso-acme/linha-de-base.md:127` diz LDAP, síncrono, 10 s. O site prevalece. Teste: o exercício 17 contém "LDAP" e não contém "SOAP".
- Âncoras antigas dos exercícios 18 e 20: o bloco 4 do site e o diagrama do exercício 20 apontam para `bloco-2-plataforma-arquitetural.md#exercicio-18`, e o enunciado do exercício 19 e o ADR apontam para os exercícios 16 a 18. Teste: os quatro links cruzados do módulo existem e as âncoras resolvem, o que o validador de links relativos também confere.
- Lista de fatores antiga reaparecendo nos blocos 2 e 4 depois da unificação. Teste: "sete fatores" só no bloco 1, e a expressão "fatores de adaptação" ausente dos blocos 2 e 4.
- Exercício que entrega a resposta junto com o artefato, em especial a classificação verde, âmbar e vermelho do item 2 do exercício 17 e a categoria STRIDE do item 3 do exercício 19. Teste: nenhuma linha de tabela de artefato desses itens contém as palavras de resposta, e o teste de verbos de construção vale para os quatro exercícios.
- Dado de caso dentro de SVG conceitual, que o teste do módulo 3 e do módulo 4 já proíbe. Teste: nenhum `modulo-5-*.svg` contém "ACME", "COBOL", "CICS", "Oracle" ou "matrícula".
- Fonte complementar citada sem conferência (artigos da LGPD, STRIDE, estruturas de zona de pouso). Teste: a bibliografia contém cada fonte de `VERIFIED_SOURCES`, e a Task 2 só mantém na lista as fontes conferidas.
- Texto do bloco 2 publicado em primeira pessoa ("percorremos", "em sala"). Teste: nenhuma página do módulo contém essas expressões.

---

### Task 1: Contrato de teste, esqueletos e navegação

**Files:**
- Create: `tests/test_modulo_5_contract.py`
- Create: esqueletos de `docs/modulo-5-frameworks-e-tecnologias/bloco-1-definicao-tecnologica-e-trm.md`, `bloco-3-seguranca-fim-a-fim.md` e `sintese.md`
- Modify: `mkdocs.yml` (navegação da Aula 5)

**Interfaces:**
- Produces: nomes de arquivo, de imagem e de âncora usados sem variação pelas tarefas seguintes:
  - `bloco-1-definicao-tecnologica-e-trm.md`, imagens `modulo-5-bloco-ao-componente.svg` e `modulo-5-trm-cinco-colunas.svg`, âncora `#exercicio-17`
  - `bloco-2-plataforma-arquitetural.md`, imagem `modulo-5-pilares-zona-de-pouso.svg`, âncora `#exercicio-18`
  - `bloco-3-seguranca-fim-a-fim.md`, imagens `modulo-5-fronteira-de-confianca-stride.svg` e `modulo-5-grade-de-permissoes.svg`, âncora `#exercicio-19`
  - `bloco-4-adr-de-plataforma.md`, imagem `modulo-5-tipos-de-lacuna.svg`, âncora `#exercicio-20`
  - constante `VERIFIED_SOURCES` em `tests/test_modulo_5_contract.py`, editada pela Task 2

- [ ] **Step 1: Criar a branch de trabalho**

```bash
git checkout modulo-5-frameworks-e-tecnologias
git status --short
```

Expected: branch `modulo-5-frameworks-e-tecnologias`, árvore limpa (o spec já está commitado no `23e4ea8`).

- [ ] **Step 2: Escrever o teste de contrato**

```python
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
    B1: (("modulo-5-bloco-ao-componente.svg", "modulo-5-trm-cinco-colunas.svg"),
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
    "Azure landing zones",
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
        nav = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        for name in ("index.md", *BLOCKS, "sintese.md"):
            with self.subTest(page=name):
                self.assertTrue((MODULE / name).is_file())
                self.assertIn(f"modulo-5-frameworks-e-tecnologias/{name}", nav)

    def test_nav_orders_blocks_one_to_four(self):
        nav = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
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
        for fact in ("diretório corporativo", "extração noturna", "mensageria"):
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
```

- [ ] **Step 3: Rodar o teste e confirmar a falha**

Run: `.venv/bin/python -m unittest tests.test_modulo_5_contract -v 2>&1 | tail -25`
Expected: FAIL em quase todos os testes, porque os blocos 1 e 3, a síntese e os visuais ainda não existem.

- [ ] **Step 4: Criar os esqueletos**

```bash
printf '# Definição tecnológica e modelo técnico de referência\n' > docs/modulo-5-frameworks-e-tecnologias/bloco-1-definicao-tecnologica-e-trm.md
printf '# Segurança fim a fim\n' > docs/modulo-5-frameworks-e-tecnologias/bloco-3-seguranca-fim-a-fim.md
printf '# Síntese da Aula 5\n' > docs/modulo-5-frameworks-e-tecnologias/sintese.md
```

- [ ] **Step 5: Atualizar a navegação**

Em `mkdocs.yml`, substituir o item da Aula 5 por:

```yaml
  - "Aula 5, frameworks e tecnologias":
      - Visão geral: modulo-5-frameworks-e-tecnologias/index.md
      - "Bloco 1: definição tecnológica e modelo técnico de referência": modulo-5-frameworks-e-tecnologias/bloco-1-definicao-tecnologica-e-trm.md
      - "Bloco 2: plataforma arquitetural": modulo-5-frameworks-e-tecnologias/bloco-2-plataforma-arquitetural.md
      - "Bloco 3: segurança fim a fim": modulo-5-frameworks-e-tecnologias/bloco-3-seguranca-fim-a-fim.md
      - "Bloco 4: ADR de plataforma e lacunas": modulo-5-frameworks-e-tecnologias/bloco-4-adr-de-plataforma.md
      - Síntese: modulo-5-frameworks-e-tecnologias/sintese.md
```

- [ ] **Step 6: Rodar os testes estruturais**

Run: `.venv/bin/python -m unittest tests.test_modulo_5_contract.ModuleFiveStructureTest.test_all_pages_exist_and_are_in_nav tests.test_modulo_5_contract.ModuleFiveStructureTest.test_nav_orders_blocks_one_to_four -v`
Expected: PASS nos dois. O restante da suíte `tests.test_modulo_5_contract` continua em FAIL até as tarefas seguintes.

- [ ] **Step 7: Rodar a suíte antiga para confirmar que nada regrediu**

Run: `.venv/bin/python -m unittest tests.test_content_contract tests.test_exercicios_fora_da_sala tests.test_modulo_3_contract tests.test_modulo_4_contract 2>&1 | tail -5`
Expected: `OK`, porque os esqueletos não são índices e portanto `test_module_indexes_state_the_rule` não os examina.

- [ ] **Step 8: Commit**

```bash
git add tests/test_modulo_5_contract.py docs/modulo-5-frameworks-e-tecnologias/bloco-1-definicao-tecnologica-e-trm.md docs/modulo-5-frameworks-e-tecnologias/bloco-3-seguranca-fim-a-fim.md docs/modulo-5-frameworks-e-tecnologias/sintese.md mkdocs.yml
git commit -m "$(cat <<'EOF'
test(aula-5): fixa o contrato do modulo e a navegacao

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 2: Fontes complementares conferidas e bibliografia

**Files:**
- Modify: `docs/referencia/bibliografia.md`
- Modify: `tests/test_modulo_5_contract.py` (somente a constante `VERIFIED_SOURCES`)
- Create: `/private/tmp/claude-501/-Volumes-Marco-Dev-dev-projeto-arquitetura-software/f3dae16e-a375-4029-8ea2-1141849cd705/scratchpad/fontes-modulo-5.md` (notas de conferência, fora do repositório)

**Interfaces:**
- Consumes: `VERIFIED_SOURCES` da Task 1
- Produces: o arquivo de notas, com um bloco por fonte (URL aberta, trecho conferido, dado extraído, veredito `conferida` ou `não conferida`). As Tasks 3 a 6 leem esse arquivo antes de citar a fonte.

- [ ] **Step 1: Conferir cada fonte na origem**

Para cada fonte abaixo, abrir a página oficial com WebFetch (carregar a ferramenta com ToolSearch `select:WebFetch` se necessário) e registrar no arquivo de notas o URL, o trecho lido e o dado que o texto vai usar:

| Fonte | Onde conferir | Dado a extrair |
| --- | --- | --- |
| Lei nº 13.709/2018 (LGPD) | `https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm` | Artigo da definição de dado pessoal e de dado pessoal sensível (art. 5º, I e II), artigo das bases legais (art. 7º), artigo da transferência internacional (art. 33) |
| Shostack (2014), *Threat modeling: designing for security* | Página da editora Wiley ou do autor | Nome das seis categorias STRIDE e a propriedade de segurança que cada uma viola |
| OWASP Top 10 2021 | `https://owasp.org/Top10/` | Nomes e códigos de A01 (controle de acesso quebrado), A03 (injeção) e A09 (falhas de registro e monitoramento), e a diferença de numeração em relação ao que o livro-texto cita (A1 e A10) |
| CWE | `https://cwe.mitre.org/` | Descrição de uma linha do que a lista cataloga |
| ISO/IEC 27001 | `https://www.iso.org/standard/27001` | Edição vigente (2022) e a descrição do escopo, sem reproduzir a norma |
| AWS Control Tower e Landing Zone Accelerator | Documentação da AWS | Nome oficial e a função da estrutura |
| Azure landing zones | Documentação da Microsoft Learn | Nome oficial e a função da estrutura |

O veredito é `não conferida` quando a página não abre, quando ela deixa de confirmar o dado ou quando diverge do que o roteiro afirma, e a fonte com esse veredito sai da lista, do texto e da bibliografia.

- [ ] **Step 2: Acrescentar as entradas conferidas à bibliografia**

Acrescentar, em ordem alfabética e em APA 7ª edição, uma entrada por fonte conferida, com a data de acesso quando a fonte for página web. Ler `docs/referencia/bibliografia.md` antes e seguir o formato das entradas existentes.

- [ ] **Step 3: Ajustar `VERIFIED_SOURCES`**

Remover de `VERIFIED_SOURCES` em `tests/test_modulo_5_contract.py` cada fonte marcada `não conferida`, e ajustar a cadeia exata de texto quando a entrada da bibliografia usar grafia diferente (por exemplo "Lei nº 13.709" contra "Lei n. 13.709").

- [ ] **Step 4: Rodar os testes**

Run: `.venv/bin/python -m unittest tests.test_modulo_5_contract.CourseIntegrationTest.test_bibliography_lists_the_verified_sources -v && .venv/bin/python scripts/validate_content.py --module referencia`
Expected: PASS e zero violação.

- [ ] **Step 5: Relatar as fontes não conferidas**

Se alguma fonte ficou `não conferida`, listar no relatório da tarefa o conceito que dependia dela e a decisão tomada: sair do texto, ou virar convenção do curso, declarada como tal no glossário.

- [ ] **Step 6: Commit**

```bash
git add docs/referencia/bibliografia.md tests/test_modulo_5_contract.py
git commit -m "$(cat <<'EOF'
docs(aula-5): bibliografia com as fontes complementares conferidas

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 3: Bloco 1, definição tecnológica e modelo técnico de referência

**Files:**
- Modify: `docs/modulo-5-frameworks-e-tecnologias/bloco-1-definicao-tecnologica-e-trm.md`
- Create: `docs/assets/images/modulo-5-bloco-ao-componente.svg`
- Create: `docs/assets/images/modulo-5-trm-cinco-colunas.svg`
- Modify: `docs/referencia/glossario.md` (Modelo técnico de referência, Definição tecnológica da solução, Lacuna de provisão)

**Interfaces:**
- Consumes: Lovatt 2.7.2 e 7.1 a 7.4 (linhas 5300 a 5548 do texto integral), roteiro `~/pka/projects/aulas/iec-ead-2026-projeto-arquitetura-solucao/1-roteiros/T-U3V1-tecnologia-trm-selecao.md` e `M-U3V2-acme-trm-e-selecao.md`, notas da Task 2
- Produces: âncora `bloco-1-definicao-tecnologica-e-trm.md#exercicio-17`, os termos do glossário `modelo-tecnico-de-referencia`, `definicao-tecnologica-da-solucao` e `lacuna-de-provisao`, e a matriz dos seis critérios, que o bloco 2 e o bloco 4 ligam por link

- [ ] **Step 1: Rodar os testes do bloco e confirmar a falha**

Run: `.venv/bin/python -m unittest tests.test_modulo_5_contract.BlockOneTest -v 2>&1 | tail -15`
Expected: FAIL nos quatro testes.

- [ ] **Step 2: Acrescentar as entradas ao glossário**

Ler `docs/referencia/glossario.md` e inserir, em ordem alfabética, uma definição de um parágrafo para cada termo:

- `## Modelo técnico de referência`: catálogo que organiza, por camada arquitetural e categoria tecnológica, os padrões, os protocolos e os produtos aprovados, proibidos ou em avaliação, e que serve de lista de partida para a escolha de tecnologia de cada solução. Também conhecido pela sigla TRM.
- `## Definição tecnológica da solução`: avaliação da infraestrutura necessária para sustentar a arquitetura de solução proposta, que lista os serviços e componentes de infraestrutura, as áreas que mudam e o custo da mudança.
- `## Lacuna de provisão`: requisito de serviço de infraestrutura da solução que não encontra correspondente no catálogo de infraestrutura, e que pode exigir serviço novo, substituição, modificação ou remoção de um serviço existente.

- [ ] **Step 3: Escrever a página**

1. `# Definição tecnológica e modelo técnico de referência`
2. Linha de enquadramento: o bloco converte o desenho lógico da Aula 4 em escolha tecnológica, partindo dos contêineres com tecnologia a definir.
3. `## Antes de começar`: links para `modelo-tecnico-de-referencia`, `definicao-tecnologica-da-solucao`, `lacuna-de-provisao`, `bloco-de-construcao-da-solucao`, `dependencia-de-fornecedor` e `adr`.
4. Seção de conceito `## Do bloco de construção ao produto`:
   - Abertura: o bloco lógico descreve uma capacidade e ainda não tem produto. As três perguntas da definição tecnológica e o risco de escolher por familiaridade, com remissão ao [exercício 16](../modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md#exercicio-16), cujos contêineres levam o rótulo tecnologia a definir.
   - `### Restrições antes da comparação`: os sete tipos de restrição tecnológica (tecnologias aprovadas ou preferidas, padrões técnicos adotados, orçamento, prazo, contratos vigentes, geografia e competências da equipe), com remissão ao [bloco 3 da Aula 2](../modulo-2-requisitos-e-partes-interessadas/bloco-3-cenarios-linha-de-base-e-restricoes.md) para o conceito de restrição.
   - `### Do bloco ao serviço de infraestrutura`: a cadeia bloco de construção, requisito, requisito de serviço com nível declarado, serviço de infraestrutura e componente, mais a saída para lacuna. Figura 1, `modulo-5-bloco-ao-componente.svg`, com legenda `*Figura 1 — Do bloco de construção ao componente de infraestrutura, com a saída para lacuna de provisão. Fonte: material do curso, com base em Lovatt (2021, seção 7.4, figura 7.1).*`
   - `### O modelo técnico de referência`: a definição operacional, a diferença em relação ao blueprint lógico em quatro dimensões (pergunta central, conteúdo, organização, público), e a dependência assimétrica entre os dois. Ligação com o [bloco 3 da Aula 4](../modulo-4-dominios-da-solucao/bloco-3-arquitetura-de-aplicacoes-e-integracao.md) quanto ao padrão técnico.
   - `### Estrutura em cinco colunas`: tabela com camada e categoria, padrão ou protocolo, exemplos aprovados e exemplos não aprovados, com duas linhas de exemplo (exposição de serviços e identidade), e os três princípios (nativo de nuvem por padrão, API em primeiro lugar, segurança desde o projeto). Parágrafo sobre a classificação em verde, âmbar e vermelho e sobre a nota de uso, segundo a qual a adoção fora da lista aprovada exige [ADR](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md) com a justificativa do desvio. Figura 2, `modulo-5-trm-cinco-colunas.svg`, legenda `*Figura 2 — O modelo técnico de referência em cinco colunas e a classificação em verde, âmbar e vermelho. Fonte: material do curso, com base em Lovatt (2021, seção 7.3).*`
   - `### Seis critérios de seleção`: aderência ao requisito, maturidade, suporte, custo total de propriedade, competência da equipe e portabilidade, e a matriz de avaliação em que cada célula cita um dado verificável. Parágrafo sobre a restrição que elimina alternativas antes da comparação, com o exemplo da ferramenta de infraestrutura como código entre dois provedores (Terraform, AWS CDK e Bicep), e sobre a matriz que alimenta o campo de alternativas do ADR. Uma frase de correspondência com os sete fatores que a disciplina usava antes: requisitos funcionais, não funcionais e arquiteturais formam a aderência, o conhecimento do time é a competência, os custos formam o custo total, a confiabilidade do fornecedor é o suporte, a facilidade de uso sai da lista e a portabilidade entra na lista. A expressão "sete fatores" aparece uma única vez, nessa frase.
   - `### Dependência de fornecedor`: o critério de portabilidade leva ao [risco de dependência de fornecedor](../referencia/glossario.md#dependencia-de-fornecedor), tratado no [bloco 4](bloco-4-adr-de-plataforma.md), e o padrão aberto como mitigação.
   - `### O exemplo do Hospital ACME`: serviço de identidade com logon único e operação contínua, que aponta para o serviço de gestão de identidade e acesso do catálogo, e a lacuna quando o catálogo não tem o serviço. Sem número do caso da universidade.
5. `## Uso pelo arquiteto`: o arquiteto parte do TRM publicado, registra a eliminação por restrição antes de somar notas e leva a matriz ao ADR, e trata a lista aprovada como ponto de partida da escolha, que só se conclui no ADR.
6. `## Exercício 17`: contexto da ACME em duas frases, link para o [exercício 16](../modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md#exercicio-16), e três itens:
   - `### Item 1: Contêineres e categorias do modelo técnico`. Diagrama Mermaid `graph LR` com os contêineres do exercício 16 rotulados "tecnologia a definir na Aula 5" (aplicativo do aluno, serviço de matrícula, serviço de notas, núcleo existente, provedor de identidade externo). Tabela do recorte do TRM da ACME com as colunas Camada e categoria, Padrão ou protocolo, Exemplos aprovados, Exemplos não aprovados e as seis linhas copiadas de `gerar-decks-mesa-u3.py` (linhas 53 a 58): Identidade e acesso (OpenID Connect obrigatório, OAuth 2.0, SAML 2.0 / Keycloak, Auth0, Azure AD B2C / diretório por SOAP nos canais novos), Exposição de serviços (REST com OpenAPI 3.x / Spring Boot, FastAPI, NestJS / WCF, ASMX), Mensageria (tópico com retenção, contrato AsyncAPI / Kafka ou compatível, RabbitMQ / arquivo posicional sem versão), Infraestrutura como código (descrição declarativa e versionada / Terraform, AWS CDK, Bicep / scripts manuais), Observabilidade (OpenTelemetry / coletores compatíveis / registro sem correlação), Banco de serviço novo (SQL, banco por serviço, região nacional / PostgreSQL ou compatível / Oracle sem ADR de desvio). Perguntas: indicar a linha e o padrão obrigatório para o provedor de identidade, o serviço de matrícula, o banco do serviço de notas e a comunicação por evento do serviço de notas com o ambiente virtual de aprendizagem (R7) / indicar quais duas linhas se aplicam a todos os contêineres novos e uma frase de motivo.
   - `### Item 2: Tecnologias da linha de base`. Tabela com Tecnologia e Dado da linha de base, sem coluna de classificação: JSF 1.2 e EJB 2.0 (410.000 linhas de Java escritas entre 2007 e 2009, servidor de aplicação fora de suporte do fornecedor desde 2018, 220 telas) / Oracle 12c (740 tabelas, 11 TB, suporte estendido encerrado em 31/03/2022, licenciamento renovado em 30/06) / acesso direto ao banco (2.300 pontos fora do núcleo) / COBOL sob CICS (6 especialistas, 2 aposentadorias previstas para 2027, manutenção sob contrato exclusivo até 30/09/2027) / diretório corporativo (LDAP síncrono, 10 s, autentica todos os perfis) / arquivo posicional sem versão (incidente de 09/07/2026, 61.400 lançamentos de nota atrasados). Conferir cada número em `docs/caso-acme/linha-de-base.md` e `docs/caso-acme/dados-operacionais.md` antes de escrever. Perguntas: classificar cada tecnologia em verde, âmbar ou vermelho, com uma linha de justificativa, e indicar qual delas só pode permanecer sob plano de migração documentado.
   - `### Item 3: Matriz de seleção do provedor de identidade`. Mermaid ou tabela com três alternativas (instalado e operado pela equipe, serviço de terceiro, gerenciado da nuvem) nas linhas e os seis critérios nas colunas, com R8, R6 (5.800 sessões, p95 em até 4 s), R12 (99,9% na janela de matrícula, 43 minutos por mês) e R14 reproduzidos com origem, e as células em branco. Perguntas: preencher as células de aderência de cada alternativa com o dado do caso, indicar a alternativa que a restrição de padrão aberto elimina antes da comparação, e responder em uma linha qual dado do contrato do fornecedor falta para avaliar o R14 nos dois serviços externos.
7. `## Fontes`: Lovatt (2021) com as seções 2.7.2, 7.1, 7.3 e 7.4 e a nota de que o Hospital ACME é a versão portuguesa do caso Fallowdale Hospital, mais `**Material do curso.**` com glossário, dossiê da ACME e linha de base. Citar as orientações da disciplina somente se a Task 2 as conferiu como fonte publicável.

- [ ] **Step 4: Desenhar os dois visuais**

`modulo-5-bloco-ao-componente.svg` e `modulo-5-trm-cinco-colunas.svg`, `viewBox="0 0 1200 675"`, `role="img"`, `aria-labelledby="title desc"`, `<title>` e `<desc>` preenchidos, paleta `#F2F6FB`, `#16243A`, `#254DB8`, `#5FC0D1`, `#F2B84B`, texto com `style="font-size:NNpx"` de 16 px ou mais.

- Primeiro: cinco caixas encadeadas, bloco de construção, requisito, requisito de serviço com nível de serviço, serviço de infraestrutura e componente, com uma seta lateral do requisito de serviço para uma caixa tracejada "sem serviço no catálogo: lacuna".
- Segundo: cabeçalho de cinco colunas (camada e categoria, padrão ou protocolo, aprovados, não aprovados e a classificação) sobre uma legenda de três faixas, verde, âmbar e vermelho, com o significado de cada uma. Rótulos genéricos, sem produto da ACME.

- [ ] **Step 5: Rodar testes e validador**

Run: `.venv/bin/python -m unittest tests.test_modulo_5_contract.BlockOneTest tests.test_modulo_5_contract.ExerciseRuleTest.test_exercises_do_not_ask_the_student_to_build_models -v && .venv/bin/python scripts/validate_content.py --module modulo-5-frameworks-e-tecnologias`
Expected: os testes do bloco 1 em PASS, e nenhuma violação em `bloco-1-definicao-tecnologica-e-trm.md`. A verificação do exercício 17 em `ExerciseRuleTest` passa para o bloco 1, e as falhas dos blocos 2 a 4 persistem até as tarefas seguintes.

- [ ] **Step 6: Commit**

```bash
git add docs/modulo-5-frameworks-e-tecnologias/bloco-1-definicao-tecnologica-e-trm.md docs/assets/images/modulo-5-bloco-ao-componente.svg docs/assets/images/modulo-5-trm-cinco-colunas.svg docs/referencia/glossario.md
git commit -m "$(cat <<'EOF'
feat(aula-5): escreve o bloco de definicao tecnologica e modelo tecnico

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 4: Bloco 2, plataforma arquitetural (revisão)

**Files:**
- Modify: `docs/modulo-5-frameworks-e-tecnologias/bloco-2-plataforma-arquitetural.md`
- Create: `docs/assets/images/modulo-5-pilares-zona-de-pouso.svg`
- Modify: `docs/referencia/glossario.md` (Zona de pouso, Infraestrutura como código)

**Interfaces:**
- Consumes: `bloco-1-definicao-tecnologica-e-trm.md` da Task 3 (link para a matriz dos seis critérios), roteiros `T-U3V3-plataforma-zona-de-pouso.md` e `M-U3V4-acme-zona-de-pouso.md`, notas da Task 2
- Produces: âncora `bloco-2-plataforma-arquitetural.md#exercicio-18` mantida, termos do glossário `zona-de-pouso` e `infraestrutura-como-codigo`, e a estrutura de pilares que o bloco 3 liga por link

- [ ] **Step 1: Rodar os testes do bloco e confirmar a falha**

Run: `.venv/bin/python -m unittest tests.test_modulo_5_contract.BlockTwoTest -v 2>&1 | tail -15`
Expected: FAIL em pelo menos três dos quatro testes.

- [ ] **Step 2: Acrescentar as entradas ao glossário**

- `## Zona de pouso`: fundação do ambiente em nuvem, preparada antes da primeira carga de trabalho, que organiza contas, rede, identidade, políticas e monitoramento para que as soluções futuras herdem padrões de segurança, governança e operação.
- `## Infraestrutura como código`: descrição da infraestrutura em arquivos declarativos, versionados e revisados como o código da aplicação, de modo que o ambiente possa ser recriado a partir da descrição.

- [ ] **Step 3: Reescrever o enquadramento e o texto do bloco**

Ler o arquivo inteiro antes de editar. Manter a definição, as quatro características e a regra de que a decisão de estilo precede a de plataforma.

1. Linha de enquadramento: remover "dá sequência à aula" e abrir pela pergunta que o bloco responde, qual conjunto de tecnologias concretiza o estilo e sobre qual fundação executa.
2. Quarta característica, adaptação ao contexto: substituir a lista numerada dos sete fatores por uma frase que remete aos seis critérios, com link para `bloco-1-definicao-tecnologica-e-trm.md` na seção de seis critérios.
3. `### Exemplos de plataforma por estilo`: reescrever a abertura sem primeira pessoa, remover o parágrafo "Esta é a seção mais longa da aula... Em sala, percorremos...", manter só quatro exemplos, com seu desenho e com link ao estilo da Aula 3: Java EE e Jakarta EE (camadas), plataforma de microsserviços, plataforma orientada a eventos e plataforma web elástica em nuvem. Remover os demais cinco exemplos e as imagens que ficarem sem uso, conferindo antes que nenhuma outra página as referencia (`grep -r plataforma-dotnet docs`). Se a página de bloco 1 ou outra referenciar uma imagem removida, manter a imagem no disco e retirar só do bloco 2.
4. Nova seção `### Zona de pouso, a fundação da plataforma`, depois dos exemplos:
   - Definição e função, com a [infraestrutura em nuvem](../modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md) da Aula 4 como lugar onde a carga executa.
   - As estruturas oficiais dos provedores, nomeadas conforme a Task 2 (AWS Control Tower e Landing Zone Accelerator, Azure landing zones), e a observação de que o detalhe de configuração fica na documentação do provedor.
   - Os cinco pilares: contas ou assinaturas por ambiente, segmentação de rede em topologia hub-spoke, identidade centralizada, políticas de conformidade automatizadas e monitoramento com faturamento consolidado. Figura 1, `modulo-5-pilares-zona-de-pouso.svg`, legenda `*Figura 1 — Os cinco pilares da zona de pouso sobre uma base comum. Fonte: material do curso, com base na documentação de zona de pouso da AWS e da Azure.*`
   - Uma frase por pilar sobre ambientes separados e rede segmentada, com a remissão: o [bloco 3](bloco-3-seguranca-fim-a-fim.md) trata esses dois pilares como controles de segurança.
   - `#### Infraestrutura como código e etiquetas`: a descrição declarativa e versionada, a ferramenta portável entre provedores como redução de dependência de fornecedor, e as quatro etiquetas obrigatórias (projeto, ambiente, time e centro de custo) aplicadas pelo código e exigidas por política.
   - `#### Observabilidade como camada transversal`: os três sinais (registro estruturado, métricas e rastreamento) e o OpenTelemetry como padrão aberto de coleta, com o rastreamento como forma de responder em que trecho o tempo foi gasto.
   - Frase de fronteira: região, zonas de disponibilidade e camadas de execução já foram tratadas no [bloco 4 da Aula 4](../modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md).
5. `## Uso pelo arquiteto`: manter o parágrafo da maior decisão tecnológica registrada em ADR, trocar "sete fatores" por "seis critérios do bloco 1", e acrescentar que a zona de pouso é registrada na decisão de plataforma.
6. `## Fontes`: acrescentar Lovatt (2021, seção 7.5) e as entradas da documentação de zona de pouso conferidas na Task 2.

- [ ] **Step 4: Reescrever o exercício 18**

Manter o contexto e o link para o exercício 10. Manter o Item 1 sem alteração. No Item 2, trocar a coluna `Fator` por `Critério` e ajustar as linhas para os seis critérios: aderência ao requisito (R6 e o requisito de duas nuvens, R4), competência (camada web com 9 pessoas, sem experiência em JSF 1.2 nos contratados desde 2021), custo total (orçamento de R$ 6,2 milhões e licenciamento Oracle que obriga a licenciar todos os núcleos físicos de ambiente virtualizado) e portabilidade (dois provedores pré-aprovados com decisões portáveis), e remeter o preenchimento ao Item 3 do [exercício 17](bloco-1-definicao-tecnologica-e-trm.md#exercicio-17) para os critérios de maturidade e suporte, e acrescentar, depois dele, o Item 3 descrito a seguir.

`### Item 3: Zona de pouso da solução`. Diagrama Mermaid `graph TB` com a organização, as contas (desenvolvimento, homologação, produção, rede central, segurança e registros), a ligação híbrida ao centro de dados e a lista de recursos, e tabela de seis recursos (o serviço de matrícula, o banco do serviço de matrícula, o gateway de APIs, o serviço de notas, a fila de eventos de notas e o bucket de trilha de auditoria) com as etiquetas que cada um traz, algumas incompletas e nenhuma marcada. Reproduzir R4, R14 (dado pessoal de aluno em território nacional) e R9 (trilha com retenção de 5 anos) com origem. Perguntas: associar cada elemento do diagrama ao pilar que ele realiza, indicar a etiqueta obrigatória que falta em cada recurso, e responder em uma linha qual requisito justifica a conta de segurança e registros.

- [ ] **Step 5: Desenhar o visual**

`modulo-5-pilares-zona-de-pouso.svg`, mesmo padrão da Task 3: cinco colunas (contas por ambiente, rede hub-spoke, identidade centralizada, políticas automatizadas, monitoramento e faturamento) sobre uma base comum "infraestrutura como código e etiquetas". Sem "ACME", "COBOL", "CICS", "Oracle" ou "matrícula".

- [ ] **Step 6: Rodar testes e validador**

Run: `.venv/bin/python -m unittest tests.test_modulo_5_contract.BlockTwoTest tests.test_modulo_5_contract.ModuleFiveStructureTest.test_pages_do_not_use_first_person_or_the_old_framing -v && .venv/bin/python scripts/validate_content.py --module modulo-5-frameworks-e-tecnologias`
Expected: testes do bloco 2 em PASS e nenhuma violação em `bloco-2-plataforma-arquitetural.md`.

- [ ] **Step 7: Commit**

```bash
git add docs/modulo-5-frameworks-e-tecnologias/bloco-2-plataforma-arquitetural.md docs/assets/images/modulo-5-pilares-zona-de-pouso.svg docs/referencia/glossario.md
git commit -m "$(cat <<'EOF'
feat(aula-5): revisa o bloco de plataforma com zona de pouso e seis criterios

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 5: Bloco 3, segurança fim a fim

**Files:**
- Modify: `docs/modulo-5-frameworks-e-tecnologias/bloco-3-seguranca-fim-a-fim.md`
- Create: `docs/assets/images/modulo-5-fronteira-de-confianca-stride.svg`
- Create: `docs/assets/images/modulo-5-grade-de-permissoes.svg`
- Modify: `docs/referencia/glossario.md` (Grade de permissões, Menor privilégio, Fronteira de confiança, STRIDE, Autoridade de design de segurança, Dado pessoal sensível)

**Interfaces:**
- Consumes: Lovatt 2.9, 4.6.7 e 7.7 (linhas 1556, 3352 e 5650 do texto integral), blocos 1 e 2 desta aula, notas de conferência da Task 2, `docs/caso-acme/index.md` (R8, R9, R14 e restrições)
- Produces: âncora `bloco-3-seguranca-fim-a-fim.md#exercicio-19` e os termos do glossário listados acima

- [ ] **Step 1: Rodar os testes do bloco e confirmar a falha**

Run: `.venv/bin/python -m unittest tests.test_modulo_5_contract.BlockThreeTest -v 2>&1 | tail -15`
Expected: FAIL nos quatro testes.

- [ ] **Step 2: Ler as notas da Task 2**

Ler `fontes-modulo-5.md` no scratchpad. Usar na página somente os artigos da LGPD, as categorias do STRIDE e os códigos do OWASP que constam como `conferida`. Se uma delas constar como `não conferida`, apresentar o conceito como convenção do curso, sem citar a fonte, e dizer isso no relatório.

- [ ] **Step 3: Acrescentar as entradas ao glossário**

Uma definição de um parágrafo para cada termo, em ordem alfabética:

- `## Autoridade de design de segurança`: grupo que decide sobre os aspectos de segurança de todas as soluções da organização e aplica dois testes, a conformidade com as diretivas e o teste de vulnerabilidade.
- `## Dado pessoal sensível`: dado pessoal sobre origem racial ou étnica, convicção religiosa, opinião política, saúde, vida sexual, dado genético ou biométrico, nos termos da LGPD, sujeito a bases legais mais restritas. Conferir a lista contra o art. 5º, II, na Task 2.
- `## Fronteira de confiança`: linha que separa partes de uma solução que operam sob níveis diferentes de confiança, e na qual os dados que a atravessam precisam ser validados e protegidos.
- `## Grade de permissões`: tabela que cruza entidades, pessoas ou sistemas, com recursos ou tarefas, e indica em cada interseção o tipo de acesso permitido e as condições.
- `## Menor privilégio`: princípio segundo o qual cada entidade recebe o acesso mínimo, com o menor nível de privilégio, que permite executar suas atividades.
- `## STRIDE`: classificação de ameaças em seis categorias, falsificação de identidade, adulteração, repúdio, divulgação de informação, negação de serviço e elevação de privilégio, usada para examinar cada fronteira de confiança.

- [ ] **Step 4: Escrever a página**

1. `# Segurança fim a fim`
2. Linha de enquadramento: o bloco avalia, sobre a tecnologia escolhida nos blocos anteriores, se a solução protege o que precisa proteger.
3. `## Antes de começar`: links para `menor-privilegio`, `fronteira-de-confianca`, `grade-de-permissoes`, `stride`, `autoridade-de-design-de-seguranca`, `dado-pessoal-sensivel` e `zona-de-pouso`.
4. Seção de conceito `## Segurança como passo da definição tecnológica`:
   - `### Segurança da informação e arquitetura de segurança`: as duas definições, a distinção entre arquitetura de segurança (mudança) e operações de segurança (dia a dia), e os quatro objetivos (Lovatt 2.9.1).
   - `### Quatro formas de especificar segurança`: requisito funcional, requisito não funcional, diretiva corporativa e padrão técnico, em tabela com um exemplo de cada, com links para o [bloco 2 da Aula 2](../modulo-2-requisitos-e-partes-interessadas/bloco-2-qualidade-e-tipos-de-requisito.md) e para o padrão técnico no [bloco 3 da Aula 4](../modulo-4-dominios-da-solucao/bloco-3-arquitetura-de-aplicacoes-e-integracao.md).
   - `### Ativos e sua classificação`: ativo em todos os domínios (papéis, unidades, dados, sistemas, nós), classificação por confidencialidade, integridade e disponibilidade, e o complemento da Lei Geral de Proteção de Dados: dado pessoal, dado pessoal sensível, base legal e transferência internacional.
   - `### Grade de permissões e menor privilégio`: a grade que cruza entidade e recurso, tipo de acesso, condição e nível de segurança. Figura 1, `modulo-5-grade-de-permissoes.svg`, legenda `*Figura 1 — Grade de permissões com tipo de acesso e nível de segurança. Fonte: material do curso, com base em Lovatt (2021, seção 4.6.7).*`
   - `### Controles da zona de pouso`: ambientes separados como fronteira de permissão, de conformidade e de efeito, sub-rede privada para serviços de retaguarda e bancos de dados, identidade centralizada por padrão aberto, cada um com link ao [bloco 2](bloco-2-plataforma-arquitetural.md).
   - `### Fronteira de confiança e STRIDE`: a definição de fronteira de confiança, as seis categorias, a propriedade violada e o controle típico de cada uma, em tabela. Figura 2, `modulo-5-fronteira-de-confianca-stride.svg`, legenda `*Figura 2 — Uma fronteira de confiança e as seis categorias STRIDE aplicadas a ela. Fonte: material do curso, com base em Shostack (2014).*`
   - `### Autoridade de design de segurança`: os dois testes, conformidade com as diretivas (ISO/IEC 27001 como exemplo) e teste de vulnerabilidade com OWASP Top 10 e CWE, a matriz RACI da atividade (descrever em tabela de três papéis, sem reproduzir a tabela do livro), e a saída: avaliação com recomendações que a equipe de solução e a de infraestrutura executam.
   - `### O exemplo do Hospital ACME`: portal de preferências de contato do paciente, que identifica o paciente por credenciais cruzadas com dados demográficos classificados como dado pessoal, com os achados de conformidade (acesso por processo definido, segredo de autenticação controlado, identidade e acesso por controles aprovados, todo acesso registrado) e três vulnerabilidades (acesso além do necessário, injeção por dado do usuário enviado ao banco, registro e monitoramento insuficientes), com os códigos do OWASP conforme a Task 2.
5. `## Uso pelo arquiteto`: o arquiteto leva à autoridade de design de segurança um desenho já com ativos classificados e permissões especificadas, e a recomendação dela retorna à equipe de solução como revisão de desenho.
6. `## Exercício 19`: contexto da ACME em duas frases, links para o [exercício 16](../modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md#exercicio-16) e para o [exercício 18](bloco-2-plataforma-arquitetural.md#exercicio-18), reprodução de R9, R14 e da restrição do parecer do Jurídico de 28/04/2026, e três itens:
   - `### Item 1: Ativos de dado e LGPD`. Diagrama Mermaid com os seis ativos ligados às capacidades. Tabela de seis ativos, nota, histórico escolar, CPF, dados socioeconômicos de bolsa, laudo de necessidade educacional específica e oferta de turmas, com colunas Ativo e Onde é gravado (retirado de `docs/caso-acme/linha-de-base.md`), e sem coluna de classificação. Perguntas: classificar cada ativo em não pessoal, pessoal ou pessoal sensível, atribuir confidencialidade baixa, média ou alta, e responder em uma linha qual ativo a restrição R14 impede de ser processado fora do território nacional e qual serviço externo da arquitetura alvo é afetado.
   - `### Item 2: Grade de permissões`. Grade com perfis nas linhas (aluno, professor, secretaria acadêmica, serviço de notas, serviço de matrícula, ambiente virtual de aprendizagem) e recursos nas colunas (nota, matrícula, histórico escolar), com L, E e nada em cada célula, contendo três erros de privilégio (por exemplo, o ambiente virtual com gravação em nota, o professor lendo matrícula de turma que não leciona e o aluno gravando nota). Os erros não são nomeados no enunciado. Perguntas: apontar as três células que violam o menor privilégio e indicar o acesso correto de cada uma.
   - `### Item 3: Ameaças na fronteira do aplicativo do aluno`. Diagrama Mermaid com a fronteira entre o aplicativo do aluno e o serviço de matrícula, retirada do diagrama do exercício 16. Tabela de seis ameaças descritas em linguagem de cenário, sem o nome da categoria, e lista de seis controles (autenticação forte por OpenID Connect, assinatura e verificação de integridade da mensagem, registro de auditoria imutável, criptografia em trânsito e em repouso, limite de taxa e reserva de capacidade, autorização por papel no serviço) em ordem diferente. Perguntas: classificar cada ameaça numa categoria STRIDE e escolher o controle correspondente.
7. `## Fontes`: Lovatt (2021) com as seções 2.9, 4.6.7 e 7.7 e a nota de que o Hospital ACME é a versão portuguesa do caso Fallowdale Hospital, as fontes complementares conferidas na Task 2 (Lei nº 13.709/2018, Shostack, OWASP, CWE, ISO/IEC 27001) e `**Material do curso.**`.

- [ ] **Step 5: Desenhar os dois visuais**

Mesmo padrão da Task 3, sem termos do caso.

- `modulo-5-grade-de-permissoes.svg`: grade genérica com três entidades (usuário final, serviço de aplicação, administrador) e três recursos, com L, E e traço, e uma coluna de nível de segurança baixo, médio e alto.
- `modulo-5-fronteira-de-confianca-stride.svg`: dois blocos separados por uma linha tracejada rotulada "fronteira de confiança", com seis setas numeradas na fronteira e a legenda das seis categorias em português.

- [ ] **Step 6: Rodar testes e validador**

Run: `.venv/bin/python -m unittest tests.test_modulo_5_contract.BlockThreeTest -v && .venv/bin/python scripts/validate_content.py --module modulo-5-frameworks-e-tecnologias`
Expected: testes do bloco 3 em PASS e nenhuma violação em `bloco-3-seguranca-fim-a-fim.md`.

- [ ] **Step 7: Commit**

```bash
git add docs/modulo-5-frameworks-e-tecnologias/bloco-3-seguranca-fim-a-fim.md docs/assets/images/modulo-5-fronteira-de-confianca-stride.svg docs/assets/images/modulo-5-grade-de-permissoes.svg docs/referencia/glossario.md
git commit -m "$(cat <<'EOF'
feat(aula-5): escreve o bloco de seguranca fim a fim

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 6: Bloco 4, ADR de plataforma e lacunas (revisão)

**Files:**
- Modify: `docs/modulo-5-frameworks-e-tecnologias/bloco-4-adr-de-plataforma.md`
- Create: `docs/assets/images/modulo-5-tipos-de-lacuna.svg`

**Interfaces:**
- Consumes: Lovatt 7.8 e 7.9 (linhas 5713 e 5743 do texto integral), bloco 1 (matriz dos seis critérios), exercícios 17 a 19
- Produces: âncora `bloco-4-adr-de-plataforma.md#exercicio-20` mantida e item 4 novo

- [ ] **Step 1: Rodar os testes do bloco e confirmar a falha**

Run: `.venv/bin/python -m unittest tests.test_modulo_5_contract.BlockFourTest -v 2>&1 | tail -15`
Expected: FAIL nos três testes.

- [ ] **Step 2: Editar o conceito**

Ler o arquivo inteiro antes de editar. Manter `### O que muda no campo de forças`, o campo de consequências e `### O par de registros`.

1. `### O que muda no campo de forças`: substituir a referência aos sete fatores por "os seis critérios do [bloco 1](bloco-1-definicao-tecnologica-e-trm.md)" e conferir que o texto restante concorda.
2. `### O que muda no campo de alternativas`: dizer que a matriz dos seis critérios do bloco 1, com a plataforma descartada avaliada pelos mesmos critérios da escolhida, é o conteúdo do campo, e manter o link para o [exercício 18](bloco-2-plataforma-arquitetural.md#exercicio-18).
3. Nova seção `### Lacunas na provisão de serviços`, depois do par de registros:
   - Definição: a comparação entre a definição tecnológica e o catálogo de infraestrutura lista o que impede ou atrapalha a implantação, e o resultado é um relatório de lacunas.
   - Os quatro tipos, em tabela com a descrição de cada um: nova (serviço ainda não provido), substituição (serviço existente trocado por outro), modificação (serviço existe e precisa de reconfiguração, ampliação ou nova região), remoção (serviço deixa de ser necessário). Figura 1, `modulo-5-tipos-de-lacuna.svg`, legenda `*Figura 1 — Os quatro tipos de lacuna na provisão de serviços de infraestrutura. Fonte: material do curso, com base em Lovatt (2021, seção 7.8).*`
   - Parágrafo: cada lacuna recebe tamanho, custo, recurso e tempo, e uma troca de serviço pode reduzir o custo recorrente depois de custar para executar. Custo acima do esperado leva a rever a tecnologia, o desenho, o escopo ou as oportunidades de linha de base. As lacunas entram no [roteiro de entrega](../modulo-6-lacunas-e-governanca/index.md) da Aula 6, tratado ali como método próprio.
4. Nova seção `### Validação da definição tecnológica`: a validação com as partes interessadas, conduzida em conjunto pela equipe de arquitetura de solução e pela função de infraestrutura, com a lista do que a oficina cobre (percurso da definição, mudanças no desenho, custos e economias, compromissos das escolhas, preocupações), em uma lista de cinco itens.
5. `## Uso pelo arquiteto`: manter o parágrafo atual e acrescentar uma frase que liga o relatório de lacunas ao custo da solução e ao roteiro.
6. `## Fontes`: acrescentar Lovatt (2021, seções 7.8 e 7.9) e manter as demais.

- [ ] **Step 3: Atualizar o exercício 20**

Manter o contexto e os Itens 1 a 3. No Item 1, trocar a referência ao "quadro comparativo" por "matriz dos seis critérios", com link ao [exercício 17](bloco-1-definicao-tecnologica-e-trm.md#exercicio-17), e acrescentar ao diagrama Mermaid um nó para o [exercício 19](bloco-3-seguranca-fim-a-fim.md#exercicio-19) como entrada de consequências. No Item 2, trocar "pelo menos três dos sete fatores de adaptação ao contexto" por "pelo menos três dos seis critérios de seleção", e acrescentar o Item 4 descrito a seguir.

`### Item 4: Lacunas de provisão`. Diagrama Mermaid `graph LR` com o catálogo de infraestrutura atual da ACME (data center próprio, núcleo e banco, diretório corporativo, extração noturna por arquivo, ausência de mensageria e de provedor de identidade) ligado à definição tecnológica da arquitetura alvo. Tabela de seis requisitos de serviço, com colunas Requisito de serviço e Situação no catálogo atual: provedor de identidade com OpenID Connect (o catálogo só tem o diretório corporativo por LDAP), mensageria com tópico e contrato AsyncAPI (não existe, hoje a troca é por arquivo), banco de serviço novo em região nacional (o catálogo só tem o banco compartilhado), diretório corporativo (autentica todos os perfis, continua em uso até o último portal migrar), extração noturna por arquivo para o data warehouse e o ambiente virtual (lote das 02h30, 140 tabelas em cópia integral), observabilidade de ponta a ponta (sem ferramenta registrada para o sistema acadêmico). Sem coluna de tipo de lacuna. Perguntas: classificar cada requisito em nova, substituição, modificação ou remoção, e indicar qual dos seis tende a reduzir o custo recorrente, com uma linha de justificativa. Os dados vêm das páginas linha-de-base e dados-operacionais da pasta `caso-acme`, e cada número é conferido ali antes da escrita.

- [ ] **Step 4: Desenhar o visual**

`modulo-5-tipos-de-lacuna.svg`, mesmo padrão da Task 3: quatro cartões em linha (nova, substituição, modificação, remoção), cada um com um mini diagrama antes e depois do catálogo de serviços, e uma faixa inferior "tamanho, custo, recurso e tempo de cada mudança". Sem termos do caso.

- [ ] **Step 5: Rodar testes e validador**

Run: `.venv/bin/python -m unittest tests.test_modulo_5_contract.BlockFourTest tests.test_modulo_5_contract.ExerciseRuleTest tests.test_modulo_5_contract.ModuleFiveStructureTest -v 2>&1 | tail -30 && .venv/bin/python scripts/validate_content.py --module modulo-5-frameworks-e-tecnologias`
Expected: os testes dos blocos 1 a 4 e a estrutura em PASS, exceto `test_each_block_cites_lovatt_with_its_sections` para a página que ainda não cita a seção, que deve passar depois deste passo, e nenhuma violação nas quatro páginas de bloco. As falhas restantes do módulo são só as de índice, síntese, cronograma e artefatos, que a Task 7 resolve.

- [ ] **Step 6: Commit**

```bash
git add docs/modulo-5-frameworks-e-tecnologias/bloco-4-adr-de-plataforma.md docs/assets/images/modulo-5-tipos-de-lacuna.svg
git commit -m "$(cat <<'EOF'
feat(aula-5): revisa o bloco de ADR com lacunas de provisao

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 7: Índice, síntese, cronograma, artefatos e gabaritos

**Files:**
- Modify: `docs/modulo-5-frameworks-e-tecnologias/index.md`
- Modify: `docs/modulo-5-frameworks-e-tecnologias/sintese.md`
- Modify: `docs/cronograma.md` (tabela da Aula 5)
- Modify: `docs/caso-acme/artefatos.md` (linha e descrição dos exercícios 17 a 20)
- Modify: `~/pka/projects/aulas/PRJ-aulas-iec-projeto-e-inovacao-em-arquitetura-de-solucoes.md` (fora do repositório)

**Interfaces:**
- Consumes: páginas das Tasks 3 a 6
- Produces: nenhum

- [ ] **Step 1: Rodar os testes de integração e confirmar a falha**

Run: `.venv/bin/python -m unittest tests.test_modulo_5_contract.CourseIntegrationTest -v 2>&1 | tail -20`
Expected: FAIL em `test_index_has_objectives_schedule_inputs_route_and_bridge`, `test_synthesis_has_checklist_chain_self_assessment_and_sources`, `test_schedule_describes_the_four_blocks_of_class_5` e `test_artifacts_page_lists_the_class_5_products`.

- [ ] **Step 2: Escrever o índice**

Ler `docs/modulo-4-dominios-da-solucao/index.md` e seguir a ordem das seções. Seções: `# Aula 5, frameworks e tecnologias`, parágrafo de abertura (a aula converte o desenho lógico da Aula 4 em tecnologia e verifica a segurança sobre a tecnologia escolhida), `## Objetivos de aprendizagem` com os seis objetivos da seção 1 do spec, `## Grade de tempo`, `## Entrada recebida da Aula 4`, `## Roteiro da aula`, `## Preparação para a Aula 6`.

Grade de tempo, sem bloco 0, com a frase de regra dos exercícios ("os exercícios são realizados fora do horário de aula") e o texto de quarenta e cinco minutos restantes:

| Horário | Atividade | Duração (min) |
| --- | --- | --- |
| 19h00–19h15 | Questões sobre a Aula 4 | 15 |
| 19h15–19h25 | Kahoot de revisão da Aula 4 | 10 |
| 19h25–19h58 | Bloco 1, definição tecnológica e modelo técnico de referência | 33 |
| 19h58–20h30 | Bloco 2, plataforma arquitetural | 32 |
| 20h30–20h45 | Intervalo | 15 |
| 20h45–20h55 | Kahoot dos blocos 1 e 2 | 10 |
| 20h55–21h28 | Bloco 3, segurança fim a fim | 33 |
| 21h28–22h00 | Bloco 4, ADR de plataforma e lacunas | 32 |
| 22h00–22h10 | Kahoot dos blocos 3 e 4 | 10 |

`## Entrada recebida da Aula 4`: o diagrama de contêineres do [exercício 16](../modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md#exercicio-16), com as relações rotuladas e os contêineres com tecnologia a definir, e o ADR de estilo do [exercício 12](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md#exercicio-12). `## Roteiro da aula`: um parágrafo por bloco, com o exercício de cada um, e a síntese. `## Preparação para a Aula 6`: a Aula 6 compara a linha de base com a arquitetura alvo, usa as lacunas de provisão como entrada do roteiro de entrega e trata governança e inovação. Remover o parágrafo que anuncia a publicação futura dos blocos 1 e 3.

- [ ] **Step 3: Escrever a síntese**

Ler `docs/modulo-4-dominios-da-solucao/sintese.md` e seguir o formato. Seções: linha de abertura, `## Checklist do que precisa permanecer`, `## Cadeia da definição tecnológica` (contêineres do exercício 16, categorias e tecnologias classificadas do exercício 17, plataforma e zona de pouso do exercício 18, controles e ameaças do exercício 19, ADR e lacunas do exercício 20, com o produto de cada exercício e o link), `## Autoavaliação` (cinco perguntas sem gabarito) e `## Fontes da aula` (todas as referências dos quatro blocos).

- [ ] **Step 4: Atualizar o cronograma e a página de artefatos**

Em `docs/cronograma.md`, tabela da Aula 5, ajustar os temas dos blocos 2 e 4 para "Plataforma arquitetural, frameworks, zona de pouso e dependência de fornecedor" e "ADR de plataforma e lacunas na provisão de serviços". Manter os números 17 a 20. Em `docs/caso-acme/artefatos.md`, ler o arquivo inteiro e substituir a linha da Aula 5 por "Contêineres associados a categorias do modelo técnico de referência, tecnologias classificadas e matriz de seleção, quadro comparativo de plataformas com os pilares da zona de pouso, ativos classificados com a grade de permissões corrigida e as ameaças por categoria STRIDE, e o ADR de plataforma com as lacunas de provisão classificadas", atualizando também qualquer descrição por exercício dessa aula.

- [ ] **Step 5: Registrar os gabaritos no PKA**

Ler `~/pka/CLAUDE.md` antes de editar. No arquivo `PRJ-aulas-iec-projeto-e-inovacao-em-arquitetura-de-solucoes.md`, verificar se há gabarito de exercício 18 e 20 já renumerado (a tabela da linha 247 indica que os gabaritos da antiga Aula 2 valem para os exercícios 12, 16, 18 e 20). Acrescentar `## Gabaritos dos exercícios da Aula 5` depois da seção da Aula 4, com `### Exercício 17` a `### Exercício 20`, no formato existente (resposta de referência, distinção entre resposta excelente, aceitável e fraca, e critério de correção). Para os exercícios 18 e 20, reaproveitar o gabarito existente e acrescentar o item novo.

Respostas de referência dos itens novos: exercício 17 item 2, JSF 1.2 e EJB 2.0 em vermelho com plano de migração documentado para as 220 telas, Oracle 12c em âmbar com ADR de desvio para projeto novo, acesso direto em vermelho, COBOL sob CICS como exceção contratual até 30/09/2027, diretório corporativo em âmbar até o último portal migrar, arquivo posicional em vermelho. Exercício 19 item 1, CPF e dado socioeconômico de bolsa como pessoais, laudo de necessidade educacional específica como sensível (saúde), com confiabilidade alta para os dois últimos, e identificação do serviço externo conforme o diagrama do exercício 16. Exercício 20 item 4, provedor de identidade e mensageria como novas, banco de serviço novo como nova, diretório corporativo como modificação (convive e depois sai), extração noturna como substituição, observabilidade como nova, com a substituição da extração noturna como a que reduz custo recorrente. Cada resposta é conferida contra as células do artefato fornecido no item 2 do exercício 17, no item 1 do exercício 19 e no item 4 do exercício 20.

- [ ] **Step 6: Rodar testes e validador**

Run: `.venv/bin/python -m unittest tests.test_modulo_5_contract -v 2>&1 | tail -15 && .venv/bin/python scripts/validate_content.py`
Expected: toda a suíte do módulo em PASS e zero violação.

- [ ] **Step 7: Commit**

```bash
git add docs/modulo-5-frameworks-e-tecnologias/index.md docs/modulo-5-frameworks-e-tecnologias/sintese.md docs/cronograma.md docs/caso-acme/artefatos.md
git commit -m "$(cat <<'EOF'
feat(aula-5): escreve indice e sintese e atualiza cronograma e artefatos

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
EOF
)"
```

---

### Task 8: Verificação integral

**Files:**
- Correções pontuais onde a verificação apontar.

**Interfaces:**
- Consumes: todas as tarefas anteriores
- Produces: evidência de aceite para os critérios das seções 12 e 13 do spec

- [ ] **Step 1: Suíte e validador**

Run: `.venv/bin/python -m unittest discover -s tests -v 2>&1 | tail -8 && .venv/bin/python scripts/validate_content.py`
Expected: todos os testes em OK e zero violação.

- [ ] **Step 2: Build estrito**

Run: `.venv/bin/mkdocs build --strict`
Expected: build sem aviso nem erro, inclusive links relativos e âncoras `#exercicio-17` a `#exercicio-20`.

- [ ] **Step 3: Conferência visual a 688 px**

Servir o site com `.venv/bin/mkdocs serve -a 127.0.0.1:8123` em segundo plano e renderizar com Playwright (Chromium) a 1424 px de largura, coluna de 688 px, as cinco páginas com figura: blocos 1 a 4. Salvar as capturas no scratchpad e ler cada uma. Conferir: legibilidade dos seis SVG, diagramas Mermaid dos exercícios 17 a 20 sem rótulo cortado nem cadeia horizontal reduzida (o Material renderiza Mermaid em shadow DOM fechado, então qualquer correção vai no código-fonte: cadeia longa em duas fileiras, títulos de subgrafo curtos, rótulos com `<br/>`, `curve: stepAfter`), e tabelas largas sem rolagem horizontal da página. Se o Playwright não estiver instalado, instalar em um diretório do scratchpad, fora do repositório, e registrar. Se não houver como renderizar, registrar no relatório que a inspeção das páginas renderizadas não foi feita.

- [ ] **Step 4: Leitura editorial**

Reler as seis páginas contra as restrições globais: verbos de construção, ausência de resposta nos artefatos fornecidos (item 2 do exercício 17, item 3 do exercício 19 e item 4 do exercício 20), negrito entre três e cinco por página, ausência de "Lovatt" no corpo, conferência dos artigos da LGPD, da descrição do STRIDE e dos nomes das estruturas de zona de pouso contra as notas da Task 2, e a divergência SOAP e LDAP registrada no relatório final para o professor ajustar o EAD.

- [ ] **Step 5: Mapa de cobertura do spec**

Conferir, seção a seção do spec, que cada requisito tem página, teste ou passo que o cubra: objetivos (índice), decisões de escopo (Tasks 3 a 6), base bibliográfica (Tasks 2 a 6), progressão (síntese), exercícios (Tasks 3 a 6), páginas de apoio (Tasks 3 a 7), estratégia visual (Tasks 3 a 6) e testes (Task 1). Listar qualquer lacuna e corrigir.

- [ ] **Step 6: Commit das correções**

```bash
git add docs tests
git commit -m "$(cat <<'EOF'
fix(aula-5): corrige apontamentos da verificacao integral

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>
EOF
)"
```
