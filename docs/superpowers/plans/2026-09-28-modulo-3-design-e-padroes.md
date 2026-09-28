# Aula 3, princípios de design, padrões e decisões

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Concluir a Aula 3 do site, com os blocos 1 e 3 novos, os blocos 2 e 4 harmonizados, índice ampliado, síntese nova, quatro visuais e a cadeia de exercícios 9 a 12.

**Architecture:** Cada página de bloco segue a anatomia de sete seções já verificada por `scripts/validate_content.py`. Um arquivo de teste novo, `tests/test_modulo_3_contract.py`, fixa antes da escrita os contratos que o validador genérico não cobre: cadeia de exercícios, taxonomia, repertórios, visuais e referências. Os visuais são SVG escritos à mão no padrão de `docs/assets/images/modulo-1-granularidade-arquitetural.svg`, com exemplos genéricos e sem dado da ACME.

**Tech Stack:** Python 3, unittest, MkDocs Material 1.6 em `.venv`, SVG estático, Markdown com `attr_list` e `md_in_html`.

**Spec:** `docs/superpowers/specs/2026-09-28-modulo-3-design-e-padroes-design.md`

## Global Constraints

- Anatomia de página de bloco, na ordem: título funcional, linha de enquadramento, `## Antes de começar`, seção de conceito com título livre, `## Uso pelo arquiteto`, `## Exercício N`, `## Fontes`.
- Exercícios numerados 9, 10, 11 e 12, um por bloco, na ordem dos blocos.
- Zero ponto-e-vírgula em texto corrido, no máximo um travessão por parágrafo fora de `## Fontes`, nenhum título abrindo com "Por que", nenhum título com subtítulo após travessão, nenhuma ocorrência da palavra "prosa".
- Negrito entre três e cinco ocorrências por página, só na seção de conceito, no primeiro uso do termo, nunca em frase inteira ou número.
- Definição antes do exemplo. Exemplos principais em domínios distintos, sem repetir o domínio principal do bloco imediatamente anterior ou seguinte. Alocação: bloco 1, rede de clínicas e serviço público municipal de licenciamento. Bloco 2, os domínios já publicados (estoque industrial, streaming de música, companhia aérea, crédito, energia, telecomunicações). Bloco 3, varejo online e transportadora de cargas. Bloco 4, o exemplo já publicado de infraestrutura com Kubernetes.
- A ACME aparece no exercício e nos trechos explicitamente marcados como aplicação. Todo dado da ACME usado no exercício é reproduzido na própria página ou apontado com link e âncora exatos.
- Nenhum gabarito, resposta fechada ou critério de correção no site. Os gabaritos dos exercícios 9 a 12 vão para `~/pka/projects/aulas/PRJ-aulas-iec-projeto-e-inovacao-em-arquitetura-de-solucoes.md`, em seção nova `## Gabaritos dos exercícios da Aula 3`.
- Termo do glossário ligado no primeiro uso. Fonte em APA 7, citação narrativa (Sobrenome, ano), bloco de Fontes no padrão das páginas existentes, e toda fonte nova acrescentada a `docs/referencia/bibliografia.md` somente depois de conferida em fonte primária ou catálogo de editora.
- Registro sóbrio e impessoal, português brasileiro com acentuação completa, sem neologismo de raiz inglesa, sem metáfora, sem frase de efeito no fim de parágrafo, média de pelo menos 14 palavras por frase.
- Datas visíveis no formato DD/MM/AAAA. Índice e cronograma sem data real de calendário.
- Visuais do módulo 3 com nome `modulo-3-*.svg`, `<title>` e `<desc>` preenchidos, marcados com `{ .module-diagram }`, sem os termos "ACME", "COBOL", "CICS" ou "matrícula".

## Review Focus

- Leitor que chega ao bloco 2 sem ter feito o exercício 9: o exercício 10 precisa oferecer princípios de referência ou um caminho explícito para quem não os tem, como já faz com os cenários. Teste: o enunciado do exercício 10 contém um link para `bloco-1-principios-de-design.md#exercicio-9`.
- Leitor que confunde Strangler Fig com estilo: nenhuma frase do bloco 2 ou do bloco 3 pode chamá-lo de estilo. Teste: o texto dos blocos 2 e 3 não contém "estilo Strangler" nem "estilo estrangulador".
- Visual que entrega a resposta: um visual com a sequência de padrões escolhida para a ACME resolveria o exercício 11. Teste: os quatro SVG não contêm os termos proibidos listados nas restrições globais.
- Frase de enquadramento herdada da organização antiga: o bloco 2 dizia "fecha a aula" e o bloco 4 dizia "abre a aula". Teste: nenhuma página do módulo contém "fecha a aula" ou "abre a aula".
- Link para âncora gerada por título alterado: a reescrita do bloco 2 muda títulos, e o bloco 4 e o exercício 11 apontam para eles. Controle: o validador já checa âncoras, e a Task 7 roda o validador completo e o build estrito.

