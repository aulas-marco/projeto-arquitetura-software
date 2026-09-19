# Revisão 1 do Módulo 1, publicado

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Aplicar as nove revisões que o professor determinou sobre o Módulo 1 já publicado: anatomia sem gabarito público, gabaritos mais profundos movidos para o PKA, exercícios numerados e itemizados, cronograma genérico sem datas reais, bibliografia em APA, e aprofundamento de conteúdo nos blocos de cenários/QAW e de estilos arquiteturais, este último ancorado no material de base do professor.

**Architecture:** Edições sobre o site já publicado, sem alterar a estrutura de diretórios. O validador de conteúdo muda de contrato (sete seções, não oito) e ganha uma checagem nova. O conteúdo de gabarito migra para um arquivo fora deste repositório, em `~/pka`.

**Tech Stack:** Igual ao plano anterior. Python 3, mkdocs-material, unittest.

**Spec:** `docs/superpowers/specs/2026-09-19-estrutura-do-curso-design.md`, seção 12 (Revisão 1)

## Global Constraints

- Zero ocorrência da palavra "prosa" em `docs/` inteiro
- Zero data de calendário real (DD/MM/AAAA de 2026) fora de `docs/caso-acme/`
- Nenhuma página de bloco contém `## Gabarito`
- Todo cabeçalho de exercício segue o padrão `## Exercício N`, N inteiro
- Enunciado de exercício com mais de uma instrução usa lista numerada, não parágrafo corrido
- Bibliografia e citações em Fontes em formato APA 7
- Negrito no máximo três a cinco termos por página de bloco, só no primeiro uso, nunca em frase inteira ou número
- Os quatro estilos comparados continuam camadas, microsserviços, orientado a eventos, microkernel. MVC, MVVM, DDD e Strangler continuam fora, por decisão confirmada em 19/09/2026

---

### Task 1: Validador e testes com a anatomia de sete seções

**Files:**
- Modify: `scripts/validate_content.py`
- Modify: `tests/test_content_contract.py`

**Interfaces:**
- Consumes: nada
- Produces: `BLOCK_SECTIONS` sem "Gabarito", checagem nova `check_exercise_numbering` e `check_no_prosa_word`, usadas por `validate()`

- [ ] **Step 1: Atualizar `BLOCK_SECTIONS` para as seis seções nomeadas restantes**

Em `scripts/validate_content.py`, `BLOCK_SECTIONS` passa a ser `("Antes de começar", "Conceito", "Uso pelo arquiteto", "Exercício", "Fontes")`. Ajustar `check_block_anatomy` para procurar `## Exercício` com ou sem número após, mas exigir que exista um número: usar regex `r"^##\s+Exerc[ií]cio\s+\d+\s*$"` em vez de comparação literal de string para essa seção específica, mantendo comparação literal para as demais.

- [ ] **Step 2: Escrever `check_no_prosa_word`**

```python
def check_prosa_word(path: Path, prose: list[tuple[int, str]]) -> list[str]:
    return [
        f"{path.relative_to(ROOT)}:{number} palavra prosa proibida"
        for number, line in prose
        if re.search(r"\bprosa\b", line, re.IGNORECASE)
    ]
```

Chamar essa função dentro de `validate()`, junto das demais.

- [ ] **Step 3: Escrever teste de comportamento para a checagem de exercício numerado**

Em `tests/test_content_contract.py`, seguindo o padrão dos testes existentes: criar `docs/modulo-1-fundamentos/bloco-9-teste-sem-numero.md` com as seis seções mas `## Exercício` sem número, confirmar que o validador acusa. Criar outro com `## Exercício 7`, confirmar que não acusa. Apagar os dois no `finally`.

- [ ] **Step 4: Escrever teste de comportamento para a checagem da palavra proibida**

Arquivo temporário com "Responda em prosa", confirmar que o validador acusa. Apagar no `finally`.

- [ ] **Step 5: Rodar a suíte e o validador**

Run: `python3 -m unittest discover -s tests -v && python3 scripts/validate_content.py`
Expected: novos testes passando. O validador vai acusar violações nas quatro páginas de bloco reais, porque elas ainda têm `## Gabarito` e `## Exercício` sem número. Essas violações são esperadas nesta tarefa e serão resolvidas pelas tarefas 4 a 7.

