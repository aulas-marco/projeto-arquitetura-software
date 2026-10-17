# Inventário de cobertura da revisão

Este inventário cobre as **72 páginas publicáveis** encontradas em `docs/`, excluindo `docs/superpowers/`, que não é publicado. Ele não afirma que todas as linhas foram reescritas. Indica onde a revisão de linguagem, conexão e visual deve ser aplicada para que o aluno não encontre formulações incompatíveis entre explicação, prática e projeto acumulado.

## Módulos de aula

| Área | Páginas | Tratamento de revisão |
| --- | --- | --- |
| Módulo 1 · Fundamentos | `index.md`, `bloco-1-arquitetura-de-solucoes-e-de-software.md`, `bloco-2-a-solucao-como-sistema.md`, `bloco-3-papel-do-arquiteto-de-solucao.md`, `bloco-4-processo-de-definicao-da-arquitetura.md`, `sintese.md` | Prioridade alta. Explicar alcance de decisão, componentes da solução, papel do arquiteto, processo e relação com o Projeto de Arquitetura de Solução. Inserir os primeiros links prospectivos para requisitos, pessoas envolvidas, decisões e governança. |
| Módulo 2 · Requisitos e partes interessadas | `index.md`, quatro páginas `bloco-*.md`, `sintese.md` | Prioridade alta. Tornar concretos direcionador, requisito, cenário, restrição, linha de base, parte interessada, ponto de vista, visão e escopo. Ligar cada conceito às decisões e modelos que ele sustenta. |
| Módulo 3 · Design e padrões | `index.md`, quatro páginas `bloco-*.md`, `sintese.md` | Prioridade alta. Tornar explícita a passagem de entrada para princípio, de princípio para decisão e de decisão para ADR, consequência e revisão. Preservar o repertório e o detalhamento dos padrões. |
| Módulo 4 · Domínios da solução | `index.md`, `bloco-0-espinha-dorsal-dos-dominios.md`, quatro páginas `bloco-*.md`, `sintese.md` | Prioridade alta. É a principal ponte para alunos com repertório técnico: explicar capacidade, fluxo de valor, processo, dado, contrato, fronteira e topologia por perguntas práticas. Reforçar que os quatro domínios descrevem a mesma solução. |
| Módulo 5 · Frameworks e tecnologias | `index.md`, quatro páginas `bloco-*.md`, `sintese.md` | Prioridade alta. Explicar que escolher tecnologia inclui operação, custo, competências, contrato, segurança e evidências. Manter TRM, critérios, plataforma, zona de pouso, segurança e ADR completos. |
| Módulo 6 · Governança, IA e caderno | `index.md`, três páginas `bloco-*.md`, `sintese.md` | Prioridade alta. Substituir metáforas de fiscalização por ações observáveis: comparar, propor, aprovar, registrar, verificar e revisar. Conectar rastreabilidade ao projeto inteiro, não somente ao percurso de um requisito. |

## Caso, caderno, referência e páginas de apoio

| Área | Páginas | Tratamento de revisão |
| --- | --- | --- |
| Início e cronograma | `index.md`, `cronograma.md` | Apresentar explicitamente o caderno como o documento que reúne o Projeto de Arquitetura de Solução. Manter a sequência e o detalhamento de cada aula. |
| Caso ACME | `caso-acme/index.md`, `linha-de-base.md`, `dados-operacionais.md`, `artefatos.md` | Manter o caso autossuficiente. Tornar mais diretas as explicações sobre contratos, custos, interesses, incidentes e dados operacionais. Em `artefatos.md`, reforçar a relação entre entradas, produto produzido e partes do projeto que usam esse produto. |
| Caderno arquitetural | `caderno/template.md`, `convencoes.md`, `mapa.md` | Preservar todas as 11 seções e seus campos. Inserir links de mão dupla entre requisito, restrição, decisão, modelo, verificação, responsável e pendência. Não adicionar obrigação de preenchimento além do que já existe. |
| Gabaritos | `gabaritos/index.md` e `gabarito-exercicio-01.md` a `gabarito-exercicio-24.md` | Revisar pela fonte em `caderno-fonte/` e regenerar. Manter o caráter cumulativo e a indicação clara de que se trata de resposta de consulta, não de material que substitui a realização do exercício. |
| Glossário e bibliografia | `referencia/glossario.md`, `referencia/bibliografia.md` | O glossário deve explicar termos e devolver o aluno ao bloco em que os utiliza. Bibliografia mantém suas referências e seu vocabulário formal; só revisar textos explicativos ao redor das referências quando necessário. |

## Ordem recomendada de edição

1. `docs/index.md`, `docs/caderno/convencoes.md`, `docs/caderno/mapa.md` e as orientações em `caderno-fonte/`: estabelecem o vocabulário e a navegação do projeto completo.
2. Módulos 1 e 2: dão ao aluno o contexto para compreender por que as decisões posteriores existem.
3. Módulos 3 e 4: conectam decisões, modelos e os quatro domínios.
4. Módulos 5 e 6: conectam a realização tecnológica ao risco, à transição e ao acompanhamento.
5. Glossário, caso ACME e gabaritos: alinham terminologia, exemplos e produtos cumulativos com as revisões feitas.
6. Sínteses e páginas de visão geral: validam que cada aula apresente sua contribuição para o projeto e os links de entrada e saída.

## Origem dos conteúdos cumulativos

| Conteúdo publicado | Fonte que deve receber a revisão | Ação posterior |
| --- | --- | --- |
| Template, orientações de seção e exercícios do caderno | `caderno-fonte/00-resumo.md` a `caderno-fonte/10-pendencias.md` | Rodar `python3 scripts/gerar_caderno.py` e conferir `python3 scripts/gerar_caderno.py --check` |
| Gabaritos 1 a 24 | Os mesmos arquivos em `caderno-fonte/` | Regenerar; não editar cada cópia cumulativa isoladamente |
| Introduções estruturais geradas | `scripts/gerar_caderno.py`, quando a passagem estiver no texto gerado | Alterar a origem e validar a saída |
| Páginas de módulo, caso, glossário e cronograma | Arquivo Markdown correspondente em `docs/` | Validar links, âncoras e regras editoriais |

## Condição de encerramento editorial

A revisão estará pronta quando as páginas de módulo, o caso, o template, os exercícios, os gabaritos e o glossário empregarem a mesma distinção conceitual; quando as relações principais do projeto puderem ser percorridas pelos links; e quando os esquemas respondam às perguntas que o texto apresenta, sem retirar detalhamento do template ou do conteúdo de aula.
