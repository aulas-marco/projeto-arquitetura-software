# Arquitetura de aplicações e integração

Quando a nota lançada por um professor precisa chegar ao ambiente virtual, alguém precisa definir por onde ela passa e o que cada lado promete ao outro. Esse é o trabalho do domínio de aplicações e integração, o terceiro da Aula 4. Uma aplicação é um programa que oferece funções ao negócio. Uma interface é o ponto pelo qual uma aplicação oferece suas funções a outra. O bloco identifica as aplicações e interfaces que realizam a mudança, distingue padrão técnico, protocolo, especificação e contrato, e representa a fronteira da solução no diagrama de contexto C4.

## Antes de começar

- [Arquitetura de aplicações](../referencia/glossario.md#arquitetura-de-aplicacoes)
- [Padrão técnico](../referencia/glossario.md#padrao-tecnico)
- [Contrato de integração](../referencia/glossario.md#contrato-de-integracao)
- [Modelo C4](../referencia/glossario.md#modelo-c4)
- Dono de cada entidade, a aplicação autorizada a gravá-la, marcado no [exercício 14](bloco-2-arquitetura-de-dados.md#exercicio-14)

## Aplicações, interfaces e contexto

<figure markdown="span">
![Mapa do bloco 0 com quatro faixas empilhadas, negócio, dados, aplicações e infraestrutura, e o que o arquiteto decide em cada uma, com a faixa de aplicações em destaque e as demais esmaecidas.](../assets/images/modulo-4-b0-mapa-aplicacoes.svg){ .module-diagram }
</figure>

No mapa do [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md), este bloco trata do domínio de aplicações. O arquiteto recebe a grade dado × aplicação, produzida no [bloco 2](bloco-2-arquitetura-de-dados.md), e o portfólio de aplicações. Ele decide que aplicações mudam, por quais interfaces e contratos elas trocam dados e onde passa a fronteira da solução. Ao bloco 4, entrega os diagramas de contexto e de contêineres, além dos contratos de integração.

Para dizer por onde a nota passa, o arquiteto parte da arquitetura de aplicações, que é o subdomínio da arquitetura corporativa que mantém a visão do portfólio de aplicações da organização e dos serviços que elas oferecem, e que liga a arquitetura de negócio à arquitetura de dados. Aplicação é um conjunto de capacidades tecnológicas que fornece funções de negócio e gerencia ativos de dados, e componente de aplicação é a unidade que encapsula uma funcionalidade e a oferece por interfaces claramente definidas. As aplicações são o principal meio de gerir o dado ao longo do seu ciclo de vida, da aquisição ao processamento, ao armazenamento, à apresentação, ao arquivamento e à exclusão.

O bloco apresenta primeiro os conceitos de aplicação e de integração, cada um ilustrado em notação livre, sem convenção formal, e reúne no fim o modelo C4, a notação que a aula adota para representar a fronteira e a decomposição da solução em diagramas de níveis de detalhe progressivos.

### Aplicações e interfaces

Quando o professor lança uma nota, o Portal do Professor a entrega ao núcleo transacional por uma interface, que é o ponto pelo qual um componente de aplicação oferece sua funcionalidade a outro componente, a uma pessoa ou a um sistema externo, e a integração é a troca de dados e de chamadas que ocorre por essas interfaces. Cada aplicação expõe as entidades de que é dona, no sentido de [propriedade do dado](bloco-2-arquitetura-de-dados.md#propriedade-do-dado) apresentado no bloco 2, e consome por interface as entidades que pertencem a outras aplicações.

O diagrama abaixo acompanha a nota da Universidade ACME. O professor faz o lançamento, o serviço de notas o registra pelo núcleo e publica a mensagem que atualiza o ambiente virtual. Cada seta exige uma interface com dados, condições e tratamento de erro definidos.

```mermaid
flowchart TB
    PRO["Portal do Professor"]
    SN["Serviço de notas"]
    NUC["Núcleo acadêmico COBOL"]
    AVA["Ambiente virtual"]
    PRO -->|"lança a nota"| SN
    SN -->|"registra pela transação existente"| NUC
    SN -->|"publica o evento de nota"| AVA
    AVA -->|"confirma o recebimento"| SN
```

### Portfólio de aplicações

Antes de mexer em qualquer aplicação, o arquiteto precisa saber o que a organização já tem, e o artefato principal do domínio para isso é o catálogo do portfólio de aplicações, que lista as aplicações em uso e planejadas, com quem as usa e como. O portfólio costuma ser um conjunto heterogêneo, adquirido ou construído em momentos diferentes da história da organização, e por isso a arquitetura de aplicações trabalha continuamente para racionalizá-lo. Para distinguir aplicações estratégicas de aplicações legadas, é frequente o uso de uma classificação em vermelho, âmbar e verde, que permite à arquitetura de solução escolher a opção mais estratégica. Nesta disciplina, verde indica aplicação estratégica a manter e evoluir, âmbar indica aplicação mantida por ora, com restrição de investimento, e vermelho indica aplicação a substituir ou a retirar.

A Figura 1 aplica a classificação ao portfólio da Universidade ACME. O ERP financeiro e o ambiente virtual permanecem, conforme a decisão de escopo. O núcleo COBOL continua durante a transição, sob contrato. Os portais legados e os acessos diretos ao banco exigem migração. A cor orienta o investimento, enquanto o roteiro define quando cada mudança pode ocorrer.

<figure markdown="span">
![Portfólio acadêmico: ERP e ambiente virtual permanecem, núcleo COBOL exige acompanhamento durante a transição e portais legados e acessos diretos ao banco exigem migração.](../assets/images/modulo-4-b3-portfolio-hospital.svg){ .module-diagram }
</figure>

*Figura 1 — Portfólio de aplicações classificado em vermelho, âmbar e verde, com a ação associada a cada cor. Fonte: material do curso, com base em Lovatt (2021, seção 2.6.1).*

Para ler o catálogo, ajuda separar as aplicações em três tipos, ilustrados na tabela abaixo com exemplos da Universidade ACME.

| Tipo | Definição | Exemplo na Universidade ACME |
| --- | --- | --- |
| Aplicação de negócio | Ligada diretamente à atividade do negócio, própria da organização ou adquirida, inclusive como serviço | Sistema acadêmico e ambiente virtual de aprendizagem |
| Aplicação genérica | Ferramenta usada para vários fins | Planilha para priorização eventual e correio eletrônico entre departamentos |
| Plataforma de aplicação | Conjunto de componentes tecnológicos que sustenta outras aplicações, em geral tratado no domínio de infraestrutura | Sistema gerenciador de banco de dados e barramento de serviços |

### Descrição de uma interface

Para que uma troca como a da nota não dependa da memória de quem a programou, a organização mantém o catálogo de interfaces de aplicações, que documenta as interfaces entre aplicações, o tipo e o nível de dependência entre elas e suas interfaces de programação, e as grades de referência cruzada relacionam aplicações a dados, a funções de negócio e a processos. O catálogo de interfaces é a fonte principal da análise de interfaces da solução. A arquitetura de software, por sua vez, responde pela estrutura e pelo comportamento de cada componente, inclusive suas interfaces internas e externas, e documenta como interfaces de programação o comportamento que outros sistemas consomem.

Cada ponto de contato entre blocos de construção da solução é descrito por seis atributos, e o conjunto dessas descrições forma o catálogo de interfaces da solução.

| Atributo | O que registra |
| --- | --- |
| Origem | O bloco de construção que inicia a troca |
| Destino | O bloco de construção que recebe a troca |
| Gatilho | O evento ou a condição que dispara a troca |
| Itens trocados | Os dados e as informações de apoio que passam pela interface |
| Sequência | A ordem das mensagens e das respostas |
| Pré e pós-condições | O que precisa valer antes da troca e o que passa a valer depois dela |

O diagrama acompanha uma interface da Universidade ACME e indica onde registrar os seis atributos. O serviço de notas é a origem, o ambiente virtual é o destino e a publicação de uma nota validada dispara a troca.

```mermaid
sequenceDiagram
    participant SN as Serviço de notas
    participant AV as Ambiente virtual
    Note over SN,AV: Pré-condição: nota validada e aluno identificado
    Note over SN: Gatilho: nota publicada
    SN->>AV: 1. enviar evento de nota
    Note over SN,AV: Dados: identificador do evento, aluno, disciplina, nota e versão
    AV-->>SN: 2. confirmar recebimento
    Note over SN,AV: Pós-condição: entrega registrada e nota disponível em até 10 minutos
```

### Padrão técnico, protocolo, especificação e contrato

Em português, a palavra padrão traduz dois termos ingleses distintos, e a distinção entre eles importa neste bloco. O termo *pattern*, no sentido usado na Aula 3, designa uma solução recorrente para um problema em um contexto, enquanto o termo *standard* designa uma especificação adotada por uma organização ou por um organismo de normalização. Este bloco usa a expressão padrão técnico para *standard* e reserva padrão arquitetural e padrão de design para *pattern*, conforme as entradas do [glossário](../referencia/glossario.md#padrao-tecnico).

Um **padrão técnico** reúne a experiência de profissionais ao longo de muitos anos e situações, e a apresenta como especificação de processos a seguir, documentação a produzir e regras e parâmetros a observar. Por ser genérico, um padrão técnico costuma conter partes que não se aplicam a uma solução específica, e por isso o arquiteto precisa recortar a parte que se aplica antes de transformá-la em requisito técnico.

Quando um portal da ACME confirma quem está entrando, ele conversa com o diretório corporativo segundo regras combinadas de antemão, e esse conjunto de regras, com formato, sequência e tratamento de erro definidos, é um protocolo. Entre os protocolos da linha de base da ACME estão três. O primeiro é o LDAP, protocolo para consultar o diretório corporativo, que é o cadastro central de usuários da instituição, e é por ele que os portais confirmam quem está entrando. O segundo é o HTTPS, a versão protegida do HTTP, usado nas chamadas ao gateway de pagamento, serviço externo que gera boleto e cobra em cartão, e ao assinador digital, serviço externo que assina o histórico e o diploma. O terceiro é um conector transacional proprietário entre os portais e o núcleo, o sistema central da ACME, escrito em COBOL. Esse conector é um componente de um fornecedor específico, que permite aos portais em Java acionar as transações do núcleo, e o formato das mensagens que ele troca pertence ao fornecedor, não a um padrão aberto. O HTTP, base do HTTPS, tem sua semântica definida pelo RFC 9110 (Fielding et al., 2022).

Dois sistemas que usam o mesmo protocolo ainda precisam combinar que mensagens trocam, e é isso que uma especificação de interface descreve de forma verificável para uma interface particular, com operações ou mensagens, esquemas e erros. Para interfaces síncronas sobre HTTP, a especificação OpenAPI define uma descrição independente de linguagem de programação, que permite a pessoas e a programas entender as capacidades de um serviço sem acesso ao código-fonte (OpenAPI Initiative, 2026). Para interfaces orientadas a mensagens, a especificação AsyncAPI descreve canais, mensagens e operações de forma independente do protocolo de transporte (AsyncAPI Initiative, n.d.). Os dois trechos abaixo descrevem, num exemplo genérico de comércio eletrônico, uma consulta síncrona de pedido e a publicação de um evento de pedido confirmado.

```yaml
openapi: 3.2.1
info:
  title: Pedidos
  version: 1.0.0
paths:
  /pedidos/{id}:
    get:
      summary: Consulta um pedido
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        "200":
          description: Pedido encontrado
        "404":
          description: Pedido inexistente
```

```yaml
asyncapi: 3.1.0
info:
  title: Eventos de pedido
  version: 1.0.0
channels:
  pedidoConfirmado:
    address: pedidos.confirmados
    messages:
      pedidoConfirmado:
        payload:
          type: object
          properties:
            idPedido:
              type: string
            versao:
              type: integer
operations:
  publicarPedidoConfirmado:
    action: send
    channel:
      $ref: "#/channels/pedidoConfirmado"
```

A especificação depende de uma linguagem de esquema, que define a estrutura e as restrições de cada mensagem de forma que um programa consiga validá-la antes de processá-la. O JSON Schema é uma linguagem declarativa para definir a estrutura e as restrições de dados JSON, serve de base ao OpenAPI e ao AsyncAPI na descrição do corpo das mensagens e tem como versão corrente a 2020-12 (JSON Schema, n.d.). O Apache Avro é um sistema de serialização com esquemas escritos em JSON, em que o dado armazenado junto do seu esquema se torna autodescritivo (Apache Software Foundation, n.d.). Em fluxos de eventos, os esquemas Avro costumam ficar num registro de esquemas, como o Schema Registry da Confluent, que guarda as versões de cada esquema e verifica a compatibilidade da versão nova com as anteriores antes de aceitá-la (Confluent, n.d.). Os Protocol Buffers são um mecanismo neutro quanto a linguagem e plataforma para serializar dados estruturados, descritos em arquivos .proto a partir dos quais se gera código em cada linguagem, e são o formato usado por padrão no gRPC (Google, n.d.).

Falta ainda o que cada parte promete à outra, e é isso que o **contrato de integração** acrescenta, por ser a especificação de interface somada às garantias que provedor e consumidor acordam, como a política de versão, a garantia de entrega, a idempotência e o nível de serviço. Os seis campos que o contrato acrescenta aos seis atributos de interface aparecem na seção [Estrutura de um contrato](#estrutura-de-um-contrato), logo abaixo do exemplo da nota fiscal eletrônica.

Um exemplo em que os quatro níveis aparecem separados é a nota fiscal eletrônica brasileira. O padrão técnico é o próprio sistema da nota fiscal eletrônica, cujo manual de orientação do contribuinte, na versão 7.00 de novembro de 2020, fixa regras e leiautes para todas as empresas emissoras e adota o perfil de interoperabilidade WS-I Basic Profile para os serviços web. Os protocolos são o TLS 1.2 ou superior com autenticação mútua e o SOAP 1.2. A especificação é dada pelos esquemas XML das mensagens, como o esquema de envio da nota na versão 4.00, publicados no portal nacional. O nível de contrato corresponde às regras que cada serviço impõe ao emissor, como o uso obrigatório de certificado digital emitido por autoridade credenciada na ICP-Brasil, do tipo A1 ou A3, as regras de validação e os códigos de retorno, que nesse caso são fixadas pela administração tributária sem negociação com cada emissor.

<figure markdown="span">
![Quatro camadas empilhadas da integração com a nota fiscal eletrônica. Na base, o padrão técnico, sistema NF-e com o manual de orientação do contribuinte 7.00 e o perfil WS-I Basic Profile. Acima, os protocolos TLS 1.2 ou superior com autenticação mútua e SOAP 1.2. Acima, a especificação por esquemas XSD, como o de envio da nota na versão 4.00. No topo, as regras impostas pelo serviço, como o certificado ICP-Brasil A1 ou A3.](../assets/images/modulo-4-b3-camadas-nfe.svg){ .module-diagram }
</figure>

*Figura 2 — Padrão técnico, protocolo, especificação e contrato na nota fiscal eletrônica. Fonte: material do curso, com base no manual de orientação do contribuinte, versão 7.00 (2020).*

### Estrutura de um contrato

Além do caminho de sucesso, um contrato precisa dizer como a integração confirma, falha e se recupera. A sequência resume essas situações e aponta o que deve ficar explícito no contrato.

```mermaid
sequenceDiagram
    participant P as Aplicação provedora
    participant C as Aplicação consumidora
    P->>C: Envio conforme operação e esquema
    C-->>P: Confirmação com resultado
    alt falha temporária
        C-->>P: Erro e código de retorno
        P->>C: Nova tentativa conforme política
    else informação inválida
        C-->>P: Rejeição com motivo
        P->>P: Corrigir e registrar tratamento
    end
```

O contrato de integração usado nesta disciplina parte dos seis atributos de interface e acrescenta seis campos, que respondem ao que a especificação sozinha deixa em aberto.

| Campo | Pergunta que responde |
| --- | --- |
| Origem, Destino, Gatilho, Itens trocados, Sequência, Pré e pós-condições | Os seis atributos de interface apresentados acima |
| Protocolo | Por quais regras de troca as mensagens trafegam? |
| Formato e esquema | Como cada mensagem é estruturada e validada? |
| Semântica de erro | Que erros podem ocorrer e o que cada parte faz diante de cada um? |
| Versionamento | Como uma mudança é publicada sem quebrar o consumidor existente? |
| Garantia de entrega e idempotência | A mensagem pode se perder ou se repetir, e o que o consumidor faz com a repetição? |
| Nível de serviço | Que prazo, volume e disponibilidade o provedor garante? |

A escolha entre comunicação síncrona e assíncrona decide boa parte desses campos. Na comunicação síncrona, o consumidor espera a resposta, e a indisponibilidade do provedor chega ao consumidor, o que pede os padrões [Timeout](../modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md#timeout), [Retry com limite](../modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md#retry-com-limite) e [Circuit Breaker](../modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md#circuit-breaker). Na comunicação assíncrona, o provedor publica e o consumidor processa depois, o que desacopla a disponibilidade das duas partes, mas exige garantia de publicação, por exemplo com o padrão [Transactional Outbox](../modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md#transactional-outbox), e consumidor idempotente, condição que o mesmo padrão impõe. Todos esses padrões foram apresentados no [bloco 3 da Aula 3](../modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md).

O primeiro diagrama, em notação livre, mostra a comunicação síncrona protegida pelos três mecanismos, com tempo limite de 2 segundos por chamada e no máximo duas retentativas antes de o Circuit Breaker abrir o circuito. Os valores numéricos são ilustrativos, porque cada contrato fixa os seus a partir do nível de serviço declarado pelo provedor.

```mermaid
sequenceDiagram
    participant C as Consumidor
    participant CB as Circuit Breaker
    participant P as Provedor
    C->>CB: requisição
    CB->>P: chamada com tempo limite de 2 s
    P--xCB: sem resposta no prazo
    CB->>P: retentativa 1 de 2, após espera
    P--xCB: sem resposta no prazo
    CB->>P: retentativa 2 de 2, após espera maior
    P--xCB: sem resposta no prazo
    Note over CB: limite de falhas atingido, circuito aberto
    CB-->>C: erro devolvido ao consumidor
    C->>CB: nova requisição
    CB-->>C: falha imediata, sem chamar o provedor
    Note over CB,P: após o intervalo, o circuito meio aberto libera uma chamada de teste
```

O segundo diagrama, também em notação livre, mostra a comunicação assíncrona com Transactional Outbox, em que o serviço grava o dado de negócio e o evento a publicar na mesma transação do banco, e um retransmissor publica o evento na fila em seguida. O consumidor guarda o identificador de cada evento processado e descarta a reentrega com identificador repetido, o que torna segura a entrega pelo menos uma vez, em que a fila pode reentregar o mesmo evento após uma falha de confirmação.

```mermaid
sequenceDiagram
    participant S as Serviço de origem
    participant DB as Banco do serviço
    participant R as Retransmissor da outbox
    participant F as Fila
    participant K as Consumidor
    S->>DB: grava pedido e registro na outbox na mesma transação
    R->>DB: lê registros pendentes da outbox
    R->>F: publica evento com id único
    R->>DB: marca registro como publicado
    F->>K: entrega evento
    K->>K: consulta ids já processados
    Note over K: id novo, processa e grava o id
    F->>K: reentrega o mesmo evento
    Note over K: id repetido, descarta sem novo efeito
```

### Estilos de integração

Escolher como duas aplicações conversam é escolher um estilo de integração, que combina um modo de comunicação com um protocolo e um formato de mensagem. O estilo de integração descreve uma troca entre duas partes e se distingue do [estilo arquitetural](../modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md), apresentado no bloco 2 da Aula 3, que organiza a solução inteira. A Figura 3 posiciona os estilos mais usados por modo e por grau de acoplamento entre emissor e receptor. Entre os síncronos, o REST opera sobre recursos com os métodos e os códigos de estado do HTTP, em geral com corpo em JSON, e o gRPC é um framework de chamada remota de procedimento que usa Protocol Buffers como linguagem de definição de interface e como formato das mensagens, transportadas sobre HTTP/2 (gRPC Authors, n.d.-a, n.d.-b). O GraphQL é uma linguagem de consulta para APIs apoiada num sistema de tipos, em que o cliente pede exatamente os campos de que precisa numa única consulta (GraphQL Foundation, n.d.).

Entre os assíncronos, o webhook é uma chamada HTTP que o provedor faz a um endereço registrado pelo consumidor quando um evento ocorre, e a mensageria entrega mensagens por filas num intermediário como o RabbitMQ, que implementa os protocolos AMQP 0-9-1 e AMQP 1.0 (RabbitMQ, n.d.). O streaming de eventos grava os eventos num registro ordenado e retido, como os tópicos do Apache Kafka, base da [arquitetura orientada a eventos](../modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md#arquitetura-orientada-a-eventos) vista na Aula 3, que um consumidor novo pode ler desde o início dentro do prazo de retenção, e a transferência de arquivo move lotes periódicos por SFTP. A posição horizontal na figura é aproximada e considera quanto o receptor precisa estar disponível no momento da troca e quanto ele conhece do emissor.

<figure markdown="span">
![Mapa com sete estilos de integração em duas faixas. Na faixa síncrona, gRPC com HTTP/2 e Protocol Buffers, REST sobre HTTP com JSON e GraphQL. Na faixa assíncrona, webhooks, mensageria AMQP com RabbitMQ, streaming de eventos com Apache Kafka e transferência de arquivo por SFTP em lote. O eixo horizontal vai do maior ao menor acoplamento, e cada cartão traz o caso de uso típico do estilo.](../assets/images/modulo-4-b3-estilos-integracao.svg){ .module-diagram }
</figure>

*Figura 3 — Estilos de integração por modo de comunicação e grau de acoplamento, com o caso de uso típico de cada um. Fonte: material do curso, com base na documentação de gRPC, GraphQL e RabbitMQ.*

Em APIs HTTP, a idempotência de métodos como POST e PATCH, condição que o padrão [Retry com limite](../modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md#retry-com-limite) da Aula 3 exige para repetir uma chamada com segurança, pode ser obtida com o cabeçalho Idempotency-Key, pelo qual o cliente envia um identificador único, recomendado no formato UUID, e o servidor reconhece a repetição de uma requisição já recebida sem repetir o efeito. O rascunho da IETF que define o cabeçalho prevê a resposta 409 quando a repetição chega enquanto a primeira requisição ainda é processada, e a resposta 422 quando a mesma chave chega com conteúdo diferente (Jena & Dalal, 2025). A revisão 07 do rascunho, de outubro de 2025, expirou em abril de 2026 sem publicação como RFC, e por isso o contrato que adotar o cabeçalho precisa declarar por escrito a semântica esperada, já que nenhuma norma vigente a fixa.

O gateway de API corresponde ao padrão [API Gateway](../modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md#api-gateway), apresentado no bloco 3 da Aula 3, e é o componente que recebe as chamadas dos consumidores antes do provedor e aplica num ponto único as regras do contrato que não pertencem à lógica do serviço, como a autenticação do consumidor, o limite de taxa de requisições e o roteamento entre versões publicadas da interface. Kong, AWS API Gateway e Azure API Management são exemplos de produto dessa categoria, e a escolha de produto, de estilo de integração e de linguagem de esquema para a ACME pertence à Aula 5, junto com a plataforma arquitetural.

### Hierarquia de serviços

A hierarquia de serviços apresentada no [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md#a-ordem-dos-dominios) organiza as relações entre os domínios em camadas, em que cada camada depende apenas da imediatamente inferior. O serviço de negócio é a interface com o cliente e é realizado por processos de negócio. O processo é apoiado por serviços de aplicação, o serviço de aplicação é realizado por componentes de aplicação, e o componente de aplicação depende de serviços de tecnologia, como armazenamento, rede e processamento. Pessoas e informação atravessam todas as camadas. A hierarquia completa a afirmação do [bloco 1](bloco-1-arquitetura-de-negocio.md), de que todo componente da solução sustenta um ou mais serviços de negócio.

A Figura 4 reúne a hierarquia de serviços, à esquerda, e as quatro camadas que governam uma integração, apresentadas acima, à direita.

<figure markdown="span">
![Diagrama em duas partes. À esquerda, uma pilha de cinco camadas, serviço de negócio, processo de negócio, serviço de aplicação, componente de aplicação e serviço de tecnologia, com cada camada dependendo da inferior. À direita, quatro camadas empilhadas da base ao topo, padrão técnico, protocolo, especificação e contrato, com os seis atributos de interface listados junto à especificação e as garantias acordadas junto ao contrato.](../assets/images/modulo-4-servicos-e-contrato.svg){ .module-diagram }
</figure>

*Figura 4 — Hierarquia de serviços e camadas do contrato de integração. Fonte: material do curso, com base em Lovatt (2021, seções 2.6 e 3.6.4).*

### Modelo C4

Os diagramas anteriores deste bloco usam notação livre, escolhida para ilustrar cada conceito, e a partir daqui a aula passa a uma notação com convenção declarada. O [modelo C4](../referencia/glossario.md#modelo-c4) é a notação de modelagem adotada nesta aula para representar a solução em qualquer nível de detalhe e em qualquer domínio, e os diagramas de contexto, de contêineres e de implantação desta seção em diante seguem a convenção do C4, que o [bloco 4](bloco-4-arquitetura-de-infraestrutura.md) usa também no diagrama de contêineres da arquitetura alvo e no diagrama de implantação.

O diagrama solto e o modelo arquitetural diferem pela convenção. O diagrama solto nasce de uma conversa, usa símbolos escolhidos na hora e serve àquela conversa. O modelo tem convenção declarada, define o que cada forma significa e o que cada nível de detalhe pode ou não conter, e por isso continua legível para quem não participou da conversa. A diferença prática aparece quando duas pessoas desenham o mesmo sistema, porque a convenção declarada permite comparar os dois desenhos forma a forma. No C4, essa convenção fixa quatro níveis de abstração e quatro tipos principais de elemento, pessoa, sistema de software, contêiner e componente.

O **modelo C4**, criado por Brown (n.d.), é uma dessas convenções. Ele organiza a descrição do sistema em quatro níveis de abstração, que permitem compreensão progressiva de acordo com o público e o propósito da documentação. O nome vem das iniciais dos quatro níveis em inglês, Context, Containers, Components e Code, e cada nível tem nome próprio, de modo que o quarto nível se chama Código.

<figure markdown="span">
![Quatro faixas empilhadas e recuadas mostram a decomposição do modelo C4. O nível 1, contexto, mostra o sistema de software com pessoas e sistemas externos. O nível 2, contêineres, decompõe o sistema em aplicações, serviços e bancos de dados. O nível 3, componentes, decompõe um contêiner. O nível 4, código, decompõe um componente em classes e funções. Os níveis 1 e 2 aparecem destacados como os usados na disciplina.](../assets/images/modulo-4-b3-c4-quatro-niveis-v2.svg){ .module-diagram }
</figure>

*Figura 5 — Os quatro níveis de abstração do C4, com o público de cada nível. Fonte: material do curso, com base em Brown (n.d.).*

Cada nível responde a uma pergunta diferente e atende a um público diferente, e essa correspondência entre pergunta e público decide qual diagrama usar em cada situação.

| Nível | Pergunta que responde | Público |
| --- | --- | --- |
| Contexto | O que o sistema faz? | Partes interessadas não técnicas que precisam entender o escopo geral |
| Contêineres | Como o sistema funciona como um todo? | Arquitetos e desenvolvedores, para entender a estrutura de alto nível |
| Componentes | Como cada parte de um contêiner é estruturada? | Desenvolvedores que implementam ou mantêm o sistema |
| Código | Como a implementação de um componente é realizada? | Desenvolvedores em nível de detalhamento máximo |

Esta aula usa os dois primeiros níveis, contexto e contêineres, como notação de modelagem no restante deste bloco e no bloco 4, e o [bloco 4](bloco-4-arquitetura-de-infraestrutura.md) acrescenta o diagrama de implantação, um dos diagramas de apoio do modelo. Os níveis de componentes e de código existem e seguem a mesma lógica de decomposição, mas ficam fora do escopo da disciplina.

Três princípios organizam o uso das abstrações. A progressividade pede começar pela visão ampla e descer ao detalhe, alinhando o nível ao público e ao propósito. A coerência pede manter as abstrações alinhadas entre os níveis, para que o que aparece como contêiner no nível 2 não reapareça como sistema externo no nível 1. O foco no propósito pede que cada diagrama tenha um objetivo claro e responda à pergunta de um grupo específico de interessados.

### Diagrama de contexto

Quando a Reitoria da ACME quer saber o que está dentro da solução e o que está fora, ela precisa de um desenho que se leia em um minuto, e esse desenho é o **diagrama de contexto**, que fornece uma visão ampla do sistema modelado e de como ele se relaciona com os atores externos. Ele comunica os limites do sistema e as interações de alto nível, e por isso trabalha com apenas três tipos de elemento: as pessoas, que representam os atores humanos que interagem diretamente com o sistema, sejam usuários finais ou outras partes interessadas, os sistemas de software, que representam tanto o sistema sendo modelado quanto os outros sistemas com que ele se comunica, e as relações, que demonstram como atores e sistemas externos interagem com o sistema principal, descrevendo o meio e o protocolo usados.

<figure markdown="span">
![Diagrama de contexto com três elementos, a pessoa Cliente, o Sistema Principal marcado como sistema e o Sistema Externo Financeiro marcado como sistema externo, ligados por relações rotuladas com a interação e o protocolo, HTTPS e REST.](../assets/images/modulo-4-b3-c4-contexto-generico-v2.svg){ .module-diagram }
</figure>

*Figura 6 — Diagrama de contexto genérico, com os três tipos de elemento e as relações rotuladas por protocolo. Fonte: material do curso, com base em Brown (n.d.).*

O roteiro para montar esse diagrama tem cinco etapas encadeadas. Primeiro se identifica o sistema de interesse, porque ele é o foco do modelo, e em seguida se definem os atores externos, que são as pessoas que interagem com ele. Depois se listam os sistemas externos que trocam informação diretamente com o sistema principal, e só então se desenham as relações, que conectam pessoas e sistemas ao sistema principal com descrição clara da interação e do protocolo. A última etapa acrescenta descrição a cada elemento, para que o diagrama seja compreensível por todos os interessados, inclusive os que não participaram do desenho.

O exemplo abaixo é o contexto do sistema acadêmico da Universidade ACME. Ele mostra pessoas, sistemas externos e a fronteira adotada no primeiro ciclo. O núcleo COBOL está dentro da solução porque sua convivência com os serviços novos faz parte do projeto.

<figure markdown="span">
![Contexto da Universidade ACME, com alunos, professores, secretaria e sistemas externos relacionados ao sistema acadêmico.](../assets/images/acme-ex15-contexto-corrigido.svg){ .module-diagram }
</figure>

*Figura 7 — Contexto do sistema acadêmico da Universidade ACME. Fonte: material do curso.*

### Diagrama de contêineres

Quando a equipe técnica precisa saber onde um requisito será implementado, o diagrama de contexto não responde, e o nível seguinte é o diagrama de contêineres, que detalha os principais contêineres que compõem o sistema, com suas responsabilidades e com a forma como interagem entre si e com os sistemas externos. Contêineres representam as aplicações, bancos de dados ou outros serviços que compõem o sistema, cada um com responsabilidade específica e tecnologia declarada. Sistemas externos e relações continuam presentes, com o mesmo significado do nível de contexto apresentado acima.

<figure markdown="span">
![Diagrama de contêineres com o Sistema Principal decomposto em Frontend Web em Angular, Backend de Aplicação em Spring Boot e Banco de Dados PostgreSQL, ligados entre si e ao Sistema Externo Financeiro por relações rotuladas com a interação e o protocolo.](../assets/images/modulo-4-b3-c4-conteineres-generico-v2.svg){ .module-diagram }
</figure>

*Figura 8 — Diagrama de contêineres genérico, com a decomposição interna do sistema e a tecnologia de cada contêiner. Fonte: material do curso, com base em Brown (n.d.).*

O roteiro de montagem do diagrama de contêineres tem quatro etapas:

1. Identificar os sistemas externos com que o sistema principal interage diretamente, que são os mesmos do nível de contexto.
2. Definir os contêineres principais, como aplicação de interface, serviço de retaguarda ou banco de dados.
3. Descrever as relações entre contêineres e entre eles e os sistemas externos, especificando protocolo e direção.
4. Acrescentar a cada contêiner uma descrição curta da responsabilidade e da tecnologia usada.

O diagrama seguinte detalha o mesmo sistema acadêmico. Os portais, o aplicativo, os serviços, os bancos e o núcleo ficam dentro da fronteira. O provedor de identidade, o ambiente virtual e as demais dependências permanecem externos. Compare os nomes com o contexto antes de acrescentar detalhes.

<figure markdown="span">
![Contêineres da arquitetura alvo da Universidade ACME, com portais, aplicativo do aluno, serviços de matrícula e notas, seus bancos e núcleo COBOL. As tecnologias dos componentes novos serão escolhidas na Aula 5.](../assets/images/acme-ex16-diagrama-de-conteineres.svg){ .module-diagram }
</figure>

*Figura 9 — Contêineres do mesmo sistema acadêmico. Fonte: material do curso.*

### Tecnologia no contêiner antes da definição tecnológica

O modelo C4 pede que cada contêiner declare sua tecnologia. Na arquitetura alvo construída nesta aula, a escolha de produto, de framework e de provedor ainda não foi feita, porque depende da plataforma arquitetural decidida na Aula 5. Por convenção do curso, os contêineres da arquitetura alvo levam o rótulo tecnologia a definir na Aula 5, e esse rótulo indica à Aula 5 exatamente quais decisões tecnológicas ela precisa tomar.

### Confira a fronteira nos dois níveis

O sistema de interesse é o mesmo nas Figuras 7 e 9. No contexto, o núcleo COBOL fica incluído na caixa do sistema acadêmico. No nível de contêineres, ele aparece como parte interna dessa caixa. O fato de uma fábrica externa fazer sua manutenção não o torna automaticamente um sistema externo: o projeto da ACME inclui sua continuidade e sua integração durante a transição.

Em ambos os níveis, o ERP financeiro e o ambiente virtual continuam externos porque serão usados sem terem sua evolução assumida pelo projeto. A fronteira representa a responsabilidade definida no escopo. Confira essa regra ao comparar os diagramas com a declaração do primeiro ciclo no caderno.

## Uso pelo arquiteto

A pergunta do arquiteto neste domínio, no roteiro do [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md), é a seguinte. Que aplicações mudam, por quais interfaces trocam essas entidades, que contrato governa cada interface e onde passa a fronteira da solução?

O arquiteto precisa que provedor e consumidor de cada interface evoluam em separado sem quebrar um ao outro, e por isso escreve o contrato de integração antes da implementação, transformando em campo verificável a garantia que cada parte espera da outra. Ele parte do dono de cada entidade, marcado na grade de dados, porque o dono é a origem natural da interface que expõe a entidade, e entrega os contratos às equipes que implementam. Sem o contrato escrito, cada equipe supõe a garantia da outra e a divergência aparece na integração, quando já existe código dos dois lados.

A mesma solução precisa ser mostrada a públicos diferentes, e o arquiteto escolhe o nível do diagrama pela audiência e pela decisão em pauta. Diante de uma parte interessada de negócio, que decide sobre escopo e sobre relação com terceiros, ele apresenta o diagrama de contexto, porque nenhuma decisão sobre estrutura interna será tomada naquela reunião, e confere que a fronteira desenhada coincide com a declaração de escopo do primeiro ciclo. Diante da equipe técnica, que precisa saber onde um requisito será implementado, apresenta o diagrama de contêineres como nível mínimo útil, e o rótulo de cada relação com tipo, volume e latência transforma o diagrama na lista de exigências que a definição tecnológica da Aula 5 precisa atender. Com o nível errado, a parte interessada de negócio recebe detalhe que não a ajuda a decidir, ou a equipe técnica recebe um desenho sem a informação de que precisa para implementar.

## No caderno arquitetural

{{ficha:5}}

**Para que serve.** A seção 5 do caderno mostra num só desenho o que está dentro da solução, quem a usa e com que outros sistemas ela conversa. Quem decide escopo e contratos com terceiros lê esse desenho em um minuto, e por isso a fronteira precisa estar no lugar certo. Antes de chegar ao desenho, o arquiteto decide o que fazer com cada aplicação existente e como a nota chega ao ambiente virtual, porque essas escolhas definem quem fica dentro e quem fica fora.

**O que você faz neste exercício.** O enunciado traz onze aplicações da ACME, como os quatro portais Java e o núcleo COBOL, o esqueleto de um contrato com doze campos para a integração de notas e um diagrama de contexto que tem dois erros. Você dá uma cor a cada aplicação, preenche o contrato, explica o que acontece quando o professor corrige uma nota já enviada e corrige o diagrama. As respostas entram no caderno na parte Portfólio, contrato de notas e diagrama de contexto.

| Campo do caderno | Como preencher | Item |
| --- | --- | --- |
| Classificação da aplicação | Diga se cada uma das onze aplicações é verde (manter e evoluir), âmbar (manter por ora, com investimento restrito) ou vermelha (substituir ou retirar) | 1 |
| Justificativa da classificação | Escreva uma linha com o fato do caso que levou à cor, como o ano da aplicação, a tecnologia ou a decisão da Reitoria de mantê-la | 1 |
| Contrato de integração de notas | Preencha, com resposta curta, os doze campos do contrato que leva a nota ao ambiente virtual, de Origem até Nível de serviço | 2 |
| Modo de comunicação | Diga se a integração é síncrona ou assíncrona e justifique pelos padrões escolhidos no exercício 11 | 2 |
| Nota corrigida | Explique o que acontece quando o professor corrige uma nota que já foi enviada ao ambiente virtual | 2 |
| Erros do diagrama | Aponte os dois erros de nível ou de fronteira que o diagrama de contexto do enunciado contém | 3 |
| Correção de cada erro | Para cada erro, diga qual elemento está errado e onde ele deve ficar no diagrama | 3 |

**O que você já tem.** O dono da entidade nota, marcado no exercício 14, que é a origem do contrato, e os padrões do exercício 11, que justificam o modo de comunicação.

**Quando está pronto.** As onze aplicações têm cor e justificativa, os doze campos do contrato estão preenchidos com o modo declarado e o tratamento da nota corrigida, e os dois erros do diagrama estão apontados e corrigidos.

[Ver esta seção no template](../caderno/template.md#5-contexto-do-sistema-c4-nivel-1){ .caderno-botao }
[Ver o gabarito do exercício 15](../gabaritos/gabarito-exercicio-15.md){ .caderno-botao }

{{/ficha}}

## Exercício 15

O exercício 15 aplica à ACME os três assuntos deste bloco, e cada assunto é um item. A ACME é uma universidade privada brasileira fictícia, com 38.400 alunos ativos, cujo sistema acadêmico, em operação desde 2004, passa por modernização incremental. O item 1 decide o destino de cada aplicação do portfólio, classificada em vermelho, âmbar ou verde. O item 2 preenche o contrato da integração que leva a nota do sistema da ACME ao ambiente virtual de aprendizagem, a plataforma de ensino a distância. O item 3 corrige um diagrama de contexto, que desenha a fronteira da solução. Os três itens servem para praticar as decisões de aplicações antes de o bloco 4 transformar o desenho em exigências de infraestrutura.

O exercício reaproveita o dono da entidade nota marcado no [exercício 14](bloco-2-arquitetura-de-dados.md#exercicio-14), que é a aplicação autorizada a gravar a nota e será a origem do contrato do item 2. Reaproveita também fatos reproduzidos da [página inicial do caso](../caso-acme/index.md), dos [dados operacionais](../caso-acme/dados-operacionais.md) e da [arquitetura de linha de base](../caso-acme/linha-de-base.md).

### Item 1: Classificação do portfólio

Como a modernização da ACME é incremental, nem toda aplicação será trocada de uma vez, e este item decide que destino cada aplicação deve ter na modernização, segundo a classificação em vermelho (substituir ou retirar), âmbar (manter por ora, com investimento restrito) e verde (manter e evoluir). O enunciado traz um catálogo de onze aplicações e serviços externos da ACME, registrados na linha de base e ainda sem classificação. As quatro primeiras linhas são os portais web em Java, para aluno, professor, secretaria e gestor, e JSF 1.2 e EJB 2.0 são tecnologias Java antigas para telas web e componentes de servidor. O núcleo transacional é o sistema central, escrito em COBOL, e o ERP financeiro e o ambiente virtual permanecem por decisão da Reitoria. Você registra uma cor e uma linha de justificativa para cada uma das onze.

| Aplicação | Ano | Tecnologia | Observação |
| --- | --- | --- | --- |
| Portal do Aluno | 2007 | JSF 1.2 e EJB 2.0 | 84 telas, sem versão responsiva, acesso direto ao banco |
| Portal do Professor | 2008 | JSF 1.2 e EJB 2.0 | 46 telas |
| Portal da Secretaria | 2008 | JSF 1.2 e EJB 2.0 | 62 telas |
| Portal do Gestor | 2009 | JSF 1.2 e EJB 2.0 | 28 telas, acesso direto ao banco |
| Núcleo transacional | 2004 | COBOL sobre CICS | 11 módulos, manutenção sob contrato até 30/09/2027 |
| ERP financeiro | Não informado | Produto contratado | Permanece por decisão da Reitoria de 12/03/2026 |
| Ambiente virtual de aprendizagem | Não informado | Produto contratado | Permanece por decisão da Reitoria de 12/03/2026 |
| Data warehouse institucional | Não informado | Não informado | Recebe cópia integral de 140 tabelas por lote |
| Assinador digital ICP-Brasil | Não informado | Serviço externo | Assinatura de histórico e diploma |
| Gateway de pagamento | Não informado | Serviço externo | Geração de boleto e cobrança em cartão, chamado pelo Portal do Aluno |
| Diretório corporativo | Não informado | LDAP | Autenticação de todos os perfis |

1. Classifique cada aplicação do catálogo em vermelho, âmbar ou verde, conforme a [classificação do portfólio](#portfolio-de-aplicacoes), com uma linha de justificativa.

Suas respostas viram os campos Classificação da aplicação e Justificativa da classificação, na seção 5 do caderno.

### Item 2: Contrato da integração de notas

Hoje a nota lançada às 15h00 só chega ao ambiente virtual no dia seguinte, e como o R7 exige 10 minutos, as duas aplicações precisam combinar por escrito como a troca passa a funcionar. Esse acordo, escrito campo a campo sobre quem envia, quando envia, em que formato e com quais garantias, é o contrato de integração, e este item o especifica para a nota que vai do sistema da ACME ao ambiente virtual. O requisito R7, declarado pela Educação a Distância, determina que a nota lançada pelo professor chegue ao ambiente virtual de aprendizagem em até 10 minutos. Hoje a exportação de notas consolidadas ocorre em lote diário, uma rotina automática que reúne os dados num arquivo e o envia em horário fixo, iniciada às 05h10, com 4.800 lançamentos em dia letivo comum e até 360.000 na janela de fechamento. A propagação em minutos exige o plano do ambiente virtual que oferece interfaces de programação, que são formas de outro sistema enviar dados a ele sem esperar o arquivo noturno, com acréscimo de 38% sobre o valor anual do contrato vigente. O diagrama abaixo, em notação livre, mostra o caminho atual da nota, do lançamento no Portal do Professor à carga no ambiente virtual pelo lote das 05h10.

```mermaid
sequenceDiagram
    participant PP as Portal do Professor
    participant NT as Núcleo transacional
    participant LT as Lote de exportação das 05h10
    participant AV as Ambiente virtual de aprendizagem
    PP->>NT: nota lançada durante o dia letivo
    NT->>NT: calcula média e situação
    Note over NT,LT: a nota aguarda o lote do dia seguinte
    LT->>NT: lê as notas consolidadas às 05h10
    LT->>AV: arquivo com 4.800 lançamentos, até 360.000 no fechamento
```

O esqueleto do contrato da integração de notas entre a ACME e o ambiente virtual de aprendizagem é a tabela abaixo, com os doze campos da [estrutura de um contrato](#estrutura-de-um-contrato) e a coluna Resposta em branco. Dois exemplos de campo são o Gatilho, que é o evento que dispara a troca, e o Nível de serviço, que é o prazo, o volume e a disponibilidade que o provedor garante.

| Campo | Resposta |
| --- | --- |
| Origem | |
| Destino | |
| Gatilho | |
| Itens trocados | |
| Sequência | |
| Pré e pós-condições | |
| Protocolo | |
| Formato e esquema | |
| Semântica de erro | |
| Versionamento | |
| Garantia de entrega e idempotência | |
| Nível de serviço | |

1. Preencha cada campo do esqueleto com resposta curta, usando como origem o dono da entidade nota marcado no exercício 14.
2. Declare se a integração é síncrona, em que o consumidor espera a resposta, ou assíncrona, em que o provedor publica e o consumidor processa depois, e justifique o modo pelos padrões que o aluno selecionou no [exercício 11](../modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md#exercicio-11) para a coexistência com o sistema antigo, a proteção contra falha de integração e a publicação confiável de mudança.
3. Indique o que acontece quando o professor corrige uma nota já enviada.

Suas respostas viram os campos Contrato de integração de notas, Modo de comunicação e Nota corrigida, na seção 5 do caderno.

### Item 3: Erros de nível ou de fronteira no diagrama de contexto

Se a fronteira do diagrama estiver no lugar errado, quem decide escopo e contratos com terceiros decide sobre um desenho enganoso, e este item treina a conferência de um diagrama de contexto, o primeiro nível do C4, que mostra o sistema como uma caixa única, com as pessoas que o usam e os sistemas externos com que ele se comunica. Dois critérios orientam a conferência. O primeiro é o nível: o contexto mostra só pessoas e sistemas e deixa de fora o que fica dentro de um sistema, como aplicações e bancos de dados. O segundo é a fronteira, a linha tracejada que separa o que fica dentro dela, que a ACME evolui e opera, do que fica fora, que outra equipe ou fornecedor mantém. O enunciado traz um diagrama de contexto da arquitetura alvo do primeiro ciclo, com três pessoas, aluno, professor e secretaria acadêmica, ligadas ao sistema acadêmico, e com os demais elementos ligados a ele. O diagrama contém dois erros de nível ou de fronteira, conforme os níveis descritos na seção [Diagrama de contexto](#diagrama-de-contexto).

<figure markdown="span">
![Diagrama de contexto do primeiro ciclo da ACME com três atores no alto, aluno, professor e secretaria acadêmica, ligados ao sistema acadêmico. Dentro da fronteira tracejada do sistema acadêmico estão o elemento sistema acadêmico e o ERP financeiro. Abaixo, ligados por linhas ortogonais, seis elementos fora da fronteira, banco de dados acadêmico, ambiente virtual de aprendizagem, assinador digital ICP-Brasil, gateway de pagamento, provedor de identidade e órgão regulador.](../assets/images/acme-ex15-diagrama-de-contexto.svg){ .module-diagram }
</figure>

1. Aponte os dois erros do diagrama e descreva a correção de cada um, indicando o elemento afetado.

Suas respostas viram os campos Erros do diagrama e Correção de cada erro, na seção 5 do caderno.

O diagrama de contexto corrigido neste item é a base do diagrama de contêineres do exercício 16, no [bloco 4](bloco-4-arquitetura-de-infraestrutura.md).

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seção 2.6, arquitetura de aplicações, hierarquia de serviços, catálogo do portfólio, classificação em vermelho, âmbar e verde e tipos de aplicação, seção 2.8, interfaces na arquitetura de software, seção 3.6.4, análise de interfaces, e seção 4.3.1, padrões técnicos. Os conceitos foram adaptados ao caso da Universidade ACME)
- Fielding, R., Nottingham, M., & Reschke, J. (Eds.). (2022). *HTTP semantics* (RFC 9110). RFC Editor. https://www.rfc-editor.org/rfc/rfc9110 (semântica do HTTP)
- OpenAPI Initiative. (2026). *OpenAPI specification* (Versão 3.2.1). https://spec.openapis.org/oas/latest.html (finalidade e estrutura da descrição de interface HTTP)
- AsyncAPI Initiative. (n.d.). *AsyncAPI specification* (Versão 3.1.0). https://www.asyncapi.com/docs/reference/specification/latest (descrição de interfaces orientadas a mensagens, independente de protocolo)
- *Sistema Nota Fiscal Eletrônica: Manual de orientação do contribuinte, visão geral* (Versão 7.00). (2020). https://www.confaz.fazenda.gov.br/legislacao/arquivo-manuais/moc7-visao-geral.pdf (seções 4.2.3 e 4.4, certificado digital, protocolos de comunicação e esquemas das mensagens)
- Brown, S. (n.d.). *The C4 model for visualising software architecture*. https://c4model.com (sítio oficial do modelo C4)
- gRPC Authors. (n.d.-a). *Introduction to gRPC*. https://grpc.io/docs/what-is-grpc/introduction/ (Protocol Buffers como linguagem de definição de interface e como formato das mensagens)
- gRPC Authors. (n.d.-b). *FAQ*. https://grpc.io/docs/what-is-grpc/faq/ (transporte das chamadas sobre HTTP/2)
- GraphQL Foundation. (n.d.). *Learn GraphQL*. https://graphql.org/learn/ (linguagem de consulta para APIs, sistema de tipos e seleção dos campos pelo cliente)
- JSON Schema. (n.d.). *What is JSON Schema?* https://json-schema.org/overview/what-is-jsonschema (definição da linguagem e versão corrente 2020-12)
- Apache Software Foundation. (n.d.). *Apache Avro documentation*. https://avro.apache.org/docs/ (esquemas escritos em JSON e dado autodescritivo)
- Confluent. (n.d.). *Schema Registry for Confluent Platform*. https://docs.confluent.io/platform/current/schema-registry/index.html (repositório central de esquemas, formatos suportados e verificação de compatibilidade)
- Google. (n.d.). *Overview*. Protocol Buffers Documentation. https://protobuf.dev/overview/ (definição de Protocol Buffers e geração de código a partir de arquivos .proto)
- RabbitMQ. (n.d.). *Which protocols does RabbitMQ support?* https://www.rabbitmq.com/docs/protocols (suporte a AMQP 0-9-1 e AMQP 1.0)
- Jena, J., & Dalal, S. (2025). *The Idempotency-Key HTTP header field* (Internet-Draft draft-ietf-httpapi-idempotency-key-header-07). IETF. https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/ (finalidade do cabeçalho, respostas 409 e 422 e estado expirado do rascunho, consultado em 03/10/2026)
- Mendes, M. (2026b). *Guias de projeto de arquitetura de software* [Material de curso, versão arquivada]. https://github.com/aulas-marco/projeto-arquitetura-software/tree/30f15cd (guias 3.1, 3.2 e 3.3, fonte dos quatro níveis, dos princípios de abstração, dos elementos dos diagramas de contexto e de contêineres, e dos dois roteiros de montagem)

**Material do curso.** O bloco usa as entradas [arquitetura de aplicações](../referencia/glossario.md#arquitetura-de-aplicacoes), [padrão técnico](../referencia/glossario.md#padrao-tecnico), [protocolo](../referencia/glossario.md#protocolo), [especificação de interface](../referencia/glossario.md#especificacao-de-interface), [contrato de integração](../referencia/glossario.md#contrato-de-integracao) e [modelo C4](../referencia/glossario.md#modelo-c4) do glossário, além do dossiê da instituição fictícia [ACME](../caso-acme/index.md).
