# Glossário

Quem abre uma página de bloco pela primeira vez costuma esbarrar em termos novos, como lacuna, linha de base ou zona de pouso, e este glossário existe para esse momento. Ele reúne os termos usados nas páginas do curso, com a definição adotada pela disciplina, e cada entrada explica o termo com palavras simples, de modo que dá para lê-la isoladamente. Como cada entrada corresponde a uma âncora, a seção "Antes de começar" das páginas de bloco leva o aluno direto à definição do termo que ele vai usar.

## Arquitetura de solução

Disciplina que produz e gerencia o plano de uma solução completa, isto é, do conjunto de pessoas, processos, informação e tecnologia que responde a uma necessidade, um problema ou uma oportunidade de negócio. A solução precisa se encaixar na estratégia da organização e causar o menor impacto negativo possível. O plano descreve a estrutura e o comportamento da solução em alto nível, antes da escolha dos produtos que a realizam.

## Espinha dorsal dos domínios

Modelo apresentado no bloco 0 da Aula 4. Para cada um dos quatro domínios da solução, que são negócio, dados, aplicações e infraestrutura, ele mostra o que o arquiteto de solução recebe, o que decide e o que entrega, e como a entrega de um domínio vira a entrada do domínio seguinte.

## Arquiteto de solução

Profissional que conduz a definição de uma solução inteira. Ele investiga o problema, levanta as partes interessadas, compara alternativas e responde pela coerência do desenho até a entrega. Suas decisões cobrem os cinco tipos de componente da solução, e não apenas o software.

## Arquitetura corporativa

Disciplina que define diretrizes, princípios e modelos válidos para a organização inteira, nos domínios de negócio, aplicações, dados, infraestrutura e segurança. Ela atua no nível mais amplo, acima de qualquer solução isolada.

## Componentes da solução

Quando a ACME decidiu que a nota deveria chegar ao ambiente virtual em até 10 minutos, a mudança envolvia mais do que programa: alguém precisaria aprender a lançar a nota na hora, e uma área teria de mudar a rotina de fechamento. Cada uma dessas peças é um componente da solução, que pode ser de cinco tipos: pessoas, estruturas organizacionais, processos, informação e tecnologia. O arquiteto os usa como lista de conferência para que nenhum fique de fora do desenho. Neste curso, "componente" sozinho quer dizer peça de TI, como um serviço, um banco de dados ou uma mensageria, e "componente da solução" é o sentido amplo, que abrange os cinco tipos.

## Bloco de construção da solução

Unidade do desenho que representa uma capacidade de que a solução precisa, antes de estar decidido qual produto ou serviço a realiza. Um bloco de granularidade grossa, isto é, mais abrangente, agrupa vários blocos de granularidade fina, mais detalhados.

## Direcionador de mudança

Fator que leva a organização a buscar uma solução. É interno quando nasce da própria operação, como custo, risco ou limite de capacidade, e externo quando vem de fora, como exigência regulatória, movimento de concorrente ou mudança de expectativa do usuário.

## Parte interessada

Pessoa, papel ou área com interesse legítimo no resultado da solução, seja porque decide sobre ela, porque a usa, porque a sustenta ou porque é afetada por ela.

## Ponto de vista

Conjunto de regras que define como construir e ler um tipo de representação da arquitetura. É escolhido de acordo com as preocupações de uma parte interessada.

## Visão

Representação concreta da arquitetura, construída segundo um ponto de vista, que responde às preocupações às quais esse ponto de vista se dirige.

## Arquitetura de linha de base

Descrição da arquitetura como ela é hoje, com os componentes existentes, suas idades, seus responsáveis e suas integrações. No caso da ACME, é o retrato de um núcleo em COBOL de 2004 que o arquiteto precisa conhecer antes de propor qualquer mudança, e serve de ponto de partida para comparar com a arquitetura alvo.

## Arquitetura alvo

Descrição da arquitetura que se pretende ter ao fim de um ciclo de evolução, como a ACME com a nota chegando ao ambiente virtual em minutos. A diferença entre ela e a arquitetura de linha de base é a lacuna, que é o objeto da análise de lacunas.

