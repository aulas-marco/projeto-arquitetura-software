---
secao: 1
titulo: Contexto
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| O que vai | A instituição e os números do problema, as restrições que chegam fechadas, as respostas já excluídas, as decisões classificadas por nível de arquitetura, os componentes da solução nos cinco tipos e os papéis de quem decide |
| Pergunta que responde | Que organização é esta, que problema ela precisa resolver e quem decide cada parte |
| Artefatos e códigos | Tabela de porte, tabela de restrições com origem e efeito, decisões D1 a Dn pelo nível que cada uma toma, premissas PR1 a PRn |
| Entrada | O dossiê do caso ACME, em particular a página inicial do caso e os dados operacionais |
| Preenchida em | Aula 1, exercícios 1 a 4 |
<!--/orientacao-->

<!--ex n=1 titulo="Instituição, restrições e decisões por nível"-->
<!--campos-->
- Instituição, pergunta central e restrições fechadas, fornecidas pelo dossiê
- Nível de arquitetura de cada decisão D1 a D9, com a justificativa pelo alcance do efeito
- Tipo de componente não tecnológico afetado pelas decisões de solução
- Dependência entre decisões
<!--/campos-->
<!--gabarito-->
#### Instituição e pergunta central

| Dimensão | Valor |
| --- | --- |
| Alunos ativos | 38.400, dos quais 10.200 na graduação a distância |
| Professores | 2.150 |
| Campi | 4, em 3 cidades |
| Sistema acadêmico | Em operação desde 2004, com núcleo em COBOL |
| Custo anual de propriedade | R$ 15,83 milhões |
| Prazo médio entre pedido aprovado e entrega | 34 dias úteis |
| Equipe do núcleo | 6 especialistas em COBOL, 2 deles com aposentadoria prevista para 2027 |
| Orçamento do primeiro ciclo | R$ 6,2 milhões em 12 meses |

A pergunta central é como evoluir o sistema acadêmico de forma segura e incremental, mantendo o núcleo em operação durante a transição. A Reitoria descartou em 12/03/2026 duas respostas, a substituição integral por produto de mercado, pelo custo de migrar os históricos de 214.000 egressos, e a reescrita em entrega única, porque nenhuma janela do calendário acadêmico comporta a virada de todos os módulos.

#### Restrições que chegam fechadas

| Código | Restrição | Origem | Consequência para a arquitetura |
| --- | --- | --- | --- |
| RT1 | O sistema acadêmico não pode parar em período letivo | Pró-Reitoria de Graduação | Toda estratégia é incremental, com o legado em operação durante a transição |
| RT2 | O ambiente virtual de aprendizagem e o ERP financeiro permanecem | Reitoria, 12/03/2026 | O trabalho é de integração e governança, sem substituição |
| RT3 | Dois provedores de nuvem pré-aprovados | Conselho Universitário, 12/03/2026 | Decisões de plataforma precisam ser portáveis entre os dois |
| RT4 | Identidade e autorização por padrões abertos | Comitê de Segurança da Informação | A escolha é de padrão, e não de produto |
| RT5 | Dado pessoal de aluno processado em território nacional | Jurídico, parecer de 28/04/2026 | Restringe a região de implantação e o uso de serviços gerenciados |
| RT6 | Manutenção do núcleo COBOL sob contrato até 30/09/2027 | Contrato de sustentação | Alterações no núcleo dependem de fornecedor externo |
| RT7 | Orçamento de R$ 6,2 milhões para o primeiro ciclo de 12 meses | Reitoria | O roteiro de evolução precisa caber nesse valor antes de nova aprovação |

#### Decisões por nível de arquitetura

O critério de classificação é o alcance do efeito da decisão. Decisão que muda só a estrutura interna de um componente é de software, a que muda processo, papel, propriedade de dado ou relação com fornecedor é de solução, e a que vale para iniciativas que ainda não existem é corporativa.

