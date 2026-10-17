---
secao: 3
titulo: Requisitos
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| Para que serve | Quando alguém diz que o sistema precisa ser rápido, ninguém consegue saber depois se a solução deu certo. Esta seção transforma o que as pessoas pedem em requisitos que dá para verificar, cada um com um número e uma situação de uso. |
| Pergunta que responde | O que a solução precisa entregar, e como saberemos que entregou? |
| O que você escreve | Você lista os requisitos do caso, cada um com tipo, medida e prioridade, e reescreve os pedidos vagos com um número que dá para medir. Depois registra os fatores que empurram a mudança, que são os direcionadores, e os cenários de qualidade, que descrevem uma situação de uso em seis partes: quem provoca, o que provoca, em que situação, o que é afetado, o que o sistema faz e como se mede o resultado. |
| Vem de onde | Das seções 1 e 2, porque as restrições e as partes interessadas mostram o que pode se tornar requisito. |
| Quando se preenche | Você preenche esta seção na Aula 2, nos exercícios 5, 6 e 7. |
<!--/orientacao-->


<!--ex n=5 titulo="Direcionadores de mudança e fatores externos"-->
<!--campos-->
- **Resposta ao direcionador:** diga, para cada um dos sete direcionadores, se a ACME responde de forma reativa, porque o direcionador já virou problema, ou antecipatória, porque a mudança é prevista e ainda não produziu efeito.
- **Evidência da resposta:** cite o dado do caso que sustenta a escolha, como uma data, um valor ou um incidente.
- **Dimensão da análise PESTLE:** para cada um dos três fatos do dossiê, diga em qual das seis dimensões do ambiente externo ele se encaixa.
- **Fator externo acrescentado:** nas dimensões que ficaram sem fato, escreva um fator plausível para os próximos três anos e marque que ele é seu, porque o dossiê não o registra.
- **Efeito do contrato do mainframe na meta de custo:** explique em até cinco linhas por que o contrato de capacidade limita o que o projeto pode prometer de economia no primeiro ciclo.
<!--/campos-->
<!--gabarito-->
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
<!--/gabarito-->
<!--/ex-->

<!--ex n=6 titulo="Catálogo de requisitos e reescritas mensuráveis"-->
<!--campos-->
- **Categoria do requisito:** diga se cada uma das oito declarações é requisito funcional, requisito de atributo de qualidade ou restrição. Nenhuma fica como requisito não funcional.
- **Justificativa da categoria:** explique em uma frase por que a declaração pertence a essa categoria.
- **Formulação:** nas declarações de atributo de qualidade, diga se estão bem formuladas, isto é, se trazem o contexto e a medida, ou mal formuladas.
- **Contexto:** nas duas declarações que você reescrever, diga em que situação o requisito vale.
- **Carga:** diga quanto uso o sistema recebe nessa situação.
- **Medida:** diga o valor a atingir. Se a declaração não nomear atributo algum, registre isso e deixe a medida sem valor.
<!--/campos-->
<!--gabarito-->
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
<!--/gabarito-->
<!--/ex-->

<!--ex n=7 titulo="Cenários de qualidade, significância arquitetural e restrições"-->
<!--campos-->
- **Resposta do cenário do pico:** escreva o que o sistema faz quando chegam as 5.800 sessões simultâneas da abertura da matrícula.
- **Medida do cenário do pico:** escreva o valor que permite verificar a resposta em teste de carga, que simula as sessões e mede o resultado.
- **Artefato do cenário do incidente:** diga qual parte do sistema sofre o efeito das transações abertas que se acumulam.
- **Resposta do cenário do incidente:** escreva o que o sistema faz para o incidente de 04/02/2026 não se repetir.
- **Medida do cenário do incidente:** escreva o valor que permite verificar que o incidente não se repete.
- **Respostas ao roteiro de significância:** marque sim ou não para cada uma das sete perguntas, em cada cenário, com uma justificativa curta.
- **Conclusão sobre significância:** diga, em até três linhas por cenário, se ele é um requisito arquiteturalmente significativo.
- **Origem da restrição:** classifique cada uma das sete restrições do caso em regulatória, contratual, de política interna ou técnica.
- **Quem pode rever a restrição:** diga quem tem autoridade para mudar a restrição.
<!--/campos-->
<!--gabarito-->
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
<!--/gabarito-->
<!--/ex-->