---

### Task 1: Contrato de conteúdo do módulo 3 e navegação

**Files:**
- Create: `tests/test_modulo_3_contract.py`
- Modify: `mkdocs.yml` (item de nav da Aula 3)
- Create: `docs/modulo-3-design-e-padroes/bloco-1-principios-de-design.md` (esqueleto)
- Create: `docs/modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md` (esqueleto)
- Create: `docs/modulo-3-design-e-padroes/sintese.md` (esqueleto)

**Interfaces:**
- Consumes: nenhum
- Produces: os nomes de arquivo e de imagem que as tarefas seguintes precisam usar sem variação:
  - `bloco-1-principios-de-design.md` com `modulo-3-principios-ao-desenho-logico.svg`
  - `bloco-2-estilos-arquiteturais.md` com `modulo-3-estilos-forcas-compromissos.svg`
  - `bloco-3-padroes-arquiteturais-e-de-design.md` com `modulo-3-niveis-de-padrao.svg`
  - `bloco-4-registro-de-decisao-arquitetural.md` com `modulo-3-ciclo-de-vida-adr.svg`
  - glossário com as âncoras `principio-de-design`, `desenho-conceitual`, `desenho-logico`, `padrao-arquitetural`, `padrao-de-design`

- [ ] **Step 1: Escrever o teste de contrato**

```python
"""Contrato de conteudo da Aula 3, que o validador generico nao cobre."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MODULE = DOCS / "modulo-3-design-e-padroes"
IMAGES = DOCS / "assets" / "images"

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
    def test_all_pages_exist_and_are_in_nav(self):
        nav = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        for name in ("index.md", *BLOCKS, "sintese.md"):
            with self.subTest(page=name):
                self.assertTrue((MODULE / name).is_file())
                self.assertIn(f"modulo-3-design-e-padroes/{name}", nav)

    def test_each_block_has_its_numbered_exercise(self):
        for name, (_, number) in BLOCKS.items():
            with self.subTest(page=name):
                self.assertRegex(read(name), rf"^## Exercício {number}\s*$")

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
                self.assertRegex(text, rf"^## {heading}\s*$")
        for name in (*BLOCKS, "sintese.md"):
            self.assertIn(f"({name})", text)

    def test_synthesis_has_checklist_chain_self_assessment_and_sources(self):
        text = read("sintese.md")
        for heading in ("Checklist do que precisa permanecer",
                        "Cadeia da decisão", "Autoavaliação", "Fontes da aula"):
            with self.subTest(heading=heading):
                self.assertRegex(text, rf"^## {heading}\s*$")
        chain = section(text, "Cadeia da decisão")
        for term in ("objetivo", "requisito", "princípio", "estilo", "padrão", "decisão"):
            self.assertIn(term, chain.lower())

    def test_glossary_defines_the_new_terms(self):
        text = (DOCS / "referencia" / "glossario.md").read_text(encoding="utf-8")
        for heading in ("Princípio de design", "Desenho conceitual", "Desenho lógico",
                        "Padrão arquitetural", "Padrão de design"):
            with self.subTest(heading=heading):
                self.assertRegex(text, rf"^## {heading}\s*$")

    def test_bibliography_lists_the_new_sources(self):
        text = (DOCS / "referencia" / "bibliografia.md").read_text(encoding="utf-8")
        for author in ("Gamma, E.", "Evans, E.", "Fowler, M.", "Richardson, C.",
                       "Nygard, M. T. (2018)", "The Open Group"):
            with self.subTest(author=author):
                self.assertIn(author, text)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Rodar o teste e confirmar a falha**

Run: `python3 -m unittest tests.test_modulo_3_contract -v`
Expected: FAIL em quase todos os testes, porque as páginas novas, os visuais, as entradas de glossário e a navegação ainda não existem.

- [ ] **Step 3: Atualizar a navegação**

Em `mkdocs.yml`, substituir o item da Aula 3 por:

```yaml
  - "Aula 3, princípios de design e padrões":
      - Visão geral: modulo-3-design-e-padroes/index.md
      - "Bloco 1: princípios de design": modulo-3-design-e-padroes/bloco-1-principios-de-design.md
      - "Bloco 2: estilos arquiteturais": modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md
      - "Bloco 3: padrões arquiteturais e de design": modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md
      - "Bloco 4: registro de decisão arquitetural": modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md
      - Síntese: modulo-3-design-e-padroes/sintese.md