- [ ] **Step 6: Commit**

```bash
git add scripts/validate_content.py tests/test_content_contract.py
git commit -m "feat(validacao): anatomia de sete secoes, exercicio numerado, proibe prosa"
```

---

### Task 2: Site genérico, sem datas reais e sem o parágrafo de abertura

**Files:**
- Modify: `docs/index.md`
- Modify: `docs/cronograma.md`
- Modify: `docs/modulo-1-fundamentos/index.md`
- Modify: `docs/modulo-1-fundamentos/sintese.md`
- Modify: `docs/modulo-2-plataforma-e-modelos/index.md` até `docs/modulo-6-evolucao-e-governanca/index.md`

**Interfaces:**
- Consumes: nada
- Produces: nenhuma data DD/MM/AAAA de 2026 fora de `docs/caso-acme/`

- [ ] **Step 1: Remover o parágrafo de abertura de `docs/index.md`**

Remover o parágrafo que começa em "Este site reúne o material da disciplina...". Reescrever a página para abrir direto pela identificação da disciplina e das turmas, sem esse parágrafo específico. Manter o resto do conteúdo (avaliação a divulgar em aula, orientação sobre a trilha do caso).

- [ ] **Step 2: Genericizar `docs/cronograma.md`**

Trocar a coluna de datas por "Aula 1" a "Aula 6", sem data. Manter o horário (19h00 às 22h30, intervalo 20h30 às 20h45), que é estrutura de bloco, não data de calendário. Manter a tabela dos quatro blocos da Aula 1.

- [ ] **Step 3: Genericizar `docs/modulo-1-fundamentos/index.md`**

Trocar "A aula ocorre em 21/09/2026" por "A aula ocorre". Trocar "A Aula 2, em 23/09/2026" por "A Aula 2". Confirmar que nenhuma outra data sobrevive na página.

- [ ] **Step 4: Genericizar `docs/modulo-1-fundamentos/sintese.md`**

Rodar `grep -n "2026" docs/modulo-1-fundamentos/sintese.md` e remover qualquer data de calendário encontrada, sem alterar o resto do conteúdo.

- [ ] **Step 5: Genericizar os cinco índices de módulo restantes**

Para `docs/modulo-2-plataforma-e-modelos/index.md` até `docs/modulo-6-evolucao-e-governanca/index.md`, remover a data e manter a frase sobre a partição em blocos ainda não estar definida.

- [ ] **Step 6: Verificar**

Run: `grep -rn "202[4-9]" docs/ --include="*.md" | grep -v caso-acme`
Expected: nenhuma ocorrência.

Run: `python3 scripts/validate_content.py`
Expected: as mesmas violações da Task 1 nas páginas de bloco, nada novo introduzido por esta tarefa.

- [ ] **Step 7: Commit**

```bash
git add docs/index.md docs/cronograma.md docs/modulo-1-fundamentos/index.md docs/modulo-1-fundamentos/sintese.md docs/modulo-2-plataforma-e-modelos/index.md docs/modulo-3-descoberta-e-riscos/index.md docs/modulo-4-dados-e-seguranca/index.md docs/modulo-5-blueprint-e-trm/index.md docs/modulo-6-evolucao-e-governanca/index.md
git commit -m "docs(cronograma): generico sem datas reais, remove abertura do indice"
```

---

### Task 3: Bibliografia em APA

**Files:**
- Modify: `docs/referencia/bibliografia.md`

**Interfaces:**
- Consumes: nada
- Produces: cinco entradas em APA 7 que as tarefas 6 e 7 vão citar nas seções Fontes

- [ ] **Step 1: Reescrever as cinco entradas verificadas em APA 7**

Usar exatamente:

```markdown
# Bibliografia

Fontes conferidas, no formato APA 7ª edição. Referências adicionais entram somente após conferência.

- International Organization for Standardization/International Electrotechnical Commission/Institute of Electrical and Electronics Engineers. (2022). *Systems and software engineering — Architecture description* (ISO/IEC/IEEE 42010:2022).
- International Organization for Standardization. (2023). *Systems and software engineering — Systems and software quality requirements and evaluation (SQuaRE) — Product quality model* (ISO/IEC 25010:2023).
- Barbacci, M., Ellison, R., Lattanze, A., Stafford, J., Weinstock, C., & Wood, W. (2003). *Quality attribute workshops (QAWs), third edition* (CMU/SEI-2003-TR-016). Software Engineering Institute, Carnegie Mellon University.
- Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley.
- Ford, N., & Richards, M. (2020). *Fundamentals of software architecture*. O'Reilly.
- Mendes, M. (2026). *Arquitetura de software* [Material de curso]. https://marco-mendes.github.io/arquitetura-software/
```

Manter a frase final sobre número de características da 25010:2023, DOI do SEI e a coletânea de 2016 continuarem fora por falta de verificação, se já existir texto equivalente na página atual.

- [ ] **Step 2: Verificar**

Run: `.venv/bin/mkdocs build --strict`
Expected: build limpo.

- [ ] **Step 3: Commit**

```bash
git add docs/referencia/bibliografia.md
git commit -m "docs(referencia): bibliografia em formato APA 7"
```

---

### Task 4: Bloco 1, sem gabarito público, exercício numerado e itemizado

**Files:**
- Modify: `docs/modulo-1-fundamentos/bloco-1-arquitetura-e-papel-do-arquiteto.md`
- Create (staging, fora da publicação): `.superpowers/sdd/2026-09-19-revisao-1-modulo-1/gabaritos-extraidos.md`

**Interfaces:**
- Consumes: anatomia da Task 1
- Produces: o texto do gabarito atual do bloco 1, extraído para o arquivo de staging, consumido pela Task 8

- [ ] **Step 1: Copiar o conteúdo atual da seção `## Gabarito` para o arquivo de staging**

Antes de apagar, copiar o texto completo da seção Gabarito deste bloco para `.superpowers/sdd/2026-09-19-revisao-1-modulo-1/gabaritos-extraidos.md`, sob um cabeçalho `## Bloco 1, arquitetura e papel do arquiteto`. Esse arquivo não é publicado, fica fora de `docs/`.

- [ ] **Step 2: Remover a seção `## Gabarito` da página pública**

- [ ] **Step 3: Renomear `## Exercício` para `## Exercício 1`**

- [ ] **Step 4: Converter o enunciado em lista numerada**

A frase "responda em prosa a três perguntas" e o parágrafo corrido com as três perguntas viram:

```markdown
Responda às três perguntas abaixo.

1. O que a instituição quer do sistema acadêmico, considerando os interesses que aparecem em mais de um papel.
2. Quem, entre os papéis listados, tem autoridade para decidir sobre orçamento, sobre padrão de identidade e sobre prazo de contrato de sustentação, e por quê.
3. Qual das sete restrições, isoladamente, elimina a alternativa de reescrever o sistema acadêmico inteiro em uma única entrega, e qual elimina a alternativa de substituí-lo por um produto de mercado.
```

Ajustar a pontuação de cada item para as regras do curso (zero ponto-e-vírgula, no máximo um travessão por parágrafo).

- [ ] **Step 5: Aplicar negrito parcimonioso na seção Conceito**

Três a cinco termos centrais no primeiro uso, por exemplo **arquitetura de software** e **enquadramento do problema**. Não repetir o mesmo termo em negrito duas vezes na página.

- [ ] **Step 6: Verificar**

Run: `python3 scripts/validate_content.py --module modulo-1-fundamentos`
Expected: zero violação nesta página. As demais três páginas de bloco continuam com violação esperada até as tarefas 5 a 7.

- [ ] **Step 7: Commit**

```bash
git add docs/modulo-1-fundamentos/bloco-1-arquitetura-e-papel-do-arquiteto.md
git commit -m "docs(modulo-1): bloco 1 sem gabarito publico, exercicio 1 itemizado"
```

---

### Task 5: Bloco 2, sem gabarito público, exercício numerado e itemizado

**Files:**
- Modify: `docs/modulo-1-fundamentos/bloco-2-qualidade-e-tipos-de-requisito.md`
- Modify: `.superpowers/sdd/2026-09-19-revisao-1-modulo-1/gabaritos-extraidos.md`

