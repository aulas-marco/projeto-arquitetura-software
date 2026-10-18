# Template do caderno arquitetural

Ao longo do curso, a arquitetura da solução da ACME vai sendo registrada num único documento, seção por seção, e esse documento é o caderno arquitetural. Cada seção responde a uma pergunta e é preenchida por um ou mais exercícios, e por isso a trilha abaixo mostra as onze partes, com uma ficha que diz o que entra em cada seção, de onde vêm as informações e quando ela é preenchida. Quem encontrar um código como D1 ou R6 sem saber o que significa pode consultar a página de [convenções](convencoes.md), e o [mapa](mapa.md) mostra qual exercício preenche cada seção.

{{trilha:todas}}

{{folha:0}}

## A solução em uma página

<details class="caderno-secao" markdown="1">
<summary>Ver para que serve e o que vai nesta seção. Clique para abrir</summary>

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Quem decide sobre o projeto da ACME raramente lê o caderno inteiro e, mesmo assim, precisa apoiá-lo ou questioná-lo depois de poucos minutos de leitura. Por isso este resumo de uma página reúne o essencial, e a decisão pode ser tomada sem percorrer as outras seções. |
| Pergunta que responde | Se alguém lesse só esta página, entenderia o projeto? |
| O que você escreve | Você escreve seis parágrafos curtos, que contam nesta ordem qual é o problema, que pergunta o projeto responde, qual é a decisão central, que exigência mais pesa no desenho, quais são as consequências da decisão para a ACME e em que estágio está o trabalho. |
| Vem de onde | O resumo não traz informação nova, porque retoma em poucas linhas o que as outras seções já registram, e por isso ele é escrito depois delas. |
| Quando se preenche | Ao fim de cada aula você reescreve o resumo, nos exercícios 4, 8, 12, 16, 20 e 24, e cada versão substitui a anterior. |

Você escreve, no exercício 24:

- **O problema:** conte a situação da ACME e por que ela exige mudança, com os números do caso.
- **A pergunta:** escreva a pergunta que o projeto responde.
- **A decisão:** diga a decisão central do projeto e o estado dela, proposta ou aceita.
- **O que mais pesa no desenho:** diga qual exigência mais pesa, escrevendo o conteúdo e a medida antes do código.
- **Consequências:** diga o que a decisão custa à ACME, com ao menos uma consequência para a equipe.
- **Como está o trabalho:** diga o que está decidido, o que está proposto e o que falta, incluindo o roteiro em ondas e a conferência final.

</details>

{{/folha}}

{{folha:1}}

## 1. Contexto

<details class="caderno-secao" markdown="1">
<summary>Ver para que serve e o que vai nesta seção. Clique para abrir</summary>

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Antes de desenhar qualquer coisa, o arquiteto da ACME precisou descobrir de onde partia: qual era a situação da universidade, o que outras pessoas já tinham decidido e o que o projeto não podia mudar. Esta seção reúne esse ponto de partida para que o desenho comece em terreno conhecido. |
| Pergunta que responde | Que organização é esta, que problema ela quer resolver e o que já está decidido antes de desenhar qualquer coisa? |
| O que você escreve | Você registra cinco coisas, cada uma numa tabela. Primeiro vêm as restrições, que são decisões de outras pessoas que o projeto precisa aceitar, e depois as decisões da modernização, classificadas por nível de arquitetura. Em seguida entram os componentes da solução, que são as peças de que ela precisa, como pessoas, processos e tecnologia, e as tarefas do projeto, com o responsável por cada uma. Por fim, os documentos do trabalho são ligados às fases do processo. Cada item recebe um código curto, como RT1 para a primeira restrição ou D2 para a segunda decisão, explicado na página de convenções. |
| Vem de onde | Os números da instituição, a pergunta central e as restrições estão no dossiê do caso ACME, e é dele que você retira o conteúdo desta seção. |
| Quando se preenche | Você preenche esta seção na Aula 1, ao resolver os exercícios 1 a 4. |

### 1.1 Instituição, restrições e decisões por nível

Esta parte é preenchida no exercício 1.

Você escreve:

- **Dado do dossiê:** a instituição, a pergunta central e as restrições já vêm preenchidas, porque são dados do caso.
- **Nível:** escolha entre arquitetura corporativa, quando a decisão vale para a universidade inteira, de solução, quando vale para este projeto como um todo, e de software, quando vale só dentro de um componente de software.
- **Justificativa:** explique por que escolheu esse nível. Ajuda perguntar até onde o efeito da decisão chega e quem precisa ser avisado quando ela mudar.
- **Componente da solução afetado:** nas decisões de solução, diga que componentes da solução a decisão atinge além da tecnologia: pessoas, estruturas organizacionais (áreas e contratos), processos ou informação.
- **Dependência entre decisões:** veja se uma decisão só faz sentido depois de outra e, se fizer, diga qual vem primeiro e o que daria errado se a ordem fosse invertida.

### 1.2 Os componentes da solução, num exemplo da ACME

Esta parte é preenchida no exercício 2.

Você escreve:

