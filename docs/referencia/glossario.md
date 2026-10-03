# Glossário

Este glossário reúne os termos usados nas páginas de conceito do curso, com a definição adotada pela disciplina. Cada entrada corresponde a uma âncora, referenciada pela seção "Antes de começar" das páginas de bloco.

## Arquitetura de solução

Disciplina responsável pela produção e pela gestão do plano de uma solução completa, que atende a uma necessidade, um problema ou uma oportunidade de negócio e se integra ao negócio em alinhamento com a estratégia, minimizando impactos negativos. O plano descreve a estrutura e o comportamento da solução em alto nível, antes da escolha dos produtos que a realizam.

## Arquiteto de solução

Profissional que conduz a definição de uma solução inteira, investiga o problema, levanta as partes interessadas, compara alternativas e responde pela integridade do desenho até a entrega. Decide sobre os cinco tipos de componente da solução, não apenas sobre software.

## Arquitetura corporativa

Disciplina que emite diretrizes, princípios e modelos válidos para a organização inteira, organizados nos domínios de negócio, aplicações, dados, infraestrutura e segurança. Opera no nível de granularidade mais alto, acima de qualquer solução isolada.

## Componentes da solução

Os cinco tipos de elemento que compõem uma solução, usados como lista de verificação para que nenhum deles fique de fora do desenho: pessoas, estruturas organizacionais, processos, informação e tecnologia.

## Bloco de construção da solução

Unidade lógica do desenho, que representa uma capacidade necessária à solução antes de estar decidido qual produto ou serviço a realiza. Um bloco de granularidade grossa agrupa vários blocos de granularidade fina.

## Direcionador de mudança

Fator que leva a organização a buscar uma solução. É interno quando nasce da própria operação, como custo, risco ou limitação de capacidade, e externo quando vem de fora, como exigência regulatória, movimento de concorrente ou mudança de expectativa do usuário.

## Parte interessada

Pessoa, papel ou área com interesse legítimo no resultado da solução, seja porque decide sobre ela, porque a usa, porque a sustenta ou porque é afetada por ela.

## Ponto de vista

Conjunto de convenções que define como construir e ler um tipo de representação da arquitetura, escolhido em função das preocupações de uma parte interessada.

## Visão

Representação concreta da arquitetura construída segundo um ponto de vista, que responde às preocupações às quais aquele ponto de vista se dirige.

## Arquitetura de linha de base

Descrição da arquitetura como ela é hoje, com os componentes existentes, suas idades, seus responsáveis e suas integrações. É o ponto de partida da comparação com a arquitetura alvo.

## Arquitetura alvo

Descrição da arquitetura pretendida ao fim de um ciclo de evolução. A diferença entre ela e a arquitetura de linha de base é o objeto da análise de lacunas.

## Artefato de linha de base

Documento ou modelo já existente que descreve parte da situação atual e entra como insumo do processo de definição da arquitetura, em vez de ser produzido do zero.

## Fase do processo de definição da arquitetura

Etapa do ciclo de vida que organiza o trabalho do arquiteto de solução, com entrada, atividades e saída próprias. O curso adota o ciclo de oito fases, de iniciação a conclusão.

## Arquitetura de software

Conjunto das decisões estruturais fundamentais sobre um sistema, difíceis de reverter depois de tomadas, que determinam sua capacidade de satisfazer os atributos de qualidade exigidos.

## Arquiteto de software

Profissional responsável por tomar e documentar as decisões estruturais de um sistema, balanceando atributos de qualidade concorrentes, requisitos funcionais e restrições de negócio.

## Atributo de qualidade

Propriedade pela qual um sistema é avaliado, como desempenho, disponibilidade, segurança ou capacidade de manutenção.

## Requisito funcional

Expectativa sobre o que o sistema faz, descrita como uma função, um comportamento ou uma resposta a um estímulo específico.

## Requisito não funcional

