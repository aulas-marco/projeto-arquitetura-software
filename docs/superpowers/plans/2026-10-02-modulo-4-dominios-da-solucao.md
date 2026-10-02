# Aula 4, domínios da arquitetura de solução

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produzir a Aula 4 do site, organizada pelos domínios de negócio, dados, aplicações e infraestrutura, com índice, síntese, quatro visuais, a cadeia de exercícios 13 a 16 e o ajuste do cronograma que transfere segurança para a Aula 5.

**Architecture:** A pasta `modulo-4-protocolos-e-representacao` é renomeada para `modulo-4-dominios-da-solucao`, com redirecionamento das URLs antigas. Um teste novo, `tests/test_modulo_4_contract.py`, fixa antes da escrita os contratos que o validador genérico não cobre. O conteúdo atual do C4 é dividido entre o bloco 3, que recebe a introdução e o nível de contexto, e o bloco 4, que recebe o nível de contêineres. Os visuais são SVG escritos à mão no padrão de `docs/assets/images/modulo-3-niveis-de-padrao.svg`.

**Tech Stack:** Python 3, unittest, MkDocs Material em `.venv` com o plugin `redirects`, SVG estático, Markdown com `attr_list` e `md_in_html`.

**Spec:** `docs/superpowers/specs/2026-10-02-modulo-4-dominios-da-solucao-design.md`

## Global Constraints

- Anatomia de página de bloco, na ordem: título funcional, linha de enquadramento, `## Antes de começar`, seção de conceito com título livre, `## Uso pelo arquiteto`, `## Exercício N`, `## Fontes`.
- Exercícios numerados 13, 14, 15 e 16, um por bloco, na ordem dos blocos.
- Regra dos exercícios: o enunciado fornece o artefato já montado e o aluno classifica, marca, rotula ou responde perguntas simples. Nenhum enunciado usa os verbos desenhe, monte, construa, modele ou mapeie como tarefa do aluno.
- O artefato fornecido não traz a resposta: capacidades sem classificação, grade sem dono, diagrama de contexto com os erros presentes, diagrama de contêineres com relações sem rótulo.
- Lovatt (2021) é a base de cada bloco, citado com a seção no texto e em Fontes. Texto integral em `/Volumes/Marco-Dev/dev/projeto-arquitetura-solucao/docs/superpowers/plans/livro-lovatt.md`.
- Termos e nomes dos casos de Lovatt em português. Fallowdale é o Hospital Vale do Pousio, e a palavra Fallowdale aparece apenas no bloco de Fontes, como origem do caso.
- Segurança não é tema de bloco da Aula 4. Zonas de confiança, controles e grade de permissões ficam para a Aula 5.
- Contêineres da arquitetura alvo levam o rótulo "tecnologia a definir na Aula 5".
- Zero ponto e vírgula em texto corrido, no máximo um travessão por parágrafo fora de `## Fontes`, nenhum título abrindo com "Por que", nenhum título com subtítulo após travessão, nenhuma ocorrência da palavra "prosa".
- Negrito entre três e cinco ocorrências por página, só na seção de conceito, no primeiro uso do termo.
- Registro sóbrio e impessoal, português brasileiro com acentuação completa, sem metáfora, sem frase de efeito no fim de parágrafo, média de pelo menos 14 palavras por frase.
- Fonte complementar entra no texto e na bibliografia somente depois de conferida na origem. Fonte não conferida sai do texto e do teste de bibliografia.
- Nenhum gabarito no site. Gabaritos dos exercícios 13 a 16 vão para `~/pka/projects/aulas/PRJ-aulas-iec-projeto-e-inovacao-em-arquitetura-de-solucoes.md`, em seção nova `## Gabaritos dos exercícios da Aula 4`.
- Visuais com nome `modulo-4-*.svg`, `<title>` e `<desc>` preenchidos, fonte interna de pelo menos 16 px, marcados com `{ .module-diagram }`, sem os termos "ACME", "COBOL", "CICS" ou "matrícula".
- Os ajustes de CSS sem commit em `mkdocs.yml` e `tests/test_modulo_3_contract.py` não entram nos commits deste plano. Em `mkdocs.yml`, o commit inclui só os trechos deste plano, por `git add -p`.

## Review Focus

- Link antigo para a página de C4: alunos guardaram a URL do bloco 4 atual. Teste: `mkdocs.yml` redireciona `modulo-4-protocolos-e-representacao/bloco-4-representacao-de-modelos-e-c4.md` para o bloco 3 novo, e nenhum alvo de redirecionamento aponta para a pasta antiga.
- Exercício que volta a pedir construção de modelo: a regra foi decidida pelo professor e é fácil de violar ao escrever o enunciado. Teste: as seções de exercício não contêm "Desenhe", "Monte", "Construa", "Modele" nem "Mapeie".
- Confusão entre padrão técnico e padrão arquitetural: teste exige "padrão técnico", "*standard*" e "*pattern*" no bloco 3.
- Nome inglês do caso no corpo do texto: teste exige "Hospital Vale do Pousio" nos blocos 1 a 3 e ausência de "Fallowdale" fora de `## Fontes`.
- Segurança reaparecendo na Aula 4 pelo cronograma: teste exige que a tabela da Aula 4 no cronograma não contenha "segurança" e que a da Aula 5 contenha "Segurança fim a fim".

---

### Task 1: Renomeação da pasta, navegação, redirecionamentos e contrato

**Files:**
- Rename: `docs/modulo-4-protocolos-e-representacao/` para `docs/modulo-4-dominios-da-solucao/`
- Rename: `bloco-4-representacao-de-modelos-e-c4.md` para `bloco-4-arquitetura-de-infraestrutura.md`
- Create: esqueletos de `bloco-1-arquitetura-de-negocio.md`, `bloco-2-arquitetura-de-dados.md`, `bloco-3-arquitetura-de-aplicacoes-e-integracao.md`, `sintese.md`
- Modify: `mkdocs.yml` (nav da Aula 4 e `redirect_maps`)
- Modify: `scripts/validate_content.py:22`, `tests/course_assertions.py:10`, `tests/test_content_contract.py:209`
- Create: `tests/test_modulo_4_contract.py`