- **Tipo do componente da solução:** classifique cada componente da solução em um dos cinco tipos: pessoas, estruturas organizacionais (áreas, contratos e acordos), processos, informação ou tecnologia.
- **Tipo do componente da solução ausente:** confira se algum tipo ficou sem nenhum componente da solução, o que indicaria algo esquecido na solução, e diga qual tipo mais muda a rotina de quem trabalha na instituição.
- **Nível do elemento:** diga se cada elemento da situação atual pertence ao sistema de negócio (o que a universidade oferece), ao sistema de informação (pessoas, processos e registros) ou ao sistema de TI (equipamentos e programas).
- **Prazo percebido:** explique por que trocar só a tecnologia pode não encurtar o prazo que o aluno percebe.

### 1.3 Papéis e responsabilidades do ciclo

Esta parte é preenchida no exercício 3.

Você escreve:

- **Responsável:** diga se a tarefa é do arquiteto de solução, do arquiteto de software ou da arquitetura corporativa, pelo mesmo critério do exercício 1: até onde o efeito da tarefa chega.
- **Justificativa:** explique em uma frase por que a tarefa é desse responsável.
- **Grupo de competência:** nas tarefas do arquiteto de solução, diga qual habilidade a tarefa pede mais: de negócio, técnica, de entrega ou prática (comunicação, relacionamento com as partes interessadas, requisitos).
- **Benefício de reaproveitar um componente de software:** escolha, entre os sete benefícios da abordagem arquitetural, o que justifica verificar se já existe um componente de software reaproveitável.

### 1.4 Artefatos nas fases do processo, premissas e escopo

Esta parte é preenchida no exercício 4.

Você escreve:

- **Fase:** diga em que fase do processo o artefato é produzido ou usado.
- **Papel:** diga se o artefato é entrada (a fase o recebe), produto intermediário (alimenta uma fase seguinte) ou entregável (é o resultado entregue ao patrocinador).
- **Linha de base:** marque os artefatos que já existiam antes de o processo começar e descrevem a situação atual.
- **Seção do caderno:** escreva em que seção do caderno o resultado do artefato fica registrado, consultando o template.
- **Dado do caso:** as premissas e as exclusões do escopo já vêm prontas, propostas pelo curso para você confirmar na descoberta.

</details>

{{/folha}}

{{folha:2}}

## 2. Partes interessadas

<details class="caderno-secao" markdown="1">
<summary>Ver para que serve e o que vai nesta seção. Clique para abrir</summary>

| Campo | Conteúdo |
| --- | --- |
| Para que serve | As decisões de um projeto dependem de pessoas, e na ACME a Reitora quer resultado em 12 meses, o Diretor Financeiro teme pagar o legado e a nuvem no mesmo ano e o Gerente de sustentação da fábrica teme perder o contrato. Esta seção registra quem são essas pessoas, o que cada uma espera e teme e como o arquiteto vai lidar com cada uma, e assim os conflitos aparecem cedo. |
| Pergunta que responde | Quem precisa participar das decisões e onde os interesses entram em conflito? |
| O que você escreve | Você monta primeiro uma tabela com o que cada pessoa ou grupo quer, o que teme e como o arquiteto vai tratá-lo: envolver nas decisões, consultar ou apenas manter informado. Depois escreve os pontos de vista de cada grupo, que são as preocupações que o desenho precisa mostrar, e a declaração de escopo, que diz o que muda no primeiro ciclo, o que fica como está e por que cada item ficou de fora. |
| Vem de onde | Da seção 1 e do mapa de atores do dossiê, que dizem quem são as pessoas envolvidas no projeto. |
| Quando se preenche | Você preenche esta seção na Aula 2, no exercício 8. |

### 2.1 Partes interessadas, pontos de vista e escopo do primeiro ciclo

Esta parte é preenchida no exercício 8.

Você escreve:

- **Categoria:** diga a que categoria de parte interessada cada um dos oito papéis pertence, entre as nove apresentadas no bloco 4, e indique qual papel exerce o patrocínio do negócio.
- **Papel que representa a categoria:** para cada uma das nove categorias, escreva o papel do mapa de atores que a representa. Se nenhum papel serve, deixe a categoria sem representante.
- **Risco da ausência:** nas categorias sem representante, explique o que pode dar errado no processo quando ninguém fala por elas.
- **Preocupação principal:** para cada um dos três papéis escolhidos, escreva a principal preocupação, partindo do que o papel teme.
- **Critério de seleção:** diga o que entra no recorte da arquitetura que o papel recebe, ou seja, quais partes do desenho interessam a ele.
- **Estrutura do artefato:** diga em que formato o documento é entregue ao papel, como uma tabela, um fluxo ou uma lista.
- **Forma de apresentação:** diga como a informação é mostrada ao papel, por exemplo lado a lado com outro dado ou com marcações.
- **Muda ou permanece:** para cada um dos dez elementos da declaração de escopo, diga se ele muda ou fica como está nos 12 meses do primeiro ciclo.
- **Origem da exclusão:** para cada elemento que permanece, diga qual restrição, contrato ou decisão de governança o manteve fora da mudança.