## Artefato de linha de base

Documento ou modelo que já existe, descreve parte da situação atual e entra como insumo do processo de definição da arquitetura. É aproveitado na forma em que a organização o mantém, sem ser refeito.

## Fase do processo de definição da arquitetura

Etapa do ciclo de vida que organiza o trabalho do arquiteto de solução, com entrada, atividades e saída próprias. O curso adota um ciclo de oito fases, da iniciação à conclusão.

## Arquitetura de software

Conjunto das decisões estruturais fundamentais sobre um sistema, que são difíceis de reverter depois de tomadas e determinam se o sistema consegue atender aos atributos de qualidade exigidos.

## Arquiteto de software

Profissional responsável por tomar e documentar as decisões estruturais de um sistema. Ele equilibra atributos de qualidade que competem entre si, requisitos funcionais e restrições de negócio.

## Atributo de qualidade

Propriedade pela qual um sistema é avaliado, como desempenho, disponibilidade, segurança ou facilidade de manutenção.

## Requisito funcional

Expectativa sobre o que o sistema faz, descrita como uma função, um comportamento ou uma resposta a um estímulo específico. Exemplo: o sistema emite o histórico escolar do aluno.

## Requisito não funcional

Categoria ampla de requisito que, em várias classificações, reúne os requisitos de atributo de qualidade e as restrições. O curso não usa o termo como sinônimo de atributo de qualidade. Atributo de qualidade é a propriedade avaliada, e requisito não funcional é o nome do grupo que reúne essa e outras expectativas que não descrevem função, incluindo as restrições.

## Requisito de atributo de qualidade

Expectativa concreta e mensurável sobre um atributo de qualidade, escrita com o estímulo que o sistema recebe, a resposta esperada e a medida dessa resposta.

## Restrição

Decisão ou condição imposta ao sistema de fora do processo de projeto, como o parecer do Jurídico da ACME que exige o processamento de dado de aluno em território nacional. Ela limita as alternativas do arquiteto, que não tem poder para negociá-la.

## Requisito arquiteturalmente significativo

Requisito cujo atendimento influencia de forma relevante a arquitetura do sistema. Pode ser de qualidade, funcional ou uma restrição.

## Direcionador arquitetural

Fator de negócio ou técnico que orienta as decisões de arquitetura antes de se transformar em requisitos específicos.

## Cenário de atributo de qualidade

Descrição estruturada de um requisito de qualidade em seis elementos: fonte do estímulo, estímulo, artefato afetado, ambiente, resposta e medida da resposta.

## Estilo arquitetural

Forma de organizar a estrutura de um sistema, que define os tipos de componente, as maneiras de conectá-los e as restrições dessa organização. Camadas e microsserviços são exemplos de estilo.

## Princípio de design

Regra durável, derivada de objetivos, requisitos e restrições, que orienta várias decisões de desenho. A aplicação do princípio pode ser verificada por evidência observável.

## Desenho conceitual

Descrição da solução em termos de capacidades, responsabilidades e relações com o ambiente, sem estrutura interna detalhada e sem escolha de tecnologia.

## Desenho lógico

Descrição da solução em elementos com responsabilidades, interfaces e fluxos declarados, ainda sem produto, linguagem ou plataforma escolhidos.

## Padrão arquitetural

Solução recorrente para uma preocupação que atravessa o sistema ou que envolve a integração entre suas partes. Tem escopo menor que o estilo arquitetural e maior que o padrão de design.

## Padrão de design

Solução recorrente para a colaboração entre responsabilidades dentro de uma parte do sistema, descrita pelos papéis, pelas interfaces e pelas relações entre os elementos.

## Plataforma arquitetural

Conjunto organizado de ferramentas, frameworks, bibliotecas e práticas de desenho que implementa um ou mais estilos arquiteturais e cobre desenvolvimento, integração, implantação e manutenção. É adotada como decisão arquitetural própria, tomada depois da decisão de estilo.

