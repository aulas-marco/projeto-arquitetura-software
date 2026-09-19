# Dados operacionais

A ACME é uma universidade privada brasileira fictícia, com 38.400 alunos ativos, cujo sistema acadêmico opera desde 2004. Esta página reúne os dados de operação do sistema no ano letivo de 2026, usados nos exercícios de cenário de qualidade e de análise de risco. Os valores vêm do painel de capacidade da Diretoria de TI, do calendário acadêmico aprovado e dos registros do service desk.

## Volumes por período

A carga do sistema não é uniforme ao longo do ano. A tabela classifica os 251 dias úteis de 2026 em seis tipos de período, sem sobreposição entre eles, e relaciona cada tipo à média diária observada. Os dois dias de abertura de matrícula estão descontados dos dias de janela de matrícula, para que cada dia útil do ano seja contado uma única vez.

| Período | Dias úteis no ano | Sessões simultâneas, média | Transações no núcleo por dia | Percentil 95 do tempo de resposta |
| --- | --- | --- | --- | --- |
| Dia letivo comum | 153 | 640 | 1,9 milhão | 2,4 s |
| Recesso | 48 | 90 | 0,3 milhão | 1,6 s |
| Semana de provas | 20 | 1.150 | 2,6 milhões | 3,1 s |
| Janela de matrícula, dias subsequentes | 18 | 2.700 | 6,1 milhões | 8,2 s |
| Janela de fechamento de notas | 10 | 1.900 | 4,8 milhões | 5,7 s |
| Abertura da matrícula, primeiro dia | 2 | 5.800 | 14,2 milhões | 11,8 s |
| Total | 251 | | | |

O pico de 5.800 sessões simultâneas é medido nos 30 minutos seguintes à abertura da janela, às 08h00 do primeiro dia. Nesse intervalo, 2.400 matrículas são confirmadas e o restante das sessões permanece em fila ou expira por tempo limite. A taxa de erro nesse intervalo chega a 6,3% das requisições, contra 0,2% em dia letivo comum.

## Sazonalidade

A média anual é a média ponderada dos seis tipos de período pela quantidade de dias úteis de cada um, conforme a tabela acima. Para as sessões simultâneas, a soma de 153 vezes 640, 48 vezes 90, 20 vezes 1.150, 18 vezes 2.700, 10 vezes 1.900 e 2 vezes 5.800 resulta em 204.440, que dividido por 251 dias úteis dá 814 sessões. O mesmo cálculo aplicado às transações resulta em 543,3 milhões no ano e média de 2,16 milhões por dia útil.

| Indicador | Média anual ponderada | Pico | Razão |
| --- | --- | --- | --- |
| Sessões simultâneas | 814 | 5.800 | 7,1 |
| Transações no núcleo por dia | 2,16 milhões | 14,2 milhões | 6,6 |

A capacidade contratada de processamento é dimensionada para o pico, que ocupa 94% dela. A ocupação média anual é de 13%, obtida pela divisão dos 94% pela razão de 7,1, e em dia letivo comum fica em 10%.

## Calendário acadêmico de 2026

| Evento | Janela | Dias úteis | Observação |
| --- | --- | --- | --- |
| Matrícula do primeiro semestre | 04/02/2026 a 18/02/2026 previstos, encerrada em 20/02/2026 | 9 previstos, 11 efetivos | Abertura às 08h00 de 04/02/2026, com prorrogação de 2 dias úteis por causa do incidente daquele dia. Os dias 16/02 e 17/02 são recesso de carnaval |
| Início das aulas do primeiro semestre | 23/02/2026 | 1 | |
| Fechamento de notas do primeiro semestre | 06/07/2026 a 10/07/2026 | 5 | 78% dos lançamentos nos dois últimos dias |
| Matrícula do segundo semestre | 27/07/2026 a 06/08/2026 | 9 | Abertura às 08h00 de 27/07/2026, sem prorrogação |
| Início das aulas do segundo semestre | 10/08/2026 | 1 | |
| Extração do censo da educação superior | Maio de 2026 | 5 | Prazo legal, sem prorrogação |
| Fechamento de notas do segundo semestre | 07/12/2026 a 11/12/2026 | 5 | Concentração igual à do primeiro semestre |

As duas janelas de matrícula somam 20 dias úteis, dos quais 2 são de abertura e 18 são dias subsequentes, o que corresponde às duas linhas da tabela de volumes.