| Código | Decisão | Nível | Justificativa pelo alcance |
| --- | --- | --- | --- |
| D1 | Identidade e autorização seguem padrões abertos, sem produto proprietário | Corporativa | Vale para qualquer iniciativa da universidade, inclusive as que ainda não existem |
| D2 | A propagação de nota ao ambiente virtual passa de lote diário a até 10 minutos | Solução | Muda o processo de fechamento de notas, o contrato com o fornecedor do ambiente virtual e a integração |
| D3 | O serviço de notas repete o envio sem confirmação, com intervalo crescente | Software | Altera o comportamento de um componente, sem que outra parte da organização precise ser avisada |
| D4 | Nenhum dado pessoal de aluno é processado fora do território nacional | Corporativa | É regra do Jurídico que vale para toda iniciativa que trate dado de aluno, presente ou futura |
| D5 | A Secretaria Acadêmica passa a responder pela correção de dado cadastral | Solução | Muda papel e propriedade de dado, porque a correção sai da equipe de sustentação |
| D6 | O índice de busca de disciplinas do portal passa a ficar em memória | Software | Altera a estrutura interna de um componente do portal, sem efeito sobre processo, papel ou fornecedor |
| D7 | O núcleo COBOL permanece sob o contrato da fábrica até 30/09/2027 | Solução | Muda a relação com o fornecedor, porque toda alteração no núcleo depende da fábrica |
| D8 | O histórico escolar é emitido com assinatura digital no padrão ICP-Brasil | Solução | Muda o procedimento de emissão e depende de certificado de terceiro, sem valer para iniciativas futuras |
| D9 | A transição ocorre por extração incremental de módulos, com o núcleo em operação | Solução | Afeta o contrato de sustentação, o calendário acadêmico e a rotina das equipes |

As decisões D1 a D3 vêm do caderno de referência, e as decisões D4 a D9 estão **propostas** e dependem de validação com as partes interessadas.

#### Componente não tecnológico afetado

| Código | Tipo de componente | Efeito |
| --- | --- | --- |
| D2 | Processos | O fechamento de notas deixa de depender da janela noturna de lote |
| D5 | Estruturas organizacionais | A correção de dado cadastral sai da equipe de sustentação, terceirizada, e passa à Secretaria Acadêmica |
| D7 | Estruturas organizacionais | O contrato com a fábrica de software, organização parceira, define quem pode alterar o núcleo |
| D8 | Processos | A emissão do histórico escolar passa a ter a assinatura digital como etapa do procedimento |
| D9 | Processos | A rotina de cada equipe muda a cada módulo extraído, no ritmo do calendário acadêmico |

#### Dependência entre decisões

A decisão D3 depende da D2. Sem a D2, o reenvio com intervalo crescente seria desenhado para um percurso em lote diário noturno, em que cada tentativa só ocorre na janela seguinte, de modo que o intervalo crescente não tem prazo de propagação que o justifique e a nota continua chegando ao aluno no dia seguinte.
<!--/gabarito-->
<!--/ex-->

<!--ex n=2 titulo="Componentes da solução do R7"-->
<!--campos-->
- Tipo de cada componente candidato CP1 a CP10
- Nível de cada elemento da situação atual N1 a N6
<!--/campos-->
<!--gabarito-->
#### Componentes da solução do R7

O R7, nota no ambiente virtual de aprendizagem em até 10 minutos, é atendido por dez componentes candidatos, que ocupam os cinco tipos.

| Código | Componente | Tipo |
| --- | --- | --- |
| CP1 | Treinamento dos professores para publicação imediata da nota | Pessoas |
| CP2 | Aditivo ao contrato do ambiente virtual, com troca para o plano que oferece interfaces de programação | Estruturas organizacionais |
| CP3 | Acordo de nível de serviço de 10 minutos entre a Diretoria de TI e a Coordenação de Educação a Distância | Estruturas organizacionais |
| CP4 | Procedimento de correção de nota já publicada | Processos |
| CP5 | Fechamento de notas sem dependência da janela noturna de lote | Processos |
| CP6 | Registro de cada envio, com horário de lançamento e de confirmação | Informação |
| CP7 | Mensagem de nota lançada, com aluno, turma, avaliação e valor | Informação |
| CP8 | Mensageria entre o núcleo acadêmico e o ambiente virtual | Tecnologia |
| CP9 | Serviço de notas que publica um evento a cada lançamento | Tecnologia |
| CP10 | Responsável na Coordenação de Educação a Distância pelas falhas de envio | Pessoas |

Nenhum tipo ficou sem componente. O tipo de maior impacto sobre quem trabalha na instituição é Processos, porque o CP5 e o CP4 mudam a rotina de fechamento e de correção de nota de professores, coordenações e Secretaria, e a mudança tecnológica sozinha não altera o prazo percebido.