**Interfaces:**
- Produces: nomes de arquivo e de imagem usados sem variação pelas tarefas seguintes:
  - `bloco-1-arquitetura-de-negocio.md` com `modulo-4-modelos-de-negocio.svg`, âncora `#exercicio-13`
  - `bloco-2-arquitetura-de-dados.md` com `modulo-4-grade-dado-aplicacao.svg`, âncora `#exercicio-14`
  - `bloco-3-arquitetura-de-aplicacoes-e-integracao.md` com `modulo-4-servicos-e-contrato.svg`, âncora `#exercicio-15`
  - `bloco-4-arquitetura-de-infraestrutura.md` com `modulo-4-solucao-como-grafo.svg`, âncora `#exercicio-16`

- [ ] **Step 1: Escrever o teste de contrato**

```python
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
```

- [ ] **Step 2: Rodar o teste e confirmar a falha**

Run: `python3 -m unittest tests.test_modulo_4_contract -v`
Expected: FAIL em quase todos os testes, porque a pasta nova ainda não existe.

- [ ] **Step 3: Renomear a pasta e o arquivo do C4**

```bash
git mv docs/modulo-4-protocolos-e-representacao docs/modulo-4-dominios-da-solucao
git mv docs/modulo-4-dominios-da-solucao/bloco-4-representacao-de-modelos-e-c4.md docs/modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md
printf '# Arquitetura de negócio da solução\n' > docs/modulo-4-dominios-da-solucao/bloco-1-arquitetura-de-negocio.md
printf '# Arquitetura de dados da solução\n' > docs/modulo-4-dominios-da-solucao/bloco-2-arquitetura-de-dados.md
printf '# Arquitetura de aplicações e integração\n' > docs/modulo-4-dominios-da-solucao/bloco-3-arquitetura-de-aplicacoes-e-integracao.md
printf '# Síntese da Aula 4\n' > docs/modulo-4-dominios-da-solucao/sintese.md
```

- [ ] **Step 4: Atualizar navegação e redirecionamentos**

Em `mkdocs.yml`, substituir os três redirecionamentos que apontam para a pasta antiga e acrescentar os dois da pasta antiga:

```yaml
        modulo-2-plataforma-e-modelos/bloco-4-representacao-de-modelos-e-c4.md: modulo-4-dominios-da-solucao/bloco-3-arquitetura-de-aplicacoes-e-integracao.md
        modulo-4-integracao-e-dados/index.md: modulo-4-dominios-da-solucao/index.md
        modulo-4-protocolos-e-representacao/index.md: modulo-4-dominios-da-solucao/index.md
        modulo-4-protocolos-e-representacao/bloco-4-representacao-de-modelos-e-c4.md: modulo-4-dominios-da-solucao/bloco-3-arquitetura-de-aplicacoes-e-integracao.md
```

Substituir o item de navegação da Aula 4 por:

```yaml
  - "Aula 4, domínios da arquitetura de solução":
      - Visão geral: modulo-4-dominios-da-solucao/index.md
      - "Bloco 1: arquitetura de negócio": modulo-4-dominios-da-solucao/bloco-1-arquitetura-de-negocio.md
      - "Bloco 2: arquitetura de dados": modulo-4-dominios-da-solucao/bloco-2-arquitetura-de-dados.md
      - "Bloco 3: arquitetura de aplicações e integração": modulo-4-dominios-da-solucao/bloco-3-arquitetura-de-aplicacoes-e-integracao.md
      - "Bloco 4: arquitetura de infraestrutura": modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md
      - Síntese: modulo-4-dominios-da-solucao/sintese.md
```

- [ ] **Step 5: Atualizar o nome da pasta no validador e nos testes genéricos**

```bash
sed -i '' 's/modulo-4-protocolos-e-representacao/modulo-4-dominios-da-solucao/' scripts/validate_content.py tests/course_assertions.py tests/test_content_contract.py
```

- [ ] **Step 6: Rodar os testes estruturais**

Run: `python3 -m unittest tests.test_modulo_4_contract.ModuleFourStructureTest.test_all_pages_exist_and_are_in_nav tests.test_modulo_4_contract.ModuleFourStructureTest.test_old_urls_redirect_to_the_new_folder tests.test_modulo_4_contract.ModuleFourStructureTest.test_old_folder_is_gone tests.test_content_contract -v`
Expected: PASS.

- [ ] **Step 7: Commit**

```bash
git add tests/test_modulo_4_contract.py scripts/validate_content.py tests/course_assertions.py tests/test_content_contract.py docs/modulo-4-dominios-da-solucao docs/modulo-4-protocolos-e-representacao
git add -p mkdocs.yml
git commit -m "test(aula-4): renomeia a pasta e fixa o contrato do modulo"
```

---

### Task 2: Cronograma, Aula 5, preparação na Aula 3 e dossiê

**Files:**
- Modify: `docs/cronograma.md`
- Modify: `docs/modulo-5-frameworks-e-tecnologias/index.md`
- Modify: `docs/modulo-3-design-e-padroes/index.md` (seção `## Preparação para a Aula 4`)
- Modify: `docs/caso-acme/artefatos.md:34`

**Interfaces:**
- Consumes: pasta renomeada da Task 1
- Produces: nomes de bloco das Aulas 4 e 5 usados pelo índice da Task 7

- [ ] **Step 1: Rodar os testes de integração e confirmar a falha**

Run: `python3 -m unittest tests.test_modulo_4_contract.CourseIntegrationTest.test_schedule_moves_security_to_class_5 tests.test_modulo_4_contract.CourseIntegrationTest.test_module_5_index_lists_the_security_block tests.test_modulo_4_contract.CourseIntegrationTest.test_module_3_prepares_for_the_domains -v`
Expected: FAIL.

- [ ] **Step 2: Atualizar o cronograma**

