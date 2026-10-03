# Arquitetura de negócio da solução

Este bloco inicia o detalhamento da solução por domínios e responde a uma pergunta que precede dados, aplicações e infraestrutura, o que a solução muda no negócio e quais modelos permitem localizar essa mudança.

## Antes de começar

- [Arquitetura de negócio](../referencia/glossario.md#arquitetura-de-negocio)
- [Capacidade](../referencia/glossario.md#capacidade)
- [Fluxo de valor](../referencia/glossario.md#fluxo-de-valor)
- [Componentes da solução](../referencia/glossario.md#componentes-da-solucao)
- [Arquitetura de solução](../referencia/glossario.md#arquitetura-de-solucao)

## Modelos de arquitetura de negócio

A Aula 3 terminou com uma decisão estrutural registrada em ADR, com o estilo e os padrões que organizam a solução. Essa decisão diz como a solução se organiza, mas não diz o que ela altera na organização que a recebe. A Aula 4 detalha a solução em quatro domínios, na ordem negócio, dados, aplicações e infraestrutura, e cada domínio consome o que o anterior estabeleceu, de modo que a mudança localizada neste bloco orienta a escolha dos dados no bloco 2.

A **arquitetura de negócio** é definida pelo Business Architecture Guild, em formulação citada por Lovatt (2021, seção 2.3), como uma representação da organização que oferece entendimento comum sobre ela e serve para alinhar objetivos estratégicos e demandas táticas. O TOGAF, também citado por Lovatt, descreve a mesma arquitetura como um conjunto de visões do negócio sobre capacidades, entrega de valor de ponta a ponta, informação e estrutura organizacional, com as relações entre essas visões e as estratégias, os produtos, as políticas e as partes interessadas. As duas definições atribuem ao domínio dois papéis na arquitetura de solução, o de origem da necessidade de mudança e o de alvo da mudança que a solução entrega.

### Quando a arquitetura de solução se aplica

Lovatt (2021, seção 2.3) lembra que a arquitetura de solução trabalha reduzindo um sistema a suas partes por meio de um modelo, e que por isso nem todo problema de negócio admite esse tratamento. Quatro perguntas decidem a aplicação do método:

1. A área do problema é um sistema?
2. O sistema pode ser modelado?
3. O modelo exibe o problema?
4. O modelo pode ser alterado para tratar o problema?

Uma resposta negativa a qualquer das quatro indica que outro método é mais adequado. Quando o problema é grande demais para ser modelado de uma vez, a alternativa recomendada é reduzir o escopo, por exemplo a uma linha de produtos, a uma região ou a um grupo delimitado de unidades organizacionais. Quando o problema é simples demais para ser chamado de sistema, o ciclo completo de arquitetura acrescenta complexidade sem revelar causa, e só algumas técnicas isoladas continuam úteis.

### Quatro modelos

A arquitetura de negócio mantém modelos que o arquiteto de solução consulta para localizar a mudança. Lovatt (2021, seção 2.3.1) apresenta os mais usados, e a tabela abaixo resume a pergunta que cada um responde e o que ele oferece ao arquiteto.

| Modelo | Pergunta que responde | O que oferece ao arquiteto |
| --- | --- | --- |
| Mapa de capacidades | O que a organização precisa conseguir fazer? | As capacidades afetadas pela solução e os recursos que as habilitam |
| Fluxo de valor | Por quais etapas o valor chega ao cliente? | As etapas em que a solução altera o valor percebido |
| Decomposição funcional | Que unidade realiza cada função? | As unidades organizacionais afetadas |
| Modelo de processo de negócio | Que atividades compõem o trabalho e quem as executa? | As atividades que mudam, desaparecem ou passam a ser automatizadas |

O **mapa de capacidades** decompõe as capacidades de topo em capacidades menores. Uma **capacidade** é aquilo que a organização precisa conseguir fazer para entregar seus serviços e executar sua estratégia, e pode ainda não existir, constando apenas do plano. Cada capacidade tem dois atributos adicionais, o volume, que é quanto se entrega em paralelo, e a competência, que é o nível de habilidade exigido, e é habilitada por recursos como pessoas, unidades organizacionais, tecnologia e conhecimento especializado. O mapa classifica as capacidades em estratégicas, operacionais e de apoio, e outras classificações, como maturidade ou núcleo e periferia, também são usadas.

O **fluxo de valor** é o conjunto de etapas de ponta a ponta que entrega valor a um cliente, do primeiro contato com a organização até a realização desse valor. A técnica tem origem na produção enxuta, que procura eliminar as etapas que não acrescentam valor suficiente, e Lovatt observa que ela combina bem com a arquitetura de solução porque as duas analisam o problema em termos de estrutura e de comportamento.

A decomposição funcional e o modelo de processo de negócio completam o conjunto. Nesta disciplina, os dois são tratados como artefatos que o arquiteto de solução lê e consulta, mantidos pela área de negócio ou pela análise de processos, e não como técnica que o arquiteto pratica. O modelo de motivação de negócio, que liga direcionadores de mudança a fins e meios, também consta da lista de Lovatt e foi tratado, pelo lado dos direcionadores, no [bloco 1 da Aula 2](../modulo-2-requisitos-e-partes-interessadas/bloco-1-direcionadores-de-mudanca.md).

<figure markdown="span">
![Diagrama com quatro cartões, um para cada modelo de arquitetura de negócio, mapa de capacidades, fluxo de valor, decomposição funcional e modelo de processo, cada um com a pergunta que responde. Abaixo, uma faixa com os cinco estágios do ciclo de mudança de negócio, alinhar, definir, projetar, implementar e realizar, com definir e projetar destacados como os estágios em que a arquitetura de solução se concentra.](../assets/images/modulo-4-modelos-de-negocio.svg){ .module-diagram }
</figure>

*Figura 1 — Os quatro modelos de arquitetura de negócio e a pergunta de cada um, sobre o ciclo de mudança de negócio. Fonte: material do curso, com base em Lovatt (2021, seções 2.3.1 e 2.3.2).*

### O exemplo do Hospital Vale do Pousio

O Hospital Vale do Pousio, caso que acompanha o livro-texto, quer melhorar a comunicação com seus pacientes. No mapa de capacidades, a capacidade de comunicar-se com pacientes já existe, mas de forma limitada, por carta impressa. O plano é aumentar o volume, para que mais comunicações ocorram, e acrescentar canais e pontualidade, por exemplo com um lembrete enviado ao paciente na véspera da consulta.

A partir dessa capacidade, o modelo de processo indica as atividades afetadas, que são a marcação de consulta, o cancelamento e a remarcação de consulta, o cancelamento e a remarcação de clínica, a gestão da lista de espera e o relatório gerencial. A decomposição funcional indica as unidades afetadas, entre elas a sala de correspondência, que perde parte do volume de cartas, e o ambulatório, que hoje dedica muitos funcionários a cancelamentos e remarcações. Nenhum desses modelos precisou ser criado pelo arquiteto, que apenas os consultou para delimitar a mudança.

### Componentes de negócio da solução

Pessoas, unidades organizacionais e processos de negócio são componentes da solução e foram apresentados no [bloco 2 da Aula 1](../modulo-1-fundamentos/bloco-2-a-solucao-como-sistema.md). Lovatt (2021, seção 2.4.3) acrescenta que todos os componentes da solução, inclusive os processos, sustentam em última instância um ou mais serviços de negócio. Essa afirmação organiza os blocos seguintes desta aula, porque dados, aplicações e infraestrutura só se justificam pelo serviço de negócio que sustentam, e o bloco 3 retoma essa relação na hierarquia que vai do serviço de negócio ao serviço de tecnologia.

### O ciclo de mudança de negócio

Lovatt (2021, seção 2.3.2) situa a arquitetura de solução num ciclo de mudança de negócio em cinco estágios, usado por analistas de negócio e arquitetos:

1. Alinhar, que examina os ambientes externo e interno em busca de oportunidades e é fonte de conceitos de solução.
2. Definir, que identifica requisitos e restrições, articula benefícios e constrói o caso de negócio.
3. Projetar, que é o foco principal da arquitetura de solução.
4. Implementar, em que a arquitetura de solução fornece o roteiro de entrega e mantém papel de governança.
5. Realizar, em que a solução é entregue ao negócio e a arquitetura acompanha a entrega.

A arquitetura de solução concentra seu trabalho nos estágios de definir e projetar, e os modelos de arquitetura de negócio são a principal entrada de ambos.

## Uso pelo arquiteto

O arquiteto de solução consulta os modelos que a arquitetura de negócio já mantém para delimitar o que a solução muda, sem redesenhar a organização a cada iniciativa. O mapa de capacidades indica onde a mudança incide, o fluxo de valor indica onde o cliente percebe a mudança, e o modelo de processo indica que atividades precisam ser revistas com as áreas responsáveis. Quando um desses modelos não existe, o arquiteto registra a ausência como risco e solicita o artefato à área de negócio, sem assumir a modelagem como tarefa própria.

## Exercício 13

Este exercício é realizado fora do horário de aula, como atividade de aplicação do conceito apresentado neste bloco ao caso da instituição fictícia ACME.

A ACME é uma universidade privada brasileira com 38.400 alunos ativos, cujo sistema acadêmico, em operação desde 2004, passa por modernização incremental. O exercício parte da declaração de escopo do primeiro ciclo, produzida no [exercício 8](../modulo-2-requisitos-e-partes-interessadas/bloco-4-partes-interessadas-e-pontos-de-vista.md#exercicio-8), e de três requisitos reproduzidos da [página inicial do caso](../caso-acme/index.md).

| Código | Declaração | Origem |
| --- | --- | --- |
| R1 | O aluno deve renovar a matrícula pelo telefone celular, sem acesso ao portal em computador | Representação discente |
| R7 | A nota lançada pelo professor chega ao ambiente virtual de aprendizagem em até 10 minutos | Educação a Distância |
| R13 | O aluno consulta o resultado da solicitação de aproveitamento de disciplina pelo portal | Secretaria Acadêmica |

O primeiro artefato lista dez capacidades acadêmicas da ACME, montadas pelo material do curso a partir do dossiê, sem classificação.

| Capacidade | Descrição |
| --- | --- |
| Admissão e ingresso | Seleção de candidatos e registro do ingresso do aluno |
| Oferta e grade curricular | Montagem semestral da oferta de 4.900 turmas |
| Matrícula em disciplinas | Inscrição do aluno nas turmas de cada período |
| Avaliação e registro de notas | Lançamento de notas, cálculo de média e situação do aluno |
| Controle de frequência | Apuração de faltas e de reprovação por infrequência |
| Emissão de documentos acadêmicos | Histórico, declaração, atestado e diploma digital |
| Gestão de bolsas e descontos | Regras de financiamento estudantil e de convênio |
| Cobrança de mensalidades | Lançamento financeiro e acompanhamento de pagamento |
| Biblioteca | Empréstimo, reserva e débito |
| Relação com o órgão regulador | Extração anual do censo da educação superior |

O segundo artefato descreve o fluxo de valor do aluno, com o tempo de cada passagem retirado da [arquitetura de linha de base](../caso-acme/linha-de-base.md).

| Etapa | Situação na linha de base |
| --- | --- |
| 1. Renovação da matrícula | Feita no Portal do Aluno, sem versão responsiva e com componente de calendário que restringe o uso em telefone celular |
| 2. Confirmação da matrícula | Confirmada no núcleo transacional durante a sessão do aluno |
| 3. Acesso à turma no ambiente virtual | Uma matrícula confirmada às 09h00 aparece no ambiente virtual às 04h55 do dia seguinte, pela carga de turmas das 04h00 |
| 4. Lançamento da nota pelo professor | Registrada no Portal do Professor durante o dia letivo |
| 5. Nota visível no ambiente virtual | Uma nota lançada às 15h00 chega ao ambiente virtual às 06h00 do dia seguinte, pela exportação das 05h10 |
| 6. Resultado de aproveitamento de disciplina | A linha de base não registra consulta desse resultado pelo portal |

O terceiro artefato descreve as atividades do processo atual de lançamento de nota e o responsável por cada uma.

| Atividade | Responsável |
| --- | --- |
| 1. Registrar a nota no Portal do Professor | Professor |
| 2. Calcular média e situação no módulo de avaliação e notas | Núcleo transacional |
| 3. Gerar o arquivo de notas consolidadas no lote das 05h10 | Equipe de integrações e execução de lotes |
| 4. Importar o arquivo de notas | Ambiente virtual de aprendizagem |
| 5. Devolver notas e frequência de atividades no lote das 06h15 | Ambiente virtual de aprendizagem |
| 6. Consultar a nota | Aluno |

1. Classifique cada capacidade do primeiro artefato em estratégica, operacional ou de apoio e marque as capacidades afetadas pelo primeiro ciclo, conforme a declaração de escopo do exercício 8, com uma linha de justificativa para cada marcação.
2. Indique, no segundo artefato, as etapas em que a latência ou a restrição de acesso compromete o valor para o aluno e qual requisito, R1, R7 ou R13, cada uma afeta.
3. Responda, sobre o terceiro artefato, quais atividades mudam com a solução, qual unidade organizacional é afetada por essa mudança e qual atividade deixa de existir se a nota passar a chegar ao ambiente virtual em até 10 minutos.

As capacidades marcadas como afetadas neste exercício são a entrada da grade de dados do exercício 14, no [bloco 2](bloco-2-arquitetura-de-dados.md).

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seção 2.3, arquitetura de negócio, quatro perguntas de aplicabilidade, modelos de arquitetura de negócio e ciclo de mudança de negócio, e seção 2.4, componentes de negócio da solução. O Hospital Vale do Pousio é a versão em português do caso Fallowdale Hospital, usado ao longo do livro)

**Material do curso.** O bloco usa as entradas [arquitetura de negócio](../referencia/glossario.md#arquitetura-de-negocio), [capacidade](../referencia/glossario.md#capacidade) e [fluxo de valor](../referencia/glossario.md#fluxo-de-valor) do glossário, além do dossiê da instituição fictícia [ACME](../caso-acme/index.md) e da sua [arquitetura de linha de base](../caso-acme/linha-de-base.md).
