---
secao: 7
titulo: Decisões
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| Para que serve | Daqui a alguns meses alguém vai perguntar por que a ACME decidiu assim, e a resposta precisa estar escrita. Esta seção guarda as escolhas principais da solução, cada uma com a razão que levou a ela, o requisito que atende e o que se aceitou perder. |
| Pergunta que responde | O que foi decidido, que requisito cada decisão atende e que consequências ela traz? |
| O que você escreve | Você registra as escolhas principais em grupos: as decisões de desenho, como o estilo da solução, as decisões sobre o sistema antigo e os dados, os blocos em que a solução se divide e as interfaces entre eles. Cada escolha importante recebe um registro de decisão arquitetural (ADR), um texto curto que guarda o contexto, as alternativas consideradas e as consequências. |
| Vem de onde | Das seções 3 e 6, porque toda decisão atende a um requisito e obedece a um princípio. |
| Quando se preenche | Você preenche esta seção nas Aulas 3 e 4, nos exercícios 10, 11, 12, 13, 14 e 16. |
<!--/orientacao-->

<!--ex n=10 titulo="Comparação de estilos e estilo recomendado"-->
<!--campos-->
- **Estilo:** escolha três dos sete estilos da aula e escreva o nome de cada um.
- **Adequação ao cenário 1:** para cada estilo, diga se ele é favorável, neutro ou desfavorável ao cenário do pico de matrícula, com o motivo em uma linha.
- **Adequação ao cenário 2:** faça o mesmo para o cenário do incidente de 04/02/2026.
- **Adequação aos princípios:** diga quais princípios priorizados no caderno o estilo sustenta e quais ele contraria.
- **Risco do estilo:** descreva o que o estilo traz de problema para a ACME.
- **Mecanismo compensatório:** diga o recurso que se acrescenta ao desenho para neutralizar esse risco.
- **Estilo recomendado:** escolha um dos três estilos.
- **Justificativa da recomendação:** explique a escolha pelo atributo de qualidade que o estilo favorece, pelo que ele prejudica e pelo princípio que desempata a comparação.
<!--/campos-->
<!--gabarito-->
#### Estilos comparados diante dos dois cenários

O pico de matrícula, com 5.800 sessões simultâneas e meta de erro abaixo de 1%, e o incidente de 04/02/2026, com 4h20 de indisponibilidade e 62% de erro, não pedem a mesma coisa de um estilo. Por isso cada um dos três estilos foi confrontado com os dois cenários, sempre com o núcleo COBOL sobre CICS em operação durante a transição.

| Estilo | Cenário 1, pico de matrícula | Cenário 2, incidente de 04/02/2026 |
| --- | --- | --- |
| Arquitetura orientada a eventos | Favorável. A fila absorve o pico, que é 7,1 vezes a média, e o núcleo processa no ritmo que sustenta | Neutro. O defeito foi a falta de tempo limite para sessões abandonadas, que continuavam ocupando o núcleo, e isso se corrige em qualquer estilo, enquanto a fila só ajuda a limitar as tarefas concorrentes |
| Arquitetura de microsserviços | Neutro. A escalabilidade seletiva, que amplia só a parte sob carga, só existe depois de extrair a matrícula do núcleo, trabalho de mais de um ciclo de 12 meses | Neutro. O isolamento de falha entre serviços ajuda, mas o abandono de sessão acontece no núcleo, que continua em operação |
| Arquitetura hexagonal | Neutro. Organiza a solução nova, mas não reduz sozinha a carga que chega ao núcleo | Favorável. O acesso ao núcleo passa por uma porta, que é o ponto único de entrada, e é nela que se declaram o tempo limite e o limite de tarefas concorrentes abaixo do limite do CICS |

#### Princípios, risco e recomendação

Depois dos cenários, cada estilo foi lido à luz dos quatro princípios priorizados no caderno, porque um estilo bom no pico ainda pode contrariar uma regra do projeto. O mecanismo compensatório é o recurso que neutraliza o risco que o estilo traz.

| Estilo | Princípios | Risco para a ACME | Mecanismo compensatório |
| --- | --- | --- | --- |
| Arquitetura orientada a eventos | Sustenta separação de responsabilidades e baixo acoplamento, e preserva o núcleo, o que atende a evolução incremental | Dificuldade de acompanhar uma operação do início ao fim, numa equipe que hoje não opera componente assíncrono | Identificador de correlação, um código que acompanha cada operação por todas as partes, e observabilidade do fluxo, que registra o que cada parte faz |
| Arquitetura de microsserviços | Sustenta separação de responsabilidades, mas contraria o baixo acoplamento com o núcleo, porque exige extrair a matrícula do COBOL | Extração do núcleo em conflito com a restrição do contrato de sustentação | Adiar a extração para depois de 30/09/2027 |
| Arquitetura hexagonal | Sustenta baixo acoplamento e evolução incremental, porque o núcleo passa a ser acessado por uma porta | Custo de uma chamada intermediária a mais em cada acesso | Limitar as portas às integrações que de fato serão substituídas |