```

- [ ] **Step 4: Criar os três esqueletos**

```bash
printf '# Princípios de design e passagem ao desenho lógico\n' > docs/modulo-3-design-e-padroes/bloco-1-principios-de-design.md
printf '# Padrões arquiteturais e padrões de design\n' > docs/modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md
printf '# Síntese da Aula 3\n' > docs/modulo-3-design-e-padroes/sintese.md
```

- [ ] **Step 5: Rodar o teste de navegação**

Run: `python3 -m unittest tests.test_modulo_3_contract.ModuleThreeStructureTest.test_all_pages_exist_and_are_in_nav -v`
Expected: PASS. Os demais testes do arquivo continuam falhando até as tarefas seguintes.

- [ ] **Step 6: Commit**

```bash
git add tests/test_modulo_3_contract.py mkdocs.yml docs/modulo-3-design-e-padroes/
git commit -m "test(aula-3): fixa o contrato de conteudo do modulo"
```

---

### Task 2: Bloco 1, princípios de design e passagem ao lógico

**Files:**
- Modify: `docs/modulo-3-design-e-padroes/bloco-1-principios-de-design.md`
- Create: `docs/assets/images/modulo-3-principios-ao-desenho-logico.svg`
- Modify: `docs/referencia/glossario.md` (entradas Princípio de design, Desenho conceitual, Desenho lógico)
- Modify: `docs/referencia/bibliografia.md` (The Open Group, se conferida)

**Interfaces:**
- Consumes: esqueleto e contrato da Task 1
- Produces: âncora `bloco-1-principios-de-design.md#exercicio-9`, produto do exercício 9 com os campos nome, motivação, implicação no desenho e evidência esperada, consumido pelos exercícios 10 e 12

- [ ] **Step 1: Rodar os testes do bloco e confirmar a falha**

Run: `python3 -m unittest tests.test_modulo_3_contract -k block_1 -k exercise_9 -v`
Expected: FAIL.

- [ ] **Step 2: Acrescentar as três entradas ao glossário**

Inserir depois de `## Estilo arquitetural`, no formato de uma definição de um parágrafo:

- `## Princípio de design`: regra durável, derivada de objetivos, requisitos e restrições, que orienta um conjunto de decisões de desenho e admite verificação da sua aplicação.
- `## Desenho conceitual`: descrição da solução em termos de capacidades, responsabilidades e relações com o ambiente, sem estrutura interna nem tecnologia.
- `## Desenho lógico`: descrição da solução em elementos lógicos com responsabilidade, interfaces e fluxos declarados, ainda sem produto, linguagem ou plataforma.

- [ ] **Step 3: Escrever a página**

Estrutura obrigatória:

1. `# Princípios de design e passagem ao desenho lógico`
2. Linha de enquadramento: o bloco abre a cadeia de decisão da aula e responde que regras devem orientar o desenho antes de qualquer escolha de estilo ou tecnologia.
3. `## Antes de começar`: links para `principio-de-design`, `desenho-conceitual`, `desenho-logico`, `requisito-de-atributo-de-qualidade` e `restricao` no glossário.
4. `## Princípios de design` (título livre da seção de conceito), com as subseções:
   - Parágrafo de abertura que situa o bloco depois da Aula 2: requisitos, cenários e restrições já existem, e o desenho ainda não.
   - `### Do objetivo ao elemento lógico`: tabela de cinco linhas, Conceito e Papel, exatamente com Objetivo, Requisito, Princípio, Decisão e Elemento lógico, com os papéis da seção 4.2 do spec. Um parágrafo com exemplo da rede de clínicas mostra os cinco conceitos encadeados (objetivo de reduzir falta em consulta, requisito de lembrete com confirmação, princípio, decisão, elemento lógico de agendamento).
   - `### Anatomia de um princípio`: definição de **princípio de design**, seguida da regra de que um princípio só conta quando tem motivação, implicação prática e forma de verificar. Parágrafo explícito dizendo que uma lista genérica de princípios, copiada sem motivação, não constitui arquitetura. Citar o formato de princípio de arquitetura do TOGAF (nome, declaração, racional, implicações), atribuído a The Open Group (2022) somente se a Task 2 Step 6 conferir a fonte.
   - `### Repertório de princípios`: tabela com os nove princípios nas colunas Princípio, Motivação típica, Implicação no desenho e Evidência de aplicação, com nomes exatos: Simplicidade, Separação de responsabilidades, Baixo acoplamento, Alta coesão, Encapsulamento, Desenho para falha, Observabilidade, Segurança por desenho, Evolução incremental. Um parágrafo sobre conflito entre princípios, com exemplo do serviço municipal de licenciamento (simplicidade contra desenho para falha), declarando que a priorização é parte do produto.
   - `### Do conceitual ao lógico`: definição de **desenho conceitual** e **desenho lógico**, lista numerada dos cinco passos da seção 4.2 do spec, e um exemplo aplicado no serviço municipal de licenciamento que percorre os cinco passos sem nomear produto, linguagem, nuvem ou framework.
   - Figura: `<figure markdown="span">` com `![...](../assets/images/modulo-3-principios-ao-desenho-logico.svg){ .module-diagram }`, texto alternativo com pelo menos 40 caracteres descrevendo a cadeia, e legenda em itálico `*Figura 1 — ... Fonte: material do curso.*`.
   - `### Aplicação à ACME`: um parágrafo que mostra como continuidade operacional, residência de dados, redução de dependência do legado e propagação de notas orientam responsabilidades lógicas, sem enunciar os princípios que o exercício pede.
