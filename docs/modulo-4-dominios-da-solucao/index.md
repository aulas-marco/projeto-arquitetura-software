# Aula 4, domínios da arquitetura de solução

Ao fim da Aula 3, a ACME, universidade privada fictícia com 38.400 alunos ativos, já tinha a forma estrutural da modernização do sistema acadêmico registrada em um ADR, mas ninguém havia dito ainda o que essa forma exige do trabalho da universidade, dos dados, das aplicações e da infraestrutura. A Aula 4 responde a essa pergunta percorrendo os quatro domínios na ordem em que cada um consome o anterior, de negócio a infraestrutura, e termina com a arquitetura alvo desenhada nos níveis de contexto e de contêineres do modelo C4, uma notação que descreve o sistema em níveis de detalhe progressivos. O caso está descrito no [dossiê do caso](../caso-acme/index.md), e cada um dos blocos 1 a 4 termina com um exercício sobre ele, numerados de 13 a 16.

## Objetivos de aprendizagem

Ao final da aula, o aluno é capaz de

- descrever, para cada domínio da solução, o que o arquiteto de solução recebe, decide e entrega, e o que o domínio seguinte consome
- usar modelos de arquitetura de negócio fornecidos para localizar o que a solução muda no negócio
- situar a solução no modelo de dados corporativo e nas áreas de gestão de dados do DMBOK, o guia de referência da associação DAMA, e atribuir a cada entidade dono, consumidores, regime de consistência e obrigações de proteção
- classificar as aplicações do portfólio pela situação estratégica e descrever uma interface pelos seis atributos de interface
- distinguir padrão técnico, protocolo, especificação de interface e contrato de integração
- reconhecer o nível correto de cada elemento num diagrama de contexto e num diagrama de contêineres
- relacionar cada interface entre contêineres ao modo de comunicação, ao volume e à latência que ela exige
- descrever as camadas de execução, a topologia em regiões e zonas de disponibilidade e o diagrama de implantação em C4 de uma solução

## Grade de tempo

A aula ocorre das 19h00 às 22h30, com intervalo de 15 minutos, das 20h30 às 20h45, e o conteúdo programado termina às 22h10, o que deixa 20 minutos até o fim do horário. Em sala, o tempo se divide entre a apresentação conceitual do bloco 0 e dos quatro blocos, as questões sobre a aula anterior e três questionários Kahoot, que são questionários de perguntas e respostas feitos em sala. Os exercícios 13 a 16 são resolvidos fora do horário de aula. A tabela abaixo é o único lugar do site em que os minutos de cada bloco aparecem, porque as páginas de bloco não exibem cronômetro.

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

O tempo útil é de 175 minutos, que são os 190 minutos entre 19h00 e 22h10 menos o intervalo de 15 minutos. Desses, o bloco 0 e os quatro blocos somam 130 minutos de apresentação conceitual, e as questões sobre a Aula 3 e os três questionários ocupam os 45 minutos restantes.

## Entrada recebida das Aulas 2 e 3

