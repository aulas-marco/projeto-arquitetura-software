# Módulo 4, domínios da arquitetura de solução

**Data:** 02/10/2026

**Estado:** em revisão pelo professor

**Escopo:** produção integral da Aula 4 e ajuste do cronograma das Aulas 4 e 5

## 1. Objetivo

O módulo detalha a arquitetura de solução nos quatro domínios que Lovatt (2021, capítulo 2) distingue além da segurança: negócio, dados, aplicações e infraestrutura. A progressão parte da decisão estrutural registrada na Aula 3 e leva o aluno a descrever, domínio a domínio, o que a modernização da ACME muda, até a representação da arquitetura alvo nos níveis de contexto e de contêineres do modelo C4.

Ao final da aula, o aluno deverá conseguir:

- usar modelos de arquitetura de negócio para localizar o que a solução muda no negócio
- distinguir dado, informação e metadado, e atribuir dono, consumidores e regime de consistência a cada entidade
- classificar aplicações do portfólio pela situação estratégica e descrever uma interface pelos seis atributos de Lovatt
- distinguir padrão técnico, protocolo, especificação e contrato de integração
- reconhecer o nível correto de cada elemento num diagrama de contexto e num diagrama de contêineres
- relacionar cada interface entre contêineres ao modo de comunicação, ao volume e à latência que ela exige

## 2. Decisões de escopo

A organização por domínios foi definida pelo professor em 02/10/2026 e substitui a organização anterior do cronograma, que reunia aplicações e dados, infraestrutura e segurança, contrato de integração e C4 em quatro blocos temáticos. Contrato de integração e C4 deixam de ser blocos próprios e passam a ser instrumentos dos blocos de aplicações e de infraestrutura.

A segurança fim a fim foi transferida para a Aula 5 por decisão do professor na mesma data. O fundamento é a estrutura de Lovatt (2021, seção 7.7), que trata a segurança fim a fim como passo da definição tecnológica da solução, avaliado sobre a tecnologia já escolhida. A Aula 5 funde seus blocos 1 e 3, definição tecnológica e modelo técnico de referência, e libera o bloco 3 para segurança. A spec do módulo 5 detalhará esse bloco a partir das seções 2.9, 4.6.7 e 7.7 de Lovatt.

Não fazem parte deste módulo:

- segurança, zonas de confiança, controles e grade de permissões, tratados na Aula 5
- mapeamento de blocos de construção em serviços de infraestrutura, modelo técnico de referência e escolha de produto, tratados na Aula 5
- níveis de componentes e de código do C4
- mapeamento e modelagem de processos de negócio como técnica a ser praticada pelo aluno
- modelagem física de banco de dados
- análise de lacunas e roteiro de transição, tratados na Aula 6

## 3. Base bibliográfica

O livro-texto Lovatt (2021) é a base de cada bloco. O texto integral consultado está em `/Volumes/Marco-Dev/dev/projeto-arquitetura-solucao/docs/superpowers/plans/livro-lovatt.md`. As seções usadas nesta aula não foram citadas nos módulos 1 a 3, com exceção da seção 3.6, cuja subseção 3.6.4 é retomada aqui com outro propósito.

| Bloco | Seções de Lovatt | Fonte complementar |
| --- | --- | --- |
| 1, negócio | 2.3 e 2.4 | Nenhuma |
| 2, dados | 2.5 | Kleppmann (2017) para sistema de registro e dado derivado, Dehghani (2022) para propriedade por domínio |
| 3, aplicações e integração | 2.6, 2.8, 3.6.4 e 4.3.1 | RFC 9110, OpenAPI 3.1, AsyncAPI 3.0, Portal da Nota Fiscal Eletrônica, Brown (n.d.) |
| 4, infraestrutura | 2.7 e 7.5 | Brown (n.d.) |

Toda fonte complementar será conferida na origem antes de entrar no texto e na bibliografia. A fonte que não puder ser conferida sai do texto, e o conceito correspondente passa a ser apresentado como convenção do curso.

Os termos e os nomes próprios dos casos de Lovatt serão vertidos ao português. O hospital Fallowdale passa a ser o Hospital Vale do Pousio, com a origem declarada em Fontes. A repetição do caso do hospital em blocos consecutivos foi aceita pelo professor, por se tratar do caso do livro-texto.

