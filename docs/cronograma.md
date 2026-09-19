# Cronograma

A disciplina tem seis aulas, das 19h00 às 22h30, com intervalo das 20h30 às 20h45 e encerramento do conteúdo até as 22h10. Cada aula é dividida em quatro blocos de quarenta minutos, com vinte e cinco minutos de conceito e quinze de exercício.

As datas de cada oferta não aparecem aqui. Elas são divulgadas pela instituição a cada turma, e este cronograma descreve apenas a sequência dos temas, que não muda entre ofertas.

## Sequência das aulas

As duas primeiras aulas estabelecem os fundamentos e as duas decisões maiores, estilo e plataforma. As quatro seguintes percorrem os domínios da arquitetura e fecham no que permanece incerto.

| Aula | Tema |
| --- | --- |
| 1 | Arquitetura, papel do arquiteto, atributos de qualidade, cenários de significância arquitetural e estilos arquiteturais |
| 2 | Registro de decisão arquitetural, plataforma arquitetural, ADR de plataforma e modelagem C4 |
| 3 | Arquitetura de aplicação e serviços |
| 4 | Arquitetura de integração e arquitetura de dados |
| 5 | Arquitetura de segurança e modelo técnico de referência |
| 6 | Mapa de riscos arquiteturais e organização de provas de conceito |

O encadeamento das aulas 3 a 6 vai de estrutura para comunicação, depois para proteção, e termina em incerteza. A Aula 3 recorta o sistema em serviços. A Aula 4 define como esses serviços conversam e quem é dono de cada dado. A Aula 5 define como o conjunto se protege e com que tecnologias. A Aula 6 identifica o que ainda não se sabe e organiza os experimentos que respondem a isso.

## Blocos de cada aula

### Aula 1, fundamentos

| Bloco | Tema | Exercício |
| --- | --- | --- |
| 1 | Arquitetura e papel do arquiteto | 1 |
| 2 | Qualidade e tipos de requisito | 2 |
| 3 | Cenários e significância arquitetural | 3 |
| 4 | Estilos arquiteturais | 4 |

### Aula 2, plataforma e modelos

| Bloco | Tema | Exercício |
| --- | --- | --- |
| 1 | Registro de decisão arquitetural | 5 |
| 2 | Plataforma arquitetural | 6 |
| 3 | ADR de plataforma | 7 |
| 4 | Representação de modelos e C4, níveis de contexto e de contêineres | 8 |

### Aula 3, aplicação e serviços

| Bloco | Tema | Exercício |
| --- | --- | --- |
| 1 | Arquitetura de aplicação, do contêiner ao componente, e a tríade de táticas | 9 |
| 2 | Decomposição em serviços, critérios de recorte e granularidade | 10 |
| 3 | Contrato de serviço, compatibilidade e versionamento | 11 |
| 4 | Convivência com o legado, fachada e extração incremental | 12 |

### Aula 4, integração e dados

| Bloco | Tema | Exercício |
| --- | --- | --- |
| 1 | Arquitetura de integração, síncrono e assíncrono, mediado e ponto a ponto | 13 |
| 2 | Do lote ao evento, garantias de entrega, ordem e idempotência | 14 |
| 3 | Arquitetura de dados, propriedade do dado e convivência com banco compartilhado | 15 |
| 4 | Táticas de dados, consistência, réplica de leitura e retenção | 16 |

### Aula 5, segurança e modelo técnico de referência

| Bloco | Tema | Exercício |
| --- | --- | --- |
| 1 | Arquitetura de segurança, identidade, autenticação e autorização | 17 |
| 2 | Proteção de dado e conformidade, criptografia, trilha de auditoria e residência de dados | 18 |
| 3 | Modelo técnico de referência, a taxonomia de serviços de plataforma | 19 |
| 4 | Montagem do modelo técnico de referência e as restrições que o moldam | 20 |

### Aula 6, riscos e provas de conceito

| Bloco | Tema | Exercício |
| --- | --- | --- |
| 1 | Risco arquitetural, identificação e classificação | 21 |
| 2 | Plano de resposta a risco | 22 |
| 3 | Prova de conceito, a pergunta delimitada e o critério de sucesso | 23 |
| 4 | Organização e encerramento de provas de conceito | 24 |

## Avaliação

Cada aula vale dez pontos, distribuídos entre os quatro exercícios daquela aula, somando sessenta pontos nas seis aulas. A participação nos encontros ao vivo vale quarenta pontos. Não há trabalho final entregue após a última aula, porque os exercícios de cada aula já são o instrumento de avaliação.

## Como os artefatos se encadeiam

Os exercícios não são independentes entre si. O artefato produzido em um bloco costuma ser a entrada do bloco seguinte, e o [caso ACME](caso-acme/index.md) é o mesmo em toda a disciplina. A página de [artefatos por aula](caso-acme/artefatos.md) descreve o que cada exercício produz, com que entrada do dossiê e sob qual critério de aceitação.