## ADR

Registro de decisão de arquitetura, do inglês Architecture Decision Record. É um documento curto que descreve uma decisão arquitetural, o contexto que a motivou e suas consequências.

## Racional arquitetural

Raciocínio que justifica as decisões de desenho de um sistema e liga cada escolha às metas estratégicas, aos requisitos técnicos e às restrições de negócio. Registra a escolha feita, o motivo, as alternativas consideradas, os critérios de seleção e os impactos esperados.

## Dependência de fornecedor

Dificuldade de trocar ou renegociar uma dependência técnica ou organizacional adotada pelo sistema. O registro de decisão precisa explicitá-la em seis dimensões: API proprietária, formato de dados, identidade, observabilidade, custo de saída dos dados e habilidades da equipe.

## Modelo C4

Notação que representa a arquitetura de um sistema em quatro níveis, do mais amplo ao mais detalhado: contexto, contêineres, componentes e código. O nome vem das iniciais dos quatro níveis em inglês, Context, Containers, Components e Code.

## Arquitetura de negócio

Representação da organização em capacidades, fluxos de valor, informação e estrutura organizacional. Serve para alinhar objetivos estratégicos e demandas do dia a dia, e é ao mesmo tempo a origem e o alvo da mudança que uma solução promove.

## Capacidade

Aquilo que a organização precisa saber fazer para entregar seus serviços e executar sua estratégia. Caracteriza-se pelo volume que consegue entregar em paralelo, pela competência exigida e pelos recursos que a sustentam.

## Fluxo de valor

Sequência de etapas, de ponta a ponta, pela qual a organização entrega valor a um cliente, do primeiro contato até o cliente receber esse valor. Cada etapa é nomeada por um verbo seguido do objeto, como solicitar exame.

## Arquitetura de dados

Estrutura geral dos dados e dos recursos relacionados a eles, tratada como parte da arquitetura corporativa. O DMBOK, guia de referência de gestão de dados, a define como uma das onze áreas dessa gestão, e a arquitetura de dados de cada solução precisa ser consistente com ela.

## Modelo de dados corporativo

Conjunto de modelos que descreve, de forma consistente, as entidades, os atributos e os relacionamentos da organização em quatro níveis: visão conceitual das áreas de assunto, visão de cada área de assunto, modelo lógico corporativo e modelos lógicos e físicos de cada aplicação ou projeto.

## Dados mestres

Entidades de negócio compartilhadas por várias aplicações, como cliente, aluno ou paciente. São geridos para reduzir redundância e melhorar a qualidade, por um de quatro estilos de implementação: registro, consolidação, coexistência ou centralizado.

## Linhagem de dados

Registro da origem de cada conjunto de dados e das transformações pelas quais ele passou, que permite rastrear um valor até a fonte que o produziu.

## Contrato de dados

Acordo formal entre o dono de um conjunto de dados e quem o consome, com esquema, regras de qualidade, nível de serviço e papéis. É padronizado pelo Open Data Contract Standard.

## Propriedade do dado

Atribuição de uma entidade de dado a um único responsável, que é o único a gravá-la. As demais partes a leem por interface ou a recebem por evento.

## Fonte de verdade