| Original | Termo adotado |
| --- | --- |
| solution building block (SBB) | bloco de construção da solução |
| SBB interface (SBBI) | interface entre blocos de construção |
| applications portfolio catalogue | catálogo do portfólio de aplicações |
| applications interface catalogue | catálogo de interfaces de aplicações |
| red–amber–green | vermelho, âmbar e verde |
| cross-reference grid | grade de referência cruzada |
| capability map | mapa de capacidades |
| value stream | fluxo de valor |
| technical standard | padrão técnico |

## 4. Progressão pedagógica

Cada bloco consome o produto do anterior e produz uma entrada para o seguinte.

| Bloco | Pergunta orientadora | Entrada | Produto do exercício |
| --- | --- | --- | --- |
| 1. Negócio | O que a solução muda no negócio? | Declaração de escopo (ex. 8) e requisitos R1, R7 e R13 | Capacidades classificadas, etapas críticas do fluxo de valor e atividades afetadas (ex. 13) |
| 2. Dados | Quais dados sustentam a mudança e quem é dono de cada um? | Capacidades afetadas (ex. 13) e esboço lógico (ex. 9) | Grade dado × aplicação com dono e regime de consistência (ex. 14) |
| 3. Aplicações e integração | Quais aplicações e interfaces realizam a mudança e o que rege a integração? | Grade do ex. 14, padrões do ex. 11 e ADR do ex. 12 | Aplicações classificadas, contrato da integração de notas e diagrama de contexto corrigido (ex. 15) |
| 4. Infraestrutura | Em quais contêineres a solução executa e o que cada interface exige? | Produtos dos ex. 14 e 15 | Diagrama de contêineres com relações rotuladas (ex. 16) |

## 5. Regra dos exercícios

Os quatro exercícios seguem a regra fixada pelo professor em 02/10/2026. O enunciado fornece o artefato já montado e pede ao aluno que classifique, marque, rotule ou responda perguntas simples sobre ele. Nenhum exercício pede que o aluno construa do zero um mapa, um fluxo, um processo ou um diagrama.

O artefato fornecido não traz a resposta. Capacidades vêm sem classificação, a grade vem sem dono, o diagrama de contexto vem com os erros ainda presentes e o diagrama de contêineres vem com as relações sem rótulo. Cada enunciado reproduz os dados do caso ACME de que precisa ou aponta com precisão o produto que o próprio aluno construiu em exercício anterior.

## 6. Bloco 1, arquitetura de negócio da solução

### 6.1 Resultado de aprendizagem

O aluno usa modelos de arquitetura de negócio fornecidos para localizar o que a solução muda no negócio antes de detalhar dados, aplicações e infraestrutura.

### 6.2 Conteúdo

O bloco se apoia em Lovatt (2021, seção 2.3) e retoma a seção 2.4 apenas por remissão, porque pessoas, organização e processos como componentes da solução já foram apresentados no bloco 2 da Aula 1, a partir da seção 1.8.

- Definição de arquitetura de negócio pelo Business Architecture Guild e pelo TOGAF, nas formulações citadas por Lovatt, e o papel do domínio como origem e como alvo da mudança.
- As quatro perguntas que decidem se um problema admite tratamento por arquitetura de solução: se a área é um sistema, se pode ser modelada, se o modelo exibe o problema e se o modelo pode ser alterado para tratá-lo.
- Mapa de capacidades, com capacidade como o que a organização precisa conseguir fazer, os atributos de volume e de competência, e a classificação em estratégica, operacional e de apoio.
- Fluxo de valor, do primeiro contato do cliente até a realização do valor.
- Decomposição funcional e modelo de processo de negócio, apresentados como artefatos que o arquiteto lê e consulta, sem prática de modelagem.
- Modelo de motivação de negócio, apenas mencionado, com remissão ao bloco 1 da Aula 2, que tratou dos direcionadores de mudança.
- Ciclo de mudança de negócio em cinco estágios, alinhar, definir, projetar, implementar e realizar, com a arquitetura de solução concentrada em definir e projetar.
- Afirmação de Lovatt de que todo componente da solução sustenta um ou mais serviços de negócio, como ponte para a hierarquia de serviços desenvolvida no bloco 3.

