# Caso ACME

Em 04/02/2026, às 08h00, a matrícula da ACME abriu e o portal caiu por mais de quatro horas, e esse dia resume o problema que o caso apresenta. A ACME é uma universidade privada brasileira fictícia, de porte consolidado, cujo sistema acadêmico foi construído ao longo de duas décadas e sustenta matrícula, avaliação, emissão de documentos e integração financeira. Esta página é a primeira das quatro que formam o dossiê do caso, isto é, o conjunto de informações sobre a ACME que os exercícios usam, e ela apresenta a instituição, a pergunta que organiza o caso, oito papéis de pessoas envolvidas (os atores), sete restrições que chegam prontas ao arquiteto e quinze requisitos, numerados de R1 a R15, que as partes interessadas declararam. Parte interessada é qualquer pessoa ou área que decide sobre o sistema, o usa, o sustenta ou é afetada por ele. Como o caso é o mesmo em todas as aulas e cada aula acrescenta a ele os documentos e diagramas que os exercícios produzem, o enunciado de cada exercício traz os dados de que precisa, tirados desta página e das três seguintes, e o aluno não precisa conhecer a ACME antes de começar.

## Porte da instituição

Antes de olhar para o problema, convém saber o tamanho da instituição que o tem. Os números abaixo descrevem a ACME no ano letivo de 2026 e servem de referência para todos os exercícios do curso.

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

Dois dos números da tabela pedem explicação, porque aparecem em quase todos os exercícios. Matrícula em disciplina é a inscrição de um aluno em uma disciplina em um semestre, e a média de 6,0 disciplinas por aluno por semestre explica o total de 230.400, que serve de base para calcular o volume de lançamento de notas descrito na página de [dados operacionais](dados-operacionais.md). Já o custo anual de propriedade é a soma do que a instituição paga por ano para manter o sistema acadêmico funcionando, detalhada nessa mesma página. Os egressos, por fim, são os ex-alunos que já concluíram o curso, e a instituição ainda guarda o histórico de todos eles.

## A pergunta central

O sistema acadêmico atende aos processos para os quais foi construído, entre eles a matrícula, o cálculo da situação do aluno, a emissão de documentos com validade legal e a alimentação do ERP financeiro. Os problemas registrados pela Diretoria de TI são de outra natureza e vêm da estrutura e da equipe. O prazo médio entre pedido aprovado e entrega em produção é de 34 dias úteis. O risco operacional concentra-se em janelas de poucos dias, como a abertura da matrícula e o fechamento de notas, nas quais ocorreram dois dos três incidentes graves dos últimos 18 meses. A alteração do módulo de matrícula depende de 1 profissional, entre os 6 especialistas em COBOL da sustentação, dos quais 2 se aposentam em 2027. COBOL é a linguagem de programação, muito antiga e hoje rara no mercado, em que está escrito o núcleo do sistema, descrito na página de [linha de base](linha-de-base.md). Sustentação é a equipe que corrige e mantém o sistema em funcionamento depois de pronto.

Diante desse quadro, a pergunta que organiza o caso é como evoluir o sistema acadêmico de forma segura e incremental, mantendo a operação contínua durante a transição e respeitando os compromissos contratuais já assumidos pela instituição.

Duas respostas óbvias já ficaram de fora quando a pergunta foi formulada. A Reitoria descartou em 12/03/2026 a substituição integral por um produto de mercado, por causa do custo de migração dos 214.000 históricos de egressos e da especificidade do regime acadêmico da instituição. A reescrita completa em uma única entrega também foi descartada, porque nenhuma janela do calendário acadêmico comporta a virada simultânea de todos os módulos.

## Mapa de atores

Cada pessoa que depende do sistema olha para ele de um lugar diferente, e o arquiteto precisa saber o que cada uma quer e o que teme antes de propor qualquer mudança. A tabela abaixo reúne oito papéis, com a área de cada um, o que espera do projeto e o que teme que aconteça, e o exercício do bloco 4 da Aula 2 parte dela para classificar as partes interessadas e delimitar o escopo do primeiro ciclo.

