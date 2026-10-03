# Arquitetura de infraestrutura da solução

Este bloco conclui o detalhamento por domínios e responde onde a solução executa, como suas partes se conectam e o que cada interface exige, sem escolher produto ou provedor, decisão reservada à Aula 5.

## Antes de começar

- [Arquitetura de infraestrutura](../referencia/glossario.md#arquitetura-de-infraestrutura)
- [Modelo C4](../referencia/glossario.md#modelo-c4)
- [Bloco de construção da solução](../referencia/glossario.md#bloco-de-construcao-da-solucao)
- Diagrama de contexto corrigido no [exercício 15](bloco-3-arquitetura-de-aplicacoes-e-integracao.md#exercicio-15)

## Infraestrutura e contêineres

A **arquitetura de infraestrutura** é a arquitetura dos componentes e serviços tecnológicos que sustentam as atividades da organização, chamada de arquitetura de tecnologia no TOGAF. Ela inclui equipamentos, sistemas operacionais, plataformas intermediárias, redes, comunicações, capacidade de processamento e padrões técnicos, e também ativos intangíveis, como contratos com fornecedores.

### Infraestrutura na solução

Os objetivos da arquitetura de infraestrutura são maximizar a eficácia e a eficiência do provimento e do uso da infraestrutura, eliminar duplicação de componentes e manter a infraestrutura alinhada às necessidades operacionais do negócio, que mudam com a estratégia e com a tecnologia disponível. Muitos componentes de infraestrutura são invisíveis às partes interessadas de negócio, embora sustentem requisitos não funcionais como desempenho e confiabilidade, e por isso os modelos de infraestrutura servem de base para as visões de quem tem essas preocupações.

Os artefatos do domínio incluem o catálogo de tecnologia de infraestrutura, o modelo técnico de referência, o catálogo de padrões técnicos, a visão de configuração, a matriz entre aplicação e tecnologia e o modelo de plataforma. A declaração formal da infraestrutura exigida por uma solução, chamada de definição tecnológica da solução, e o modelo técnico de referência são tratados na Aula 5. Este bloco permanece no nível lógico, com os contêineres que a solução precisa, no sentido do [diagrama de contêineres](bloco-3-arquitetura-de-aplicacoes-e-integracao.md#diagrama-de-conteineres) do bloco 3, e as exigências de cada interface entre eles.

### A solução como grafo

A solução pode ser representada como um grafo, em que cada [bloco de construção](../referencia/glossario.md#bloco-de-construcao-da-solucao) é um vértice e cada interface, descrita pelos seis atributos apresentados no [bloco 3](bloco-3-arquitetura-de-aplicacoes-e-integracao.md#descricao-de-uma-interface), é uma aresta. O grau de um vértice é o número de arestas ligadas a ele, e a soma dos graus de todos os vértices, dividida por dois, dá o número de interfaces da solução. Registrar o número de interfaces de cada bloco de construção permite, portanto, calcular o total de interfaces que a solução precisa sustentar.

Num exemplo genérico com cinco blocos de construção, dois blocos têm grau 3 e três blocos têm grau 2. A soma dos graus é 12, e a solução tem 6 interfaces. Cada uma dessas interfaces é examinada separadamente quanto ao tipo e ao volume de tráfego que passa por ela, porque é desse exame que sai a exigência de comunicação que a infraestrutura precisa atender. Nem toda interface usa rede, já que uma passagem entre dois processos pode ser manual, e mesmo assim todas as interfaces são examinadas para que nenhuma seja esquecida.

<figure markdown="span">
![Grafo genérico com cinco blocos de construção, rotulados de BC1 a BC5, ligados por seis arestas. Cada vértice traz o próprio grau anotado, dois com grau 3 e três com grau 2, e uma conta mostra que a soma dos graus, 12, dividida por 2 dá 6 interfaces. Uma aresta destacada mostra os dois rótulos que cada interface recebe, o tipo de comunicação e o volume de tráfego.](../assets/images/modulo-4-solucao-como-grafo.svg){ .module-diagram }
</figure>

*Figura 1 — Solução como grafo de blocos de construção e interfaces. Fonte: material do curso, com base em Lovatt (2021, seção 7.5).*

### Camadas de execução

Uma camada de execução é o nível de abstração em que um bloco de construção da solução recebe processamento, memória e rede, e cada camada define quais responsabilidades ficam com a equipe da solução e quais ficam com a operação de infraestrutura ou com o provedor de nuvem. A escolha da camada para cada contêiner pertence à definição tecnológica da solução, tratada na Aula 5, mas o arquiteto precisa conhecer as camadas para declarar o que cada contêiner exige de isolamento, de elasticidade e de tempo de inicialização. A lista abaixo define as cinco camadas representadas na Figura 2, do servidor físico à função sem servidor, e acrescenta os conceitos de nó e de cluster do Kubernetes.

- Servidor físico é o equipamento dedicado em que o sistema operacional executa diretamente sobre o hardware, com toda a capacidade reservada a uma carga e com a manutenção do equipamento a cargo da organização que o possui.
- Máquina virtual é um computador simulado por um hipervisor, como VMware ESXi ou KVM, ou oferecido como serviço, como o Amazon EC2, e cada máquina virtual tem sistema operacional próprio sobre uma fatia do servidor físico.
- Contêiner é um processo isolado que compartilha o núcleo do sistema operacional do hospedeiro e leva a aplicação e as dependências dela numa imagem, formato popularizado pelo Docker e executado também por alternativas como o Podman.
- Orquestrador é a plataforma que distribui contêineres por um conjunto de máquinas, reinicia instâncias que falham e ajusta o número de réplicas, papel cumprido pelo Kubernetes, em que o pod é a menor unidade implantável e agrupa um ou mais contêineres com rede e armazenamento compartilhados (The Kubernetes Authors, n.d.-b).
- No Kubernetes, o nó é a máquina virtual ou física que executa pods, e o cluster é o conjunto de nós gerenciados por um plano de controle, que mantém em cada nó os serviços necessários para executar pods (The Kubernetes Authors, n.d.-a).
- Função sem servidor é uma unidade de código executada em resposta a um evento ou a uma chamada, com servidores, capacidade, escalonamento e atualizações gerenciados pelo provedor, como no AWS Lambda e no Azure Functions (Amazon Web Services, n.d.-b).

<figure markdown="span">
![Cinco colunas comparam servidor físico, máquina virtual, contêiner, orquestrador Kubernetes e função sem servidor. Cada coluna empilha aplicação, ambiente de execução, sistema operacional, virtualização e hardware, coloridos conforme a camada fique com a equipe da solução ou com a plataforma, e uma caixa abaixo lista o que o arquiteto declara em cada caso.](../assets/images/modulo-4-b4-camadas-de-execucao.svg){ .module-diagram }
</figure>

*Figura 2 — Camadas de execução, responsável por camada e itens declarados pelo arquiteto. Fonte: material do curso, com base em Lovatt (2021, seção 2.7), The Kubernetes Authors (n.d.-a, n.d.-b) e Amazon Web Services (n.d.-b).*

O que o arquiteto declara diminui à medida que a plataforma assume camadas. Num servidor físico ou numa máquina virtual, a declaração inclui processadores, memória, disco e sistema operacional, enquanto num contêiner ela se concentra na imagem, nas portas e nos limites de recursos, e numa função sem servidor ela se reduz ao código, ao gatilho, à memória reservada e ao tempo máximo de execução, que no AWS Lambda é de 15 minutos por invocação (Amazon Web Services, n.d.-b).

Sistemas corporativos antigos acrescentam uma sexta plataforma de execução, o mainframe com monitor transacional, em que um monitor como o IBM CICS ou o IBM IMS TM coordena transações curtas de muitos usuários simultâneos sobre programas e bases de dados do próprio mainframe. Essa plataforma não se encaixa nas colunas da Figura 2, porque a capacidade é contratada e operada como um conjunto, e um bloco de construção que permanece no mainframe aparece no diagrama de implantação como nó próprio, ligado aos demais nós por uma conexão cuja latência e cuja largura de banda o arquiteto precisa declarar.

### Topologia de implantação

A topologia de implantação é a disposição dos nós de execução e de rede da solução, com a localização física ou lógica de cada nó e os caminhos que as requisições e os dados percorrem entre eles. Os elementos que aparecem na maior parte das topologias de soluções em nuvem estão listados abaixo, cada um com exemplos de serviço da AWS e da Microsoft Azure.

- DNS é o serviço que traduz o nome do sistema para o endereço do ponto de entrada e que pode direcionar o usuário para outro endereço quando o primeiro deixa de responder, papel cumprido pelo Amazon Route 53 e pelo Azure DNS.
- CDN é uma rede de servidores distribuídos geograficamente que guarda cópias do conteúdo estático perto do usuário, como Amazon CloudFront e Azure Front Door, e reduz a latência percebida e a carga sobre os serviços de origem.
- Balanceador de carga é o componente que recebe as requisições e as distribui entre as réplicas de um serviço, retirando da distribuição as réplicas que deixam de responder à verificação de saúde, como o Elastic Load Balancing da AWS e o Azure Load Balancer.
- Região é uma área geográfica separada do provedor, e zona de disponibilidade é um dos vários locais isolados dentro de uma região, de modo que distribuir instâncias entre zonas protege a aplicação da falha de um único local (Amazon Web Services, n.d.-a).
- Conexão dedicada é um enlace privado entre a rede da organização e o provedor, que não passa pela internet pública, como o AWS Direct Connect (Amazon Web Services, n.d.-c) e o Azure ExpressRoute (Microsoft, 2026).
- VPN é um túnel cifrado que atravessa a internet pública entre o centro de dados local e o provedor, com custo de implantação menor que o da conexão dedicada e com latência que depende das condições da internet.

<figure markdown="span">
![Usuários consultam o DNS, recebem conteúdo estático de uma CDN e enviam requisições HTTPS a um balanceador de carga dentro de uma região do provedor. O balanceador distribui as requisições entre quatro réplicas do serviço em duas zonas de disponibilidade, o banco primário da zona A é replicado para a zona B, e uma conexão dedicada ou VPN liga a região a um centro de dados local com um sistema legado.](../assets/images/modulo-4-b4-topologia-de-implantacao.svg){ .module-diagram }
</figure>

*Figura 3 — Topologia de implantação com DNS, CDN, balanceador de carga, duas zonas de disponibilidade e conexão ao centro de dados local. Fonte: material do curso, com base em Amazon Web Services (n.d.-a, n.d.-c) e Microsoft (2026).*

O número de zonas de disponibilidade decorre da disponibilidade exigida. Com réplicas numa única zona, a solução fica indisponível sempre que aquela zona falha, e com réplicas em duas zonas a indisponibilidade simultânea das duas passa a ser o evento que interrompe o serviço. Num cálculo ilustrativo, que supõe falhas independentes entre as zonas, duas zonas com 99,5% de disponibilidade cada resultam em 1 − 0,005 × 0,005, ou 99,9975%, valor que não considera falhas da região inteira nem de componentes compartilhados entre as zonas.

A redundância entre zonas também tem custo de capacidade. Se o pico de uso exige quatro réplicas do serviço, cada zona precisa sustentar as quatro réplicas sozinha para que a falha de uma zona não reduza o desempenho, o que leva a oito réplicas provisionadas ou a uma regra de escalonamento automático capaz de dobrar a capacidade da zona remanescente em poucos minutos.

Os componentes de infraestrutura invisíveis às partes interessadas de negócio, citados no início do bloco, sustentam requisitos não funcionais de desempenho e confiabilidade, e a topologia é o artefato em que essa ligação aparece de modo verificável. O requisito de disponibilidade define o número de zonas e a replicação do banco, o requisito de tempo de resposta define a capacidade de cada réplica e a presença de CDN, e o requisito de integração com sistemas que permanecem no centro de dados local define a escolha entre conexão dedicada e VPN. A seleção de provedor, de região e de serviços para a ACME pertence à definição tecnológica da Aula 5.

### Diagrama de implantação em C4

O diagrama de implantação é o diagrama de apoio do modelo C4 que mostra como instâncias de sistemas de software e de contêineres do modelo estático são implantadas na infraestrutura de um ambiente de implantação, como produção, homologação ou desenvolvimento (Brown, n.d.). Cada contêiner do [diagrama de contêineres](bloco-3-arquitetura-de-aplicacoes-e-integracao.md#diagrama-de-conteineres) do bloco 3 é mapeado em nós de implantação aninhados, que vão do ambiente à região do provedor, à zona de disponibilidade, ao cluster Kubernetes, à máquina virtual e ao serviço gerenciado em que a instância executa. A notação do modelo C4 e os diagramas de contexto e de contêineres estão no [bloco 3](bloco-3-arquitetura-de-aplicacoes-e-integracao.md#modelo-c4), e o público do diagrama de implantação é técnico, de dentro e de fora da equipe de desenvolvimento, incluindo arquitetos de software, desenvolvedores, arquitetos de infraestrutura e pessoal de operação e suporte.

O diagrama de implantação segue quatro regras de construção, derivadas da definição publicada no sítio oficial do modelo C4 (Brown, n.d.):

1. Cada diagrama cobre um único ambiente de implantação, e a solução que tem produção, homologação e desenvolvimento recebe três diagramas, porque a quantidade de réplicas e de zonas costuma variar entre os ambientes.
2. O nó de implantação representa o lugar onde uma instância executa e pode ser infraestrutura física, máquina virtual, contêiner Docker ou ambiente de execução, e os nós se aninham, como um ambiente de execução dentro de um contêiner Docker, dentro de uma máquina virtual, dentro de uma zona de disponibilidade.
3. Cada instância de contêiner corresponde a um contêiner do [diagrama de contêineres](bloco-3-arquitetura-de-aplicacoes-e-integracao.md#diagrama-de-conteineres) e leva o mesmo nome, e um contêiner com quatro réplicas aparece como quatro instâncias sem que o diagrama de contêineres mude.
4. Os nós de infraestrutura, como DNS, balanceador de carga e firewall, aparecem como elementos de apoio, ligados às instâncias que atendem.

O contêiner do modelo C4 é uma unidade executável ou de armazenamento de dados, como uma aplicação web, um serviço ou um banco, e pode ser implantado num contêiner Docker, numa máquina virtual ou numa função sem servidor, de modo que os dois usos da palavra contêiner precisam ser distinguidos no texto que acompanha o diagrama. A Figura 4 mostra, em C4, o ambiente de produção do sistema de agendamento da Clínica Odontológica ACME, cujos contêineres aparecem no [exemplo em C4 do bloco 3](bloco-3-arquitetura-de-aplicacoes-e-integracao.md#diagrama-de-conteineres), com os nós aninhados da região até as instâncias de contêiner do painel da recepção, do serviço de agenda e do banco de agendamentos.

<figure markdown="span">
![Diagrama de implantação em C4 do ambiente de produção do sistema de agendamento da clínica. No alto, o telefone do paciente executa o aplicativo e o computador da recepção abre o painel no navegador, e os dois enviam requisições HTTPS ao balanceador de carga, depois de o aplicativo consultar o DNS. Dentro da região do provedor de nuvem, duas zonas de disponibilidade têm cada uma um cluster Kubernetes em máquina virtual Linux com instâncias do painel da recepção e do serviço de agenda, e um banco de agendamentos gerenciado, primário na zona A e réplica na zona B, ligados por replicação. O serviço de agenda chama por HTTPS a operadora de convênio e o serviço de mensagens, sistemas externos à direita.](../assets/images/modulo-4-b4-c4-implantacao-clinica.svg){ .module-diagram }
</figure>

*Figura 4 — Diagrama de implantação em C4 do ambiente de produção da Clínica Odontológica ACME, com nós aninhados, nós de infraestrutura, instâncias de contêiner, nós de cliente e sistemas externos. Fonte: material do curso, com base em Brown (n.d.).*

Os nós de cliente aparecem fora do ambiente de produção, porque o aplicativo do paciente executa no telefone de cada paciente e o painel da recepção é aberto no navegador do computador da recepção. A operadora de convênio e o serviço de mensagens permanecem como sistemas externos, com os mesmos nomes do diagrama de contexto do bloco 3, e cada instância de contêiner leva o nome do contêiner correspondente do diagrama de contêineres.

As setas do diagrama de implantação repetem as interfaces do grafo da Figura 1, agora com a indicação do nó em que cada extremidade executa, e por isso o diagrama mostra quais interfaces atravessam a fronteira entre zonas, entre a região e o centro de dados local ou entre a solução e a internet. Na fase lógica, os nós recebem nomes genéricos, como máquina virtual Linux ou nó do cluster Kubernetes, e o nome do serviço do provedor só aparece depois da definição tecnológica da Aula 5.

## Uso pelo arquiteto

O arquiteto usa a visão de infraestrutura para converter cada contêiner do [diagrama de contêineres](bloco-3-arquitetura-de-aplicacoes-e-integracao.md#diagrama-de-conteineres) e cada interface do grafo em exigências de execução e de comunicação que a Aula 5 recebe como entrada. Para cada contêiner, ele registra a camada de execução compatível, o número de réplicas e de zonas de disponibilidade imposto pelo requisito de disponibilidade e a capacidade necessária no pico, e para cada interface registra o modo de comunicação, o volume, a latência e se ela cruza a fronteira entre a nuvem e o centro de dados local, caso em que exige conexão dedicada ou VPN. O diagrama de implantação desse estágio usa nós genéricos, como máquina virtual, cluster de contêineres ou função sem servidor, e não nomeia provedor, região nem produto, porque a definição tecnológica da solução e o modelo técnico de referência, que fazem essa escolha, são o assunto da Aula 5.

## Exercício 16

A ACME é uma universidade privada brasileira com 38.400 alunos ativos, cujo sistema acadêmico, em operação desde 2004, passa por modernização incremental. O exercício parte do diagrama de contexto corrigido no [exercício 15](bloco-3-arquitetura-de-aplicacoes-e-integracao.md#exercicio-15) e de fatos reproduzidos dos [dados operacionais](../caso-acme/dados-operacionais.md), da [arquitetura de linha de base](../caso-acme/linha-de-base.md) e da [página inicial do caso](../caso-acme/index.md).

### Item 1: Modo, volume e latência das relações

O diagrama abaixo é o diagrama de contêineres da arquitetura alvo do primeiro ciclo, coerente com o diagrama de contexto corrigido no exercício 15. Cada contêiner novo leva o rótulo tecnologia a definir na Aula 5, e as relações estão apenas numeradas, sem rótulo de comunicação.

```mermaid
graph TD
    ALU["Aluno"]
    PROF["Professor"]
    SEC["Secretaria acadêmica"]

    subgraph SA["Sistema acadêmico"]
        APP["Aplicativo do aluno<br/>tecnologia a definir na Aula 5"]
        PP["Portal do Professor<br/>tecnologia a definir na Aula 5"]
        PS["Portal da Secretaria<br/>tecnologia a definir na Aula 5"]
        SM["Serviço de matrícula<br/>tecnologia a definir na Aula 5"]
        SN["Serviço de notas<br/>tecnologia a definir na Aula 5"]
        NUC["Núcleo transacional COBOL"]
        BD[("Banco acadêmico<br/>tecnologia a definir na Aula 5")]
    end

    AVA["Ambiente virtual de aprendizagem"]
    ERP["ERP financeiro"]
    IDP["Provedor de identidade"]
    PAG["Gateway de pagamento"]
    ASS["Assinador digital ICP-Brasil"]
    REG["Órgão regulador"]

    ALU --> APP
    PROF --> PP
    SEC --> PS
    APP -->|"1"| SM
    PP -->|"2"| SN
    SM -->|"3"| NUC
    SN -->|"4"| NUC
    NUC -->|"5"| BD
    SN -->|"6"| AVA
    SM -->|"7"| PAG
    APP -->|"8"| IDP
    PS -->|"9"| ASS
    NUC -->|"10"| ERP
    NUC -->|"11"| REG
```


A tabela traz os volumes registrados nos dados operacionais.

| Fato | Valor |
| --- | --- |
| Sessões simultâneas no pico, nos 30 minutos seguintes à abertura da matrícula | 5.800 |
| Matrículas confirmadas nesses 30 minutos | 2.400 |
| Sessões simultâneas em dia letivo comum | 640 |
| Lançamentos de nota exportados ao ambiente virtual em dia letivo comum | 4.800 |
| Lançamentos de nota exportados na janela de fechamento | até 360.000 |

1. Rotule cada relação numerada com o modo de comunicação, síncrono ou assíncrono, e com o volume e a latência exigidos, usando os fatos da tabela quando se aplicarem e escrevendo não informado quando o dossiê não trouxer o dado.

As relações rotuladas neste item são a lista de exigências de comunicação que a definição tecnológica da Aula 5 recebe como entrada.

### Item 2: Relações ligadas aos requisitos

Os dois requisitos abaixo, da página inicial do caso, fixam tempo de resposta e prazo de propagação para relações do diagrama do item 1.

| Código | Declaração |
| --- | --- |
| R6 | Percentil 95 do tempo de confirmação da matrícula em até 4 segundos, com 5.800 sessões simultâneas |
| R7 | Nota lançada pelo professor no ambiente virtual em até 10 minutos |

```mermaid
graph LR
    R6["R6, confirmação da matrícula em até 4 s no pico"]
    R7["R7, nota no ambiente virtual em até 10 min"]
    REL["Relações numeradas de 1 a 11 do item 1"]
    R6 -.->|"quais relações sustentam?"| REL
    R7 -.->|"quais relações sustentam?"| REL
```

1. Indique, pelo número, quais relações do diagrama do item 1 sustentam diretamente o requisito R6 e quais sustentam o requisito R7.

### Item 3: Núcleo transacional na arquitetura alvo

O núcleo transacional executa sob o monitor CICS em ambiente de grande porte no centro de dados da ACME, e as restrições abaixo constam da página inicial do caso e dos dados operacionais. O diagrama de implantação parcial, na notação C4 da seção [Diagrama de implantação em C4](#diagrama-de-implantacao-em-c4), mostra onde ficam o núcleo e os dois serviços novos que o chamam.

| Restrição | Origem |
| --- | --- |
| R10, a manutenção dos programas COBOL do núcleo permanece sob o contrato da fábrica até 30/09/2027 | Contrato de sustentação |
| A equipe interna não pode alterar o núcleo, mesmo para expor interfaces | Contrato de sustentação |
| R4, a solução opera em um dos dois provedores de nuvem aprovados em 12/03/2026 | Conselho Universitário |

```mermaid
%%{init: {"flowchart": {"curve": "stepAfter"}}}%%
flowchart TB
    subgraph NV["Nó: nuvem aprovada"]
        SM["«contêiner»<br/>Serviço de matrícula<br/>tecnologia a definir<br/>na Aula 5"]
        SN["«contêiner»<br/>Serviço de notas<br/>tecnologia a definir<br/>na Aula 5"]
    end
    subgraph DC["Nó: centro de dados"]
        subgraph MF["Nó: grande porte"]
            NUC["«contêiner»<br/>Núcleo transacional<br/>COBOL sob CICS"]
        end
    end
    SM -->|"relação 3<br/>conexão a definir"| NUC
    SN -->|"relação 4<br/>conexão a definir"| NUC
```

1. Responda, em uma frase, por que o núcleo transacional COBOL permanece como contêiner na arquitetura alvo do primeiro ciclo.

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seção 2.7, arquitetura de infraestrutura, objetivos, artefatos e relação com a solução, e seção 7.5, infraestrutura de rede e solução como grafo)
- Brown, S. (n.d.). *The C4 model for visualising software architecture*. https://c4model.com (diagrama de implantação, https://c4model.com/diagrams/deployment, escopo de um ambiente, nós de implantação aninhados, nós de infraestrutura, instâncias de contêiner e público técnico)
- Amazon Web Services. (n.d.-a). *Regions and zones*. Amazon EC2 User Guide. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html (definição de região e de zona de disponibilidade e distribuição de instâncias entre zonas)
- Amazon Web Services. (n.d.-b). *What is AWS Lambda?* AWS Lambda Developer Guide. https://docs.aws.amazon.com/lambda/latest/dg/welcome.html (computação sem servidor, infraestrutura gerenciada pelo provedor e limite de 15 minutos por invocação)
- Amazon Web Services. (n.d.-c). *What is Direct Connect?* AWS Direct Connect User Guide. https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html (ligação por fibra entre a rede interna e a AWS sem passar por provedores de internet)
- Microsoft. (2026). *Azure ExpressRoute overview: Connect over a private connection*. Microsoft Learn. https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction (conexão privada entre a rede local e a nuvem da Microsoft, que não passa pela internet pública)
- The Kubernetes Authors. (n.d.-a). *Nodes*. Kubernetes Documentation. https://kubernetes.io/docs/concepts/architecture/nodes/ (nó como máquina virtual ou física gerenciada pelo plano de controle, com os serviços necessários para executar pods)
- The Kubernetes Authors. (n.d.-b). *Pods*. Kubernetes Documentation. https://kubernetes.io/docs/concepts/workloads/pods/ (pod como menor unidade implantável, com um ou mais contêineres e rede e armazenamento compartilhados)

**Material do curso.** O bloco usa as entradas [arquitetura de infraestrutura](../referencia/glossario.md#arquitetura-de-infraestrutura), [modelo C4](../referencia/glossario.md#modelo-c4) e [bloco de construção da solução](../referencia/glossario.md#bloco-de-construcao-da-solucao) do glossário, além do dossiê da instituição fictícia [ACME](../caso-acme/index.md) e dos seus [dados operacionais](../caso-acme/dados-operacionais.md).
