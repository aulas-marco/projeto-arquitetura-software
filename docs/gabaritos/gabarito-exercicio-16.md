# Gabarito do exercício 16

{{progresso:16}}

Este é o caderno da ACME depois do exercício 16. Ele reúne o que os exercícios 1 a 16 produziram, e a moldura âmbar marca o que o exercício 16 acrescentou. Compare com o seu caderno e veja onde as respostas diferem. O [enunciado do exercício 16](../modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md#exercicio-16) está na página do bloco.

## A solução em uma página

{{novo}}

**O problema.** A ACME é uma universidade privada com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, com núcleo em COBOL, que custa R$ 15,83 milhões por ano e leva 34 dias úteis para colocar uma mudança em produção. Dos 6 especialistas em COBOL, 2 se aposentam em 2027.

**A pergunta.** Como evoluir o sistema acadêmico de forma segura e incremental, com o núcleo em operação durante a transição e respeitando os contratos já assumidos.

**A decisão central.** A do ADR 001, a arquitetura orientada a eventos na entrada da matrícula. Os domínios de negócio, de dados, de aplicações e de integração já têm o efeito do primeiro ciclo registrado, com o diagrama de contexto e o de contêineres da arquitetura alvo.

**O requisito que guia o desenho.** O R6 para a matrícula e o R7 para a nota. A relação entre o serviço de notas e o ambiente virtual é assíncrona, e o núcleo COBOL, que a equipe da ACME não pode alterar até 30/09/2027, permanece como sistema de registro.

**O que a organização aceita em troca.** A confirmação assíncrona da matrícula e a dependência da fábrica de software para gravar o evento junto com a nota no programa COBOL.

**Como está o trabalho.** A arquitetura de negócio, de dados, de aplicações e de integração está registrada. Faltam a infraestrutura e a tecnologia, e os pontos sem informação no dossiê constam como pendências.

{{/novo}}

## 1. Contexto

### 1.1 Instituição, restrições e decisões por nível

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

As decisões da tabela não têm todas o mesmo estado. D1, D4 e D7 apenas repetem restrições que chegaram prontas (RT4, RT5 e RT6). As outras seis, D2, D3, D5, D6, D8 e D9, estão **propostas**: ainda dependem de validação com as partes interessadas.

#### Componente da solução afetado

Uma decisão de solução quase nunca é só técnica. A tabela a seguir mostra, para cada uma delas, que componentes da solução ela atinge além da tecnologia (pessoas, estruturas organizacionais, processos e informação).

| Código | Tipo do componente da solução | Efeito |
| --- | --- | --- |
| D2 | Processos | O fechamento de notas deixa de depender da janela noturna de lote |
| D5 | Estruturas organizacionais | A correção de dado cadastral sai da equipe de sustentação, terceirizada, e passa à Secretaria Acadêmica |
| D7 | Estruturas organizacionais | O contrato com a fábrica de software, organização parceira, define quem pode alterar o núcleo |
| D8 | Processos | A emissão do histórico escolar passa a ter a assinatura digital como etapa do procedimento |
| D9 | Processos | A rotina de cada equipe muda a cada módulo extraído, no ritmo do calendário acadêmico |

#### Dependência entre decisões

A D3 só faz sentido depois da D2. Imagine decidir o reenvio com intervalo crescente quando a nota ainda segue por um lote noturno: cada nova tentativa só aconteceria na janela seguinte, e esperar mais entre as tentativas não aproximaria a nota do aluno, que continuaria chegando no dia seguinte. Só depois que a D2 fixa o prazo de 10 minutos o intervalo entre as tentativas passa a ter o que o justifique.

### 1.2 Os componentes da solução, num exemplo da ACME

#### Um exemplo da ACME: a nota que precisa chegar em 10 minutos

Para ver como uma solução se divide em componentes da solução (pessoas, áreas, processos, informação e tecnologia), vale um exemplo concreto da ACME. A Coordenação de Educação a Distância quer que a nota lançada pelo professor chegue ao ambiente virtual de aprendizagem em até 10 minutos. Hoje a nota só chega no dia seguinte, em um envio noturno, e a cada fechamento algum aluno reclama. No dossiê, esse pedido tem o código R7. Para atendê-lo, a ACME listou dez candidatos a componente da solução, e eles se distribuem pelos cinco tipos (pessoas, estruturas organizacionais, processos, informação e tecnologia), dois em cada um.

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

Nenhum dos cinco tipos ficou vazio, e isso é bom sinal: a solução não depende só de tecnologia. O tipo que mais muda o trabalho de quem está na instituição é Processos, porque o CP4 e o CP5 mexem na rotina de fechamento e de correção de nota de professores, coordenações e Secretaria. Trocar apenas a tecnologia não altera o prazo que o aluno percebe.

#### Os fatos da situação atual, em três níveis

Os seis fatos sobre a situação atual podem ser lidos em três níveis, do mais amplo ao mais técnico: o negócio, a informação e a TI.

| Código | Elemento da situação atual | Nível |
| --- | --- | --- |
| N1 | Serviço de avaliação com resultado publicado no calendário acadêmico | Sistema de negócio |
| N2 | Calendário acadêmico que fixa a data de fechamento das notas | Sistema de negócio |
| N3 | Rotina de conferência manual das notas antes da publicação | Sistema de informação |
| N4 | Registros de nota entre professor, coordenação e Secretaria | Sistema de informação |
| N5 | Portal do professor e núcleo COBOL que calcula a situação do aluno | Sistema de TI |
| N6 | Exportação noturna por lote ao ambiente virtual | Sistema de TI |

Imagine uma solução que atue só no nível de sistema de TI. Ela troca o lote noturno por um envio em minutos, mas deixa intactos o calendário de fechamento e a conferência manual, que são os que decidem quando a nota está pronta para publicar. O aluno continua vendo a nota no prazo do fechamento.

### 1.3 Papéis e responsabilidades do ciclo

#### Responsável por cada tarefa

Para dividir as tarefas, vale a mesma pergunta usada nas decisões: até onde o efeito da tarefa chega?

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

No total, seis tarefas cabem ao arquiteto de solução, três ao arquiteto de software ou à equipe de desenvolvimento e uma à arquitetura corporativa. Repare que as seis tarefas do arquiteto de solução usam os quatro grupos de competência, o que mostra o quanto o papel exige de habilidades diferentes.

#### Benefício por trás da tarefa T10

A tarefa T10 se justifica pelo benefício do **reúso**. Antes de especificar algo novo, o arquiteto consulta o catálogo de aplicações e a arquitetura de software para saber se já existe um componente de software que sirva ao novo uso. Sem essa verificação, a ACME acabaria construindo um segundo componente de envio de mensagem, pagaria duas vezes pela manutenção e pela integração e faria uma mudança maior do que o necessário.

### 1.4 Artefatos nas fases do processo, premissas e escopo

#### Artefatos nas fases do processo

Para dar um papel a cada artefato, ajuda pensar no caminho que ele faz. Alguns já existem quando a fase começa, como o mapa de atores, e a fase só os recebe e usa: são as entradas. Outros nascem no meio do trabalho e servem de matéria-prima para a fase seguinte, como o catálogo de blocos de construção e interfaces: são os produtos intermediários. E há os que o arquiteto entrega ao patrocinador como resultado do seu trabalho, como o modelo único de componentes da solução: são os entregáveis. Dois casos pedem um pouco mais de cuidado. O documento que autoriza a equipe a investigar conta como entrada, porque é com ele em mãos que a equipe começa. E a comparação das duas alternativas é o caso de negócio que o Conselho Universitário recebe para decidir, por isso é um entregável da fase de análise.

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

Três artefatos já existiam antes de o processo começar e descrevem parte da situação atual: A1, A2 e A4. Eles formam a linha de base. Quanto à data de conclusão, o pedido chega logo depois do A9, ainda na iniciação, mas a data só pode ser dada com precisão depois da fase 7, quando saem as estimativas de prazo e de custo. Até lá, o caderno registra a data como pendência na seção 10.

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

## 2. Partes interessadas

### 2.1 Partes interessadas, pontos de vista e escopo do primeiro ciclo

#### Categoria de cada papel

A Reitora quer resultado em 12 meses, o Diretor Financeiro teme pagar duas vezes e o Gerente de sustentação teme perder o contrato. Para saber como falar com cada um, o arquiteto enquadrou os oito papéis nas nove categorias de parte interessada, e os papéis que acumulam funções aparecem com uma observação.

| Papel | Categoria | Observação |
| --- | --- | --- |
| Reitora | Donos do negócio e gestores seniores | Exerce o patrocínio do negócio |
| Pró-Reitora de Graduação | Donos do negócio e gestores seniores | Responde pelo processo acadêmico afetado e tem atores de negócio sob sua responsabilidade |
| Diretor de TI | Arquitetura corporativa e subdomínios | Também participa do desenho, e esse acúmulo de papéis precisa ser declarado |
| Diretor Financeiro | Donos do negócio e gestores seniores | Decide sobre o desembolso, e não sobre o desenho |
| Gerente de sustentação da fábrica | Fornecedores de produto e serviço | Tem interesse comercial contrário à internalização do conhecimento do núcleo |
| Coordenadora de Educação a Distância | Usuários finais e atores de negócio | Opera o processo afetado |
| Encarregada de proteção de dados | Reguladores e entidades setoriais | Função de conformidade, que responde dentro da instituição por uma exigência vinda de fora |
| Representação discente | Clientes e usuários dos serviços | Recebe o serviço afetado |

A patrocinadora de negócio é a Reitora, porque tem a autoridade sobre os R$ 6,2 milhões, tomou a decisão de 12/03/2026 que fechou duas alternativas e responde pelo resultado na avaliação regulatória.

#### Categorias sem representante

Depois de classificar os papéis, o arquiteto fez o caminho inverso e perguntou quem fala por cada categoria. Duas categorias ficaram sem ninguém, e a segunda tabela mostra o que isso custa ao processo.

| Categoria | Papel do mapa de atores que a representa |
| --- | --- |
| Donos do negócio e gestores seniores | Reitora, Pró-Reitora de Graduação e Diretor Financeiro |
| Patrocinador de negócio | Reitora |
| Usuários finais e atores de negócio | Coordenadora de Educação a Distância |
| Clientes e usuários dos serviços | Representação discente |
| Arquitetura corporativa e subdomínios | Diretor de TI, que acumula esse papel porque a ACME não tem uma arquitetura corporativa formal no mapa |
| Participantes do desenho | Diretor de TI |
| Participantes da implantação | Sem representante |
| Fornecedores de produto e serviço | Gerente de sustentação da fábrica |
| Reguladores e entidades setoriais | Sem representante externo, porque a Encarregada de proteção de dados fala só pela instituição e o órgão que conduz a avaliação do curso não aparece no mapa |

| Categoria sem representante | Risco da ausência |
| --- | --- |
| Participantes da implantação | O desenho pode sair sem quem o construa e o sustente depois da internalização, e a operação só recusa o que foi desenhado quando já é tarde para mudar |
| Reguladores e entidades setoriais | A exigência externa chega depois da decisão, quando o custo de mudar o desenho já é alto |

#### Pontos de vista de três papéis

O Diretor Financeiro, a Pró-Reitora e o Gerente de sustentação olham para o mesmo sistema com medos diferentes, e por isso cada um recebe um recorte próprio da descrição de arquitetura. A preocupação principal de cada um vem da coluna O que teme do mapa de atores.

| Papel | Preocupação principal | Critério de seleção | Estrutura do artefato | Forma de apresentação |
| --- | --- | --- | --- | --- |
| Diretor Financeiro | Pagar o legado e a nuvem no mesmo exercício | Componentes com custo e contrato associados | Tabela de desembolso por exercício | Comparação com o plano plurianual já provisionado |
| Pró-Reitora de Graduação | Repetir o incidente na janela de matrícula e prorrogar de novo o prazo | Componentes que estão no caminho crítico da matrícula | Fluxo do processo com os pontos de falha marcados | Duas versões comparáveis, a atual e a pretendida |
| Gerente de sustentação da fábrica | Perder receita e escopo com a internalização do conhecimento do núcleo | Programas sob contrato e interfaces afetadas | Lista de programas com as chamadas que mudam | Marcação do que muda antes e depois de 30/09/2027 |

#### Declaração de escopo do primeiro ciclo

Para o primeiro ciclo caber nos R$ 6,2 milhões e nos 12 meses, o arquiteto separou o que a mudança toca do que ela deixa como está, e anotou quem decidiu cada exclusão para que ninguém a reabra sem saber de onde veio. A correção do dado cadastral de aluno (E10) muda porque a Aula 1 decidiu, na decisão D5, passá-la da equipe de sustentação à Secretaria Acadêmica.

| Código | Elemento | Muda ou permanece | Origem da exclusão |
| --- | --- | --- | --- |
| E1 | Integração de notas e turmas com o ambiente virtual de aprendizagem | Muda, desde que a Reitoria aprove o plano superior do ambiente virtual, que traz as interfaces de programação | Não se aplica |
| E2 | Ambiente virtual de aprendizagem | Permanece | Restrição RT2, decisão da Reitoria de 12/03/2026 |
| E3 | ERP financeiro | Permanece | Restrição RT2, decisão da Reitoria de 12/03/2026 |
| E4 | Programas COBOL do núcleo acadêmico | Permanece | Restrição RT6, contrato de sustentação até 30/09/2027 |
| E5 | Portal do aluno, na renovação de matrícula pelo telefone celular | Muda | Não se aplica |
| E6 | Autenticação de alunos e professores por padrões abertos | Muda | Não se aplica |
| E7 | Trilha de auditoria de leitura de dado pessoal de aluno | Muda | Não se aplica |
| E8 | Contrato de capacidade do mainframe | Permanece | Contrato de capacidade, com piso de volume, até 31/12/2028 |
| E9 | Região de implantação dos componentes em nuvem | Permanece | Restrição RT5, parecer do Jurídico de 28/04/2026, que exige território nacional |
| E10 | Responsabilidade pela correção de dado cadastral de aluno | Muda | Não se aplica |

## 3. Requisitos

### 3.1 Direcionadores de mudança e fatores externos

#### Direcionadores de mudança

A ACME enfrenta sete pressões para mudar, e nem todas têm a mesma urgência. Algumas já viraram problema, como os 34 dias úteis para entregar uma mudança, e a resposta a elas é reativa. Outras ainda não produziram efeito, como as aposentadorias de 2027, e por isso permitem uma resposta antecipatória.

| Direcionador | Origem | Resposta | Evidência |
| --- | --- | --- | --- |
| Custo de propriedade do sistema acadêmico | Interno | Antecipatória | A meta de R$ 11,0 milhões tem prazo no fim de 2029, sem gatilho imediato |
| Lentidão de resposta a pedido de mudança | Interno | Reativa | Os 34 dias úteis entre pedido aprovado e entrega já pesam na operação de hoje |
| Risco de perda de competência | Interno | Antecipatória | Duas das 6 aposentadorias de especialistas em COBOL estão previstas para 2027 |
| Exigência de proteção de dado pessoal | Externo | Reativa | O parecer jurídico de 28/04/2026 já impõe a obrigação de processar em território nacional |
| Avaliação regulatória | Externo | Antecipatória | A preocupação da Reitoria é com uma queda futura de nota |
| Expectativa do aluno | Externo | Reativa | O pedido de aplicativo e a falha na abertura da matrícula já aconteceram, com 2 dos 3 incidentes graves na janela de matrícula |
| Disponibilidade de nuvem contratável | Externo | Antecipatória | É uma oportunidade aberta pela pré-aprovação de 12/03/2026, sem pressão imediata |

O risco de perda de competência tem as duas faces. Só 1 dos 6 especialistas em COBOL domina a alteração do módulo de matrícula, o que já é problema hoje, enquanto as duas aposentadorias de 2027 são um risco que a ACME ainda pode evitar.

#### Fatores externos pela análise PESTLE

Para olhar o ambiente externo, o arquiteto partiu dos três fatos que o dossiê já registra, que cobrem as dimensões Legal, Tecnológica e Sociocultural. Como o dossiê não diz nada sobre as outras três, elas receberam fatores plausíveis, marcados como acréscimo do aluno.

| Dimensão | Fator externo | Origem do fator |
| --- | --- | --- |
| Política | Mudança na política de regulação do ensino superior | Acréscimo do aluno |
| Econômica | Queda da captação de alunos e aumento da inadimplência | Acréscimo do aluno |
| Sociocultural | Aluno que espera aplicativo móvel e matrícula que não falhe na abertura (F3) | Dossiê |
| Tecnológica | Dois provedores de nuvem pré-aprovados em 12/03/2026 (F2) | Dossiê |
| Legal | Processamento de dado pessoal de aluno em território nacional, pelo parecer de 28/04/2026 (F1) | Dossiê |
| Ambiental | Consumo de energia do parque próprio de equipamentos | Acréscimo do aluno |

#### Meta de custo e contrato do mainframe

A meta de R$ 11,0 milhões depende de um contrato que só termina em 31/12/2028, e por isso a tabela ordena no tempo os marcos que prendem o custo.

| Marco | Efeito sobre a meta |
| --- | --- |
| Primeiro ciclo de 12 meses, com R$ 6,2 milhões | O contrato de capacidade continua valendo, e a carga retirada do mainframe não reduz o desembolso |
| 31/12/2028, fim do contrato de capacidade com piso de volume | O piso de volume contratado é devido mesmo com menos carga, e a nuvem soma seu custo ao que já existe |
| Fim de 2029, meta de R$ 11,0 milhões | É o primeiro exercício em que a redução pode aparecer, depois do fim do contrato |

Por isso o projeto só pode prometer, dentro do primeiro ciclo, a construção das condições para reduzir o custo, e não a redução em si. A meta tem prazo em 2029 porque o contrato termina em 31/12/2028.

### 3.2 Catálogo de requisitos e reescritas mensuráveis

#### Catálogo de requisitos classificados

As entrevistas trouxeram declarações com graus diferentes de clareza, e antes de projetar qualquer coisa o arquiteto as separou em três categorias de trabalho. Nas declarações de atributo de qualidade, a última coluna mostra se o contexto e a medida estão presentes, porque é isso que as torna verificáveis.

| Código | Declaração | Categoria | Justificativa | Formulação |
| --- | --- | --- | --- | --- |
| R5 | O sistema emite histórico escolar com assinatura digital no padrão ICP-Brasil | Requisito funcional | Descreve uma capacidade do sistema, a de emitir o histórico assinado | Não se aplica |
| R13 | O aluno consulta o resultado da solicitação de aproveitamento de disciplina pelo portal | Requisito funcional | Descreve uma capacidade do sistema, a de consultar o resultado | Não se aplica |
| R4 | A solução opera em um dos dois provedores de nuvem aprovados em 12/03/2026 | Restrição | Fecha a alternativa de plataforma por uma decisão anterior ao projeto | Não se aplica |
| R10 | A manutenção dos programas COBOL do núcleo permanece sob o contrato da fábrica até 30/09/2027 | Restrição | Fecha a alternativa de fornecedor do núcleo por uma decisão anterior ao projeto | Não se aplica |
| R6 | O portal sustenta 5.800 sessões simultâneas na abertura da matrícula, com percentil 95 do tempo de confirmação em até 4 segundos | Requisito de atributo de qualidade | Diz quão bem o portal responde sob carga | Bem formulada, com contexto (abertura da matrícula), carga (5.800 sessões) e medida (4 segundos no percentil 95) |
| R2 | A matrícula não pode cair | Requisito de atributo de qualidade | Trata de disponibilidade | Mal formulada, sem contexto, carga nem medida |
| R3 | O tempo de resposta precisa ser bom | Requisito de atributo de qualidade | Trata de desempenho | Mal formulada, sem contexto, carga nem medida |
| R11 | O sistema precisa ser moderno e escalável | Requisito de atributo de qualidade | Só a palavra escalável nomeia um atributo | Mal formulada, e em parte sem reescrita possível, porque moderno não nomeia atributo algum |

#### Reescritas mensuráveis

Uma declaração como a matrícula não pode cair só vira requisito quando se sabe em que situação ela vale, quanto uso o sistema recebe e que valor deve atingir. Por isso o R2 e o R3 foram reescritos com contexto, carga e medida, e o R11 aparece à parte, porque uma metade dele não pode ser reescrita.

| Elemento | R2, a matrícula não pode cair | R3, o tempo de resposta precisa ser bom |
| --- | --- | --- |
| Contexto | Janela de matrícula, no pico de abertura | Confirmação de matrícula na abertura da janela |
| Carga | 5.800 sessões simultâneas | 5.800 sessões simultâneas |
| Medida | Disponibilidade de 99,9% no mês e taxa de erro abaixo de 1% nas tentativas de confirmação | Percentil 95 do tempo de confirmação em até 4 segundos |

| Parte da declaração sobre o sistema moderno e escalável (R11) | Tratamento |
| --- | --- |
| Moderno | Não nomeia atributo e não tem reescrita possível, por isso a declaração volta à Reitoria com a pergunta do que ela quer dizer, sem que se invente uma medida |
| Escalável | Nomeia o atributo escalabilidade e pode ser reescrito com a carga de abertura de 5.800 sessões, a medida a combinar com a Reitoria e a Diretoria de TI |

### 3.3 Cenários de qualidade, significância arquitetural e restrições

#### Cenário do pico de matrícula

Na abertura da matrícula, o portal sai da média anual de 815 sessões e chega a 5.800, e é nesse pico que a taxa de erro sobe a 6,3%. Os quatro primeiros elementos do cenário vêm do enunciado, e os dois últimos, a resposta e a medida, são o que o exercício pede.

| Elemento | Especificação |
| --- | --- |
| Fonte do estímulo | Alunos veteranos e ingressantes na abertura da matrícula |
| Estímulo | 5.800 sessões simultâneas solicitando inscrição em turmas |
| Ambiente | Abertura da matrícula, com razão de 7,1 entre pico e média |
| Artefato | Portal do aluno e serviço de matrícula |
| Resposta | O portal e o serviço de matrícula registram a inscrição e devolvem a confirmação ao aluno |
| Medida da resposta | Taxa de erro abaixo de 1% das requisições no intervalo de pico, contra os 6,3% de hoje, verificada em teste de carga com 5.800 sessões simultâneas |

#### Cenário do incidente de 04/02/2026

Em 04/02/2026, navegadores abandonados no meio da matrícula deixaram transações abertas no núcleo até o monitor CICS esgotar o limite de tarefas. O cenário abaixo diz como o sistema deve reagir para que isso não se repita.

| Elemento | Especificação |
| --- | --- |
| Fonte do estímulo | Navegadores de alunos abandonados durante a sessão de matrícula |
| Estímulo | Acúmulo de transações abertas no núcleo sem encerramento da sessão web |
| Ambiente | Abertura da matrícula, no pico de 5.800 sessões simultâneas |
| Artefato | Monitor CICS e núcleo transacional |
| Resposta | A sessão web é encerrada por tempo limite antes que o monitor atinja o limite de tarefas concorrentes |
| Medida da resposta | Nenhuma tarefa presa por sessão abandonada e indisponibilidade de até 43 minutos no mês na janela de matrícula, contra os 260 minutos do incidente |

#### Significância arquitetural dos dois cenários

Para decidir se os dois cenários merecem análise de arquitetura, o roteiro de sete perguntas foi aplicado a cada um. O pico respondeu sim a todas e o incidente respondeu sim a cinco, e por isso os dois foram considerados significativos.

| Pergunta do roteiro | Cenário do pico | Cenário do incidente |
| --- | --- | --- |
| Quais decisões mudariam? | Sim, a forma de ligar o portal ao núcleo, com fila ou com capacidade maior | Sim, onde tratar o tempo limite da sessão |
| O alcance atravessa vários elementos? | Sim, o portal e o núcleo juntos | Sim, a camada web e o núcleo |
| Há incerteza, escala incomum ou consequência grave? | Sim, o pico é 7,1 vezes a média, com 6,3% de erro | Sim, 62% das tentativas de matrícula deram erro e 9.400 alunos não concluíram a inscrição |
| Uma decisão tardia provocaria reconstrução? | Sim, subdimensionar tarde custa caro | Não, o tempo limite pode ser acrescentado depois sem refazer a estrutura |
| Melhorar uma qualidade prejudica outra? | Sim, mais capacidade melhora o desempenho e aumenta o custo | Não, o tempo limite não troca uma qualidade por outra |
| Demanda protótipo, teste de carga ou prova de conceito? | Sim, teste de carga com 5.800 sessões | Sim, o incidente só aparece em produção porque não há ambiente de teste de carga |
| Está ligada a objetivo de negócio prioritário? | Sim, a matrícula sem falha é a preocupação da Pró-Reitoria de Graduação | Sim, o incidente obrigou a prorrogar a janela em 2 dias úteis |

| Cenário | Requisito arquiteturalmente significativo? | Defesa |
| --- | --- | --- |
| Pico de matrícula | Sim | Atinge portal e núcleo, custa caro se for dimensionado tarde e obriga a escolher entre custo de capacidade e desempenho |
| Incidente de 04/02/2026 | Sim | Revela um risco técnico que já aconteceu, atravessa a camada web e o núcleo e obriga a decidir onde tratar o tempo limite de sessão |

#### Origem das restrições

Cada restrição foi decidida por alguém de fora do projeto, e saber quem decidiu mostra a quem recorrer se uma delas precisar mudar. Nenhuma das sete é técnica.

| Restrição | Origem | Quem pode revê-la |
| --- | --- | --- |
| O sistema acadêmico não pode parar em período letivo | De política interna | Nova decisão da Pró-Reitoria de Graduação |
| O ambiente virtual de aprendizagem e o ERP financeiro permanecem | De política interna | Nova decisão da Reitoria |
| Uso de apenas dois provedores de nuvem pré-aprovados | De política interna | Nova decisão do Conselho Universitário |
| Identidade e autorização por padrões abertos | De política interna | Nova decisão do Comitê de Segurança da Informação |
| Dado pessoal de aluno processado em território nacional | Regulatória | Só muda se a norma mudar, e o parecer do Jurídico acompanha a norma |
| Manutenção do núcleo COBOL sob contrato até 30/09/2027 | Contratual | Negociação com o fornecedor, dentro dos prazos previstos |
| Orçamento de R$ 6,2 milhões para o primeiro ciclo de 12 meses | De política interna | Nova aprovação da Reitoria |

## 4. Linha de base e lacunas

### 4.1 Artefatos de linha de base que sustentam os cenários

#### Artefatos de linha de base dos cenários

Os cenários do pico e do incidente só são confiáveis se os números que os sustentam estiverem corretos, e esses números vêm dos artefatos da linha de base, os documentos e as medições que descrevem o sistema atual. Quatro dos seis artefatos sustentam os cenários, mas o L3, o prazo de 34 dias úteis, e o L4, o custo de R$ 15,83 milhões, não aparecem em nenhum deles.

| Artefato | Dado que fornece | Efeito de um dado desatualizado |
| --- | --- | --- |
| L6, série de medição de sessões simultâneas e de taxa de erro do portal | A média anual de 815 sessões, o pico de 5.800 e a taxa de erro de 6,3% no pico | A razão de 7,1 e a meta de erro ficariam erradas, e o teste de carga simularia um pico diferente do real |
| L2, registro dos três incidentes graves dos últimos 18 meses | A sequência do incidente de 04/02/2026, com 4h20 de duração e 62% das tentativas com erro | O cenário do incidente trataria uma causa que não aconteceu, e a medida de 260 minutos perderia o ponto de comparação |
| L1, inventário de componentes do sistema acadêmico | O monitor CICS, o limite de tarefas e as camadas que o estímulo atravessa | O campo Artefato apontaria uma parte do sistema que já mudou, e a resposta seria desenhada para o lugar errado |
| L5, contratos de sustentação e de capacidade | O prazo de 30/09/2027 para qualquer alteração no núcleo COBOL | A resposta poderia prever alteração no núcleo sem que o contrato permita, e o tempo limite teria de ficar na camada web |

## 5. Contexto do sistema (C4, nível 1)

### 5.1 Portfólio, contrato de notas e diagrama de contexto

#### Portfólio de aplicações

O catálogo traz onze aplicações da ACME. A tabela dá a cor de cada uma e o fato do caso que a sustenta. Os quatro portais usam tecnologia que o fornecedor deixou de apoiar, o núcleo ainda sustenta a operação e continua sob contrato, e o ERP financeiro e o ambiente virtual ficam por decisão da Reitoria.

| Aplicação | Cor | Justificativa |
| --- | --- | --- |
| Portal do Aluno | Vermelho | JSF 1.2 e EJB 2.0 de 2007, sobre servidor sem suporte desde 2018, sem versão responsiva, o que impede o R1, e com acesso direto ao banco |
| Portal do Professor | Vermelho | JSF 1.2 e EJB 2.0 de 2008, sobre o mesmo servidor sem suporte |
| Portal da Secretaria | Vermelho | JSF 1.2 e EJB 2.0 de 2008, sobre o mesmo servidor sem suporte |
| Portal do Gestor | Vermelho | JSF 1.2 e EJB 2.0 de 2009, sobre o mesmo servidor sem suporte, e com acesso direto ao banco |
| Núcleo transacional | Âmbar | COBOL sobre CICS, com manutenção sob contrato até 30/09/2027. Vermelho também é aceito quando a resposta cita o horizonte de retirada |
| ERP financeiro | Verde | Permanece por decisão da Reitoria de 12/03/2026 |
| Ambiente virtual de aprendizagem | Verde | Permanece por decisão da Reitoria de 12/03/2026 |
| Data warehouse institucional | Âmbar | O dossiê não informa ano nem tecnologia, e a cópia integral de 140 tabelas por lote é o único dado disponível. A cor é provisória, e a Diretoria de TI precisa confirmá-la |
| Assinador digital ICP-Brasil | Verde | Serviço externo exigido pelo R5, que pede histórico escolar com assinatura nesse padrão |
| Gateway de pagamento | Verde | Serviço externo chamado pelo Portal do Aluno, sem problema registrado no dossiê. A cor é provisória pelo mesmo motivo do data warehouse |
| Diretório corporativo | Âmbar | Autentica todos os perfis por LDAP, mas o R8 pede padrões abertos de identidade, e o diretório atende só os portais atuais |

#### Contrato da integração de notas

A nota nasce no núcleo transacional, que é o dono da nota consolidada pela decisão do exercício 14. Hoje ela segue para o ambiente virtual num arquivo gerado às 05h10, e o R7 pede que chegue em até 10 minutos. O contrato abaixo descreve a troca nova campo a campo, com o modo assíncrono.

| Campo | Resposta |
| --- | --- |
| Origem | Núcleo transacional, dono da nota consolidada, que publica pelo serviço de notas |
| Destino | Ambiente virtual de aprendizagem |
| Gatilho | Nota lançada ou alterada pelo professor |
| Itens trocados | Identificador do aluno, turma, avaliação, nota, situação, versão e data do lançamento |
| Sequência | Publicação do evento, recebimento pelo ambiente virtual e confirmação do processamento |
| Pré e pós-condições | Antes, o aluno está matriculado numa turma já enviada ao ambiente virtual. Depois, a nota está visível ao aluno no ambiente virtual |
| Protocolo | HTTPS ou mensageria, conforme o plano do ambiente virtual que oferece interfaces de programação, com acréscimo de 38% sobre o valor anual do contrato |
| Formato e esquema | Mensagem estruturada, com esquema versionado e descrito em AsyncAPI |
| Semântica de erro | Aluno ou turma inexistente vai para uma fila de exceção, tratada pela Secretaria Acadêmica. Indisponibilidade do destino gera nova tentativa, com limite |
| Versionamento | Cada versão do esquema é compatível com a anterior, e uma mudança incompatível sai em versão nova |
| Garantia de entrega e idempotência | Entrega pelo menos uma vez, com chave de idempotência formada por aluno, avaliação e versão, de modo que a repetição de uma mensagem não duplica a nota |
| Nível de serviço | Até 10 minutos entre o lançamento e a visibilidade, conforme o R7, com capacidade para 360.000 lançamentos na janela de fechamento |

A integração é assíncrona, porque a indisponibilidade do ambiente virtual não pode impedir o professor de lançar a nota. O padrão Transactional Outbox garante que a nota e o evento sejam gravados na mesma transação, e o consumidor idempotente absorve a entrega repetida. A gravação do evento junto com a nota ocorre hoje dentro do programa COBOL de avaliação e notas, que só a fábrica pode alterar até 30/09/2027, e por isso a forma de capturá-la fica como decisão pendente, a definir com a fábrica contratada. O modo síncrono também é aceito quando a resposta declara tempo limite, nova tentativa com limite e Circuit Breaker.

Quando o professor corrige uma nota já enviada, o serviço publica uma nova versão da mesma nota, com a mesma chave de aluno e avaliação e uma versão maior. O ambiente virtual substitui o valor anterior pelo da versão mais recente.

#### Diagrama de contexto da solução

Os dois erros do diagrama do enunciado eram o banco de dados acadêmico desenhado como elemento externo e o ERP financeiro desenhado dentro da fronteira. O banco é um contêiner, parte interna do sistema, e só aparece no nível seguinte. O ERP permanece por decisão da Reitoria e é mantido por outra equipe, então precisa ficar fora da caixa. A correção do segundo erro também elimina a caixa duplicada do sistema acadêmico que existia dentro da fronteira.

![Diagrama de contexto corrigido do primeiro ciclo da ACME, com aluno, professor e secretaria acadêmica ligados ao sistema acadêmico, que é uma caixa única dentro da fronteira tracejada, e com seis sistemas externos fora dela: ERP financeiro, ambiente virtual de aprendizagem, assinador digital ICP-Brasil, gateway de pagamento, provedor de identidade e órgão regulador.](../assets/images/acme-ex15-contexto-corrigido.svg){ .module-diagram }

A legenda abaixo diz, para cada elemento, se ele está dentro ou fora da solução e por quê.

| Elemento | Tipo | Posição | Motivo |
| --- | --- | --- | --- |
| Aluno, professor e secretaria acadêmica | Pessoa | Fora | Usam a solução e são mostrados no alto do diagrama |
| Sistema acadêmico, com o núcleo COBOL | Sistema da solução | Dentro | A ACME responde pela evolução e pela operação do núcleo, e a fábrica contratada só faz a manutenção dos programas |
| ERP financeiro | Sistema externo | Fora | Permanece por decisão da Reitoria de 12/03/2026, e a ACME apenas o integra |
| Ambiente virtual de aprendizagem | Sistema externo | Fora | Permanece pela mesma decisão e recebe as notas |
| Assinador digital ICP-Brasil | Sistema externo | Fora | Serviço que assina o histórico escolar, usado sem ser alterado |
| Gateway de pagamento | Sistema externo | Fora | Serviço que gera boleto e cobrança em cartão |
| Provedor de identidade | Sistema externo | Fora | A ACME usa o serviço para autenticar, e o produto só é escolhido na Aula 5 |
| Órgão regulador | Sistema externo | Fora | Recebe a extração anual do censo da educação superior |

## 6. Princípios

### 6.1 Princípios priorizados e esboço lógico

#### Princípios priorizados

A ACME levantou quatro exigências na Aula 2, e cada uma originou um princípio. Os princípios estão em ordem de prioridade, porque quando dois entram em conflito vence o que aparece primeiro.

| Prioridade | Princípio | Motivação | Implicação no desenho | Evidência esperada |
| --- | --- | --- | --- | --- |
| 1 | Evolução incremental | Continuidade operacional: o sistema acadêmico não pode parar em período letivo (RT1) | Todo elemento novo entra em produção por ativação gradual, convive com o núcleo e pode voltar ao caminho legado se falhar. Fica proibida a virada de um módulo inteiro em uma única data | Nenhuma parada em período letivo e plano de retorno executado em homologação a cada entrega |
| 2 | Segurança por desenho | Residência de dados: o parecer jurídico de 28/04/2026 exige dado pessoal de aluno em território nacional (RT5) | Todo elemento que lê ou grava dado pessoal de aluno é marcado como tal e só pode ser implantado em região nacional. Fica proibido o serviço gerenciado sem região no Brasil | Inventário dos fluxos de dado pessoal com a região de execução de cada elemento |
| 3 | Baixo acoplamento | Dependência do legado: o núcleo COBOL fica sob contrato de sustentação até 30/09/2027 (RT6), com 6 especialistas, 2 deles aposentados em 2027, e só 1 domina o módulo de matrícula | Os elementos novos acessam o núcleo apenas pelas transações que ele já oferece e não dependem de alteração de programa COBOL. Fica proibido ler ou gravar as tabelas do núcleo diretamente | Nenhuma entrega do primeiro ciclo depende de demanda aberta com a fábrica de software |
| 4 | Separação de responsabilidades | Propagação de notas: o requisito R7 pede a nota no ambiente virtual em até 10 minutos, contra o lote diário das 05h10 | Registrar a nota e entregá-la ao ambiente virtual são responsabilidades de elementos distintos, e a entrega passa a ocorrer no ritmo do lançamento, não no do lote | Intervalo entre o lançamento e a chegada da nota, com percentil 95 abaixo de 10 minutos |

A evolução incremental ocupa o primeiro lugar porque vem de uma restrição fechada, que o arquiteto não negocia. A residência de dados, também de natureza legal, vem logo depois. A propagação de notas fica por último porque é um requisito de uma parte interessada, e prazo e alcance podem ser negociados. Quando a nota em 10 minutos entrar em conflito com a continuidade, a continuidade prevalece.

#### Esboço lógico

Com os princípios definidos, as oito responsabilidades foram distribuídas entre cinco elementos, descritos só pelo que fazem. A coluna de situação mostra o que muda e o que fica no núcleo por causa das quatro exigências.

| Elemento lógico | Responsabilidades | Situação na transição | Motivo |
| --- | --- | --- | --- |
| Entrada da matrícula | RS1 | Novo | Recebe o pedido na frente do núcleo e permite ativar a mudança aos poucos, como pede a evolução incremental |
| Registro acadêmico | RS2, RS3, RS8 | Permanece no núcleo | A regra de prioridade de vaga e o registro da nota estão no núcleo, e tirá-los dali exigiria alterar o COBOL, o que o contrato de sustentação impede até 30/09/2027. O histórico escolar não tem exigência de mudança e fica onde está |
| Publicação de notas | RS4 | Novo | Entrega cada nota ao ambiente virtual sem esperar o lote, o que atende o R7 |
| Integração financeira | RS5 | Permanece no núcleo | Nenhuma das quatro exigências pede mudança no envio dos lançamentos ao ERP financeiro, então o lote do núcleo continua |
| Identidade e auditoria | RS6, RS7 | Novo | O registro de toda leitura de dado pessoal precisa ficar fora do núcleo, que não pode ser alterado, e o elemento trata dado pessoal em região nacional |

O risco principal do esboço são os 2.300 pontos de acesso direto ao banco do núcleo, existentes na camada Java dos portais. Eles contornam qualquer elemento novo e ameaçam o princípio de baixo acoplamento. A decisão pendente é como capturar o lançamento de nota no momento em que ocorre sem alterar o programa COBOL de avaliação e notas, escolha que afeta o princípio de separação de responsabilidades e entra em tensão com o de baixo acoplamento.

## 7. Decisões

### 7.1 Comparação de estilos e estilo recomendado

#### Estilos comparados diante dos dois cenários

O pico de matrícula, com 5.800 sessões simultâneas e meta de erro abaixo de 1%, e o incidente de 04/02/2026, com 4h20 de indisponibilidade e 62% de erro, não pedem a mesma coisa de um estilo. Por isso cada um dos três estilos foi confrontado com os dois cenários, sempre com o núcleo COBOL sobre CICS em operação durante a transição.

| Estilo | Cenário 1, pico de matrícula | Cenário 2, incidente de 04/02/2026 |
| --- | --- | --- |
| Arquitetura orientada a eventos | Favorável. A fila absorve a razão de 7,1 entre o pico e a média, e o núcleo processa no ritmo que sustenta | Neutro. O defeito é a falta de tempo limite de sessão, que se corrige em qualquer estilo, e a fila só ajuda a limitar as tarefas concorrentes |
| Arquitetura de microsserviços | Neutro. A escalabilidade seletiva só existe depois de extrair a matrícula do núcleo, trabalho de mais de um ciclo de 12 meses | Neutro. O isolamento de falha entre serviços ajuda, mas o abandono de sessão acontece no núcleo, que continua em operação |
| Arquitetura hexagonal | Neutro. Organiza a solução nova, mas não reduz sozinha a carga que chega ao núcleo | Favorável. O acesso ao núcleo passa por uma porta, e é nela que se declaram o tempo limite e o limite de tarefas concorrentes abaixo do limite do CICS |

#### Princípios, risco e recomendação

Depois dos cenários, cada estilo foi lido à luz dos quatro princípios priorizados no caderno, porque um estilo bom no pico ainda pode contrariar uma regra do projeto. O mecanismo compensatório é o recurso que neutraliza o risco que o estilo traz.

| Estilo | Princípios | Risco para a ACME | Mecanismo compensatório |
| --- | --- | --- | --- |
| Arquitetura orientada a eventos | Sustenta separação de responsabilidades e baixo acoplamento, e preserva o núcleo, o que atende a evolução incremental | Perda de rastreabilidade ponta a ponta, numa equipe que hoje não opera componente assíncrono | Identificador de correlação e observabilidade do fluxo |
| Arquitetura de microsserviços | Sustenta separação de responsabilidades, mas contraria o baixo acoplamento com o núcleo, porque exige extrair a matrícula do COBOL | Extração do núcleo em conflito com a restrição do contrato de sustentação | Adiar a extração para depois de 30/09/2027 |
| Arquitetura hexagonal | Sustenta baixo acoplamento e evolução incremental, porque o núcleo passa a ser acessado por uma porta | Custo de indireção em cada chamada | Limitar as portas às integrações que de fato serão substituídas |

O estilo recomendado é a arquitetura orientada a eventos na borda, com o núcleo preservado. O atributo favorecido é a escalabilidade elástica na entrada, que absorve o pico de matrícula, e o atributo prejudicado é a simplicidade de rastrear uma operação de ponta a ponta. A comparação se desempata pelo primeiro princípio, a evolução incremental, porque os eventos atendem o pico sem exigir alteração do COBOL.

### 7.2 Padrões para os três problemas

#### Padrões escolhidos para os três problemas

Cada problema da ACME pediu um padrão diferente. A tabela liga cada um ao padrão escolhido, ao elemento do esboço lógico que o recebe e ao que a escolha traz e custa.

| Problema | Padrão e nível | Elemento afetado | Consequência favorável | Custo aceito |
| --- | --- | --- | --- | --- |
| Coexistência entre o legado e a solução nova | Strangler Fig e Anti-Corruption Layer, padrões arquiteturais, com Adapter, padrão de design, para implementar a tradução | Entrada da matrícula e Registro acadêmico | Cada funcionalidade é ativada por vez, com retorno ao legado, e a camada de tradução usa as transações CICS que já existem, sem depender da fábrica antes de 30/09/2027 | Duas implementações mantidas e dado sincronizado enquanto os 2.300 pontos de acesso direto existirem |
| Proteção contra falha de integração | Timeout, Circuit Breaker e Bulkhead, padrões arquiteturais | Entrada da matrícula | O tempo limite ataca a causa registrada do incidente de 04/02/2026, o disjuntor contém a falha do núcleo e a separação de conexões protege os demais portais | Desenhar o comportamento degradado da matrícula e ajustar limites sem ambiente de teste de carga, ausência registrada na linha de base |
| Publicação confiável de mudança acadêmica | Transactional Outbox, padrão arquitetural, com consumidor idempotente | Registro acadêmico e Publicação de notas | Toda nota gravada gera a sua mensagem, o que sustenta o R7 de 10 minutos sem esperar o lote das 05h10 | Entrega ao menos uma vez, volume de até 360.000 lançamentos no fechamento e plano do ambiente virtual com interfaces de programação, com acréscimo de 38% sobre o contrato |

A tabela de saída do Transactional Outbox precisa ser gravada na mesma transação da nota, e hoje essa gravação ocorre dentro do programa COBOL. Essa dependência fica registrada como risco e como decisão pendente, a confirmar com a fábrica de software.

#### Padrões descartados

Dois padrões foram considerados e deixados de fora, porque não combinam com o contexto da ACME.

| Problema | Padrão descartado | Motivo |
| --- | --- | --- |
| Proteção contra falha de integração | Retry com limite na confirmação de matrícula | A operação não é idempotente e pode duplicar a inscrição, e a repetição simultânea no pico amplia a sobrecarga que se quer conter |
| Publicação confiável de mudança acadêmica | Saga | A operação é uma gravação seguida de notificação, sem etapas em serviços distintos que exijam compensação |

### 7.3 ADR do estilo e dos padrões

#### ADR 001, estilo orientado a eventos com padrões de convivência e de resiliência

O registro abaixo junta o que os exercícios 9 a 11 decidiram, nos dez campos do modelo da aula. O estado é proposta porque o caso ainda não traz a data nem quem decide, e por isso esses dois pontos ficam marcados como a definir.

| Campo | Conteúdo |
| --- | --- |
| Título | ADR 001, adoção da arquitetura orientada a eventos na entrada da matrícula, com Strangler Fig, Anti-Corruption Layer, Timeout, Circuit Breaker, Bulkhead e Transactional Outbox |
| Estado | Proposta |
| Data | A definir, com o Diretor de TI |
| Contexto | O Portal do Aluno recebe em média 815 sessões simultâneas e chega a 5.800 na abertura da matrícula, com erro de 6,3% contra a meta de 1%. Em 04/02/2026, sessões abandonadas esgotaram as tarefas do CICS, com 4h20 de indisponibilidade e 62% de erro na matrícula. O núcleo COBOL não pode ser alterado nem substituído durante a transição. Fica fora deste registro a escolha do produto de mensageria |
| Forças | Absorver a razão de 7,1 entre o pico e a média, princípio da evolução incremental. Levar o erro de 6,3% a menos de 1%. Conter a indisponibilidade nos 43 minutos mensais do acordo de nível de serviço. Preservar o núcleo, princípio do baixo acoplamento e restrição do contrato de sustentação. Entregar a nota em 10 minutos, princípio da separação de responsabilidades. Manter o dado pessoal em território nacional, princípio da segurança por desenho |
| Alternativas | Manter a arquitetura em camadas atual atende a preservação do núcleo, mas não as três primeiras forças, porque é a configuração que produz os 6,3% de erro. Microsserviços atenderiam a escalabilidade seletiva, mas exigem extrair a matrícula do COBOL, trabalho de mais de um ciclo de 12 meses em conflito com a preservação do núcleo. A arquitetura hexagonal protegeria o acesso ao núcleo, mas não reduz a carga do pico e acrescenta indireção |
| Decisão | Adotar a arquitetura orientada a eventos na entrada da matrícula, com fila entre o portal e o núcleo. Usar Strangler Fig e Anti-Corruption Layer para a convivência com o legado, Timeout, Circuit Breaker e Bulkhead contra a falha de integração e Transactional Outbox para publicar a nota. A fila absorve o pico sem tocar o núcleo, e os padrões atendem as forças de erro, de disponibilidade e de 10 minutos |
| Consequências | Positiva: o núcleo deixa de receber a rajada direta e processa no ritmo que sustenta. Negativa: a confirmação deixa de ser síncrona para o aluno, e a equipe passa a operar um componente assíncrono, com os custos de cada padrão, entre eles a manutenção de duas implementações, o ajuste de limites sem teste de carga e a entrega ao menos uma vez. Neutra: o tratamento de erro sai do horário de pico e passa para o processamento da fila |
| Evidências | Não existe teste de carga, porque a linha de base registra a ausência desse ambiente. A evidência disponível é o histórico do incidente de 04/02/2026, reproduzível pelos registros de operação do CICS. A evidência desejável e ausente é um ensaio de carga com 5.800 sessões em ambiente equivalente ao de produção |
| Revisão | Reabrir o registro se a taxa de erro na janela de matrícula seguinte ficar acima de 2%, ou se o percentil 95 do intervalo entre o lançamento e a chegada da nota ao ambiente virtual passar de 10 minutos por duas semanas seguidas |

Campos incompletos: a data e os decisores dependem do Diretor de TI, e a evidência de carga depende de um ambiente que a ACME ainda não tem.

### 7.4 Efeito da solução no negócio

#### Capacidades acadêmicas e o primeiro ciclo

O arquiteto começa por saber onde a mudança toca o trabalho da universidade. Das dez capacidades, duas são alteradas de forma direta, porque os pedidos do primeiro ciclo recaem sobre a matrícula e sobre as notas, e uma terceira é atingida de forma indireta. A classificação segue este critério: estratégica é a capacidade ligada aos objetivos da modernização, operacional é a que executa o serviço acadêmico de rotina, e de apoio é a que sustenta as demais sem contato direto com o aluno.

| Capacidade | Classificação | Afetada no primeiro ciclo | Justificativa |
| --- | --- | --- | --- |
| Admissão e ingresso | Operacional | Não | Fica fora do escopo declarado no exercício 8 |
| Oferta e grade curricular | Operacional | Não | Fica fora do escopo declarado no exercício 8 |
| Matrícula em disciplinas | Estratégica | Sim | O R1 pede a renovação pelo celular, o R6 fixa o tempo de confirmação, e o incidente de 04/02/2026 ocorreu na abertura da matrícula |
| Avaliação e registro de notas | Estratégica | Sim | O R7 pede a nota no ambiente virtual em até 10 minutos |
| Controle de frequência | Operacional | Não | Nenhum dos três requisitos do exercício a atinge |
| Emissão de documentos acadêmicos | Operacional | Não | Fica fora do escopo declarado no exercício 8 |
| Gestão de bolsas e descontos | Operacional | Indiretamente | A matrícula depende do cálculo da parcela feito por esse módulo, que não muda, mas precisa continuar acessível |
| Cobrança de mensalidades | De apoio | Não | O ERP financeiro permanece por decisão da Reitoria |
| Biblioteca | De apoio | Não | Fica fora do escopo declarado no exercício 8 |
| Relação com o órgão regulador | De apoio | Não | É obrigação legal, e a extração do censo não muda no primeiro ciclo |

#### Etapas do fluxo de valor com problema

Quatro das seis etapas do fluxo do aluno têm problema. Três delas têm um requisito que pede a melhoria, e a etapa 3 mostra um atraso que nenhum requisito do exercício cobre.

| Etapa | Problema | Requisito |
| --- | --- | --- |
| 1. Renovar a matrícula | O Portal do Aluno não tem versão responsiva e restringe o uso em telefone celular | R1 |
| 3. Acessar a turma no ambiente virtual | Uma matrícula confirmada às 09h00 só aparece às 04h55 do dia seguinte, pela carga das 04h00 | Nenhum dos três |
| 5. Consultar a nota no ambiente virtual | Uma nota lançada às 15h00 só chega às 06h00 do dia seguinte | R7 |
| 6. Consultar o resultado de aproveitamento | A linha de base não registra consulta desse resultado pelo portal | R13 |

A etapa 2, a confirmação da matrícula, não entra na lista, porque ocorre no núcleo durante a sessão do aluno e não depende de lote.

#### Processo de lançamento de nota

Quando a nota passa a chegar em até 10 minutos, o arquivo gerado no lote das 05h10 perde a razão de existir, e a importação desse arquivo no ambiente virtual muda junto com ele. As demais atividades permanecem.

| Atividade | Situação | Motivo |
| --- | --- | --- |
| 1. Registrar a nota no Portal do Professor | Permanece | O professor continua lançando a nota no mesmo lugar |
| 2. Calcular média e situação | Permanece | Ocorre no núcleo, cuja manutenção está sob contrato até 30/09/2027 |
| 3. Gerar o arquivo de notas no lote das 05h10 | Muda e deixa de existir | A nota passa a ser publicada a cada lançamento |
| 4. Importar o arquivo de notas no ambiente virtual | Muda | O ambiente virtual passa a receber cada nota publicada |
| 5. Consultar a nota | Permanece | O aluno continua consultando no ambiente virtual |
| Retorno das 06h15 | Permanece | A devolução de nota de atividade e presença fica fora do alcance do R7 |

A unidade afetada é a equipe de integrações e execução de lotes, que hoje gera o arquivo das 05h10. A Coordenação de Educação a Distância percebe o efeito, porque deixa de esperar o dia seguinte pela nota.

### 7.5 Dados: dono, consistência e proteção

#### Dono de cada entidade

Cada entidade precisa de um único responsável por gravá-la. A grade do enunciado mostra o núcleo transacional gravando as cinco entidades, enquanto o ambiente virtual e o ERP financeiro devolvem dado à ACME, e por isso nota e lançamento financeiro têm dois donos, cada um para um tipo de dado diferente.

| Entidade | Dono | Capacidade que sustenta | Observação |
| --- | --- | --- | --- |
| Aluno | Núcleo transacional | Matrícula em disciplinas | O cadastro acadêmico do núcleo grava o aluno |
| Matrícula | Núcleo transacional | Matrícula em disciplinas | O serviço de matrícula pode ser o dono quando a regra de matrícula for extraída do núcleo, o que o contrato de sustentação até 30/09/2027 adia |
| Nota | Núcleo transacional para a nota consolidada, e ambiente virtual para a nota de atividade | Avaliação e registro de notas | A nota de atividade nasce no ambiente virtual e volta à ACME no lote das 06h15 |
| Lançamento financeiro | Núcleo transacional para o lançamento, e ERP financeiro para a baixa de pagamento | Gestão de bolsas e descontos, que alimenta a parcela da matrícula | A baixa nasce no ERP e volta à ACME no lote das 05h30 |
| Turma | Núcleo transacional | Matrícula em disciplinas | A turma é a base da matrícula e da carga do ambiente virtual |

Os portais Java não são donos de nenhuma entidade, embora gravem nas tabelas, porque gravam por acesso direto ao banco e sem passar pelo dono.

#### Regime de consistência por consumidor

Na abertura da matrícula o aluno espera resposta rápida de quem lê a fonte, e a Educação a Distância quer a nota no ambiente virtual em até 10 minutos, que são o R6 e o R7 do dossiê. Para os demais consumidores nenhum requisito pede prazo menor do que o lote atual, então o prazo declarado é o do lote que já existe.

| Entidade | Núcleo transacional | Portais Java | ERP financeiro | Ambiente virtual | Data warehouse |
| --- | --- | --- | --- | --- | --- |
| Aluno | Dono, grava | Forte, lê pelas transações do núcleo | Eventual, até 1 dia, lote das 23h10 | Eventual, até 1 dia, lote das 04h00 | Eventual, até 1 dia, lote das 02h30 |
| Matrícula | Dono, grava | Forte na confirmação ao aluno, com percentil 95 de até 4 segundos pelo R6 | Não registrado | Eventual, até 1 dia, lote das 04h00 | Eventual, até 1 dia, lote das 02h30 |
| Nota | Dono da nota consolidada, grava | Forte | Não registrado | Eventual, até 10 minutos pelo R7, e devolução da nota de atividade em até 1 dia, lote das 06h15 | Eventual, até 1 dia, lote das 02h30 |
| Lançamento financeiro | Dono do lançamento, grava | Forte | Eventual, até 1 dia, lote das 23h10, e devolução da baixa em até 1 dia, lote das 05h30 | Não registrado | Eventual, até 1 dia, lote das 02h30 |
| Turma | Dono, grava | Forte | Não registrado | Eventual, até 1 dia, lote das 04h00 | Eventual, até 1 dia, lote das 02h30 |

O prazo de 1 dia, onde o dossiê não traz exigência, é a suposição adotada pelo curso. O dossiê registra que um pagamento compensado só aparece na situação do aluno cerca de 30 horas depois, e a Secretaria Acadêmica ou a Diretoria de TI pode pedir prazo menor.

#### Dado mestre do aluno

O aluno é a entidade compartilhada da ACME, com 38.400 alunos ativos e 214.000 egressos. Hoje só o cadastro acadêmico grava o aluno, e o aplicativo previsto para a arquitetura alvo vai atualizar endereço e telefone. O estilo centralizado atende a esse caso, porque a escrita ocorre num só lugar, o cadastro acadêmico, e todas as demais aplicações recebem cópia dele.

| Campo | Registro |
| --- | --- |
| Estilo | Centralizado, com o cadastro acadêmico do núcleo como sistema de registro |
| Contexto | Ambiente virtual, ERP financeiro e data warehouse recebem cópia do aluno por lote, e o aplicativo do aluno vai gravar endereço e telefone |
| Decisão | A escrita ocorre só no cadastro acadêmico, e o aplicativo grava por meio dele, pelas transações existentes do núcleo |
| Consequência | Endereço e telefone deixam de divergir entre as cópias. O aplicativo depende das transações do núcleo, que não podem ser alteradas até 30/09/2027 |

#### Obrigações do dado pessoal do aluno

A tabela classifica os seis atributos pelo art. 5º da LGPD. Origem racial ou étnica e dado referente à saúde são dados pessoais sensíveis, e por isso cor ou raça e condição de deficiência exigem controle mais estrito.

| Atributo | Classificação | Destinos | Situação perante a necessidade |
| --- | --- | --- | --- |
| Nome e CPF | Dado pessoal | Ambiente virtual, ERP financeiro e data warehouse | O ambiente virtual identifica o aluno, e o CPF pode ser mais do que ele precisa |
| Endereço e telefone | Dado pessoal | ERP financeiro e data warehouse | O ERP usa para cobrança |
| Nota e situação por disciplina | Dado pessoal | Ambiente virtual e data warehouse | O ambiente virtual usa para exibir a nota |
| Cor ou raça autodeclarada | Dado pessoal sensível | Data warehouse | Coletada para o censo, que o núcleo extrai direto para o órgão regulador |
| Condição de deficiência | Dado pessoal sensível | Data warehouse | Coletada para o censo, como o atributo anterior |
| Histórico escolar de egresso | Dado pessoal | Data warehouse | Guardado para emissão de histórico com validade legal |

O destino que recebe mais do que a finalidade exige é o data warehouse, porque a cópia integral de 140 tabelas leva os dois atributos sensíveis, e o dossiê não registra finalidade analítica para eles. A hipótese do art. 16 que autoriza guardar o histórico dos 214.000 egressos é o cumprimento de obrigação legal ou regulatória pelo controlador (inciso I), já que a ACME emite histórico com validade legal. O dossiê não informa a norma que fixa o prazo de guarda, e a Encarregada de proteção de dados precisa confirmá-la. O R14 decorre de decisão da instituição, apoiada no parecer do Jurídico de 28/04/2026, e não da LGPD, que não exige que o dado permaneça no território nacional.

#### Acesso direto ao banco

O banco Oracle, com 740 tabelas, é compartilhado entre o núcleo COBOL e a camada Java. Os 2.300 acessos diretos contrariam a propriedade do dado, porque fazem duas aplicações gravar as mesmas tabelas sem passar pelo dono. Qualquer mudança de estrutura passa a exigir alteração combinada no código COBOL e no código Java, mantidos por equipes distintas, e nenhum módulo pode ser extraído sem reescrever os pontos que o acessam.

### 7.6 Contêineres e relações da arquitetura alvo

{{novo}}

#### Contêineres da arquitetura alvo e suas relações

Ao fim do primeiro ciclo, o aluno renova a matrícula pelo aplicativo, o professor lança a nota pelo portal, e dois serviços novos, o de matrícula e o de notas, chamam o núcleo COBOL pelas transações que ele já tem. Cada serviço novo tem banco próprio, e o núcleo continua gravando no banco Oracle existente. A figura mostra os contêineres e as 15 relações numeradas, e a tabela dá o que cada relação exige da comunicação.

![Diagrama de contêineres da arquitetura alvo do primeiro ciclo da ACME. No alto, professor, aluno e secretaria acadêmica. Dentro da fronteira do sistema acadêmico, o Portal do Professor e o Portal da Secretaria existentes, o aplicativo do aluno, os serviços de notas e de matrícula com banco próprio cada um e tecnologia a definir, e o núcleo transacional COBOL existente com o banco Oracle existente. À direita, fora da fronteira, provedor de identidade, assinador digital ICP-Brasil, ambiente virtual de aprendizagem, gateway de pagamento, ERP financeiro e órgão regulador. As relações estão numeradas de 1 a 15.](../assets/images/acme-ex16-diagrama-de-conteineres.svg){ .module-diagram }

| Relação | Origem e destino | Modo | Volume | Latência |
| --- | --- | --- | --- | --- |
| 1 | Aplicativo do aluno para serviço de matrícula | Síncrono | 5.800 sessões simultâneas no pico e 2.400 confirmações em 30 minutos | Percentil 95 de até 4 segundos, pelo R6 |
| 2 | Portal do Professor para serviço de notas | Síncrono | 4.800 lançamentos em dia letivo comum e até 360.000 na janela de fechamento | Não informado |
| 3 | Serviço de matrícula para núcleo | Síncrono | O mesmo da relação 1 | Dentro dos 4 segundos do R6 |
| 4 | Serviço de notas para núcleo | Síncrono | O mesmo da relação 2 | Não informado |
| 5 | Núcleo para banco Oracle | Síncrono | Até 14,2 milhões de transações no núcleo no primeiro dia da matrícula | Dentro dos 4 segundos do R6 |
| 6 | Serviço de notas para ambiente virtual | Assíncrono | Até 360.000 lançamentos na janela de fechamento | Até 10 minutos, pelo R7 |
| 7 | Serviço de matrícula para gateway de pagamento | Síncrono | Não informado | Tempo limite atual de 15 segundos |
| 8 | Aplicativo do aluno para provedor de identidade | Síncrono | 5.800 sessões simultâneas no pico | Tempo limite atual do diretório de 10 segundos |
| 9 | Portal da Secretaria para assinador digital | Síncrono | Não informado | Tempo limite atual de 45 segundos |
| 10 | Núcleo para ERP financeiro | Assíncrono | Não informado, em lote diário às 23h10, mantido no primeiro ciclo | Lote de 1h40 de duração média |
| 11 | Núcleo para órgão regulador | Assíncrono | Extração anual em maio | 6h20 de duração |
| 12 | Serviço de matrícula para o banco do serviço | Síncrono | Não informado | Não informado |
| 13 | Serviço de notas para o banco do serviço | Síncrono | Não informado | Não informado |
| 14 | Aplicativo do aluno para serviço de notas | Síncrono | Não informado | Não informado |
| 15 | Portal da Secretaria para núcleo | Síncrono | Não informado | Tempo limite atual de 30 segundos do conector dos portais |

O R6 é sustentado pelas relações 1, 3, 5 e 8, que formam o caminho da confirmação, da entrada do aluno ao banco. As relações 3 e 5 herdam o orçamento de 4 segundos, o que faz do núcleo o ponto provável de gargalo da matrícula. O R7 é sustentado pelas relações 2, 4 e 6, que levam a nota do portal ao ambiente virtual. A relação 12 fica fora da lista do R6, porque o dossiê não diz se a gravação no banco do serviço entra no tempo da confirmação, e a 13 fica fora da lista do R7 pelo mesmo motivo.

O núcleo transacional fica dentro da fronteira, como contêiner. A ACME detém a responsabilidade pelo núcleo e terceiriza à fábrica apenas a manutenção dos programas COBOL, e o critério que decide a posição de um elemento é a fronteira de responsabilidade sobre ele. O contrato de sustentação até 30/09/2027 impede que a equipe interna altere o núcleo, e por isso os serviços novos o acessam pelas transações existentes.

{{/novo}}

## 10. O que ainda falta decidir

{{novo}}

| Pendência | Quem decide | Quando se resolve |
| --- | --- | --- |
| Data de conclusão do ciclo | Reitoria, candidata a patrocinadora, com o roteiro autorizado | Fase 7, desenvolvimento do roteiro |
| Nomeação do patrocinador de negócio | Reitoria | Antes da fase 3, definição do esboço da solução |
| Validação das decisões propostas D2, D3, D5, D6, D8 e D9 | Partes interessadas da seção 2 | Fase 6, validação |
| Confirmação das premissas PR1 a PR7 | Responsáveis indicados na coluna Como verificar | Fase 2, descoberta |
| Aprovação da Reitoria ao plano superior do ambiente virtual, condição para o elemento E1 mudar | Reitoria | Antes do início do primeiro ciclo |
| Data e decisores do ADR 001 | Diretor de TI | Antes da aprovação do registro |
| Ensaio de carga com 5.800 sessões em ambiente equivalente ao de produção | Diretoria de TI | Antes de aceitar o ADR 001, pois o ambiente de carga ainda não existe |
| Escolha do produto de mensageria | Diretoria de TI, com a fábrica de software | Na Aula 5, definição tecnológica |
| Gravação da tabela de saída do Transactional Outbox na mesma transação da nota, hoje dentro do programa COBOL | Fábrica de software | Antes de implantar o serviço de notas |
| Prazo de guarda do histórico e norma que o sustenta, ligado ao R9 | Encarregada de proteção de dados | Antes de fixar a retenção no data warehouse |
| Ano e tecnologia do data warehouse, para fechar a classificação da aplicação | Diretoria de TI | Na Aula 5, definição tecnológica |
| Volume e latência das relações 12 e 13 do diagrama de contêineres, ausentes do dossiê | Diretoria de TI | Antes de fechar o dimensionamento |

{{/novo}}

Ainda em branco, para os próximos exercícios: 8. Tecnologia e plataforma, 9. Roteiro e governança
