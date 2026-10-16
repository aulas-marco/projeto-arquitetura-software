# Template do caderno arquitetural

O caderno arquitetural da ACME é o documento em que a arquitetura da solução fica registrada, seção por seção, ao longo do curso. Cada seção responde a uma pergunta e é preenchida por um ou mais exercícios. A trilha abaixo mostra as onze partes, e cada ficha explica o que entra na seção, de onde vêm as informações e quando ela é preenchida. Se um código como D1 ou R6 não for familiar, a página de [convenções](convencoes.md) explica todos, e o [mapa](mapa.md) mostra qual exercício preenche cada seção.

{{trilha:todas}}

{{folha:0}}

## A solução em uma página

| Campo | Conteúdo |
| --- | --- |
| O que é esta seção | Um resumo de uma página, para quem não vai ler o caderno inteiro. |
| Pergunta que responde | Se alguém lesse só esta página, entenderia o projeto? |
| O que você escreve | Seis parágrafos curtos: o problema, a pergunta, a decisão central, o requisito que mais pesa, o que a ACME aceita perder em troca e como está o trabalho. |
| Vem de onde | Das outras seções. O resumo só repete, em poucas linhas, o que o caderno já registra. |
| Quando se preenche | Ao fim de cada aula, nos exercícios 4, 8, 12, 16, 20 e 24. Cada versão substitui a anterior. |

{{/folha}}

{{folha:1}}

## 1. Contexto

| Campo | Conteúdo |
| --- | --- |
| O que é esta seção | A situação da ACME e o que a modernização precisa respeitar. |
| Pergunta que responde | Que organização é esta, que problema ela quer resolver e o que já está decidido antes de desenhar qualquer coisa? |
| O que você escreve | Tabelas com as restrições (RT1 a RT7), as decisões (D1 a D9), os componentes da solução (CP1 a CP10), as tarefas do ciclo (T1 a T10), os artefatos do processo (A1 a A10) e as premissas (PR1 a PR7). A página de convenções explica cada código. |
| Vem de onde | Do dossiê do caso ACME, que traz os números da instituição, a pergunta central e as restrições. |
| Quando se preenche | Na Aula 1, com os exercícios 1 a 4. |

### 1.1 Instituição, restrições e decisões por nível

Esta parte é preenchida no exercício 1.

Você escreve:

- **Dado do dossiê:** a instituição, a pergunta central e as restrições já vêm preenchidas, porque são dados do caso.
- **Nível:** diga se cada decisão, de D1 a D9, é de arquitetura corporativa, de solução ou de software.
- **Justificativa:** explique em uma frase o que a decisão muda e quem é afetado por ela.
- **Componente não tecnológico afetado:** nas decisões de solução, diga se a mudança atinge pessoas, estruturas organizacionais, processos ou informação.
- **Dependência entre decisões:** diga qual decisão precisa vir antes de outra e o que acontece se a ordem for invertida.

### 1.2 Componentes da solução do R7

Esta parte é preenchida no exercício 2.

Você escreve:

- **Tipo do componente:** classifique cada componente, de CP1 a CP10, em pessoas, estruturas organizacionais, processos, informação ou tecnologia.
- **Tipo sem componente:** confira se algum dos cinco tipos ficou vazio e diga qual tipo mais muda o trabalho de quem está na instituição.
- **Nível do elemento:** diga se cada elemento da situação atual, de N1 a N6, pertence ao sistema de negócio, ao sistema de informação ou ao sistema de TI.
- **Prazo percebido:** explique por que uma solução só de TI pode não reduzir o prazo que o aluno percebe.

### 1.3 Papéis e responsabilidades do ciclo

Esta parte é preenchida no exercício 3.

Você escreve:

- **Responsável:** diga se cada tarefa, de T1 a T10, cabe ao arquiteto de solução, ao arquiteto de software ou à arquitetura corporativa.
- **Justificativa:** explique em uma frase por que a tarefa é desse responsável.
- **Grupo de competência:** nas tarefas do arquiteto de solução, diga se elas pedem competência de negócio, técnica, de entrega ou prática.
- **Benefício da tarefa T10:** escolha o benefício da abordagem arquitetural que justifica verificar se já existe um componente reaproveitável.