**Interfaces:**
- Consumes: Task 4 (mesmo arquivo de staging)
- Produces: gabarito extraído do bloco 2, acrescentado ao arquivo de staging

- [ ] **Step 1: Extrair o gabarito atual para o arquivo de staging, sob `## Bloco 2, qualidade e tipos de requisito`**

- [ ] **Step 2: Remover `## Gabarito`, renomear para `## Exercício 2`**

- [ ] **Step 3: Converter o enunciado em lista numerada**

"Classifique cada um dos oito requisitos... justificando em uma frase. Em seguida, escolha dois requisitos... reescreva..." vira:

```markdown
1. Classifique cada um dos oito requisitos em uma das quatro categorias, requisito funcional, requisito não funcional, requisito de atributo de qualidade ou restrição, justificando em uma frase.
2. Escolha dois requisitos que sejam requisitos de atributo de qualidade mal formulados e reescreva cada um em forma mensurável, seguindo o padrão de contexto, carga e medida usado no exemplo de desempenho da plataforma de vídeo.
```

- [ ] **Step 4: Negrito parcimonioso na seção Conceito**, três a cinco termos.

- [ ] **Step 5: Verificar**

Run: `python3 scripts/validate_content.py --module modulo-1-fundamentos`
Expected: zero violação nesta página.

- [ ] **Step 6: Commit**

```bash
git add docs/modulo-1-fundamentos/bloco-2-qualidade-e-tipos-de-requisito.md
git commit -m "docs(modulo-1): bloco 2 sem gabarito publico, exercicio 2 itemizado"
```

---

### Task 6: Bloco 3, aprofundamento do método QAW, sem gabarito público

**Files:**
- Modify: `docs/modulo-1-fundamentos/bloco-3-cenarios-e-significancia-arquitetural.md`
- Modify: `.superpowers/sdd/2026-09-19-revisao-1-modulo-1/gabaritos-extraidos.md`

**Interfaces:**
- Consumes: `docs/superpowers/specs/2026-09-19-texto-referencia-atributos-qualidade.md`, seções 2.3 e 7
- Produces: gabarito extraído, acrescentado ao staging

Esta tarefa não é só mecânica. O professor pediu tratamento mais rigoroso, mais profundidade e mais exemplos do método QAW.

- [ ] **Step 1: Extrair o gabarito atual para o staging, sob `## Bloco 3, cenários e significância arquitetural`**

- [ ] **Step 2: Aprofundar a seção Conceito sobre QAW**

Sem perder o que já está lá, acrescentar: descrição mais completa do processo de elicitação do QAW (quem participa, como os cenários brutos dos interessados são coletados, consolidados, priorizados e refinados, conforme a seção 2.3 do texto de referência), e pelo menos mais um exemplo completo de cenário no formato de seis elementos, além dos dois já existentes, em domínio ainda não usado como principal em bloco algum desta aula (verificar os já usados: comércio eletrônico, controle industrial, banco, hospital, pagamentos com múltiplos adquirentes, expansão internacional). Sugestão: um cenário de segurança, seguindo o exemplo de autenticação da seção 2 do texto de referência, ou um de confiabilidade.

- [ ] **Step 3: Remover `## Gabarito`, renomear para `## Exercício 3`**

- [ ] **Step 4: Converter o enunciado em lista numerada**

```markdown
1. Escreva dois cenários de atributo de qualidade para a ACME, no formato de seis elementos apresentado no Conceito. O primeiro cenário deve ter como estímulo o pico de sazonalidade descrito acima, e pode partir, como orientação de continuidade e sem obrigatoriedade, da reescrita mensurável de R2 sobre disponibilidade na janela de matrícula produzida no bloco 2. O segundo deve ter como estímulo o incidente descrito acima.
2. Para cada um dos dois cenários, aplique o roteiro de sete perguntas e defenda, com base nas respostas, se aquele cenário constitui um requisito arquiteturalmente significativo.
```

- [ ] **Step 5: Negrito parcimonioso** na seção Conceito ampliada.