Na janela de matrícula, 34.800 alunos renovam a inscrição em disciplina. Os outros 3.600 são ingressantes, que entram pelo processo seletivo e têm matrícula registrada pela Secretaria Acadêmica. O primeiro dia concentra 14.300 confirmações, ou 41% do total da janela, porque a ordem de chegada define a prioridade de vaga em turma com lotação esgotada.

Na janela de fechamento, 2.150 professores lançam notas de 4.900 turmas. A base é de 230.400 matrículas em disciplina, com 4 avaliações por disciplina, o que resulta em 921.600 lançamentos de nota por semestre. A concentração de 78% nos dois últimos dias significa 359.424 lançamentos nesses dois dias e cerca de 67.600 por dia nos três primeiros.

## Incidentes registrados

Os três incidentes abaixo ocorreram nos últimos 18 meses e estão descritos nos relatórios de análise de causa arquivados pela Diretoria de TI. Nenhum deles teve origem em erro de regra acadêmica. As causas foram limite de recurso, acoplamento por formato de arquivo e rotina operacional, isto é, propriedades estruturais do sistema.

### Esgotamento de tarefas do CICS na abertura da matrícula

| Campo | Registro |
| --- | --- |
| Data | 04/02/2026 |
| Duração | 4h20, das 08h00 às 12h20 |
| Causa | O limite de tarefas concorrentes do monitor CICS foi atingido porque sessões da camada JSF permaneciam com transação aberta após o abandono do navegador, sem tempo limite de sessão configurado |
| Impacto | 62% das tentativas de matrícula retornaram erro, 9.400 alunos não concluíram a inscrição no dia, a janela foi prorrogada em 2 dias úteis e passou a encerrar em 20/02/2026, e o service desk registrou 1.100 chamados em 24 horas |

### Interrupção do lote de exportação de notas para o ambiente virtual

| Campo | Registro |
| --- | --- |
| Data | 09/07/2026 |
| Duração | 9h15, das 05h10 às 14h25 |
| Causa | A inclusão de um campo no cadastro acadêmico alterou o layout do arquivo posicional que a ACME produz no lote de exportação de notas das 05h10, sem aviso ao fornecedor do ambiente virtual de aprendizagem, e a carga do lado do fornecedor abortou no primeiro registro fora de posição |
| Impacto | Os 61.400 lançamentos de nota referentes a 08/07/2026 não chegaram ao ambiente virtual, o reprocessamento foi manual, e a publicação de notas atrasou 2 dias para 8.700 alunos, dentro da janela de fechamento do primeiro semestre |

### Indisponibilidade total do portal do aluno

| Campo | Registro |
| --- | --- |
| Data | 24/11/2025 |
| Duração | 2h50, das 09h40 às 12h30 |
| Causa | A rotina de expurgo de arquivos de recuperação do Oracle não foi executada por três dias, a área de arquivamento atingiu 100% de ocupação e o banco suspendeu todas as escritas |
| Impacto | 3.200 solicitações de documento foram perdidas e precisaram ser refeitas, R$ 148 mil em boletos não foram gerados no dia, e o incidente ocorreu em data de prazo regulatório de entrega de relatório |

## Custo anual do sistema acadêmico

O total abaixo é o custo de propriedade do sistema acadêmico. Ele soma infraestrutura, licenciamento, contrato de sustentação externa e a folha das 15 pessoas internas que a [arquitetura de linha de base](linha-de-base.md) atribui à sustentação do sistema, a um custo médio anual de R$ 186 mil por pessoa, já com encargos.

| Item | Valor anual |
| --- | --- |
| Contrato de capacidade de processamento de grande porte | R$ 4,80 milhões |
| Contrato de sustentação com fábrica de software | R$ 3,60 milhões |
| Pessoal interno de sustentação, 15 pessoas | R$ 2,79 milhões |
| Licenciamento Oracle, edição corporativa, 16 processadores | R$ 2,10 milhões |
| Data center próprio, energia, refrigeração e enlaces | R$ 1,90 milhão |
| Servidor de aplicação e middleware de integração | R$ 0,64 milhão |
| Total | R$ 15,83 milhões |

O custo por aluno ativo é de R$ 412 por ano, ou 2,8% do orçamento anual da instituição. A Diretoria de TI declarou a meta de reduzir esse mesmo total, com o mesmo escopo, para R$ 11,0 milhões até o fim de 2029, registrada como requisito R15 na [página inicial do caso](index.md).

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
