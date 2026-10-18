# Gabarito do exercício 9

{{progresso:9}}

Depois do exercício 9, o caderno da ACME reúne o que os exercícios 1 a 9 produziram, e a moldura âmbar marca o que o exercício 9 acrescentou. Compare com o seu caderno para ver onde as suas respostas diferem. O [enunciado do exercício 9](../modulo-3-design-e-padroes/bloco-1-principios-de-design.md#exercicio-9) está na página do bloco.

## A solução em uma página

<details class="caderno-secao" markdown="1">
<summary>Construída no exercício 8. Clique para abrir</summary>

**O problema.** A ACME é uma universidade privada com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, com núcleo em COBOL, que custa R$ 15,83 milhões por ano e leva 34 dias úteis para colocar uma mudança em produção. A situação se agrava porque, dos 6 especialistas em COBOL que o sustentam, 2 se aposentam em 2027.

**A pergunta.** Diante desse quadro, o projeto pergunta como evoluir o sistema acadêmico de forma segura e incremental, com o núcleo em operação durante a transição e respeitando os contratos já assumidos.

**A decisão.** Ainda não há. A Reitora pede resultado em 12 meses, e o primeiro ciclo já tem o escopo registrado na seção 2, com a lista do que muda e do que permanece. A escolha do estilo de arquitetura fica para a Aula 3.

**O que mais pesa no desenho.** A matrícula. Na abertura, o Portal do Aluno precisa sustentar 5.800 sessões simultâneas, com o tempo de confirmação em até 4 segundos para 95% das requisições (o requisito R6 do dossiê). O segundo ponto de atenção é a nota: o professor lança e o aluno precisa vê-la no ambiente virtual de aprendizagem em até 10 minutos (o R7). Os cenários do pico de matrícula e do incidente de sessão foram julgados significativos para a arquitetura.

**Consequências.** A definir, depois da escolha do estilo de arquitetura na Aula 3.

**Como está o trabalho.** Os direcionadores de mudança, os requisitos, os cenários, as restrições e as partes interessadas estão registrados. As nove decisões levantadas na Aula 1 e as sete premissas continuam propostas.

</details>

## 1. Contexto

<details class="caderno-secao" markdown="1">
<summary>Construída nos exercícios 1, 2, 3 e 4. Clique para abrir</summary>

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

### 1.2 Os componentes da solução, num exemplo da ACME

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

### 1.3 Papéis e responsabilidades do ciclo

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

### 1.4 Artefatos nas fases do processo, premissas e escopo

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

</details>

## 2. Partes interessadas

<details class="caderno-secao" markdown="1">
<summary>Construída no exercício 8. Clique para abrir</summary>

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
| Participantes da implantação | Ninguém da equipe que vai construir e manter a solução participa do desenho, e as objeções dessa equipe só aparecem quando mudar o desenho já custa caro |
| Reguladores e entidades setoriais | A exigência externa chega depois da decisão, quando o custo de mudar o desenho já é alto |

#### Pontos de vista de três papéis

O Diretor Financeiro, a Pró-Reitora e o Gerente de sustentação olham para o mesmo sistema com medos diferentes, e por isso cada um recebe um recorte próprio da descrição de arquitetura. A preocupação principal de cada um vem da coluna O que teme do mapa de atores.

| Papel | Preocupação principal | Critério de seleção | Estrutura do artefato | Forma de apresentação |
| --- | --- | --- | --- | --- |
| Diretor Financeiro | Pagar o legado e a nuvem no mesmo exercício | Componentes com custo e contrato associados | Tabela de desembolso por exercício | Comparação com o plano plurianual já provisionado |
| Pró-Reitora de Graduação | Repetir o incidente na janela de matrícula e prorrogar de novo o prazo | Componentes que estão no caminho crítico da matrícula | Fluxo do processo com os pontos de falha marcados | Duas versões comparáveis, a atual e a pretendida |
| Gerente de sustentação da fábrica | Perder receita e escopo se a ACME passar a dominar o núcleo COBOL sem depender da fábrica | Programas sob contrato e interfaces afetadas | Lista de programas com as chamadas que mudam | Marcação do que muda antes e depois de 30/09/2027 |

#### Declaração de escopo do primeiro ciclo

Para o primeiro ciclo caber nos R$ 6,2 milhões e nos 12 meses, o arquiteto separou o que a mudança toca do que ela deixa como está, e anotou quem decidiu cada exclusão para que ninguém a reabra sem saber de onde veio. Os dez elementos recebem os códigos E1 a E10, e a coluna de origem cita as restrições da seção 1: RT2 (o ambiente virtual e o ERP financeiro permanecem), RT5 (dado pessoal de aluno em território nacional) e RT6 (núcleo COBOL sob contrato até 30/09/2027). A correção do dado cadastral de aluno (E10) muda porque a Aula 1 decidiu passá-la da equipe de sustentação à Secretaria Acadêmica (decisão D5).

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

</details>

## 3. Requisitos

<details class="caderno-secao" markdown="1">
<summary>Construída nos exercícios 5, 6 e 7. Clique para abrir</summary>

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
| Expectativa do aluno | Externo | Reativa | O pedido de aplicativo e a falha na abertura da matrícula já aconteceram, com 2 dos 3 incidentes graves em janelas críticas, a abertura da matrícula e o fechamento de notas |
| Disponibilidade de nuvem contratável | Externo | Antecipatória | É uma oportunidade aberta pela pré-aprovação de 12/03/2026, sem pressão imediata |

O risco de perda de competência tem as duas faces. Só 1 dos 6 especialistas em COBOL domina a alteração do módulo de matrícula, o que já é problema hoje, enquanto as duas aposentadorias de 2027 são um risco que a ACME ainda pode evitar.

#### Fatores externos pela análise PESTLE

Para olhar o ambiente externo, o arquiteto partiu dos três fatos que o dossiê já registra (F1, F2 e F3), que cobrem as dimensões Legal, Tecnológica e Sociocultural. Como o dossiê não diz nada sobre as outras três, elas receberam fatores plausíveis, marcados como acréscimo do aluno.

| Dimensão | Fator externo | Origem do fator |
| --- | --- | --- |
| Política | Mudança na política de regulação do ensino superior | Acréscimo do aluno |
| Econômica | Queda da captação de alunos e aumento da inadimplência | Acréscimo do aluno |
| Sociocultural | Aluno que espera aplicativo móvel e matrícula que não falhe na abertura (F3) | Dossiê |
| Tecnológica | Dois provedores de nuvem pré-aprovados em 12/03/2026 (F2) | Dossiê |
| Legal | Processamento de dado pessoal de aluno em território nacional, pelo parecer de 28/04/2026 (F1) | Dossiê |
| Ambiental | Consumo de energia do parque próprio de equipamentos | Acréscimo do aluno |

#### Meta de custo e contrato do mainframe

A meta de R$ 11,0 milhões depende do contrato de capacidade do mainframe, que obriga a ACME a pagar um volume mínimo de uso mesmo que a carga diminua e só termina em 31/12/2028. Por isso a tabela ordena no tempo os marcos que prendem o custo.

| Marco | Efeito sobre a meta |
| --- | --- |
| Primeiro ciclo de 12 meses, com R$ 6,2 milhões | O contrato de capacidade continua valendo, e a carga retirada do mainframe não reduz o desembolso |
| 31/12/2028, fim do contrato de capacidade com piso de volume | O piso de volume contratado é devido mesmo com menos carga, e a nuvem soma seu custo ao que já existe |
| Fim de 2029, meta de R$ 11,0 milhões | É o primeiro exercício em que a redução pode aparecer, depois do fim do contrato |

Por isso o projeto só pode prometer, dentro do primeiro ciclo, a construção das condições para reduzir o custo. A redução propriamente dita só pode aparecer depois do contrato, e a meta tem prazo em 2029 porque o contrato termina em 31/12/2028.

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

Uma declaração como a matrícula não pode cair só se torna requisito quando se sabe em que situação ela vale, quanto uso o sistema recebe e que valor deve atingir. Por isso as declarações sobre a matrícula não poder cair (R2) e sobre o tempo de resposta ser bom (R3) foram reescritas com contexto, carga e medida, e a declaração sobre o sistema ser moderno e escalável (R11) aparece à parte, porque uma metade dela não pode ser reescrita.

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

Cada restrição foi decidida por alguém de fora do projeto, e saber quem decidiu mostra a quem recorrer se uma delas precisar mudar. Nenhuma das sete restrições da seção 1 (RT1 a RT7) é técnica, e nenhuma é regulatória, porque a exigência de território nacional vem de parecer jurídico da própria instituição, e a LGPD não a impõe.

| Restrição | Origem | Quem pode revê-la |
| --- | --- | --- |
| O sistema acadêmico não pode parar em período letivo | De política interna | Nova decisão da Pró-Reitoria de Graduação |
| O ambiente virtual de aprendizagem e o ERP financeiro permanecem | De política interna | Nova decisão da Reitoria |
| Uso de apenas dois provedores de nuvem pré-aprovados | De política interna | Nova decisão do Conselho Universitário |
| Identidade e autorização por padrões abertos | De política interna | Nova decisão do Comitê de Segurança da Informação |
| Dado pessoal de aluno processado em território nacional | De política interna, apoiada em parecer jurídico | Nova decisão do Jurídico, porque a LGPD não exige residência nacional e o parecer é decisão da instituição |
| Manutenção do núcleo COBOL sob contrato até 30/09/2027 | Contratual | Negociação com o fornecedor, dentro dos prazos previstos |
| Orçamento de R$ 6,2 milhões para o primeiro ciclo de 12 meses | De política interna | Nova aprovação da Reitoria |

</details>

## 4. Linha de base e lacunas

<details class="caderno-secao" markdown="1">
<summary>Construída no exercício 7. Clique para abrir</summary>

### 4.1 Artefatos de linha de base que sustentam os cenários

#### Artefatos de linha de base dos cenários

Os cenários do pico de matrícula, com 5.800 sessões simultâneas, e do incidente de 04/02/2026 só são confiáveis se os números que os sustentam estiverem corretos, e esses números vêm dos artefatos da linha de base, os documentos e as medições que descrevem o sistema atual. Quatro dos seis artefatos (L1, L2, L5 e L6) sustentam os cenários, mas o prazo de 34 dias úteis (L3) e o custo anual de R$ 15,83 milhões (L4) não aparecem em nenhum deles.

| Artefato | Dado que fornece | Efeito de um dado desatualizado |
| --- | --- | --- |
| L6, série de medição de sessões simultâneas e de taxa de erro do portal | A média anual de 815 sessões, o pico de 5.800 e a taxa de erro de 6,3% no pico | A razão de 7,1 entre o pico e a média e a meta de erro ficariam erradas, e o teste de carga simularia um pico diferente do real |
| L2, registro dos três incidentes graves dos últimos 18 meses | A sequência do incidente de 04/02/2026, com 4h20 de duração e 62% das tentativas com erro | O cenário do incidente trataria uma causa que não aconteceu, e a medida de 260 minutos de indisponibilidade perderia o ponto de comparação |
| L1, inventário de componentes do sistema acadêmico | O monitor CICS, o limite de tarefas e as camadas que o estímulo atravessa | O campo Artefato apontaria uma parte do sistema que já mudou, e a resposta seria desenhada para o lugar errado |
| L5, contratos de sustentação e de capacidade | O prazo de 30/09/2027 para qualquer alteração no núcleo COBOL | A resposta poderia prever alteração no núcleo sem que o contrato permita, e o tempo limite teria de ficar na camada web |

</details>

## 6. Princípios

<details class="caderno-secao" markdown="1" open>
<summary>Atualizada neste exercício</summary>

### 6.1 Princípios priorizados e esboço lógico

{{novo}}

#### Princípios priorizados

A ACME levantou quatro exigências na Aula 2, e cada uma originou um princípio. Os princípios estão em ordem de prioridade, porque quando dois entram em conflito vence o que aparece primeiro.

| Prioridade | Princípio | Motivação | Implicação no desenho | Evidência esperada |
| --- | --- | --- | --- | --- |
| 1 | Evolução incremental | Continuidade operacional: o sistema acadêmico não pode parar em período letivo (RT1) | Todo elemento novo entra em produção por ativação gradual, convive com o núcleo e pode voltar ao caminho legado se falhar. Fica proibida a virada de um módulo inteiro em uma única data | Nenhuma parada em período letivo e plano de retorno executado em homologação a cada entrega |
| 2 | Segurança por desenho | Residência de dados: o parecer jurídico de 28/04/2026 exige dado pessoal de aluno em território nacional (RT5) | Todo elemento que lê ou grava dado pessoal de aluno é marcado como tal e só pode ser implantado em região nacional. Fica proibido o serviço gerenciado sem região no Brasil | Inventário dos fluxos de dado pessoal com a região de execução de cada elemento |
| 3 | Baixo acoplamento, que mantém cada parte pouco dependente das outras | Dependência do legado: o núcleo COBOL fica sob contrato de sustentação até 30/09/2027 (RT6), com 6 especialistas, 2 deles aposentados em 2027, e só 1 domina o módulo de matrícula | Os elementos novos acessam o núcleo apenas pelas transações que ele já oferece e não dependem de alteração de programa COBOL. Fica proibido ler ou gravar as tabelas do núcleo diretamente | Nenhuma entrega do primeiro ciclo depende de demanda aberta com a fábrica de software |
| 4 | Separação de responsabilidades | Propagação de notas: o requisito R7 pede a nota no ambiente virtual em até 10 minutos, contra o lote diário das 05h10 | Registrar a nota e entregá-la ao ambiente virtual são responsabilidades de elementos distintos, e a entrega passa a ocorrer no ritmo do lançamento, não no do lote | Intervalo entre o lançamento e a chegada da nota, com percentil 95, o valor abaixo do qual ficam 95% dos casos, inferior a 10 minutos |

A evolução incremental ocupa o primeiro lugar porque nasce da restrição de que o sistema acadêmico não pode parar em período letivo (RT1), que o arquiteto não negocia. A residência de dados, regra de que o dado pessoal de aluno fique em território nacional (RT5), vem do parecer do Jurídico e fica logo depois. A propagação de notas fica por último porque é um requisito de uma parte interessada, e prazo e alcance podem ser negociados. Quando a nota em 10 minutos entrar em conflito com a continuidade, a continuidade prevalece.

#### Esboço lógico

Com os princípios definidos, as oito responsabilidades foram distribuídas entre cinco elementos, descritos só pelo que fazem. A coluna de situação mostra o que muda e o que fica no núcleo por causa das quatro exigências.

| Elemento lógico | Responsabilidades | Situação na transição | Motivo |
| --- | --- | --- | --- |
| Entrada da matrícula | RS1 | Novo | Recebe o pedido na frente do núcleo e permite ativar a mudança aos poucos, como pede a evolução incremental |
| Registro acadêmico | RS2, RS3, RS8 | Permanece no núcleo | A regra de prioridade de vaga e o registro da nota estão no núcleo, e tirá-los dali exigiria alterar o COBOL, o que o contrato de sustentação impede até 30/09/2027. O histórico escolar não tem exigência de mudança e fica onde está |
| Publicação de notas | RS4 | Novo | Entrega cada nota ao ambiente virtual sem esperar o lote, o que atende o requisito de 10 minutos para a nota (R7) |
| Integração financeira | RS5 | Permanece no núcleo | Nenhuma das quatro exigências pede mudança no envio dos lançamentos ao ERP financeiro, então o lote do núcleo continua |
| Identidade e auditoria | RS6, RS7 | Novo | O registro de toda leitura de dado pessoal precisa ficar fora do núcleo, que não pode ser alterado, e o elemento trata dado pessoal em região nacional |

O risco principal do esboço são os 2.300 pontos de acesso direto ao banco do núcleo, existentes na camada Java dos portais. Eles contornam qualquer elemento novo e ameaçam o princípio de baixo acoplamento. A decisão pendente é como capturar o lançamento de nota no momento em que ocorre sem alterar o programa COBOL de avaliação e notas, escolha que afeta o princípio de separação de responsabilidades e entra em tensão com o de baixo acoplamento.

{{/novo}}

</details>

## 10. O que ainda falta decidir

<details class="caderno-secao" markdown="1">
<summary>Construída no exercício 8. Clique para abrir</summary>

| Pendência | Quem decide | Quando se resolve |
| --- | --- | --- |
| Data de conclusão do ciclo | Reitoria, candidata a patrocinadora, com o roteiro autorizado | Fase 7, desenvolvimento do roteiro |
| Nomeação do patrocinador de negócio | Reitoria | Antes da fase 3, definição do esboço da solução |
| Validação das seis decisões ainda propostas (D2, D3, D5, D6, D8 e D9) | Partes interessadas da seção 2 | Fase 6, validação |
| Confirmação das sete premissas (PR1 a PR7), as hipóteses assumidas sem confirmação | Responsáveis indicados na coluna Como verificar | Fase 2, descoberta |
| Aprovação da Reitoria à troca do plano do ambiente virtual de aprendizagem para o que oferece interfaces de programação, condição para mudar o envio de notas (elemento E1 do escopo) | Reitoria | Antes do início do primeiro ciclo |

</details>

Ainda em branco, para os próximos exercícios: 5. Contexto do sistema (C4, nível 1), 7. Decisões, 8. Tecnologia e plataforma, 9. Roteiro e governança
