# Aula 2, ADR, plataforma arquitetural e modelagem C4

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Escrever o Módulo 2 completo do site, quatro páginas de bloco (registro de decisão arquitetural, plataforma arquitetural, ADR de plataforma, representação de modelos e C4 níveis 1 e 2), mais índice e síntese, seguindo a anatomia de sete seções e todas as regras já em vigor no Módulo 1.

**Architecture:** Mesmo padrão do Módulo 1: página de bloco com sete seções, exercício numerado, sem gabarito público, referência com local exato, negrito parcimonioso, exemplos em domínios distintos. Os blocos 1 e 3 desta aula encadeiam com o exercício do bloco 4 da Aula 1 e com o exercício do bloco 2 desta mesma aula, respectivamente.

**Tech Stack:** Igual ao já estabelecido. Python 3, mkdocs-material, unittest.

**Spec:** `docs/superpowers/specs/2026-09-19-estrutura-do-curso-design.md`, seção 13

## Global Constraints

- Anatomia de sete seções: título, linha de enquadramento, Antes de começar, Conceito, Uso pelo arquiteto, Exercício N, Fontes. Sem Gabarito.
- Exercícios numerados 5, 6, 7, 8, dando sequência aos quatro já usados na Aula 1
- Zero ponto-e-vírgula, no máximo um travessão por parágrafo, exceto legenda de figura
- Negrito entre três e cinco por página, na seção Conceito, no primeiro uso, nunca em frase inteira ou número
- Toda referência a exemplo, seção ou bloco de outra parte do site vem com o local exato e link Markdown quando o alvo existir
- Exemplos em pelo menos dois domínios distintos por seção de conceito, sem repetir o domínio principal do bloco imediatamente anterior ou seguinte
- Enunciado de exercício com mais de uma instrução usa lista numerada
- Fontes em formato APA, citação narrativa (Sobrenome, ano), linkando para `../referencia/bibliografia.md`
- Gabarito de cada bloco vai para a narrativa do PKA (`~/pka/projects/aulas/PRJ-aulas-iec-asd-10-estrategias-e-projeto-de-arquitetura-de-software.md`), nunca para o site público
- Datas visíveis ao leitor no formato DD/MM/AAAA, mas o cronograma e os índices de módulo continuam genéricos, sem data real (decisão da revisão anterior, que vale para toda a disciplina)

---

### Task 1: Navegação, índice e síntese do Módulo 2

**Files:**
- Modify: `mkdocs.yml`
- Modify: `docs/modulo-2-plataforma-e-modelos/index.md`
- Create: `docs/modulo-2-plataforma-e-modelos/sintese.md`

**Interfaces:**
- Consumes: nenhum
- Produces: a grade de tempo da Aula 2, único lugar do site com os minutos, consumida pelas tarefas seguintes por referência

- [ ] **Step 1: Atualizar `mkdocs.yml`**

No item de nav "Aula 2 — Plataforma e modelos", acrescentar as quatro páginas de bloco e a síntese, seguindo exatamente o padrão já usado no item da Aula 1:

```yaml
  - "Aula 2 — Plataforma e modelos":
      - Visão geral: modulo-2-plataforma-e-modelos/index.md
      - "Bloco 1: registro de decisão arquitetural": modulo-2-plataforma-e-modelos/bloco-1-registro-de-decisao-arquitetural.md
      - "Bloco 2: plataforma arquitetural": modulo-2-plataforma-e-modelos/bloco-2-plataforma-arquitetural.md
      - "Bloco 3: ADR de plataforma": modulo-2-plataforma-e-modelos/bloco-3-adr-de-plataforma.md
      - "Bloco 4: representação de modelos e C4": modulo-2-plataforma-e-modelos/bloco-4-representacao-de-modelos-e-c4.md
      - Síntese: modulo-2-plataforma-e-modelos/sintese.md
```

- [ ] **Step 2: Criar os quatro arquivos de bloco em esqueleto**

Para o build não quebrar antes das tarefas seguintes escreverem o conteúdo real:

```bash
cd ~/code/projeto-arquitetura-software
printf '# Registro de decisão arquitetural\n' > docs/modulo-2-plataforma-e-modelos/bloco-1-registro-de-decisao-arquitetural.md
printf '# Plataforma arquitetural\n' > docs/modulo-2-plataforma-e-modelos/bloco-2-plataforma-arquitetural.md
printf '# ADR de plataforma\n' > docs/modulo-2-plataforma-e-modelos/bloco-3-adr-de-plataforma.md
printf '# Representação de modelos e C4\n' > docs/modulo-2-plataforma-e-modelos/bloco-4-representacao-de-modelos-e-c4.md
```

- [ ] **Step 3: Escrever `docs/modulo-2-plataforma-e-modelos/index.md`**

Título funcional. Uma linha com a pergunta que a aula responde: como registrar uma decisão arquitetural de forma rastreável, e como escolher e representar a plataforma que sustenta o estilo já decidido. Objetivos de aprendizagem em verbos observáveis (registrar, comparar, justificar, modelar). A grade de tempo em tabela, com os quatro blocos, o conceito de cada um, e a marcação de 25 e 15 minutos, único lugar da página com os minutos. Um roteiro ligando cada bloco à sua página, mostrando o que entra e o que sai de cada exercício, deixando explícito que o bloco 1 consome o exercício do bloco 4 da Aula 1 e que o bloco 3 consome o exercício do bloco 2 desta aula. Uma seção curta dizendo como esta aula prepara a Aula 3.

Sem data real de calendário, seguindo a decisão já em vigor para todo o site.

- [ ] **Step 4: Escrever `docs/modulo-2-plataforma-e-modelos/sintese.md`**

Checklist do que precisa permanecer, autoavaliação, fontes da aula inteira em APA.

- [ ] **Step 5: Verificar**

Run: `cd ~/code/projeto-arquitetura-software && python3 scripts/validate_content.py --module modulo-2-plataforma-e-modelos && .venv/bin/mkdocs build --strict`
Expected: violações esperadas nas quatro páginas de bloco, ainda em esqueleto (falta a seção Exercício). Zero violação em `index.md` e `sintese.md`. Build limpo.

- [ ] **Step 6: Commit**

```bash
git add mkdocs.yml docs/modulo-2-plataforma-e-modelos/
git commit -m "docs(modulo-2): navegacao, indice e sintese da Aula 2"
```

---

### Task 2: Bloco 1, registro de decisão arquitetural

**Files:**
- Modify: `docs/modulo-2-plataforma-e-modelos/bloco-1-registro-de-decisao-arquitetural.md`
- Modify (staging, fora da publicação): `.superpowers/sdd/2026-09-19-aula-2-adr-plataforma-modelos/gabaritos-extraidos.md`

**Interfaces:**
- Consumes: o exercício do bloco 4 da Aula 1 (`docs/modulo-1-fundamentos/bloco-4-estilos-arquiteturais.md`), que pede ao aluno escolher um estilo entre três comparados
- Produces: a ADR de estilo, artefato que o próprio aluno já teria em mãos ao chegar neste bloco

LEIA ANTES DE ESCREVER: `docs/modulo-1-fundamentos/bloco-4-estilos-arquiteturais.md` inteiro, para saber exatamente o que o exercício daquele bloco pediu, e `docs/modulo-1-fundamentos/bloco-1-arquitetura-e-papel-do-arquiteto.md` e `bloco-3-cenarios-e-significancia-arquitetural.md`, para casar padrão de anatomia e tom.

- [ ] **Step 1: Escrever a seção Conceito**

Cobrir: o que é uma decisão arquitetural, distinta de decisão de implementação (já ensinado no bloco 1 da Aula 1, pode ser referenciado com o local exato, sem repetir a explicação inteira). O que é um Architecture Decision Record, ADR, e o racional que ele documenta. O formato de Nygard, com as cinco partes: título, contexto, decisão, status, consequências. O formato MADR como alternativa mais estruturada, citando `MADR, sem data, Markdown Architectural Decision Records`. Por que manter o ADR versionado junto do código, como artefato vivo, em vez de documento externo estático.

Use dois domínios de exemplo distintos dos já usados como principal nos blocos adjacentes desta aula (o bloco 2 vai usar plataforma arquitetural, o bloco 4 vai usar C4, então evite repetir domínio principal com eles). Domínios sugeridos, ainda não usados como principal em bloco algum do curso: sistema de gestão hospitalar de leitos, ou plataforma de agendamento de serviços. Escolha dois.

