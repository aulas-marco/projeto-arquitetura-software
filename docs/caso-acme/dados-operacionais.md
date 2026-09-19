# Dados operacionais

A ACME é uma universidade privada brasileira fictícia, com 38.400 alunos ativos, cujo sistema acadêmico opera desde 2004. Esta página reúne os dados de operação do sistema no ano letivo de 2026, usados nos exercícios de cenário de qualidade e de análise de risco. Os valores vêm do painel de capacidade da Diretoria de TI, do calendário acadêmico aprovado e dos registros do service desk.

## Volumes por período

A carga do sistema não é uniforme ao longo do ano. A tabela relaciona cada tipo de período à média diária observada em 2026.

| Período | Dias no ano | Sessões simultâneas, média | Transações no núcleo por dia | Percentil 95 do tempo de resposta |
| --- | --- | --- | --- | --- |
| Dia letivo comum | 168 | 640 | 1,9 milhão | 2,4 s |
| Semana de provas | 20 | 1.150 | 2,6 milhões | 3,1 s |
| Janela de fechamento de notas | 10 | 1.900 | 4,8 milhões | 5,7 s |
| Janela de matrícula | 18 | 2.700 | 6,1 milhões | 8,2 s |
| Abertura da matrícula, primeiro dia | 2 | 5.800 | 14,2 milhões | 11,8 s |
| Recesso | 47 | 90 | 0,3 milhão | 1,6 s |

O pico de 5.800 sessões simultâneas é medido nos 30 minutos seguintes à abertura da janela, às 08h00 do primeiro dia. Nesse intervalo, 2.400 matrículas são confirmadas e o restante das sessões permanece em fila ou expira por tempo limite. A taxa de erro nesse intervalo chega a 6,3% das requisições, contra 0,2% em dia letivo comum.

## Sazonalidade

A razão entre pico e média é o número que dimensiona a capacidade ociosa do sistema. Dois indicadores a expressam.

| Indicador | Média anual | Pico | Razão |
| --- | --- | --- | --- |
| Sessões simultâneas | 640 | 5.800 | 9,1 |
| Transações no núcleo por dia | 1,9 milhão | 14,2 milhões | 7,5 |

A capacidade contratada de processamento é dimensionada para o pico. Em dia letivo comum, a ocupação média fica em 24% da capacidade contratada, e nos dois dias de abertura de matrícula do ano ela chega a 94%. A instituição paga o ano inteiro por uma capacidade usada integralmente em 2 dias.

## Calendário acadêmico de 2026

| Evento | Janela | Dias úteis | Observação |
| --- | --- | --- | --- |
| Matrícula do primeiro semestre | 04/02/2026 a 16/02/2026 | 9 | Abertura às 08h00 de 04/02/2026 |
| Início das aulas do primeiro semestre | 23/02/2026 | 1 | |
| Fechamento de notas do primeiro semestre | 06/07/2026 a 10/07/2026 | 5 | 78% dos lançamentos nos dois últimos dias |
| Matrícula do segundo semestre | 27/07/2026 a 06/08/2026 | 9 | Abertura às 08h00 de 27/07/2026 |
| Início das aulas do segundo semestre | 10/08/2026 | 1 | |
| Extração do censo da educação superior | Maio de 2026 | 5 | Prazo legal, sem prorrogação |
| Fechamento de notas do segundo semestre | 07/12/2026 a 11/12/2026 | 5 | Concentração igual à do primeiro semestre |

Na janela de matrícula, 34.800 alunos renovam a inscrição em disciplina. Os outros 3.600 são ingressantes, que entram pelo processo seletivo e têm matrícula registrada pela Secretaria Acadêmica. O primeiro dia concentra 14.300 confirmações, ou 41% do total da janela, porque a ordem de chegada define a prioridade de vaga em turma com lotação esgotada.

Na janela de fechamento, 2.150 professores lançam notas de 4.900 turmas. A base é de 230.400 matrículas em disciplina, com 4 avaliações por disciplina, o que resulta em 921.600 lançamentos de nota por semestre.

## Incidentes registrados

Os três incidentes abaixo ocorreram nos últimos 18 meses e estão descritos nos relatórios de análise de causa arquivados pela Diretoria de TI.

### Esgotamento de tarefas do CICS na abertura da matrícula

| Campo | Registro |
| --- | --- |
| Data | 04/02/2026 |
| Duração | 4h20, das 08h00 às 12h20 |
| Causa | O limite de tarefas concorrentes do monitor CICS foi atingido porque sessões da camada JSF permaneciam com transação aberta após o abandono do navegador, sem tempo limite de sessão configurado |
| Impacto | 62% das tentativas de matrícula retornaram erro, 9.400 alunos não concluíram a inscrição no dia, a janela foi prorrogada em 2 dias úteis e o service desk registrou 1.100 chamados em 24 horas |