O exemplo principal é o planejamento por capacidade do Hospital Vale do Pousio, em que a capacidade de comunicar-se com pacientes existe, mas precisa ganhar volume e canais, e os processos afetados são marcação, cancelamento, remarcação e lista de espera.

### 6.3 Exercício 13

O enunciado fornece três artefatos da ACME, montados pelo material do curso a partir do dossiê.

1. Mapa com cerca de dez capacidades acadêmicas, como admissão, oferta de disciplinas, matrícula, avaliação e registro de notas, emissão de documentos, gestão de bolsas e relação com o órgão regulador. O aluno classifica cada capacidade em estratégica, operacional ou de apoio e marca as afetadas pelo primeiro ciclo, com uma linha de justificativa.
2. Fluxo de valor do aluno, da renovação da matrícula à consulta da nota, com o tempo de cada passagem retirado da linha de base. O aluno indica as etapas em que a latência compromete o valor e o requisito, R1, R7 ou R13, que cada uma afeta.
3. Processo de lançamento de nota, com atividades e responsáveis. O aluno responde quais atividades mudam com a solução, qual unidade organizacional é afetada e qual diretiva rege o processo.

## 7. Bloco 2, arquitetura de dados da solução

### 7.1 Resultado de aprendizagem

O aluno identifica as entidades de dado que sustentam a mudança, verifica sua consistência com a arquitetura de dados corporativa e atribui a cada entidade um dono, consumidores e um regime de consistência.

### 7.2 Conteúdo

- Arquitetura de dados como subdomínio da arquitetura corporativa, e a exigência de que a arquitetura de dados da solução seja consistente com a corporativa (Lovatt, 2021, seção 2.5).
- Dado, informação e metadado, nas definições da ISO/IEC 2382 citadas por Lovatt.
- Objetivos, atividades e artefatos da arquitetura de dados, com destaque para a grade que cruza entidades de dado com aplicações e serve à análise de impacto.
- Abstração de entidade, generalização e especialização.
- Fonte de verdade, cópia derivada e regime de consistência, forte ou eventual com prazo declarado, com Kleppmann (2017) como fonte complementar.
- Propriedade do dado, em que um único responsável grava e os demais leem por interface ou recebem por evento. O banco compartilhado entre aplicações entra como antipadrão de integração, descrito pelo acoplamento que produz. Dehghani (2022) é citado como fonte da propriedade por domínio, sem desenvolvimento de malha de dados.

O exemplo principal combina os dois casos de Lovatt na seção 2.5, a produtora de vídeo com as definições inconsistentes de cliente e de autor, e as entidades, a generalização e a especialização do Hospital Vale do Pousio.

### 7.3 Exercício 14

O enunciado fornece a grade dado × aplicação com as cinco entidades, aluno, matrícula, nota, lançamento financeiro e turma, e as aplicações que hoje as leem ou gravam, retiradas da linha de base. O enunciado reproduz também os 2.300 pontos de acesso direto ao Oracle e a tabela de lotes noturnos.

O aluno marca o dono de cada entidade e o regime de consistência exigido para cada consumidor, forte ou eventual com prazo. Em seguida, indica qual capacidade marcada como afetada no exercício 13 depende de cada entidade e responde em até três linhas por que os 2.300 acessos diretos contrariam a propriedade do dado.

## 8. Bloco 3, arquitetura de aplicações e integração

### 8.1 Resultado de aprendizagem

O aluno classifica aplicações pela situação estratégica, descreve uma interface pelos seis atributos de Lovatt, distingue padrão técnico, protocolo, especificação e contrato, e reconhece o nível correto dos elementos num diagrama de contexto C4.

### 8.2 Desambiguação de padrão

Em português, a palavra padrão traduz tanto *standard* quanto *pattern*, e a Aula 3 usou padrão no sentido de *pattern*. O bloco adota a expressão padrão técnico para *standard* e declara a distinção na primeira ocorrência e no glossário.

### 8.3 Conteúdo

