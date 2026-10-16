# Template do caderno arquitetural

O caderno arquitetural da ACME é o documento em que a arquitetura da solução fica registrada, seção por seção, ao longo do curso. Cada seção responde a uma pergunta e é preenchida por um ou mais exercícios. A trilha abaixo mostra as onze partes, e cada ficha explica o que entra na seção, de onde vêm as informações e quando ela é preenchida. Se um código como D1 ou R6 não for familiar, a página de [convenções](convencoes.md) explica todos, e o [mapa](mapa.md) mostra qual exercício preenche cada seção.

{{trilha:todas}}

{{folha:0}}

## A solução em uma página

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Quem decide sobre o projeto raramente lê o caderno inteiro. Este resumo de uma página dá a essa pessoa o essencial para apoiar o projeto ou questioná-lo. |
| Pergunta que responde | Se alguém lesse só esta página, entenderia o projeto? |
| O que você escreve | Seis parágrafos curtos: qual é o problema, que pergunta o projeto responde, qual é a decisão central, que requisito mais pesa no desenho, o que a ACME aceita perder em troca e em que pé está o trabalho. |
| Vem de onde | Das outras seções. O resumo só repete, em poucas linhas, o que o caderno já registra. |
| Quando se preenche | Ao fim de cada aula, nos exercícios 4, 8, 12, 16, 20 e 24. Cada versão substitui a anterior. |

{{/folha}}

{{folha:1}}

## 1. Contexto

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Antes de desenhar a solução, o arquiteto precisa conhecer o ponto de partida: a situação da ACME, o que outras pessoas já decidiram e o que o projeto não pode mudar. Esta seção reúne esse ponto de partida. |
| Pergunta que responde | Que organização é esta, que problema ela quer resolver e o que já está decidido antes de desenhar qualquer coisa? |
| O que você escreve | Cinco coisas, cada uma numa tabela. As restrições, que são decisões de outras pessoas que o projeto precisa aceitar. As decisões da modernização, classificadas por nível de arquitetura. Os componentes da solução, que são as peças de que ela precisa, como pessoas, processos e tecnologia. As tarefas do projeto, com o responsável por cada uma. E os documentos do trabalho, ligados às fases do processo. Cada item recebe um código curto, como RT1 ou D2, explicado na página de convenções. |
| Vem de onde | Do dossiê do caso ACME, que traz os números da instituição, a pergunta central e as restrições. |
| Quando se preenche | Na Aula 1, com os exercícios 1 a 4. |

### 1.1 Instituição, restrições e decisões por nível

Esta parte é preenchida no exercício 1.

Você escreve:

- **Dado do dossiê:** a instituição, a pergunta central e as restrições já vêm preenchidas, porque são dados do caso.
- **Nível:** escolha entre arquitetura corporativa, quando a decisão vale para a universidade inteira, de solução, quando vale para este projeto como um todo, e de software, quando vale só dentro de um componente.
- **Justificativa:** explique por que escolheu esse nível. Ajuda perguntar até onde o efeito da decisão chega e quem precisa ser avisado quando ela mudar.
- **Componente não tecnológico afetado:** nas decisões de solução, diga que parte da organização a decisão atinge além da tecnologia: as pessoas, a estrutura (áreas e contratos), os processos ou as informações.
- **Dependência entre decisões:** veja se uma decisão só faz sentido depois de outra e, se fizer, diga qual vem primeiro e o que daria errado se a ordem fosse invertida.

### 1.2 Componentes da solução do R7

Esta parte é preenchida no exercício 2.

Você escreve:

- **Tipo do componente:** classifique cada componente em um dos cinco tipos: pessoas, estruturas organizacionais (áreas, contratos e acordos), processos, informação ou tecnologia.
- **Tipo sem componente:** confira se algum tipo ficou sem nenhum componente, o que indicaria algo esquecido na solução, e diga qual tipo mais muda a rotina de quem trabalha na instituição.
- **Nível do elemento:** diga se cada elemento da situação atual pertence ao sistema de negócio (o que a universidade oferece), ao sistema de informação (pessoas, processos e registros) ou ao sistema de TI (equipamentos e programas).
- **Prazo percebido:** explique por que trocar só a tecnologia pode não encurtar o prazo que o aluno percebe.

### 1.3 Papéis e responsabilidades do ciclo

Esta parte é preenchida no exercício 3.

Você escreve:

- **Responsável:** diga se a tarefa é do arquiteto de solução, do arquiteto de software ou da arquitetura corporativa, pelo mesmo critério do exercício 1: até onde o efeito da tarefa chega.
- **Justificativa:** explique em uma frase por que a tarefa é desse responsável.
- **Grupo de competência:** nas tarefas do arquiteto de solução, diga qual habilidade a tarefa pede mais: de negócio, técnica, de entrega ou prática (comunicação, relacionamento com as partes interessadas, requisitos).
- **Benefício da tarefa T10:** escolha, entre os sete benefícios da abordagem arquitetural, o que justifica verificar se já existe um componente reaproveitável.

### 1.4 Artefatos nas fases do processo, premissas e escopo

Esta parte é preenchida no exercício 4.

Você escreve:

- **Fase:** diga em que fase do processo o artefato é produzido ou usado.
- **Papel:** diga se o artefato é entrada (a fase o recebe), produto intermediário (alimenta uma fase seguinte) ou entregável (é o resultado entregue ao patrocinador).
- **Linha de base:** marque os artefatos que já existiam antes de o processo começar e descrevem a situação atual.
- **Seção do caderno:** escreva em que seção do caderno o resultado do artefato fica registrado, consultando o template.
- **Dado do caso:** as premissas e as exclusões do escopo já vêm prontas, propostas pelo curso para você confirmar na descoberta.

{{/folha}}

{{folha:2}}

## 2. Partes interessadas

| Campo | Conteúdo |
| --- | --- |
| Para que serve | As decisões de um projeto dependem de pessoas, e elas nem sempre querem a mesma coisa. Esta seção registra quem são, o que cada uma espera e teme e como o arquiteto vai lidar com cada uma, para que os conflitos apareçam cedo. |
| Pergunta que responde | Quem precisa participar das decisões e onde os interesses entram em conflito? |
| O que você escreve | Uma tabela com o que cada pessoa ou grupo quer, o que teme e como o arquiteto vai tratá-lo: envolver nas decisões, consultar ou apenas manter informado. Depois, os pontos de vista de cada grupo, que são as preocupações que o desenho precisa mostrar, e a declaração de escopo: o que muda no primeiro ciclo, o que fica como está e por que cada item ficou de fora. |
| Vem de onde | Da seção 1 e do mapa de atores do dossiê. |
| Quando se preenche | Na Aula 2, no exercício 8. |

{{/folha}}

{{folha:3}}

## 3. Requisitos

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Um pedido vago, como "o sistema precisa ser rápido", não permite saber se a solução deu certo. Esta seção transforma o que as pessoas pedem em requisitos que dá para verificar, com número e situação de uso. |
| Pergunta que responde | O que a solução precisa entregar, e como saberemos que entregou? |
| O que você escreve | A lista de requisitos do caso, cada um com tipo, medida e prioridade, e os pedidos vagos reescritos com um número que dá para medir. Também os fatores que empurram a mudança, que são os direcionadores, e os cenários de qualidade, que descrevem uma situação de uso em seis partes: quem provoca, o que provoca, em que situação, o que é afetado, o que o sistema faz e como se mede o resultado. |
| Vem de onde | Das seções 1 e 2, porque restrições e partes interessadas dizem o que pode virar requisito. |
| Quando se preenche | Na Aula 2, nos exercícios 5, 6 e 7. |

{{/folha}}

{{folha:4}}

## 4. Linha de base e lacunas

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Uma mudança só pode ser planejada se o ponto de partida for conhecido. Esta seção descreve o sistema atual, onde ele é frágil e o que o separa da solução desenhada. Linha de base é o nome da situação atual. |
| Pergunta que responde | Onde o sistema atual é frágil, e o que é preciso mudar para chegar ao que se quer construir? |
| O que você escreve | A descrição do sistema atual, com as camadas que o formam, as integrações com outros sistemas e os incidentes que já aconteceram. Depois, a lista de lacunas: cada diferença entre o sistema atual e o que foi desenhado, com a forma de fechá-la. |
| Vem de onde | Do dossiê e da seção 3. Para as lacunas, também das seções 5 a 8, que descrevem a solução desenhada. |
| Quando se preenche | A descrição do sistema atual, na Aula 2 (exercício 7). A lista de lacunas, na Aula 6 (exercício 21). |

{{/folha}}

{{folha:5}}

## 5. Contexto do sistema (C4, nível 1)

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Mostra os limites da solução num único desenho: o que está dentro, quem a usa e com quais outros sistemas ela conversa. É o desenho que qualquer pessoa consegue ler em um minuto. |
| Pergunta que responde | O que está dentro da solução, o que está fora e com quem ela se relaciona? |
| O que você escreve | Um diagrama de contexto no formato C4, nível 1, que mostra a solução como uma caixa só, cercada por quem a usa e pelos outros sistemas com que ela conversa. Junto, uma legenda e um parágrafo explicando por que cada sistema ficou dentro ou fora da solução. |
| Vem de onde | Das seções 2 e 4: as partes interessadas mostram quem usa a solução, e o sistema atual mostra com quem ela conversa. |
| Quando se preenche | Na Aula 4, no exercício 15. |

