# Gabarito do exercício 4

{{progresso:4}}

Depois do exercício 4, o caderno da ACME reúne o que os exercícios 1 a 4 produziram, e a moldura âmbar marca o que o exercício 4 acrescentou. Compare com o seu caderno para ver onde as suas respostas diferem. O [enunciado do exercício 4](../modulo-1-fundamentos/bloco-4-processo-de-definicao-da-arquitetura.md#exercicio-4) está na página do bloco.

## A solução em uma página

<details class="caderno-secao" markdown="1" open>
<summary>Atualizada neste exercício</summary>

{{novo}}

**O problema.** A ACME é uma universidade privada com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, com núcleo em COBOL, que custa R$ 15,83 milhões por ano e leva 34 dias úteis para colocar uma mudança em produção. A situação se agrava porque, dos 6 especialistas em COBOL que o sustentam, 2 se aposentam em 2027.

**A pergunta.** Diante desse quadro, o projeto pergunta como evoluir o sistema acadêmico de forma segura e incremental, com o núcleo em operação durante a transição e respeitando os contratos já assumidos.

**A decisão.** Ainda não há. O processo está na fase de descoberta, e a Reitoria já descartou a substituição integral e a reescrita em entrega única.

**O que mais pesa no desenho.** A definir na Aula 2, quando as exigências do projeto forem classificadas e medidas.

**Consequências.** A definir, depois da escolha do estilo de arquitetura na Aula 3.

**Como está o trabalho.** As nove decisões levantadas estão classificadas por nível. Seis delas, assim como as sete premissas, ainda são propostas e precisam de validação das partes interessadas. A data de conclusão do ciclo depende da fase 7 do processo.

{{/novo}}

</details>

## 1. Contexto

<details class="caderno-secao" markdown="1" open>
<summary>Atualizada neste exercício</summary>

### 1.1 Instituição, restrições e decisões por nível

<details class="caderno-secao" markdown="1">
<summary>Construída no exercício 1. Clique para abrir</summary>

#### Instituição e pergunta central

Todo caderno começa por quem é a ACME e por qual problema ela quer resolver. Esses dados vêm do dossiê do caso e já aparecem preenchidos no seu caderno, porque o exercício não pede que você os produza.

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

O problema do projeto cabe numa pergunta: como evoluir o sistema acadêmico de forma segura e incremental, mantendo o núcleo em operação durante a transição? Em 12/03/2026, a Reitoria já descartou duas respostas. Uma é a substituição integral por um produto de mercado, que exigiria migrar os históricos de 214.000 egressos. A outra é a reescrita em uma única entrega, porque nenhuma janela do calendário acadêmico comporta a virada de todos os módulos de uma vez.

#### Restrições que chegam fechadas

Antes de desenhar qualquer coisa, o arquiteto descobre o que não pode mudar. São as restrições: decisões que outras pessoas ou áreas da ACME já tomaram e que o projeto precisa aceitar como estão. As sete abaixo chegam prontas, e cada uma diz quem a tomou e o que ela impõe à arquitetura.

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

A tabela traz as nove decisões que a ACME já tomou ou propôs, cada uma com o nível de arquitetura a que pertence. Para chegar a esse nível, ajuda perguntar até onde o efeito da decisão alcança. Quando ela mexe só no funcionamento interno de um componente de software, é uma decisão de arquitetura de software. Quando muda um processo, um papel, a responsabilidade por um dado ou a relação com um fornecedor, é de arquitetura de solução. E quando vale também para iniciativas que ainda nem existem, é de arquitetura corporativa.

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

As decisões da tabela não têm todas o mesmo estado. Três apenas repetem restrições que chegaram prontas: os padrões abertos de identidade (D1, vinda da restrição RT4), o dado pessoal em território nacional (D4, vinda da RT5) e o núcleo COBOL sob contrato (D7, vinda da RT6). As outras seis estão **propostas** e ainda dependem de validação com as partes interessadas: a nota em até 10 minutos (D2), o reenvio com intervalo crescente (D3), a correção cadastral pela Secretaria Acadêmica (D5), o índice de busca em memória (D6), a assinatura digital do histórico (D8) e a extração incremental de módulos (D9).

#### Componente da solução afetado

Quando a ACME decide algo como mudar o prazo da nota, a decisão quase nunca é só técnica. A tabela a seguir mostra, para cada decisão de solução, que componentes da solução ela atinge além da tecnologia (pessoas, estruturas organizacionais, processos e informação).

| Código | Tipo do componente da solução | Efeito |
| --- | --- | --- |
| D2 | Processos | O fechamento de notas deixa de depender da janela noturna de lote |
| D5 | Estruturas organizacionais | A correção de dado cadastral sai da equipe de sustentação, terceirizada, e passa à Secretaria Acadêmica |
| D7 | Estruturas organizacionais | O contrato com a fábrica de software, organização parceira, define quem pode alterar o núcleo |
| D8 | Processos | A emissão do histórico escolar passa a ter a assinatura digital como etapa do procedimento |
| D9 | Processos | A rotina de cada equipe muda a cada módulo extraído, no ritmo do calendário acadêmico |

#### Dependência entre decisões

O reenvio com intervalo crescente (D3) só faz sentido depois da decisão de levar a nota ao ambiente virtual em até 10 minutos (D2). Imagine decidir o reenvio com intervalo crescente quando a nota ainda segue por um lote noturno: cada nova tentativa só aconteceria na janela seguinte, e esperar mais entre as tentativas não aproximaria a nota do aluno, que continuaria chegando no dia seguinte. Só depois que essa decisão fixa o prazo de 10 minutos o intervalo entre as tentativas passa a ter o que o justifique.

</details>

### 1.2 Os componentes da solução, num exemplo da ACME

<details class="caderno-secao" markdown="1">
<summary>Construída no exercício 2. Clique para abrir</summary>

#### Um exemplo da ACME: a nota que precisa chegar em 10 minutos

Um exemplo da ACME mostra como uma solução se reúne em componentes da solução. A Coordenação de Educação a Distância quer que a nota lançada pelo professor chegue ao ambiente virtual de aprendizagem em até 10 minutos. Hoje a nota só chega no dia seguinte, em um envio noturno, e a cada fechamento algum aluno reclama. O dossiê registra esse pedido com o código R7. Para atendê-lo, a ACME listou dez candidatos a componente da solução, e eles se distribuem pelos cinco tipos (pessoas, estruturas organizacionais, processos, informação e tecnologia), dois em cada um.

| Código | Tipo do componente da solução | Componente da solução |
| --- | --- | --- |
| CP1 | Pessoas | Treinamento dos professores para publicação imediata da nota |
| CP2 | Estruturas organizacionais | Aditivo ao contrato do ambiente virtual, com troca para o plano que oferece interfaces de programação |
| CP3 | Estruturas organizacionais | Acordo de nível de serviço de 10 minutos entre a Diretoria de TI e a Coordenação de Educação a Distância |
| CP4 | Processos | Procedimento de correção de nota já publicada |
| CP5 | Processos | Fechamento de notas sem dependência da janela noturna de lote |
| CP6 | Informação | Registro de cada envio, com horário de lançamento e de confirmação |
| CP7 | Informação | Mensagem de nota lançada, com aluno, turma, avaliação e valor |
| CP8 | Tecnologia | Mensageria entre o núcleo acadêmico e o ambiente virtual |
| CP9 | Tecnologia | Serviço de notas que publica um evento a cada lançamento |
| CP10 | Pessoas | Responsável na Coordenação de Educação a Distância pelas falhas de envio |

Nenhum dos cinco tipos ficou vazio, o que mostra que a solução não depende só de tecnologia. O tipo que mais muda o trabalho de quem está na instituição é Processos, porque o procedimento de correção de nota já publicada (CP4) e o fechamento sem dependência da janela noturna (CP5) mexem na rotina de professores, coordenações e Secretaria, e por isso trocar apenas a tecnologia não altera o prazo que o aluno percebe.

#### Os fatos da situação atual, em três níveis

Para saber onde o prazo da nota se forma, os seis fatos da situação atual podem ser lidos em três níveis, do mais amplo ao mais técnico: o negócio, a informação e a TI.

| Código | Elemento da situação atual | Nível |
| --- | --- | --- |
| N1 | Serviço de avaliação com resultado publicado no calendário acadêmico | Sistema de negócio |
| N2 | Calendário acadêmico que fixa a data de fechamento das notas | Sistema de negócio |
| N3 | Rotina de conferência manual das notas antes da publicação | Sistema de informação |
| N4 | Registros de nota entre professor, coordenação e Secretaria | Sistema de informação |
| N5 | Portal do professor e núcleo COBOL que calcula a situação do aluno | Sistema de TI |
| N6 | Exportação noturna por lote ao ambiente virtual | Sistema de TI |

Imagine uma solução que atue só no nível de sistema de TI. Ela troca o lote noturno por um envio em minutos, mas deixa intactos o calendário de fechamento e a conferência manual, que são os que decidem quando a nota está pronta para publicar. O aluno continua vendo a nota no prazo do fechamento.

</details>

### 1.3 Papéis e responsabilidades do ciclo

<details class="caderno-secao" markdown="1">
<summary>Construída no exercício 3. Clique para abrir</summary>

#### Responsável por cada tarefa

Para dividir as tarefas, vale a mesma pergunta usada nas decisões: até onde o efeito da tarefa chega?

| Código | Tarefa | Responsável | Grupo de competência | Justificativa |
| --- | --- | --- | --- | --- |
| TA1 | Entrevistar a Pró-Reitoria de Graduação e a Educação a Distância | Arquiteto de solução | Prático | Levantar o que cada área precisa é tratamento de requisitos e gestão de partes interessadas |
| TA2 | Definir a consistência de dado entre o serviço extraído e o núcleo | Arquiteto de software | | Decide como o módulo extraído se comporta por dentro durante a coexistência |
| TA3 | Estimar o custo da mudança tecnológica do primeiro ciclo | Arquiteto de solução | Entrega | A estimativa de custo é uma das três saídas da arquitetura de solução |
| TA4 | Escolher a estrutura de dados do serviço de matrícula | Arquiteto de software | | Altera só a estrutura interna de um componente de software |
| TA5 | Negociar com a fábrica a abertura de interfaces no núcleo | Arquiteto de solução | Prático | Muda a relação com o fornecedor e exige negociação com partes interessadas |
| TA6 | Redigir a política institucional de dado pessoal de aluno | Arquitetura corporativa | | Vale para qualquer sistema da universidade, presente ou futuro |
| TA7 | Produzir o roteiro de entrega do ciclo | Arquiteto de solução | Entrega | O roteiro de entrega é uma das três saídas da arquitetura de solução |
| TA8 | Decidir que a Secretaria responde pela correção de dado cadastral | Arquiteto de solução | Negócio | Muda papel e propriedade de dado, o que exige leitura do modelo operacional |
| TA9 | Configurar o servidor de integração contínua | Arquiteto de software | | É configuração de ferramenta da equipe de desenvolvimento |
| TA10 | Verificar se já existe componente de software de envio de mensagem reaproveitável | Arquiteto de solução | Técnico | Exige conhecer a tecnologia vigente antes de especificar componente de software novo |

Dividido o ciclo, seis tarefas cabem ao arquiteto de solução, três ao arquiteto de software ou à equipe de desenvolvimento e uma à arquitetura corporativa. As seis tarefas do arquiteto de solução usam os quatro grupos de competência, o que mostra o quanto o papel exige de habilidades diferentes.

#### A justificativa de reaproveitar um componente de software de envio de mensagem

A tarefa de verificar se já existe componente de software de envio de mensagem reaproveitável (TA10) se justifica pelo benefício do **reuso**. Antes de especificar algo novo, o arquiteto consulta o catálogo de aplicações e a arquitetura de software para saber se já existe um componente de software que sirva ao novo uso. Sem essa verificação, a ACME acabaria construindo um segundo componente de envio de mensagem, pagaria duas vezes pela manutenção e pela integração e faria uma mudança maior do que o necessário.

</details>

### 1.4 Artefatos nas fases do processo, premissas e escopo

{{novo}}

#### Artefatos nas fases do processo

Para dar um papel a cada artefato, ajuda pensar no caminho que ele faz. Alguns já existem quando a fase começa, como o mapa de atores, e a fase só os recebe e usa: são as entradas. Outros nascem no meio do trabalho e servem de matéria-prima para a fase seguinte, como o catálogo de blocos de construção e interfaces: são os produtos intermediários. E há os que o arquiteto entrega ao patrocinador como resultado do seu trabalho, como o modelo único de componentes da solução: são os entregáveis. Dois casos pedem um pouco mais de cuidado. O documento que autoriza a equipe a investigar conta como entrada, porque é com ele em mãos que a equipe começa. E a comparação das duas alternativas é o caso de negócio que o Conselho Universitário recebe para decidir, por isso é um entregável da fase de análise.

| Código | Artefato | Fase | Papel | Linha de base | Seção do caderno |
| --- | --- | --- | --- | --- | --- |
| AR1 | Mapa de atores | 2. Descoberta | Entrada | Sim | 2 |
| AR2 | Inventário dos componentes de software atuais | 2. Descoberta | Entrada | Sim | 4 |
| AR3 | Catálogo de blocos de construção e interfaces | 4. Análise | Produto intermediário | Não | 7 |
| AR4 | Registro da decisão da Reitoria de 12/03/2026 | 1. Iniciação | Entrada | Sim | 1 |
| AR5 | Comparação de duas alternativas de modernização | 4. Análise | Entregável | Não | 7 |
| AR6 | Modelo único de componentes da solução | 5. Desenho lógico | Entregável | Não | 7 |
| AR7 | Sequência de extração dos módulos | 7. Desenvolvimento do roteiro | Entregável | Não | 9 |
| AR8 | Lista de componentes da solução acrescentados, removidos e alterados | 6. Validação | Produto intermediário | Não | 4 |
| AR9 | Documento que autoriza a equipe a iniciar a investigação | 1. Iniciação | Entrada | Não | 1 |
| AR10 | Modelos da solução implantada, devolvidos ao repositório | 8. Conclusão | Entregável | Não | Todas |

Três artefatos já existiam antes de o processo começar e descrevem parte da situação atual: o mapa de atores (AR1), o inventário dos componentes de software atuais (AR2) e o registro da decisão da Reitoria de 12/03/2026 (AR4). Eles formam a linha de base. Quanto à data de conclusão do trabalho, o pedido da Reitoria chega logo depois do documento que autoriza a investigação (AR9), ainda na iniciação, mas a data só pode ser dada com precisão depois da fase 7, de desenvolvimento do roteiro, quando saem as estimativas de prazo e de custo. Até lá, o caderno registra a data como pendência na seção 10, a de pendências.

#### Premissas

As premissas e as exclusões a seguir também são dados do caso. O curso as propõe para você confirmar na fase de descoberta, e por isso elas não fazem parte da resposta do exercício.

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

</details>

## 10. O que ainda falta decidir

<details class="caderno-secao" markdown="1" open>
<summary>Atualizada neste exercício</summary>

{{novo}}

| Pendência | Quem decide | Quando se resolve |
| --- | --- | --- |
| Data de conclusão do ciclo | Reitoria, candidata a patrocinadora, com o roteiro autorizado | Fase 7, desenvolvimento do roteiro |
| Nomeação do patrocinador de negócio | Reitoria | Antes da fase 3, definição do esboço da solução |
| Validação das seis decisões ainda propostas (D2, D3, D5, D6, D8 e D9) | Partes interessadas da seção 2 | Fase 6, validação |
| Confirmação das sete premissas (PR1 a PR7), as hipóteses assumidas sem confirmação | Responsáveis indicados na coluna Como verificar | Fase 2, descoberta |

{{/novo}}

</details>

Ainda em branco, para os próximos exercícios: 2. Partes interessadas, 3. Requisitos, 4. Linha de base e lacunas, 5. Contexto do sistema (C4, nível 1), 6. Princípios, 7. Decisões, 8. Tecnologia e plataforma, 9. Roteiro e governança
