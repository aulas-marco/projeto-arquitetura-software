# Gabarito do exercício 4

{{progresso:4}}

Este é o caderno da ACME depois do exercício 4. Ele reúne o que os exercícios 1 a 4 produziram, e a moldura âmbar marca o que o exercício 4 acrescentou. Compare com o seu caderno e veja onde as respostas diferem. O [enunciado do exercício 4](../modulo-1-fundamentos/bloco-4-processo-de-definicao-da-arquitetura.md#exercicio-4) está na página do bloco.

## A solução em uma página

{{novo}}

**O problema.** A ACME é uma universidade privada com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, com núcleo em COBOL, que custa R$ 15,83 milhões por ano e leva 34 dias úteis para colocar uma mudança em produção. Dos 6 especialistas em COBOL, 2 se aposentam em 2027.

**A pergunta.** Como evoluir o sistema acadêmico de forma segura e incremental, com o núcleo em operação durante a transição e respeitando os contratos já assumidos.

**A decisão central.** Ainda não há. O processo está na fase de descoberta, e a Reitoria já descartou a substituição integral e a reescrita em entrega única.

**O requisito que guia o desenho.** A definir na Aula 2, quando os requisitos declarados forem classificados e medidos.

**O que a organização aceita em troca.** A definir, depois da escolha do estilo na Aula 3.

**Como está o trabalho.** As decisões D1 a D9 estão classificadas por nível, as decisões D2, D3, D5, D6, D8 e D9 e as sete premissas estão **propostas**, e a data de conclusão do ciclo depende da fase 7 do processo.

{{/novo}}

## 1. Contexto

### 1.1 Instituição, restrições e decisões por nível

#### Instituição e pergunta central

Estes são os dados do caso que abrem o caderno. Eles já vêm preenchidos, porque não são resposta do exercício.

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

Restrição é uma decisão tomada por outra pessoa ou área, que o arquiteto precisa aceitar. As sete abaixo já chegam prontas ao projeto.

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

A tabela reúne as nove decisões que a ACME já tomou ou propôs. Para classificar cada uma, pergunte até onde o efeito da decisão chega. Se ela muda só o funcionamento interno de um componente de software, é de arquitetura de software. Se muda um processo, um papel, a responsabilidade por um dado ou a relação com um fornecedor, é de arquitetura de solução. Se vale para iniciativas que ainda nem existem, é de arquitetura corporativa.

| Código | Decisão | Nível | Justificativa |
| --- | --- | --- | --- |
| D1 | Identidade e autorização seguem padrões abertos, sem produto proprietário | Corporativa | Vale para qualquer iniciativa da universidade, inclusive as que ainda não existem |
| D2 | A propagação de nota ao ambiente virtual passa de lote diário a até 10 minutos | Solução | Muda o processo de fechamento de notas, o contrato com o fornecedor do ambiente virtual e a integração entre os sistemas |
| D3 | O serviço de notas repete o envio sem confirmação, com intervalo crescente | Software | Muda só o comportamento de um componente de software, e ninguém fora da equipe que o constrói precisa ser avisado |
| D4 | Nenhum dado pessoal de aluno é processado fora do território nacional | Corporativa | É regra do Jurídico para qualquer iniciativa que trate dado de aluno, hoje ou no futuro |
| D5 | A Secretaria Acadêmica passa a responder pela correção de dado cadastral | Solução | Muda quem responde pelo dado cadastral: sai a equipe de sustentação e entra a Secretaria Acadêmica |
| D6 | O índice de busca de disciplinas do portal passa a ficar em memória | Software | Muda só como um componente de software do portal funciona por dentro, sem efeito sobre processo, papel ou fornecedor |
| D7 | O núcleo COBOL permanece sob o contrato da fábrica até 30/09/2027 | Solução | Define quem pode mexer no núcleo: toda alteração passa pela fábrica de software, por contrato |
| D8 | O histórico escolar é emitido com assinatura digital no padrão ICP-Brasil | Solução | Muda o procedimento de emissão do histórico e depende de certificado de terceiro, mas não vale para iniciativas futuras |
| D9 | A transição ocorre por extração incremental de módulos, com o núcleo em operação | Solução | Afeta o contrato de sustentação, o calendário acadêmico e a rotina das equipes |

As decisões D1, D4 e D7 reproduzem as restrições fechadas RT4, RT5 e RT6. As decisões D2, D3, D5, D6, D8 e D9 estão **propostas** e dependem de validação com as partes interessadas.

#### Componente da solução afetado

Nas decisões de solução, a tabela mostra quais componentes da solução são atingidos além da tecnologia (pessoas, estruturas organizacionais, processos e informação).

| Código | Tipo de componente da solução | Efeito |
| --- | --- | --- |
| D2 | Processos | O fechamento de notas deixa de depender da janela noturna de lote |
| D5 | Estruturas organizacionais | A correção de dado cadastral sai da equipe de sustentação, terceirizada, e passa à Secretaria Acadêmica |
| D7 | Estruturas organizacionais | O contrato com a fábrica de software, organização parceira, define quem pode alterar o núcleo |
| D8 | Processos | A emissão do histórico escolar passa a ter a assinatura digital como etapa do procedimento |
| D9 | Processos | A rotina de cada equipe muda a cada módulo extraído, no ritmo do calendário acadêmico |

#### Dependência entre decisões

A decisão D3 depende da D2. Sem a D2, o reenvio seria desenhado para um percurso em lote noturno, em que cada nova tentativa só acontece na janela seguinte. Nesse percurso, o intervalo crescente entre tentativas não tem prazo de propagação que o justifique, e a nota continua chegando ao aluno no dia seguinte.

### 1.2 Componentes da solução do R7

#### Componentes da solução do R7

O R7 pede que a nota lançada pelo professor chegue ao ambiente virtual de aprendizagem em até 10 minutos. Dez candidatos a componente da solução atendem a esse pedido, e juntos eles ocupam os cinco tipos (pessoas, estruturas organizacionais, processos, informação e tecnologia).

| Código | Componente da solução | Tipo |
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

Nenhum tipo ficou sem componente da solução. O tipo que mais muda o trabalho de quem está na instituição é Processos, porque o CP4 e o CP5 mudam a rotina de fechamento e de correção de nota de professores, coordenações e Secretaria. Só a mudança de tecnologia não altera o prazo que o aluno percebe.

#### Os três níveis do R7

Cada elemento da situação atual pertence a um destes três níveis: o negócio, a informação ou a TI.

| Código | Elemento da situação atual | Nível |
| --- | --- | --- |
| N1 | Serviço de avaliação com resultado publicado no calendário acadêmico | Sistema de negócio |
| N2 | Calendário acadêmico que fixa a data de fechamento das notas | Sistema de negócio |
| N3 | Rotina de conferência manual das notas antes da publicação | Sistema de informação |
| N4 | Registros de nota entre professor, coordenação e Secretaria | Sistema de informação |
| N5 | Portal do professor e núcleo COBOL que calcula a situação do aluno | Sistema de TI |
| N6 | Exportação noturna por lote ao ambiente virtual | Sistema de TI |

Uma solução só no nível de sistema de TI troca o lote noturno por envio em minutos, mas deixa intactos o calendário de fechamento e a conferência manual, que decidem quando a nota está pronta para publicar. Por isso o aluno continua vendo a nota no prazo do fechamento.

### 1.3 Papéis e responsabilidades do ciclo

#### Responsável por cada tarefa

O critério é o mesmo da classificação das decisões: até onde o efeito da tarefa chega.

| Código | Tarefa | Responsável | Grupo de competência | Justificativa |
| --- | --- | --- | --- | --- |
| T1 | Entrevistar a Pró-Reitoria de Graduação e a Educação a Distância | Arquiteto de solução | Prático | Levantar o que cada área precisa é tratamento de requisitos e gestão de partes interessadas |
| T2 | Definir a consistência de dado entre o serviço extraído e o núcleo | Arquiteto de software | | Decide como o módulo extraído se comporta por dentro durante a coexistência |
| T3 | Estimar o custo da mudança tecnológica do primeiro ciclo | Arquiteto de solução | Entrega | A estimativa de custo é uma das três saídas da arquitetura de solução |
| T4 | Escolher a estrutura de dados do serviço de matrícula | Arquiteto de software | | Altera só a estrutura interna de um componente de software |
| T5 | Negociar com a fábrica a abertura de interfaces no núcleo | Arquiteto de solução | Prático | Muda a relação com o fornecedor e exige negociação com partes interessadas |
| T6 | Redigir a política institucional de dado pessoal de aluno | Arquitetura corporativa | | Vale para qualquer sistema da universidade, presente ou futuro |
| T7 | Produzir o roteiro de entrega do ciclo | Arquiteto de solução | Entrega | O roteiro de entrega é uma das três saídas da arquitetura de solução |
| T8 | Decidir que a Secretaria responde pela correção de dado cadastral | Arquiteto de solução | Negócio | Muda papel e propriedade de dado, o que exige leitura do modelo operacional |
| T9 | Configurar o servidor de integração contínua | Arquiteto de software | | É configuração de ferramenta da equipe de desenvolvimento |
| T10 | Verificar se já existe componente de software de envio de mensagem reaproveitável | Arquiteto de solução | Técnico | Exige conhecer a tecnologia vigente antes de especificar componente de software novo |

Seis tarefas cabem ao arquiteto de solução, três ao arquiteto de software ou à equipe de desenvolvimento e uma à arquitetura corporativa. As seis tarefas do arquiteto de solução usam os quatro grupos de competência.

#### Benefício por trás da tarefa T10

A tarefa T10 se justifica pelo benefício do **reúso**: consultar o catálogo de aplicações e a arquitetura de software mostra se já existe um componente de software que serve ao novo uso. Sem essa verificação, a ACME especificaria e construiria um segundo componente de software de envio de mensagem, pagaria a duplicação de manutenção e de integração e perderia o custo e a perturbação mínimos que a análise de lacunas busca.

### 1.4 Artefatos nas fases do processo, premissas e escopo

{{novo}}

#### Artefatos nas fases do processo

Para dar um papel a cada artefato, use o critério do bloco 3. Entrada é o artefato que a fase recebe. Produto intermediário é a saída que alimenta uma fase seguinte. Entregável é a saída que o patrocinador recebe como resultado do trabalho do arquiteto. O documento de iniciação conta como entrada, e a comparação de alternativas é o caso de negócio levado ao Conselho, por isso é entregável da análise.

| Código | Artefato | Fase | Papel | Linha de base | Seção do caderno |
| --- | --- | --- | --- | --- | --- |
| A1 | Mapa de atores | 2. Descoberta | Entrada | Sim | 2 |
| A2 | Inventário dos componentes de software atuais | 2. Descoberta | Entrada | Sim | 4 |
| A3 | Catálogo de blocos de construção e interfaces | 4. Análise | Produto intermediário | Não | 7 |
| A4 | Registro da decisão da Reitoria de 12/03/2026 | 1. Iniciação | Entrada | Sim | 1 |
| A5 | Comparação de duas alternativas de modernização | 4. Análise | Entregável | Não | 7 |
| A6 | Modelo único de componentes da solução | 5. Desenho lógico | Entregável | Não | 7 |
| A7 | Sequência de extração dos módulos | 7. Desenvolvimento do roteiro | Entregável | Não | 9 |
| A8 | Lista de componentes da solução acrescentados, removidos e alterados | 6. Validação | Produto intermediário | Não | 4 |
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

{{/novo}}

## 10. O que ainda falta decidir

{{novo}}

| Pendência | Quem decide | Quando se resolve |
| --- | --- | --- |
| Data de conclusão do ciclo | Reitoria, candidata a patrocinadora, com o roteiro autorizado | Fase 7, desenvolvimento do roteiro |
| Nomeação do patrocinador de negócio | Reitoria | Antes da fase 3, definição do esboço da solução |
| Validação das decisões propostas D2, D3, D5, D6, D8 e D9 | Partes interessadas da seção 2 | Fase 6, validação |
| Confirmação das premissas PR1 a PR7 | Responsáveis indicados na coluna Como verificar | Fase 2, descoberta |

{{/novo}}

Ainda em branco, para os próximos exercícios: 2. Partes interessadas, 3. Requisitos, 4. Linha de base e lacunas, 5. Contexto do sistema (C4, nível 1), 6. Princípios, 7. Decisões, 8. Tecnologia e plataforma, 9. Roteiro e governança