Na tabela de sequência, a linha 4 passa a "Arquitetura de negócio, de dados, de aplicações e de infraestrutura da solução, com contrato de integração e modelagem C4", e a linha 5 passa a "Definição tecnológica e modelo técnico de referência, plataforma arquitetural e frameworks, segurança fim a fim e ADR de plataforma". O parágrafo do encadeamento passa a dizer que a Aula 4 detalha a solução em seus domínios e a representa. As tabelas de bloco das Aulas 4 e 5 passam ao conteúdo abaixo, com exercícios 13 a 20 mantidos:

```markdown
### Aula 4, domínios da arquitetura de solução

| Bloco | Tema | Exercício |
| --- | --- | --- |
| 1 | Arquitetura de negócio da solução, capacidades, fluxo de valor e processos | 13 |
| 2 | Arquitetura de dados da solução, com propriedade do dado | 14 |
| 3 | Arquitetura de aplicações e integração, contrato de integração e diagrama de contexto C4 | 15 |
| 4 | Arquitetura de infraestrutura da solução e diagrama de contêineres C4 | 16 |

### Aula 5, frameworks e tecnologias

| Bloco | Tema | Exercício |
| --- | --- | --- |
| 1 | Definição tecnológica e modelo técnico de referência, do bloco de construção ao serviço de infraestrutura | 17 |
| 2 | Plataforma arquitetural, frameworks e dependência de fornecedor | 18 |
| 3 | Segurança fim a fim | 19 |
| 4 | ADR de plataforma e lacunas na provisão de serviços | 20 |
```

- [ ] **Step 3: Atualizar o índice do módulo 5**

Substituir a tabela pela nova divisão, com links mantidos para os blocos 2 e 4 publicados, e o primeiro parágrafo passa a mencionar a segurança fim a fim avaliada sobre a tecnologia escolhida, conforme Lovatt (2021, seção 7.7).

- [ ] **Step 4: Atualizar a preparação na Aula 3**

Reescrever o parágrafo de `## Preparação para a Aula 4` em `docs/modulo-3-design-e-padroes/index.md`: a Aula 4 detalha a solução nos domínios de negócio, dados, aplicações e infraestrutura, partindo da declaração de escopo do exercício 8, do esboço lógico do exercício 9, dos padrões do exercício 11 e do ADR do exercício 12, e termina na representação C4 de contexto e de contêineres. Escolhas de produto continuam na Aula 5.

- [ ] **Step 5: Atualizar o dossiê**

Na linha da Aula 4 de `docs/caso-acme/artefatos.md`, o tema passa a "Domínios da arquitetura de solução" e os artefatos passam a: capacidades classificadas com etapas críticas do fluxo de valor, grade dado × aplicação com dono e regime de consistência, aplicações classificadas com o contrato da integração de notas e o diagrama de contexto corrigido, e o diagrama de contêineres com relações rotuladas. Na linha da Aula 5, acrescentar a avaliação de segurança fim a fim. No parágrafo de rastreabilidade, ajustar a frase da Aula 4.

- [ ] **Step 6: Rodar testes e validador**

Run: `python3 -m unittest tests.test_modulo_4_contract.CourseIntegrationTest -v && python3 scripts/validate_content.py`
Expected: os três testes do Step 1 em PASS e zero violação nos arquivos alterados.

- [ ] **Step 7: Commit**

```bash
git add docs/cronograma.md docs/modulo-5-frameworks-e-tecnologias/index.md docs/modulo-3-design-e-padroes/index.md docs/caso-acme/artefatos.md
git commit -m "docs(curso): reorganiza Aulas 4 e 5 por dominios e seguranca"
```

---

### Task 3: Bloco 1, arquitetura de negócio

**Files:**
- Modify: `docs/modulo-4-dominios-da-solucao/bloco-1-arquitetura-de-negocio.md`
- Create: `docs/assets/images/modulo-4-modelos-de-negocio.svg`
- Modify: `docs/referencia/glossario.md` (Arquitetura de negócio, Capacidade, Fluxo de valor)

**Interfaces:**
- Consumes: Lovatt seções 2.3 e 2.4 (linhas 1046 a 1224 do texto integral)
- Produces: âncora `bloco-1-arquitetura-de-negocio.md#exercicio-13`, produto com capacidades classificadas, consumido pelo exercício 14

- [ ] **Step 1: Rodar os testes do bloco e confirmar a falha**

Run: `python3 -m unittest tests.test_modulo_4_contract -k block_1 -k exercise_13 -v`
Expected: FAIL.

- [ ] **Step 2: Acrescentar as entradas ao glossário**

Depois de `## Modelo C4`, uma definição de um parágrafo para cada termo:

- `## Arquitetura de negócio`: representação da organização em capacidades, fluxos de valor, informação e estrutura organizacional, usada para alinhar objetivos estratégicos e demandas táticas, e que é ao mesmo tempo origem e alvo da mudança promovida pela solução.
- `## Capacidade`: aquilo que a organização precisa conseguir fazer para entregar seus serviços e executar sua estratégia, caracterizada por volume, competência e pelos recursos que a habilitam.
- `## Fluxo de valor`: conjunto de etapas de ponta a ponta pelo qual a organização entrega valor a um cliente, do primeiro contato até a realização desse valor.

- [ ] **Step 3: Escrever a página**