</details>

{{/folha}}

{{folha:3}}

## 3. Requisitos

<details class="caderno-secao" markdown="1">
<summary>Ver para que serve e o que vai nesta seção. Clique para abrir</summary>

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Quando alguém diz que o sistema precisa ser rápido, ninguém consegue saber depois se a solução deu certo. Esta seção transforma o que as pessoas pedem em requisitos que dá para verificar, cada um com um número e uma situação de uso. |
| Pergunta que responde | O que a solução precisa entregar, e como saberemos que entregou? |
| O que você escreve | Você lista os requisitos do caso, cada um com tipo, medida e prioridade, e reescreve os pedidos vagos com um número que dá para medir. Depois registra os fatores que empurram a mudança, que são os direcionadores, e os cenários de qualidade, que descrevem uma situação de uso em seis partes: quem provoca, o que provoca, em que situação, o que é afetado, o que o sistema faz e como se mede o resultado. |
| Vem de onde | Das seções 1 e 2, porque as restrições e as partes interessadas mostram o que pode se tornar requisito. |
| Quando se preenche | Você preenche esta seção na Aula 2, nos exercícios 5, 6 e 7. |

### 3.1 Direcionadores de mudança e fatores externos

Esta parte é preenchida no exercício 5.

Você escreve:

- **Resposta ao direcionador:** diga, para cada um dos sete direcionadores, se a ACME responde de forma reativa, porque o direcionador já virou problema, ou antecipatória, porque a mudança é prevista e ainda não produziu efeito.
- **Evidência da resposta:** cite o dado do caso que sustenta a escolha, como uma data, um valor ou um incidente.
- **Dimensão da análise PESTLE:** para cada um dos três fatos do dossiê, diga em qual das seis dimensões do ambiente externo ele se encaixa.
- **Fator externo acrescentado:** nas dimensões que ficaram sem fato, escreva um fator plausível para os próximos três anos e marque que ele é seu, porque o dossiê não o registra.
- **Efeito do contrato do mainframe na meta de custo:** explique em até cinco linhas por que o contrato de capacidade limita o que o projeto pode prometer de economia no primeiro ciclo.

### 3.2 Catálogo de requisitos e reescritas mensuráveis

Esta parte é preenchida no exercício 6.

Você escreve:

- **Categoria do requisito:** diga se cada uma das oito declarações é requisito funcional, requisito de atributo de qualidade ou restrição. Nenhuma fica como requisito não funcional.
- **Justificativa da categoria:** explique em uma frase por que a declaração pertence a essa categoria.
- **Formulação:** nas declarações de atributo de qualidade, diga se estão bem formuladas, isto é, se trazem o contexto e a medida, ou mal formuladas.
- **Contexto:** nas duas declarações que você reescrever, diga em que situação o requisito vale.
- **Carga:** diga quanto uso o sistema recebe nessa situação.
- **Medida:** diga o valor a atingir. Se a declaração não nomear atributo algum, registre isso e deixe a medida sem valor.

### 3.3 Cenários de qualidade, significância arquitetural e restrições

Esta parte é preenchida no exercício 7.

Você escreve:

- **Resposta do cenário do pico:** escreva o que o sistema faz quando chegam as 5.800 sessões simultâneas da abertura da matrícula.
- **Medida do cenário do pico:** escreva o valor que permite verificar a resposta em teste de carga, que simula as sessões e mede o resultado.
- **Artefato do cenário do incidente:** diga qual parte do sistema sofre o efeito das transações abertas que se acumulam.
- **Resposta do cenário do incidente:** escreva o que o sistema faz para o incidente de 04/02/2026 não se repetir.
- **Medida do cenário do incidente:** escreva o valor que permite verificar que o incidente não se repete.
- **Respostas ao roteiro de significância:** marque sim ou não para cada uma das sete perguntas, em cada cenário, com uma justificativa curta.
- **Conclusão sobre significância:** diga, em até três linhas por cenário, se ele é um requisito arquiteturalmente significativo.
- **Origem da restrição:** classifique cada uma das sete restrições do caso em regulatória, contratual, de política interna ou técnica.
- **Quem pode rever a restrição:** diga quem tem autoridade para mudar a restrição.

</details>

{{/folha}}

{{folha:4}}

## 4. Linha de base e lacunas

<details class="caderno-secao" markdown="1">
<summary>Ver para que serve e o que vai nesta seção. Clique para abrir</summary>

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Uma mudança só pode ser planejada quando se conhece o ponto de partida, e na ACME esse ponto é o sistema atual, com as suas fragilidades. Esta seção descreve esse sistema e o que o separa da solução desenhada, e linha de base é o nome da situação atual. |
| Pergunta que responde | Onde o sistema atual é frágil, e o que é preciso mudar para chegar ao que se quer construir? |
| O que você escreve | Você descreve o sistema atual, com as camadas que o formam, as integrações com outros sistemas e os incidentes que já aconteceram. Depois lista as lacunas, e cada uma é uma diferença entre o sistema atual e o que foi desenhado, acompanhada da forma de fechá-la. |
| Vem de onde | Do dossiê e da seção 3 para a descrição do sistema atual, e das seções 5 a 8, que descrevem a solução desenhada, para a lista de lacunas. |
| Quando se preenche | Você descreve o sistema atual na Aula 2, no exercício 7, e só depois, na Aula 6, no exercício 21, lista as lacunas. |