- [ ] **Step 2: Escrever a seção Uso pelo arquiteto**

Parágrafo curto sobre por que o arquiteto escreve a ADR no momento da decisão, não depois, e por que isso importa para quem entra no projeto mais tarde.

- [ ] **Step 3: Escrever o Exercício 5**

Enunciado autocontido. Reintroduza a ACME em uma frase. Diga explicitamente: "No exercício do [bloco 4 da Aula 1](../modulo-1-fundamentos/bloco-4-estilos-arquiteturais.md), você comparou três estilos arquiteturais contra os dois cenários da ACME e defendeu um deles. Escreva a ADR que registra essa decisão, no formato de Nygard." Lista numerada com o que a ADR precisa conter: 1) título, 2) contexto, citando os dois cenários que motivaram a análise, 3) decisão, nomeando o estilo escolhido e ao menos um estilo alternativo descartado, 4) status, 5) consequências, ao menos uma positiva e uma negativa. NÃO peça para o aluno reler nenhum dado novo do caso, o exercício depende só do que ele já produziu.

- [ ] **Step 4: Título, linha de enquadramento, Antes de começar, Fontes**

Título funcional, por exemplo "Registro de decisão arquitetural". Antes de começar linka `../referencia/glossario.md`, mas confirme que os termos existem no glossário. Se "registro de decisão arquitetural" ou "ADR" não estiverem no glossário, ACRESCENTE a entrada em `docs/referencia/glossario.md`, seguindo o padrão das entradas já existentes, com definição em uma frase. Fontes cita Nygard (2011) e MADR (sem data), ambos listados na bibliografia (ver Task 6 desta lista, que atualiza a bibliografia, ou acrescente você mesmo as duas entradas em `docs/referencia/bibliografia.md` se ainda não existirem, no formato: "Nygard, M. (2011). *Documenting architecture decisions*. Cognitect Blog." e "MADR. (n.d.). *Markdown Architectural Decision Records*. https://adr.github.io/madr/", com a ressalva de que a data e a atribuição de Nygard não foram verificadas nesta sessão, apoiadas em conhecimento consolidado da área.

- [ ] **Step 5: Extrair o gabarito para o staging**

Critério de avaliação da ADR: uma resposta forte nomeia pelo menos um estilo descartado e explica por que ele perde para o escolhido num dos dois cenários, não só afirma a escolha. Escrever sob `## Bloco 1, registro de decisão arquitetural` em `.superpowers/sdd/2026-09-19-aula-2-adr-plataforma-modelos/gabaritos-extraidos.md`, criando o arquivo se não existir.

- [ ] **Step 6: Verificar**

Run: `python3 scripts/validate_content.py --module modulo-2-plataforma-e-modelos`
Expected: zero violação nesta página.

- [ ] **Step 7: Commit**

```bash
git add docs/modulo-2-plataforma-e-modelos/bloco-1-registro-de-decisao-arquitetural.md docs/referencia/bibliografia.md docs/referencia/glossario.md
git commit -m "docs(modulo-2): bloco 1, registro de decisao arquitetural"
```

---

### Task 3: Bloco 2, plataforma arquitetural

**Files:**
- Modify: `docs/modulo-2-plataforma-e-modelos/bloco-2-plataforma-arquitetural.md`
- Modify (staging): `.superpowers/sdd/2026-09-19-aula-2-adr-plataforma-modelos/gabaritos-extraidos.md`

**Interfaces:**
- Consumes: o estilo escolhido no bloco 4 da Aula 1
- Produces: a plataforma escolhida, consumida pelo Exercício 7 do bloco 3 desta mesma aula

LEIA: `2.2 Plataforma Arquitetural.md` na raiz do repositório, matéria-prima a reescrever, NÃO copiar. Esse arquivo mistura tecnologia de produto (Java EE, Spring Boot, Kafka) com estilo arquitetural de forma solta, sem a disciplina terminológica que este curso já fixou. Reescreva com rigor, definindo plataforma arquitetural como o conjunto de frameworks, bibliotecas e ferramentas que concretizam um estilo já decidido, nunca confundindo escolha de plataforma com escolha de estilo.

- [ ] **Step 1: Escrever a seção Conceito**

Cobrir: o que é plataforma arquitetural, e por que essa decisão vem depois da decisão de estilo, não antes ou junto. Como uma mesma plataforma pode concretizar mais de um estilo, e como um estilo pode ser implementado por mais de uma plataforma candidata. Critérios de comparação entre plataformas candidatas: maturidade, custo de licenciamento ou operação, disponibilidade de mão de obra qualificada, aderência ao estilo já escolhido, e compatibilidade com o que já existe no ambiente (relevante para o caso ACME, sistema legado). Dois domínios de exemplo distintos dos blocos adjacentes (bloco 1 usou os domínios sugeridos na Task 2, bloco 4 vai usar C4). Sugestões ainda não usadas: sistema de emissão de bilhetes de evento, ou plataforma de telemedicina.

- [ ] **Step 2: Escrever a seção Uso pelo arquiteto**

Como o arquiteto documenta a comparação de plataformas antes de decidir, para que a escolha resista a questionamento posterior.

- [ ] **Step 3: Escrever o Exercício 6**

Enunciado autocontido, reintroduzindo a ACME em uma frase e o resumo da linha de base (núcleo COBOL sobre CICS, camada web JSF e EJB, integrações em lote), extraído de `docs/caso-acme/linha-de-base.md`. Diga: "Considerando o estilo arquitetural que você escolheu no exercício do [bloco 4 da Aula 1](../modulo-1-fundamentos/bloco-4-estilos-arquiteturais.md), levante duas plataformas candidatas capazes de concretizar esse estilo, considerando que o núcleo COBOL sobre CICS permanece em operação durante a transição." Lista numerada: 1) nomear as duas plataformas candidatas, 2) comparar as duas por pelo menos três critérios, entre os apresentados no Conceito, 3) escolher uma e justificar considerando a restrição de convivência com o legado.