O estilo recomendado é a arquitetura orientada a eventos na borda, com o núcleo preservado. O atributo favorecido é a escalabilidade elástica na entrada, que cresce e encolhe conforme a demanda e absorve o pico de matrícula, e o atributo prejudicado é a simplicidade de rastrear uma operação de ponta a ponta. A comparação se desempata pelo primeiro princípio, a evolução incremental, porque os eventos atendem o pico sem exigir alteração do COBOL.
<!--/gabarito-->
<!--/ex-->

<!--ex n=11 titulo="Padrões para os três problemas"-->
<!--campos-->
- **Padrão:** para cada um dos três problemas, escolha um padrão do repertório de dez da aula, ou mais de um quando resolverem partes diferentes do mesmo problema.
- **Nível do padrão:** diga se cada padrão é de estilo arquitetural, de padrão arquitetural ou de padrão de design, conforme a tabela de três níveis da aula.
- **Elemento afetado:** indique qual elemento do esboço lógico do caderno recebe o padrão.
- **Consequência favorável:** descreva o que a ACME ganha com o padrão.
- **Custo aceito:** descreva o que a ACME passa a pagar por ele.
- **Padrão descartado:** indique um padrão que você considerou e não adotou, em um dos três problemas.
- **Motivo do descarte:** explique por que o padrão não serve ao contexto da ACME.
<!--/campos-->
<!--gabarito-->
#### Padrões escolhidos para os três problemas

Cada problema da ACME pediu um padrão diferente. A tabela liga cada um ao padrão escolhido, ao elemento do esboço lógico que o recebe e ao que a escolha traz e custa. O Strangler Fig substitui o sistema antigo por partes, e o Anti-Corruption Layer traduz as chamadas entre o sistema novo e o antigo. O Timeout encerra a espera por uma resposta que demora, o Circuit Breaker interrompe as chamadas a um destino que falha, e o Bulkhead separa os recursos de cada chamador. O Transactional Outbox grava o evento na mesma transação do dado.

| Problema | Padrão e nível | Elemento afetado | Consequência favorável | Custo aceito |
| --- | --- | --- | --- | --- |
| Coexistência entre o legado e a solução nova | Strangler Fig e Anti-Corruption Layer, padrões arquiteturais, com Adapter, padrão de design, para implementar a tradução | Entrada da matrícula e Registro acadêmico | Cada funcionalidade é ativada por vez, com retorno ao legado, e a camada de tradução usa as transações CICS que já existem, sem depender da fábrica antes de 30/09/2027 | Duas implementações mantidas e dado sincronizado enquanto os 2.300 pontos de acesso direto existirem |
| Proteção contra falha de integração | Timeout, Circuit Breaker e Bulkhead, padrões arquiteturais | Entrada da matrícula | O tempo limite ataca a causa registrada do incidente de 04/02/2026, o disjuntor contém a falha do núcleo e a separação de conexões protege os demais portais | Desenhar o comportamento degradado da matrícula e ajustar limites sem ambiente de teste de carga, ausência registrada na linha de base |
| Publicação confiável de mudança acadêmica | Transactional Outbox, padrão arquitetural, com consumidor idempotente | Registro acadêmico e Publicação de notas | Toda nota gravada gera a sua mensagem, o que sustenta a entrega da nota em 10 minutos (requisito R7) sem esperar o lote das 05h10 | Entrega ao menos uma vez, volume de até 360.000 lançamentos no fechamento e plano do ambiente virtual com interfaces de programação, com acréscimo de 38% sobre o contrato |

A tabela de saída do Transactional Outbox, onde o evento espera para ser publicado, precisa ser gravada na mesma transação da nota, e hoje essa gravação ocorre dentro do programa COBOL. Essa dependência fica registrada como risco e como decisão pendente, a confirmar com a fábrica de software.

#### Padrões descartados

Dois padrões foram considerados e deixados de fora, porque não combinam com o contexto da ACME.

| Problema | Padrão descartado | Motivo |
| --- | --- | --- |
| Proteção contra falha de integração | Retry com limite na confirmação de matrícula | A operação não é idempotente, ou seja, repeti-la duplica o efeito, e pode duplicar a inscrição, e a repetição simultânea no pico amplia a sobrecarga que se quer conter |
| Publicação confiável de mudança acadêmica | Saga | A operação é uma gravação seguida de notificação, sem etapas em serviços distintos que exijam compensação, isto é, desfazer o que já foi feito |
<!--/gabarito-->
<!--/ex-->