1. `# Arquitetura de negócio da solução`
2. Linha de enquadramento: o bloco abre o detalhamento por domínios localizando o que a solução muda no negócio antes de dados, aplicações e infraestrutura.
3. `## Antes de começar`: links para `arquitetura-de-negocio`, `capacidade`, `fluxo-de-valor`, `componentes-da-solucao` e `arquitetura-de-solucao`.
4. Seção de conceito `## Modelos de arquitetura de negócio`:
   - Definições citadas por Lovatt (2021, seção 2.3), do Business Architecture Guild e do TOGAF, em tradução, e o domínio como origem e alvo da mudança.
   - `### Quando a arquitetura de solução se aplica`: as quatro perguntas, se a área é um sistema, se pode ser modelada, se o modelo exibe o problema e se pode ser alterado, e a redução de escopo quando o problema é grande demais.
   - `### Quatro modelos`: tabela Modelo, Pergunta que responde, O que oferece ao arquiteto, com linhas Mapa de capacidades, Fluxo de valor, Decomposição funcional e Modelo de processo de negócio. Um parágrafo para mapa de capacidades com volume e competência e a classificação em estratégica, operacional e de apoio. Um parágrafo para fluxo de valor com a origem na produção enxuta. Um parágrafo dizendo que decomposição funcional e modelo de processo são artefatos que o arquiteto lê, e que modelar processo não é atribuição do arquiteto de solução nesta disciplina. Menção ao modelo de motivação de negócio com link para o bloco 1 da Aula 2.
   - Figura `modulo-4-modelos-de-negocio.svg` com legenda `*Figura 1 — Os quatro modelos de arquitetura de negócio e a pergunta de cada um. Fonte: material do curso, com base em Lovatt (2021, seção 2.3).*`
   - `### O exemplo do Hospital Vale do Pousio`: capacidade de comunicar-se com pacientes, volume e canais, e os processos de marcação, cancelamento, remarcação e lista de espera, com a origem do caso em Lovatt.
   - `### Componentes de negócio da solução`: um parágrafo de remissão a `../modulo-1-fundamentos/bloco-2-a-solucao-como-sistema.md`, dizendo que pessoas, unidades organizacionais e processos foram apresentados ali, e a afirmação de Lovatt (2021, seção 2.4.3) de que todo componente sustenta um ou mais serviços de negócio, como ponte para o bloco 3.
   - `### O ciclo de mudança de negócio`: os cinco estágios, alinhar, definir, projetar, implementar e realizar, com a arquitetura de solução concentrada em definir e projetar.
5. `## Uso pelo arquiteto`: o arquiteto consulta os modelos que a arquitetura de negócio já mantém para delimitar o que muda e evita redesenhar a organização.
6. `## Exercício 13`: frase padrão de exercício fora do horário de aula, contexto da ACME, link para `../modulo-2-requisitos-e-partes-interessadas/bloco-4-partes-interessadas-e-pontos-de-vista.md#exercicio-8`, e reprodução de R1, R7 e R13 com origem. Três artefatos fornecidos:
   - Tabela de dez capacidades sem classificação: Admissão e ingresso, Oferta e grade curricular, Matrícula em disciplinas, Avaliação e registro de notas, Controle de frequência, Emissão de documentos acadêmicos, Gestão de bolsas e descontos, Cobrança de mensalidades, Biblioteca, Relação com o órgão regulador. Pergunta: classificar cada uma em estratégica, operacional ou de apoio e marcar as afetadas pelo primeiro ciclo, com uma linha de justificativa.
   - Tabela do fluxo de valor do aluno com cinco etapas e o tempo de cada passagem retirado de `../caso-acme/linha-de-base.md`: renovação da matrícula no portal, confirmação da matrícula, matrícula visível no ambiente virtual às 04h55 do dia seguinte, nota lançada pelo professor, nota visível no ambiente virtual às 06h00 do dia seguinte. Pergunta: indicar as etapas em que a latência compromete o valor e qual requisito, R1, R7 ou R13, cada uma afeta.
   - Tabela do processo de lançamento de nota com seis atividades e responsável: professor registra nota no portal, núcleo calcula média e situação, secretaria trata pedido de revisão, lote das 05h10 exporta notas, ambiente virtual recebe arquivo, aluno consulta nota. Três perguntas: quais atividades mudam com a solução, qual unidade organizacional é afetada, qual diretiva rege o processo.
7. `## Fontes`: Lovatt (2021) com as seções 2.3 e 2.4 e a nota de que o Hospital Vale do Pousio é a versão portuguesa do caso Fallowdale Hospital, mais `**Material do curso.**` com glossário e dossiê.

- [ ] **Step 4: Desenhar o visual**

`modulo-4-modelos-de-negocio.svg`, `viewBox="0 0 1200 675"`, `role="img"`, `aria-labelledby="title desc"`, paleta `#F2F6FB`, `#16243A`, `#254DB8`, `#5FC0D1`, `#F2B84B`, fonte de pelo menos 16 px. Quatro cartões, um por modelo, com o nome e a pergunta que responde, e uma faixa inferior com os cinco estágios do ciclo de mudança, destacando definir e projetar.

- [ ] **Step 5: Rodar testes e validador**

Run: `python3 -m unittest tests.test_modulo_4_contract -k block_1 -k exercise_13 -v && python3 scripts/validate_content.py --module modulo-4-dominios-da-solucao`
Expected: testes do bloco 1 em PASS e nenhuma violação em `bloco-1-arquitetura-de-negocio.md`.

- [ ] **Step 6: Commit**

```bash
git add docs/modulo-4-dominios-da-solucao/bloco-1-arquitetura-de-negocio.md docs/assets/images/modulo-4-modelos-de-negocio.svg docs/referencia/glossario.md
git commit -m "feat(aula-4): escreve o bloco de arquitetura de negocio"
```

---

### Task 4: Bloco 2, arquitetura de dados

**Files:**
- Modify: `docs/modulo-4-dominios-da-solucao/bloco-2-arquitetura-de-dados.md`
- Create: `docs/assets/images/modulo-4-grade-dado-aplicacao.svg`
- Modify: `docs/referencia/glossario.md` (Arquitetura de dados, Propriedade do dado, Fonte de verdade, Regime de consistência)
- Modify: `docs/referencia/bibliografia.md` (Kleppmann, Dehghani, se conferidos)

**Interfaces:**
- Consumes: âncora `#exercicio-13` da Task 3, Lovatt seção 2.5 (linhas 1225 a 1355)
- Produces: âncora `bloco-2-arquitetura-de-dados.md#exercicio-14`, produto com o dono de cada entidade, consumido pelo exercício 15

- [ ] **Step 1: Rodar os testes do bloco e confirmar a falha**

Run: `python3 -m unittest tests.test_modulo_4_contract -k block_2 -k exercise_14 -v`
Expected: FAIL.