### 1.4 Artefatos nas fases do processo, premissas e escopo

Esta parte é preenchida no exercício 4.

Você escreve:

- **Fase:** diga em que fase do processo cada artefato, de A1 a A10, é produzido ou usado.
- **Papel:** diga se o artefato é entrada, produto intermediário ou entregável.
- **Linha de base:** marque os artefatos que já existiam antes de o processo começar.
- **Seção do caderno:** diga em que seção do caderno o resultado de cada artefato fica registrado.
- **Dado do caso:** as premissas e as exclusões do escopo já vêm prontas, propostas pelo curso para você confirmar na descoberta.

{{/folha}}

{{folha:2}}

## 2. Partes interessadas

| Campo | Conteúdo |
| --- | --- |
| O que é esta seção | As pessoas e os grupos com interesse no projeto. |
| Pergunta que responde | Quem precisa participar das decisões e onde os interesses entram em conflito? |
| O que você escreve | Uma tabela com o que cada pessoa ou grupo quer, o que teme e como o arquiteto vai tratá-lo (envolver nas decisões, consultar ou manter informado). Depois, os pontos de vista de cada grupo e a declaração de escopo: o que muda no primeiro ciclo, o que fica como está e por que cada item ficou de fora. |
| Vem de onde | Da seção 1 e do mapa de atores do dossiê. |
| Quando se preenche | Na Aula 2, no exercício 8. |

{{/folha}}

{{folha:3}}

## 3. Requisitos

| Campo | Conteúdo |
| --- | --- |
| O que é esta seção | O que o sistema precisa fazer, escrito de um jeito que dá para verificar. |
| Pergunta que responde | O que a solução precisa entregar, e como saberemos que entregou? |
| O que você escreve | A lista de requisitos do caso (R1 a R15), cada um com tipo, medida e prioridade, e os requisitos vagos reescritos com um número que dá para medir. Também os fatores que empurram a mudança, os direcionadores, e os cenários de qualidade (CQ1, CQ2 e assim por diante), que descrevem uma situação de uso em seis partes: quem provoca, o que provoca, em que situação, o que é afetado, o que o sistema faz e como se mede. |
| Vem de onde | Das seções 1 e 2, porque restrições e partes interessadas dizem o que pode virar requisito. |
| Quando se preenche | Na Aula 2, nos exercícios 5, 6 e 7. |

{{/folha}}

{{folha:4}}

## 4. Linha de base e lacunas

| Campo | Conteúdo |
| --- | --- |
| O que é esta seção | Como o sistema é hoje e o que falta para chegar à solução desenhada. Linha de base é o nome da situação atual. |
| Pergunta que responde | Onde o sistema atual é frágil, e o que é preciso mudar para chegar ao que se quer construir? |
| O que você escreve | A descrição do sistema atual, com camadas, integrações e incidentes. Depois, a lista de lacunas (L1, L2 e assim por diante): cada diferença entre o sistema atual e o desenhado, com a forma de fechá-la. |
| Vem de onde | Do dossiê e da seção 3. Para as lacunas, também das seções 5 a 8, que descrevem a solução desenhada. |
| Quando se preenche | A descrição do sistema atual, na Aula 2 (exercício 7). A lista de lacunas, na Aula 6 (exercício 21). |

{{/folha}}

{{folha:5}}

## 5. Contexto do sistema (C4, nível 1)

| Campo | Conteúdo |
| --- | --- |
| O que é esta seção | Um desenho simples que mostra a solução como uma caixa só, quem a usa e com quais outros sistemas ela conversa. |
| Pergunta que responde | O que está dentro da solução, o que está fora e com quem ela se relaciona? |
| O que você escreve | Um diagrama de contexto no formato C4, nível 1, com legenda, e um parágrafo que explica por que cada sistema ficou dentro ou fora. |
| Vem de onde | Das seções 2 e 4: as partes interessadas mostram quem usa a solução, e o sistema atual mostra com quem ela conversa. |
| Quando se preenche | Na Aula 4, no exercício 15. |