Local em que uma entidade de dado é registrada e mantida com autoridade, e do qual as demais cópias derivam. Nesta disciplina, equivale ao [sistema de registro](#sistema-de-registro).

## Sistema de registro

Sistema que guarda a versão autoritativa de um dado e no qual o dado é escrito primeiro. Os sistemas de dado derivado guardam cópias transformadas a partir dele. Nesta disciplina, equivale à [fonte de verdade](#fonte-de-verdade).

## Regime de consistência

Garantia declarada sobre o momento em que uma leitura, feita na fonte ou numa cópia, reflete a fonte de verdade. É forte quando reflete imediatamente e eventual quando reflete dentro de um prazo declarado.

## Arquitetura de aplicações

Subdomínio da arquitetura corporativa que mantém a visão do conjunto de aplicações da organização e dos serviços que elas oferecem, e liga a arquitetura de negócio à arquitetura de dados.

## Padrão técnico

Conjunto de processos, documentação, regras e parâmetros a observar, fixado por organismo de normalização, por autoridade ou pela própria organização, e adotado pela solução, como o sistema da nota fiscal eletrônica. Corresponde ao termo inglês *standard*. Não se confunde com a especificação de interface, que descreve uma interface particular, nem com o padrão arquitetural e o padrão de design, que correspondem a *pattern*.

## Protocolo

Conjunto de regras que duas partes seguem para trocar mensagens, com formato, sequência e tratamento de erro definidos.

## Especificação de interface

Descrição verificável de uma interface particular, com as operações ou mensagens, os esquemas dos dados trocados e os erros possíveis.

## Contrato de integração

Especificação de interface somada às garantias acordadas entre quem fornece e quem consome, como versionamento, garantia de entrega, idempotência (repetir a mesma mensagem não altera o resultado) e nível de serviço.

## Arquitetura de infraestrutura

Arquitetura dos componentes e serviços tecnológicos que sustentam as atividades da organização, como equipamentos, redes, plataformas e capacidade de processamento. O TOGAF, método de arquitetura corporativa, a chama de arquitetura de tecnologia.

## BPMN

Notação padronizada pelo Object Management Group para desenhar processos de negócio em raias, com eventos, tarefas, gateways e fluxos de sequência. A versão em uso é a 2.0.2, publicada em 2014.

## ArchiMate

Linguagem de modelagem de arquitetura corporativa mantida pela The Open Group, na versão 4, publicada em abril de 2026. Sua camada de estratégia define os elementos capacidade e fluxo de valor.

## Captura de mudanças de dados

Técnica que lê as alterações confirmadas no sistema de registro, em geral pelo log de transações do banco, e as envia como eventos para as cópias derivadas, como faz o Debezium.

## Banco por serviço

Prática em que o dado persistente de cada serviço é privado e só pode ser acessado pela interface desse serviço. É a forma de aplicar a propriedade do dado.

## Linguagem de esquema

Notação que define a estrutura e as restrições de uma mensagem, para que um programa possa validá-la. JSON Schema, Avro e Protocol Buffers são exemplos.

## Gateway de API

Componente que recebe as chamadas antes de elas chegarem a quem fornece o serviço e aplica, num ponto único, autenticação, limite de chamadas por período e roteamento entre versões da interface.

## Estilo de integração

Combinação de modo de comunicação, protocolo e formato usada numa interface, como REST, gRPC, GraphQL, mensageria, streaming de eventos, webhook ou transferência de arquivo.

## Zona de disponibilidade

Local isolado dentro de uma região de um provedor de nuvem. As réplicas da aplicação são distribuídas em zonas diferentes para que a falha de um único local não interrompa o serviço.

## Diagrama de implantação

Diagrama de apoio do modelo C4 que mostra onde as instâncias dos sistemas e dos contêineres são implantadas, nos nós de um único ambiente. Elementos de infraestrutura, como DNS, balanceador de carga e firewall, aparecem como elementos de apoio.

## Balanceador de carga

Componente que distribui as requisições entre as réplicas de um serviço e deixa de enviar requisições às réplicas que falham na verificação de saúde.

## Definição tecnológica da solução

Avaliação da infraestrutura necessária para sustentar a arquitetura de solução proposta. Ela lista os serviços e os componentes de infraestrutura exigidos, as áreas da infraestrutura atual que mudam e o custo, o prazo e os recursos dessa mudança.

## Lacuna de provisão

Requisito de serviço de infraestrutura da solução que não tem correspondente no catálogo de infraestrutura da organização. Pode exigir um serviço novo ou a substituição, a modificação ou a remoção de um serviço existente.

## Modelo técnico de referência

Catálogo que organiza, por camada arquitetural e categoria tecnológica, os padrões, os protocolos e os produtos que a organização aprova, proíbe ou mantém em avaliação. Serve de lista de partida para escolher a tecnologia de cada solução. Também é conhecido pela sigla TRM, do inglês Technical Reference Model.

## Zona de pouso

Base do ambiente em nuvem, preparada antes da primeira carga de trabalho, para que a ACME não precise reconfigurar segurança e rede a cada solução nova. Organiza contas, rede, identidade, políticas e monitoramento para que as soluções futuras já nasçam com os padrões de segurança, governança e operação da organização.

## Infraestrutura como código

Descrição da infraestrutura em arquivos declarativos, versionados e revisados como o código da aplicação, de modo que o ambiente possa ser recriado a partir da descrição.

## Autoridade de design de segurança

Grupo que decide sobre os aspectos de segurança de todas as soluções da organização. Avalia cada desenho por dois testes: a conformidade com as diretivas de segurança adotadas e o teste de vulnerabilidade contra catálogos de ameaças e de fraquezas conhecidas.

## Dado pessoal sensível

Dado pessoal sobre origem racial ou étnica, convicção religiosa, opinião política, filiação a sindicato ou a organização de caráter religioso, filosófico ou político, dado referente à saúde ou à vida sexual, dado genético ou biométrico, quando vinculado a uma pessoa natural, nos termos do art. 5º, II, da Lei Geral de Proteção de Dados Pessoais, Lei nº 13.709/2018.

## Fronteira de confiança

Linha que separa partes de uma solução que operam sob níveis diferentes de confiança. Os dados e as chamadas que a atravessam precisam ser autenticados, validados e protegidos.

## Grade de permissões

Tabela que cruza entidades, que podem ser pessoas, papéis ou sistemas, com recursos ou tarefas. Em cada cruzamento indica o tipo de acesso permitido, como leitura ou gravação, e as condições para concedê-lo.

## Menor privilégio

Princípio segundo o qual cada entidade recebe acesso apenas aos recursos de que precisa, com o menor nível de privilégio que ainda permite executar as atividades de negócio que lhe cabem.

## STRIDE

Classificação de ameaças em seis categorias: falsificação de identidade, adulteração, repúdio, divulgação de informação, negação de serviço e elevação de privilégio. Cada categoria corresponde a uma propriedade de segurança violada, e a classificação é usada para examinar cada fronteira de confiança de uma solução.

## Descrição de arquitetura

Conjunto de documentos e modelos que mostra como é a arquitetura de um sistema num determinado momento, seja de uma organização, de uma aplicação ou de uma solução. A arquitetura de linha de base e a arquitetura alvo de uma solução têm descrições diferentes, e a análise de lacunas compara as duas.

## Entregável de arquitetura

Documento ou relatório que a equipe de arquitetura produz para uma descrição de arquitetura. Reúne artefatos, que são as informações organizadas, e comentários e análises em texto livre. São exemplos a declaração de requisitos, o caso de negócio, o esboço da solução, o desenho lógico e o relatório de impacto.

## Artefato de arquitetura

Catálogo, mapa, tabela, diagrama ou modelo que trata de um aspecto da arquitetura e mostra como as entidades se relacionam. A visão é um tipo de artefato, feito a partir de um ponto de vista. O mesmo artefato pode aparecer em vários entregáveis, como o catálogo de interfaces, o diagrama de contexto e o modelo de dados.

## Entidade de arquitetura

Elemento que faz parte da arquitetura de um sistema e interessa a quem a analisa, como um requisito, uma interface ou um componente. Uma entidade pode aparecer em mais de um artefato e se relacionar com outras, por abstração, quando é generalizada numa categoria, ou por composição, quando é formada por várias.

## Caderno arquitetural

Documento em que a arquitetura da solução da ACME vai sendo registrada ao longo do curso, em dez seções mais um resumo, do contexto ao roteiro e à governança, de modo que quem chegar depois ao projeto entenda o que foi decidido e por quê. Cada exercício preenche uma parte dele. O [template](../caderno/template.md) mostra o caderno vazio, e a seção Gabaritos mostra o caderno preenchido a cada exercício.