{{/folha}}

{{folha:6}}

## 6. Princípios

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Princípios são regras que valem para todas as decisões do projeto. Escrevê-los antes de decidir permite recusar uma proposta que quebre uma regra, sem discutir do zero cada caso. |
| Pergunta que responde | Que regras o desenho precisa respeitar, de modo que uma proposta possa ser recusada por quebrá-las? |
| O que você escreve | Uma tabela de princípios, cada um com a regra, o que ela proíbe e o requisito ou a restrição que a justifica. Um exemplo é "o sistema antigo não é alterado por quem não é o fornecedor", que proíbe mexer no núcleo por conta própria. |
| Vem de onde | Das seções 1 e 3, porque os princípios nascem das restrições e dos requisitos. |
| Quando se preenche | Na Aula 3, no exercício 9. |

{{/folha}}

{{folha:7}}

## 7. Decisões

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Aqui ficam as escolhas principais da solução, cada uma com a razão que levou a ela. Quem ler daqui a alguns meses entende por que se decidiu assim, o que a decisão atende e o que se aceitou perder. |
| Pergunta que responde | O que foi decidido, que requisito cada decisão atende e o que se aceita perder com ela? |
| O que você escreve | As escolhas principais, em grupos: as decisões de desenho, como o estilo da solução, as decisões sobre o sistema antigo e os dados, os blocos em que a solução se divide e as interfaces entre eles. Cada escolha importante vira um registro de decisão arquitetural (ADR), um texto curto que guarda o contexto, as alternativas consideradas e as consequências. |
| Vem de onde | Das seções 3 e 6: toda decisão atende a um requisito e obedece a um princípio. |
| Quando se preenche | Nas Aulas 3 e 4, nos exercícios 10, 11, 12, 13, 14 e 16. |

{{/folha}}

{{folha:8}}

## 8. Tecnologia e plataforma

| Campo | Conteúdo |
| --- | --- |
| Para que serve | A tecnologia só se escolhe depois que as decisões estruturais estão tomadas. Esta seção mostra com que produtos e plataforma a solução será construída e como ela será protegida contra ameaças. |
| Pergunta que responde | Que produtos e que plataforma atendem às decisões já tomadas, e que riscos de segurança precisam de resposta? |
| O que você escreve | A lista de tecnologias aprovadas, proibidas e em avaliação, e a comparação entre alternativas por seis critérios. A plataforma e a zona de pouso escolhidas, que é a base em nuvem onde a solução roda. A classificação dos dados por sensibilidade, as ameaças de segurança com os controles contra cada uma e o registro da decisão sobre a plataforma. |
| Vem de onde | Das seções 5 e 7: o desenho e as decisões já tomadas mostram o que a tecnologia precisa fazer. |
| Quando se preenche | Na Aula 5, nos exercícios 17, 18, 19 e 20. |

{{/folha}}

{{folha:9}}

## 9. Roteiro e governança

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Uma boa solução falha se for entregue na ordem errada ou sem acompanhamento. Esta seção define a ordem das entregas e como a arquitetura é vigiada para que a obra não se afaste do desenho. |
| Pergunta que responde | Em que ordem as lacunas serão fechadas, e como evitar que a obra se afaste do que foi desenhado? |
| O que você escreve | O roteiro dividido em ondas, que são etapas de entrega, cada uma com suas entregas e o critério para dá-la por concluída. A rotina de revisão da arquitetura, os testes automáticos que avisam quando uma decisão deixa de ser cumprida e o registro dos atalhos aceitos, que se chama dívida técnica. |
| Vem de onde | Da seção 4, porque as lacunas confirmadas são a matéria das ondas. |
| Quando se preenche | Na Aula 6, nos exercícios 22 e 23. |

{{/folha}}

{{folha:10}}

## 10. O que ainda falta decidir

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Nem tudo está decidido. Esta seção lista o que ainda falta, para que ninguém trate como certo o que ainda é dúvida, e diz quem pode resolver cada ponto. |
| Pergunta que responde | O que ainda impede o projeto de seguir, e quem resolve? |
| O que você escreve | Uma tabela com cada pendência, quem decide e quando ela deve ser resolvida. Na versão final entra também a avaliação de uma tendência tecnológica e do efeito que ela teria sobre a solução. |
| Vem de onde | De todas as seções: toda premissa ainda não confirmada vira uma pendência. |
| Quando se preenche | Ao fim de cada aula, nos exercícios 4, 8, 12, 16, 20 e 24. Cada versão substitui a anterior. |

{{/folha}}
