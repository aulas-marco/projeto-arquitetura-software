# Template do caderno arquitetural

O caderno arquitetural é o documento de arquitetura da solução da ACME. Ele reúne, em dez seções, as decisões que o curso ensina a tomar, cada uma ligada ao requisito que a motivou. A tabela de cada seção indica o que vai nela, a pergunta que responde, os artefatos que a compõem, a entrada de que depende e o exercício que a preenche. As [convenções](convencoes.md) definem os códigos dos artefatos, e o [mapa](mapa.md) relaciona seção, bloco e exercício.

{{trilha:todas}}

{{folha:0}}

## A solução em uma página

| Campo | Conteúdo |
| --- | --- |
| O que vai | O problema, a pergunta, a decisão central, o requisito que guia o desenho, o que a organização aceita em troca e o estado das decisões |
| Pergunta que responde | O que um leitor que lesse só esta página precisaria saber para apoiar ou questionar o projeto |
| Artefatos | Cinco parágrafos curtos, um para cada item acima, e uma linha de estado que diz o que está proposto e o que depende de prova |
| Entrada | Todas as seções seguintes, porque o resumo só repete o que elas já registram |
| Preenchida em | Revista ao fim de cada aula, nos exercícios 4, 8, 12, 16, 20 e 24, e fechada no exercício 24 |

{{/folha}}

{{folha:1}}

## 1. Contexto

| Campo | Conteúdo |
| --- | --- |
| O que vai | A instituição e os números do problema, as restrições que chegam fechadas, as respostas já excluídas, as decisões classificadas por nível de arquitetura, os componentes da solução nos cinco tipos e os papéis de quem decide |
| Pergunta que responde | Que organização é esta, que problema ela precisa resolver e quem decide cada parte |
| Artefatos e códigos | Tabela de porte, tabela de restrições com origem e efeito, decisões D1 a Dn pelo nível que cada uma toma, premissas PR1 a PRn |
| Entrada | O dossiê do caso ACME, em particular a página inicial do caso e os dados operacionais |
| Preenchida em | Aula 1, exercícios 1 a 4 |

{{/folha}}

{{folha:2}}

## 2. Partes interessadas

| Campo | Conteúdo |
| --- | --- |
| O que vai | Os papéis envolvidos, o que cada um quer e teme, o tratamento dado a cada um, os conflitos de expectativa, os pontos de vista e a declaração de escopo do primeiro ciclo |
| Pergunta que responde | Quem precisa ser envolvido nas decisões e onde as expectativas se chocam |
| Artefatos e códigos | Matriz de partes interessadas com tratamento (envolver, consultar, manter informado), pontos de vista, declaração de escopo com o que muda, o que permanece e a origem de cada exclusão |
| Entrada | Seção 1, em particular as restrições fechadas e o mapa de atores |
| Preenchida em | Aula 2, exercício 8 |

{{/folha}}

{{folha:3}}

## 3. Requisitos

| Campo | Conteúdo |
| --- | --- |
| O que vai | Os direcionadores de mudança classificados, o catálogo de requisitos com tipo, medida e prioridade, os requisitos vagos reescritos de forma mensurável, os cenários de qualidade e os requisitos derivados |
| Pergunta que responde | O que a solução precisa entregar e com que medida se verifica que entregou |
| Artefatos e códigos | Direcionadores com evidência, catálogo R1 a Rn, requisitos derivados RD1 a RDn, cenários CQ com seis elementos (fonte, estímulo, ambiente, artefato, resposta, medida) |
| Entrada | Seções 1 e 2, porque restrição e parte interessada delimitam o que é requisito |
| Preenchida em | Aula 2, exercícios 5, 6 e 7 |

{{/folha}}

{{folha:4}}

## 4. Linha de base e lacunas

| Campo | Conteúdo |
| --- | --- |
| O que vai | A descrição da arquitetura atual, com camadas, integrações, incidentes e dívida técnica, e a lista das lacunas entre a linha de base e a arquitetura alvo |
| Pergunta que responde | Como o sistema é hoje, onde ele é frágil e o que falta para chegar ao alvo |
| Artefatos e códigos | Descrição da linha de base, tabela de incidentes com causa e impacto, relatório de lacunas L1 a Ln com domínio, forma de fechamento e onda |
| Entrada | Seção 3 para a linha de base, e as seções 5 a 8 para a arquitetura alvo com que a linha de base é comparada |
| Preenchida em | Linha de base na Aula 2, exercício 7, e lacunas na Aula 6, exercício 21 |

{{/folha}}

{{folha:5}}

## 5. Contexto do sistema (C4, nível 1)