### 4.1 Artefatos de linha de base que sustentam os cenários

Esta parte é preenchida no exercício 7.

Você escreve:

- **Artefato de linha de base:** escolha quatro dos seis artefatos do enunciado que sustentam os dois cenários de qualidade.
- **Dado que o artefato fornece:** diga qual informação do artefato aparece no cenário.
- **Efeito de um dado desatualizado:** diga o que aconteceria com o cenário se esse dado estivesse desatualizado.

### 4.2 Lacunas por domínio e tipo

Esta parte é preenchida no exercício 21.

Você escreve:

- **Domínio da lacuna:** para cada uma das oito lacunas do enunciado, escolha um dos sete domínios do relatório de lacunas.
- **Tipo da lacuna:** diga se a lacuna é técnica ou organizacional.
- **Justificativa da classificação:** cite, em uma frase, o dado do caso que sustenta o tipo escolhido.
- **Forma de fechar a lacuna organizacional:** para cada lacuna organizacional, diga se ela pede capacitação, mudança de processo ou decisão de contrato.

</details>

{{/folha}}

{{folha:5}}

## 5. Contexto do sistema (C4, nível 1)

<details class="caderno-secao" markdown="1">
<summary>Ver para que serve e o que vai nesta seção. Clique para abrir</summary>

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Para que qualquer pessoa entenda a solução em um minuto, o arquiteto a desenha numa única figura, que mostra o que está dentro dela, quem a usa e com quais outros sistemas ela conversa. |
| Pergunta que responde | O que está dentro da solução, o que está fora e com quem ela se relaciona? |
| O que você escreve | Você desenha um diagrama de contexto no formato C4, nível 1, em que a solução aparece como uma caixa só, cercada por quem a usa e pelos outros sistemas com que ela conversa. Junto vão uma legenda e um parágrafo que explica por que cada sistema ficou dentro ou fora da solução. |
| Vem de onde | Das seções 2 e 4, porque as partes interessadas mostram quem usa a solução e o sistema atual mostra com quem ela conversa. |
| Quando se preenche | Você preenche esta seção na Aula 4, no exercício 15. |

### 5.1 Portfólio, contrato de notas e diagrama de contexto

Esta parte é preenchida no exercício 15.

Você escreve:

- **Classificação da aplicação:** diga se cada uma das onze aplicações do catálogo é verde (manter e evoluir), âmbar (manter por ora, com investimento restrito) ou vermelha (substituir ou retirar).
- **Justificativa da classificação:** escreva uma linha com o fato do caso que levou à cor, como o ano da aplicação, a tecnologia ou a decisão da Reitoria de mantê-la.
- **Contrato de integração de notas:** preencha, com resposta curta, os doze campos do contrato que leva a nota do sistema da ACME ao ambiente virtual de aprendizagem, de Origem até Nível de serviço.
- **Modo de comunicação:** diga se a integração é síncrona, quando quem pede espera a resposta, ou assíncrona, quando quem envia segue adiante, e justifique pelos padrões escolhidos no exercício 11.
- **Nota corrigida:** explique o que acontece quando o professor corrige uma nota que já foi enviada ao ambiente virtual.
- **Erros do diagrama:** aponte os dois erros de nível ou de fronteira que o diagrama de contexto do enunciado contém.
- **Correção de cada erro:** para cada erro, diga qual elemento está errado e onde ele deve ficar no diagrama.

</details>

{{/folha}}

{{folha:6}}

## 6. Princípios

<details class="caderno-secao" markdown="1">
<summary>Ver para que serve e o que vai nesta seção. Clique para abrir</summary>

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Quando chega uma proposta e ninguém sabe se ela é aceitável, a discussão recomeça do zero. Os princípios evitam isso, porque são regras que valem para todas as decisões do projeto, e escrevê-los antes de decidir permite recusar a proposta que quebre uma delas. |
| Pergunta que responde | Que regras o desenho precisa respeitar, de modo que uma proposta possa ser recusada por quebrá-las? |
| O que você escreve | Você monta uma tabela de princípios, cada um com a regra, o que ela proíbe e o requisito ou a restrição que a justifica. Um exemplo é o princípio de que o sistema antigo não é alterado por quem não é o fornecedor, que proíbe mexer no núcleo sem o fornecedor. |
| Vem de onde | Das seções 1 e 3, porque os princípios nascem das restrições e dos requisitos. |
| Quando se preenche | Você preenche esta seção na Aula 3, no exercício 9. |

### 6.1 Princípios priorizados e esboço lógico

Esta parte é preenchida no exercício 9.

Você escreve:

- **Princípio:** escolha, no repertório de nove princípios da aula, de três a cinco que as quatro exigências do caso justificam, e escreva o nome de cada um.
- **Motivação:** diga qual das quatro exigências originou o princípio, para que ele não pareça uma regra adotada por hábito.
- **Implicação no desenho:** descreva o que muda na solução quando o princípio é seguido e o que passa a ser proibido.
- **Evidência esperada:** diga o que se poderia medir ou conferir para provar que o princípio foi aplicado.
- **Prioridade:** numere os princípios do mais importante ao menos importante e explique qual deles vence quando dois entram em conflito.
- **Elemento lógico:** agrupe as oito responsabilidades que o enunciado numera de RS1 a RS8, como receber o pedido de renovação de matrícula, em três a cinco elementos e dê a cada um um nome que diga o que ele faz, sem citar produto, linguagem ou provedor.
- **Situação do elemento:** diga se o elemento continua sendo atendido pelo núcleo legado durante a transição ou se passa a ser um elemento novo.
- **Risco:** aponte ao menos uma coisa que pode dar errado no esboço e o princípio que ela ameaça.
- **Decisão pendente:** aponte ao menos uma escolha que ainda não pode ser feita e o princípio que ela afeta.

</details>

{{/folha}}

{{folha:7}}

## 7. Decisões

<details class="caderno-secao" markdown="1">
<summary>Ver para que serve e o que vai nesta seção. Clique para abrir</summary>

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Daqui a alguns meses alguém vai perguntar por que a ACME decidiu assim, e a resposta precisa estar escrita. Esta seção guarda as escolhas principais da solução, cada uma com a razão que levou a ela, o requisito que atende e o que se aceitou perder. |
| Pergunta que responde | O que foi decidido, que requisito cada decisão atende e que consequências ela traz? |
| O que você escreve | Você registra as escolhas principais em grupos: as decisões de desenho, como o estilo da solução, as decisões sobre o sistema antigo e os dados, os blocos em que a solução se divide e as interfaces entre eles. Cada escolha importante recebe um registro de decisão arquitetural (ADR), um texto curto que guarda o contexto, as alternativas consideradas e as consequências. |
| Vem de onde | Das seções 3 e 6, porque toda decisão atende a um requisito e obedece a um princípio. |
| Quando se preenche | Você preenche esta seção nas Aulas 3 e 4, nos exercícios 10, 11, 12, 13, 14 e 16. |

### 7.1 Comparação de estilos e estilo recomendado

Esta parte é preenchida no exercício 10.

Você escreve:

- **Estilo:** escolha três dos sete estilos da aula e escreva o nome de cada um.
- **Adequação ao cenário 1:** para cada estilo, diga se ele é favorável, neutro ou desfavorável ao cenário do pico de matrícula, com o motivo em uma linha.
- **Adequação ao cenário 2:** faça o mesmo para o cenário do incidente de 04/02/2026.
- **Adequação aos princípios:** diga quais princípios priorizados no caderno o estilo sustenta e quais ele contraria.
- **Risco do estilo:** descreva o que o estilo traz de problema para a ACME.
- **Mecanismo compensatório:** diga o recurso que se acrescenta ao desenho para neutralizar esse risco.
- **Estilo recomendado:** escolha um dos três estilos.
- **Justificativa da recomendação:** explique a escolha pelo atributo de qualidade que o estilo favorece, pelo que ele prejudica e pelo princípio que desempata a comparação.

### 7.2 Padrões para os três problemas

Esta parte é preenchida no exercício 11.

Você escreve:

- **Padrão:** para cada um dos três problemas, escolha um padrão do repertório de dez da aula, ou mais de um quando resolverem partes diferentes do mesmo problema.
- **Nível do padrão:** diga se cada padrão é de estilo arquitetural, de padrão arquitetural ou de padrão de design, conforme a tabela de três níveis da aula.
- **Elemento afetado:** indique qual elemento do esboço lógico do caderno recebe o padrão.
- **Consequência favorável:** descreva o que a ACME ganha com o padrão.
- **Custo aceito:** descreva o que a ACME passa a pagar por ele.
- **Padrão descartado:** indique um padrão que você considerou e não adotou, em um dos três problemas.
- **Motivo do descarte:** explique por que o padrão não serve ao contexto da ACME.

### 7.3 ADR do estilo e dos padrões

Esta parte é preenchida no exercício 12.

Você escreve:

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

### 7.4 Efeito da solução no negócio

Esta parte é preenchida no exercício 13.

Você escreve:

- **Classificação da capacidade:** diga se cada uma das dez capacidades acadêmicas é estratégica, quando orienta a oferta e a qualidade do serviço, operacional, quando entrega o serviço ao aluno, ou de apoio, quando sustenta as demais.
- **Capacidade afetada:** marque as capacidades que o primeiro ciclo altera, conforme a declaração de escopo do exercício 8, e escreva uma linha de justificativa para cada marcação.
- **Etapa com problema:** aponte as etapas do fluxo de valor do aluno em que ele percebe atraso, restrição de acesso ou falta de função.
- **Requisito da etapa:** para cada etapa apontada, diga se o problema é o da renovação pelo celular (R1), o da nota em até 10 minutos (R7) ou o da consulta do resultado de aproveitamento pelo portal (R13), ou registre que nenhum dos três se aplica.
- **Atividade que muda:** aponte as atividades do processo de lançamento de nota que mudam quando a nota passa a chegar ao ambiente virtual em até 10 minutos.
- **Unidade afetada:** diga qual unidade da organização sente essa mudança e qual atividade deixa de existir.

