# Caso ACME

A ACME é uma universidade privada brasileira fictícia, de porte consolidado, cujo sistema acadêmico foi construído ao longo de duas décadas e sustenta matrícula, avaliação, emissão de documentos e integração financeira. Esta página apresenta a instituição, a pergunta que organiza o caso, os atores envolvidos, as restrições que chegam fechadas ao arquiteto e os requisitos declarados pelas partes interessadas. O caso é o mesmo em todas as aulas da disciplina, e cada aula acrescenta uma camada de artefatos a ele.

## Porte da instituição

Os números abaixo descrevem a instituição no ano letivo de 2026 e são referência para todos os exercícios do curso.

| Dimensão | Valor |
| --- | --- |
| Alunos ativos | 38.400 |
| Graduação presencial | 24.600 |
| Graduação a distância | 10.200 |
| Pós-graduação lato sensu | 3.100 |
| Mestrado e doutorado | 500 |
| Egressos com dados retidos | 214.000 |
| Professores | 2.150 |
| Técnico-administrativos | 1.480 |
| Campi | 4, distribuídos em 3 cidades |
| Cursos de graduação | 62 |
| Turmas por semestre | 4.900 |
| Matrículas em disciplina por semestre | 230.400 |
| Orçamento anual da instituição | R$ 560 milhões |
| Custo anual de propriedade do sistema acadêmico | R$ 15,83 milhões |

A média de 6,0 disciplinas por aluno por semestre explica o total de 230.400 matrículas em disciplina, base de cálculo do volume de lançamento de notas descrito na página de [dados operacionais](dados-operacionais.md).

## A pergunta central

O sistema acadêmico atende aos processos para os quais foi construído, entre eles a matrícula, o cálculo da situação do aluno, a emissão de documentos com validade legal e a alimentação do ERP financeiro. Os problemas registrados pela Diretoria de TI são de outra natureza. O prazo médio entre pedido aprovado e entrega em produção é de 34 dias úteis. O risco operacional concentra-se em janelas de poucos dias, nas quais ocorreram dois dos três incidentes graves dos últimos 18 meses. A alteração do módulo de matrícula depende de 1 profissional, entre os 6 especialistas em COBOL da sustentação, dos quais 2 se aposentam em 2027.

A pergunta que organiza o caso é como evoluir o sistema acadêmico de forma segura e incremental, mantendo a operação contínua durante a transição e respeitando os compromissos contratuais já assumidos pela instituição.

Essa formulação exclui duas respostas. A primeira é a substituição integral por um produto de mercado, descartada pela Reitoria em 12/03/2026 por causa do custo de migração dos 214.000 históricos de egressos e da especificidade do regime acadêmico da instituição. A segunda é a reescrita completa em uma única entrega, descartada porque nenhuma janela do calendário acadêmico comporta a virada simultânea de todos os módulos.

## Mapa de atores

Cada linha da tabela descreve um papel, a área à qual ele pertence, o resultado que persegue e o risco que o preocupa. O exercício do bloco 1 da Aula 1 parte desta tabela para identificar quem decide o quê.

| Papel | Área | O que quer | O que teme |
| --- | --- | --- | --- |
| Reitora | Reitoria | Resultado visível em 12 meses e aplicativo móvel do aluno em operação antes do vestibular de 2027 | Investimento de R$ 6,2 milhões sem efeito perceptível e queda de nota na avaliação regulatória |
| Pró-Reitora de Graduação | Graduação | Matrícula sem falha e notas publicadas dentro do calendário | Repetição do incidente de 04/02/2026 e nova prorrogação da janela de matrícula |
| Diretor de TI | Tecnologia da Informação | Reduzir a dependência de especialistas COBOL e o custo anual de R$ 15,83 milhões | Perder os 6 profissionais de COBOL e ficar sem quem sustente o núcleo |
| Diretor Financeiro | Administração e Finanças | Preservar os contratos vigentes até o fim do prazo, já provisionados no plano plurianual | Desembolso duplicado, com legado e nuvem cobrados no mesmo exercício |
| Gerente de sustentação | Fábrica de software contratada | Manter o escopo e a previsibilidade do contrato até 30/09/2027 | Perder receita e escopo com a internalização do conhecimento do núcleo |
| Coordenadora de Educação a Distância | Educação a Distância | Notas e turmas propagadas ao ambiente virtual de aprendizagem em minutos | Continuar dependente do lote diário, com reclamação de aluno a cada fechamento |
| Encarregada de proteção de dados | Jurídico | Conformidade com a LGPD, base legal declarada e trilha de auditoria sobre dado pessoal | Transferência de dado de aluno para fora do território nacional sem amparo |
| Representação discente | Diretório Central dos Estudantes | Aplicativo móvel e matrícula que não falhe na abertura | Perda de vaga em disciplina por indisponibilidade do portal |

## Interesses em conflito

Três pares de atores têm interesses que não se resolvem por acordo técnico e exigem decisão de quem tem autoridade orçamentária ou de quem responde pelo processo acadêmico.