### Interrupção do lote de notas para o ambiente virtual

| Campo | Registro |
| --- | --- |
| Data | 09/07/2026 |
| Duração | 9h15, das 06h15 às 15h30 |
| Causa | A inclusão de um campo no cadastro acadêmico alterou o layout do arquivo posicional sem aviso ao fornecedor do ambiente virtual de aprendizagem, e o lote de retorno abortou no primeiro registro fora de posição |
| Impacto | 61.400 lançamentos de nota deixaram de ser propagados, o reprocessamento foi manual, e a publicação de notas atrasou 2 dias para 8.700 alunos, dentro da janela de fechamento do primeiro semestre |

### Indisponibilidade total do portal do aluno

| Campo | Registro |
| --- | --- |
| Data | 24/11/2025 |
| Duração | 2h50, das 09h40 às 12h30 |
| Causa | A rotina de expurgo de arquivos de recuperação do Oracle não foi executada por três dias, a área de arquivamento atingiu 100% de ocupação e o banco suspendeu todas as escritas |
| Impacto | 3.200 solicitações de documento foram perdidas e precisaram ser refeitas, R$ 148 mil em boletos não foram gerados no dia, e o incidente ocorreu em data de prazo regulatório de entrega de relatório |

Os três incidentes têm uma característica comum. Nenhum deles decorre de defeito na regra acadêmica. Todos decorrem de limite de recurso, de acoplamento por formato de arquivo ou de rotina operacional, isto é, de propriedades estruturais do sistema.

## Custo anual de infraestrutura

| Item | Valor anual |
| --- | --- |
| Contrato de capacidade de processamento de grande porte | R$ 4,80 milhões |
| Licenciamento Oracle, edição corporativa, 16 processadores | R$ 2,10 milhões |
| Servidor de aplicação e middleware de integração | R$ 0,64 milhão |
| Data center próprio, energia, refrigeração e enlaces | R$ 1,90 milhão |
| Contrato de sustentação com fábrica de software | R$ 3,60 milhões |
| Total | R$ 13,04 milhões |

O custo por aluno ativo é de R$ 340 por ano, ou 1,1% do orçamento anual da instituição. A Diretoria de TI declarou a meta de reduzir o total para R$ 9,0 milhões até o fim de 2029, registrada como requisito R15 na [página inicial do caso](index.md).

## Contratos vigentes

Cada contrato abaixo restringe uma classe de decisão arquitetural. A coluna de restrição indica o que a cláusula impede ou encarece.

| Contrato | Vigência | Cláusula relevante | Restrição imposta |
| --- | --- | --- | --- |
| Capacidade de processamento de grande porte | Até 31/12/2028 | Volume mínimo contratado, sem desconto por redução de uso antes do término | Retirar carga do núcleo não reduz desembolso antes de 2029 |
| Licenciamento Oracle | Renovação anual em 30/06 | Obrigação de licenciar todos os núcleos físicos de qualquer ambiente virtualizado onde o banco possa ser executado | Inviabiliza virtualização parcial e encarece réplica em nuvem |
| Sustentação do núcleo acadêmico | Até 30/09/2027 | Exclusividade sobre a manutenção dos programas COBOL do núcleo | Equipe interna não pode alterar o núcleo, mesmo para expor interfaces |
| Ambiente virtual de aprendizagem | Até 31/07/2029 | Integração incluída apenas por arquivo em formato do fornecedor, com interfaces de programação restritas ao plano superior | Propagação em minutos custa 38% a mais no valor anual |
| Gateway de pagamento | Até 30/04/2027 | Multa rescisória equivalente a 6 meses de tarifa média | Troca de provedor de cobrança fica fora do primeiro ciclo |
| Acordo de nível de serviço interno com a Graduação | Revisão anual em dezembro | Disponibilidade de 99,5% em período letivo e de 99,9% nas janelas de matrícula e fechamento | Define a medida de disponibilidade usada nos cenários de qualidade |

A disponibilidade de 99,9% na janela de matrícula corresponde a 43 minutos de indisponibilidade tolerada por mês. O incidente de 04/02/2026 consumiu 260 minutos, seis vezes o limite acordado.

## Leitura complementar

A composição dos módulos, o efetivo de sustentação e a dívida técnica medida estão na página de [arquitetura de linha de base](linha-de-base.md). Os atores, as restrições fechadas e a lista de requisitos declarados estão na [página inicial do caso](index.md).