### 7.5 Dados: dono, consistência e proteção

Esta parte é preenchida no exercício 14.

Você escreve:

- **Dono da entidade:** marque, para cada uma das cinco entidades, a aplicação ou o elemento do esboço lógico do exercício 9 que passa a ser o único autorizado a gravá-la na arquitetura alvo.
- **Justificativa do dono:** escreva uma linha por entidade, citando a capacidade afetada do exercício 13 que ela sustenta.
- **Regime de consistência:** para cada consumidor de cada entidade, diga se a leitura precisa refletir a gravação na hora (forte) ou dentro de um prazo (eventual, com o prazo escrito).
- **Estilo de dado mestre do aluno:** escolha entre registro, consolidação, coexistência e centralizado para o cadastro único do aluno.
- **Registro da escolha do dado mestre:** escreva em três linhas o contexto, a decisão e uma consequência da escolha.
- **Classificação dos atributos:** diga, para cada um dos seis atributos do aluno, se é dado pessoal ou dado pessoal sensível.
- **Destino com excesso de dado:** indique o destino que recebe mais atributos do que a finalidade exige.
- **Hipótese de conservação e origem do R14:** diga qual hipótese do art. 16 da LGPD autoriza guardar o histórico dos egressos e se a exigência de dado pessoal em território nacional (R14) vem da lei ou de decisão da instituição.
- **Motivo contra o acesso direto ao banco:** explique em até três linhas por que os 2.300 acessos diretos contrariam a propriedade do dado.

### 7.6 Contêineres e relações da arquitetura alvo

Esta parte é preenchida no exercício 16.

Você escreve:

- **Catálogo de blocos lógicos:** o catálogo dos blocos da arquitetura alvo, com a responsabilidade de cada um e a situação no primeiro ciclo, já vem pronto, e a Aula 5 o transforma em candidatos concretos, sem escolher produto nesta seção.
- **Modo de comunicação:** para cada uma das 15 relações do diagrama de contêineres, diga se é síncrona, quando quem chama espera a resposta, ou assíncrona, quando segue adiante.
- **Volume e latência:** para cada relação, escreva quanto passa por ela e quanto tempo a troca pode levar, usando os fatos dos dados operacionais, e escreva "não informado" quando o dossiê não trouxer o dado.
- **Relações do R6:** indique, pelo número, as relações que fazem parte do caminho da confirmação de recebimento do pedido de matrícula em até 4 segundos (requisito R6).
- **Relações do R7:** indique, pelo número, as relações que fazem parte do caminho da nota até o ambiente virtual em até 10 minutos (requisito R7).
- **Posição do núcleo transacional:** diga se o núcleo COBOL fica dentro ou fora da fronteira da solução, e por quê.

</details>

{{/folha}}

{{folha:8}}

## 8. Tecnologia e plataforma

<details class="caderno-secao" markdown="1">
<summary>Ver para que serve e o que vai nesta seção. Clique para abrir</summary>

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Só depois de tomadas as decisões estruturais faz sentido escolher a tecnologia. Esta seção mostra com que produtos e plataforma a solução será construída e como ela será protegida contra ameaças. |
| Pergunta que responde | Que produtos e que plataforma atendem às decisões já tomadas, e que riscos de segurança precisam de resposta? |
| O que você escreve | Você lista as tecnologias aprovadas, proibidas e em avaliação e compara as alternativas por seis critérios. Depois registra a plataforma e a zona de pouso escolhidas, que é a base em nuvem onde a solução roda, classifica os dados por sensibilidade, relaciona cada ameaça de segurança aos controles contra ela e registra, para cada controle, quem o executa e como se verifica. A seção termina com o registro da decisão sobre a plataforma. |
| Vem de onde | Das seções 5 e 7, porque o desenho e as decisões já tomadas mostram o que a tecnologia precisa fazer. |
| Quando se preenche | Você preenche esta seção na Aula 5, nos exercícios 17, 18, 19 e 20. |

### 8.1 Modelo técnico, tecnologias da linha de base e provedor de identidade

Esta parte é preenchida no exercício 17.

Você escreve:

- **Linha do modelo e candidatos por bloco:** para cada bloco do catálogo, exceto o núcleo transacional que permanece, diga qual linha do modelo técnico de referência vale, qual padrão ela exige e quais exemplos aprovados da linha são os produtos candidatos, ou escreva candidato a levantar quando não houver linha.
- **Linhas válidas para todos os contêineres:** indique as duas linhas do recorte que valem para qualquer contêiner novo, qualquer que seja a função dele, e explique em uma frase.
- **Classificação da tecnologia:** classifique cada tecnologia da linha de base em verde, âmbar ou vermelho e justifique em uma linha com o dado da tabela.
- **Tecnologias sob plano de migração:** entre as vermelhas, diga quais continuam em uso hoje e só podem ficar enquanto houver plano de migração documentado.
- **Aderência e portabilidade das alternativas:** para cada forma de obter o provedor de identidade (PI1, PI2 e PI3), escreva o dado do caso que sustenta a aderência ao requisito e a portabilidade, citando o código do requisito ou da restrição.
- **Dado que falta por critério:** para maturidade, suporte, custo total de propriedade e competência da equipe, diga qual informação o caso não traz e precisa ser levantada.
- **Regra de eliminação pela restrição:** escolha R8 ou R14, diga qual condição elimina uma candidata e qual documento pediria para comprovar atendimento. Não descarte PI1, PI2 ou PI3 apenas pela forma de contratação.

### 8.2 Plataforma escolhida e zona de pouso

Esta parte é preenchida no exercício 18.

Você escreve:

- **Plataformas candidatas e ferramentas:** indique duas plataformas capazes de concretizar o estilo recomendado no exercício 10 e liste as ferramentas concretas de cada uma.
- **Comparação pelos critérios com dado:** para aderência ao requisito, custo total de propriedade, competência da equipe e portabilidade, diga qual plataforma atende melhor, ou se empatam, explicando por que em uma linha.
- **Dado que falta em maturidade e suporte:** escreva qual informação falta nesses dois critérios e quem poderia fornecê-la, sem dar valor às plataformas.
- **Plataforma escolhida:** escolha uma das duas e justifique pela convivência com o sistema antigo.
- **Pilar de cada elemento da zona de pouso:** ligue cada elemento do diagrama ao pilar da zona de pouso que ele realiza.
- **Etiquetas que faltam:** para cada recurso da tabela, diga quais das quatro etiquetas obrigatórias (projeto, ambiente, time e centro de custo) estão ausentes.
- **Requisito da conta de segurança e registros:** diga em uma linha qual requisito justifica a existência dessa conta.

### 8.3 Segurança dos dados, permissões e ameaças

Esta parte é preenchida no exercício 19.

Você escreve:

- **Classificação LGPD do ativo:** classifique cada um dos seis ativos em não pessoal, pessoal ou pessoal sensível, conforme o art. 5º da Lei Geral de Proteção de Dados (LGPD).
- **Nível de confidencialidade:** atribua nível baixo, médio ou alto a cada ativo e justifique em uma linha o nível do ativo pessoal sensível.
- **Ativos restritos pelo R14:** diga quais ativos não podem ser processados fora do território nacional, conforme a exigência R14, e qual sistema externo recebe hoje um deles.
- **Células que violam o menor privilégio:** aponte as três células da grade de permissões que dão acesso maior que o necessário, com o perfil e o recurso.
- **Acesso correto:** escreva o acesso correto de cada uma das três células, com a condição quando houver.
- **Categoria STRIDE da ameaça:** classifique cada ameaça, de AM1 a AM6, em uma das seis categorias do STRIDE, modelo que classifica ameaças em falsificação, adulteração, repúdio, divulgação de informação, negação de serviço e elevação de privilégio.
- **Controle da ameaça:** associe a cada ameaça a letra do controle que a trata.
- **Controle que também atende ao R9:** indique qual dos seis controles também atende ao requisito de trilha de auditoria (R9).
- **Decisão de segurança:** escreva em uma linha o que cada uma das cinco decisões, de DS1 a DS5, estabelece, usando as respostas dos itens 1 a 3.
- **Quem executa a decisão:** indique, para cada decisão, a equipe ou o papel que a executa, e os dois quando a execução se divide.
- **Como se verifica a decisão:** escreva em uma linha o teste ou a evidência que mostra o cumprimento de cada decisão.

### 8.4 ADR de plataforma e lacunas de provisão

Esta parte é preenchida no exercício 20.

Você escreve:

- **Título, estado e data:** escreva o título do ADR, o estado (proposto) e a data do registro.
- **Contexto:** descreva a situação que levou à decisão, citando pelo título o ADR de estilo do exercício 12.
- **Alternativas:** transporte o quadro comparativo do exercício 18, com as plataformas avaliadas pelos seis critérios do exercício 17.
- **Forças:** liste as pressões que pesam na escolha, com pelo menos três critérios de seleção e uma dimensão de dependência de fornecedor, cada uma com o dado do caso.
- **Decisão:** nomeie a plataforma escolhida e ligue a justificativa às forças.
- **Consequências:** escreva ao menos uma consequência positiva, uma negativa e uma neutra, considerando os achados de segurança do exercício 19.
- **Evidências:** diga o que sustentaria a escolha e onde poderia ser reproduzido, nomeando a evidência desejável que não existe.
- **Revisão:** escreva um gatilho observável, ligado à convivência com o núcleo COBOL sobre CICS, que indique a hora de reavaliar a plataforma.
- **Tipo da lacuna de provisão:** classifique cada um dos seis itens da definição tecnológica como lacuna nova, substituição, modificação ou remoção, com o dado da coluna de situação.
- **Lacuna que reduz custo recorrente:** indique qual item reduz custo recorrente já registrado nos dados operacionais e cite o dado.