- [ ] **Step 4: Título, enquadramento, Antes de começar, Fontes**

Se "plataforma arquitetural" não estiver no glossário, acrescente a entrada. Fontes cita Ford e Richards (2020), já na bibliografia, se a comparação de plataformas remeter a atributo de qualidade favorecido por cada uma.

- [ ] **Step 5: Extrair o gabarito para o staging**, sob `## Bloco 2, plataforma arquitetural`, acrescentado ao arquivo já existente da Task 2, sem apagar a seção anterior.

- [ ] **Step 6: Verificar**

Run: `python3 scripts/validate_content.py --module modulo-2-plataforma-e-modelos`
Expected: zero violação nesta página.

- [ ] **Step 7: Commit**

```bash
git add docs/modulo-2-plataforma-e-modelos/bloco-2-plataforma-arquitetural.md docs/referencia/glossario.md
git commit -m "docs(modulo-2): bloco 2, plataforma arquitetural"
```

---

### Task 4: Bloco 3, ADR de plataforma

**Files:**
- Modify: `docs/modulo-2-plataforma-e-modelos/bloco-3-adr-de-plataforma.md`
- Modify (staging): `.superpowers/sdd/2026-09-19-aula-2-adr-plataforma-modelos/gabaritos-extraidos.md`

**Interfaces:**
- Consumes: a escolha de plataforma do exercício do bloco 2 desta aula
- Produces: a ADR de plataforma, segunda prática do formato ensinado no bloco 1

LEIA `docs/modulo-2-plataforma-e-modelos/bloco-1-registro-de-decisao-arquitetural.md` (já escrito pela Task 2) para não repetir a explicação do formato de Nygard, apenas referenciar com o local exato.

- [ ] **Step 1: Escrever a seção Conceito**

Não repita a explicação do formato de Nygard, que já está no bloco 1, referencie com "conforme o formato apresentado no [bloco 1](bloco-1-registro-de-decisao-arquitetural.md) desta aula". Em vez disso, aprofunde: o que muda quando a decisão registrada é de plataforma em vez de estilo, por exemplo a consequência de mudança de plataforma tende a ter custo de treinamento e de migração de código, diferente da consequência de mudança de estilo, que tende a ter custo de reestruturação de componentes. Dois domínios de exemplo, coerentes com a continuidade da aula, mas sem repetir o domínio principal do bloco 2.

- [ ] **Step 2: Escrever a seção Uso pelo arquiteto**

