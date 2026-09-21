# Plataforma arquitetural

Este bloco dá sequência à aula respondendo a uma pergunta que só faz sentido depois do estilo já decidido, qual conjunto de tecnologias concretiza esse estilo na prática de desenvolvimento e operação.

## Antes de começar

- [Plataforma arquitetural](../referencia/glossario.md#plataforma-arquitetural)
- [Racional arquitetural](../referencia/glossario.md#racional-arquitetural)

## Conceito

Uma **plataforma arquitetural** é um conjunto estruturado e consistente de ferramentas, frameworks, bibliotecas e práticas de desenho, organizadas para implementar um ou mais estilos arquiteturais. Diferentemente de um framework isolado ou de uma biblioteca, a plataforma é um ambiente integrado que cobre todos os aspectos do ciclo de vida do software, incluindo desenvolvimento, integração, implantação e manutenção. Ela atua como a concretização prática de um estilo arquitetural, alinhando o princípio teórico às demandas operacionais de construir e executar o sistema.

A plataforma não escolhe o estilo, ela o executa. Por isso essa decisão vem depois da decisão de estilo, nunca antes ou junto, porque decidir framework, banco de dados ou orquestrador de execução antes de fixar o padrão estrutural inverte a ordem de dependência entre as duas decisões.

### Quatro características de uma plataforma arquitetural

A primeira é a **instanciação de estilos arquiteturais**. Toda plataforma está baseada em um ou mais estilos. O Java EE implementa arquitetura em camadas e web. O Spring Boot com Spring Cloud concretiza microsserviços. O Event Store e o Apache Kafka dão suporte à arquitetura baseada em eventos.

A segunda é a **composição multidimensional**. Uma plataforma não é monolítica, ela reúne quatro tipos de peça. Frameworks base definem o núcleo funcional e estrutural, como o Spring Framework ou o ASP.NET Core. Ferramentas de integração cuidam da comunicação e da orquestração, como o RabbitMQ ou o gRPC. Ferramentas de monitoramento e manutenção acompanham a execução, como o Prometheus e o Grafana. Bibliotecas complementares resolvem necessidades pontuais, como o Axios para acesso HTTP e o Zod para validação de dados.

A terceira é o **alinhamento com práticas de engenharia**. A plataforma promove testabilidade, com ferramentas como o Jest e o JUnit, automação, com integração contínua e esteiras de implantação, e escalabilidade e manutenção, com orquestração de execução em Kubernetes ou Service Fabric.

A quarta é a **adaptação ao contexto**. Plataformas não são universais. Elas são selecionadas e configuradas a partir de um racional arquitetural, apresentado no Conceito do [bloco 4 da Aula 3](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md), que leva em conta sete fatores.

1. atendimento aos requisitos funcionais
2. atendimento aos requisitos não funcionais, como escalabilidade e tolerância a falhas
3. atendimento integral aos requisitos arquiteturais
4. conhecimento técnico do time
5. custos de aquisição e de renovação de ferramentas
6. facilidade de uso
7. confiabilidade dos fornecedores

Esses sete fatores são os critérios de comparação entre plataformas candidatas. Uma plataforma tecnicamente superior que ninguém no time sabe operar tem custo real maior do que o preço de licença sugere, e é o quarto fator que captura isso.

### Exemplos de plataforma por estilo

Os exemplos abaixo são ilustrações de composição, não recomendações de uso. Cada um começa pelo estilo que materializa e pela função da plataforma, ou seja, o caminho que o trabalho percorre de ponta a ponta dentro dela, e só então nomeia as peças principais e o que cada uma faz. Ler na ordem inversa, da lista de ferramentas para a função, é o erro que faz uma plataforma parecer um amontoado de nomes.

Sete dos exemplos vêm acompanhados de desenho. Quatro deles usam a convenção de diagrama de plataforma, que mostra a pilha inteira com os serviços transversais na base, e três usam a convenção de diagrama de infraestrutura do fornecedor, em que o nome do produto aparece em amarelo.

Esta é a seção mais longa da aula e serve como catálogo de consulta. Em sala, percorremos dois ou três exemplos, escolhidos conforme os estilos que a turma defendeu no exercício da Aula 3, e os demais ficam para leitura posterior e para apoiar o Exercício 18.

#### Plataforma Java EE e Jakarta EE

Materializa o estilo em camadas. O pedido entra pelo navegador ou por um cliente móvel, sempre sobre HTTPS, e chega a um servidor de aplicação que executa tudo em um processo só. Dentro dele o trabalho atravessa três contêineres com responsabilidades separadas. O contêiner web recebe a requisição e cuida da apresentação. O contêiner de negócio executa a regra de domínio e delimita a transação. O contêiner de integração conversa com o mundo externo, com a mensageria e com os sistemas corporativos que a organização já tem. A persistência sai do contêiner de negócio para o banco por um mapeador objeto-relacional. Quatro serviços transversais, segurança, transação, observabilidade e configuração, valem para os três contêineres ao mesmo tempo, e é isso que distingue uma plataforma de um conjunto de bibliotecas, você não os instala componente a componente.

Entre as peças, o Servlet é a base de tudo no contêiner web, a interface de programação que recebe a requisição HTTP e devolve a resposta. Sobre ela, o JSF monta a tela no servidor a partir de componentes reutilizáveis, e o JAX-RS expõe a mesma lógica como serviço REST para quem consome por programa. No contêiner de negócio, o CDI injeta dependências e controla o ciclo de vida dos objetos, o EJB embrulha a regra de negócio em componentes cuja transação é aberta e fechada pelo próprio servidor, sem código explícito, e o Bean Validation declara a regra de validação junto do dado que ela protege. No contêiner de integração, o JMS troca mensagens assíncronas, o conector JCA é a ponte padronizada com sistemas legados e o agendador dispara rotinas em horário fixo. Entre negócio e banco, o JPA define o mapeamento objeto-relacional e o Hibernate é a implementação mais usada dele.

![Plataforma Java EE e Jakarta EE. À esquerda, navegador e cliente móvel acessam por HTTPS e REST. No centro, um servidor de aplicação Java reúne três contêineres, o web com JSF, Servlet e JAX-RS, o de negócio com CDI, EJB e Bean Validation, e o de integração com JMS, conector JCA e agendador. Abaixo, JPA e Hibernate persistem em PostgreSQL e Oracle. À direita, mensageria Kafka ou ActiveMQ e sistemas externos de ERP, CRM e legado. Na base, serviços transversais de segurança, transações, observabilidade e configuração.](../assets/images/plataforma-java-ee.png)

*Plataforma Java EE e Jakarta EE. Os três contêineres são a divisão estrutural que o estilo em camadas impõe, e a faixa de serviços transversais na base é o que nenhum framework isolado entrega. Fonte: material base do professor.*

Esta é a plataforma da camada web da ACME, descrita na [arquitetura de linha de base](../caso-acme/linha-de-base.md) como JSF e EJB sobre servidor de aplicação fora de suporte desde 2018.

#### Plataforma .NET

Materializa o mesmo estilo em camadas, com a camada de domínio isolada no centro. O tráfego entra por um ponto único de borda, que resolve o endereço e encaminha, passa por uma camada de gestão de API, que aplica política de acesso, cota e versão antes de o pedido tocar a aplicação, e só então alcança a plataforma de aplicação. Ali convivem quatro modelos de execução para públicos diferentes, todos apoiados na mesma camada de domínio, o que garante que a regra de negócio não seja reescrita a cada canal. A persistência vai para três repositórios com propósitos distintos, e o que é assíncrono sai por um intermediário de mensagens. O empacotamento em contêiner e a orquestração ficam abaixo da aplicação, e os serviços transversais de identidade, telemetria e entrega atravessam tudo.

Entre as peças, o ASP.NET Core é o framework que atende requisição web e de API. O serviço de trabalho executa processamento em segundo plano, fora do ciclo da requisição, para tarefas longas ou agendadas. O gRPC é o canal de chamada entre serviços, com contrato declarado e formato binário, mais eficiente do que REST quando as duas pontas são internas. O Blazor executa código C# no próprio navegador, o que dispensa uma segunda linguagem na interface. O Entity Framework Core é o mapeador objeto-relacional, com migrações geradas a partir do código. Do lado de fora, o SQL Server guarda o dado relacional, o Cosmos DB o dado sem esquema fixo e o Redis o dado de acesso muito frequente em memória. A observabilidade vem do OpenTelemetry, que é o padrão aberto de coleta de métricas e rastros, e do Application Insights, que os apresenta.

![Plataforma .NET. À esquerda, navegador, aplicativo móvel e API de parceiro entram por Azure Front Door e gestão de API. No centro, a plataforma de aplicação .NET com ASP.NET Core, serviço de trabalho, serviço gRPC e Blazor sobre uma camada de domínio e Entity Framework Core. À direita, repositórios de dados com SQL Server, Cosmos DB e Redis, e mensageria com Azure Service Bus ou RabbitMQ. Abaixo, empacotamento em Docker e orquestração em AKS Kubernetes. Na base, serviços transversais de plataforma, Microsoft Entra ID, OpenTelemetry, Application Insights e a esteira de integração e entrega.](../assets/images/plataforma-dotnet.png)

*Plataforma .NET. É a mesma forma estrutural da plataforma Java EE acima, com outro conjunto de ferramentas, e esse par é a demonstração de que um estilo admite mais de uma plataforma candidata. Fonte: material base do professor.*

Em variantes dessa mesma pilha aparecem ainda o Razor Pages para páginas renderizadas no servidor, o MediatR para separar comando de consulta, o Identity Server com OAuth2 e OpenID Connect para autenticação delegada, o Autofac para injeção de dependências, o Swashbuckle para gerar documentação OpenAPI a partir do código, e xUnit com FluentAssertions para teste.

#### Plataforma web elástica em nuvem

Materializa um estilo em camadas distribuído entre zonas de disponibilidade, que são instalações fisicamente separadas dentro da mesma região. A função aqui é sobreviver à perda de uma zona inteira sem interrupção perceptível, e absorver variação de carga sem intervenção manual. O nome do domínio é resolvido por um serviço de DNS gerenciado. O conteúdo estático sai de uma rede de distribuição apoiada em armazenamento de objetos, o que tira esse tráfego de cima dos servidores. O pedido dinâmico cai num balanceador, que distribui entre máquinas virtuais organizadas em grupos de autoescalonamento, replicados nas duas zonas. Há dois níveis desses grupos, um para a camada web e outro para a de aplicação, e o banco fica em serviço gerenciado com réplica na segunda zona.

A peça que define essa plataforma é o grupo de autoescalonamento, que cria e destrói máquinas conforme a métrica observada, e é ele que transforma capacidade fixa em capacidade elástica. O balanceador é o que torna isso invisível para o cliente, porque o endereço não muda quando o número de máquinas muda. A réplica do banco entre zonas é o que impede que a perda de uma zona leve o dado junto.

![Arquitetura web sobre serviços da AWS, com Route 53 e CloudFront na borda, recursos estáticos em S3, duas camadas de balanceamento elástico sobre grupos de autoescalonamento de instâncias EC2 distribuídos em duas zonas de disponibilidade, e banco RDS principal replicado entre zonas.](../assets/images/plataforma-web-aws.png)

*Plataforma web elástica sobre serviços da AWS. As duas colunas cinza são as zonas de disponibilidade, e as setas amarelas horizontais são os grupos de autoescalonamento que atravessam as duas. Fonte: material base do professor.*

#### Plataforma de serviços gerenciados em nuvem

Materializa um estilo de serviços escaláveis em que a organização entrega ao provedor a operação da infraestrutura e fica com a lógica. A função é reduzir o trabalho de sustentação, trocando servidor administrado por serviço contratado, ao custo de aumentar a dependência do fornecedor. O processamento de dados roda em serviço gerenciado que executa o mesmo código em lote ou em fluxo contínuo. O dado estruturado vai para um armazém analítico que escala separadamente do processamento, e o não estruturado para armazenamento de objetos. A comunicação entre serviços passa por mensageria gerenciada, e o que precisa de controle fino de execução roda em contêineres orquestrados.

Entre as peças, o Apache Beam é o modelo de programação que permite escrever a transformação uma vez e executá-la em lote ou em fluxo, e o Dataflow é o serviço que a executa sem que alguém administre o agrupamento. O BigQuery separa armazenamento de processamento, o que permite consultar volume grande pagando pelo que foi lido. O Cloud Pub/Sub desacopla quem publica de quem consome. O Google Kubernetes Engine orquestra contêineres com escalonamento automático e suporte nativo ao Istio, que cuida de tráfego e segurança entre serviços. O Terraform descreve toda essa infraestrutura como código versionado, de modo que o ambiente possa ser recriado, e o Identity-Aware Proxy controla o acesso por identidade em vez de por endereço de rede.

#### Plataforma de microsserviços

Materializa o estilo de microsserviços. A função é permitir que times diferentes construam, implantem e escalem partes do sistema de forma independente, e toda a plataforma existe para tornar essa independência operacionalmente viável. O cliente entra por um único ponto, o gateway de API, que roteia para o serviço correto e concentra o que seria repetido em cada um, como terminação de HTTPS e limite de requisição. Dentro do agrupamento, cada serviço roda em contêiner próprio, com seu armazenamento, e se comunica com os demais por chamada direta quando precisa de resposta imediata ou por barramento de eventos quando não precisa. A observabilidade é obrigatória e não opcional, porque com o sistema dividido em muitos processos não existe mais um registro único onde olhar. A esteira de entrega faz parte da plataforma, não é acessório dela, porque implantação independente sem automação de implantação é promessa vazia.

Entre as peças, o Kubernetes é o orquestrador que decide em qual máquina cada contêiner roda, reinicia o que falha e escala o que satura. O Docker é o formato de empacotamento que torna o serviço idêntico em qualquer máquina. O NGINX Ingress é o gateway que traduz o endereço externo para o serviço interno. O Kafka é o barramento que guarda o evento publicado e permite que vários consumidores o leiam no próprio ritmo. O Prometheus coleta métricas, o Grafana as apresenta em painel e o OpenTelemetry padroniza a coleta de rastros que atravessam vários serviços, que é o único jeito de responder onde um pedido demorou.

![Plataforma de microsserviços. À esquerda, clientes web, móvel e usuários entram por HTTP e HTTPS num gateway de API com NGINX Ingress. No centro, um agrupamento Kubernetes com camada de serviço e três pods em contêineres Docker, um serviço de catálogo em Java, um de pedidos em .NET e um de pagamentos em Node.js, apoiados por Redis, PostgreSQL e um barramento Kafka. À direita, observabilidade com Prometheus para métricas, Grafana para painéis e OpenTelemetry para rastros. Na base, a esteira de integração e entrega, do código ao GitHub Actions, ao registro de contêineres e à implantação no Kubernetes.](../assets/images/plataforma-microsservicos.png)

*Plataforma de microsserviços. Os três serviços usam linguagens diferentes, o que o estilo permite e a plataforma precisa sustentar, e a esteira na base mostra que a implantação independente é parte da plataforma. Fonte: material base do professor.*

Na variante Java dessa pilha, o Spring Boot é o framework base de cada serviço, o Spring Cloud Config centraliza a configuração fora do código, o Eureka permite que um serviço descubra o endereço do outro sem endereço fixo, o Spring Cloud Gateway faz o papel do gateway de API, o Keycloak cuida de autenticação e autorização, o Elastic Stack concentra os registros de todos os serviços em um lugar só, e o WireMock simula as APIs externas durante o teste.

#### Plataforma orientada a eventos

Materializa o estilo orientado a eventos. A função é desacoplar quem produz de quem consome no tempo, de modo que o produtor não espere resposta e o consumidor processe no seu próprio ritmo, o que é justamente o que permite absorver pico. O produtor publica um evento num fluxo, e o fluxo o retém por um período configurado. A partir dele, consumidores independentes fazem coisas diferentes com o mesmo evento, um grava em armazenamento bruto para análise posterior, outro dispara uma função que atualiza um banco de resposta rápida, outro alimenta uma aplicação de processamento contínuo. Acrescentar um quarto consumidor depois não exige mudar o produtor, e essa propriedade é o principal ganho do estilo.

Entre as peças, o fluxo de eventos é o centro da plataforma, e o que o distingue de uma fila tradicional é a retenção, porque a fila entrega e descarta, enquanto o fluxo guarda e permite releitura. O processamento contínuo sobre o fluxo é o que transforma evento em agregação sem passar por banco intermediário. O armazenamento de eventos guarda a sequência completa como fonte da verdade, de modo que o estado atual possa ser recalculado. Um mediador de integração cuida de rotas e conversões entre formatos quando as pontas não falam a mesma língua, e um gateway de API publica para fora o que é consumido por terceiros.

![Arquitetura de streaming sobre serviços da AWS, com fluxo de dados em tempo real chegando ao Amazon Kinesis, que despacha para bucket S3, para funções Lambda com persistência em DynamoDB, e para aplicações Kinesis executando em instâncias EC2.](../assets/images/plataforma-streaming-aws.png)

*Plataforma orientada a eventos sobre serviços da AWS. Um mesmo fluxo alimenta três destinos diferentes ao mesmo tempo, que é a propriedade que o estilo busca. Fonte: material base do professor.*

Na pilha aberta equivalente, o Apache Kafka é o fluxo, o Kafka Streams o processamento contínuo, o Event Store o armazenamento de eventos, o Apache Camel o mediador de integração, o Kong API Gateway a publicação externa e o Confluent Control Center o monitoramento do fluxo.

#### Plataforma serverless orientada a eventos

Materializa o mesmo estilo orientado a eventos, com uma diferença de custo e de operação. Aqui não há servidor administrado nem contêiner em execução contínua. A função só existe enquanto processa, e o provedor a instancia quando um evento chega e a descarta quando termina, o que faz o custo acompanhar o uso em vez do tempo. A contrapartida é que a função precisa ser curta, sem estado guardado entre invocações, e que a primeira execução depois de um período ocioso é mais lenta.

Entre as peças, a função sob demanda é a unidade de execução. A fila desacopla e garante que o evento não se perca se a função falhar. O orquestrador de fluxos coordena várias funções em sequência com estado e repetição, porque a função isolada não sabe o que veio antes. O gateway de API transforma a função em endereço HTTP público. O armazenamento de objetos aqui é também produtor de eventos, já que criar ou modificar um arquivo dispara processamento. A observabilidade depende de rastreamento distribuído, porque uma requisição pode atravessar muitas funções curtas, e o ambiente de simulação local é o que torna esse tipo de plataforma testável sem custo de nuvem.

#### Plataforma de data lake

Materializa o estilo de pipelines de processamento de dados. A função é receber dado de muitas origens, com formatos e ritmos diferentes, e levá-lo por refinamentos sucessivos até ficar consumível por quem decide. O dado entra por três caminhos, fluxo contínuo para o que é gerado o tempo todo, chamada de API para o que vem de sistema de terceiro, e lote para o que chega em arquivo. Depois de ingerido, ele atravessa três zonas de armazenamento. A zona bruta guarda o dado como chegou, sem transformação, o que permite reprocessar tudo se a regra mudar. A zona curada guarda o dado limpo, com esquema conhecido e duplicidade resolvida. A zona analítica guarda o dado já agregado no formato que a pergunta de negócio espera. O processamento é que move o dado de uma zona para a seguinte, e a governança vale sobre as três ao mesmo tempo.

Entre as peças, o armazenamento de objetos é a base, porque é barato por volume e separa o custo de guardar do custo de processar. O Spark é o motor de processamento distribuído que executa a transformação pesada. O dbt organiza a transformação da zona curada para a analítica como código versionado e testado, em vez de consulta solta. O catálogo de dados é o que permite alguém descobrir qual conjunto existe e o que cada coluna significa, sem o qual o data lake vira depósito. A qualidade de dados aplica regras de validação na entrada, e o controle de acesso governa quem lê o quê, que é o que separa um data lake de uma pasta compartilhada grande.

![Plataforma de data lake. À esquerda, fontes de dados de ERP, CRM, IoT, SaaS, arquivos e fluxos de eventos. Em seguida, ingestão por Kafka ou Kinesis, por API e em lote. No centro, armazenamento de objetos dividido em três zonas, bruta, curada e analítica. Acima, governança com catálogo de dados, qualidade de dados e controle de acesso. Abaixo, processamento com Spark, ETL e ELT e dbt. À direita, consumidores, análise SQL com Athena ou Trino, painéis em Power BI, aprendizado de máquina com SageMaker e aplicações.](../assets/images/plataforma-data-lake.png)

*Plataforma de data lake. As três zonas são a restrição estrutural do estilo, e a faixa de governança no topo é o que distingue um data lake de um depósito de arquivos. Fonte: material base do professor.*

Numa pilha aberta e menor, o Apache NiFi orquestra os fluxos de ingestão com interface gráfica e controle de prioridade, o Apache Beam descreve a transformação de forma independente do motor que a executa, o Great Expectations declara as expectativas de qualidade como teste do dado, e o NiFi Registry versiona a definição dos próprios fluxos, o que os torna auditáveis.

#### Plataforma de internet das coisas

Materializa um estilo de coleta distribuída com processamento central. A função é receber dado de muitos dispositivos pequenos, com conectividade instável e pouca capacidade, e entregá-lo a uma aplicação que os comanda de volta. Os dispositivos não falam HTTP com o servidor. Eles publicam em um protocolo leve de publicação e assinatura, desenhado para rede ruim e mensagem curta, sobre um canal cifrado, e cada dispositivo se autentica por certificado próprio, e não por senha compartilhada. Um serviço de nuvem faz a ponte entre esse mundo e a aplicação, que roda com a mesma elasticidade e redundância entre zonas das plataformas web. O usuário comanda pelo celular, e o comando percorre o caminho inverso até o dispositivo.

A peça que define essa plataforma é o protocolo MQTT, que troca mensagens por tópico, permite que um dispositivo publique sem saber quem vai ler e sobrevive a queda de conexão. O certificado por dispositivo é o que torna possível revogar o acesso de um aparelho comprometido sem afetar os demais, e é a decisão de segurança mais importante desse tipo de plataforma.

![Plataforma de automação residencial, com dispositivos conectados em cômodos da casa falando MQTT sobre SSL com o Amazon IoT, e aplicação em instâncias EC2 distribuídas em duas zonas de disponibilidade atrás de balanceador elástico, acessada por telefone celular via Route 53.](../assets/images/plataforma-iot-residencial.png)

*Plataforma de automação residencial. O cadeado e o selo sobre a linha de MQTT são a cifragem e o certificado por dispositivo, que é o ponto de controle de segurança dessa plataforma. Fonte: material base do professor.*

#### Plataformas de camada de interface

As duas pilhas abaixo não materializam um estilo de sistema inteiro, elas organizam a camada de interface de um sistema cujo estilo já foi decidido em outro lugar. A função de ambas é a mesma, manter a tela sincronizada com o dado sem que o desenvolvedor escreva o código dessa sincronia a cada campo, e resolver de forma padronizada os problemas recorrentes de interface, navegação entre telas, validação de formulário, chamada ao servidor, tradução e teste.

Na pilha móvel com React Native, o Zustand guarda o estado compartilhado entre telas em um lugar só, o React Navigation controla a pilha de telas e o botão de voltar, o Zod declara o formato esperado do dado e valida a entrada contra ele, o TanStack Query cuida do dado que vem do servidor, incluindo cache, nova tentativa e invalidação, e o MMKV guarda dado local com leitura rápida. Na pilha web de página única com Vue.js, o Pinia faz o papel do repositório de estado, o Vue Router a navegação, o Vuetify entrega componentes visuais prontos, o Axios faz a chamada HTTP e o Vite empacota o código para o navegador.

A pilha móvel segue o *Model-View-ViewModel*, e aqui cabe uma ressalva de vocabulário. Boa parte da literatura, e o próprio material base desta disciplina, lista MVC e MVVM entre os estilos arquiteturais. Esta disciplina os trata como padrão de organização da camada de interface, e não como estilo, porque a definição adotada no [bloco 2 da Aula 3](../modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md) exige que o estilo descreva a forma estrutural do sistema inteiro, não a organização interna de uma camada. É escolha de recorte desta disciplina, não erro da literatura, e vale conhecer as duas leituras porque você vai encontrar ambas em texto profissional.

## Uso pelo arquiteto

Assim como o estilo arquitetural é a maior decisão que um arquiteto toma em um projeto, a plataforma arquitetural é a maior decisão tecnológica do projeto. Por consequência, ela precisa ser justificada e registrada em um ADR próprio, escrito no [bloco 4](bloco-4-adr-de-plataforma.md) desta aula.

O arquiteto documenta a comparação antes de decidir, em um **quadro comparativo** que lista as plataformas candidatas nas linhas e os sete fatores de adaptação ao contexto nas colunas, com uma nota curta em cada célula. Esse quadro entra no ADR de plataforma como evidência de que a escolha considerou alternativas reais, não apenas a plataforma mais familiar ao time, o que faz a decisão resistir a questionamento meses depois.

## Exercício 18

A ACME é a universidade privada brasileira em modernização incremental do sistema acadêmico, cujo núcleo transacional em COBOL sobre o monitor CICS segue em operação durante toda a transição, com uma camada web em JSF e EJB e integrações com o ERP financeiro e o ambiente virtual de aprendizagem resolvidas por arquivo, em lote noturno.

Considerando o estilo arquitetural que você escolheu no exercício do [bloco 2 da Aula 3](../modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md), levante duas plataformas candidatas capazes de concretizar esse estilo, considerando que o núcleo COBOL sobre CICS permanece em operação durante a transição.

1. Nomeie as duas plataformas candidatas, com as ferramentas concretas de cada uma, no nível de detalhe dos exemplos de plataforma por estilo apresentados no Conceito.
2. Monte o quadro comparativo das duas, usando pelo menos quatro dos sete fatores de adaptação ao contexto listados no Conceito.
3. Escolha uma das duas e justifique a escolha considerando a restrição de convivência com o legado.

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Mendes, M. (2026b). *Guias de projeto de arquitetura de software* [Material de curso, versão arquivada]. https://github.com/aulas-marco/projeto-arquitetura-software/tree/30f15cd (guia 2.2, fonte da definição, das quatro características, dos sete fatores de adaptação ao contexto, dos oito exemplos de plataforma por estilo e das representações visuais reproduzidas nesta página)
- Ford, N., & Richards, M. (2020). *Fundamentals of software architecture*. O'Reilly. (comparação por atributo de qualidade, aplicada aqui a plataformas)

**Material do curso.** Glossário, entradas [plataforma arquitetural](../referencia/glossario.md#plataforma-arquitetural) e [racional arquitetural](../referencia/glossario.md#racional-arquitetural). Dossiê da instituição fictícia [ACME](../caso-acme/index.md) e [arquitetura de linha de base](../caso-acme/linha-de-base.md).