</details>

{{/folha}}

{{folha:9}}

## 9. Roteiro e governança

<details class="caderno-secao" markdown="1">
<summary>Ver para que serve e o que vai nesta seção. Clique para abrir</summary>

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Uma boa solução falha quando é entregue na ordem errada ou sem acompanhamento. Esta seção define a ordem das entregas e a forma de vigiar a arquitetura, para que a obra não se afaste do desenho. |
| Pergunta que responde | Em que ordem as lacunas serão fechadas, e como evitar que a obra se afaste do que foi desenhado? |
| O que você escreve | Você divide o roteiro em ondas, que são etapas de entrega, e dá a cada uma as suas entregas e o critério para considerá-la concluída. Depois descreve a rotina de revisão da arquitetura, os testes automáticos que avisam quando uma decisão deixa de ser cumprida e o registro dos atalhos aceitos, que se chama dívida técnica. Por fim, você registra as regras de uso de IA no projeto, isto é, como cada saída de modelo é verificada e como a assistência é anotada no registro de decisão. |
| Vem de onde | Da seção 4, porque as lacunas confirmadas são a matéria das ondas. |
| Quando se preenche | Você preenche esta seção na Aula 6, nos exercícios 21, 22 e 23. |

### 9.1 Ordem das ondas e critério de conclusão

Esta parte é preenchida no exercício 21.

Você escreve:

- **Ordem das ondas:** coloque as três entregas do enunciado na ordem das ondas 1, 2 e 3.
- **Justificativa pelo critério de conclusão:** para cada onda, escreva em uma frase a dependência ou o critério de conclusão que justifica a posição.
- **Entrega que depende do fim da exclusividade da fábrica:** diga qual das três entregas só pode alterar o núcleo depois de 30/09/2027.
- **Ondas do primeiro ciclo:** diga quais ondas formam o primeiro ciclo de 12 meses e que orçamento elas respeitam.

### 9.2 Desvio, mecanismos de governança e quem decide

Esta parte é preenchida no exercício 22.

Você escreve:

- **Mecanismo contra o desvio:** associe cada uma das cinco situações do enunciado a um dos cinco mecanismos e diga o que o mecanismo faz nela.
- **Quem decide:** para cada pedido do enunciado, diga o tipo da decisão e quem a aprova.
- **Regra que vira função de adequação:** marque quais das quatro regras podem ser verificadas por um teste automático e diga quando o teste roda.
- **Decisão protegida pela função de adequação:** para cada regra marcada, diga qual decisão registrada ela protege.

### 9.3 Verificação de uma saída de IA e registro da assistência

Esta parte é preenchida no exercício 23.

Você escreve:

- **Verificação de rastreabilidade:** diga, para cada afirmação do contexto gerado, se ela tem origem em dado vigente e corrija as que não têm, citando a fonte.
- **Consequência omitida:** escreva as consequências negativas que o rascunho não traz, com o dado do enunciado que as comprova.
- **Decisão que volta à autoridade:** corrija o estado e a data do registro e diga quem decide.
- **Registro da assistência de IA:** escreva a ferramenta, as partes rascunhadas, o prompt e a versão, as verificações aplicadas e o revisor.

</details>

{{/folha}}

{{folha:10}}

## 10. O que ainda falta decidir

<details class="caderno-secao" markdown="1">
<summary>Ver para que serve e o que vai nesta seção. Clique para abrir</summary>

| Campo | Conteúdo |
| --- | --- |
| Para que serve | Nem tudo está decidido, e tratar como certo o que ainda é dúvida leva a decisões frágeis. Esta seção lista o que ainda falta e diz quem pode resolver cada ponto. |
| Pergunta que responde | O que ainda impede o projeto de seguir, e quem resolve? |
| O que você escreve | Você monta uma tabela com cada pendência, quem decide e quando ela deve ser resolvida. Na versão final, escrita no exercício 24, entra também a conferência do caderno completo, que aponta as decisões sem requisito de origem, os requisitos sem decisão e as pendências sem responsável. |
| Vem de onde | De todas as seções, porque toda premissa ainda não confirmada passa a ser uma pendência. |
| Quando se preenche | Ao fim de cada aula você atualiza a lista, nos exercícios 4, 8, 12, 16, 20 e 24, e cada versão substitui a anterior. |

Você escreve, no exercício 4:

- **Pendência da data de conclusão:** na seção 10, escreva quem decide a data de conclusão do ciclo e em que fase ela pode ser dada com precisão.

Você escreve, no exercício 24:

- **Inconsistência apontada:** indique a linha da tabela de rastreabilidade que viola uma regra e diga o que falta nela.
- **Regra violada:** diga qual das três regras de rastreabilidade a linha viola.
- **Pendência:** escreva cada pendência em uma frase que se entenda sozinha.
- **Quem decide:** nomeie o responsável por resolver a pendência.
- **Quando se resolve:** diga o marco ou a data em que a pendência deve estar resolvida.

</details>

{{/folha}}
