# Cronograma

## Sequência das aulas

Um projeto de arquitetura começa entendendo o problema, e por isso as duas primeiras aulas tratam da disciplina e do seu processo e depois das entradas, dos requisitos e das partes interessadas. Só então as quatro seguintes percorrem o desenho, a tecnologia e a entrega. Alguns termos técnicos da tabela, como ADR e modelagem C4, podem ser novos para você, e cada um é explicado na primeira aula em que aparece e reunido no [glossário](referencia/glossario.md). O ADR é o registro curto de uma decisão de arquitetura, e a modelagem C4 é uma forma de desenhar o sistema em quatro níveis de detalhe.

| Aula | Tema |
| --- | --- |
| 1 | Arquitetura de soluções e arquitetura de software, componentes da solução (pessoas, áreas, processos, informação e tecnologia), papel do arquiteto e processo de definição da arquitetura |
| 2 | Direcionadores de mudança, requisitos e atributos de qualidade, artefatos de linha de base, restrições e partes interessadas |
| 3 | Princípios de design, estilos arquiteturais, padrões de design e registro de decisão arquitetural |
| 4 | Arquitetura de negócio, de dados, de aplicações e de infraestrutura da solução, com contrato de integração e modelagem C4 |
| 5 | Definição tecnológica e modelo técnico de referência, plataforma arquitetural e frameworks, segurança ponta a ponta e ADR de plataforma |
| 6 | Governança da mudança, aceleradores de IA e apresentação do caderno arquitetural |

A ordem das aulas é a de um projeto real, que parte do enquadramento, passa pelo desenho e pela tecnologia e termina na entrega governada. A Aula 1 apresenta a disciplina e o processo pelo qual ela opera, e a Aula 2 reúne tudo o que entra antes de qualquer alternativa, de modo que a Aula 3 já pode escolher a forma estrutural e registrar a escolha. Com a forma escolhida, a Aula 4 detalha a solução nos domínios de negócio, dados, aplicações e infraestrutura e a representa nos níveis de contexto e de contêineres do modelo C4. Depois disso, a Aula 5 converte o desenho lógico em tecnologia e avalia a segurança ponta a ponta sobre a tecnologia escolhida, e a Aula 6 organiza a entrega em ondas, mostra como governar a mudança, apresenta os aceleradores de IA no trabalho do arquiteto e fecha o caderno arquitetural da ACME.

## Blocos de cada aula

### Aula 1, arquitetura de soluções e seu processo

| Bloco | Tema | Exercício |
| --- | --- | --- |
| 1 | Arquitetura de soluções e arquitetura de software | 1 |
| 2 | A solução como sistema e seus componentes (pessoas, áreas, processos, informação e tecnologia) | 2 |
| 3 | O papel do arquiteto de solução | 3 |
| 4 | O processo de definição da arquitetura | 4 |

### Aula 2, entradas, requisitos e partes interessadas

| Bloco | Tema | Exercício |
| --- | --- | --- |
| 1 | Direcionadores de mudança, internos e externos | 5 |
| 2 | Qualidade e tipos de requisito | 6 |
| 3 | Cenários de qualidade, linha de base e restrições | 7 |
| 4 | Partes interessadas, pontos de vista e escopo | 8 |

### Aula 3, princípios de design e padrões

| Bloco | Tema | Exercício |
| --- | --- | --- |
| 1 | Princípios de design da solução e a passagem do conceitual ao lógico | 9 |
| 2 | Estilos arquiteturais e sua relação com atributo de qualidade | 10 |
| 3 | Padrões de design e sua relação com padrões arquiteturais | 11 |
| 4 | Registro de decisão arquitetural, formatos Nygard e MADR, dois modelos de ficha para anotar uma decisão | 12 |

### Aula 4, domínios da arquitetura de solução

| Bloco | Tema | Exercício |
| --- | --- | --- |
| 0 | Os quatro domínios numa só solução, com o que o arquiteto recebe, decide e entrega | Sem exercício |
| 1 | Arquitetura de negócio da solução, capacidades, fluxo de valor e processos | 13 |
| 2 | Arquitetura de dados da solução, com propriedade do dado | 14 |
| 3 | Arquitetura de aplicações e integração, contrato de integração e modelo C4 | 15 |
| 4 | Arquitetura de infraestrutura da solução, topologia e diagrama de implantação | 16 |

### Aula 5, frameworks e tecnologias

| Bloco | Tema | Exercício |
| --- | --- | --- |
| 1 | Definição tecnológica e modelo técnico de referência, do bloco de construção ao serviço de infraestrutura | 17 |
| 2 | Plataforma arquitetural, frameworks e zona de pouso, a base preparada do ambiente em nuvem | 18 |
| 3 | Segurança ponta a ponta | 19 |
| 4 | ADR de plataforma, dependência de fornecedor e lacunas na provisão de serviços | 20 |

### Aula 6, governança, aceleradores de IA e apresentação do caderno

| Bloco | Tema | Exercício |
| --- | --- | --- |
| 1 | Governança da mudança, lacunas, roteiro em ondas, desvio arquitetural e ciclo ADM | 21 e 22 |
| 2 | Aceleradores de IA no trabalho do arquiteto | 23 |
| 3 | Apresentação do caderno arquitetural | 24 |

## Avaliação

Como os exercícios de cada aula já são o instrumento de avaliação, não há trabalho final entregue após a última aula. Cada aula vale dez pontos, distribuídos entre os quatro exercícios daquela aula, e as seis aulas somam sessenta pontos. A página de [artefatos por aula](caso-acme/artefatos.md) mostra o que cada exercício entrega, e a participação nos encontros ao vivo vale os outros quarenta pontos.

## Como os artefatos se encadeiam

Quem faz o exercício de classificar os requisitos da ACME na Aula 2 percebe, na Aula 3, que o desenho parte justamente dessa classificação. Os exercícios dependem uns dos outros desse modo, porque o artefato produzido em um bloco, isto é, o documento ou diagrama que o exercício entrega, costuma ser a entrada do bloco seguinte. Como o exercício é feito fora do horário de aula, o aluno chega ao encontro seguinte com o artefato que aquela aula consome, sempre sobre o mesmo [caso ACME](caso-acme/index.md). A página de [artefatos por aula](caso-acme/artefatos.md) descreve o que cada exercício produz, com qual parte do dossiê e sob qual critério de aceitação.