<!--ex n=12 titulo="ADR do estilo e dos padrões"-->
<!--campos-->
- **Título:** escreva a sigla ADR, o número do registro e a decisão em uma frase.
- **Estado:** diga se o registro é proposta, aceito, substituído ou rejeitado.
- **Data:** escreva a data da decisão, ou "a definir" com o responsável, quando ela ainda não foi tomada.
- **Contexto:** descreva de forma neutra os dois cenários que motivaram a análise e diga o que fica fora do registro.
- **Forças:** liste o que diferencia as alternativas, ligando cada força a um princípio ou cenário e dando a medida quando o caso a traz.
- **Alternativas:** compare, pelas mesmas forças, os estilos que você descartou no exercício 10.
- **Decisão:** diga o estilo escolhido e os padrões do exercício 11, ligando a justificativa às forças listadas.
- **Consequências:** escreva ao menos uma consequência positiva, uma negativa e uma neutra, com o custo de cada padrão.
- **Evidências:** diga o que sustenta a decisão e onde cada evidência pode ser reproduzida.
- **Revisão:** escreva um gatilho que dá para observar, com valor e prazo.
<!--/campos-->
<!--gabarito-->
#### O registro da decisão sobre o estilo, orientado a eventos com padrões de convivência e de resiliência

O registro abaixo, o primeiro registro de decisão arquitetural (ADR) do caderno, junta o que os exercícios 9 a 11 decidiram, nos dez campos do modelo da aula. O estado é proposta porque o caso ainda não traz a data nem quem decide, e por isso esses dois pontos ficam marcados como a definir.

| Campo | Conteúdo |
| --- | --- |
| Título | ADR 001, adoção da arquitetura orientada a eventos na entrada da matrícula, com Strangler Fig, Anti-Corruption Layer, Timeout, Circuit Breaker, Bulkhead e Transactional Outbox |
| Estado | Proposta |
| Data | A definir, com o Diretor de TI |
| Contexto | O Portal do Aluno recebe em média 815 sessões simultâneas e chega a 5.800 na abertura da matrícula, com erro de 6,3% contra a meta de 1%. Em 04/02/2026, sessões abandonadas esgotaram as tarefas simultâneas que o servidor de transações CICS aceita, com 4h20 de indisponibilidade e 62% de erro na matrícula. O núcleo COBOL não pode ser alterado nem substituído durante a transição. Fica fora deste registro a escolha do produto de mensageria |
| Forças | Absorver o pico, que é 7,1 vezes a média, princípio da evolução incremental. Levar o erro de 6,3% a menos de 1%. Conter a indisponibilidade nos 43 minutos mensais de indisponibilidade que o acordo de nível de serviço, o compromisso de disponibilidade, permite. Preservar o núcleo, princípio do baixo acoplamento e restrição do contrato de sustentação. Entregar a nota em 10 minutos, princípio da separação de responsabilidades. Manter o dado pessoal em território nacional, princípio da segurança por desenho |
| Alternativas | Manter a arquitetura em camadas atual atende a preservação do núcleo, mas não as três primeiras forças, porque é a configuração que produz os 6,3% de erro. Microsserviços atenderiam a escalabilidade seletiva, mas exigem extrair a matrícula do COBOL, trabalho de mais de um ciclo de 12 meses em conflito com a preservação do núcleo. A arquitetura hexagonal protegeria o acesso ao núcleo, mas não reduz a carga do pico e acrescenta indireção |
| Decisão | Adotar a arquitetura orientada a eventos na entrada da matrícula, com fila entre a entrada da matrícula e o núcleo. Usar Strangler Fig e Anti-Corruption Layer para a convivência com o legado, Timeout, Circuit Breaker e Bulkhead contra a falha de integração e Transactional Outbox para publicar a nota. A fila absorve o pico sem tocar o núcleo, e os padrões atendem as forças de erro, de disponibilidade e de 10 minutos |
| Consequências | Positiva: o núcleo deixa de receber a rajada direta e processa no ritmo que sustenta. Negativa: o aluno recebe na hora só a confirmação de recebimento do pedido, a confirmação da matrícula chega depois, e a equipe passa a operar um componente assíncrono, em que quem envia segue adiante sem esperar resposta, com os custos de cada padrão, entre eles a manutenção de duas implementações, o ajuste de limites sem teste de carga e a entrega ao menos uma vez. Neutra: o tratamento de erro sai do horário de pico e passa para o processamento da fila |
| Evidências | Não existe teste de carga, porque a linha de base registra a ausência desse ambiente. A evidência disponível é o histórico do incidente de 04/02/2026, reproduzível pelos registros de operação do CICS. A evidência desejável e ausente é um ensaio de carga com 5.800 sessões em ambiente equivalente ao de produção |
| Revisão | Reabrir o registro se a taxa de erro na janela de matrícula seguinte ficar acima de 2%, ou se o percentil 95 do intervalo entre o lançamento e a chegada da nota ao ambiente virtual passar de 10 minutos por duas semanas seguidas |