5. `## Uso pelo arquiteto`: um parágrafo sobre usar princípios priorizados para decidir sem reabrir discussão a cada escolha e para revisar desenho de terceiros.
6. `## Exercício 9`: primeiro parágrafo com o contexto da ACME. Tabela das quatro entradas, reproduzidas do caso com a origem:
   - "O sistema acadêmico não pode parar em período letivo", Pró-Reitoria de Graduação
   - "Dado pessoal de aluno processado em território nacional", Jurídico, parecer de 28/04/2026
   - "Manutenção do núcleo COBOL sob contrato até 30/09/2027", com 6 especialistas, 2 aposentadorias previstas em 2027 e 1 profissional que domina a matrícula
   - "R7, a nota lançada pelo professor chega ao ambiente virtual de aprendizagem em até 10 minutos", contra o lote diário das 05h10
   Enunciado em lista numerada: (1) derivar de três a cinco princípios, cada um com nome, motivação, implicação no desenho e evidência esperada, (2) priorizar os princípios e justificar o primeiro lugar, (3) produzir um esboço lógico com os elementos lógicos e suas responsabilidades, sem nomear produto tecnológico, (4) marcar no esboço um risco e uma decisão pendente. Fechar com a frase de que o produto deste exercício é a entrada do exercício 10.
7. `## Fontes`: parágrafo padrão de APA e bibliografia, entradas com o trecho consultado entre parênteses, incluindo Lovatt (2021) (seções 2.2 e 3.7), Bass et al. (2021) e, se conferida, The Open Group (2022). Linha final `**Material do curso.**` com glossário e dossiê da ACME.

- [ ] **Step 4: Desenhar o visual**

`modulo-3-principios-ao-desenho-logico.svg`, `viewBox="0 0 1200 675"`, com `role="img"`, `aria-labelledby="title desc"`, paleta e fonte iguais a `modulo-1-granularidade-arquitetural.svg` (`#F2F6FB`, `#16243A`, `#254DB8`, `#5FC0D1`, `#F2B84B`). Conteúdo: faixa com Objetivo, Requisito e restrição, Princípio, Decisão e Elemento lógico ligados por setas, e abaixo os cinco passos do conceitual ao lógico, sem termo da lista proibida e sem princípio aplicado a caso concreto, porque o exercício 9 pede exatamente essa aplicação.

- [ ] **Step 5: Rodar testes e validador**

Run: `python3 -m unittest tests.test_modulo_3_contract -k block_1 -k exercise_9 -v && python3 scripts/validate_content.py --module modulo-3-design-e-padroes`
Expected: testes do bloco 1 em PASS. Validador sem violação em `bloco-1-principios-de-design.md`.

- [ ] **Step 6: Conferir e registrar a fonte TOGAF**

Conferir em opengroup.org o título e a edição do TOGAF Standard, 10ª edição (2022), e a parte que define princípios de arquitetura. Se confirmada, acrescentar à bibliografia `The Open Group. (2022). *The TOGAF standard* (10th ed.). The Open Group.` com o trecho no bloco de Fontes. Se a fonte não for confirmada, a citação sai do texto do bloco 1 e o teste `test_bibliography_lists_the_new_sources` deixa de exigir "The Open Group".

- [ ] **Step 7: Commit**

```bash
git add docs/modulo-3-design-e-padroes/bloco-1-principios-de-design.md docs/assets/images/modulo-3-principios-ao-desenho-logico.svg docs/referencia/glossario.md docs/referencia/bibliografia.md
git commit -m "feat(aula-3): escreve o bloco de principios de design"
```

---

### Task 3: Bloco 2, harmonização dos estilos arquiteturais

**Files:**
- Modify: `docs/modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md`
- Create: `docs/assets/images/modulo-3-estilos-forcas-compromissos.svg`

**Interfaces:**
- Consumes: âncora `bloco-1-principios-de-design.md#exercicio-9` e os nomes dos nove princípios da Task 2
- Produces: âncora `bloco-2-estilos-arquiteturais.md#exercicio-10`, com o estilo recomendado consumido pelos exercícios 11 e 12. Os títulos `### <estilo>` com os nomes exatos da constante `STYLES`

- [ ] **Step 1: Rodar os testes do bloco e confirmar a falha**

Run: `python3 -m unittest tests.test_modulo_3_contract -k block_2 -k exercise_10 -k old_framing -v`
Expected: FAIL.

- [ ] **Step 2: Reescrever a página preservando o conteúdo tecnicamente válido**

