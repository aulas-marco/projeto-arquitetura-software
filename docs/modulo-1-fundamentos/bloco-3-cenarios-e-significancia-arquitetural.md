# Cenários de qualidade e significância arquitetural

Este bloco responde a uma pergunta que segue diretamente da anterior, como tornar um requisito de atributo de qualidade concreto o bastante para orientar decisão, e como julgar se um requisito, de qualquer natureza, deve pesar sobre a arquitetura.

## Antes de começar

- [Cenário de atributo de qualidade](../referencia/glossario.md#cenario-de-atributo-de-qualidade)
- [Requisito arquiteturalmente significativo](../referencia/glossario.md#requisito-arquiteturalmente-significativo)
- [Direcionador arquitetural](../referencia/glossario.md#direcionador-arquitetural)

## Conceito

Um requisito de atributo de qualidade, mesmo bem formulado, ainda deixa dúvida sobre em que situação exata ele vale e sobre como equipes diferentes devem interpretá-lo. O Software Engineering Institute usa cenários para reduzir essa ambiguidade. O relatório CMU/SEI-2003-TR-016 descreve o Quality Attribute Workshop, QAW, como método conduzido com os interessados para descobrir atributos de qualidade importantes e esclarecer requisitos antes mesmo de existir uma arquitetura detalhada. No QAW, os interessados geram, consolidam, priorizam e refinam cenários que representam os requisitos de qualidade do sistema. Esse trabalho também revela suposições e conflitos que permaneceriam ocultos em expressões genéricas como rápido, seguro ou flexível.

Um cenário de atributo de qualidade organiza essa expectativa em seis elementos.

| Elemento | Pergunta respondida |
| --- | --- |
| Fonte do estímulo | Quem ou o que provoca o evento |
| Estímulo | O que acontece |
| Ambiente | Sob quais condições |
| Artefato | Que parte do sistema é afetada |
| Resposta | O que o sistema deve fazer |
| Medida da resposta | Como se verificará o atendimento |

O exemplo abaixo aplica a estrutura a um requisito de desempenho, na mesma progressão de contexto e medida vista no bloco anterior.

| Elemento | Especificação |
| --- | --- |
| Fonte | Usuários autenticados do aplicativo móvel |
| Estímulo | Submissão de consulta de saldo |
| Ambiente | Pico mensal de 2.000 requisições por segundo |
| Artefato | API de contas e dependências necessárias |
| Resposta | Validar a identidade, recuperar o saldo e devolver a resposta |
| Medida | p95 até 500 ms, p99 até 1 s, erros abaixo de 0,1% |

O exemplo seguinte aplica a mesma estrutura a um requisito de modificabilidade, em um sistema de pagamentos com múltiplos adquirentes.

| Elemento | Especificação |
| --- | --- |
| Fonte | Equipe de produto |
| Estímulo | Solicitação de inclusão de novo adquirente |
| Ambiente | Sistema em evolução normal |
| Artefato | Componente de roteamento de pagamentos |
| Resposta | Implementar e ativar a nova integração sem alterar as integrações existentes |
| Medida | Até dez dias úteis, alterações limitadas ao adaptador, configuração e testes contratuais |

Um cenário bem escrito não é, por si, um requisito arquiteturalmente significativo. Depois de formulado, ele ainda precisa ser priorizado e avaliado quanto ao impacto sobre a arquitetura.

Nem todo requisito produz o mesmo efeito sobre a solução. Incluir um campo opcional em uma tela já existente costuma ser mudança local, contida em poucos componentes. Já a exigência de que um sistema de pagamentos permaneça disponível mesmo após a perda completa de uma região de nuvem pode alterar implantação, replicação de dados, comunicação entre serviços, tratamento de falha, monitoramento e custo operacional. A arquitetura passa a importar quando uma necessidade produz efeito amplo, envolve risco elevado ou exige escolha difícil de reverter.

Um requisito arquiteturalmente significativo, ASR, é um requisito cuja satisfação exerce influência importante sobre a arquitetura, podendo determinar estrutura, responsabilidade, interface, tecnologia, mecanismo, padrão de interação ou forma de implantação. Arquiteturalmente significativo não nomeia uma categoria temática nova de requisito. É um juízo sobre o impacto que aquele requisito produz sobre a arquitetura. Um requisito tende a ser um ASR quando sua satisfação apresenta ao menos uma das oito condições abaixo.

- força escolhas estruturais importantes
- afeta vários componentes ou equipes
- exige mecanismos arquiteturais específicos
- produz riscos técnicos relevantes
- envolve compromissos entre atributos de qualidade
- restringe tecnologias ou estilos arquiteturais
- tem alto custo de alteração tardia
- demanda experimentação, prototipação ou análise antecipada

Um direcionador arquitetural é um fator prioritário que orienta a formação ou a avaliação da arquitetura. Dependendo do método e do autor, o termo pode incluir ASRs, objetivos de negócio, restrições e preocupações críticas. No processo QAW, o SEI inclui entre os direcionadores requisitos de alto nível, preocupações de negócio ou de missão, objetivos e atributos de qualidade, e cabe aos interessados e facilitadores estabelecer consenso sobre quais são decisivos para aquele sistema. Requisito arquiteturalmente significativo e direcionador arquitetural, portanto, também não são intercambiáveis. Um objetivo de negócio como entrar em cinco países em doze meses não é, por si, um requisito de sistema já formulado, mas funciona como direcionador de requisitos de configurabilidade, localização, conformidade e escalabilidade que ainda precisam ser decompostos.

A relação entre atributo de qualidade e ASR não é de equivalência. Um atributo de qualidade é uma propriedade, como desempenho ou disponibilidade. Um requisito de atributo de qualidade estabelece o comportamento esperado em relação a essa propriedade. Um ASR é um requisito que influencia materialmente a arquitetura, e essa influência não decorre do rótulo do requisito, decorre do efeito que ele produz sobre decisões estruturais. Um requisito de atributo de qualidade pode ser arquiteturalmente significativo, mas não necessariamente será, como acontece com uma consulta administrativa de baixo volume que continua sendo requisito de desempenho válido sem provocar qualquer decisão arquitetural nova. Um ASR, por sua vez, não precisa ser um requisito de atributo de qualidade. No sistema de pagamentos com múltiplos adquirentes, o requisito de escolher dinamicamente entre cinco adquirentes, considerando custo, disponibilidade, risco e regra contratual, sem duplicar cobrança durante tentativa de contingência, tem núcleo funcional. Ainda assim ele pode exigir estratégia intercambiável entre adquirentes, normalização de contrato, idempotência, gerenciamento de estado, tratamento de falha parcial, auditoria e observabilidade distribuída, o que o torna um ASR funcional. Na expansão internacional, o objetivo de disponibilizar o produto em cinco países em doze meses ainda não especifica comportamento de software, mas pode gerar ASRs de localização, configurabilidade, extensibilidade e conformidade regulatória, sem que nenhum desses ASRs seja, sozinho, um requisito de qualidade nomeado como tal. Os dois conjuntos, requisito de atributo de qualidade e ASR, se cruzam sem coincidir. Existem requisitos de qualidade que são ASR e requisitos de qualidade que não são. Existem ASR funcionais e existem ASR que são restrição. Existe também requisito funcional comum sem nenhuma significância arquitetural relevante.

Diante de um requisito qualquer, um roteiro prático ajuda a decidir se ele deve pesar sobre a arquitetura.

1. Quais decisões mudariam? O requisito influencia decomposição, interfaces, comunicação, persistência, implantação ou tecnologias?
2. Qual é o alcance? Afeta um único componente ou atravessa vários elementos, serviços e equipes?
3. Qual é o risco? Há incerteza técnica, escala incomum, dependências frágeis ou consequências graves de falha?
4. Qual é o custo de adiamento? Uma decisão tardia provocaria reconstrução substancial?
5. Há compromisso entre qualidades? Melhorar segurança, consistência ou disponibilidade prejudica desempenho, usabilidade, custo ou modificabilidade?
6. É necessário validar hipóteses cedo? O requisito demanda protótipo, teste de carga, experimento ou prova de conceito?
7. Qual é a prioridade para os interessados? A exigência está ligada a objetivos de negócio ou de missão realmente prioritários?

Uma heurística resume o roteiro. Se uma alteração relevante no requisito obrigaria a reconsiderar decisões fundamentais, caras ou transversais da solução, há boa evidência de significância arquitetural. Essa heurística não substitui julgamento, porque significância depende de escala, riscos, arquitetura existente, competências disponíveis e custo de mudança, e pode variar entre sistemas e entre estágios do ciclo de vida do mesmo sistema.

Dois erros conceituais recorrentes merecem atenção neste ponto. O primeiro é tratar todo requisito não funcional como ASR. Nem todo requisito de qualidade altera a arquitetura, e alguns são satisfeitos por configuração local, implementação convencional ou capacidade já existente, como no exemplo da consulta administrativa citado acima. O segundo é tratar todo ASR como requisito não funcional. Funcionalidade, restrição regulatória, padrão corporativo e integração mandatória também podem condicionar a arquitetura, como mostra o próprio exemplo do roteamento entre adquirentes de pagamento, que é, no núcleo, um requisito funcional.

## Uso pelo arquiteto

O arquiteto usa o cenário e o roteiro de sete perguntas para decidir onde investir esforço de design, dentro de um conjunto de requisitos que nunca recebe atenção equivalente. Cenários bem formados tornam comparável o que antes era apenas uma lista de rótulos de atributo, e o roteiro filtra, entre os cenários escritos, quais realmente pesam sobre decisão estrutural, risco ou custo de mudança tardia. O resultado orienta a prioridade de análise antes de qualquer proposta de solução, evitando que o esforço de arquitetura se disperse sobre requisito que a implementação convencional já resolve.

## Exercício

A ACME é uma universidade privada brasileira cujo sistema acadêmico está em modernização, e cujo portal registra 815 sessões simultâneas em média anual ponderada, com pico de 5.800 sessões na abertura da matrícula, uma razão de 7,1 entre pico e média. Nessa mesma abertura, em 04/02/2026, o limite de tarefas concorrentes do monitor CICS foi atingido, porque sessões da camada web permaneciam com transação aberta após o abandono do navegador, sem tempo limite de sessão configurado. O incidente durou 4h20, 62% das tentativas de matrícula retornaram erro, 9.400 alunos não concluíram a inscrição no dia e a janela foi prorrogada em 2 dias úteis.

Escreva dois cenários de atributo de qualidade para a ACME, no formato de seis elementos apresentado no Conceito. O primeiro cenário deve ter como estímulo o pico de sazonalidade descrito acima. O segundo deve ter como estímulo o incidente descrito acima. Em seguida, para cada um dos dois cenários, aplique o roteiro de sete perguntas e defenda, com base nas respostas, se aquele cenário constitui um requisito arquiteturalmente significativo.

## Gabarito

<details>
<summary>Critério de avaliação</summary>

Como o exercício pede produção interpretativa sobre um caso real, não há resposta única. Um cenário bem formado preenche os seis elementos sem lacuna e sem redundância entre eles. Fonte e estímulo distinguem quem provoca o evento do que efetivamente acontece, o ambiente declara a condição de carga ou de falha em que o evento ocorre, articulando um dos números do extrato acima, o artefato nomeia a parte do sistema afetada com precisão suficiente para orientar decisão, e não apenas o sistema em geral, a resposta descreve o comportamento esperado, e a medida da resposta permite verificação objetiva, com prazo, percentual ou taxa de erro.

Para o cenário de pico, uma resposta forte usa a razão de 7,1 entre pico e média para justificar por que dimensionar a capacidade pelo pico tem custo diferente de dimensionar pela média, e usa a taxa de erro observada no intervalo, 6,3%, como parte da medida de resposta. Para o cenário de incidente, uma resposta forte identifica o mecanismo estrutural causador, a ausência de tempo limite de sessão, como o ponto que o cenário deve testar, e não apenas o sintoma de erro na matrícula.

Uma defesa de significância bem argumentada percorre as sete perguntas do roteiro sem pular nenhuma, mesmo quando a resposta a alguma delas é curta, e conclui com um juízo explícito, é ASR ou não é, apoiado nas respostas dadas e não apenas na suposição de que todo requisito de disponibilidade importa. Para os dois cenários da ACME, uma resposta forte tende a concluir que ambos são ASR, o de pico porque envolve alcance sobre vários componentes e alto custo de subdimensionamento tardio, o do incidente porque revela um risco técnico concreto, já materializado, com custo de correção que atravessa a camada web e o núcleo transacional. Uma resposta fraca aplica o roteiro de forma genérica, sem amarrar cada resposta a um dado do extrato, ou classifica os dois cenários como ASR apenas porque tratam de disponibilidade, incorrendo no primeiro erro conceitual apresentado no Conceito.

</details>

## Fontes

Glossário do curso, entradas [cenário de atributo de qualidade](../referencia/glossario.md#cenario-de-atributo-de-qualidade), [requisito arquiteturalmente significativo](../referencia/glossario.md#requisito-arquiteturalmente-significativo) e [direcionador arquitetural](../referencia/glossario.md#direcionador-arquitetural). ISO/IEC/IEEE 42010:2022. ISO/IEC 25010. CMU/SEI-2003-TR-016, Quality Attribute Workshops (QAWs), Third Edition, Barbacci e outros, Software Engineering Institute, Carnegie Mellon University. Dossiê da instituição fictícia [ACME](../caso-acme/index.md), dados operacionais de sazonalidade e incidentes.