- [ ] **Step 6: Verificar**

Run: `python3 scripts/validate_content.py --module modulo-1-fundamentos && .venv/bin/mkdocs build --strict`
Expected: zero violação nesta página, build limpo.

- [ ] **Step 7: Commit**

```bash
git add docs/modulo-1-fundamentos/bloco-3-cenarios-e-significancia-arquitetural.md
git commit -m "docs(modulo-1): bloco 3 aprofunda QAW, sem gabarito publico, exercicio 3 itemizado"
```

---

### Task 7: Bloco 4, aprofundamento de estilos com o material de base do professor

**Files:**
- Modify: `docs/modulo-1-fundamentos/bloco-4-estilos-arquiteturais.md`
- Modify: `.superpowers/sdd/2026-09-19-revisao-1-modulo-1/gabaritos-extraidos.md`

**Interfaces:**
- Consumes: `marco-mendes/arquitetura-software`, arquivos `docs/modulo-1-visao-geral/conceitos.md` e `padroes-e-decisoes.md`, para inspiração de rigor, não para cópia
- Produces: gabarito extraído, acrescentado ao staging

Esta tarefa é a de maior densidade de conteúdo novo do plano.

- [ ] **Step 1: Extrair o gabarito atual para o staging, sob `## Bloco 4, estilos arquiteturais`**

- [ ] **Step 2: Aprofundar a seção Conceito**

Para cada um dos quatro estilos já comparados (camadas, microsserviços, orientado a eventos, microkernel), acrescentar, no padrão de rigor do material de base do professor:
- Uma tabela ou lista curta de força típica e anti-padrão típico daquele estilo
- Uma heurística prática de quando o estilo deixa de servir (para camadas, por exemplo, a regra de que se mais de 80% das chamadas apenas repassam sem decidir, validar ou transformar, o estilo provavelmente não é o certo)
- Onde fizer sentido, referência à Lei de Conway (organizações produzem arquiteturas que espelham sua estrutura de comunicação) como explicação de por que um estilo emerge

NÃO reabrir a lista de estilos comparados, NÃO incluir MVC, MVVM, DDD ou Strangler como estilo.

- [ ] **Step 3: Remover `## Gabarito`, renomear para `## Exercício 4`**

- [ ] **Step 4: Converter o enunciado em lista numerada**

```markdown
1. Escolha três dos estilos apresentados no Conceito e compare cada um contra os dois cenários acima. Para cada estilo, avalie se ele sustentaria a resposta e a medida descritas, considerando o núcleo COBOL sobre CICS como parte que permanece em operação durante a transição.
2. Defenda qual dos três estilos se ajusta melhor a um contexto de modernização incremental de um sistema legado crítico, justificando a escolha por atributo de qualidade favorecido e por atributo de qualidade prejudicado.
```

- [ ] **Step 5: Atualizar Fontes para citar o material de base do professor**

Acrescentar, no formato APA já fixado na Task 3: "Mendes, M. (2026). *Arquitetura de software* [Material de curso]. https://marco-mendes.github.io/arquitetura-software/", além de Ford e Richards e Bass, Clements e Kazman já citados.

- [ ] **Step 6: Negrito parcimonioso** na seção Conceito ampliada.

- [ ] **Step 7: Verificar**

Run: `python3 scripts/validate_content.py && .venv/bin/mkdocs build --strict`
Expected: zero violação em todo o repositório, build limpo, porque esta é a última das quatro páginas de bloco a ser corrigida.

- [ ] **Step 8: Commit**

```bash
git add docs/modulo-1-fundamentos/bloco-4-estilos-arquiteturais.md
git commit -m "docs(modulo-1): bloco 4 aprofunda estilos com material de base, exercicio 4 itemizado"
```

---

### Task 8: Gabaritos aprofundados na narrativa do PKA

**Files:**
- Modify: `/Users/marcomendes/Library/CloudStorage/Dropbox/Pessoal/pka/projects/aulas/PRJ-aulas-iec-asd-10-estrategias-e-projeto-de-arquitetura-de-software.md`