Campos incompletos: a data e os decisores dependem do Diretor de TI, e a evidência de carga depende de um ambiente que a ACME ainda não tem.
<!--/gabarito-->
<!--/ex-->

<!--ex n=13 titulo="Efeito da solução no negócio"-->
<!--campos-->
- **Classificação da capacidade:** diga se cada uma das dez capacidades acadêmicas é estratégica, quando orienta a oferta e a qualidade do serviço, operacional, quando entrega o serviço ao aluno, ou de apoio, quando sustenta as demais.
- **Capacidade afetada:** marque as capacidades que o primeiro ciclo altera, a partir dos elementos que mudam na declaração de escopo do exercício 8, e escreva uma linha de justificativa para cada marcação.
- **Etapa com problema:** aponte as etapas do fluxo de valor do aluno em que ele percebe atraso, restrição de acesso ou falta de função.
- **Requisito da etapa:** para cada etapa apontada, diga se o problema é o da renovação pelo celular (R1), o da nota em até 10 minutos (R7) ou o da consulta do resultado de aproveitamento pelo portal (R13), ou registre que nenhum dos três se aplica.
- **Atividade que muda:** aponte as atividades do processo de lançamento de nota que mudam quando a nota passa a chegar ao ambiente virtual em até 10 minutos.
- **Unidade afetada:** diga qual unidade da organização sente essa mudança e qual atividade deixa de existir.
<!--/campos-->
<!--gabarito-->
#### Capacidades acadêmicas e o primeiro ciclo

O arquiteto começa por saber onde a mudança toca o trabalho da universidade. Das dez capacidades, duas são alteradas de forma direta, porque os pedidos do primeiro ciclo recaem sobre a matrícula e sobre as notas, e uma terceira é atingida de forma indireta. A classificação segue o critério do enunciado: estratégica é a capacidade que orienta a oferta e a qualidade do serviço, operacional é a que entrega o serviço ao aluno, e de apoio é a que sustenta as demais.

| Capacidade | Classificação | Afetada no primeiro ciclo | Justificativa |
| --- | --- | --- | --- |
| Admissão e ingresso | Operacional | Não | Nenhum dos cinco elementos que mudam toca esta capacidade |
| Oferta e grade curricular | Estratégica | Não | Nenhum dos cinco elementos que mudam toca esta capacidade |
| Matrícula em disciplinas | Operacional | Sim | O elemento E5 muda a renovação pelo celular, que é o requisito R1, e o incidente de 04/02/2026 ocorreu na abertura da matrícula |
| Avaliação e registro de notas | Operacional | Sim | O elemento E1 muda a integração de notas com o ambiente virtual, e o requisito R7 pede a nota nesse ambiente em até 10 minutos |
| Controle de frequência | Operacional | Não | Nenhum elemento que muda nem requisito do exercício a atinge |
| Emissão de documentos acadêmicos | Operacional | Não | Nenhum dos cinco elementos que mudam toca esta capacidade |
| Gestão de bolsas e descontos | Operacional | Indiretamente | A matrícula consulta essa capacidade para calcular a parcela, ela não muda, mas precisa continuar acessível |
| Cobrança de mensalidades | De apoio | Não | O ERP financeiro permanece por decisão da Reitoria |
| Biblioteca | De apoio | Não | Nenhum dos cinco elementos que mudam toca esta capacidade |
| Relação com o órgão regulador | De apoio | Não | É obrigação legal, e a extração do censo não muda no primeiro ciclo |

#### Etapas do fluxo de valor com problema

Ao percorrer o fluxo de valor do aluno, o arquiteto encontra problema em quatro das seis etapas. Três delas têm um requisito que pede a melhoria, a saber a renovação pelo celular (R1), a nota em até 10 minutos (R7) e a consulta do aproveitamento pelo portal (R13), e a etapa 3 mostra um atraso que nenhum requisito do exercício cobre.

| Etapa | Problema | Requisito |
| --- | --- | --- |
| 1. Renovar a matrícula | O Portal do Aluno não tem versão responsiva e restringe o uso em telefone celular | R1 |
| 3. Acessar a turma no ambiente virtual | Uma matrícula confirmada às 09h00 só aparece às 04h55 do dia seguinte, pela carga das 04h00 | Nenhum dos três |
| 5. Consultar a nota no ambiente virtual | Uma nota lançada às 15h00 só chega às 06h00 do dia seguinte | R7 |
| 6. Consultar o resultado de aproveitamento | A linha de base não registra consulta desse resultado pelo portal | R13 |