| Papel | Área | O que quer | O que teme |
| --- | --- | --- | --- |
| Reitora | Reitoria | Resultado visível em 12 meses e aplicativo móvel do aluno em operação antes do vestibular de 2027 | Investimento de R$ 6,2 milhões sem efeito perceptível e queda de nota na avaliação regulatória |
| Pró-Reitora de Graduação | Graduação | Matrícula sem falha e notas publicadas dentro do calendário | Repetição do incidente de 04/02/2026 e nova prorrogação da janela de matrícula |
| Diretor de TI | Tecnologia da Informação | Reduzir a dependência de especialistas COBOL e o custo anual de R$ 15,83 milhões | Perder os 6 profissionais de COBOL e ficar sem quem sustente o núcleo |
| Diretor Financeiro | Administração e Finanças | Preservar os contratos vigentes até o fim do prazo, já provisionados no plano plurianual | Desembolso duplicado, com legado e nuvem cobrados no mesmo exercício |
| Gerente de sustentação | Fábrica de software contratada | Manter o escopo e a previsibilidade do contrato até 30/09/2027 | Perder receita e escopo com a internalização do conhecimento do núcleo |
| Coordenadora de Educação a Distância | Educação a Distância | Notas e turmas propagadas ao ambiente virtual de aprendizagem em minutos | Continuar dependente do lote diário, com reclamação de aluno a cada fechamento |
| Encarregada de proteção de dados | Jurídico | Conformidade com a LGPD, a lei brasileira de proteção de dados pessoais, base legal declarada e trilha de auditoria sobre dado pessoal | Transferência de dado de aluno para fora do território nacional sem amparo |
| Representação discente | Diretório Central dos Estudantes | Aplicativo móvel e matrícula que não falhe na abertura | Perda de vaga em disciplina por indisponibilidade do portal |

## Interesses em conflito

Quando dois atores querem coisas incompatíveis, o arquiteto não resolve a diferença sozinho, porque nenhum desenho técnico concilia o que as duas partes pedem. Três pares de atores do mapa acima estão nessa situação, e a decisão cabe a quem tem autoridade orçamentária ou responde pelo processo acadêmico.

O primeiro par opõe o Diretor de TI ao Diretor Financeiro. O primeiro quer iniciar a migração de carga para nuvem no primeiro ciclo de 12 meses. O segundo observa que o contrato de capacidade do mainframe, o computador central onde roda o núcleo do sistema, vai até 31/12/2028 com volume mínimo contratado e cobrado mesmo que a ACME use menos, de modo que retirar carga não reduz desembolso antes de 2029 e apenas soma um custo novo ao custo existente. Desembolso é o dinheiro que sai do caixa da instituição.

O segundo par opõe o Diretor de TI ao Gerente de sustentação da fábrica. A cláusula de exclusividade do contrato de sustentação reserva à fábrica a manutenção dos programas COBOL do núcleo acadêmico até 30/09/2027. Qualquer estratégia que exija alterar esses programas para expor interfaces novas depende de um fornecedor cujo interesse comercial é preservar o escopo atual.

O terceiro par opõe a Coordenadora de Educação a Distância ao Diretor Financeiro. Hoje as notas lançadas pelo professor chegam ao ambiente virtual de aprendizagem, a plataforma em que os alunos de educação a distância acompanham as disciplinas, só no dia seguinte. Para que cheguem em minutos, o fornecedor da plataforma exige um plano superior, o único que oferece interfaces de programação, isto é, as portas pelas quais um sistema conversa com outro, com acréscimo de 38% sobre o valor anual do contrato vigente.

## Restrições fechadas

Algumas decisões já chegam tomadas ao arquiteto, e ele precisa projetar em torno delas. Restrição é a decisão tomada fora do processo de projeto, que limita as alternativas do arquiteto sem ser negociável por ele. Um exemplo é a proibição de parar o sistema em período letivo, que obriga qualquer mudança a ser feita aos poucos. As sete restrições abaixo chegam fechadas ao caso, e cada linha informa quem a impôs e o que ela implica para a arquitetura.

