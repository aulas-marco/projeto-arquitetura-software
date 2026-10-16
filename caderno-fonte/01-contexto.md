---
secao: 1
titulo: Contexto
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| O que é esta seção | A situação da ACME e o que a modernização precisa respeitar. |
| Pergunta que responde | Que organização é esta, que problema ela quer resolver e o que já está decidido antes de desenhar qualquer coisa? |
| O que você escreve | Tabelas com as restrições (RT1 a RT7), as decisões (D1 a D9), os componentes da solução (CP1 a CP10), as tarefas do ciclo (T1 a T10), os artefatos do processo (A1 a A10) e as premissas (PR1 a PR7). A página de convenções explica cada código. |
| Vem de onde | Do dossiê do caso ACME, que traz os números da instituição, a pergunta central e as restrições. |
| Quando se preenche | Na Aula 1, com os exercícios 1 a 4. |
<!--/orientacao-->

<!--ex n=1 titulo="Instituição, restrições e decisões por nível"-->
<!--campos-->
- **Dado do dossiê:** a instituição, a pergunta central e as restrições já vêm preenchidas, porque são dados do caso.
- **Nível:** diga se cada decisão, de D1 a D9, é de arquitetura corporativa, de solução ou de software.
- **Justificativa:** explique em uma frase o que a decisão muda e quem é afetado por ela.
- **Componente não tecnológico afetado:** nas decisões de solução, diga se a mudança atinge pessoas, estruturas organizacionais, processos ou informação.
- **Dependência entre decisões:** diga qual decisão precisa vir antes de outra e o que acontece se a ordem for invertida.
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

A pergunta central é como evoluir o sistema acadêmico de forma segura e incremental, mantendo o núcleo em operação durante a transição. Em 12/03/2026, a Reitoria descartou duas respostas: a substituição integral por produto de mercado, que exigiria migrar os históricos de 214.000 egressos, e a reescrita em entrega única, porque nenhuma janela do calendário acadêmico comporta a virada de todos os módulos.

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

Para classificar, pergunte até onde o efeito da decisão chega. Se ela muda só o funcionamento interno de um componente de software, é de arquitetura de software. Se muda um processo, um papel, a responsabilidade por um dado ou a relação com um fornecedor, é de arquitetura de solução. Se vale para iniciativas que ainda nem existem, é de arquitetura corporativa.

| Código | Decisão | Nível | Justificativa |
| --- | --- | --- | --- |
| D1 | Identidade e autorização seguem padrões abertos, sem produto proprietário | Corporativa | Vale para qualquer iniciativa da universidade, inclusive as que ainda não existem |
| D2 | A propagação de nota ao ambiente virtual passa de lote diário a até 10 minutos | Solução | Muda o processo de fechamento de notas, o contrato com o fornecedor do ambiente virtual e a integração entre os sistemas |
| D3 | O serviço de notas repete o envio sem confirmação, com intervalo crescente | Software | Muda só o comportamento de um componente, e ninguém fora da equipe que o constrói precisa ser avisado |
| D4 | Nenhum dado pessoal de aluno é processado fora do território nacional | Corporativa | É regra do Jurídico para qualquer iniciativa que trate dado de aluno, hoje ou no futuro |
| D5 | A Secretaria Acadêmica passa a responder pela correção de dado cadastral | Solução | Muda quem responde pelo dado cadastral: sai a equipe de sustentação e entra a Secretaria Acadêmica |
| D6 | O índice de busca de disciplinas do portal passa a ficar em memória | Software | Muda só como um componente do portal funciona por dentro, sem efeito sobre processo, papel ou fornecedor |
| D7 | O núcleo COBOL permanece sob o contrato da fábrica até 30/09/2027 | Solução | Define quem pode mexer no núcleo: toda alteração passa pela fábrica de software, por contrato |
| D8 | O histórico escolar é emitido com assinatura digital no padrão ICP-Brasil | Solução | Muda o procedimento de emissão do histórico e depende de certificado de terceiro, mas não vale para iniciativas futuras |
| D9 | A transição ocorre por extração incremental de módulos, com o núcleo em operação | Solução | Afeta o contrato de sustentação, o calendário acadêmico e a rotina das equipes |

