# Gabarito do exercício 1

{{progresso:1}}

Este é o caderno da ACME depois do exercício 1, e a moldura âmbar marca o que ele acrescentou. Compare com o seu caderno e veja onde as respostas diferem. O [enunciado do exercício 1](../modulo-1-fundamentos/bloco-1-arquitetura-de-solucoes-e-de-software.md#exercicio-1) está na página do bloco.

## 1. Contexto

### 1.1 Instituição, restrições e decisões por nível

{{novo}}

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

{{/novo}}

Ainda em branco, para os próximos exercícios: A solução em uma página, 2. Partes interessadas, 3. Requisitos, 4. Linha de base e lacunas, 5. Contexto do sistema (C4, nível 1), 6. Princípios, 7. Decisões, 8. Tecnologia e plataforma, 9. Roteiro e governança, 10. O que ainda falta decidir