- Linha de enquadramento nova: o bloco recebe os princípios do bloco 1 e os cenários da Aula 2 e pergunta que organização estrutural os sustenta melhor. Remover "fecha a aula".
- `## Antes de começar`: acrescentar link para `principio-de-design`.
- Seção de conceito: manter a definição de estilo em três partes, a analogia da casa com a figura existente e o parágrafo de Ford e Richards. Manter o quadro comparativo de sete estilos e acrescentar a coluna "Princípios que tende a sustentar", com os nomes exatos do bloco 1, e um parágrafo de ligação com link para `bloco-1-principios-de-design.md`.
- Um `### <estilo>` por estilo, com os nomes exatos de `STYLES`. Cada seção contém o parágrafo de exemplo já publicado (mesmo domínio) e uma tabela de duas colunas, Aspecto e Descrição, com as linhas Forma estrutural, Componentes e comunicação, Favorece, Prejudica, Quando usar, Quando evitar, Anti-padrão e heurística de alerta. O conteúdo das tabelas de força e anti-padrão e das heurísticas existentes é transportado para essas linhas, sem perda de dado numérico (80% de repasse no sumidouro, dois ou três serviços na cadeia síncrona).
- Lei de Conway: manter uma única explicação, na seção de microsserviços, ligada à fronteira de equipe do exemplo da plataforma de streaming. Retirar as outras três menções.
- Figura nova `modulo-3-estilos-forcas-compromissos.svg` depois do quadro comparativo, com legenda Figura 2 e texto alternativo descritivo. A figura da casa permanece como Figura 1.
- `## Uso pelo arquiteto`: acrescentar que a comparação usa os princípios priorizados como critério de desempate.
- `## Exercício 10`: manter o contexto e os dois cenários. Acrescentar parágrafo que indica o produto do [exercício 9](bloco-1-principios-de-design.md#exercicio-9) como entrada, com três princípios de referência para quem não fez o exercício 9 (continuidade da operação durante a transição, dado pessoal tratado só em território nacional, substituição gradual de responsabilidade do núcleo legado), formulados como enunciado, sem motivação nem implicação. Enunciado em lista numerada: (1) escolher três estilos, (2) para cada estilo registrar adequação aos cenários e aos princípios, risco introduzido e mecanismo compensatório necessário, (3) recomendar um estilo para o contexto de modernização incremental. Fechar dizendo que o estilo recomendado é a entrada do exercício 11.
- `## Fontes`: manter as entradas atuais.

- [ ] **Step 3: Desenhar o visual**

`modulo-3-estilos-forcas-compromissos.svg` segue o mesmo padrão visual da Task 2 e mostra uma matriz com os sete estilos nas linhas e quatro colunas de força genérica, acoplamento, implantação independente, consistência e simplicidade operacional, marcadas como favorece, neutro ou prejudica. A legenda interna da figura declara que a matriz indica tendência e não regra, e o arquivo não contém nenhum termo da lista proibida das restrições globais.

- [ ] **Step 4: Rodar testes e validador**

Run: `python3 -m unittest tests.test_modulo_3_contract -k block_2 -k exercise_10 -k old_framing -k strangler -v && python3 scripts/validate_content.py --module modulo-3-design-e-padroes`
Expected: testes do bloco 2 em PASS. Validador sem violação no bloco 2.

- [ ] **Step 5: Commit**

```bash
git add docs/modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md docs/assets/images/modulo-3-estilos-forcas-compromissos.svg
git commit -m "refactor(aula-3): padroniza os estilos e liga aos principios"
```

---

### Task 4: Bloco 3, padrões arquiteturais e padrões de design

**Files:**
- Modify: `docs/modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md`
- Create: `docs/assets/images/modulo-3-niveis-de-padrao.svg`
- Modify: `docs/referencia/glossario.md` (Padrão arquitetural, Padrão de design)
- Modify: `docs/referencia/bibliografia.md` (Gamma et al., Evans, Fowler, Richardson, Nygard 2018)

**Interfaces:**
- Consumes: âncora `bloco-2-estilos-arquiteturais.md#exercicio-10`
- Produces: âncora `bloco-3-padroes-arquiteturais-e-de-design.md#exercicio-11`, com o mapa problema, padrão e consequência consumido pelo exercício 12. Títulos `#### <padrão>` com os nomes exatos de `PATTERNS`

- [ ] **Step 1: Rodar os testes do bloco e confirmar a falha**

Run: `python3 -m unittest tests.test_modulo_3_contract -k block_3 -k exercise_11 -v`
Expected: FAIL.

- [ ] **Step 2: Conferir as fontes novas**

Conferir em catálogo de editora ou página do autor, e só então acrescentar à bibliografia:

- Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design patterns: Elements of reusable object-oriented software*. Addison-Wesley.
- Evans, E. (2003). *Domain-driven design: Tackling complexity in the heart of software*. Addison-Wesley.
- Fowler, M. (2004, 29 de junho). *StranglerFigApplication*. martinfowler.com. https://martinfowler.com/bliki/StranglerFigApplication.html
- Richardson, C. (2018). *Microservices patterns: With examples in Java*. Manning.
- Nygard, M. T. (2018). *Release it! Design and deploy production-ready software* (2nd ed.). Pragmatic Bookshelf.

Qualquer dado não confirmado (data do artigo de Fowler, subtítulo) é corrigido pela fonte ou a entrada fica fora da bibliografia e do texto.

- [ ] **Step 3: Acrescentar as duas entradas ao glossário**

- `## Padrão arquitetural`: solução recorrente para uma preocupação transversal ou de integração entre partes do sistema, com escopo menor que o estilo e maior que o padrão de design.
- `## Padrão de design`: solução recorrente para a colaboração entre responsabilidades dentro de uma parte do sistema, descrita em termos de papéis, interfaces e relações.

- [ ] **Step 4: Escrever a página**

1. `# Padrões arquiteturais e padrões de design`
2. Linha de enquadramento: dentro do estilo recomendado no bloco 2, que soluções recorrentes tratam problemas específicos, e em que nível cada uma atua.
3. `## Antes de começar`: links para `estilo-arquitetural`, `padrao-arquitetural` e `padrao-de-design`.
4. `## Três níveis de decisão` (título livre da seção de conceito):
   - Definição de padrão como solução recorrente para um problema em um contexto, com forças e consequências, atribuída a Gamma et al. (1994).
   - Tabela da seção 6.2 do spec, com Nível, Pergunta e Exemplos, linhas Estilo arquitetural, Padrão arquitetural e Padrão de design. **Padrão arquitetural** e **padrão de design** em negrito no primeiro uso.
   - Parágrafo que declara Strangler Fig como padrão de modernização, e DDD como abordagem de modelagem e delimitação que dá origem ao Anti-Corruption Layer, sem tratá-lo como padrão isolado nem como estilo (Evans, 2003).
   - Figura `modulo-3-niveis-de-padrao.svg`, Figura 1, com texto alternativo descritivo.
   - Parágrafo sobre seleção por problema, com advertência contra complexidade acidental e contra padrão adotado sem evidência de necessidade.
   - `### Modernização e integração`, com `#### Strangler Fig`, `#### Anti-Corruption Layer`, `#### Adapter` e `#### API Gateway`. Exemplo principal em varejo online migrando o catálogo e o checkout de uma plataforma antiga.
   - `### Resiliência na integração`, com `#### Timeout`, `#### Retry com limite`, `#### Circuit Breaker` e `#### Bulkhead`. Exemplo principal em transportadora de cargas que consulta rastreamento e tarifa em parceiros externos. Citar Nygard (2018).
   - `### Consistência entre partes distribuídas`, com `#### Transactional Outbox` e `#### Saga`. Exemplo no varejo online, pedido, estoque e pagamento. Citar Richardson (2018).
   - Cada `####` contém um parágrafo de definição com exemplo e uma tabela de duas colunas, Aspecto e Descrição, com as linhas exatas Problema, Contexto e forças, Estrutura mínima, Consequência favorável, Custo e Sinal de uso inadequado. Adapter é o único padrão de design do repertório, e o texto diz isso.
   - `### Combinações`: um parágrafo sobre combinar padrões apenas quando resolvem problemas distintos, com um exemplo na transportadora (Timeout e Circuit Breaker sobre a mesma dependência) e um contraexemplo de redundância.
5. `## Uso pelo arquiteto`: selecionar pelo problema declarado, registrar o custo aceito e o sinal que indicaria retirada do padrão.
6. `## Exercício 11`: contexto da ACME e parágrafo apontando o estilo recomendado no [exercício 10](bloco-2-estilos-arquiteturais.md#exercicio-10). Tabela dos três problemas com os dados do caso reproduzidos:
   - coexistência entre legado e solução nova: núcleo COBOL em operação durante a transição, 2.300 pontos de acesso direto ao banco na camada Java, alteração do núcleo restrita ao contrato até 30/09/2027
   - proteção contra falha de integração: conector transacional para o CICS com tempo limite de 30 s, incidente de 04/02/2026 com 4h20 de duração e esgotamento do limite de tarefas concorrentes
   - publicação confiável de mudança acadêmica: R7 com 10 minutos, lote de notas das 05h10, até 360.000 lançamentos na janela de fechamento
   Enunciado em lista numerada: (1) para cada problema, escolher um padrão e indicar seu nível na taxonomia, (2) registrar problema, padrão, elemento afetado, consequência favorável e custo aceito, (3) indicar um padrão que foi considerado e descartado e o motivo. Fechar dizendo que o mapa é a entrada do ADR do exercício 12.
7. `## Fontes`: Gamma et al. (1994), Evans (2003), Fowler (2004), Richardson (2018), Nygard (2018), Ford e Richards (2020), Mendes (2026a) com o catálogo de padrões do material base, e `**Material do curso.**`.

- [ ] **Step 5: Desenhar o visual**

`modulo-3-niveis-de-padrao.svg` segue o mesmo padrão visual e mostra três faixas empilhadas, estilo, padrão arquitetural e padrão de design, cada uma com a pergunta do nível e dois exemplos genéricos da tabela da seção 6.2 do spec. A figura não associa nenhum problema do caso a um padrão, porque essa associação é o produto do exercício 11.

- [ ] **Step 6: Rodar testes e validador**

Run: `python3 -m unittest tests.test_modulo_3_contract -k block_3 -k exercise_11 -k strangler -k glossary -k bibliography -v && python3 scripts/validate_content.py --module modulo-3-design-e-padroes`
Expected: PASS nos testes listados, com a ressalva de que o teste da bibliografia só passa quando as cinco entradas do Step 2 estiverem conferidas. Se alguma entrada não for conferida, o teste é ajustado para retirar o autor correspondente, e o ajuste fica registrado na mensagem de commit desta tarefa.

- [ ] **Step 7: Commit**

```bash
git add docs/modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md docs/assets/images/modulo-3-niveis-de-padrao.svg docs/referencia/glossario.md docs/referencia/bibliografia.md
git commit -m "feat(aula-3): escreve o bloco de padroes arquiteturais e de design"
```

---

### Task 5: Bloco 4, harmonização do registro de decisão

**Files:**
- Modify: `docs/modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md`
- Create: `docs/assets/images/modulo-3-ciclo-de-vida-adr.svg`

**Interfaces:**
- Consumes: âncoras `#exercicio-9`, `#exercicio-10` e `#exercicio-11` das Tasks 2 a 4
- Produces: âncora `bloco-4-registro-de-decisao-arquitetural.md#exercicio-12`

- [ ] **Step 1: Rodar os testes do bloco e confirmar a falha**

Run: `python3 -m unittest tests.test_modulo_3_contract -k block_4 -k exercise_12 -v`
Expected: FAIL.

- [ ] **Step 2: Revisar a página**

- Linha de enquadramento nova: o bloco fecha a cadeia da aula, registrando a decisão construída nos blocos 1 a 3 de forma compreensível, rastreável e revisável. Remover "abre a aula".
- Conceito: preservar a distinção entre decisão e racional, a abordagem leve, os formatos Nygard e MADR, o exemplo do Kubernetes e as práticas. Acrescentar parágrafo que o ADR registra uma decisão e não substitui o desenho nem o plano de implementação, e que suas forças vêm dos princípios e cenários já produzidos.
- Tabela do template de dez campos com quatro colunas: Campo, O que registrar, Critério de qualidade, Erro frequente. O conteúdo atual de "O que registrar" é preservado.
- Remover a sobreposição entre o parágrafo "Os dois campos que o formato de Nygard não tem" e a tabela, mantendo um único trecho sobre Evidências e Revisão.
- Figura `modulo-3-ciclo-de-vida-adr.svg`, com legenda e texto alternativo, na subseção de práticas, mostrando os estados proposta, aceita, substituída e rejeitada, e a anatomia do ADR com os dez campos.
- `## Exercício 12`: o ADR registra o estilo recomendado no exercício 10 e os padrões do exercício 11. Enunciado com os links `bloco-1-principios-de-design.md#exercicio-9`, `bloco-2-estilos-arquiteturais.md#exercicio-10` e `bloco-3-padroes-arquiteturais-e-de-design.md#exercicio-11`. As forças vêm dos princípios priorizados, as alternativas são comparadas por essas forças, as consequências incluem o custo aceito de cada padrão, e o gatilho de revisão é observável. Manter as quatro frases modelo e a instrução sobre estado proposta.
- `## Fontes`: preservar as entradas e acrescentar Richardson (2018) apenas se o texto citar.

- [ ] **Step 3: Desenhar o visual**

`modulo-3-ciclo-de-vida-adr.svg` segue o mesmo padrão visual, com a máquina de estados do ADR à esquerda e, à direita, o arquivo ADR com os dez campos agrupados em contexto, escolha, efeito e controle. O arquivo não contém nenhum termo da lista proibida das restrições globais.

- [ ] **Step 4: Rodar testes e validador**

Run: `python3 -m unittest tests.test_modulo_3_contract -k block_4 -k exercise_12 -k old_framing -v && python3 scripts/validate_content.py --module modulo-3-design-e-padroes`
Expected: PASS e zero violação no bloco 4.

- [ ] **Step 5: Commit**

```bash
git add docs/modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md docs/assets/images/modulo-3-ciclo-de-vida-adr.svg
git commit -m "refactor(aula-3): harmoniza o bloco de registro de decisao"
```

---

### Task 6: Índice, síntese, dossiê e gabaritos

**Files:**
- Modify: `docs/modulo-3-design-e-padroes/index.md`
- Modify: `docs/modulo-3-design-e-padroes/sintese.md`
- Modify: `docs/caso-acme/artefatos.md` (linha da Aula 3)
- Modify: `~/pka/projects/aulas/PRJ-aulas-iec-projeto-e-inovacao-em-arquitetura-de-solucoes.md` (fora do repositório)

**Interfaces:**
- Consumes: páginas das Tasks 2 a 5
- Produces: nenhum

- [ ] **Step 1: Rodar os testes e confirmar a falha**

Run: `python3 -m unittest tests.test_modulo_3_contract -k index -k synthesis -v`
Expected: FAIL.

- [ ] **Step 2: Escrever o índice**

Seções na ordem: título, parágrafo de abertura, `## Objetivos de aprendizagem` com os seis objetivos da seção 1 do spec em verbos observáveis, `## Grade de tempo` com o mesmo formato da Aula 2 (19h00 às 22h30, intervalo 20h30 às 20h45, quatro blocos de 25 e 15 minutos, total de 160 minutos), `## Entrada recebida da Aula 2` com os cenários, as restrições e a declaração de escopo, cada um com link para o bloco de origem na Aula 2, `## Roteiro da aula` com um parágrafo por bloco ligando a página e dizendo o que o exercício recebe e entrega, mais a síntese, e `## Preparação para a Aula 4`. Remover o parágrafo sobre blocos publicados antes da reorganização.

- [ ] **Step 3: Escrever a síntese**

Seções: linha de abertura, `## Checklist do que precisa permanecer`, `## Cadeia da decisão` com a cadeia objetivo, requisito, princípio, estilo, padrão e decisão em lista numerada e um parágrafo sobre o produto de cada exercício, `## Autoavaliação` com cinco perguntas sem gabarito, `## Fontes da aula` com todas as referências usadas nos quatro blocos.

- [ ] **Step 4: Atualizar o dossiê**

Em `docs/caso-acme/artefatos.md`, na linha da Aula 3, substituir o texto por: princípios de design priorizados com esboço lógico, comparação de estilos contra os cenários da Aula 2 e contra os princípios, mapa de problema, padrão e consequência, e o ADR que registra estilo e padrões.

- [ ] **Step 5: Registrar os gabaritos no PKA**

Acrescentar `## Gabaritos dos exercícios da Aula 3` depois da seção `## Gabaritos dos exercícios novos das Aulas 1 e 2`, com `### Exercício 9` a `### Exercício 12`, no formato das entradas existentes: resposta de referência, distinção entre resposta excelente, aceitável e fraca, e o critério de correção.

- [ ] **Step 6: Rodar testes e validador**

Run: `python3 -m unittest tests.test_modulo_3_contract -v && python3 scripts/validate_content.py`
Expected: todos os testes do módulo em PASS e zero violação.

- [ ] **Step 7: Commit**

```bash
git add docs/modulo-3-design-e-padroes/index.md docs/modulo-3-design-e-padroes/sintese.md docs/caso-acme/artefatos.md
git commit -m "feat(aula-3): escreve indice e sintese do modulo"
```

---

### Task 7: Verificação integral

**Files:**
- Nenhum arquivo novo. Correções pontuais onde a verificação apontar.

**Interfaces:**
- Consumes: todas as tarefas anteriores
- Produces: evidência de aceite para os critérios da seção 12 do spec

- [ ] **Step 1: Suíte e validador**

Run: `python3 -m unittest discover -s tests -v && python3 scripts/validate_content.py`
Expected: todos os testes em OK e `Resumo: 0 violacao(oes).`

- [ ] **Step 2: Build estrito**

Run: `.venv/bin/mkdocs build --strict`
Expected: build sem aviso nem erro.

- [ ] **Step 3: Inspeção visual**

Gerar miniaturas dos quatro SVG com `qlmanage -t -s 1200 -o <scratchpad> docs/assets/images/modulo-3-*.svg` e ler cada PNG, conferindo legibilidade, sobreposição de texto e ausência de dado do caso. Para as páginas, servir o site com `.venv/bin/mkdocs serve` e capturar as seis páginas com um navegador sem interface, se houver um disponível. Se não houver, registrar no relatório que a inspeção das páginas renderizadas não foi feita e que só os SVG e o HTML gerado foram conferidos.

- [ ] **Step 4: Leitura editorial**

Reler as seis páginas contra as restrições globais: negrito entre três e cinco por página, frases com média de pelo menos 14 palavras, ausência de metáfora e de frase de efeito, domínios de exemplo conforme a alocação, nenhum trecho que responda aos exercícios.

- [ ] **Step 5: Commit das correções**

```bash
git add -A docs tests mkdocs.yml
git commit -m "fix(aula-3): corrige apontamentos da verificacao integral"
```