**Interfaces:**
- Consumes: `.superpowers/sdd/2026-09-19-revisao-1-modulo-1/gabaritos-extraidos.md`, produzido pelas tarefas 4 a 7
- Produces: seção de gabaritos no arquivo de narrativa do PKA, fora deste repositório

Este arquivo é do PKA do professor, não do repositório do site. É outro projeto, em outro caminho.

- [ ] **Step 1: Ler o arquivo de narrativa do PKA e o arquivo de staging com os quatro gabaritos extraídos**

- [ ] **Step 2: Acrescentar uma seção `## Gabaritos, Aula 1` ao arquivo de narrativa do PKA**

Para cada um dos quatro blocos, reescrever o gabarito extraído com MAIS profundidade do que tinha no site: além do critério de avaliação já existente, acrescentar o que caracteriza uma resposta excelente contra uma resposta apenas aceitável, e, quando fizer sentido, uma resposta de referência completa (não só o critério), já que este arquivo é de uso exclusivo do professor e pode conter a resposta fechada.

- [ ] **Step 3: Adicionar uma narrativa datada de 19/09/2026 registrando a revisão**

Seguindo o padrão de narrativas já usado no arquivo (ver as narrativas anteriores de 19/09/2026 já presentes), registrar que os gabaritos saíram do site público e passaram a viver neste arquivo, com mais profundidade.

- [ ] **Step 4: Verificar**

Run: `python3 system/scripts/validate-pka.py --files "projects/aulas/PRJ-aulas-iec-asd-10-estrategias-e-projeto-de-arquitetura-de-software.md"` (rodar a partir de `/Users/marcomendes/Library/CloudStorage/Dropbox/Pessoal/pka`)
Expected: 0 erros.

- [ ] **Step 5: Este passo não gera commit no repositório do site.** O arquivo do PKA tem seu próprio controle, fora deste plano. Apenas confirme que o arquivo foi salvo.

---

### Task 9: Verificação final da revisão

**Files:** nenhum, salvo correções encontradas

- [ ] **Step 1: Rodar a suíte completa**

Run: `cd /Users/marcomendes/code/projeto-arquitetura-software && python3 -m unittest discover -s tests -v && python3 scripts/validate_content.py && .venv/bin/mkdocs build --strict`
Expected: testes passando, zero violações, build limpo.

- [ ] **Step 2: Confirmar ausência da palavra "prosa"**

Run: `grep -rni "prosa" docs/ --include="*.md"`
Expected: nenhuma ocorrência (o validador da Task 1 já cobre isso, esta é conferência humana adicional).

- [ ] **Step 3: Confirmar ausência de data real fora do caso**

Run: `grep -rn "202[4-9]" docs/ --include="*.md" | grep -v caso-acme`
Expected: nenhuma ocorrência.

- [ ] **Step 4: Confirmar ausência de Gabarito público**

Run: `grep -rn "## Gabarito" docs/`
Expected: nenhuma ocorrência.

- [ ] **Step 5: Confirmar numeração de exercício**

Run: `grep -rn "^## Exercício" docs/modulo-1-fundamentos/`
Expected: quatro linhas, com números 1, 2, 3, 4, um por bloco.

- [ ] **Step 6: Confirmar bibliografia em APA e a citação ao material do professor**

Ler `docs/referencia/bibliografia.md` e `docs/modulo-1-fundamentos/bloco-4-estilos-arquiteturais.md`, seção Fontes.

- [ ] **Step 7: Confirmar que o arquivo de narrativa do PKA tem os quatro gabaritos**

Run: `grep -c "^### Bloco" "/Users/marcomendes/Library/CloudStorage/Dropbox/Pessoal/pka/projects/aulas/PRJ-aulas-iec-asd-10-estrategias-e-projeto-de-arquitetura-de-software.md"` ou equivalente, conforme o formato real usado na Task 8.

- [ ] **Step 8: Ler as quatro páginas de bloco por inteiro**

Confirmar tom, negrito parcimonioso (não mais que cinco por página), e que a lista numerada de cada exercício está clara.

- [ ] **Step 9: Commit final, se houver correção**

Se tudo já estiver certo, não commitar nada vazio. Se houver correção pontual, commit com `chore(revisao-1):` descrevendo o que foi ajustado.