- Arquitetura de aplicações, aplicação e componente de aplicação, e a hierarquia serviço de negócio, processo, serviço de aplicação, componente de aplicação e serviço de tecnologia (Lovatt, 2021, seção 2.6, figura 2.4).
- Catálogo do portfólio de aplicações, classificação em vermelho, âmbar e verde entre estratégico e legado, e tipos de aplicação, de negócio, genérica e plataforma de aplicação.
- Catálogo de interfaces de aplicações e grades de referência cruzada como fonte da análise de interfaces.
- Relação entre arquitetura de software e arquitetura de solução quanto a interfaces e componentes (Lovatt, 2021, seção 2.8).
- Os seis atributos de interface de Lovatt (2021, seção 3.6.4), origem, destino, gatilho, itens trocados, sequência e pré e pós-condições.
- Padrão técnico como especificação adotada pela organização, que exige recorte da parte aplicável (Lovatt, 2021, seção 4.3.1).
- Protocolo como regra de troca entre partes, com exemplos da linha de base da ACME, LDAP, HTTPS e conector transacional, e o RFC 9110 como referência de HTTP.
- Especificação de interface como descrição verificável de uma interface particular, com OpenAPI para interface síncrona e AsyncAPI para interface orientada a mensagens, apresentadas por exemplo curto e sem exigência de escrita pelo aluno.
- Contrato de integração como especificação somada às garantias acordadas entre provedor e consumidor. A estrutura parte dos seis atributos de Lovatt e acrescenta protocolo, formato e esquema, semântica de erro, versionamento e compatibilidade, garantia de entrega e idempotência, e nível de serviço.
- Escolha entre comunicação síncrona e assíncrona, ligada aos padrões da Aula 3, Transactional Outbox, Retry com limite e Circuit Breaker.
- Modelo C4, os quatro níveis, os três princípios de abstração e o diagrama de contexto, com o roteiro de cinco etapas, preservados da página atual do bloco 4.

O exemplo principal de padrão técnico, protocolo e especificação é a nota fiscal eletrônica brasileira, em que o padrão nacional, o transporte por serviço web sobre HTTPS e o esquema XSD com o manual de integração aparecem separados. Os detalhes serão conferidos no Portal da Nota Fiscal Eletrônica antes de entrar no texto. Os exemplos de C4 do agendamento odontológico e do internet banking são preservados no nível de contexto.

### 8.4 Exercício 15

O enunciado fornece três artefatos.

1. Catálogo das aplicações da ACME, com os quatro portais, o núcleo transacional, o ERP financeiro, o ambiente virtual de aprendizagem, o data warehouse, o assinador digital e o diretório corporativo. O aluno classifica cada aplicação em vermelho, âmbar ou verde, com uma linha de justificativa.
2. Esqueleto do contrato da integração de notas entre a ACME e o ambiente virtual de aprendizagem, com os seis atributos de Lovatt e as extensões em branco. O aluno preenche cada campo com resposta curta, declarando o modo síncrono ou assíncrono e o tratamento de nota corrigida, e usa como origem do contrato o dono da entidade nota marcado no exercício 14. O enunciado reproduz o requisito R7, a exportação de notas das 05h10 e o acréscimo de 38% no contrato do ambiente virtual para o plano com interfaces de programação.
3. Diagrama de contexto da arquitetura alvo com dois erros de nível. O aluno aponta e corrige os dois erros.

## 9. Bloco 4, arquitetura de infraestrutura da solução

### 9.1 Resultado de aprendizagem

O aluno situa a infraestrutura como provedora de serviços aos requisitos não funcionais, reconhece contêineres como unidades que executam e se comunicam, e relaciona cada interface ao modo de comunicação, ao volume e à latência que ela exige.

### 9.2 Fronteira com a Aula 5

O bloco permanece no nível lógico. Ele trata de quais contêineres existem, de como se conectam e do que cada interface exige. A escolha de serviço de infraestrutura e de produto pertence à Aula 5, e os contêineres da arquitetura alvo levam o rótulo tecnologia a definir na Aula 5.

### 9.3 Conteúdo