Como o arquiteto usa a segunda ADR para consolidar o hábito de registro, e como duas ADRs relacionadas (estilo e plataforma que o concretiza) devem se referenciar uma à outra no próprio texto.

- [ ] **Step 3: Escrever o Exercício 7**

Enunciado autocontido: "Escreva a ADR que registra a escolha de plataforma que você fez no exercício do [bloco 2](bloco-2-plataforma-arquitetural.md) desta aula, no mesmo formato de Nygard usado no [bloco 1](bloco-1-registro-de-decisao-arquitetural.md)." Lista numerada com as cinco partes do formato, mais uma instrução extra: a ADR de plataforma deve referenciar, no campo de contexto, a ADR de estilo escrita no bloco 1, pelo título dela.

- [ ] **Step 4: Título, enquadramento, Antes de começar, Fontes**

Fontes repete Nygard (2011) e MADR, já na bibliografia.

- [ ] **Step 5: Extrair o gabarito para o staging**, sob `## Bloco 3, ADR de plataforma`.

- [ ] **Step 6: Verificar**

Run: `python3 scripts/validate_content.py --module modulo-2-plataforma-e-modelos`
Expected: zero violação nesta página.

- [ ] **Step 7: Commit**

```bash
git add docs/modulo-2-plataforma-e-modelos/bloco-3-adr-de-plataforma.md
git commit -m "docs(modulo-2): bloco 3, ADR de plataforma"
```

---

### Task 5: Bloco 4, representação de modelos e C4 níveis 1 e 2

**Files:**
- Modify: `docs/modulo-2-plataforma-e-modelos/bloco-4-representacao-de-modelos-e-c4.md`
- Modify (staging): `.superpowers/sdd/2026-09-19-aula-2-adr-plataforma-modelos/gabaritos-extraidos.md`

**Interfaces:**
- Consumes: nenhum artefato de exercício anterior, mas usa a linha de base da ACME como base de modelagem
- Produces: nada consumido por tarefa futura desta aula

LEIA `3.1 Modelagem C4.md`, `3.2 Nível C1.md` e `3.3 Nível C2.md` na raiz do repositório, matéria-prima a reescrever, NÃO copiar. ATENÇÃO: a fonte original chama o quarto nível do modelo de "Diagrama de Código (C4)", confundindo o nome do nível com o nome do modelo inteiro, que também se chama C4. NÃO reproduza essa confusão. O modelo inteiro se chama C4 porque tem quatro níveis, Contexto, Contêineres, Componentes e Código, mas cada nível tem nome próprio, não "C4" outra vez. Como esta aula só cobre os níveis 1 e 2, mencione a existência dos níveis 3 e 4 en passant, sem detalhar, e sem repetir o erro de nomenclatura da fonte.

- [ ] **Step 1: Escrever a seção Conceito**

Cobrir: por que representar um modelo de arquitetura, e o que separa um bom modelo de um diagrama solto sem convenção (a revisão de modelagem arquitetural pedida na ementa). O modelo C4, criado por Brown, sua lógica de abstração progressiva. Nível 1, diagrama de contexto: o sistema, os atores humanos e os sistemas externos com que ele troca informação. Nível 2, diagrama de contêineres: como o sistema se decompõe em aplicações, bancos de dados e serviços, cada um com sua tecnologia. Use PELO MENOS UM diagrama Mermaid mostrando um exemplo de diagrama de contexto (nível 1) genérico, com pessoa, sistema principal e sistema externo, e outro mostrando um exemplo de diagrama de contêineres (nível 2), seguindo o padrão de Mermaid já usado em `docs/caso-acme/linha-de-base.md`. Dois domínios de exemplo, sem repetir o domínio principal do bloco 3.

- [ ] **Step 2: Escrever a seção Uso pelo arquiteto**

Como o arquiteto escolhe o nível de detalhe do diagrama conforme a audiência, alto nível para stakeholders de negócio, nível de contêineres para a própria equipe técnica.

- [ ] **Step 3: Escrever o Exercício 8**