- [ ] **Step 2: Conferir as fontes complementares**

Conferir no catálogo da O'Reilly Media o título, o ano e a editora de Kleppmann, *Designing data-intensive applications* (2017), e de Dehghani, *Data mesh: Delivering data-driven value at scale* (2022). Fonte confirmada entra na bibliografia em APA 7. Fonte não confirmada sai do texto do bloco e da tupla de `test_bibliography_lists_the_verified_sources` em `tests/test_modulo_4_contract.py`.

- [ ] **Step 3: Acrescentar as entradas ao glossário**

- `## Arquitetura de dados`: subdomínio da arquitetura corporativa que trata dos dados, metadados e informação da organização, e ao qual a arquitetura de dados de cada solução precisa ser consistente.
- `## Propriedade do dado`: atribuição de uma entidade de dado a um único responsável, que a grava, enquanto os demais a leem por interface ou a recebem por evento.
- `## Fonte de verdade`: local onde uma entidade de dado é registrada e mantida com autoridade, do qual as demais cópias derivam.
- `## Regime de consistência`: garantia declarada sobre quando uma cópia reflete a fonte de verdade, forte quando reflete imediatamente, eventual quando reflete dentro de um prazo declarado.

- [ ] **Step 4: Escrever a página**

1. `# Arquitetura de dados da solução`
2. Linha de enquadramento: o bloco identifica os dados que sustentam a mudança localizada no bloco 1 e atribui a cada um dono e regime de consistência.
3. `## Antes de começar`: links para `arquitetura-de-dados`, `propriedade-do-dado`, `fonte-de-verdade`, `regime-de-consistencia` e para o exercício 13.
4. Seção de conceito `## Dados na solução`:
   - Arquitetura de dados como subdomínio e a exigência de consistência com a arquitetura corporativa (Lovatt, 2021, seção 2.5), com o caso da produtora de vídeo, em que cliente e autor têm definições inconsistentes e a mudança de contato é registrada em um só deles.
   - `### Dado, informação e metadado`: as definições da ISO/IEC 2382 citadas por Lovatt, em tradução, e a escolha do livro de reunir dado e informação numa única arquitetura.
   - `### Objetivos, atividades e artefatos`: lista dos objetivos e dos artefatos de 2.5.1 a 2.5.3, com destaque para a grade que cruza entidade de dado com aplicação e serve à análise de impacto.
   - `### Entidade, generalização e especialização`: os três exemplos do Hospital Vale do Pousio, entidades paciente, convite, clínica, consulta e profissional de saúde, generalização em pessoa, especialização em enfermeiro especialista e médico.
   - `### Fonte de verdade e regime de consistência`: definição de fonte de verdade e cópia derivada, com Kleppmann (2017) se conferido, e os dois regimes, forte e eventual com prazo declarado.
   - `### Propriedade do dado`: um responsável grava, os demais leem por interface ou recebem por evento. O banco compartilhado entre aplicações como antipadrão de integração, com o custo descrito em termos de acoplamento entre equipes e entre esquemas. Dehghani (2022), se conferido, como fonte da propriedade por domínio, em uma frase.
   - Figura `modulo-4-grade-dado-aplicacao.svg` com legenda `*Figura 1 — Grade dado × aplicação com dono, consumidores e regime de consistência. Fonte: material do curso, com base em Lovatt (2021, seção 2.5.3).*`
5. `## Uso pelo arquiteto`: a grade localiza o impacto de mudar uma entidade e revela entidades sem dono ou com mais de um.
6. `## Exercício 14`: contexto da ACME, link para `bloco-1-arquitetura-de-negocio.md#exercicio-13`, reprodução dos 2.300 pontos de acesso direto e da tabela de lotes noturnos de `../caso-acme/linha-de-base.md`. Artefato fornecido: grade com as linhas aluno, matrícula, nota, lançamento financeiro e turma, as colunas núcleo transacional, portais Java, ERP financeiro, ambiente virtual de aprendizagem e data warehouse, e em cada célula o uso atual (lê, grava, recebe por lote), sem coluna de dono. Perguntas: marcar o dono de cada entidade, marcar o regime de consistência exigido por consumidor, forte ou eventual com prazo, indicar qual capacidade marcada como afetada no exercício 13 depende de cada entidade, e responder em até três linhas por que os 2.300 acessos diretos contrariam a propriedade do dado.
7. `## Fontes`: Lovatt (2021) seção 2.5, as fontes complementares conferidas e a nota sobre o Hospital Vale do Pousio.

- [ ] **Step 5: Desenhar o visual**

`modulo-4-grade-dado-aplicacao.svg`: grade genérica com entidades Cliente, Pedido e Fatura nas linhas e três aplicações genéricas nas colunas, uma coluna de dono destacada e uma coluna de regime com forte e eventual de 5 min, no mesmo padrão visual da Task 3.

- [ ] **Step 6: Rodar testes e validador**

Run: `python3 -m unittest tests.test_modulo_4_contract -k block_2 -k exercise_14 -v && python3 scripts/validate_content.py --module modulo-4-dominios-da-solucao`
Expected: PASS e nenhuma violação em `bloco-2-arquitetura-de-dados.md`.

- [ ] **Step 7: Commit**

```bash
git add docs/modulo-4-dominios-da-solucao/bloco-2-arquitetura-de-dados.md docs/assets/images/modulo-4-grade-dado-aplicacao.svg docs/referencia/glossario.md docs/referencia/bibliografia.md
git commit -m "feat(aula-4): escreve o bloco de arquitetura de dados"
```

---

### Task 5: Bloco 3, arquitetura de aplicações e integração

**Files:**
- Modify: `docs/modulo-4-dominios-da-solucao/bloco-3-arquitetura-de-aplicacoes-e-integracao.md`
- Modify: `docs/modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md` (retirada da introdução do C4 e do nível de contexto, que passam ao bloco 3)
- Create: `docs/assets/images/modulo-4-servicos-e-contrato.svg`
- Modify: `docs/referencia/glossario.md` (Arquitetura de aplicações, Padrão técnico, Protocolo, Especificação de interface, Contrato de integração)
- Modify: `docs/referencia/bibliografia.md` (RFC 9110, OpenAPI, AsyncAPI, Portal da NF-e, se conferidos)