A etapa 2, a confirmação da matrícula, não entra na lista, porque ocorre no núcleo durante a sessão do aluno e não depende de lote. A etapa 4, o lançamento da nota, também não entra, porque o professor a registra no Portal do Professor durante o dia letivo, e o atraso só aparece na etapa 5.

#### Processo de lançamento de nota

Quando a nota passa a chegar em até 10 minutos, o arquivo gerado no lote das 05h10, a rotina noturna que processa os registros acumulados, perde a razão de existir, e a importação desse arquivo no ambiente virtual muda junto com ele. As demais atividades permanecem.

| Atividade | Situação | Motivo |
| --- | --- | --- |
| 1. Registrar a nota no Portal do Professor | Permanece | O professor continua lançando a nota no mesmo lugar |
| 2. Calcular média e situação | Permanece | Ocorre no núcleo, cuja manutenção está sob contrato até 30/09/2027 |
| 3. Gerar o arquivo de notas no lote das 05h10 | Muda e deixa de existir | A nota passa a ser publicada a cada lançamento |
| 4. Importar o arquivo de notas no ambiente virtual | Muda | O ambiente virtual passa a receber cada nota publicada |
| 5. Consultar a nota | Permanece | O aluno continua consultando no ambiente virtual |
| Retorno das 06h15 | Permanece | A devolução de nota de atividade e presença fica fora do alcance do requisito de 10 minutos (R7) |

A unidade afetada é a equipe de integrações e execução de lotes, que hoje gera o arquivo das 05h10. A Coordenação de Educação a Distância percebe o efeito, porque deixa de esperar o dia seguinte pela nota.
<!--/gabarito-->
<!--/ex-->

<!--ex n=14 titulo="Dados: dono, consistência e proteção"-->
<!--campos-->
- **Dono da entidade:** marque, para cada uma das cinco entidades, a aplicação ou o elemento do esboço lógico do exercício 9 que passa a ser o único autorizado a gravá-la na arquitetura alvo.
- **Justificativa do dono:** escreva uma linha por entidade, citando a capacidade afetada do exercício 13 que ela sustenta.
- **Regime de consistência:** para cada consumidor de cada entidade, diga se a leitura precisa refletir a gravação na hora (forte) ou dentro de um prazo (eventual, com o prazo escrito).
- **Estilo de dado mestre do aluno:** escolha entre registro, consolidação, coexistência e centralizado para o cadastro único do aluno.
- **Registro da escolha do dado mestre:** escreva em três linhas o contexto, a decisão e uma consequência da escolha.
- **Classificação dos atributos:** diga, para cada um dos seis atributos do aluno, se é dado pessoal ou dado pessoal sensível.
- **Destino com excesso de dado:** indique o destino que recebe mais atributos do que a finalidade exige.
- **Hipótese de conservação e origem do R14:** diga qual hipótese do art. 16 da LGPD autoriza guardar o histórico dos egressos e se a exigência de dado pessoal em território nacional (R14) vem da lei ou de decisão da instituição.
- **Motivo contra o acesso direto ao banco:** explique em até três linhas por que os 2.300 acessos diretos contrariam a propriedade do dado.
<!--/campos-->
<!--gabarito-->
#### Dono de cada entidade

Cada entidade, ou cada tipo de dado dentro dela, precisa de um único responsável por gravá-lo. A grade do enunciado mostra o núcleo transacional gravando as cinco entidades, enquanto o ambiente virtual e o ERP financeiro devolvem dado à ACME, e por isso a nota e o lançamento financeiro têm um dono para cada tipo de dado, o que mantém um único dono por tipo.

| Entidade | Dono | Capacidade que sustenta | Observação |
| --- | --- | --- | --- |
| Aluno | Núcleo transacional | Matrícula em disciplinas | O cadastro acadêmico do núcleo grava o aluno |
| Matrícula | Núcleo transacional | Matrícula em disciplinas | O serviço de matrícula pode ser o dono quando a regra de matrícula for extraída do núcleo, o que o contrato de sustentação até 30/09/2027 adia |
| Nota | Núcleo transacional para a nota consolidada, e ambiente virtual para a nota de atividade | Avaliação e registro de notas | A nota de atividade nasce no ambiente virtual e volta à ACME no lote das 06h15 |
| Lançamento financeiro | Núcleo transacional para o lançamento, e ERP financeiro para a baixa de pagamento | Gestão de bolsas e descontos, que alimenta a parcela da matrícula | A baixa nasce no ERP e volta à ACME no lote das 05h30 |
| Turma | Núcleo transacional | Matrícula em disciplinas | A turma é a base da matrícula e da carga do ambiente virtual |

