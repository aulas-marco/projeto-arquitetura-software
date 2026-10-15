# Plataforma arquitetural

Este bloco responde a duas perguntas que só fazem sentido depois do estilo já decidido, qual conjunto de tecnologias concretiza esse estilo na prática de desenvolvimento e operação e sobre qual fundação em nuvem esse conjunto executa.

## Antes de começar

- [Plataforma arquitetural](../referencia/glossario.md#plataforma-arquitetural)
- [Racional arquitetural](../referencia/glossario.md#racional-arquitetural)
- [Zona de pouso](../referencia/glossario.md#zona-de-pouso)
- [Infraestrutura como código](../referencia/glossario.md#infraestrutura-como-codigo)

## Conceito

Uma **plataforma arquitetural** é um conjunto estruturado e consistente de ferramentas, frameworks, bibliotecas e práticas de desenho, organizadas para implementar um ou mais [estilos arquiteturais](../modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md). Diferentemente de um framework isolado ou de uma biblioteca, a plataforma é um ambiente integrado que cobre todos os aspectos do ciclo de vida do software, incluindo desenvolvimento, integração, implantação e manutenção. Ela atua como a concretização prática de um estilo arquitetural, alinhando o princípio teórico às demandas operacionais de construir e executar o sistema.

A plataforma não escolhe o estilo, ela o executa. Por isso essa decisão vem depois da decisão de estilo, nunca antes ou junto, porque decidir framework, banco de dados ou orquestrador de execução antes de fixar o padrão estrutural inverte a ordem de dependência entre as duas decisões.

### Quatro características de uma plataforma arquitetural

A primeira é a **instanciação de estilos arquiteturais**. Toda plataforma está baseada em um ou mais estilos. O Java EE implementa a [arquitetura em camadas](../modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md#arquitetura-em-camadas) para sistemas web. O Spring Boot com Spring Cloud concretiza a [arquitetura de microsserviços](../modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md#arquitetura-de-microsservicos). O Event Store e o Apache Kafka dão suporte à [arquitetura orientada a eventos](../modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md#arquitetura-orientada-a-eventos).

A segunda é a **composição multidimensional**. Uma plataforma não é monolítica, ela reúne quatro tipos de peça. Frameworks base definem o núcleo funcional e estrutural, como o Spring Framework ou o ASP.NET Core. Ferramentas de integração cuidam da comunicação e da orquestração, como o RabbitMQ ou o gRPC. Ferramentas de monitoramento e manutenção acompanham a execução, como o Prometheus e o Grafana. Bibliotecas complementares resolvem necessidades pontuais, como o Axios para acesso HTTP e o Zod para validação de dados.

A terceira é o **alinhamento com práticas de engenharia**. A plataforma promove testabilidade, com ferramentas como o Jest e o JUnit, automação, com integração contínua e esteiras de implantação, e escalabilidade e manutenção, com orquestração de execução em Kubernetes ou Service Fabric.

A quarta é a **adaptação ao contexto**. Plataformas não são universais. Elas são selecionadas e configuradas a partir de um racional arquitetural, apresentado no Conceito do [bloco 4 da Aula 3](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md), e a comparação entre plataformas candidatas usa os seis critérios de seleção do [bloco 1](bloco-1-definicao-tecnologica-e-trm.md#seis-criterios-de-selecao), que são aderência ao requisito, maturidade, suporte, custo total de propriedade, competência da equipe e portabilidade. Uma plataforma tecnicamente superior que ninguém no time sabe operar tem custo real maior do que o preço de licença sugere, e é o critério de competência da equipe que captura isso.

### Exemplos de plataforma por estilo

Os quatro exemplos abaixo ilustram a composição de plataformas para estilos da Aula 3 e não constituem recomendação de uso. Cada um começa pelo estilo que materializa e pela função da plataforma, ou seja, o caminho que o trabalho percorre de ponta a ponta dentro dela, e só então nomeia as peças principais e o que cada uma faz. Todos vêm acompanhados de desenho, que segue a convenção de diagrama de plataforma, com os serviços transversais na base, ou a convenção de infraestrutura do fornecedor, em que o nome do produto aparece em amarelo. A leitura da função para a lista de ferramentas evita que a plataforma pareça um amontoado de nomes.

#### Plataforma Java EE e Jakarta EE

Materializa o [estilo em camadas](../modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md#arquitetura-em-camadas). O pedido entra pelo navegador ou por um cliente móvel, sempre sobre HTTPS, e chega a um servidor de aplicação que executa tudo em um processo só. Dentro dele o trabalho atravessa três contêineres com responsabilidades separadas. O contêiner web recebe a requisição e cuida da apresentação. O contêiner de negócio executa a regra de domínio e delimita a transação. O contêiner de integração conversa com o mundo externo, com a mensageria e com os sistemas corporativos que a organização já tem. A persistência sai do contêiner de negócio para o banco por um mapeador objeto-relacional. Quatro serviços transversais, segurança, transação, observabilidade e configuração, valem para os três contêineres ao mesmo tempo, e é isso que distingue uma plataforma de um conjunto de bibliotecas, você não os instala componente a componente.

Entre as peças, o Servlet é a base de tudo no contêiner web, a interface de programação que recebe a requisição HTTP e devolve a resposta. Sobre ela, o JSF monta a tela no servidor a partir de componentes reutilizáveis, e o JAX-RS expõe a mesma lógica como serviço REST para quem consome por programa. No contêiner de negócio, o CDI injeta dependências e controla o ciclo de vida dos objetos, o EJB embrulha a regra de negócio em componentes cuja transação é aberta e fechada pelo próprio servidor, sem código explícito, e o Bean Validation declara a regra de validação junto do dado que ela protege. No contêiner de integração, o JMS troca mensagens assíncronas, o conector JCA é a ponte padronizada com sistemas legados e o agendador dispara rotinas em horário fixo. Entre negócio e banco, o JPA define o mapeamento objeto-relacional e o Hibernate é a implementação mais usada dele.

![Plataforma Java EE e Jakarta EE. À esquerda, navegador e cliente móvel acessam por HTTPS e REST. No centro, um servidor de aplicação Java reúne três contêineres, o web com JSF, Servlet e JAX-RS, o de negócio com CDI, EJB e Bean Validation, e o de integração com JMS, conector JCA e agendador. Abaixo, JPA e Hibernate persistem em PostgreSQL e Oracle. À direita, mensageria Kafka ou ActiveMQ e sistemas externos de ERP, CRM e legado. Na base, serviços transversais de segurança, transações, observabilidade e configuração.](../assets/images/plataforma-java-ee.png)

*Plataforma Java EE e Jakarta EE. Os três contêineres são a divisão estrutural que o estilo em camadas impõe, e a faixa de serviços transversais na base é o que nenhum framework isolado entrega. Fonte: material base do professor.*

Esta é a plataforma da camada web da ACME, descrita na [arquitetura de linha de base](../caso-acme/linha-de-base.md) como JSF e EJB sobre servidor de aplicação fora de suporte desde 2018.

#### Plataforma web elástica em nuvem

Materializa um [estilo em camadas](../modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md#arquitetura-em-camadas) distribuído entre zonas de disponibilidade, que são instalações fisicamente separadas dentro da mesma região. A função aqui é sobreviver à perda de uma zona inteira sem interrupção perceptível, e absorver variação de carga sem intervenção manual. O nome do domínio é resolvido por um serviço de DNS gerenciado. O conteúdo estático sai de uma rede de distribuição apoiada em armazenamento de objetos, o que tira esse tráfego de cima dos servidores. O pedido dinâmico cai num balanceador, que distribui entre máquinas virtuais organizadas em grupos de autoescalonamento, replicados nas duas zonas. Há dois níveis desses grupos, um para a camada web e outro para a de aplicação, e o banco fica em serviço gerenciado com réplica na segunda zona.

A peça que define essa plataforma é o grupo de autoescalonamento, que cria e destrói máquinas conforme a métrica observada, e é ele que transforma capacidade fixa em capacidade elástica. O balanceador é o que torna isso invisível para o cliente, porque o endereço não muda quando o número de máquinas muda. A réplica do banco entre zonas é o que impede que a perda de uma zona leve o dado junto.

![Arquitetura web sobre serviços da AWS, com Route 53 e CloudFront na borda, recursos estáticos em S3, duas camadas de balanceamento elástico sobre grupos de autoescalonamento de instâncias EC2 distribuídos em duas zonas de disponibilidade, e banco RDS principal replicado entre zonas.](../assets/images/plataforma-web-aws.png)

*Plataforma web elástica sobre serviços da AWS. As duas colunas cinza são as zonas de disponibilidade, e as setas amarelas horizontais são os grupos de autoescalonamento que atravessam as duas. Fonte: material base do professor.*

#### Plataforma de microsserviços

Materializa o [estilo de microsserviços](../modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md#arquitetura-de-microsservicos). A função é permitir que times diferentes construam, implantem e escalem partes do sistema de forma independente, e toda a plataforma existe para tornar essa independência operacionalmente viável. O cliente entra por um único ponto, o gateway de API, que aplica o padrão [API Gateway](../modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md#api-gateway), roteia para o serviço correto e concentra o que seria repetido em cada um, como terminação de HTTPS e limite de requisição. Dentro do agrupamento, cada serviço roda em contêiner próprio, com seu armazenamento, e se comunica com os demais por chamada direta quando precisa de resposta imediata ou por barramento de eventos quando não precisa. A observabilidade é obrigatória e não opcional, porque com o sistema dividido em muitos processos não existe mais um registro único onde olhar. A esteira de entrega faz parte da plataforma, não é acessório dela, porque implantação independente sem automação de implantação é promessa vazia.

Entre as peças, o Kubernetes é o orquestrador que decide em qual máquina cada contêiner roda, reinicia o que falha e escala o que satura. O Docker é o formato de empacotamento que torna o serviço idêntico em qualquer máquina. O NGINX Ingress é o gateway que traduz o endereço externo para o serviço interno. O Kafka é o barramento que guarda o evento publicado e permite que vários consumidores o leiam no próprio ritmo. O Prometheus coleta métricas, o Grafana as apresenta em painel e o OpenTelemetry padroniza a coleta de rastros que atravessam vários serviços, que é o único jeito de responder onde um pedido demorou.

![Plataforma de microsserviços. À esquerda, clientes web, móvel e usuários entram por HTTP e HTTPS num gateway de API com NGINX Ingress. No centro, um agrupamento Kubernetes com camada de serviço e três pods em contêineres Docker, um serviço de catálogo em Java, um de pedidos em .NET e um de pagamentos em Node.js, apoiados por Redis, PostgreSQL e um barramento Kafka. À direita, observabilidade com Prometheus para métricas, Grafana para painéis e OpenTelemetry para rastros. Na base, a esteira de integração e entrega, do código ao GitHub Actions, ao registro de contêineres e à implantação no Kubernetes.](../assets/images/plataforma-microsservicos.png)

*Plataforma de microsserviços. Os três serviços usam linguagens diferentes, o que o estilo permite e a plataforma precisa sustentar, e a esteira na base mostra que a implantação independente é parte da plataforma. Fonte: material base do professor.*

Na variante Java dessa pilha, o Spring Boot é o framework base de cada serviço, o Spring Cloud Config centraliza a configuração fora do código, o Eureka permite que um serviço descubra o endereço do outro sem endereço fixo, o Spring Cloud Gateway faz o papel do gateway de API, o Keycloak cuida de autenticação e autorização, o Elastic Stack concentra os registros de todos os serviços em um lugar só, e o WireMock simula as APIs externas durante o teste.

#### Plataforma orientada a eventos

Materializa o [estilo orientado a eventos](../modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md#arquitetura-orientada-a-eventos). A função é desacoplar quem produz de quem consome no tempo, de modo que o produtor não espere resposta e o consumidor processe no seu próprio ritmo, o que é justamente o que permite absorver pico. O produtor publica um evento num fluxo, e o fluxo o retém por um período configurado. A partir dele, consumidores independentes fazem coisas diferentes com o mesmo evento, um grava em armazenamento bruto para análise posterior, outro dispara uma função que atualiza um banco de resposta rápida, outro alimenta uma aplicação de processamento contínuo. Acrescentar um quarto consumidor depois não exige mudar o produtor, e essa propriedade é o principal ganho do estilo.

Entre as peças, o fluxo de eventos é o centro da plataforma, e o que o distingue de uma fila tradicional é a retenção, porque a fila entrega e descarta, enquanto o fluxo guarda e permite releitura. O processamento contínuo sobre o fluxo é o que transforma evento em agregação sem passar por banco intermediário. O armazenamento de eventos guarda a sequência completa como fonte da verdade, de modo que o estado atual possa ser recalculado. Um mediador de integração cuida de rotas e conversões entre formatos quando as pontas não falam a mesma língua, e um gateway de API publica para fora o que é consumido por terceiros.

![Arquitetura de streaming sobre serviços da AWS, com fluxo de dados em tempo real chegando ao Amazon Kinesis, que despacha para bucket S3, para funções Lambda com persistência em DynamoDB, e para aplicações Kinesis executando em instâncias EC2.](../assets/images/plataforma-streaming-aws.png)

*Plataforma orientada a eventos sobre serviços da AWS. Um mesmo fluxo alimenta três destinos diferentes ao mesmo tempo, que é a propriedade que o estilo busca. Fonte: material base do professor.*

Na pilha aberta equivalente, o Apache Kafka é o fluxo, o Kafka Streams o processamento contínuo, o Event Store o armazenamento de eventos, o Apache Camel o mediador de integração, o Kong API Gateway a publicação externa e o Confluent Control Center o monitoramento do fluxo.


### Zona de pouso, a fundação da plataforma

A plataforma escolhida precisa de um ambiente que a receba, e esse ambiente é a **[zona de pouso](../referencia/glossario.md#zona-de-pouso)**, do inglês *landing zone*, a fundação do ambiente em nuvem preparada antes da primeira carga de trabalho. Ela organiza contas, rede, identidade, políticas e monitoramento para que cada solução futura chegue a um ambiente já definido e herde os padrões de segurança, governança e operação da organização. A zona de pouso é o lugar onde a carga executa, e a [infraestrutura em nuvem](../modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md) descrita na Aula 4 fornece as camadas de execução e a topologia sobre as quais ela se apoia.

Os provedores oferecem estruturas oficiais para essa fundação. Na AWS, o AWS Control Tower configura e governa um ambiente de várias contas conforme práticas prescritivas, e o Landing Zone Accelerator on AWS, solução de código aberto construída sobre o AWS CDK, complementa o Control Tower em cargas altamente reguladas. Na Azure, a Azure landing zone é uma arquitetura para governar, proteger e escalar um ambiente de várias assinaturas, composta por uma landing zone de plataforma, com recursos centralizados, e por landing zones de carga de trabalho. O detalhe de configuração de cada estrutura fica na documentação do provedor, e este bloco trata dos pilares que elas têm em comum.

Os pilares são cinco, e a Figura 1 os apresenta sobre uma base comum de infraestrutura como código e etiquetas.

<figure markdown="span">
![Cinco colunas numeradas sobre uma base comum. As colunas são contas ou assinaturas por ambiente, rede em topologia hub-spoke, identidade centralizada, políticas automatizadas e monitoramento com faturamento consolidado. Sob as colunas, a base comum indica infraestrutura como código e etiquetas de projeto, ambiente, time e centro de custo.](../assets/images/modulo-5-pilares-zona-de-pouso.svg){ .module-diagram }
</figure>

*Figura 1 — Os cinco pilares da zona de pouso sobre uma base comum. Fonte: material do curso, com base na documentação de zona de pouso da AWS e da Azure.*

1. As contas, na AWS, ou assinaturas, na Azure, separam os ambientes de desenvolvimento, homologação e produção, de modo que a credencial usada por um desenvolvedor em desenvolvimento deixe de alcançar os dados de produção e que um erro de teste fique contido na conta onde ocorreu.
2. A segmentação de rede segue a topologia hub-spoke, em que uma rede central compartilhada se liga a redes privadas dedicadas a cada carga de trabalho, com apenas o ponto de entrada, como o gateway de APIs ou o balanceador de carga, em sub-rede pública, e com serviços de retaguarda e bancos de dados em sub-redes privadas. Quando parte da solução permanece num centro de dados próprio, a rede central concentra também a ligação com ele, por enlace dedicado ou por VPN.
3. A identidade centralizada reúne num só lugar o controle de quem da equipe acessa cada conta e com qual perfil, o que facilita a auditoria das operações sensíveis.
4. As políticas de conformidade automatizadas, que na AWS são as políticas de controle de serviço do AWS Organizations e na Azure são o Azure Policy, aplicam as regras da organização a todo recurso criado, como a recusa de um recurso fora da região permitida ou sem as etiquetas obrigatórias.
5. O monitoramento com faturamento consolidado permite acompanhar no mesmo lugar o comportamento e o custo de todos os ambientes.

Os dois primeiros pilares, ambientes separados e rede segmentada, também funcionam como controles de segurança, e o [bloco 3](bloco-3-seguranca-fim-a-fim.md) os trata nesse papel.

#### Infraestrutura como código e etiquetas

A **[infraestrutura como código](../referencia/glossario.md#infraestrutura-como-codigo)** descreve a infraestrutura em arquivos declarativos, versionados e revisados como o código da aplicação. Com essa descrição, o ambiente pode ser recriado a partir dos arquivos, cada mudança de rede, de política ou de capacidade passa a ter autor, data e revisão no histórico, e os três ambientes podem ser criados da mesma descrição com parâmetros diferentes, o que reduz a diferença entre homologação e produção. A descrição declarativa também reduz a [dependência de fornecedor](../referencia/glossario.md#dependencia-de-fornecedor), e uma ferramenta portável entre provedores, como o Terraform, mantém uma só base de código quando a organização opera em mais de uma nuvem.

As etiquetas obrigatórias são quatro, projeto, ambiente, time e centro de custo. Aplicadas pelo código e exigidas por uma política que recusa recurso sem etiqueta, elas permitem responder quanto custa o ambiente de produção de um serviço e quanto uma equipe consome em homologação.

#### Observabilidade como camada transversal

A observabilidade define como a equipe sabe o que acontece na solução, e por isso atravessa todas as camadas da plataforma. Ela se organiza em três sinais, o registro estruturado de eventos, as métricas e o rastreamento, e o OpenTelemetry é o padrão aberto de coleta de métricas e rastros. Quando a solução se divide em vários serviços, deixa de existir um registro único onde olhar, e o rastreamento que atravessa os serviços é a forma de responder em que trecho do caminho o tempo foi gasto.

Região, zonas de disponibilidade e camadas de execução já foram tratadas no [bloco 4 da Aula 4](../modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md), e este bloco não as repete.

## Uso pelo arquiteto

Assim como o estilo arquitetural é a maior decisão que um arquiteto toma em um projeto, a plataforma arquitetural é a maior decisão tecnológica do projeto. Por consequência, ela precisa ser justificada e registrada em um ADR próprio, escrito no [bloco 4](bloco-4-adr-de-plataforma.md) desta aula, e a zona de pouso que recebe a plataforma é registrada na mesma decisão.

O arquiteto documenta a comparação antes de decidir, em um **quadro comparativo** que lista as plataformas candidatas nas linhas e os seis critérios de seleção do [bloco 1](bloco-1-definicao-tecnologica-e-trm.md#seis-criterios-de-selecao) nas colunas, com uma nota curta em cada célula. Esse quadro entra no ADR de plataforma como evidência de que a escolha considerou alternativas reais, não apenas a plataforma mais familiar ao time, o que faz a decisão resistir a questionamento meses depois.

## Exercício 18

A ACME é a universidade privada brasileira em modernização incremental do sistema acadêmico, cujo núcleo transacional em COBOL sobre o monitor CICS segue em operação durante toda a transição, com uma camada web em JSF e EJB e integrações com o ERP financeiro e o ambiente virtual de aprendizagem resolvidas por arquivo, em lote noturno. O exercício parte do estilo arquitetural recomendado no [exercício 10](../modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md#exercicio-10) da Aula 3, e a plataforma escolhida aqui é a entrada do ADR de plataforma do exercício 20, no [bloco 4](bloco-4-adr-de-plataforma.md).

### Item 1: Plataformas candidatas para o estilo escolhido

O diagrama abaixo mostra as partes do sistema atual com as quais qualquer plataforma candidata precisa conviver durante a transição, conforme a [arquitetura de linha de base](../caso-acme/linha-de-base.md).

```mermaid
graph LR
    NOVA["Plataforma candidata"] -.->|"convive com"| CICS["Núcleo COBOL sobre CICS, em operação até o fim da transição"]
    NOVA -.->|"convive com"| ORA[("Banco Oracle 12c compartilhado, 11 TB")]
    NOVA -.->|"convive com"| LOTE["Lotes noturnos por arquivo"]
    LOTE --> ERP["ERP financeiro"]
    LOTE --> AVA["Ambiente virtual de aprendizagem"]
    CICS --> ORA
```

1. Indique, entre os exemplos de plataforma por estilo apresentados no Conceito, duas plataformas candidatas capazes de concretizar o estilo recomendado no exercício 10.
2. Para cada plataforma candidata, liste as ferramentas concretas que a compõem, no nível de detalhe dos exemplos do Conceito.

### Item 2: Quadro comparativo pelos seis critérios

A tabela abaixo reúne dados do [dossiê da ACME](../caso-acme/index.md) e da linha de base para os seis critérios de seleção apresentados no [bloco 1](bloco-1-definicao-tecnologica-e-trm.md#seis-criterios-de-selecao). O quadro preenchido neste item é o que alimenta o campo de alternativas do ADR de plataforma do exercício 20, no [bloco 4](bloco-4-adr-de-plataforma.md).

| Critério | Dado do caso |
| --- | --- |
| Aderência ao requisito | R6, o portal sustenta 5.800 sessões simultâneas na abertura da matrícula, com percentil 95 do tempo de confirmação em até 4 segundos, e R4, a solução opera em um dos dois provedores de nuvem aprovados em 12/03/2026 |
| Maturidade | O dossiê não registra dado sobre a maturidade das plataformas candidatas |
| Suporte | O dossiê não registra dado sobre o suporte das plataformas candidatas |
| Custo total de propriedade | Orçamento de R$ 6,2 milhões para o primeiro ciclo de 12 meses, e licenciamento Oracle que obriga a licenciar todos os núcleos físicos de qualquer ambiente virtualizado |
| Competência da equipe | Camada web em Java sustentada por 9 pessoas, 6 internas e 3 da fábrica, sem escassez, mas sem experiência em JSF 1.2 nos contratados desde 2021 |
| Portabilidade | Dois provedores de nuvem pré-aprovados pelo Conselho Universitário em 12/03/2026, com decisões de plataforma portáveis entre os dois, e autenticação por padrões abertos de identidade |

1. Para cada um dos quatro critérios com dado do caso, marque qual das duas plataformas candidatas do Item 1 atende melhor, ou se as duas empatam, e registre o motivo em uma linha com base no dado.
2. Para os critérios maturidade e suporte, escreva uma frase que diga qual dado falta e quem poderia fornecê-lo, sem atribuir valor às plataformas, conforme o Item 3 do [exercício 17](bloco-1-definicao-tecnologica-e-trm.md#exercicio-17).
3. Escolha uma das duas plataformas e justifique a escolha considerando a restrição de convivência com o legado mostrada no diagrama do Item 1.

### Item 3: Zona de pouso da solução

O diagrama abaixo descreve a zona de pouso proposta para a solução nova da ACME, com a organização na nuvem, as cinco contas, a ligação híbrida ao centro de dados onde permanecem o núcleo COBOL e o Oracle, e os recursos da conta de produção.

```mermaid
graph LR
    ORG["Organização<br/>da ACME<br/>na nuvem"]
    REG["Regras aplicadas<br/>a todas as contas"]
    ACE["Acesso da equipe<br/>por perfil, com<br/>credencial única"]
    CUS["Consulta de custo<br/>por projeto, ambiente,<br/>time e centro de custo"]
    DEV["Conta de<br/>desenvolvimento"]
    HOM["Conta de<br/>homologação"]
    PRD["Conta de<br/>produção"]
    NET["Conta de<br/>rede central"]
    SEC["Conta de segurança<br/>e registros"]
    RED["Rede da produção:<br/>gateway em sub-rede pública,<br/>serviços e bancos<br/>em sub-redes privadas"]
    REC["Recursos da produção,<br/>listados na<br/>tabela abaixo"]
    CD["Centro de dados da ACME<br/>núcleo COBOL sob CICS<br/>e banco Oracle"]
    ORG --> REG
    ORG --> ACE
    ORG --> CUS
    ORG --> DEV
    ORG --> HOM
    ORG --> PRD
    ORG --> NET
    ORG --> SEC
    NET ---|"ligação híbrida"| CD
    NET --> RED
    PRD --> RED
    PRD --> REC
    PRD -.->|"envia os registros"| SEC
```

Os três requisitos do [dossiê](../caso-acme/index.md) que orientam o desenho são os seguintes.

| Código | Requisito | Origem |
| --- | --- | --- |
| R4 | A solução opera em um dos dois provedores de nuvem aprovados em 12/03/2026 | Conselho Universitário |
| R14 | Nenhum dado pessoal de aluno é processado fora do território nacional | Jurídico, parecer de 28/04/2026 |
| R9 | Toda leitura de dado pessoal de aluno é registrada em trilha de auditoria, com retenção de 5 anos | Encarregada de proteção de dados |

A tabela a seguir lista seis recursos da conta de produção com as etiquetas que cada um traz. Os valores das etiquetas são ilustrativos e não constam do dossiê.

| Recurso | Etiquetas que o recurso traz |
| --- | --- |
| Serviço de matrícula | projeto, ambiente, time |
| Banco do serviço de matrícula | projeto, time, centro de custo |
| Gateway de APIs | ambiente, time, centro de custo |
| Serviço de notas | projeto, ambiente, time, centro de custo |
| Fila de eventos de notas | projeto, ambiente |
| Bucket de trilha de auditoria | projeto, ambiente, centro de custo |

1. Associe cada elemento do diagrama ao pilar da zona de pouso, entre os cinco da Figura 1, que ele realiza.
2. Indique, para cada recurso da tabela, a etiqueta obrigatória que falta, ou registre que as quatro estão presentes.
3. Responda em uma linha qual requisito justifica a existência da conta de segurança e registros.
4. Indique qual dos requisitos R4 e R14 leva a descrever os pilares com uma ferramenta de infraestrutura como código portável entre provedores, e qual deles justifica uma política que recuse recursos fora da região nacional.

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Mendes, M. (2026b). *Guias de projeto de arquitetura de software* [Material de curso, versão arquivada]. https://github.com/aulas-marco/projeto-arquitetura-software/tree/30f15cd (guia 2.2, fonte da definição, das quatro características e dos exemplos de plataforma por estilo e das representações visuais reproduzidas nesta página)
- Ford, N., & Richards, M. (2020). *Fundamentals of software architecture*. O'Reilly. (comparação por atributo de qualidade, aplicada aqui a plataformas)
- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seção 7.5, definição da infraestrutura de rede, em que cada interface entre componentes recebe o serviço de rede que a sustenta, base da segmentação de rede e da ligação híbrida da zona de pouso)
- Amazon Web Services. (n.d.-d). *What is AWS Control Tower?* AWS Control Tower User Guide. Acesso em 15 de outubro de 2026. https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html
- Amazon Web Services. (n.d.-e). *Landing Zone Accelerator on AWS: Solution overview*. Landing Zone Accelerator on AWS Implementation Guide. Acesso em 15 de outubro de 2026. https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/solution-overview.html
- Microsoft. (2025). *What is an Azure landing zone?* Cloud Adoption Framework, Microsoft Learn. Acesso em 15 de outubro de 2026. https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/

**Material do curso.** Glossário, entradas [plataforma arquitetural](../referencia/glossario.md#plataforma-arquitetural), [racional arquitetural](../referencia/glossario.md#racional-arquitetural), [zona de pouso](../referencia/glossario.md#zona-de-pouso) e [infraestrutura como código](../referencia/glossario.md#infraestrutura-como-codigo). Dossiê da instituição fictícia [ACME](../caso-acme/index.md) e [arquitetura de linha de base](../caso-acme/linha-de-base.md). A estrutura dos cinco pilares, as quatro etiquetas obrigatórias e a figura 1 são convenções do curso.
