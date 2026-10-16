# Gabarito do exercício 2

{{progresso:2}}

O caderno abaixo reúne o resultado dos exercícios 1 a 2, e o trecho em destaque é o que o exercício 2 preenche. O [enunciado do exercício 2](../modulo-1-fundamentos/bloco-2-a-solucao-como-sistema.md#exercicio-2) está na página do bloco.

## 1. Contexto

### 1.1 Instituição, restrições e decisões por nível

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

### 1.2 Componentes da solução do R7

{{novo}}

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

{{/novo}}

Seções que os exercícios seguintes preenchem: A solução em uma página, 2. Partes interessadas, 3. Requisitos, 4. Linha de base e lacunas, 5. Contexto do sistema (C4, nível 1), 6. Princípios, 7. Decisões, 8. Tecnologia e plataforma, 9. Roteiro e governança, 10. O que ainda falta decidir