Os exercícios desta aula não começam do zero, porque cada domínio precisa de um produto que o aluno já fez. Quando o arquiteto quiser saber o que muda no primeiro ciclo, recorre à declaração de escopo produzida no [exercício 8](../modulo-2-requisitos-e-partes-interessadas/bloco-4-partes-interessadas-e-pontos-de-vista.md#exercicio-8), um quadro que marca, para dez elementos do sistema acadêmico e do entorno, o que muda e o que permanece nos primeiros 12 meses, e que delimita as capacidades afetadas. Quando quiser saber que partes a solução tem, parte do esboço lógico do [exercício 9](../modulo-3-design-e-padroes/bloco-1-principios-de-design.md#exercicio-9), que agrupa em poucos elementos as oito responsabilidades da solução e que os domínios desta aula detalham. Na hora de escolher entre comunicação síncrona e assíncrona no contrato de integração, usa os padrões selecionados no [exercício 11](../modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md#exercicio-11), que resolvem três problemas da ACME, a coexistência com o sistema antigo, a proteção contra falha de integração e a publicação confiável de mudança. O estilo arquitetural do ADR do [exercício 12](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md#exercicio-12), o registro da decisão de arquitetura, fica como pano de fundo dos diagramas e não entra como insumo de exercício.

## Roteiro da aula

A aula começa pelo [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md), que mostra a solução inteira antes de abrir cada parte. Para cada domínio, o bloco diz o que o arquiteto de solução recebe, o que decide e o que entrega ao domínio seguinte, e a pergunta que ele responde. A abertura não tem exercício, e os blocos 1 a 4 retomam a mesma figura, cada um com o próprio domínio em destaque.

O [bloco 1](bloco-1-arquitetura-de-negocio.md) começa pela pergunta que vem antes de qualquer desenho, a de saber se o problema admite tratamento por arquitetura de solução, e depois mostra os quatro modelos de arquitetura de negócio que localizam a mudança, com o ciclo de mudança de negócio como pano de fundo. O exemplo acompanha a publicação de notas da Universidade ACME, do lançamento pelo professor à consulta no ambiente virtual. No exercício 13, a análise se amplia com dez capacidades acadêmicas, o fluxo de valor do aluno em seis etapas e o processo de lançamento de nota, e o aluno classifica as capacidades e localiza nas etapas e nas atividades o efeito da solução, guiado pelos requisitos R1, R7 e R13.

O [bloco 2](bloco-2-arquitetura-de-dados.md) parte de uma dúvida comum a qualquer sistema com várias aplicações, a de saber qual versão de um dado vale quando duas aplicações o guardam. Para respondê-la, o bloco apresenta as áreas de gestão de dados do DMBOK, o modelo de dados corporativo em quatro níveis, o panorama de dados e a linhagem, a distinção entre fonte de verdade e cópia derivada, o regime de consistência, os dados mestres, a propriedade do dado, os requisitos de qualidade e de proteção pela LGPD e a passagem do dado operacional ao analítico. No exercício 14, a grade da linha de base da ACME cruza cinco entidades acadêmicas, aluno, matrícula, nota, lançamento financeiro e turma, com as aplicações que as gravam ou leem, e o aluno decide, em cinco itens, o dono de cada entidade, o regime de consistência de cada consumidor, o estilo de dado mestre do aluno, isto é, como manter um cadastro único que várias aplicações compartilham, e as obrigações do dado pessoal. O último item pede que explique por que o acesso direto ao banco contraria a propriedade do dado.

O [bloco 3](bloco-3-arquitetura-de-aplicacoes-e-integracao.md) pergunta o que acontece quando a nota lançada por um professor precisa chegar a outra aplicação, e para responder apresenta as aplicações e interfaces, o portfólio de aplicações, os seis atributos de uma interface, a distinção entre padrão técnico, protocolo, especificação e contrato, a estrutura de um contrato de integração, os estilos de integração e a hierarquia de serviços. O bloco termina com o modelo C4, que é a notação de modelagem da aula nos níveis de contexto e de contêineres. No exercício 15, o aluno classifica as onze aplicações da ACME, preenche o contrato da integração de notas com o ambiente virtual de aprendizagem e corrige um diagrama de contexto com dois erros de nível ou de fronteira.

O [bloco 4](bloco-4-arquitetura-de-infraestrutura.md) fecha o percurso com a pergunta sobre onde a solução executa e o que cada ligação entre as partes exige da rede. Ele trata a infraestrutura no nível lógico, representa a solução como grafo de blocos de construção e interfaces, descreve as camadas de execução e a topologia de implantação e termina no diagrama de implantação do modelo C4, aplicado ao mesmo exemplo de contêineres do bloco 3, sem escolha de produto, que pertence à Aula 5. No exercício 16, o diagrama de contêineres da arquitetura alvo da ACME chega com 15 relações numeradas, e o aluno rotula cada uma com modo de comunicação, volume e latência, indica as relações que sustentam os requisitos R6 (confirmação da matrícula em até 4 segundos no pico de 5.800 sessões simultâneas) e R7 (nota no ambiente virtual em até 10 minutos) e deduz a posição do núcleo transacional, o sistema central da ACME escrito em COBOL, a partir da divisão de responsabilidade entre a ACME e a fábrica contratada.

Depois dos quatro blocos, a [síntese](sintese.md) fecha o módulo com o checklist do que precisa permanecer, a cadeia dos domínios construída na aula, a autoavaliação e as fontes principais, e as demais constam das Fontes de cada bloco e da bibliografia.

## Adições no Caderno Arquitetural da Aula 4

Nas aulas anteriores, o caderno arquitetural da ACME ganhou o contexto do caso, as partes interessadas, os requisitos e os princípios, e a Aula 3 deixou nele as primeiras decisões de estilo e de padrões. Com esse material em mãos, a Aula 4 detalha a solução domínio por domínio, e cada exercício acrescenta ao caderno o que o domínio decidiu: o efeito da solução no negócio, as decisões sobre dados, a decisão sobre as aplicações com o desenho da fronteira na seção 5 e, na seção 7, o desenho dos contêineres com as relações rotuladas. O caderno que sai da Aula 4 é o do [gabarito do exercício 16](../gabaritos/gabarito-exercicio-16.md).

{{trilha:7:4}}

| Bloco | Exercício | O que entra no caderno | Gabarito |
| --- | --- | --- | --- |
| 1 | 13 | A classificação das dez capacidades acadêmicas, as etapas do fluxo de valor do aluno com problema e as atividades do processo de lançamento de nota que mudam | [Gabarito 13](../gabaritos/gabarito-exercicio-13.md) |
| 2 | 14 | O dono e o regime de consistência de cada uma das cinco entidades, o estilo de dado mestre do aluno e as obrigações do dado pessoal | [Gabarito 14](../gabaritos/gabarito-exercicio-14.md) |
| 3 | 15 | A cor das onze aplicações, o contrato da integração de notas e o diagrama de contexto corrigido, na seção 5 | [Gabarito 15](../gabaritos/gabarito-exercicio-15.md) |
| 4 | 16 | O modo, o volume e a latência das 15 relações entre contêineres, as relações que sustentam o R6 e o R7 e a posição do núcleo transacional | [Gabarito 16](../gabaritos/gabarito-exercicio-16.md) |

## Preparação para a Aula 5

Os contêineres da arquitetura alvo saem desta aula com o rótulo tecnologia a definir, e a Aula 5 os converte em escolhas de serviço de infraestrutura, de plataforma e de framework, classificadas no modelo técnico de referência. Depois dessas escolhas, a mesma aula avalia a segurança ponta a ponta sobre a tecnologia escolhida e registra a decisão de plataforma em ADR, com as lacunas de provisão, e o [cronograma](../cronograma.md) traz a sequência completa das seis aulas.
