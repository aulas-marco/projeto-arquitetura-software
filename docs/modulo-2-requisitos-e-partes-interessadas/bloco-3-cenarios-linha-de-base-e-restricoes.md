# Cenários de qualidade, linha de base e restrições

Este bloco trata de como tornar um requisito de atributo de qualidade concreto o bastante para orientar decisão, como julgar se um requisito deve pesar sobre a arquitetura, e quais insumos já existentes entram no processo antes de qualquer desenho, os artefatos de linha de base e as restrições.

## Antes de começar

- [Cenário de atributo de qualidade](../referencia/glossario.md#cenario-de-atributo-de-qualidade)
- [Requisito arquiteturalmente significativo](../referencia/glossario.md#requisito-arquiteturalmente-significativo)
- [Direcionador arquitetural](../referencia/glossario.md#direcionador-arquitetural)
- [Artefato de linha de base](../referencia/glossario.md#artefato-de-linha-de-base)
- [Arquitetura de linha de base](../referencia/glossario.md#arquitetura-de-linha-de-base)

## Conceito

Um requisito de atributo de qualidade, mesmo bem formulado, ainda deixa dúvida sobre em que situação exata ele vale e sobre como equipes diferentes devem interpretá-lo. O Software Engineering Institute usa cenários para reduzir essa ambiguidade. O relatório CMU/SEI-2003-TR-016 descreve o Quality Attribute Workshop, QAW, como método conduzido com os interessados para descobrir atributos de qualidade importantes e esclarecer requisitos antes mesmo de existir uma arquitetura detalhada. No QAW, os interessados geram, consolidam, priorizam e refinam cenários que representam os requisitos de qualidade do sistema. Esse trabalho também revela suposições e conflitos que permaneceriam ocultos em expressões genéricas como rápido, seguro ou flexível.

Um **cenário de atributo de qualidade** organiza essa expectativa em seis elementos.

| Elemento | Pergunta respondida |
| --- | --- |
| Fonte do estímulo | Quem ou o que provoca o evento |
| Estímulo | O que acontece |
| Ambiente | Sob quais condições |
| Artefato | Que parte do sistema é afetada |
| Resposta | O que o sistema deve fazer |
| Medida da resposta | Como se verificará o atendimento |

![Diagrama horizontal com seis caixas conectadas por setas, numeradas de 1 a 6, sob o título Cenário de atributo de qualidade e o subtítulo estrutura para especificar requisitos não funcionais. Caixa 1, Fonte do estímulo, quem gera o evento. Caixa 2, Estímulo, evento que exige resposta. Caixa 3, Ambiente, condições no momento do evento. Caixa 4, Artefato, elemento que recebe o estímulo. Caixa 5, Resposta, ação executada pelo sistema. Caixa 6, Medida de resposta, critério mensurável para verificar o requisito.](../assets/images/bloco-3-cenario-atributo-qualidade.png)

*Figura 1 — A estrutura de seis elementos do cenário de atributo de qualidade. Fonte: material do curso.*

Um exemplo aplicado torna a estrutura concreta antes das três variações detalhadas a seguir.

![Diagrama do exemplo desempenho do catálogo, seis caixas conectadas por setas. Fonte do estímulo, 5.000 usuários simultâneos. Estímulo, realizam buscas no catálogo. Ambiente, operação normal. Artefato, serviço de catálogo. Resposta, consulta e retorna resultados. Medida de resposta, 95% das buscas em até 2 segundos. Uma barra de destaque abaixo afirma que o cenário transforma uma expectativa de qualidade em um requisito verificável.](../assets/images/bloco-3-exemplo-desempenho-catalogo.png)

*Figura 2 — Exemplo aplicado da estrutura de seis elementos a um requisito de desempenho de um serviço de catálogo. Fonte: material do curso.*

O exemplo abaixo aplica a mesma estrutura a um requisito de desempenho em outro domínio, na mesma progressão de contexto e medida vista no exemplo de desempenho da plataforma de vídeo, apresentado na seção Conceito do [bloco 2](bloco-2-qualidade-e-tipos-de-requisito.md).

| Elemento | Especificação |
| --- | --- |
| Fonte | Usuários autenticados do aplicativo de rastreamento de encomendas |
| Estímulo | Submissão de consulta de status de uma encomenda |
| Ambiente | Pico mensal de 2.000 requisições por segundo |
| Artefato | API de rastreamento e dependências necessárias |
| Resposta | Validar a identidade, recuperar o status da encomenda e devolver a resposta |
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

O terceiro exemplo aplica a mesma estrutura a um requisito de segurança, em um domínio ainda não usado nesta aula, o portal de sinistros de uma seguradora.

| Elemento | Especificação |
| --- | --- |
| Fonte | Agente que tenta acesso não autorizado a uma conta de segurado |
| Estímulo | Cinco tentativas de autenticação inválida para a mesma conta em dez minutos |
| Ambiente | Operação normal do portal de sinistros |
| Artefato | Serviço de identidade do portal de sinistros |
| Resposta | Bloquear novas tentativas, registrar o evento e notificar o segurado |
| Medida | Bloqueio por quinze minutos, registro em log de auditoria, notificação em até um minuto |

Um cenário bem escrito não é, por si, um requisito arquiteturalmente significativo. Depois de formulado, ele ainda precisa ser priorizado e avaliado quanto ao impacto sobre a arquitetura.

Nem todo requisito produz o mesmo efeito sobre a solução. Incluir um campo opcional em uma tela já existente costuma ser mudança local, contida em poucos componentes. Já a exigência de que um sistema de pagamentos permaneça disponível mesmo após a perda completa de uma região de nuvem pode alterar implantação, replicação de dados, comunicação entre serviços, tratamento de falha, monitoramento e custo operacional. A arquitetura passa a importar quando uma necessidade produz efeito amplo, envolve risco elevado ou exige escolha difícil de reverter.

Um **requisito arquiteturalmente significativo**, ASR, é um requisito cuja satisfação exerce influência importante sobre a arquitetura, podendo determinar estrutura, responsabilidade, interface, tecnologia, mecanismo, padrão de interação ou forma de implantação. Arquiteturalmente significativo não nomeia uma categoria temática nova de requisito. É um juízo sobre o impacto que aquele requisito produz sobre a arquitetura. Um requisito tende a ser um ASR quando sua satisfação apresenta ao menos uma das oito condições abaixo.

- força escolhas estruturais importantes
- afeta vários componentes ou equipes
- exige mecanismos arquiteturais específicos
- produz riscos técnicos relevantes
- envolve compromissos entre atributos de qualidade
- restringe tecnologias ou estilos arquiteturais
- tem alto custo de alteração tardia
- demanda experimentação, prototipação ou análise antecipada

Um **direcionador arquitetural** é um fator prioritário que orienta a formação ou a avaliação da arquitetura. Dependendo do método e do autor, o termo pode incluir ASRs, objetivos de negócio, restrições e preocupações críticas. No processo QAW, o SEI inclui entre os direcionadores requisitos de alto nível, preocupações de negócio ou de missão, objetivos e atributos de qualidade, e cabe aos interessados e facilitadores estabelecer consenso sobre quais são decisivos para aquele sistema. Requisito arquiteturalmente significativo e direcionador arquitetural, portanto, também não são intercambiáveis. Um objetivo de negócio como entrar em cinco países em doze meses não é, por si, um requisito de sistema já formulado, mas funciona como direcionador de requisitos de configurabilidade, localização, conformidade e escalabilidade que ainda precisam ser decompostos.

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

Dois erros conceituais recorrentes merecem atenção neste ponto. O primeiro é tratar todo requisito não funcional como ASR. Nem todo requisito de qualidade altera a arquitetura, e alguns são satisfeitos por configuração local, implementação convencional ou capacidade já existente, como no exemplo da consulta administrativa, citado no parágrafo sobre a relação entre atributo de qualidade e ASR, nesta mesma seção Conceito. O segundo é tratar todo ASR como requisito não funcional. Funcionalidade, restrição regulatória, padrão corporativo e integração mandatória também podem condicionar a arquitetura, como mostra o exemplo do roteamento entre adquirentes de pagamento, apresentado no mesmo parágrafo sobre a relação entre atributo de qualidade e ASR, que é, no núcleo, um requisito funcional.

### Artefatos de linha de base

Cenário e julgamento de significância não são os únicos insumos da fase de descoberta. Parte do que o arquiteto precisa já existe na organização, descrita como situação atual, e recebe o nome de artefato de linha de base. Usá-los evita refazer levantamento e, mais importante, evita que a solução seja desenhada sobre uma leitura inventada do sistema existente.

Os artefatos de linha de base mais frequentes são a descrição da arquitetura atual, com componentes e integrações, o catálogo de aplicações, os modelos de processo de negócio, os modelos de dados, os contratos vigentes com fornecedores e os registros de incidente e de capacidade. Cada um deles tem data, dono e grau de confiabilidade, e parte do trabalho de descoberta é justamente estabelecer quanto de cada artefato ainda descreve a realidade.

Na ACME, universidade privada brasileira fictícia com sistema acadêmico em operação desde 2004, os artefatos de linha de base disponíveis incluem o inventário de componentes com idade e responsável, o registro dos três incidentes graves dos últimos 18 meses, a medição de 34 dias úteis entre pedido aprovado e entrega em produção, o custo anual de propriedade de R$ 15,83 milhões e os contratos de sustentação e de capacidade, com prazos em 30/09/2027 e 31/12/2028.

### Restrições ao desenho

Restrição é decisão tomada fora do processo de projeto, que limita as alternativas do arquiteto sem ser negociável por ele. Ela difere do requisito em dois pontos. O requisito descreve o que a solução precisa entregar e admite discussão sobre a forma de atendê-lo, enquanto a restrição fecha alternativas antes da análise. Tratar restrição como requisito leva a comparar opções que a organização já descartou, e tratar requisito como restrição leva a aceitar como fechado o que ainda podia ser negociado.

As restrições chegam de origens distintas, e a origem determina quem pode revê-las. Restrição regulatória vem de fora e só muda com mudança normativa. Restrição contratual vem de acordo assinado e muda por negociação com o fornecedor, dentro dos prazos previstos. Restrição de política interna vem de decisão de governança e muda com nova decisão do mesmo nível. Restrição técnica vem do parque instalado e muda com investimento.

Sete restrições chegam fechadas ao caso da ACME, entre elas a impossibilidade de parar o sistema em período letivo, imposta pela Pró-Reitoria de Graduação, a permanência do ambiente virtual de aprendizagem e do ERP financeiro, decidida pela Reitoria em 12/03/2026, o uso de apenas dois provedores de nuvem pré-aprovados pelo Conselho Universitário, e o processamento de dado pessoal de aluno em território nacional, conforme parecer jurídico de 28/04/2026.

## Uso pelo arquiteto

O arquiteto usa o cenário e o roteiro de sete perguntas para decidir onde investir esforço de design, dentro de um conjunto de requisitos que nunca recebe atenção equivalente. Cenários bem formados tornam comparável o que antes era apenas uma lista de rótulos de atributo, e o roteiro filtra, entre os cenários escritos, quais realmente pesam sobre decisão estrutural, risco ou custo de mudança tardia. O resultado orienta a prioridade de análise antes de qualquer proposta de solução, evitando que o esforço de arquitetura se disperse sobre requisito que a implementação convencional já resolve.

## Exercício 7

A ACME é uma universidade privada brasileira cujo sistema acadêmico está em modernização, e cujo portal registra 815 sessões simultâneas em média anual ponderada, com pico de 5.800 sessões na abertura da matrícula, uma razão de 7,1 entre pico e média, e taxa de erro de 6,3% das requisições nesse intervalo de pico, contra 0,2% em dia letivo comum. Nessa mesma abertura, em 04/02/2026, o limite de tarefas concorrentes do monitor CICS foi atingido, porque sessões da camada web permaneciam com transação aberta após o abandono do navegador, sem tempo limite de sessão configurado. O incidente durou 4h20, 62% das tentativas de matrícula retornaram erro, 9.400 alunos não concluíram a inscrição no dia e a janela foi prorrogada em 2 dias úteis.

1. Escreva dois cenários de atributo de qualidade para a ACME, no formato de seis elementos apresentado no Conceito. O primeiro cenário deve ter como estímulo o pico de sazonalidade descrito acima, e pode partir, como orientação de continuidade e sem obrigatoriedade, da reescrita mensurável de R2 sobre disponibilidade na janela de matrícula, produzida no exercício do [bloco 2](bloco-2-qualidade-e-tipos-de-requisito.md) desta mesma aula. O segundo cenário deve ter como estímulo o incidente descrito acima.
2. Para cada um dos dois cenários, aplique o roteiro de sete perguntas apresentado no Conceito e defenda, com base nas respostas, se aquele cenário constitui um requisito arquiteturalmente significativo.
3. Liste quatro artefatos de linha de base da ACME que você usaria para sustentar os dois cenários, indicando para cada um o dado específico que ele fornece e o que aconteceria com o cenário se esse dado estivesse desatualizado.
4. Tome as sete restrições fechadas do caso e classifique cada uma pela origem, entre regulatória, contratual, de política interna e técnica, indicando quem teria autoridade para revê-la.

## Fontes

Glossário do curso, entradas [cenário de atributo de qualidade](../referencia/glossario.md#cenario-de-atributo-de-qualidade), [requisito arquiteturalmente significativo](../referencia/glossario.md#requisito-arquiteturalmente-significativo) e [direcionador arquitetural](../referencia/glossario.md#direcionador-arquitetural). International Organization for Standardization/International Electrotechnical Commission/Institute of Electrical and Electronics Engineers (2022), listada na [bibliografia](../referencia/bibliografia.md). International Organization for Standardization (2023), listada na [bibliografia](../referencia/bibliografia.md). Barbacci et al. (2003), listado na [bibliografia](../referencia/bibliografia.md). Lovatt (2021), seções 4.7 e 4.8, listado na [bibliografia](../referencia/bibliografia.md). Dossiê da instituição fictícia [ACME](../caso-acme/index.md), dados operacionais de sazonalidade e incidentes, restrições fechadas e [arquitetura de linha de base](../caso-acme/linha-de-base.md).
