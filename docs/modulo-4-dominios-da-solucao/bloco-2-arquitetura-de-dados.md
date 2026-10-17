# Arquitetura de dados da solução

Quando a nota ou o endereço de um aluno aparecem diferentes em dois sistemas, ninguém sabe qual versão vale. A arquitetura de dados da solução evita esse problema. Este é o segundo dos quatro domínios da Aula 4 e trata dos dados que sustentam a mudança localizada no bloco 1. Uma entidade é um tipo de coisa sobre a qual o sistema guarda dados, como aluno, turma ou nota. Para cada entidade, o bloco responde: o que a solução recebe da arquitetura de dados da organização, a quem ela pertence, onde é registrada com autoridade, com que atraso cada cópia pode refletir a mudança e quais obrigações o dado carrega.

## Antes de começar

- [Arquitetura de dados](../referencia/glossario.md#arquitetura-de-dados)
- [Modelo de dados corporativo](../referencia/glossario.md#modelo-de-dados-corporativo)
- [Fonte de verdade](../referencia/glossario.md#fonte-de-verdade)
- [Regime de consistência](../referencia/glossario.md#regime-de-consistencia)
- [Propriedade do dado](../referencia/glossario.md#propriedade-do-dado)
- [Dados mestres](../referencia/glossario.md#dados-mestres)
- Capacidades afetadas, a lista de capacidades marcadas como afetadas pelo primeiro ciclo no [exercício 13](bloco-1-arquitetura-de-negocio.md#exercicio-13)

## Dados na solução

<figure markdown="span">
![Mapa do bloco 0 com quatro faixas empilhadas, negócio, dados, aplicações e infraestrutura, e o que o arquiteto decide em cada uma, com a faixa de dados em destaque e as demais esmaecidas.](../assets/images/modulo-4-b0-mapa-dados.svg){ .module-diagram }
</figure>

No mapa do [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md), este bloco trata do domínio de dados. O arquiteto recebe as capacidades afetadas, localizadas no [bloco 1](bloco-1-arquitetura-de-negocio.md), e o modelo de dados corporativo. Para cada entidade, decide dono, fonte de verdade, regime de consistência e obrigações. A entrega ao bloco 3 é a grade dado × aplicação.

Como toda solução nova mexe em dados que a organização já gerencia, o arquiteto precisa de uma referência comum, e a DAMA International, associação profissional que mantém o corpo de conhecimento em gestão de dados conhecido como DMBOK (*Data Management Body of Knowledge*), define a **arquitetura de dados** como a estrutura geral dos dados e dos recursos relacionados a dados, tratada como parte integrante da arquitetura corporativa. A referência vigente é a segunda edição revisada do DMBOK, publicada em 2024 e disponível em português, e a terceira edição está prevista para 2027 (DAMA International, 2024). Toda solução tem uma arquitetura de dados própria, mais específica que a corporativa, e essa arquitetura precisa ser consistente com a arquitetura de dados da organização, porque a inconsistência na definição ou no uso do dado produz erro em serviço de negócio.

Na Universidade ACME, o cadastro do aluno aparece no núcleo acadêmico, no ERP financeiro e no ambiente virtual. Quando endereço e telefone divergem entre as cópias, a equipe precisa descobrir qual registro vale. O exemplo mostra por que o projeto identifica uma fonte oficial e define como atualizar cada consumidor. O exercício 14 aplica essa análise aos dados do dossiê.

A arquitetura de dados trata dado, informação e metadado num único domínio. Para o arquiteto de solução, o metadado aparece em forma concreta, como glossário de negócio, dicionário de dados, contrato de dados e registro de linhagem, e cada uma dessas formas é tratada nas seções seguintes.

### As áreas de gestão de dados

O DMBOK organiza a gestão de dados em onze áreas de conhecimento, coordenadas pela governança de dados, e a arquitetura de dados é uma delas. O arquiteto de solução pratica diretamente poucas dessas áreas, e cada uma delas entrega insumo ou impõe exigência à solução, como resume a tabela.

| Área do DMBOK | O que a solução recebe ou decide |
| --- | --- |
| Governança de dados | Quem decide sobre cada dado, inclusive qual sistema é o sistema de registro |
| Arquitetura de dados | Modelo de dados corporativo, panorama de dados e princípios |
| Modelagem e design de dados | Modelos lógico e físico da própria solução |
| Armazenamento e operações | Banco, cópias, retenção e recuperação |
| Segurança de dados | Classificação, controle de acesso e trilha de auditoria |
| Integração e interoperabilidade | Fluxos entre sistemas, por interface, evento ou lote |
| Dados mestres e de referência | Entidades compartilhadas, como aluno, professor ou disciplina |
| Data warehousing e inteligência de negócio | Destino analítico das cópias derivadas |
| Metadados | Glossário, dicionário, contrato e linhagem |
| Qualidade de dados | Dimensões de qualidade convertidas em requisito mensurável |
| Documentos e conteúdo | Dado não estruturado, como históricos escolares e contratos digitalizados |

A interação entre as áreas ocorre pelos processos de governança. Um exemplo dado pela própria DAMA é a governança de dados mestres e de referência, que inclui determinar o sistema de registro de cada dado e as regras de negócio que se aplicam a ele (DAMA Denmark, 2020), decisão que este bloco trata como fonte de verdade.

### Modelo de dados corporativo

Antes de propor qualquer entidade nova, o arquiteto verifica o que a organização já modelou, e esse acervo é o **modelo de dados corporativo**, que reúne modelos de perspectivas e níveis de detalhe diferentes, que descrevem de forma consistente o entendimento da organização sobre entidades, atributos e relacionamentos. O DMBOK o organiza em quatro níveis, a visão conceitual com as áreas de assunto da organização, a visão de cada área de assunto com suas entidades e relacionamentos, o modelo lógico corporativo com entidades parcialmente atribuídas, e os modelos lógicos e físicos específicos de cada aplicação ou projeto (DAMA Rocky Mountain Chapter, 2023). O mapeamento entre níveis permite seguir uma entidade de cima a baixo, e a mesma entidade presente em modelos do mesmo nível liga esses modelos entre si.

A distinção entre os níveis de modelagem orienta o que o arquiteto de solução lê e o que ele decide. O modelo conceitual registra conceitos de negócio e seus relacionamentos, sem atributo técnico, o modelo lógico acrescenta atributos e chaves, ainda independente de tecnologia, e o modelo físico traduz o lógico em tabelas, tipos e índices de um gerenciador de banco específico, como o PostgreSQL.

<figure markdown="span">
![Modelo de dados acadêmicos em quatro níveis: áreas de assunto, entidades aluno, disciplina, matrícula e nota, atributos da nota e modelo físico e contrato de mensagem produzidos pelo projeto.](../assets/images/modulo-4-b2-modelo-corporativo.svg){ .module-diagram }
</figure>

*Figura 1 — Modelo de dados corporativo em quatro níveis, com o recorte que entra na solução e o que a solução produz. Fonte: material do curso, com base em DAMA Rocky Mountain Chapter (2023).*

A Figura 1 aplica os quatro níveis à publicação de notas da Universidade ACME. A área de assunto é a vida acadêmica. As entidades incluem aluno, disciplina, matrícula e nota. O modelo lógico detalha os atributos e relacionamentos dessas entidades. O projeto produz o modelo físico do serviço e o contrato da mensagem de nota, enquanto a escolha do banco é feita na Aula 5. Uma entidade aparentemente nova deve ser comparada às definições existentes antes de receber outro nome.

### Panorama de dados e linhagem

A edição revisada do DMBOK substituiu o conceito de desenho de fluxo de dados pelo de **panorama de dados** (*data landscape*), que descreve onde cada dado reside e como circula entre aplicações (DAMA International, n.d.). Na formulação da edição de 2017, os fluxos de dados relacionam o dado às aplicações dentro de um processo de negócio, aos repositórios em que ele é armazenado, aos segmentos de rede, aos papéis de negócio responsáveis por criar, atualizar, usar e excluir o dado, e às localidades, e constituem um tipo de documentação de linhagem (Steenbeek, 2017).

Para a solução, o panorama assume duas formas. A primeira é a grade dado × aplicação, uma matriz que cruza entidades com as aplicações que as gravam, leem ou recebem, e que torna visível, na análise de impacto, quais componentes são atingidos por uma mudança numa entidade. A segunda é o diagrama de fluxo entre sistemas, que mostra o sentido, o meio e o horário de cada troca, como os diagramas de integração do [bloco 3](bloco-3-arquitetura-de-aplicacoes-e-integracao.md).

<figure markdown="span">
![Grade genérica que cruza três entidades, cliente, pedido e fatura, com três aplicações, loja virtual, logística e faturamento. Cada célula indica se a aplicação grava, lê por interface ou recebe por evento. Uma coluna destacada indica o dono de cada entidade e outra coluna indica o regime de consistência de cada consumidor, forte ou eventual com prazo de dez minutos.](../assets/images/modulo-4-grade-dado-aplicacao.svg){ .module-diagram }
</figure>

*Figura 2 — Grade dado × aplicação com dono, consumidores e regime de consistência. Fonte: material do curso, com base em Lovatt (2021).*

A **linhagem de dados** registra de onde cada conjunto de dados veio e por quais transformações passou, e permite responder, diante de um número errado num relatório, qual origem e qual processamento o produziram. O OpenLineage, projeto da LF AI & Data Foundation, padroniza a coleta desse registro com três entidades, a execução (*run*), o trabalho (*job*) e o conjunto de dados (*dataset*), e o Marquez é sua implementação de referência (OpenLineage, n.d.).

### Fonte de verdade e regime de consistência

Uma cópia não se torna fonte de verdade por ser a mais acessível. O esquema separa quem responde pelo dado, onde ele é gravado com autoridade, quem o consome e qual prazo de atualização foi combinado.

```mermaid
flowchart LR
    R["Responsável de negócio"] -->|"define regras"| F["Fonte de verdade"]
    A["Aplicação dona"] -->|"grava com autoridade"| F
    F -->|"propaga no prazo acordado"| C1["Consumidor 1"]
    F -->|"propaga no prazo acordado"| C2["Consumidor 2"]
    F -.->|"controle de acesso e auditoria"| G["Obrigações do dado"]
```

Quando um dado existe em vários lugares, é preciso saber qual deles manda. Kleppmann (2017) distingue, para isso, dois tipos de sistema que guardam dado: o sistema de registro, que guarda a versão autoritativa e em que o dado é escrito primeiro, e o sistema de dado derivado, que guarda dado transformado ou processado a partir do sistema de registro, como um cache, um índice de busca ou uma base analítica, e pode ser reconstruído a partir da origem. Nesta disciplina, o termo **fonte de verdade** designa o lugar em que a entidade é registrada com autoridade, e toda outra ocorrência da entidade é cópia derivada.

O sistema de registro costuma ser um banco relacional com transação ACID, sigla de atomicidade, consistência, isolamento e durabilidade, como o PostgreSQL ou o Oracle, e o gerenciador anota cada mudança confirmada num log de transações, que no PostgreSQL se chama write-ahead log. As cópias derivadas mais comuns cumprem papéis distintos.

- A réplica de leitura é uma cópia do próprio banco, alimentada pelo log de transações do servidor primário, que atende consultas e reduz a carga sobre ele.
- O cache, como o Redis, guarda em memória o resultado de leituras frequentes para reduzir o tempo de resposta.
- O índice de busca, como o OpenSearch, reorganiza o dado para consultas por texto livre e por combinações de filtros.
- O data warehouse, como o BigQuery, o Snowflake ou o Redshift, guarda o dado em armazenamento colunar para consultas analíticas sobre grande volume histórico.

A captura de mudanças de dados, conhecida pela sigla CDC, propaga cada alteração confirmada no sistema de registro para as cópias. O Debezium é um conjunto de conectores de origem para o Kafka Connect que lê o log de transações do banco, no PostgreSQL por meio da decodificação lógica do write-ahead log, e emite um evento para cada inserção, atualização e exclusão de linha (Debezium, n.d.-a, n.d.-b). Por padrão, os eventos de cada tabela vão para um tópico próprio do Apache Kafka, que retém as mensagens em ordem dentro de cada partição e permite que cada consumidor leia no próprio ritmo.

<figure markdown="span">
![Fluxo em que a aplicação grava em transação no PostgreSQL, sistema de registro, que alimenta uma réplica de leitura. O Debezium lê o log de transações e publica eventos no Apache Kafka, de onde o cache Redis, o índice OpenSearch e o data warehouse recebem as mudanças, cada um com regime eventual e prazo declarado.](../assets/images/modulo-4-b2-fonte-de-verdade-copias.svg){ .module-diagram }
</figure>

*Figura 3 — Fonte de verdade e cópias derivadas alimentadas por captura de mudanças e por eventos. Fonte: material do curso, com base em Kleppmann (2017) e Debezium (n.d.-a).*

Saber qual é a fonte não basta, porque cada consumidor lê a entidade num momento diferente. Por isso cada consumidor precisa de um **regime de consistência** declarado, que diz quando a leitura feita na fonte ou numa cópia reflete a fonte de verdade. O regime é forte quando a leitura reflete a fonte imediatamente, o que exige ler da própria fonte de verdade ou de cópia atualizada de forma síncrona, e eventual quando reflete dentro de um prazo declarado, por exemplo cinco minutos ou um dia. Um regime eventual sem prazo declarado não pode ser verificado, e por isso não é aceito como decisão. A Figura 4 coloca os dois regimes na mesma linha do tempo, com a nota da Universidade ACME gravada no núcleo acadêmico e copiada para o ambiente virtual.

```mermaid
sequenceDiagram
    participant AP as Serviço de integração
    participant SR as Núcleo acadêmico, sistema de registro
    participant CD as Ambiente virtual, cópia derivada
    rect rgb(216, 233, 255)
    Note over AP,SR: Consistência forte
    AP->>SR: 1. grava o nota em transação
    SR-->>AP: 2. transação confirmada
    AP->>SR: 3. lê o registro acadêmico
    SR-->>AP: 4. devolve o registro com a nota
    end
    rect rgb(255, 244, 221)
    Note over AP,CD: Consistência eventual com prazo de dez minutos
    AP->>CD: 5. lê as pendências logo após a confirmação
    CD-->>AP: 6. devolve o registro ainda sem a nota, dentro do prazo
    SR-)CD: 7. evento de mudança chega pela captura de mudanças
    Note over CD: cópia atualizada antes do fim do prazo
    AP->>CD: 8. lê as pendências de novo
    CD-->>AP: 9. devolve o registro com a nota
    end
```

*Figura 4 — Consistência forte e consistência eventual com prazo declarado. Fonte: material do curso, com base em Kleppmann (2017).*

Os produtos citados neste bloco são exemplos de cada categoria, e a escolha de banco, cache, índice, barramento e data warehouse para a ACME pertence à Aula 5.

### Dados mestres e de referência

Algumas entidades, como o aluno, aparecem em várias aplicações ao mesmo tempo, e a gestão delas tem nome próprio. **Dados mestres** são as entidades de negócio compartilhadas por várias aplicações, como aluno, professor ou fornecedor, e dados de referência são os conjuntos de valores que classificam outros dados, como a tabela de países, de moedas ou de códigos de disciplina. O DMBOK define a gestão dessa área como a gestão do dado compartilhado para reduzir redundância e garantir melhor qualidade (DAMA Denmark, 2020). O cadastro do aluno exemplifica esse problema quando endereço e telefone divergem entre o núcleo e suas cópias.

As soluções de gestão de dados mestres seguem quatro estilos de implementação, que se distinguem pelo lugar em que a escrita ocorre e pelo papel do repositório central, chamado *hub* (Carr, 2026).

| Estilo | Onde a escrita ocorre | Papel do hub |
| --- | --- | --- |
| Registro | Nos sistemas de origem | Guarda apenas o identificador global e as ligações entre os registros, sem devolver dado às origens |
| Consolidação | Nos sistemas de origem | Reúne as cópias num registro consolidado, usado para leitura e análise |
| Coexistência | Nos sistemas de origem e no hub | Sincroniza o registro consolidado de volta para as origens |
| Centralizado | No hub | É o sistema de registro, e as aplicações gravam e leem por ele |

Para a solução, o estilo escolhido define a fonte de verdade da entidade mestre e, portanto, o dono e os contratos que a expõem. Na Universidade ACME, um índice de identificação ajudaria a reconhecer o mesmo aluno nos sistemas. Para impedir que endereço e telefone voltem a divergir, é preciso também definir onde a alteração é feita e como chega às cópias. O gabarito do exercício 14 propõe escrita centralizada no cadastro acadêmico.

### Propriedade do dado

Para evitar que duas aplicações alterem a mesma entidade, a **propriedade do dado** atribui cada entidade a um único responsável, que é a parte autorizada a gravá-la. As demais partes leem a entidade pela interface que o responsável oferece ou a recebem por evento publicado por ele. Dehghani (2022) aplica o mesmo princípio ao dado analítico, atribuindo a propriedade ao domínio de negócio mais próximo da origem do dado, como um dos quatro princípios da malha de dados (*data mesh*).

O banco compartilhado entre aplicações contraria a propriedade do dado. Quando duas aplicações leem e gravam as mesmas tabelas, cada mudança de estrutura passa a exigir alteração coordenada em dois códigos-fonte, frequentemente mantidos por equipes distintas, e nenhuma das duas pode evoluir o modelo de dados sem a outra. A forma técnica mais comum da propriedade do dado é a prática de um banco por serviço, em que o dado persistente de cada serviço é privado e acessível apenas pela interface desse serviço (Richardson, n.d.). Os consumidores leem pela interface ou recebem os eventos que o dono publica no Kafka, no estilo da [arquitetura orientada a eventos](../modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md#arquitetura-orientada-a-eventos) apresentada na Aula 3, e dependem só do contrato, que o dono mantém estável enquanto altera o esquema interno.

<figure markdown="span">
![Dois painéis. À esquerda, as aplicações de agenda e de comunicação leem e gravam as mesmas tabelas num banco único, com o acoplamento destacado no esquema. À direita, o serviço de agenda é dono da consulta, tem banco próprio, oferece interface e publica o evento consulta agendada, e o acoplamento fica restrito ao contrato.](../assets/images/modulo-4-b2-banco-por-servico.svg){ .module-diagram }
</figure>

*Figura 5 — Banco compartilhado comparado com um dono por entidade. Fonte: material do curso, com base em Richardson (n.d.) e Dehghani (2022).*

Quando o dono publica um conjunto de dados, o consumidor precisa saber o que pode esperar dele, e o **contrato de dados** formaliza o que o dono garante. O Open Data Contract Standard (ODCS), mantido pelo projeto Bitol na LF AI & Data Foundation, descreve o contrato num arquivo YAML com seções para esquema, regras de qualidade, acordo de nível de serviço, papéis e servidores, e está na versão 3.2.0, publicada em setembro de 2026 (Bitol, 2026). A prática é recente, e o [contrato de integração](bloco-3-arquitetura-de-aplicacoes-e-integracao.md) do bloco 3 cumpre a mesma função para as interfaces entre aplicações.

### Requisitos de dados: qualidade e proteção

A qualidade de dados entra na solução como requisito mensurável. A edição revisada do DMBOK lista nove dimensões de qualidade, exatidão, validade, completude, integridade, unicidade, tempestividade, razoabilidade, consistência e atualidade (*currency*), esta última incluída na revisão (DAMA International, n.d.). Cada dimensão relevante recebe métrica e limite, como no requisito que exige o endereço do aluno confirmado nos últimos 12 meses, que é um requisito de atualidade.

Quando a solução guarda dados do aluno, como a cor ou raça autodeclarada, a Lei Geral de Proteção de Dados Pessoais, Lei nº 13.709/2018, impõe a ela exigências que o arquiteto precisa traduzir em decisão de dados (Brasil, 2018).

| Exigência | Dispositivo da LGPD | Decisão de dados na solução |
| --- | --- | --- |
| Distinguir dado pessoal de dado pessoal sensível, que inclui dado referente à saúde, origem racial ou étnica e dado biométrico | Art. 5º, I e II | Classificar cada atributo e aplicar controle mais estrito ao sensível |
| Limitar o tratamento ao mínimo necessário para a finalidade | Art. 6º, III | Não copiar atributo pessoal para destino que não precisa dele |
| Eliminar o dado após o término do tratamento, com conservação autorizada para obrigação legal ou regulatória, entre outras hipóteses | Arts. 15 e 16 | Declarar retenção e rotina de eliminação por entidade, inclusive nas cópias derivadas |
| Manter registro das operações de tratamento | Art. 37 | Trilha de auditoria e linhagem do dado pessoal |
| Observar as medidas de segurança desde a concepção do produto ou serviço | Art. 46, § 2º | Incluir classificação e proteção no desenho da solução |
| Restringir a transferência internacional a hipóteses como país com proteção adequada ou cláusulas contratuais | Art. 33 | Verificar a região de cada serviço gerenciado e de cada cópia |

A LGPD se aplica independentemente do país em que os dados estejam localizados (art. 3º) e não exige que o dado permaneça no território nacional. A exigência de processamento no Brasil, quando existe, decorre de decisão da organização ou de contrato, e entra na solução como restrição registrada.

### Dado operacional e dado analítico

A mesma entidade serve a dois usos, o de atender à transação do dia e o de responder a perguntas sobre o histórico. O dado operacional registra o estado corrente do negócio e atende às transações das aplicações, enquanto o dado analítico reúne fatos históricos e agregados para análise. As arquiteturas analíticas mais citadas são o data warehouse em modelagem dimensional, com tabelas de fatos e de dimensões organizadas em esquema estrela (Kimball Group, n.d.), o data lake, que guarda o dado bruto na forma em que a origem o fornece (Fowler, 2015), e o lakehouse, que oferece sobre formatos abertos de arquivo as funções de gestão de dados de um data warehouse e evita manter as duas camadas separadas (Armbrust et al., 2021). No lakehouse, a arquitetura medallion organiza os dados em três camadas, bronze com o dado bruto, prata com o dado limpo e conciliado e ouro com o dado pronto para consumo (Databricks, n.d.).

```mermaid
flowchart TB
    subgraph L1[" "]
        direction LR
        PG[("PostgreSQL<br/>sistema de registro")] -->|"log de transações"| DBZ["Debezium"] --> KF["Kafka"]
    end
    subgraph L2[" "]
        direction LR
        BR["Bronze<br/>dado bruto"] --> PR["Prata<br/>dado limpo e conciliado"] --> OU["Ouro<br/>dado pronto para consumo"] --> BI["Painéis<br/>e relatórios"]
    end
    L1 --> L2
    style L1 fill:none,stroke:none
    style L2 fill:none,stroke:none
```

*Figura 6 — Caminho do dado operacional ao analítico, com captura de mudanças e camadas da arquitetura medallion. Fonte: material do curso, com base em Debezium (n.d.-a) e Databricks (n.d.).*

Para o arquiteto de solução, a escolha da plataforma analítica pertence em geral à arquitetura corporativa. A solução decide como o dado operacional chega a essa plataforma, com que regime de consistência e com quais atributos pessoais removidos ou pseudonimizados.

## Uso pelo arquiteto

A pergunta do arquiteto neste domínio, no roteiro do [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md), é a seguinte. Que entidades sustentam as capacidades afetadas, quem é o dono de cada uma, onde fica a fonte de verdade, com que regime cada cópia a reflete e que obrigações o dado carrega?

O arquiteto da ACME precisa saber o que mais é atingido quando uma entidade muda e quem responde por ela. Ele recebe da arquitetura de dados corporativa o recorte do modelo corporativo na zona de impacto e monta a grade dado × aplicação, que cruza cada entidade com as aplicações que a gravam ou a leem. A grade localiza o impacto de mudar uma entidade e revela as entidades sem dono declarado ou gravadas por mais de uma aplicação, que são as que exigem decisão. Para cada entidade ele registra o dono, a fonte de verdade, o estilo de dado mestre quando a entidade é compartilhada, o regime de consistência de cada consumidor e as obrigações de qualidade e de proteção, e devolve ao modelo corporativo a diferença que a solução cria. Em seguida leva o registro ao domínio de aplicações, porque o dono de cada entidade é a origem natural das interfaces que a expõem no [bloco 3](bloco-3-arquitetura-de-aplicacoes-e-integracao.md), e o regime de consistência de cada consumidor é a exigência que o [contrato de integração](../referencia/glossario.md#contrato-de-integracao) precisa garantir. Sem a grade, duas aplicações continuam gravando a mesma entidade e o contrato de integração é escrito sobre uma fonte de verdade indefinida.

## No caderno arquitetural

{{ficha:7:4}}

**Para que serve.** Na seção 7 do caderno, as decisões sobre dados dizem quem responde por cada informação da universidade e quanto atraso cada cópia pode ter. Sem elas, duas aplicações gravam a mesma tabela, ninguém sabe qual versão vale, e o aluno descobre o problema quando a nota ou o endereço aparecem diferentes em dois sistemas. Registrar o dono, o prazo e as obrigações de cada entidade permite que o bloco seguinte desenhe interfaces que garantem o que o caderno promete.

**O que você faz neste exercício.** O enunciado traz cinco entidades acadêmicas, aluno, matrícula, nota, lançamento financeiro e turma, numa grade que mostra quais aplicações as gravam ou as recebem. Em cinco itens você escolhe o dono de cada entidade, o prazo de cada cópia, o estilo do cadastro único do aluno e as obrigações da LGPD sobre os dados dele, e explica por que o acesso direto ao banco é um problema. As respostas entram no caderno na parte Dados: dono, consistência e proteção.

| Campo do caderno | Como preencher | Item |
| --- | --- | --- |
| Dono da entidade | Marque, para cada uma das cinco entidades, a aplicação ou o elemento do esboço lógico do exercício 9 que passa a ser o único autorizado a gravá-la | 1 |
| Justificativa do dono | Escreva uma linha por entidade, citando a capacidade afetada do exercício 13 que ela sustenta | 1 |
| Regime de consistência | Para cada consumidor de cada entidade, diga se a leitura precisa refletir a gravação na hora (forte) ou dentro de um prazo (eventual, com o prazo escrito) | 2 |
| Estilo de dado mestre do aluno | Escolha entre registro, consolidação, coexistência e centralizado para o cadastro único do aluno | 3 |
| Registro da escolha do dado mestre | Escreva em três linhas o contexto, a decisão e uma consequência da escolha | 3 |
| Classificação dos atributos | Diga, para cada um dos seis atributos do aluno, se é dado pessoal ou dado pessoal sensível | 4 |
| Destino com excesso de dado | Indique o destino que recebe mais atributos do que a finalidade exige | 4 |
| Hipótese de conservação e origem do R14 | Diga qual hipótese do art. 16 da LGPD autoriza guardar o histórico dos egressos e se o R14 vem da lei ou de decisão da instituição | 4 |
| Motivo contra o acesso direto ao banco | Explique em até três linhas por que os 2.300 acessos diretos contrariam a propriedade do dado | 5 |

**O que você já tem.** As capacidades afetadas do exercício 13, o esboço lógico do exercício 9 e os requisitos R6, R7, R9 e R14, reproduzidos no enunciado.

**Quando está pronto.** As cinco entidades têm dono e justificativa, cada consumidor tem regime com prazo, o aluno tem estilo de dado mestre com o registro de três linhas, os seis atributos estão classificados e o motivo contra o acesso direto ao banco está escrito.

[Ver esta seção no template](../caderno/template.md#7-decisoes){ .caderno-botao }
[Ver o gabarito do exercício 14](../gabaritos/gabarito-exercicio-14.md){ .caderno-botao }

{{/ficha}}

## Exercício 14

O exercício 14 aplica à ACME as decisões de dados deste bloco. A ACME é uma universidade privada brasileira fictícia, com 38.400 alunos ativos e sistema acadêmico em operação desde 2004. O enunciado traz cinco entidades acadêmicas, que são aluno, matrícula, nota, lançamento financeiro e turma, numa grade que cruza cada uma com as aplicações que a gravam, leem ou recebem. Cada um dos cinco itens pede uma decisão sobre essas entidades, do dono ao tratamento do dado pessoal. As decisões servem para que, na arquitetura alvo, que é a forma que a solução terá ao fim do primeiro ciclo, cada dado tenha um responsável claro e cada cópia tenha um atraso aceito, antes de o bloco 3 definir as interfaces.

O exercício usa três produtos anteriores. Do [exercício 13](bloco-1-arquitetura-de-negocio.md#exercicio-13), vêm as [capacidades](../referencia/glossario.md#capacidade) marcadas como afetadas, entre as dez capacidades acadêmicas do mapa daquele exercício. Do [exercício 9](../modulo-3-design-e-padroes/bloco-1-principios-de-design.md#exercicio-9), vem o esboço lógico, que agrupou as oito responsabilidades da solução em poucos elementos e distribuiu essas responsabilidades entre eles. Da [arquitetura de linha de base](../caso-acme/linha-de-base.md) e da [página inicial do caso](../caso-acme/index.md), vêm os fatos reproduzidos em cada item.

### Item 1: Dono de cada entidade

Na linha de base da ACME, o núcleo transacional e os portais Java gravam as mesmas entidades, e por isso o primeiro passo é decidir quem responde por cada uma das cinco. Dono de uma entidade é a aplicação ou o elemento com autorização exclusiva para gravá-la, e as demais partes apenas leem a entidade ou recebem cópia dela. A grade dado × aplicação abaixo foi montada pelo material do curso a partir da linha de base e não traz a coluna de dono, que é a resposta do item. As colunas são as aplicações do sistema atual. O núcleo transacional é o sistema central da ACME, escrito em COBOL, em que ficam as regras acadêmicas. Os portais Java são os quatro portais web, do aluno, do professor, da secretaria e do gestor. O ERP financeiro é o sistema de gestão financeira, o ambiente virtual é a plataforma de ensino a distância, e o data warehouse é a base que reúne cópias dos dados para relatórios e análises. Uma célula como "Recebe por lote às 04h00" indica uma cópia enviada por arquivo, de forma automática, naquele horário da madrugada.

| Entidade | Núcleo transacional | Portais Java | ERP financeiro | Ambiente virtual | Data warehouse |
| --- | --- | --- | --- | --- | --- |
| Aluno | Grava | Lê ou grava, por conector e por acesso direto ao banco, sem distribuição registrada por entidade | Recebe por lote às 23h10, como pagador do lançamento | Recebe por lote às 04h00, vinculado à turma | Recebe por lote às 02h30 |
| Matrícula | Grava | Lê ou grava, por conector e por acesso direto ao banco, sem distribuição registrada por entidade | Não registrado | Recebe por lote às 04h00 | Recebe por lote às 02h30 |
| Nota | Grava a nota consolidada | Lê ou grava, por conector e por acesso direto ao banco, sem distribuição registrada por entidade | Não registrado | Recebe por lote às 05h10 e devolve nota de atividade às 06h15 | Recebe por lote às 02h30 |
| Lançamento financeiro | Grava | Lê ou grava, por conector e por acesso direto ao banco, sem distribuição registrada por entidade | Recebe por lote às 23h10 e devolve baixa às 05h30 | Não registrado | Recebe por lote às 02h30 |
| Turma | Grava | Lê ou grava, por conector e por acesso direto ao banco, sem distribuição registrada por entidade | Não registrado | Recebe por lote às 04h00 | Recebe por lote às 02h30 |

1. Marque, para cada uma das cinco entidades, a aplicação ou o elemento do esboço lógico do exercício 9 que deve ser o dono na arquitetura alvo.
2. Justifique cada marcação em uma linha, citando a capacidade afetada do exercício 13 que a entidade sustenta.

Suas respostas viram os campos Dono da entidade e Justificativa do dono, na seção 7 do caderno.

O dono marcado para a entidade nota é a origem do contrato de integração do exercício 15, no [bloco 3](bloco-3-arquitetura-de-aplicacoes-e-integracao.md), em que esse dono passa a ser a aplicação que envia a nota ao ambiente virtual.

### Item 2: Regime de consistência por consumidor

Quando o professor lança uma nota às 15h00, o aluno só a enxerga no ambiente virtual às 06h00 do dia seguinte, e esse atraso é o que o regime de consistência declara, isto é, o atraso aceito entre a gravação da entidade na fonte de verdade e o momento em que o consumidor a enxerga. Consumidor é toda aplicação que lê ou recebe uma entidade, como as colunas da grade do item 1. O regime é forte quando a leitura reflete a gravação na hora, e eventual quando reflete dentro de um prazo declarado, como 10 minutos. Este item decide o regime de cada consumidor para cada entidade. Hoje toda troca com o ERP financeiro e com o ambiente virtual de aprendizagem ocorre por arquivo, em lote noturno, e o data warehouse recebe uma extração diária. O diagrama mostra o sentido e o horário de cada um dos seis lotes da linha de base.

```mermaid
graph LR
    ACA["Sistema acadêmico da ACME"]
    ERP["ERP financeiro"]
    AVA["Ambiente virtual de aprendizagem"]
    DW["Data warehouse"]

    ACA -->|"23h10 lançamentos financeiros"| ERP
    ERP -->|"05h30 baixas de pagamento"| ACA
    ACA -->|"02h30 cópia de 140 tabelas"| DW
    ACA -->|"04h00 turmas e matrículas"| AVA
    ACA -->|"05h10 notas consolidadas"| AVA
    AVA -->|"06h15 notas e frequência de atividades"| ACA
```

Dois requisitos do caso, reproduzidos na tabela abaixo, afetam o regime de consistência. O R7, pedido pela Educação a Distância, define o prazo de propagação da nota até o ambiente virtual. O R6, da Diretoria de TI, exige tempo de resposta do sistema de registro durante a matrícula, o que interessa à decisão de o consumidor ler a fonte com consistência forte. O percentil 95 do R6 é o valor abaixo do qual ficam 95% das respostas.

| Código | Declaração |
| --- | --- |
| R6 | O portal sustenta 5.800 sessões simultâneas na abertura da matrícula, com percentil 95 do tempo de confirmação em até 4 segundos |
| R7 | A nota lançada pelo professor chega ao ambiente virtual de aprendizagem em até 10 minutos |

1. Marque, para cada consumidor de cada entidade na grade do item 1, o regime de consistência exigido, forte ou eventual com o prazo, usando o R7 como prazo de propagação da nota e o R6 como exigência de tempo de resposta para os consumidores que leem a fonte com consistência forte durante a matrícula. Registre o resultado numa tabela com as mesmas linhas e colunas da grade.

Sua resposta vira o campo Regime de consistência, na seção 7 do caderno.

### Item 3: Estilo de dado mestre para o aluno

O aluno consta do cadastro acadêmico, do ambiente virtual, do ERP financeiro e do data warehouse, e cada cópia pode divergir das outras. Para evitar a divergência, a ACME escolhe um estilo de dado mestre, que define onde a escrita ocorre e qual papel o repositório central tem, conforme a tabela de quatro estilos da seção Dados mestres e de referência. Este item escolhe o estilo para manter um cadastro único de aluno entre as aplicações. O aluno é a entidade compartilhada da ACME, com 38.400 alunos ativos e 214.000 egressos, que são ex-alunos cujos dados a instituição ainda retém. O cadastro acadêmico grava o aluno, e as demais aplicações recebem ou mantêm cópia dele, como mostra o diagrama. A seta tracejada indica uma relação prevista na arquitetura alvo, a do aplicativo do aluno, que atualiza endereço e telefone e ainda não existe.

```mermaid
graph LR
    CAD[("Cadastro acadêmico, alunos ativos e egressos")]
    CAD -->|"04h00, aluno vinculado à turma"| AVA["Ambiente virtual, usuário do aluno"]
    CAD -->|"23h10, aluno como pagador do lançamento"| ERP["ERP financeiro, responsável financeiro"]
    CAD -->|"02h30, cópia integral"| DW["Data warehouse"]
    APP["Aplicativo do aluno, arquitetura alvo"] -.->|"atualiza endereço e telefone"| CAD
```

1. Escolha o estilo de dado mestre, registro, consolidação, coexistência ou centralizado, para a entidade aluno na arquitetura alvo.
2. Registre a escolha em três linhas, com o contexto, a decisão e uma consequência, como os campos correspondentes do ADR, o registro de decisão arquitetural apresentado no [bloco 4 da Aula 3](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md).

Suas respostas viram os campos Estilo de dado mestre do aluno e Registro da escolha do dado mestre, na seção 7 do caderno.

### Item 4: Obrigações do dado pessoal do aluno

O data warehouse da ACME recebe cópia dos seis atributos da tabela abaixo, e a LGPD, a Lei Geral de Proteção de Dados Pessoais, obriga a perguntar se cada cópia é necessária. Este item traduz a LGPD em obrigações sobre os dados do aluno. Dado pessoal é a informação relacionada a uma pessoa identificada ou identificável, e dado pessoal sensível é a categoria que exige controle mais estrito, como o dado sobre saúde ou sobre origem racial ou étnica, conforme a tabela da seção Requisitos de dados. A tabela abaixo, montada pelo material do curso a partir da linha de base, lista seis atributos do aluno usados pela ACME e os destinos, isto é, os sistemas que recebem cópia de cada atributo. A cor ou raça autodeclarada e a condição de deficiência são coletadas para a extração anual do censo da educação superior.

| Atributo | Destinos na linha de base |
| --- | --- |
| Nome e CPF | Ambiente virtual, ERP financeiro e data warehouse |
| Endereço e telefone | ERP financeiro e data warehouse |
| Nota e situação por disciplina | Ambiente virtual e data warehouse |
| Cor ou raça autodeclarada | Data warehouse |
| Condição de deficiência | Data warehouse |
| Histórico escolar de egresso, 214.000 registros | Data warehouse |

O caso também registra dois requisitos sobre o dado pessoal. O R9, declarado pela Encarregada de proteção de dados, papel da área Jurídica que responde pela conformidade da ACME com a LGPD, exige trilha de auditoria de toda leitura de dado pessoal de aluno, isto é, um registro de cada leitura, guardado por 5 anos. A encarregada pediu essa trilha para ter conformidade com a LGPD e base legal declarada, e o dossiê não informa de onde vem o prazo de 5 anos. O R14, do Jurídico, proíbe processar dado pessoal de aluno fora do território nacional. Ele se apoia num parecer do Jurídico de 28/04/2026, que o dossiê cita sem reproduzir o conteúdo, e responde ao receio da encarregada de que dado de aluno seja transferido para o exterior sem amparo.

1. Classifique cada atributo como dado pessoal ou dado pessoal sensível, conforme o art. 5º da LGPD.
2. Indique um destino que recebe atributo além do necessário para a finalidade, conforme o princípio da necessidade, segundo o qual o tratamento se limita ao mínimo necessário (art. 6º, III).
3. Indique qual hipótese do art. 16 da LGPD autoriza a ACME a conservar os históricos de egressos e se o R14 decorre da LGPD ou de decisão da instituição.

Suas respostas viram os campos Classificação dos atributos, Destino com excesso de dado e Hipótese de conservação e origem do R14, na seção 7 do caderno.

### Item 5: Acesso direto ao banco

Na ACME, o banco Oracle de 740 tabelas é usado ao mesmo tempo pelo núcleo COBOL e pelos portais, e este item pede que o aluno explique, com esse caso real, o problema do banco compartilhado descrito na seção sobre propriedade do dado, segundo a qual cada entidade tem um único responsável autorizado a gravá-la. O banco é compartilhado entre o núcleo COBOL e a camada Java, que reúne os quatro portais web, sem separação de esquema por responsabilidade. O caminho normal dos portais é chamar as transações do núcleo, que o monitor CICS recebe e processa e nas quais ficam as regras acadêmicas. Em 2.300 pontos do código Java, porém, os portais leem ou gravam as tabelas do núcleo diretamente, contornando essas transações, e o inventário não registra a distribuição desses pontos por entidade.

```mermaid
graph TD
    PJ["Portais Java"]
    NUC["Núcleo transacional"]
    BD[("Banco Oracle com 740 tabelas")]

    PJ -->|"chama por conector transacional"| NUC
    NUC -->|"lê e grava pelas transações do núcleo"| BD
    PJ -->|"lê e grava diretamente em 2.300 pontos do código"| BD
```

1. Responda, em até três linhas, por que os 2.300 acessos diretos ao banco contrariam a propriedade do dado.

Sua resposta vira o campo Motivo contra o acesso direto ao banco, na seção 7 do caderno.

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Armbrust, M., Ghodsi, A., Xin, R., & Zaharia, M. (2021). Lakehouse: A new generation of open platforms that unify data warehousing and advanced analytics. *Conference on Innovative Data Systems Research (CIDR '21)*. https://www.cidrdb.org/cidr2021/papers/cidr2021_paper17.pdf (definição de lakehouse e crítica à arquitetura de duas camadas)
- Bitol. (2026). *Open Data Contract Standard* (Versão 3.2.0). LF AI & Data Foundation. https://bitol-io.github.io/open-data-contract-standard/latest/ (estrutura do contrato de dados)
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD)*. https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm (arts. 3º, 5º, 6º, 15, 16, 33, 37 e 46)
- Carr, A. (2026). *4 common master data management implementation styles*. Stibo Systems. https://www.stibosystems.com/blog/4-common-master-data-management-implementation-styles (estilos de registro, consolidação, coexistência e centralizado)
- DAMA Denmark. (2020). *Data management body of knowledge: Overview of the DMBOK2* [Apresentação]. https://www.dama-dk.org/onewebmedia/DAMA%20DMBOK2_PDF.pdf (onze áreas de conhecimento, definição de arquitetura de dados e de dados mestres e de referência, interação pela governança)
- DAMA International. (2024). *DAMA-DMBOK: Data management body of knowledge* (2nd ed., revised). Technics Publications. (obra de referência, consultada por meio das publicações da DAMA listadas nesta seção)
- DAMA International. (n.d.). *DMBOK 2.0 revision*. https://www.damadmbok.org/dmbok2-revisions (panorama de dados no lugar do desenho de fluxo de dados e nove dimensões de qualidade)
- DAMA Rocky Mountain Chapter. (2023). *DMBoK figure 23: Enterprise data model*. https://damarmc.org/news/13270755 (quatro níveis do modelo de dados corporativo)
- Databricks. (n.d.). *Medallion architecture*. https://www.databricks.com/glossary/medallion-architecture (camadas bronze, prata e ouro)
- Debezium. (n.d.-a). *Debezium features*. https://debezium.io/documentation/reference/stable/features.html (captura de mudanças baseada em log, conectores de origem para o Kafka Connect, captura de exclusões)
- Debezium. (n.d.-b). *Debezium connector for PostgreSQL*. https://debezium.io/documentation/reference/stable/connectors/postgresql.html (decodificação lógica do log de transações, evento por inserção, atualização e exclusão de linha, um tópico do Kafka por tabela)
- Dehghani, Z. (2022). *Data mesh: Delivering data-driven value at scale*. O'Reilly Media. (princípio da propriedade do dado pelo domínio)
- Fowler, M. (2015). *Data lake*. https://martinfowler.com/bliki/DataLake.html (dado bruto na forma fornecida pela origem)
- Kimball Group. (n.d.). *Dimensional modeling techniques*. https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/ (tabelas de fatos e de dimensões e esquema estrela)
- Kleppmann, M. (2017). *Designing data-intensive applications: The big ideas behind reliable, scalable, and maintainable systems*. O'Reilly Media. (parte III, sistemas de registro e dado derivado)
- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seção 2.5, arquitetura de dados corporativa e de solução, artefatos e grade de análise de impacto, generalização para reconhecer entidades existentes. Os conceitos foram adaptados ao caso da Universidade ACME)
- OpenLineage. (n.d.). *OpenLineage* [Repositório]. LF AI & Data Foundation. https://github.com/OpenLineage/OpenLineage (entidades run, job e dataset e implementação de referência Marquez)
- Richardson, C. (n.d.). *Pattern: Database per service*. Microservices.io. https://microservices.io/patterns/data/database-per-service.html (dado persistente privado ao serviço e acessível apenas pela interface dele)
- Steenbeek, I. (2017, 10 de setembro). *New vision on data lineage/flow in DAMA-DMBOK2*. Data Crossroads. https://datacrossroads.nl/2017/09/10/new-vision-on-data-lineage-flow-in-dama-dm-bok-2/ (fluxos de dados como documentação de linhagem, segundo o capítulo 4 do DMBOK2)

**Material do curso.** O bloco usa as entradas [arquitetura de dados](../referencia/glossario.md#arquitetura-de-dados), [modelo de dados corporativo](../referencia/glossario.md#modelo-de-dados-corporativo), [dados mestres](../referencia/glossario.md#dados-mestres), [propriedade do dado](../referencia/glossario.md#propriedade-do-dado), [fonte de verdade](../referencia/glossario.md#fonte-de-verdade) e [regime de consistência](../referencia/glossario.md#regime-de-consistencia) do glossário, além do dossiê da instituição fictícia [ACME](../caso-acme/index.md) e da sua [arquitetura de linha de base](../caso-acme/linha-de-base.md).