| Restrição | Origem e data | Consequência para a arquitetura |
| --- | --- | --- |
| O sistema acadêmico não pode parar em período letivo | Pró-Reitoria de Graduação | Toda estratégia é incremental, com o legado em operação durante a transição |
| O ambiente virtual de aprendizagem e o ERP financeiro permanecem | Reitoria, 12/03/2026 | O trabalho consiste em integrar e governar esses dois sistemas, sem substituí-los |
| Dois provedores de nuvem pré-aprovados | Conselho Universitário, 12/03/2026 | Decisões de plataforma precisam ser portáveis entre os dois |
| Identidade e autorização por padrões abertos, isto é, regras públicas para provar quem é o usuário e o que ele pode acessar | Comitê de Segurança da Informação | A escolha recai sobre o padrão, e o produto fica em aberto |
| Dado pessoal de aluno processado em território nacional | Jurídico, parecer de 28/04/2026 | Restringe a região de implantação, isto é, o local onde a nuvem executa o sistema, e o uso de serviços gerenciados, que o provedor opera no lugar da equipe |
| Manutenção do núcleo COBOL sob contrato até 30/09/2027 | Contrato de sustentação | Alterações no núcleo dependem de fornecedor externo |
| Orçamento de R$ 6,2 milhões para o primeiro ciclo de 12 meses | Reitoria | O roteiro de evolução precisa caber nesse valor antes de nova aprovação |

## Requisitos declarados pelas partes interessadas

Nas entrevistas de levantamento, cada parte interessada disse o que esperava do sistema, e o arquiteto chama de requisito toda exigência declarada sobre o que o sistema deve fazer ou sobre a qualidade com que deve funcionar. A tabela abaixo reproduz as quinze declarações recebidas, sem depuração editorial, e cada uma ganhou um código de R1 a R15, que os exercícios e os gabaritos usam para se referir a ela. Alguns itens trazem números a verificar, como o R6 e o R12, mas outros dizem apenas que o tempo de resposta "precisa ser bom" (R3) e que o sistema "precisa ser moderno" (R11), e ninguém consegue conferir se isso foi atendido. O exercício do bloco 2 da Aula 2 classifica esses requisitos e reescreve os que não admitem verificação.

| Código | Declaração | Origem |
| --- | --- | --- |
| R1 | O aluno deve renovar a matrícula pelo telefone celular, sem acesso ao portal em computador | Representação discente |
| R2 | A matrícula não pode cair | Pró-Reitoria de Graduação |
| R3 | O tempo de resposta precisa ser bom | Representação discente |
| R4 | A solução opera em um dos dois provedores de nuvem aprovados em 12/03/2026 | Conselho Universitário |
| R5 | O sistema emite histórico escolar com assinatura digital no padrão ICP-Brasil, a infraestrutura brasileira de certificados que dá validade legal a documentos eletrônicos | Secretaria Acadêmica |
| R6 | O portal sustenta 5.800 sessões simultâneas na abertura da matrícula, com percentil 95 do tempo de confirmação em até 4 segundos | Diretoria de TI |
| R7 | A nota lançada pelo professor chega ao ambiente virtual de aprendizagem em até 10 minutos | Educação a Distância |
| R8 | A autenticação usa padrões abertos de identidade, sem produto proprietário | Comitê de Segurança da Informação |
| R9 | Toda leitura de dado pessoal de aluno é registrada em trilha de auditoria, o registro de quem acessou o quê e quando, com retenção de 5 anos | Encarregada de proteção de dados |
| R10 | A manutenção dos programas COBOL do núcleo permanece sob o contrato da fábrica até 30/09/2027 | Contrato de sustentação |
| R11 | O sistema precisa ser moderno e escalável | Reitoria |
| R12 | A disponibilidade na janela de matrícula é de 99,9%, medida em minutos de indisponibilidade no mês | Pró-Reitoria de Graduação |
| R13 | O aluno consulta o resultado da solicitação de aproveitamento de disciplina pelo portal | Secretaria Acadêmica |
| R14 | Nenhum dado pessoal de aluno é processado fora do território nacional | Jurídico |
| R15 | O custo anual de propriedade do sistema acadêmico, hoje em R$ 15,83 milhões, cai para R$ 11,0 milhões até o fim de 2029, no mesmo escopo de medição | Diretoria de TI |

## Continuação do dossiê

Para saber de que o sistema é feito, a [arquitetura de linha de base](linha-de-base.md) descreve os componentes atuais, sua idade, quem os sustenta e o tipo de cada integração, isto é, a forma como dois sistemas trocam informação. Para saber como ele se comporta ao longo do ano, os [dados operacionais](dados-operacionais.md) trazem volumes, calendário acadêmico, incidentes, custos e contratos. E a página de [artefatos por aula](artefatos.md) registra o que cada aula acrescenta ao caso.