As decisões D1, D4 e D7 reproduzem as restrições fechadas RT4, RT5 e RT6. As decisões D2, D3, D5, D6, D8 e D9 estão **propostas** e dependem de validação com as partes interessadas.

#### Componente não tecnológico afetado

| Código | Tipo de componente | Efeito |
| --- | --- | --- |
| D2 | Processos | O fechamento de notas deixa de depender da janela noturna de lote |
| D5 | Estruturas organizacionais | A correção de dado cadastral sai da equipe de sustentação, terceirizada, e passa à Secretaria Acadêmica |
| D7 | Estruturas organizacionais | O contrato com a fábrica de software, organização parceira, define quem pode alterar o núcleo |
| D8 | Processos | A emissão do histórico escolar passa a ter a assinatura digital como etapa do procedimento |
| D9 | Processos | A rotina de cada equipe muda a cada módulo extraído, no ritmo do calendário acadêmico |

#### Dependência entre decisões

A decisão D3 depende da D2. Sem a D2, o reenvio seria desenhado para um percurso em lote noturno, em que cada nova tentativa só acontece na janela seguinte. Nesse percurso, o intervalo crescente entre tentativas não tem prazo de propagação que o justifique, e a nota continua chegando ao aluno no dia seguinte.
<!--/gabarito-->
<!--/ex-->

<!--ex n=2 titulo="Componentes da solução do R7"-->
<!--campos-->
- **Tipo do componente:** classifique cada componente, de CP1 a CP10, em pessoas, estruturas organizacionais, processos, informação ou tecnologia.
- **Tipo sem componente:** confira se algum dos cinco tipos ficou vazio e diga qual tipo mais muda o trabalho de quem está na instituição.
- **Nível do elemento:** diga se cada elemento da situação atual, de N1 a N6, pertence ao sistema de negócio, ao sistema de informação ou ao sistema de TI.
- **Prazo percebido:** explique por que uma solução só de TI pode não reduzir o prazo que o aluno percebe.
<!--/campos-->
<!--gabarito-->
#### Componentes da solução do R7

O R7 pede que a nota lançada pelo professor chegue ao ambiente virtual de aprendizagem em até 10 minutos. Dez componentes candidatos atendem a esse pedido, e juntos eles ocupam os cinco tipos.

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

Nenhum tipo ficou sem componente. O tipo que mais muda o trabalho de quem está na instituição é Processos, porque o CP4 e o CP5 mudam a rotina de fechamento e de correção de nota de professores, coordenações e Secretaria. Só a mudança de tecnologia não altera o prazo que o aluno percebe.

#### Os três níveis do R7

| Código | Elemento da situação atual | Nível |
| --- | --- | --- |
| N1 | Serviço de avaliação com resultado publicado no calendário acadêmico | Sistema de negócio |
| N2 | Calendário acadêmico que fixa a data de fechamento das notas | Sistema de negócio |
| N3 | Rotina de conferência manual das notas antes da publicação | Sistema de informação |
| N4 | Registros de nota entre professor, coordenação e Secretaria | Sistema de informação |
| N5 | Portal do professor e núcleo COBOL que calcula a situação do aluno | Sistema de TI |
| N6 | Exportação noturna por lote ao ambiente virtual | Sistema de TI |

Uma solução só no nível de sistema de TI troca o lote noturno por envio em minutos, mas deixa intactos o calendário de fechamento e a conferência manual, que decidem quando a nota está pronta para publicar. Por isso o aluno continua vendo a nota no prazo do fechamento.
<!--/gabarito-->
<!--/ex-->

