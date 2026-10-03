# Aula 4, domínios da arquitetura de solução

A aula detalha a solução cuja forma estrutural foi registrada na Aula 3, percorrendo os domínios de negócio, dados, aplicações e infraestrutura na ordem em que cada um consome o anterior, e termina com a representação da arquitetura alvo nos níveis de contexto e de contêineres do modelo C4.

## Objetivos de aprendizagem

Ao final da aula, o aluno é capaz de

- descrever, para cada domínio da solução, o que o arquiteto de solução recebe, decide e entrega, e o que o domínio seguinte consome
- usar modelos de arquitetura de negócio fornecidos para localizar o que a solução muda no negócio
- situar a solução no modelo de dados corporativo e nas áreas de gestão de dados do DMBOK, e atribuir a cada entidade dono, consumidores, regime de consistência e obrigações de proteção
- classificar as aplicações do portfólio pela situação estratégica e descrever uma interface pelos seis atributos de interface
- distinguir padrão técnico, protocolo, especificação de interface e contrato de integração
- reconhecer o nível correto de cada elemento num diagrama de contexto e num diagrama de contêineres
- relacionar cada interface entre contêineres ao modo de comunicação, ao volume e à latência que ela exige
- descrever as camadas de execução, a topologia em regiões e zonas de disponibilidade e o diagrama de implantação em C4 de uma solução

## Grade de tempo

A aula ocorre das 19h00 às 22h30, com intervalo das 20h30 às 20h45, e o tempo de conteúdo encerra até as 22h10. O tempo de aula é dividido entre a apresentação conceitual do bloco 0 e dos quatro blocos, as questões sobre a aula anterior e três questionários Kahoot, e os exercícios são realizados fora do horário de aula. A tabela abaixo é o único lugar do site em que os minutos de cada bloco aparecem, porque as páginas de bloco não exibem cronômetro.

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

O bloco 0 e os quatro blocos somam 130 minutos de apresentação conceitual, e os três questionários e as questões iniciais ocupam os 45 minutos restantes do tempo útil de 175 minutos.

## Entrada recebida das Aulas 2 e 3

A aula parte de três produtos das aulas anteriores. A declaração de escopo do primeiro ciclo, produzida no [exercício 8](../modulo-2-requisitos-e-partes-interessadas/bloco-4-partes-interessadas-e-pontos-de-vista.md#exercicio-8), delimita as capacidades que a solução afeta. O esboço lógico do [exercício 9](../modulo-3-design-e-padroes/bloco-1-principios-de-design.md#exercicio-9) distribui as responsabilidades que os domínios desta aula detalham. Os padrões selecionados no [exercício 11](../modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md#exercicio-11) orientam a escolha entre comunicação síncrona e assíncrona no contrato de integração. O estilo registrado no ADR do [exercício 12](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md#exercicio-12) é o pano de fundo dos diagramas desta aula, que não o usam como entrada de exercício.

## Roteiro da aula

O [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md) apresenta, no início da aula, o modelo que os blocos seguintes detalham, em que cada domínio aparece com o que o arquiteto de solução recebe, decide e entrega, e com a pergunta que ele responde. A abertura não tem exercício, e os blocos 1 a 4 começam pela mesma figura, com o próprio domínio em destaque.

O [bloco 1](bloco-1-arquitetura-de-negocio.md) apresenta a definição de arquitetura de negócio, as quatro perguntas que decidem a aplicabilidade da arquitetura de solução, os quatro modelos de arquitetura de negócio e o ciclo de mudança de negócio, com o exemplo do Hospital ACME e da modernização da comunicação com os laboratórios de apoio, que passam a trocar pedidos de exame e resultados por meio eletrônico, integrados ao prontuário. O exercício 13 fornece as capacidades acadêmicas, o fluxo de valor do aluno e o processo de lançamento de nota da ACME, e pede ao aluno que classifique as capacidades e localize nas etapas e nas atividades o efeito da solução.

O [bloco 2](bloco-2-arquitetura-de-dados.md) trata da arquitetura de dados da solução a partir das áreas de gestão de dados do DMBOK, do modelo de dados corporativo em quatro níveis, do panorama de dados e da linhagem, da distinção entre fonte de verdade e cópia derivada, do regime de consistência, dos dados mestres, da propriedade do dado, dos requisitos de qualidade e de proteção pela LGPD e da passagem do dado operacional ao analítico. O exercício 14 fornece a grade da linha de base da ACME e pede ao aluno, em cinco itens, que decida o dono de cada entidade, o regime de consistência exigido por consumidor, o estilo de dado mestre do aluno e as obrigações do dado pessoal, e que explique por que o acesso direto ao banco contraria a propriedade do dado.

O [bloco 3](bloco-3-arquitetura-de-aplicacoes-e-integracao.md) trata das aplicações e interfaces, do portfólio de aplicações, dos seis atributos de uma interface, da distinção entre padrão técnico, protocolo, especificação e contrato, da estrutura de um contrato de integração, dos estilos de integração e da hierarquia de serviços, e termina com o modelo C4, apresentado como a notação de modelagem da aula nos níveis de contexto e de contêineres. O exercício 15 pede a classificação das aplicações da ACME, o preenchimento do contrato da integração de notas e a correção de um diagrama de contexto com dois erros de nível ou de fronteira.

O [bloco 4](bloco-4-arquitetura-de-infraestrutura.md) trata da arquitetura de infraestrutura no nível lógico, da representação da solução como grafo de blocos de construção e interfaces, das camadas de execução, da topologia de implantação e do diagrama de implantação do modelo C4, aplicado ao mesmo exemplo de contêineres do bloco 3, sem escolha de produto, que pertence à Aula 5. O exercício 16 fornece o diagrama de contêineres da arquitetura alvo e pede ao aluno, em três itens, que rotule cada relação com modo de comunicação, volume e latência, que indique as relações que sustentam os requisitos R6 e R7 e que deduza a posição do núcleo transacional COBOL a partir da divisão de responsabilidade entre a ACME e a fábrica contratada.

A [síntese](sintese.md) fecha o módulo com o checklist do que precisa permanecer, a cadeia dos domínios construída na aula, a autoavaliação e as fontes principais da aula, e as demais constam das Fontes de cada bloco e da bibliografia.

## Preparação para a Aula 5

A Aula 5 converte os contêineres rotulados com tecnologia a definir em escolhas de serviço de infraestrutura, de plataforma e de framework, classificadas no modelo técnico de referência. A mesma aula avalia a segurança fim a fim sobre a tecnologia escolhida e registra a decisão de plataforma em ADR, com as lacunas de provisão, e o [cronograma](../cronograma.md) traz a sequência completa das seis aulas.