**Interfaces:**
- Consumes: âncora `#exercicio-14` da Task 4, Lovatt seções 2.6, 2.8, 3.6.4 e 4.3.1, conteúdo do C4 no arquivo do bloco 4
- Produces: âncora `bloco-3-arquitetura-de-aplicacoes-e-integracao.md#exercicio-15`, com o diagrama de contexto corrigido, consumido pelo exercício 16

- [ ] **Step 1: Rodar os testes do bloco e confirmar a falha**

Run: `python3 -m unittest tests.test_modulo_4_contract -k block_3 -k exercise_15 -v`
Expected: FAIL.

- [ ] **Step 2: Conferir as fontes complementares**

Conferir na origem: RFC 9110 em rfc-editor.org (título *HTTP Semantics*, junho de 2022, autores Fielding, Nottingham e Reschke), a versão vigente da especificação OpenAPI em spec.openapis.org, a versão vigente da AsyncAPI em asyncapi.com e, no Portal da Nota Fiscal Eletrônica em nfe.fazenda.gov.br, a existência do manual de orientação do contribuinte, do esquema XSD e do transporte por serviço web. Fonte confirmada entra em APA 7 na bibliografia. Fonte não confirmada sai do texto e da tupla de `test_bibliography_lists_the_verified_sources` em `tests/test_modulo_4_contract.py`.

- [ ] **Step 3: Acrescentar as entradas ao glossário**

- `## Arquitetura de aplicações`: subdomínio da arquitetura corporativa que mantém a visão do portfólio de aplicações e dos serviços que elas oferecem, ligando arquitetura de negócio e arquitetura de dados.
- `## Padrão técnico`: especificação adotada pela organização que fixa processo, documentação, regras e parâmetros a observar, correspondente ao termo inglês *standard* e distinta do padrão arquitetural ou de design, correspondente a *pattern*.
- `## Protocolo`: conjunto de regras que duas partes seguem para trocar mensagens, com formato, sequência e tratamento de erro definidos.
- `## Especificação de interface`: descrição verificável de uma interface particular, com operações, mensagens, esquemas e erros.
- `## Contrato de integração`: especificação de interface somada às garantias acordadas entre provedor e consumidor, como versão, garantia de entrega, idempotência e nível de serviço.

- [ ] **Step 4: Escrever a página**

1. `# Arquitetura de aplicações e integração`
2. Linha de enquadramento: o bloco identifica as aplicações e interfaces que realizam a mudança, especifica o contrato de uma integração e representa a fronteira da solução no diagrama de contexto.
3. `## Antes de começar`: links para `arquitetura-de-aplicacoes`, `padrao-tecnico`, `contrato-de-integracao`, `modelo-c4` e para o exercício 14.
4. Seção de conceito `## Aplicações, interfaces e contexto`:
   - `### Portfólio de aplicações`: aplicação e componente de aplicação, hierarquia de serviços da figura 2.4 de Lovatt, catálogo do portfólio, classificação em vermelho, âmbar e verde, tipos de aplicação com os exemplos do Hospital Vale do Pousio, catálogo de interfaces e grades de referência cruzada. Uma frase sobre arquitetura de software como responsável pelas interfaces internas e externas (Lovatt, 2021, seção 2.8).
   - `### Descrição de uma interface`: os seis atributos de Lovatt (2021, seção 3.6.4) em tabela com os rótulos exatos Origem, Destino, Gatilho, Itens trocados, Sequência e Pré e pós-condições, e o catálogo de interfaces da solução como produto.
   - `### Padrão técnico, protocolo, especificação e contrato`: parágrafo de desambiguação com *standard* e *pattern*, definição de **padrão técnico** pela seção 4.3.1, protocolo com LDAP, HTTPS e conector transacional e o RFC 9110, especificação com um trecho curto de OpenAPI e um de AsyncAPI em bloco de código, **contrato de integração** como especificação somada às garantias. Exemplo da nota fiscal eletrônica separando padrão nacional, transporte por serviço web e esquema XSD, conforme conferido no Step 2.
   - `### Estrutura de um contrato`: tabela com os seis atributos de Lovatt e as extensões protocolo, formato e esquema, semântica de erro, versionamento e compatibilidade, garantia de entrega e idempotência, e nível de serviço. Parágrafo sobre síncrono e assíncrono ligado a Transactional Outbox, Retry com limite e Circuit Breaker, com link para `../modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md`.
   - Figura `modulo-4-servicos-e-contrato.svg` com legenda `*Figura 1 — Hierarquia de serviços e camadas do contrato de integração. Fonte: material do curso, com base em Lovatt (2021, seções 2.6 e 3.6.4).*`
   - `### Modelo C4 e diagrama de contexto`: transferir do arquivo do bloco 4 os parágrafos de diagrama solto e modelo, a definição do modelo C4, a figura `c4-quatro-niveis.png`, a tabela de níveis, os três princípios, a seção do nível 1 com a figura `c4-exemplo-contexto.png` e o roteiro de cinco etapas, e o primeiro diagrama Mermaid do agendamento odontológico. Ajustar a frase de escopo para dizer que esta aula cobre contexto neste bloco e contêineres no bloco 4.