Os portais Java não são donos de nenhuma entidade, embora gravem nas tabelas, porque gravam por acesso direto ao banco e sem passar pelo dono.

#### Regime de consistência por consumidor

Na abertura da matrícula a confirmação ao aluno deve ficar em até 4 segundos (requisito R6), e a Educação a Distância quer a nota no ambiente virtual em até 10 minutos (requisito R7). Consistência forte significa que a leitura reflete a gravação na hora, e eventual significa que a leitura reflete a gravação dentro de um prazo. Para os demais consumidores nenhum requisito pede prazo menor do que o lote atual, então o prazo declarado é o do lote que já existe.

| Entidade | Núcleo transacional | Portais Java | ERP financeiro | Ambiente virtual | Data warehouse |
| --- | --- | --- | --- | --- | --- |
| Aluno | Dono, grava | Forte, lê pelas transações do núcleo | Eventual, até 1 dia, lote das 23h10 | Eventual, até 1 dia, lote das 04h00 | Eventual, até 1 dia, lote das 02h30 |
| Matrícula | Dono, grava | Forte na confirmação de recebimento ao aluno, com percentil 95 de até 4 segundos pelo R6 | Não registrado | Eventual, até 1 dia, lote das 04h00 | Eventual, até 1 dia, lote das 02h30 |
| Nota | Dono da nota consolidada, grava | Forte | Não registrado | Eventual, até 10 minutos pelo R7, e devolução da nota de atividade em até 1 dia, lote das 06h15 | Eventual, até 1 dia, lote das 02h30 |
| Lançamento financeiro | Dono do lançamento, grava | Forte | Eventual, até 1 dia, lote das 23h10, e devolução da baixa em até 1 dia, lote das 05h30 | Não registrado | Eventual, até 1 dia, lote das 02h30 |
| Turma | Dono, grava | Forte | Não registrado | Eventual, até 1 dia, lote das 04h00 | Eventual, até 1 dia, lote das 02h30 |

O prazo de 1 dia, onde o dossiê não traz exigência, é a suposição adotada pelo curso. O dossiê registra que um pagamento compensado só aparece na situação do aluno cerca de 30 horas depois, e a Secretaria Acadêmica ou a Diretoria de TI pode pedir prazo menor.

#### Dado mestre do aluno

O aluno é a entidade compartilhada da ACME, com 38.400 alunos ativos e 214.000 egressos. Hoje só o cadastro acadêmico grava o aluno, e o aplicativo previsto para a arquitetura alvo vai atualizar endereço e telefone. O estilo centralizado atende a esse caso, porque a escrita ocorre num só lugar, o cadastro acadêmico, e todas as demais aplicações recebem cópia dele.

| Campo | Registro |
| --- | --- |
| Estilo | Centralizado, com o cadastro acadêmico do núcleo como sistema de registro, isto é, a fonte oficial do dado |
| Contexto | Ambiente virtual, ERP financeiro e data warehouse recebem cópia do aluno por lote, e o aplicativo do aluno vai gravar endereço e telefone |
| Decisão | A escrita ocorre só no cadastro acadêmico, e o aplicativo grava por meio dele, pelas transações existentes do núcleo |
| Consequência | Endereço e telefone deixam de divergir entre as cópias. O aplicativo depende das transações do núcleo, que não podem ser alteradas até 30/09/2027 |

#### Obrigações do dado pessoal do aluno

A tabela classifica os seis atributos pelo art. 5º da Lei Geral de Proteção de Dados (LGPD). Origem racial ou étnica e dado referente à saúde são dados pessoais sensíveis, e por isso cor ou raça e condição de deficiência exigem controle mais estrito.

| Atributo | Classificação | Destinos | Situação perante a necessidade |
| --- | --- | --- | --- |
| Nome e CPF | Dado pessoal | Ambiente virtual, ERP financeiro e data warehouse | O ambiente virtual identifica o aluno, e o CPF pode ser mais do que ele precisa |
| Endereço e telefone | Dado pessoal | ERP financeiro e data warehouse | O ERP usa para cobrança |
| Nota e situação por disciplina | Dado pessoal | Ambiente virtual e data warehouse | O ambiente virtual usa para exibir a nota |
| Cor ou raça autodeclarada | Dado pessoal sensível | Data warehouse | Coletada para o censo, que o núcleo extrai direto para o órgão regulador |
| Condição de deficiência | Dado pessoal sensível | Data warehouse | Coletada para o censo, como o atributo anterior |
| Histórico escolar de egresso | Dado pessoal | Data warehouse | Guardado para emissão de histórico com validade legal |