{{/folha}}

{{folha:6}}

## 6. Princípios

| Campo | Conteúdo |
| --- | --- |
| O que é esta seção | As regras que valem para todas as decisões de desenho. |
| Pergunta que responde | Que regras o desenho precisa respeitar, de modo que uma proposta possa ser recusada por quebrá-las? |
| O que você escreve | Uma tabela de princípios (P1, P2 e assim por diante). Cada princípio diz o que proíbe e qual requisito ou restrição o justifica. |
| Vem de onde | Das seções 1 e 3, porque os princípios nascem das restrições e dos requisitos. |
| Quando se preenche | Na Aula 3, no exercício 9. |

{{/folha}}

{{folha:7}}

## 7. Decisões

| Campo | Conteúdo |
| --- | --- |
| O que é esta seção | As escolhas principais da solução, cada uma com o motivo. |
| Pergunta que responde | O que foi decidido, que requisito cada decisão atende e o que se aceita perder com ela? |
| O que você escreve | As decisões de desenho (DD1, DD2...), as decisões sobre o sistema antigo e os dados (DL1, DL2...), os blocos da solução (B1, B2...), as interfaces entre blocos (I1, I2...) e os registros de decisão arquitetural (ADR). O ADR é um texto curto que guarda o contexto, as alternativas e as consequências de uma escolha importante. |
| Vem de onde | Das seções 3 e 6: toda decisão atende a um requisito e obedece a um princípio. |
| Quando se preenche | Nas Aulas 3 e 4, nos exercícios 10, 11, 12, 13, 14 e 16. |

{{/folha}}

{{folha:8}}

## 8. Tecnologia e plataforma

| Campo | Conteúdo |
| --- | --- |
| O que é esta seção | Com que tecnologia a solução será construída e como ela será protegida. |
| Pergunta que responde | Que produtos e que plataforma atendem às decisões já tomadas, e que riscos de segurança precisam de resposta? |
| O que você escreve | A lista de tecnologias aprovadas, proibidas e em avaliação, a comparação entre alternativas por seis critérios, a plataforma e a zona de pouso escolhidas (a base em nuvem onde a solução roda), a classificação dos dados, as ameaças de segurança com seus controles (C1, C2...) e o ADR da plataforma. |
| Vem de onde | Das seções 5 e 7: o desenho e as decisões já tomadas mostram o que a tecnologia precisa fazer. |
| Quando se preenche | Na Aula 5, nos exercícios 17, 18, 19 e 20. |

{{/folha}}

{{folha:9}}

## 9. Roteiro e governança

| Campo | Conteúdo |
| --- | --- |
| O que é esta seção | A ordem em que a mudança acontece e como a arquitetura é acompanhada depois de aprovada. |
| Pergunta que responde | Em que ordem as lacunas serão fechadas, e como evitar que a obra se afaste do que foi desenhado? |
| O que você escreve | O roteiro dividido em ondas, cada onda com suas entregas e o critério para dá-la por concluída. Também a rotina de revisão da arquitetura, os testes automáticos que avisam quando uma decisão deixa de ser cumprida (FA1, FA2...) e o registro dos atalhos aceitos, que se chama dívida técnica. |
| Vem de onde | Da seção 4, porque as lacunas confirmadas são a matéria das ondas. |
| Quando se preenche | Na Aula 6, nos exercícios 22 e 23. |

{{/folha}}

{{folha:10}}

## 10. O que ainda falta decidir

| Campo | Conteúdo |
| --- | --- |
| O que é esta seção | O que ainda não foi decidido ou confirmado, e quem pode decidir. |
| Pergunta que responde | O que ainda impede o projeto de seguir, e quem resolve? |
| O que você escreve | Uma tabela com cada pendência, quem decide e quando ela deve ser resolvida. Na versão final entra também a avaliação de uma tendência tecnológica. |
| Vem de onde | De todas as seções: toda premissa ainda não confirmada vira uma pendência. |
| Quando se preenche | Ao fim de cada aula, nos exercícios 4, 8, 12, 16, 20 e 24. Cada versão substitui a anterior. |

{{/folha}}