#### Os três níveis do R7

| Código | Elemento da situação atual | Nível |
| --- | --- | --- |
| N1 | Serviço de avaliação com resultado publicado no calendário acadêmico | Sistema de negócio |
| N2 | Calendário acadêmico que fixa a data de fechamento das notas | Sistema de negócio |
| N3 | Rotina de conferência manual das notas antes da publicação | Sistema de informação |
| N4 | Registros de nota entre professor, coordenação e Secretaria | Sistema de informação |
| N5 | Portal do professor e núcleo COBOL que calcula a situação do aluno | Sistema de TI |
| N6 | Exportação noturna por lote ao ambiente virtual | Sistema de TI |

Uma solução construída apenas no nível de sistema de TI troca o lote noturno por propagação em minutos e mantém o calendário de fechamento e a conferência manual, que determinam quando a nota está pronta para publicar, de modo que o prazo percebido pelo aluno continua sendo o do fechamento.
<!--/gabarito-->
<!--/ex-->

<!--ex n=3 titulo="Papéis e responsabilidades do ciclo"-->
<!--campos-->
- Nível de arquitetura responsável por cada tarefa T1 a T10
- Grupo de competência das tarefas do arquiteto de solução
- Benefício da abordagem que justifica a tarefa T10
<!--/campos-->
<!--gabarito-->
#### Responsável por cada tarefa

O critério é o alcance do efeito, o mesmo da decisão por nível.

| Código | Tarefa | Responsável | Grupo de competência | Justificativa |
| --- | --- | --- | --- | --- |
| T1 | Entrevistar a Pró-Reitoria de Graduação e a Educação a Distância | Arquiteto de solução | Prático | Levantar o que cada área precisa é tratamento de requisitos e gestão de partes interessadas |
| T2 | Definir a consistência de dado entre o serviço extraído e o núcleo | Arquiteto de software | | Decide como o módulo extraído se comporta por dentro durante a coexistência |
| T3 | Estimar o custo da mudança tecnológica do primeiro ciclo | Arquiteto de solução | Entrega | A estimativa de custo é uma das três saídas da arquitetura de solução |
| T4 | Escolher a estrutura de dados do serviço de matrícula | Arquiteto de software | | Altera só a estrutura interna de um componente |
| T5 | Negociar com a fábrica a abertura de interfaces no núcleo | Arquiteto de solução | Prático | Muda a relação com o fornecedor e exige negociação com partes interessadas |
| T6 | Redigir a política institucional de dado pessoal de aluno | Arquitetura corporativa | | Vale para qualquer sistema da universidade, presente ou futuro |
| T7 | Produzir o roteiro de entrega do ciclo | Arquiteto de solução | Entrega | O roteiro de entrega é uma das três saídas da arquitetura de solução |
| T8 | Decidir que a Secretaria responde pela correção de dado cadastral | Arquiteto de solução | Negócio | Muda papel e propriedade de dado, o que exige leitura do modelo operacional |
| T9 | Configurar o servidor de integração contínua | Arquiteto de software | | É configuração de ferramenta da equipe de desenvolvimento |
| T10 | Verificar se já existe componente de envio de mensagem reaproveitável | Arquiteto de solução | Técnico | Exige conhecer a tecnologia vigente antes de especificar componente novo |

Seis tarefas cabem ao arquiteto de solução, três ao arquiteto de software ou à equipe de desenvolvimento e uma à arquitetura corporativa, e os quatro grupos de competência aparecem nas tarefas do arquiteto de solução.

#### Benefício por trás da tarefa T10

A tarefa T10 se justifica pelo benefício do **reúso**, porque a consulta ao catálogo de aplicações e à arquitetura de software revela se um componente existente serve ao novo uso. Sem a verificação, a instituição especifica e constrói um segundo componente de envio de mensagem, paga a duplicação de manutenção e de integração e perde o custo e a perturbação mínimos que a análise de lacunas procura.
<!--/gabarito-->
<!--/ex-->

<!--ex n=4 titulo="Artefatos nas fases do processo, premissas e escopo"-->
<!--campos-->
- Fase, papel e seção do caderno de cada artefato A1 a A10
- Artefatos de linha de base
- Premissas e exclusões do escopo, fornecidas pelo caderno de referência
<!--/campos-->
<!--gabarito-->
#### Artefatos nas fases do processo