Enunciado autocontido, reintroduzindo a ACME e um resumo da linha de base (núcleo COBOL sobre CICS, camada web JSF e EJB, ERP financeiro, ambiente virtual de aprendizagem, extraído de `docs/caso-acme/linha-de-base.md`). Lista numerada: 1) desenhar o diagrama de contexto (nível 1) da ACME, identificando o sistema acadêmico, os atores (aluno, secretaria) e os sistemas externos (ERP, ambiente virtual), 2) desenhar o diagrama de contêineres (nível 2), decompondo o sistema acadêmico nos contêineres que a linha de base já descreve (núcleo COBOL, camada web, integrações), 3) justificar em uma frase por que um stakeholder de negócio só precisaria ver o diagrama de contexto. Peça que os dois diagramas sejam entregues em Mermaid ou em desenho livre, à escolha do aluno.

- [ ] **Step 4: Título, enquadramento, Antes de começar, Fontes**

Se "modelo C4" ou termos equivalentes não estiverem no glossário, acrescente. Fontes cita Brown (n.d.), a ser acrescentado à bibliografia se ainda não estiver (Task 6 desta lista trata a bibliografia, mas acrescente você mesmo se chegar aqui primeiro).

- [ ] **Step 5: Extrair o gabarito para o staging**, sob `## Bloco 4, representação de modelos e C4`.

- [ ] **Step 6: Verificar**

Run: `python3 scripts/validate_content.py && .venv/bin/mkdocs build --strict`
Expected: ZERO violação em todo o repositório, porque esta é a última página de bloco desta aula. Build limpo.

- [ ] **Step 7: Commit**

```bash
git add docs/modulo-2-plataforma-e-modelos/bloco-4-representacao-de-modelos-e-c4.md docs/referencia/bibliografia.md docs/referencia/glossario.md
git commit -m "docs(modulo-2): bloco 4, representacao de modelos e C4 niveis 1 e 2"
```

---

### Task 6: Gabaritos no PKA e verificação final

**Files:**
- Modify: `/Users/marcomendes/Library/CloudStorage/Dropbox/Pessoal/pka/projects/aulas/PRJ-aulas-iec-asd-10-estrategias-e-projeto-de-arquitetura-de-software.md`

**Interfaces:**
- Consumes: `.superpowers/sdd/2026-09-19-aula-2-adr-plataforma-modelos/gabaritos-extraidos.md`, com as quatro seções das tarefas 2 a 5

Este arquivo fica fora do repositório do site, mesmo padrão da Task 8 da revisão anterior.

- [ ] **Step 1: Ler o arquivo de staging com os quatro gabaritos extraídos**

- [ ] **Step 2: Acrescentar `## Gabaritos, Aula 2` à narrativa do PKA**, logo após a seção `## Gabaritos, Aula 1` já existente, com os quatro gabaritos reescritos com mais profundidade que no site: distinção entre resposta excelente e aceitável em cada um, e resposta de referência completa onde fizer sentido, por exemplo uma ADR de exemplo completa para o bloco 1 e uma para o bloco 3, e um par de diagramas de referência (contexto e contêineres da ACME) para o bloco 4.

- [ ] **Step 3: Narrativa datada de 19/09/2026** registrando a criação do Módulo 2 e a correção retroativa da ementa da Aula 1.

- [ ] **Step 4: Verificar**

Run: `cd ~/pka && python3 system/scripts/validate-pka.py --files "projects/aulas/PRJ-aulas-iec-asd-10-estrategias-e-projeto-de-arquitetura-de-software.md"`
Expected: 0 erros.

- [ ] **Step 5: Verificação final do site**

Run:
```
cd ~/code/projeto-arquitetura-software
python3 -m unittest discover -s tests -v
python3 scripts/validate_content.py
.venv/bin/mkdocs build --strict
```
Expected: testes OK, zero violação em todo o repositório, build limpo.

Confirme com grep que nenhuma página nova usa a palavra "prosa", que os quatro exercícios estão numerados 5, 6, 7, 8, que nenhuma página nova tem `## Gabarito`, e que MVC, MVVM, DDD e Strangler não aparecem em lugar nenhum.

- [ ] **Step 6: Servir o site e conferir a renderização**

Run: `.venv/bin/mkdocs serve &`, esperar, depois `curl` nas quatro páginas de bloco do Módulo 2 e na página inicial, confirmando 200 em todas. Confirmar que os diagramas Mermaid do bloco 4 aparecem como `<pre class="mermaid">` no HTML servido. Parar o servidor.

- [ ] **Step 7: Commit final**, se houver correção. Se tudo já estiver certo, não commitar vazio.