5. `## Uso pelo arquiteto`: contrato escrito antes da implementação permite que provedor e consumidor evoluam em separado, e o diagrama de contexto é a visão para quem decide escopo e relação com terceiros.
6. `## Exercício 15`: contexto da ACME e link para `bloco-2-arquitetura-de-dados.md#exercicio-14`. Três artefatos fornecidos:
   - Catálogo com Portal do Aluno, Portal do Professor, Portal da Secretaria, Portal do Gestor, núcleo transacional COBOL, ERP financeiro, ambiente virtual de aprendizagem, data warehouse institucional, assinador digital e diretório corporativo, com ano, tecnologia e observação retirados da linha de base. Pergunta: classificar cada aplicação em vermelho, âmbar ou verde, com uma linha de justificativa.
   - Esqueleto do contrato da integração de notas, tabela com as linhas Origem, Destino, Gatilho, Itens trocados, Sequência, Pré e pós-condições, Protocolo, Formato e esquema, Semântica de erro, Versionamento, Garantia de entrega e idempotência, Nível de serviço, e coluna de resposta em branco. O enunciado reproduz R7, a exportação de notas das 05h10 e o acréscimo de 38% no contrato do ambiente virtual. Pergunta: preencher cada campo com resposta curta, declarar o modo síncrono ou assíncrono, o tratamento de nota corrigida, e usar como origem o dono da entidade nota marcado no exercício 14.
   - Diagrama de contexto da arquitetura alvo em Mermaid com dois erros de nível: o banco de dados acadêmico aparece como caixa ao lado do sistema acadêmico, e o ERP financeiro aparece dentro da fronteira do sistema. Pergunta: apontar e corrigir os dois erros. O enunciado não diz quais são os elementos errados.
7. `## Fontes`: Lovatt (2021) seções 2.6, 2.8, 3.6.4 e 4.3.1, Brown (n.d.), Mendes (2026b) com as figuras transferidas, as fontes conferidas no Step 2, e a nota sobre o Hospital Vale do Pousio.

- [ ] **Step 5: Retirar do bloco 4 o conteúdo transferido**

Remover de `bloco-4-arquitetura-de-infraestrutura.md` tudo o que foi transferido no Step 4, mantendo nível 2, o segundo Mermaid, o internet banking e a discussão da fronteira do mainframe para a Task 6.

- [ ] **Step 6: Desenhar o visual**

`modulo-4-servicos-e-contrato.svg`: à esquerda, a pilha serviço de negócio, processo, serviço de aplicação, componente de aplicação e serviço de tecnologia. À direita, quatro camadas concêntricas ou empilhadas, padrão técnico, protocolo, especificação e contrato, com os seis atributos de interface listados na camada de especificação.

- [ ] **Step 7: Rodar testes e validador**

Run: `python3 -m unittest tests.test_modulo_4_contract -k block_3 -k exercise_15 -v && python3 scripts/validate_content.py --module modulo-4-dominios-da-solucao`
Expected: PASS e nenhuma violação em `bloco-3-arquitetura-de-aplicacoes-e-integracao.md`.

- [ ] **Step 8: Commit**

```bash
git add docs/modulo-4-dominios-da-solucao/ docs/assets/images/modulo-4-servicos-e-contrato.svg docs/referencia/glossario.md docs/referencia/bibliografia.md
git commit -m "feat(aula-4): escreve o bloco de aplicacoes e integracao"
```

---

### Task 6: Bloco 4, arquitetura de infraestrutura

**Files:**
- Modify: `docs/modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md`
- Create: `docs/assets/images/modulo-4-solucao-como-grafo.svg`
- Modify: `docs/referencia/glossario.md` (Arquitetura de infraestrutura)

**Interfaces:**
- Consumes: âncora `#exercicio-15` da Task 5, Lovatt seções 2.7 (linhas 1416 a 1478) e 7.5 (linhas 5548 a 5592)
- Produces: âncora `bloco-4-arquitetura-de-infraestrutura.md#exercicio-16`

- [ ] **Step 1: Rodar os testes do bloco e confirmar a falha**

Run: `python3 -m unittest tests.test_modulo_4_contract -k block_4 -k exercise_16 -v`
Expected: FAIL.

- [ ] **Step 2: Acrescentar a entrada ao glossário**

- `## Arquitetura de infraestrutura`: arquitetura dos componentes e serviços tecnológicos que sustentam as atividades da organização, chamada de arquitetura de tecnologia no TOGAF.

- [ ] **Step 3: Reescrever a página**

1. `# Arquitetura de infraestrutura da solução`
2. Linha de enquadramento: o bloco fecha o detalhamento por domínios situando onde a solução executa e o que cada interface exige, sem escolher produto.
3. `## Antes de começar`: links para `arquitetura-de-infraestrutura`, `modelo-c4`, `bloco-de-construcao-da-solucao` e para o exercício 15.
4. Seção de conceito `## Infraestrutura e contêineres`:
   - `### Infraestrutura na solução`: definição de **arquitetura de infraestrutura** (Lovatt, 2021, seção 2.7), objetivos de eficácia e eficiência, relação com a solução pelos requisitos não funcionais, lista dos artefatos de 2.7.2 em uma frase, com a remissão de que o modelo técnico de referência e a definição tecnológica são tratados na Aula 5.
   - `### A solução como grafo`: blocos de construção como vértices, interfaces como arestas, cálculo do número de interfaces pela soma dos graus dividida por dois, e o exame de cada interface pelo tipo e pelo volume de tráfego (Lovatt, 2021, seção 7.5). Exemplo numérico genérico com cinco blocos.
   - Figura `modulo-4-solucao-como-grafo.svg` com legenda `*Figura 1 — Solução como grafo de blocos de construção e interfaces. Fonte: material do curso, com base em Lovatt (2021, seção 7.5).*`
   - `### Diagrama de contêineres`: conteúdo preservado do nível 2, com a figura `c4-exemplo-conteineres.png`, o roteiro de quatro etapas, o Mermaid de contêineres do agendamento odontológico e a nota de coerência dos sistemas externos.
   - `### Tecnologia no contêiner antes da definição tecnológica`: o C4 pede tecnologia declarada no contêiner, e na arquitetura alvo da Aula 4 o rótulo é "tecnologia a definir na Aula 5", porque a escolha de produto depende da plataforma.
   - `### Um exemplo completo nos dois níveis`: internet banking e fronteira do mainframe, preservados.