O destino que recebe mais do que a finalidade exige é o data warehouse, porque a cópia integral de 140 tabelas leva os dois atributos sensíveis, e o dossiê não registra finalidade analítica para eles. A hipótese do art. 16 que autoriza guardar o histórico dos 214.000 egressos é o cumprimento de obrigação legal ou regulatória pelo controlador (inciso I), já que a ACME emite histórico com validade legal. O dossiê não informa a norma que fixa o prazo de guarda, e a Encarregada de proteção de dados precisa confirmá-la. A exigência de que nenhum dado pessoal de aluno seja processado fora do território nacional (R14) decorre de decisão da instituição, apoiada no parecer do Jurídico de 28/04/2026, e não da LGPD, que não exige que o dado permaneça no território nacional.

#### Acesso direto ao banco

O banco Oracle, com 740 tabelas, é compartilhado entre o núcleo COBOL e a camada Java. Os 2.300 acessos diretos contrariam a propriedade do dado, porque fazem duas aplicações gravar as mesmas tabelas sem passar pelo dono. Qualquer mudança de estrutura passa a exigir alteração combinada no código COBOL e no código Java, mantidos por equipes distintas, e nenhum módulo pode ser extraído sem reescrever os pontos que o acessam.
<!--/gabarito-->
<!--/ex-->

<!--ex n=16 titulo="Contêineres e relações da arquitetura alvo"-->
<!--campos-->
- **Catálogo de blocos lógicos:** o catálogo dos blocos da arquitetura alvo, com a responsabilidade de cada um e a situação no primeiro ciclo, já vem pronto, e a Aula 5 o transforma em candidatos concretos, sem escolher produto nesta seção.
- **Modo de comunicação:** para cada uma das 15 relações do diagrama de contêineres, diga se é síncrona, quando quem chama espera a resposta, ou assíncrona, quando segue adiante.
- **Volume e latência:** para cada relação, escreva quanto passa por ela e quanto tempo a troca pode levar, usando os fatos dos dados operacionais, e escreva "não informado" quando o dossiê não trouxer o dado.
- **Relações do R6:** indique, pelo número, as relações que fazem parte do caminho da confirmação de recebimento do pedido de matrícula em até 4 segundos (requisito R6).
- **Relações do R7:** indique, pelo número, as relações que fazem parte do caminho da nota até o ambiente virtual em até 10 minutos (requisito R7).
- **Posição do núcleo transacional:** diga se o núcleo COBOL fica dentro ou fora da fronteira da solução, e por quê.
<!--/campos-->
<!--gabarito-->
#### Contêineres da arquitetura alvo e suas relações

Ao fim do primeiro ciclo, o aluno renova a matrícula pelo aplicativo, o professor lança a nota pelo portal, e dois serviços novos, o de matrícula e o de notas, chamam o núcleo COBOL pelas transações que ele já tem. Cada serviço novo tem banco próprio, e o núcleo continua gravando no banco Oracle existente. A figura mostra os contêineres e as 15 relações numeradas, e a tabela dá o que cada relação exige da comunicação. Contêiner, no modelo C4, é uma parte executável da solução, como um portal, um serviço ou um banco. O R6 é o requisito de confirmar o pedido de matrícula em até 4 segundos com 5.800 sessões simultâneas, e o R7 é o de entregar a nota em até 10 minutos. Na entrada da matrícula há uma fila entre o serviço de matrícula e o núcleo, proposta no ADR 001 e adotada como premissa do exercício 12, para que o pico de pedidos não chegue ao núcleo de uma só vez e não repita o esgotamento de tarefas do CICS de 04/02/2026.

#### Catálogo de blocos lógicos da arquitetura alvo

Esta é a lista de ABBs que a Aula 5 transforma em candidatos concretos. Ela declara responsabilidades, e não escolhe produto, framework ou provedor.

| ABB, bloco lógico | Responsabilidade | Situação no primeiro ciclo |
| --- | --- | --- |
| Interface do aplicativo do aluno | Permitir matrícula e consulta de notas no canal móvel | Novo |
| Portal do Professor | Permitir o lançamento de notas no canal já usado pelos professores | Modificado |
| Portal da Secretaria | Sustentar as operações acadêmicas da secretaria durante a transição | Modificado |
| Provedor de identidade | Autenticar e autorizar alunos, professores e equipe com padrões abertos | Novo, serviço contratado, com tecnologia a definir na Aula 5 |
| Serviço de matrícula | Receber solicitações e aplicar regras acadêmicas | Novo |
| Serviço de notas | Registrar, consultar e disponibilizar notas | Novo |
| Banco do serviço de matrícula | Persistir os dados próprios da matrícula | Novo |
| Banco do serviço de notas | Persistir os dados próprios das notas | Novo |
| Fila de solicitações de matrícula | Absorver o pico de pedidos e entregá-los ao núcleo no ritmo que ele sustenta | Novo |
| Evento de nota | Comunicar a publicação de notas ao ambiente virtual | Novo |
| Camada anticorrupção | Isolar os serviços novos das particularidades do COBOL | Novo |
| Observabilidade | Correlacionar eventos, métricas e registros dos serviços novos | Novo |
| Núcleo transacional COBOL sob CICS | Executar regras acadêmicas durante a transição | Permanece |