- Infraestrutura como componentes e serviços tecnológicos que sustentam o negócio, objetivos de eficácia e eficiência, e relação com a arquitetura de solução pelos requisitos não funcionais (Lovatt, 2021, seção 2.7). Os artefatos da seção 2.7.2 são apenas listados, e o modelo técnico de referência fica para a Aula 5.
- Solução como grafo, em que blocos de construção são vértices e interfaces são arestas, e o exame de cada interface pelo tipo e pelo volume de tráfego (Lovatt, 2021, seção 7.5).
- Diagrama de contêineres, com o roteiro de quatro etapas, o exemplo do agendamento odontológico no segundo nível, o internet banking nos dois níveis e a discussão da fronteira do mainframe, preservados da página atual.
- Coerência entre níveis, com o mesmo conjunto de sistemas externos no contexto e nos contêineres.
- Escolha do nível pela audiência, preservada da seção Uso pelo arquiteto da página atual.

### 9.4 Exercício 16

O enunciado fornece o diagrama de contêineres da arquitetura alvo do primeiro ciclo, coerente com o diagrama de contexto corrigido no exercício 15, com as relações sem rótulo. O enunciado reproduz os volumes e a sazonalidade dos dados operacionais.

O aluno rotula cada relação com o modo de comunicação, síncrono ou assíncrono, e com o volume e a latência exigidos. Em seguida, responde em uma frase por que o núcleo COBOL permanece como contêiner na arquitetura alvo.

## 10. Índice e síntese

O índice do módulo terá objetivos de aprendizagem em verbos observáveis, grade de tempo no formato do módulo 3 com questões sobre a Aula 3, três Kahoots e quatro blocos de 32 ou 33 minutos, roteiro causal da aula, entrada recebida das Aulas 2 e 3, com a declaração de escopo do exercício 8 e os produtos dos exercícios 9, 11 e 12, e preparação para a Aula 5.

A síntese terá checklist dos conceitos essenciais, a cadeia negócio, dados, aplicações e infraestrutura com o produto de cada exercício, autoavaliação sem gabarito público e as fontes da aula.

## 11. Estratégia visual

Cada bloco terá ao menos um visual principal em SVG, com a classe `module-diagram` e o padrão dos quatro SVG do módulo 3. Nenhum visual traz dado decisório da ACME nem resolve exercício.

| Bloco | Visual principal |
| --- | --- |
| 1 | Os quatro modelos de arquitetura de negócio e a pergunta que cada um responde |
| 2 | Grade genérica dado × aplicação com dono, consumidores e regime de consistência |
| 3 | Hierarquia de serviços da figura 2.4 de Lovatt redesenhada, e camadas de padrão técnico, protocolo, especificação e contrato |
| 4 | Solução como grafo de blocos de construção e interfaces, com as figuras atuais do C4 preservadas |

## 12. Regras editoriais

Cada página de bloco seguirá a anatomia vigente, com título funcional, linha de enquadramento, Antes de começar, Conceito, Uso pelo arquiteto, exercício numerado e Fontes. O texto mantém o padrão do curso, com definição antes do exemplo, negrito parcimonioso, ausência de ponto e vírgula, travessão no máximo uma vez por parágrafo, referências em APA 7 com o trecho consultado entre parênteses e ausência de gabarito público. Cada termo do glossário será ligado no primeiro uso dentro da página, pela âncora da entrada em `docs/referencia/glossario.md`.

## 13. Arquivos previstos

A pasta do módulo será renomeada de `modulo-4-protocolos-e-representacao` para `modulo-4-dominios-da-solucao`, e a aula passa a se chamar Aula 4, domínios da arquitetura de solução.

Arquivos novos:

- `docs/modulo-4-dominios-da-solucao/bloco-1-arquitetura-de-negocio.md`
- `docs/modulo-4-dominios-da-solucao/bloco-2-arquitetura-de-dados.md`
- `docs/modulo-4-dominios-da-solucao/bloco-3-arquitetura-de-aplicacoes-e-integracao.md`, que recebe a introdução do C4 e o nível de contexto da página atual
- `docs/modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md`, que recebe o nível de contêineres e o exemplo do internet banking da página atual
- `docs/modulo-4-dominios-da-solucao/sintese.md`
- quatro SVG em `docs/assets/images/`
- `tests/test_modulo_4_contract.py`

Arquivos revisados:

- `docs/modulo-4-dominios-da-solucao/index.md`, movido da pasta antiga e reescrito
- `docs/cronograma.md`, nas tabelas das Aulas 4 e 5 e na sequência das aulas
- `docs/modulo-5-frameworks-e-tecnologias/index.md`, com a fusão dos blocos 1 e 3 e o bloco de segurança
- `docs/modulo-3-design-e-padroes/index.md`, na seção de preparação para a Aula 4
- `docs/caso-acme/artefatos.md`, na linha da Aula 4
- `docs/referencia/glossario.md` e `docs/referencia/bibliografia.md`
- `mkdocs.yml`, com navegação nova e redirecionamentos das URLs antigas, inclusive os que hoje apontam para a pasta antiga
- `tests/course_assertions.py`, `tests/test_content_contract.py` e `scripts/validate_content.py`, com o nome novo da pasta

A página atual `bloco-4-representacao-de-modelos-e-c4.md` deixa de existir, e sua URL é redirecionada para o bloco 3, onde o C4 começa.

Os ajustes de CSS ainda sem commit em `mkdocs.yml` e `tests/test_modulo_3_contract.py` pertencem a outro trabalho e não entram nos commits deste módulo.

## 14. Glossário e bibliografia

Entradas novas do glossário: arquitetura de negócio, capacidade, fluxo de valor, arquitetura de dados, propriedade do dado, fonte de verdade, regime de consistência, arquitetura de aplicações, padrão técnico, protocolo, especificação de interface, contrato de integração e arquitetura de infraestrutura.

Fontes novas da bibliografia, todas conferidas antes do registro: Kleppmann (2017), Dehghani (2022), RFC 9110 (2022), especificação OpenAPI 3.1, especificação AsyncAPI 3.0 e Portal da Nota Fiscal Eletrônica. Lovatt (2021), Brown (n.d.) e Mendes (2026b) já constam da bibliografia.

## 15. Validação e critérios de aceite

Os testes de contrato do módulo serão escritos antes do conteúdo e verificarão:

- existência das páginas e presença na navegação
- exercício numerado de 13 a 16 e visual local acessível em cada bloco
- cadeia de consumo entre os exercícios 13, 14, 15 e 16
- citação de Lovatt com seção em cada bloco
- presença dos seis atributos de interface no bloco 3
- desambiguação de padrão técnico no bloco 3
- reprodução do acréscimo de 38% no exercício 15
- ausência de segurança como tema de bloco da Aula 4 no cronograma
- presença do bloco de segurança na Aula 5 do cronograma e no índice do módulo 5
- redirecionamento das URLs da pasta antiga
- novos termos no glossário e novas fontes na bibliografia

O módulo estará concluído quando:

- os quatro blocos, o índice e a síntese estiverem publicados e navegáveis
- os exercícios 13 a 16 seguirem a regra da seção 5 e formarem uma cadeia coerente de produtos
- cada bloco tiver Lovatt como base, com a seção citada
- nenhum visual ou texto entregar a resposta fechada do exercício
- links, âncoras, fontes e imagens locais forem válidos
- `scripts/validate_content.py` não registrar violações
- a suíte de testes estiver verde
- `mkdocs build --strict` concluir sem erro
- os quatro blocos forem inspecionados visualmente no site gerado

## 16. Riscos e controles

| Risco | Controle |
| --- | --- |
| Sobreposição do bloco 1 com o bloco 2 da Aula 1 | Usar a seção 2.3 como eixo e tratar a seção 2.4 apenas por remissão |
| Sobreposição do bloco 4 com o bloco 1 da Aula 5 | Manter o bloco 4 no nível lógico, com tecnologia a definir na Aula 5 |
| Confusão entre padrão técnico e padrão arquitetural | Desambiguar na primeira ocorrência, no glossário e no teste de contrato |
| Bloco 3 extenso demais por reunir aplicações, contrato e C4 | Limitar especificação de interface a exemplo curto e manter no bloco 3 apenas o nível de contexto |
| Exercício complexo demais | Aplicar a regra da seção 5 e revisar cada enunciado contra ela |
| Artefato fornecido entregar a resposta | Fornecer artefatos sem classificação, sem dono, sem rótulo e com os erros presentes |
| Fonte complementar não verificável | Retirar a fonte e apresentar o conceito como convenção do curso |
| Links quebrados pela renomeação da pasta | Redirecionar todas as URLs antigas e rodar `mkdocs build --strict` |