Categoria tradicional e mais ampla de requisito, que em diversas taxonomias reúne tanto requisitos de atributo de qualidade quanto restrições. O curso não trata requisito não funcional como sinônimo de atributo de qualidade. Atributo de qualidade é a propriedade avaliada, requisito não funcional é a categoria que agrupa essa e outras expectativas não funcionais, incluindo restrições.

## Requisito de atributo de qualidade

Expectativa concreta e mensurável sobre um atributo de qualidade, expressa em termos de estímulo, resposta e medida da resposta.

## Restrição

Decisão ou condição imposta ao sistema a partir de fora do processo de projeto, que limita as alternativas disponíveis ao arquiteto sem ser negociável por ele.

## Requisito arquiteturalmente significativo

Requisito cuja satisfação influencia materialmente a arquitetura do sistema, podendo ser de qualidade, funcional ou restritivo.

## Direcionador arquitetural

Fator, de negócio ou técnico, que orienta as decisões de arquitetura antes de se traduzir em requisitos específicos.

## Cenário de atributo de qualidade

Descrição estruturada de um requisito de qualidade em seis elementos, fonte do estímulo, estímulo, artefato afetado, ambiente, resposta e medida da resposta.

## Estilo arquitetural

Padrão de organização estrutural de um sistema, que define tipos de componentes, formas de conexão entre eles e restrições sobre essa organização.

## Princípio de design

Regra durável, derivada de objetivos, requisitos e restrições, que orienta um conjunto de decisões de desenho e admite verificação da sua aplicação por evidência observável.

## Desenho conceitual

Descrição da solução em termos de capacidades, responsabilidades e relações com o ambiente, sem estrutura interna detalhada e sem compromisso com tecnologia.

## Desenho lógico

Descrição da solução em elementos lógicos com responsabilidades, interfaces e fluxos declarados, ainda sem produto, linguagem ou plataforma escolhidos.

## Padrão arquitetural

Solução recorrente para uma preocupação transversal ou de integração entre partes de um sistema, com escopo menor que o do estilo arquitetural e maior que o do padrão de design.

## Padrão de design

Solução recorrente para a colaboração entre responsabilidades dentro de uma parte do sistema, descrita em termos de papéis, interfaces e relações entre elementos.

## Plataforma arquitetural

Conjunto estruturado e consistente de ferramentas, frameworks, bibliotecas e práticas de desenho, organizadas para implementar um ou mais estilos arquiteturais, cobrindo desenvolvimento, integração, implantação e manutenção. Adotada como decisão arquitetural própria, posterior à decisão de estilo.

## ADR

Registro de decisão de arquitetura, do inglês Architecture Decision Record, documento curto que descreve uma decisão arquitetural, o contexto que a motivou e suas consequências.

## Racional arquitetural

Base intelectual que justifica as decisões de desenho de um sistema, conectando cada escolha às metas estratégicas, aos requisitos técnicos e às restrições de negócio. Registra não apenas a escolha feita, mas o raciocínio por trás dela, as alternativas consideradas, os critérios de seleção e os impactos esperados.

## Dependência de fornecedor

Dificuldade de trocar ou negociar uma dependência técnica ou organizacional adotada pelo sistema. Precisa ficar explícita no registro de decisão em seis dimensões, API proprietária, formato de dados, identidade, observabilidade, custo de saída de dados e habilidades da equipe.

## Modelo C4

Notação para representar a arquitetura de um sistema em quatro níveis de abstração progressiva, Contexto, Contêineres, Componentes e Código, cada nível com nome próprio, o modelo inteiro chamado C4 por ter quatro níveis.

## Arquitetura de negócio

Representação da organização em capacidades, fluxos de valor, informação e estrutura organizacional, usada para alinhar objetivos estratégicos e demandas táticas, e que é ao mesmo tempo origem e alvo da mudança promovida por uma solução.

## Capacidade