| Código | Artefato | Fase | Papel | Linha de base | Seção do caderno |
| --- | --- | --- | --- | --- | --- |
| A1 | Mapa de atores | 2. Descoberta | Entrada | Sim | 2 |
| A2 | Inventário dos componentes atuais | 2. Descoberta | Entrada | Sim | 4 |
| A3 | Catálogo de blocos de construção e interfaces | 4. Análise | Produto intermediário | Não | 7 |
| A4 | Registro da decisão da Reitoria de 12/03/2026 | 1. Iniciação | Entrada | Sim | 1 |
| A5 | Comparação de duas alternativas de modernização | 4. Análise | Produto intermediário | Não | 7 |
| A6 | Modelo único de componentes da solução | 5. Desenho lógico | Entregável | Não | 7 |
| A7 | Sequência de extração dos módulos | 7. Desenvolvimento do roteiro | Entregável | Não | 9 |
| A8 | Lista de componentes acrescentados, removidos e alterados | 6. Validação | Produto intermediário | Não | 4 |
| A9 | Documento que autoriza a equipe a iniciar a investigação | 1. Iniciação | Entrada | Não | 1 |
| A10 | Modelos da solução implantada, devolvidos ao repositório | 8. Conclusão | Entregável | Não | Todas |

Os artefatos de linha de base são A1, A2 e A4, porque já descreviam parte da situação atual antes do início do processo. O pedido da data de conclusão chega depois do A9, na iniciação, e a data só pode ser dada com precisão depois da fase 7, em que sai a estimativa de prazo e de custo. Até lá, o caderno registra a pendência na seção 10.

#### Premissas

| Código | Premissa | Se for falsa | Como verificar |
| --- | --- | --- | --- |
| PR1 | O único especialista que domina o módulo de matrícula permanece na sustentação até 2027 | Ninguém consegue alterar a regra de prioridade de vaga | Consultar a fábrica contratada antes de qualquer desenho que dependa do módulo |
| PR2 | As transações que já existem no núcleo cobrem a confirmação da matrícula e o cálculo da parcela, sem alterar programa | A camada de tradução não consegue chamar o núcleo, e a alteração só ocorre depois de 30/09/2027 | Inventário das 380 transações com a fábrica e prova de conceito com uma confirmação |
| PR3 | A captura de mudanças pelo registro do banco Oracle funciona sem tocar o COBOL e sem violar o licenciamento | As cópias de leitura e os eventos de nota deixam de existir | Prova de conceito com o administrador do banco e a área de licenciamento |
| PR4 | A fábrica aceita executar testes de caracterização em paralelo ao núcleo | O conhecimento da regra de prioridade de vaga não é capturado antes das aposentadorias | Negociação com o gerente de sustentação, com base no contrato |
| PR5 | O roteiro começa no início de 2027 | As ondas deslizam e o primeiro ciclo cruza janelas de matrícula diferentes das previstas | Data de aprovação do roteiro pelo patrocinador |
| PR6 | O ERP financeiro aceita receber lançamentos por interface automatizada | A eliminação da troca manual fica sem destino técnico | Consulta ao fornecedor e à equipe de integrações |
| PR7 | Os dois provedores aprovados oferecem região no território nacional com os serviços que a solução usa | A restrição de dado pessoal elimina serviços gerenciados e muda a zona de pouso | Catálogo de cada provedor |

#### O que fica fora do escopo

| Exclusão | Motivo |
| --- | --- |
| Substituição do ERP financeiro e do ambiente virtual de aprendizagem | Decisão da Reitoria de 12/03/2026 |
| Substituição integral por produto de mercado | Custo de migrar 214.000 históricos de egressos, decisão da Reitoria de 12/03/2026 |
| Reescrita completa em uma única entrega | Nenhuma janela do calendário comporta a virada de todos os módulos |
| Alteração de programas COBOL pela equipe interna até 30/09/2027 | Exclusividade contratual da fábrica |
| Troca do provedor do gateway de pagamento no primeiro ciclo | Multa rescisória de 6 meses de tarifa média até 30/04/2027 |
| Migração do banco Oracle no primeiro ciclo | O licenciamento obriga a licenciar todos os núcleos físicos do ambiente virtualizado, e o núcleo continua gravando no Oracle |
<!--/gabarito-->
<!--/ex-->