O primeiro par opõe o Diretor de TI ao Diretor Financeiro. O primeiro quer iniciar a migração de carga para nuvem no primeiro ciclo de 12 meses. O segundo observa que o contrato de capacidade do mainframe vai até 31/12/2028 com piso de volume contratado, de modo que retirar carga não reduz desembolso antes de 2029 e apenas soma um custo novo ao custo existente.

O segundo par opõe o Diretor de TI ao Gerente de sustentação da fábrica. A cláusula de exclusividade do contrato de sustentação reserva à fábrica a manutenção dos programas COBOL do núcleo acadêmico até 30/09/2027. Qualquer estratégia que exija alterar esses programas para expor interfaces novas depende de um fornecedor cujo interesse comercial é preservar o escopo atual.

O terceiro par opõe a Coordenadora de Educação a Distância ao Diretor Financeiro. A propagação de notas em minutos, e não em horas, exige o plano do ambiente virtual de aprendizagem que oferece interfaces de programação, com acréscimo de 38% sobre o valor anual do contrato vigente.

## Restrições fechadas

Restrição é decisão tomada fora do processo de projeto, que limita as alternativas do arquiteto sem ser negociável por ele. As sete abaixo chegam fechadas ao caso.

| Restrição | Origem e data | Consequência para a arquitetura |
| --- | --- | --- |
| O sistema acadêmico não pode parar em período letivo | Pró-Reitoria de Graduação | Toda estratégia é incremental, com o legado em operação durante a transição |
| O ambiente virtual de aprendizagem e o ERP financeiro permanecem | Reitoria, 12/03/2026 | O trabalho é de integração e governança, não de substituição |
| Dois provedores de nuvem pré-aprovados | Conselho Universitário, 12/03/2026 | Decisões de plataforma precisam ser portáveis entre os dois |
| Identidade e autorização por padrões abertos | Comitê de Segurança da Informação | A escolha é de padrão, não de produto |
| Dado pessoal de aluno processado em território nacional | Jurídico, parecer de 28/04/2026 | Restringe a região de implantação e o uso de serviços gerenciados |
| Manutenção do núcleo COBOL sob contrato até 30/09/2027 | Contrato de sustentação | Alterações no núcleo dependem de fornecedor externo |
| Orçamento de R$ 6,2 milhões para o primeiro ciclo de 12 meses | Reitoria | O roteiro de evolução precisa caber nesse valor antes de nova aprovação |

## Requisitos declarados pelas partes interessadas

A lista abaixo reproduz o que cada parte interessada declarou nas entrevistas de levantamento, sem depuração editorial. Alguns itens estão expressos de forma mensurável e outros não. O exercício do bloco 2 da Aula 1 classifica esses requisitos e reescreve os que não admitem verificação.

| Código | Declaração | Origem |
| --- | --- | --- |
| R1 | O aluno deve renovar a matrícula pelo telefone celular, sem acesso ao portal em computador | Representação discente |
| R2 | A matrícula não pode cair | Pró-Reitoria de Graduação |
| R3 | O tempo de resposta precisa ser bom | Representação discente |
| R4 | A solução opera em um dos dois provedores de nuvem aprovados em 12/03/2026 | Conselho Universitário |
| R5 | O sistema emite histórico escolar com assinatura digital no padrão ICP-Brasil | Secretaria Acadêmica |
| R6 | O portal sustenta 5.800 sessões simultâneas na abertura da matrícula, com percentil 95 do tempo de confirmação em até 4 segundos | Diretoria de TI |
| R7 | A nota lançada pelo professor chega ao ambiente virtual de aprendizagem em até 10 minutos | Educação a Distância |
| R8 | A autenticação usa padrões abertos de identidade, sem produto proprietário | Comitê de Segurança da Informação |
| R9 | Toda leitura de dado pessoal de aluno é registrada em trilha de auditoria, com retenção de 5 anos | Encarregada de proteção de dados |
| R10 | A manutenção dos programas COBOL do núcleo permanece sob o contrato da fábrica até 30/09/2027 | Contrato de sustentação |
| R11 | O sistema precisa ser moderno e escalável | Reitoria |
| R12 | A disponibilidade na janela de matrícula é de 99,9%, medida em minutos de indisponibilidade no mês | Pró-Reitoria de Graduação |
| R13 | O aluno consulta o resultado da solicitação de aproveitamento de disciplina pelo portal | Secretaria Acadêmica |
| R14 | Nenhum dado pessoal de aluno é processado fora do território nacional | Jurídico |
| R15 | O custo anual de propriedade do sistema acadêmico, hoje em R$ 15,83 milhões, cai para R$ 11,0 milhões até o fim de 2029, no mesmo escopo de medição | Diretoria de TI |

## Continuação do dossiê

A [arquitetura de linha de base](linha-de-base.md) descreve os componentes atuais, sua idade, quem os sustenta e o tipo de cada integração. Os [dados operacionais](dados-operacionais.md) trazem volumes, calendário acadêmico, incidentes, custos e contratos. A página de [artefatos por aula](artefatos.md) registra o que cada aula acrescenta ao caso.