Aquilo que a organização precisa conseguir fazer para entregar seus serviços e executar sua estratégia, caracterizada pelo volume que consegue entregar em paralelo, pela competência exigida e pelos recursos que a habilitam.

## Fluxo de valor

Conjunto de etapas de ponta a ponta pelo qual a organização entrega valor a um cliente, do primeiro contato com a organização até a realização desse valor pelo cliente.

## Arquitetura de dados

Subdomínio da arquitetura corporativa que trata dos dados, dos metadados e da informação da organização, e ao qual a arquitetura de dados de cada solução precisa ser consistente.

## Propriedade do dado

Atribuição de uma entidade de dado a um único responsável, que a grava, enquanto as demais partes a leem por interface ou a recebem por evento.

## Fonte de verdade

Local em que uma entidade de dado é registrada e mantida com autoridade, e do qual as demais cópias derivam.

## Regime de consistência

Garantia declarada sobre o momento em que uma cópia reflete a fonte de verdade, forte quando reflete imediatamente e eventual quando reflete dentro de um prazo declarado.

## Arquitetura de aplicações

Subdomínio da arquitetura corporativa que mantém a visão do portfólio de aplicações da organização e dos serviços que elas oferecem, e que liga a arquitetura de negócio à arquitetura de dados.

## Padrão técnico

Especificação adotada pela organização que fixa processos, documentação, regras e parâmetros a observar, correspondente ao termo inglês *standard* e distinta do padrão arquitetural e do padrão de design, que correspondem a *pattern*.

## Protocolo

Conjunto de regras que duas partes seguem para trocar mensagens, com formato, sequência e tratamento de erro definidos.

## Especificação de interface

Descrição verificável de uma interface particular, com as operações ou mensagens, os esquemas dos dados trocados e os erros possíveis.

## Contrato de integração

Especificação de interface somada às garantias acordadas entre provedor e consumidor, como versionamento, garantia de entrega, idempotência e nível de serviço.

## Arquitetura de infraestrutura

Arquitetura dos componentes e serviços tecnológicos que sustentam as atividades da organização, como equipamentos, redes, plataformas e capacidade de processamento, chamada de arquitetura de tecnologia no TOGAF.

## BPMN

Notação padronizada pelo Object Management Group para representar processos de negócio em raias, com eventos, tarefas, gateways e fluxos de sequência, na versão 2.0.2 publicada em 2014.

## ArchiMate

Linguagem de modelagem de arquitetura corporativa mantida pela The Open Group, cuja camada de estratégia define os elementos capacidade e fluxo de valor.

## Captura de mudanças de dados

Técnica que lê as alterações confirmadas no sistema de registro, em geral pelo log de transações do banco, e as propaga como eventos para as cópias derivadas, como faz o Debezium.

## Banco por serviço

Prática em que o dado persistente de cada serviço é privado e acessível apenas pela interface desse serviço, como forma de aplicar a propriedade do dado.

## Linguagem de esquema

Notação que define a estrutura e as restrições de uma mensagem para permitir validá-la por programa, como JSON Schema, Avro e Protocol Buffers.

## Gateway de API

Componente que recebe as chamadas antes do provedor e aplica num ponto único autenticação, limite de taxa e roteamento entre versões da interface.

## Estilo de integração

Combinação de modo de comunicação, protocolo e formato usada numa interface, como REST, gRPC, GraphQL, mensageria, streaming de eventos, webhook ou transferência de arquivo.

## Zona de disponibilidade

Local isolado dentro de uma região de um provedor de nuvem, usado para distribuir réplicas de modo que a falha de um único local não interrompa a aplicação.

## Diagrama de implantação

Diagrama de apoio do modelo C4 que mostra como instâncias de sistemas de software e de contêineres são implantadas nos nós de infraestrutura de um único ambiente.

## Balanceador de carga

Componente que distribui requisições entre as réplicas de um serviço e retira da distribuição as réplicas que falham na verificação de saúde.