Fila de solicitações de matrícula, evento de nota, camada anticorrupção e observabilidade são responsabilidades lógicas transversais e podem ficar dentro de contêineres ou nas relações entre eles. Por isso, não precisam ganhar uma caixa própria no C4. O provedor de identidade é um serviço novo, contratado, e por isso fica fora da fronteira, mas leva o rótulo tecnologia a definir. O ambiente virtual, o gateway de pagamento, o ERP, o assinador digital e o órgão regulador são dependências externas. Eles influenciam os contratos, mas não são blocos que a ACME realiza neste ciclo.

![Diagrama de contêineres da arquitetura alvo do primeiro ciclo da ACME. No alto, professor, aluno e secretaria acadêmica. Dentro da fronteira do sistema acadêmico, o Portal do Professor e o Portal da Secretaria existentes, o aplicativo do aluno, os serviços de notas e de matrícula com banco próprio cada um e tecnologia a definir, e o núcleo transacional COBOL existente com o banco Oracle existente. À direita, fora da fronteira, o provedor de identidade, serviço novo contratado com tecnologia a definir, e os sistemas externos assinador digital ICP-Brasil, ambiente virtual de aprendizagem, gateway de pagamento, ERP financeiro e órgão regulador. As relações estão numeradas de 1 a 15.](../assets/images/acme-ex16-diagrama-de-conteineres-v2.svg){ .module-diagram }

| Relação | Origem e destino | Modo | Volume | Latência |
| --- | --- | --- | --- | --- |
| 1 | Aplicativo do aluno para serviço de matrícula | Síncrono | 5.800 sessões simultâneas no pico e 2.400 confirmações em 30 minutos | Percentil 95 de até 4 segundos para a confirmação de recebimento, pelo R6 |
| 2 | Portal do Professor para serviço de notas | Síncrono | 4.800 lançamentos em dia letivo comum e até 360.000 na janela de fechamento | Não informado |
| 3 | Serviço de matrícula para núcleo, por meio da fila | Assíncrono | O mesmo da relação 1 | Fora dos 4 segundos do R6, porque o serviço grava o pedido na fila e segue adiante, e o núcleo consome no ritmo que sustenta |
| 4 | Serviço de notas para núcleo | Síncrono | O mesmo da relação 2 | Não informado |
| 5 | Núcleo para banco Oracle | Síncrono | Até 14,2 milhões de transações no núcleo no primeiro dia da matrícula | Não informado, e fora dos 4 segundos do R6, porque o núcleo processa depois da fila |
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

O requisito de confirmação em até 4 segundos (R6) é sustentado pelas relações 1 e 8, que formam o caminho da confirmação de recebimento do pedido, da entrada do aluno ao serviço de matrícula e ao provedor de identidade. A fila da relação 3 tira o núcleo desse caminho, e é essa a justificativa da decisão do ADR 001: o núcleo, que a equipe não pode alterar até 30/09/2027 e que esgotou as tarefas do CICS no pico de 04/02/2026, passa a receber os pedidos no ritmo que sustenta, e não mais a rajada de 5.800 sessões. A confirmação da matrícula em si chega ao aluno depois, quando o núcleo processa o pedido, e a leitura do R6 como confirmação de recebimento fica registrada como pendência para a Diretoria de TI confirmar. O requisito de nota em até 10 minutos (R7) é sustentado pelas relações 2, 4 e 6, que levam a nota do portal ao ambiente virtual. A relação 12 fica fora da lista do R6, porque o dossiê não diz se a gravação no banco do serviço entra no tempo da confirmação, e a 13 fica fora da lista do R7 pelo mesmo motivo.

O núcleo transacional fica dentro da fronteira, como contêiner. A ACME detém a responsabilidade pelo núcleo e terceiriza à fábrica apenas a manutenção dos programas COBOL, e o critério que decide a posição de um elemento é a fronteira de responsabilidade sobre ele. O contrato de sustentação até 30/09/2027 impede que a equipe interna altere o núcleo, e por isso os serviços novos o acessam pelas transações existentes.
<!--/gabarito-->
<!--/ex-->
