# Módulo 4, bloco 0, espinha dorsal dos domínios

Data: 03/10/2026. Situação: desenho aprovado em conversa com o autor do curso, pendente de revisão desta especificação.

## 1. Objetivo

A Aula 4 detalha a solução em quatro domínios, negócio, dados, aplicações e infraestrutura, e hoje a ligação entre eles só aparece de forma explícita na síntese, ao fim da aula. O bloco 0 abre a aula com um modelo conceitual que mostra o que o arquiteto de solução faz em cada domínio e como esse trabalho se encadeia, de modo que os blocos 1 a 4 sejam lidos como aprofundamento de uma estrutura já apresentada.

Critério de sucesso: antes de qualquer detalhe, o aluno consegue dizer, para cada domínio, que pergunta o arquiteto responde, o que recebe e de quem, o que decide, o que entrega ao domínio seguinte e o que não assume.

## 2. Decisões de escopo

| Decisão | Escolha |
| --- | --- |
| Alcance | Espinha dorsal da Aula 4, sem bloco 0 nas demais aulas |
| Natureza | Conceitual, centrada no trabalho do arquiteto de solução, sem caso e sem exemplo de organização |
| Forma | Pilha dos quatro domínios com fio de rastreabilidade de decisões e hierarquia de serviços como eixo lateral |
| Tempo | Abertura de 10 minutos em aula, tirados dos blocos 1 e 2 |
| Exercício | Nenhum. A prática da aula continua na cadeia dos exercícios 13 a 16 |
| Caso ACME | Ausente do bloco 0. Continua apenas nos exercícios dos blocos 1 a 4 |

## 3. Página do bloco 0

Arquivo `docs/modulo-4-dominios-da-solucao/bloco-0-espinha-dorsal-dos-dominios.md`, com título de navegação "Bloco 0: os quatro domínios numa só solução", inserido logo após a visão geral da aula.

Anatomia: "Antes de começar", seção de conceito, "Uso pelo arquiteto" e "Fontes", sem "Exercício".

Conteúdo da seção de conceito, na ordem:

1. O papel nos domínios. O arquiteto de solução não modela a organização inteira. Em cada domínio ele consulta o que a arquitetura corporativa e as áreas especialistas mantêm, decide o que é próprio da solução e entrega ao domínio seguinte a decisão de que ele precisa. O parágrafo liga ao papel do arquiteto apresentado no bloco 3 da Aula 1.
2. A figura central, descrita na seção 4.
3. Tabela de quatro linhas, uma por domínio, com as colunas pergunta que o arquiteto responde, o que recebe e de quem, o que decide, artefato que produz, e limite do papel. Os limites registrados são a modelagem de processos, que cabe à análise de negócio, o modelo corporativo de dados, que cabe à arquitetura de dados, a escolha de produto, que cabe à Aula 5, e a operação da plataforma, que cabe à infraestrutura.
4. A hierarquia de serviços, do serviço de negócio ao serviço de tecnologia, como explicação da ordem dos domínios, porque cada camada se justifica pelo serviço que sustenta.

"Uso pelo arquiteto" traz um roteiro de quatro perguntas, uma por domínio, que os blocos 1 a 4 retomam com a mesma redação.

"Fontes" cita Lovatt (2021), seções 1.5 a 1.7, papel do arquiteto de solução, e seções 2.3 a 2.7, domínios da arquitetura, além do material do curso.

## 4. Figura central

Arquivo `docs/assets/images/modulo-4-b0-espinha-dorsal.svg`, com viewBox de 1.200 de largura, fonte mínima de 16 px, `<title>` e `<desc>`, paleta das demais figuras e sem dado da ACME.

Composição de cima para baixo:

- Faixa de entrada: "Aula 3, estilo e padrões registrados em ADR".
- Quatro camadas, cada uma com o nome do domínio, a pergunta do arquiteto e três colunas, Recebe, Decide e Entrega.

| Domínio | Recebe | Decide | Entrega |
| --- | --- | --- | --- |
| Negócio | Mapa de capacidades, fluxo de valor e modelo de processo, da arquitetura corporativa e da análise de negócio | Onde a mudança incide | Capacidades, etapas e atividades afetadas |
| Dados | Capacidades afetadas e modelo de dados corporativo | Dono, fonte de verdade, regime de consistência e obrigações do dado | Grade dado × aplicação |
| Aplicações | Grade dado × aplicação e portfólio de aplicações | Aplicações que mudam, interfaces, contratos e fronteira da solução | Diagramas de contexto e de contêineres e contratos de integração |
| Infraestrutura | Contêineres e relações | Modo, volume e latência de cada relação, camada de execução e topologia | Diagrama de implantação e exigências para a definição tecnológica |

- Faixa de saída: "Aula 5, definição tecnológica".
- Fio de rastreabilidade: seta ortogonal da coluna Entrega de cada camada à coluna Recebe da camada seguinte, da faixa de entrada à faixa de saída.
- Eixo lateral à esquerda: serviço de negócio e processo junto ao negócio, informação que sustenta os serviços junto aos dados, serviço de aplicação e componente junto às aplicações, serviço de tecnologia junto à infraestrutura.
- A coluna Decide recebe destaque de cor. Recebe e Entrega ficam neutras.