| Campo | Conteúdo |
| --- | --- |
| O que vai | O diagrama de contexto do sistema, com a fronteira da solução, os perfis de usuário e os sistemas externos, e a razão de cada elemento ficar dentro ou fora da fronteira |
| Pergunta que responde | O que está dentro da solução, o que fica fora e com quem ela se relaciona |
| Artefatos e códigos | Diagrama C4 de nível 1 com legenda e um parágrafo que justifica a fronteira |
| Entrada | Seções 2 e 4, porque as partes interessadas e a linha de base definem usuários e sistemas externos |
| Preenchida em | Aula 4, exercício 15 |

{{/folha}}

{{folha:6}}

## 6. Princípios

| Campo | Conteúdo |
| --- | --- |
| O que vai | As regras que orientam todas as decisões de design, cada uma com o que ela proíbe e com o requisito ou a restrição que a motiva |
| Pergunta que responde | Que regras o desenho precisa respeitar, de modo que uma decisão possa ser recusada por violá-las |
| Artefatos e códigos | Tabela de princípios P1 a Pn, com a proibição correspondente e a rastreabilidade ao requisito |
| Entrada | Seções 1 e 3, porque os princípios derivam de restrições e de requisitos |
| Preenchida em | Aula 3, exercício 9 |

{{/folha}}

{{folha:7}}

## 7. Decisões

| Campo | Conteúdo |
| --- | --- |
| O que vai | As decisões de desenho, de padrões, de negócio, de dados, de aplicações e integração e de infraestrutura, cada uma com a escolha, o requisito a que responde e o registro de decisão arquitetural que a formaliza |
| Pergunta que responde | Que decisões estruturais foram tomadas, com que compromisso e como se confirma que valeram |
| Artefatos e códigos | Decisões de design DD1 a DDn, decisões de legado e dados DL1 a DLn, blocos B1 a Bn, interfaces I1 a In, registros ADR 001 a ADR nnn |
| Entrada | Seções 3 e 6, porque cada decisão responde a requisito e obedece a princípio |
| Preenchida em | Aulas 3 e 4, exercícios 10, 11, 12, 13, 14 e 16 |

{{/folha}}

{{folha:8}}

## 8. Tecnologia e plataforma

| Campo | Conteúdo |
| --- | --- |
| O que vai | O modelo técnico de referência em cinco colunas, a matriz de seleção, a plataforma e a zona de pouso escolhidas, a avaliação de segurança fim a fim, o registro de decisão da plataforma e as lacunas de provisão |
| Pergunta que responde | Com que tecnologia a solução pode ser construída, sobre que plataforma ela executa e como se protege |
| Artefatos e códigos | Modelo técnico de referência com classificação verde, âmbar e vermelho, matriz dos seis critérios, quadro comparativo de plataformas, ativos classificados, grade de permissões, ameaças por categoria STRIDE, controles C1 a Cn, ADR de plataforma |
| Entrada | Seções 5 e 7, porque os contêineres e as decisões estruturais definem o que a tecnologia precisa realizar |
| Preenchida em | Aula 5, exercícios 17, 18, 19 e 20 |

{{/folha}}

{{folha:9}}

## 9. Roteiro e governança

| Campo | Conteúdo |
| --- | --- |
| O que vai | A ordem em que a mudança acontece, em ondas com entregas, valor e critério de conclusão, e o modo como a arquitetura é governada durante e depois da execução |
| Pergunta que responde | Em que ordem as lacunas se fecham e como se impede que a arquitetura derive depois de aprovada |
| Artefatos e códigos | Tabela de ondas, conselho de revisão com periodicidade, funções de aptidão FA1 a FAn, registro de dívida técnica, níveis de serviço |
| Entrada | Seção 4, porque as lacunas confirmadas são a matéria das ondas |
| Preenchida em | Aula 6, exercícios 22 e 23 |

{{/folha}}

{{folha:10}}

## 10. O que ainda falta decidir

| Campo | Conteúdo |
| --- | --- |
| O que vai | As pendências que impedem fechar uma decisão e a pessoa ou o grupo com autoridade para resolvê-las |
| Pergunta que responde | O que ainda depende de decisão ou de verificação e quem decide |
| Artefatos e códigos | Tabela de pendência e responsável, com a tendência tecnológica avaliada no encerramento |
| Entrada | Todas as seções anteriores, porque cada premissa não confirmada gera uma pendência |
| Preenchida em | Revista ao fim de cada aula, nos exercícios 4, 8, 12, 16, 20 e 24, e fechada no exercício 24 |

{{/folha}}