<!--ex n=3 titulo="Papéis e responsabilidades do ciclo"-->
<!--campos-->
- **Responsável:** diga se cada tarefa, de T1 a T10, cabe ao arquiteto de solução, ao arquiteto de software ou à arquitetura corporativa.
- **Justificativa:** explique em uma frase por que a tarefa é desse responsável.
- **Grupo de competência:** nas tarefas do arquiteto de solução, diga se elas pedem competência de negócio, técnica, de entrega ou prática.
- **Benefício da tarefa T10:** escolha o benefício da abordagem arquitetural que justifica verificar se já existe um componente reaproveitável.
<!--/campos-->
<!--gabarito-->
#### Responsável por cada tarefa

O critério é o mesmo da classificação das decisões: até onde o efeito da tarefa chega.

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

Seis tarefas cabem ao arquiteto de solução, três ao arquiteto de software ou à equipe de desenvolvimento e uma à arquitetura corporativa. As seis tarefas do arquiteto de solução usam os quatro grupos de competência.

#### Benefício por trás da tarefa T10

A tarefa T10 se justifica pelo benefício do **reúso**: consultar o catálogo de aplicações e a arquitetura de software mostra se já existe um componente que serve ao novo uso. Sem essa verificação, a ACME especificaria e construiria um segundo componente de envio de mensagem, pagaria a duplicação de manutenção e de integração e perderia o custo e a perturbação mínimos que a análise de lacunas busca.
<!--/gabarito-->
<!--/ex-->

<!--ex n=4 titulo="Artefatos nas fases do processo, premissas e escopo"-->
<!--campos-->
- **Fase:** diga em que fase do processo cada artefato, de A1 a A10, é produzido ou usado.
- **Papel:** diga se o artefato é entrada, produto intermediário ou entregável.
- **Linha de base:** marque os artefatos que já existiam antes de o processo começar.
- **Seção do caderno:** diga em que seção do caderno o resultado de cada artefato fica registrado.
- **Dado do caso:** as premissas e as exclusões do escopo já vêm prontas, propostas pelo curso para você confirmar na descoberta.
<!--/campos-->
<!--gabarito-->
#### Artefatos nas fases do processo

Para dar um papel a cada artefato, use o critério do bloco 3. Entrada é o artefato que a fase recebe. Produto intermediário é a saída que alimenta uma fase seguinte. Entregável é a saída que o patrocinador recebe como resultado do trabalho do arquiteto. O documento de iniciação conta como entrada, e a comparação de alternativas é o caso de negócio levado ao Conselho, por isso é entregável da análise.

| Código | Artefato | Fase | Papel | Linha de base | Seção do caderno |
| --- | --- | --- | --- | --- | --- |
| A1 | Mapa de atores | 2. Descoberta | Entrada | Sim | 2 |
| A2 | Inventário dos componentes atuais | 2. Descoberta | Entrada | Sim | 4 |
| A3 | Catálogo de blocos de construção e interfaces | 4. Análise | Produto intermediário | Não | 7 |
| A4 | Registro da decisão da Reitoria de 12/03/2026 | 1. Iniciação | Entrada | Sim | 1 |
| A5 | Comparação de duas alternativas de modernização | 4. Análise | Entregável | Não | 7 |
| A6 | Modelo único de componentes da solução | 5. Desenho lógico | Entregável | Não | 7 |
| A7 | Sequência de extração dos módulos | 7. Desenvolvimento do roteiro | Entregável | Não | 9 |
| A8 | Lista de componentes acrescentados, removidos e alterados | 6. Validação | Produto intermediário | Não | 4 |
| A9 | Documento que autoriza a equipe a iniciar a investigação | 1. Iniciação | Entrada | Não | 1 |
| A10 | Modelos da solução implantada, devolvidos ao repositório | 8. Conclusão | Entregável | Não | Todas |

Os artefatos de linha de base são A1, A2 e A4, porque já descreviam parte da situação atual antes de o processo começar. O pedido da data de conclusão chega depois do A9, ainda na iniciação, e a data só pode ser dada com precisão depois da fase 7, em que saem as estimativas de prazo e de custo. Até lá, o caderno registra a data como pendência na seção 10.

#### Premissas

As premissas e as exclusões a seguir são dados do caso. O curso as propõe para você confirmar na fase de descoberta, e elas não fazem parte da resposta do exercício.

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