## 5. Retomadas nos blocos 1 a 4

Quatro figuras reduzidas, `modulo-4-b0-mapa-negocio.svg`, `modulo-4-b0-mapa-dados.svg`, `modulo-4-b0-mapa-aplicacoes.svg` e `modulo-4-b0-mapa-infraestrutura.svg`, com as quatro camadas empilhadas, só o nome do domínio e a frase da coluna Decide, a camada do bloco destacada e as demais esmaecidas, em altura baixa.

Cada bloco de 1 a 4 abre a seção de conceito com a figura reduzida e uma frase no padrão "No mapa do bloco 0, este bloco trata do domínio de X: o arquiteto recebe A, decide B e entrega C", que substitui o parágrafo de abertura que hoje explica a ordem dos domínios.

No bloco 3, a seção da hierarquia de serviços passa a retomar o eixo do bloco 0, com link, e mantém a Figura 4, que detalha as camadas do contrato.

A seção "Uso pelo arquiteto" de cada bloco começa com a pergunta do roteiro do bloco 0 correspondente ao domínio.

A seção "Cadeia dos domínios" da síntese remete ao bloco 0 e à figura central, e continua descrevendo a cadeia dos exercícios 13 a 16.

## 6. Grade de tempo

| Horário | Atividade | Duração (min) |
| --- | --- | --- |
| 19h00–19h15 | Questões sobre a Aula 3 | 15 |
| 19h15–19h25 | Kahoot de revisão da Aula 3 | 10 |
| 19h25–19h35 | Bloco 0, os quatro domínios numa só solução | 10 |
| 19h35–20h03 | Bloco 1, arquitetura de negócio da solução | 28 |
| 20h03–20h30 | Bloco 2, arquitetura de dados da solução | 27 |
| 20h30–20h45 | Intervalo | 15 |
| 20h45–20h55 | Kahoot dos blocos 1 e 2 | 10 |
| 20h55–21h28 | Bloco 3, arquitetura de aplicações e integração | 33 |
| 21h28–22h00 | Bloco 4, arquitetura de infraestrutura da solução | 32 |
| 22h00–22h10 | Kahoot dos blocos 3 e 4 | 10 |

A soma dos blocos 0 a 4 permanece em 130 minutos.

## 7. Arquivos previstos

| Arquivo | Alteração |
| --- | --- |
| `docs/modulo-4-dominios-da-solucao/bloco-0-espinha-dorsal-dos-dominios.md` | Novo |
| `docs/assets/images/modulo-4-b0-espinha-dorsal.svg` | Novo |
| `docs/assets/images/modulo-4-b0-mapa-{negocio,dados,aplicacoes,infraestrutura}.svg` | Novos |
| `docs/modulo-4-dominios-da-solucao/bloco-{1,2,3,4}-*.md` | Figura reduzida, frase de abertura e pergunta no "Uso pelo arquiteto" |
| `docs/modulo-4-dominios-da-solucao/index.md` | Objetivo novo, grade, roteiro |
| `docs/modulo-4-dominios-da-solucao/sintese.md` | Remissão ao bloco 0 na cadeia dos domínios |
| `docs/cronograma.md` | Bloco 0 na lista da Aula 4 |
| `docs/referencia/glossario.md` | Entrada "Espinha dorsal dos domínios" |
| `mkdocs.yml` | Entrada de navegação |
| `scripts/validate_content.py` | Página `bloco-0-*` dispensada da seção Exercício |
| `tests/test_content_contract.py` | Teste da dispensa no validador |
| `tests/test_modulo_4_contract.py` | Testes do bloco 0 e das retomadas |
| `tests/test_exercicios_fora_da_sala.py` | Grade com a linha do bloco 0 |

## 8. Regras editoriais

Valem as regras do curso: português com acentuação completa, registro impessoal, sem neologismo, metáfora, idiomatismo ou antítese, parágrafo que termina com dado, sem ponto e vírgula em prosa, no máximo um travessão por parágrafo, autor citado só nas Fontes e nas legendas, conceitos já vistos ligados por link ao bloco de origem. O termo "espinha dorsal" aparece só no título e no glossário, e o corpo descreve o encadeamento em termos literais.

## 9. Validação e critérios de aceite

1. `python3 -m pytest -q`, `python3 scripts/validate_content.py` e `mkdocs build --strict` sem falha.
2. O validador dispensa a seção Exercício só em `bloco-0-*` e continua exigindo-a nos blocos 1 a 4.
3. A página do bloco 0 está no menu, contém os quatro domínios e as palavras recebe, decide e entrega, e não contém "ACME", "Hospital", "Clínica", "COBOL" ou "matrícula".
4. A figura central e as quatro reduzidas têm `<title>`, `<desc>`, fonte mínima de 16 px e nenhum dado da ACME.
5. Cada bloco de 1 a 4 referencia o bloco 0 e a sua figura reduzida.
6. A grade da Aula 4 tem a linha do bloco 0, e os blocos 0 a 4 somam 130 minutos, com três Kahoots.
7. A figura central e as reduzidas foram conferidas renderizadas a 688 px de coluna.
