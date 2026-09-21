# Artefatos por aula

A ACME é uma universidade privada brasileira fictícia, com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, usado como caso único ao longo das seis aulas da disciplina. Esta página registra o que cada aula acrescenta ao dossiê do caso.

O dossiê é cumulativo. A maior parte dos exercícios produz um artefato que serve de entrada para a aula seguinte, de modo que o aluno termina a disciplina com um conjunto encadeado de decisões sobre o mesmo sistema, e não com exercícios isolados.

## Aula 1, arquitetura de soluções e seu processo

A tabela abaixo cobre os quatro blocos da aula. Nenhum deles produz artefato de projeto, porque a aula estabelece o enquadramento da disciplina e do processo antes do levantamento propriamente dito.

| Bloco | Artefato produzido | Entrada usada do dossiê | Critério de aceitação |
| --- | --- | --- | --- |
| 1 | Classificação de nove decisões do caso em arquitetura corporativa, de solução e de software | Restrições fechadas e requisitos declarados da [página inicial do caso](index.md) | Cada decisão classificada com justificativa pelo alcance do efeito, e duas decisões de solução ligadas a um componente não tecnológico |
| 2 | Inventário de componentes da solução nos cinco tipos, com a leitura do requisito nos três níveis | Requisito R7 e interesses em conflito da [página inicial do caso](index.md) | Ao menos um componente em cada um dos cinco tipos, e a distinção entre o que é de sistema de negócio, de informação e de TI |
| 3 | Atribuição de dez tarefas do ciclo de modernização aos três níveis de arquitetura | Restrições contratuais dos [dados operacionais](dados-operacionais.md) | Cada tarefa atribuída com justificativa, e as tarefas do arquiteto de solução ligadas a um dos quatro grupos de competência |
| 4 | Associação de dez artefatos do caso às fases do processo, com a distinção entre entrada, produto intermediário e entregável | [Arquitetura de linha de base](linha-de-base.md) e decisões registradas na [página inicial do caso](index.md) | Cada artefato associado a uma fase, com os artefatos de linha de base identificados |

## Aula 2, entradas, requisitos e partes interessadas

Esta é a aula em que o dossiê passa a receber artefatos de projeto. Os três primeiros blocos produzem os insumos que a Aula 3 consome.

| Bloco | Artefato produzido | Entrada usada do dossiê | Critério de aceitação |
| --- | --- | --- | --- |
| 1 | Classificação dos direcionadores em reativos e antecipatórios, com análise PESTLE do caso | Pergunta central e custos da [página inicial do caso](index.md) | Cada direcionador classificado com evidência, e um fator externo plausível em cada uma das seis categorias |
| 2 | Classificação das declarações em requisito funcional, requisito de atributo de qualidade ou restrição, com reescrita de dois itens em forma mensurável | Requisitos R2, R3, R4, R5, R6, R10, R11 e R13 da [página inicial do caso](index.md) | Os oito itens classificados com justificativa de uma linha, e os dois requisitos mal formulados reescritos com contexto, carga e medida |
| 3 | Dois cenários de atributo de qualidade no formato de seis elementos, com julgamento de significância, mais a leitura dos artefatos de linha de base e a classificação das restrições por origem | Volumes, sazonalidade e incidentes dos [dados operacionais](dados-operacionais.md) e restrições fechadas | Cada cenário com os seis elementos, a defesa da significância pelo roteiro de sete perguntas, e cada restrição classificada com a autoridade que poderia revê-la |
| 4 | Mapa de partes interessadas por categoria, três pontos de vista definidos e a declaração de escopo do primeiro ciclo | Mapa de atores e interesses em conflito da [página inicial do caso](index.md) | Cada papel classificado, as categorias ausentes apontadas com o risco correspondente, e a declaração de escopo indicando o que muda, o que permanece e a origem de cada exclusão |

## Aulas 3 a 6

| Aula | Tema | Artefatos produzidos nos quatro exercícios |
| --- | --- | --- |
| 3 | Princípios de design, padrões e registro de decisão | Princípios de design da solução com as restrições deles derivadas, comparação de estilos contra os cenários da Aula 2, classificação de padrões por nível, e o ADR que registra a escolha de estilo |
| 4 | Protocolos, especificações e representação | Situação dos componentes nos domínios de aplicação e de dados, pontos de controle de segurança no fluxo, contrato de uma integração, e modelo C4 de contexto e de contêineres |
| 5 | Frameworks, tecnologias e definição tecnológica | Mapeamento de blocos de construção em serviços de infraestrutura, quadro comparativo de plataformas, modelo técnico de referência, e o ADR de plataforma com as lacunas de provisão |
| 6 | Lacunas, roteiro, governança e inovação | Análise de lacunas entre linha de base e arquitetura alvo, roteiro de entrega em ondas, pontos de governança com métricas, e avaliação de uma tendência quanto ao efeito sobre a solução |

## Rastreabilidade entre artefatos

A dependência entre artefatos define a ordem em que eles podem ser produzidos. A Aula 1 não alimenta formalmente a Aula 2, porque seu produto é o enquadramento da disciplina e do processo, e não um artefato de projeto. A cadeia formal começa na Aula 2 e é linear a partir do bloco 2. Os cenários dependem da classificação de requisitos, porque só requisito de atributo de qualidade vira cenário. A declaração de escopo depende do mapa de partes interessadas, porque escopo é acordado com quem tem autoridade para aprová-lo.

Das aulas seguintes, a cadeia continua linear. A comparação de estilos da Aula 3 depende dos cenários da Aula 2, porque estilo se avalia contra exigência medida, e o ADR de estilo depende dessa comparação. Os contratos e a modelagem da Aula 4 recaem sobre a forma estrutural já escolhida. A definição tecnológica da Aula 5 converte em produto o que a Aula 4 desenhou de forma lógica, e o ADR de plataforma depende do quadro comparativo montado ali. A análise de lacunas da Aula 6 compara a arquitetura de linha de base do dossiê com a arquitetura alvo construída nas aulas anteriores, e o roteiro de entrega ordena as mudanças que essa comparação revelou.

As restrições contratuais registradas nos [dados operacionais](dados-operacionais.md), em especial os prazos de 30/09/2027 e de 31/12/2028, delimitam o que pode ser decidido em cada aula, porque elas fecham alternativas antes de qualquer análise técnica.
