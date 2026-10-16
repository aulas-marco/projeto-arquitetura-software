---
secao: 6
titulo: Princípios
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| Para que serve | Quando chega uma proposta e ninguém sabe se ela é aceitável, a discussão recomeça do zero. Os princípios evitam isso, porque são regras que valem para todas as decisões do projeto, e escrevê-los antes de decidir permite recusar a proposta que quebre uma delas. |
| Pergunta que responde | Que regras o desenho precisa respeitar, de modo que uma proposta possa ser recusada por quebrá-las? |
| O que você escreve | Você monta uma tabela de princípios, cada um com a regra, o que ela proíbe e o requisito ou a restrição que a justifica. Um exemplo é o princípio de que o sistema antigo não é alterado por quem não é o fornecedor, que proíbe mexer no núcleo sem o fornecedor. |
| Vem de onde | Das seções 1 e 3, porque os princípios nascem das restrições e dos requisitos. |
| Quando se preenche | Você preenche esta seção na Aula 3, no exercício 9. |
<!--/orientacao-->

<!--ex n=9 titulo="Princípios priorizados e esboço lógico"-->
<!--campos-->
- **Princípio:** escolha, no repertório de nove princípios da aula, de três a cinco que as quatro exigências do caso justificam, e escreva o nome de cada um.
- **Motivação:** diga qual das quatro exigências originou o princípio, para que ele não pareça uma regra adotada por hábito.
- **Implicação no desenho:** descreva o que muda na solução quando o princípio é seguido e o que passa a ser proibido.
- **Evidência esperada:** diga o que se poderia medir ou conferir para provar que o princípio foi aplicado.
- **Prioridade:** numere os princípios do mais importante ao menos importante e explique qual deles vence quando dois entram em conflito.
- **Elemento lógico:** agrupe as oito responsabilidades do enunciado (RS1 a RS8) em três a cinco elementos e dê a cada um um nome que diga o que ele faz, sem citar produto, linguagem ou provedor.
- **Situação do elemento:** diga se o elemento continua sendo atendido pelo núcleo legado durante a transição ou se passa a ser um elemento novo.
- **Risco:** aponte ao menos uma coisa que pode dar errado no esboço e o princípio que ela ameaça.
- **Decisão pendente:** aponte ao menos uma escolha que ainda não pode ser feita e o princípio que ela afeta.
<!--/campos-->
<!--gabarito-->
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
<!--/gabarito-->
<!--/ex-->