5. `## Uso pelo arquiteto`: conteúdo preservado sobre escolha do nível pela audiência e o erro simétrico.
6. `## Exercício 16`: frase padrão, contexto da ACME, link para `bloco-3-arquitetura-de-aplicacoes-e-integracao.md#exercicio-15`, reprodução dos volumes e da sazonalidade de `../caso-acme/dados-operacionais.md` (5.800 sessões simultâneas na abertura da matrícula, 4.800 lançamentos de nota em dia comum e até 360.000 na janela de fechamento). Artefato fornecido: diagrama de contêineres em Mermaid com Portal do Aluno, Portal do Professor, serviço de matrícula, serviço de notas, núcleo transacional COBOL encapsulado, banco acadêmico, ERP financeiro e ambiente virtual de aprendizagem, cada contêiner com "tecnologia a definir na Aula 5" e as relações sem rótulo. Perguntas: rotular cada relação com síncrono ou assíncrono, volume e latência exigidos, e responder em uma frase por que o núcleo COBOL permanece como contêiner.
7. `## Fontes`: Lovatt (2021) seções 2.7 e 7.5, Brown (n.d.) e Mendes (2026b).

- [ ] **Step 4: Desenhar o visual**

`modulo-4-solucao-como-grafo.svg`: cinco vértices rotulados BC1 a BC5 ligados por seis arestas, cada vértice com o grau anotado, e a conta soma dos graus 12 dividida por 2 igual a 6 interfaces, mais uma aresta destacada com os rótulos tipo e volume.

- [ ] **Step 5: Rodar testes e validador**

Run: `python3 -m unittest tests.test_modulo_4_contract -k block_4 -k exercise_16 -v && python3 scripts/validate_content.py --module modulo-4-dominios-da-solucao`
Expected: PASS e nenhuma violação em `bloco-4-arquitetura-de-infraestrutura.md`.

- [ ] **Step 6: Commit**

```bash
git add docs/modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md docs/assets/images/modulo-4-solucao-como-grafo.svg docs/referencia/glossario.md
git commit -m "feat(aula-4): escreve o bloco de arquitetura de infraestrutura"
```

---

### Task 7: Índice, síntese e gabaritos

**Files:**
- Modify: `docs/modulo-4-dominios-da-solucao/index.md`
- Modify: `docs/modulo-4-dominios-da-solucao/sintese.md`
- Modify: `~/pka/projects/aulas/PRJ-aulas-iec-projeto-e-inovacao-em-arquitetura-de-solucoes.md` (fora do repositório)

**Interfaces:**
- Consumes: páginas das Tasks 3 a 6
- Produces: nenhum

- [ ] **Step 1: Rodar os testes e confirmar a falha**

Run: `python3 -m unittest tests.test_modulo_4_contract -k index -k synthesis -v`
Expected: FAIL.

- [ ] **Step 2: Escrever o índice**

Seções na ordem: `# Aula 4, domínios da arquitetura de solução`, parágrafo de abertura, `## Objetivos de aprendizagem` com os seis objetivos da seção 1 do spec, `## Grade de tempo` no formato da Aula 3 com Questões sobre a Aula 3 e Kahoot de revisão da Aula 3 e os quatro blocos com os nomes do cronograma, `## Entrada recebida das Aulas 2 e 3` com os exercícios 8, 9, 11 e 12 ligados, `## Roteiro da aula` com um parágrafo por bloco e a síntese, `## Preparação para a Aula 5` dizendo que a Aula 5 converte os contêineres em tecnologia e avalia a segurança fim a fim.

- [ ] **Step 3: Escrever a síntese**

Seções: linha de abertura, `## Checklist do que precisa permanecer`, `## Cadeia dos domínios` com negócio, dados, aplicações e infraestrutura e o produto de cada exercício, `## Autoavaliação` com cinco perguntas sem gabarito, `## Fontes da aula` com todas as referências dos quatro blocos.

- [ ] **Step 4: Registrar os gabaritos no PKA**

Acrescentar `## Gabaritos dos exercícios da Aula 4` depois da seção de gabaritos da Aula 3, com `### Exercício 13` a `### Exercício 16`, no formato existente: resposta de referência, distinção entre resposta excelente, aceitável e fraca, e critério de correção.

- [ ] **Step 5: Rodar testes e validador**

Run: `python3 -m unittest tests.test_modulo_4_contract -v && python3 scripts/validate_content.py`
Expected: todos os testes do módulo em PASS e zero violação.

- [ ] **Step 6: Commit**

```bash
git add docs/modulo-4-dominios-da-solucao/index.md docs/modulo-4-dominios-da-solucao/sintese.md
git commit -m "feat(aula-4): escreve indice e sintese do modulo"
```

---

### Task 8: Verificação integral

**Files:**
- Correções pontuais onde a verificação apontar.

**Interfaces:**
- Consumes: todas as tarefas anteriores
- Produces: evidência de aceite para os critérios da seção 15 do spec

- [ ] **Step 1: Suíte e validador**

Run: `python3 -m unittest discover -s tests -v && python3 scripts/validate_content.py`
Expected: todos os testes em OK e zero violação. Falhas preexistentes ligadas ao CSS sem commit são registradas e não corrigidas.

- [ ] **Step 2: Build estrito**

Run: `.venv/bin/mkdocs build --strict`
Expected: build sem aviso nem erro.

- [ ] **Step 3: Inspeção visual**

Gerar miniaturas dos quatro SVG com `qlmanage -t -s 1200 -o <scratchpad> docs/assets/images/modulo-4-*.svg` e ler cada PNG, conferindo legibilidade, sobreposição de texto e ausência de dado do caso. Se houver navegador sem interface, capturar as seis páginas servidas por `.venv/bin/mkdocs serve`. Se não houver, registrar no relatório final que a inspeção das páginas renderizadas não foi feita e que só os SVG e o HTML gerado em `site/` foram conferidos.

- [ ] **Step 4: Leitura editorial**

Reler as seis páginas contra as restrições globais, em especial a regra dos exercícios, a ausência de resposta nos artefatos fornecidos e o negrito entre três e cinco por página.

- [ ] **Step 5: Commit das correções**

```bash
git add docs tests
git commit -m "fix(aula-4): corrige apontamentos da verificacao integral"
```
