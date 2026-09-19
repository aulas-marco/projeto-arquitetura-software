# Texto de referência do professor — Atributos de qualidade e requisitos arquiteturalmente significativos

> Fornecido pelo Marco em 19/09/2026, com apoio do ChatGPT. Fonte primária para os blocos 2 e 3 da Aula 1, e modelo de tom para todo o material do curso. Preservar o conteúdo factual e a sequência de seções ao adaptar. Não preservar a pontuação: o curso usa zero ponto-e-vírgula e no máximo um travessão por parágrafo, e este texto-fonte usa os dois livremente.

## 1. O que significa qualidade em um sistema de software

Antes de discutir arquitetura, é necessário compreender o que se quer dizer com qualidade. Em linguagem cotidiana, qualidade costuma significar que alguma coisa é "boa". Em engenharia de software, essa formulação é insuficiente, pois sistemas diferentes precisam ser bons de maneiras diferentes.

Um aplicativo bancário, por exemplo, precisa proteger dados e transações. Uma plataforma de transmissão de vídeo precisa atender muitos usuários sem interrupção perceptível. Um sistema utilizado por décadas precisa permitir mudanças sem que cada alteração comprometa todo o produto. Segurança, desempenho, disponibilidade e facilidade de modificação são aspectos diferentes da qualidade.

Por isso, a qualidade de um sistema não deve ser tratada como uma propriedade única. Ela é observada por meio de diversas características. A ISO/IEC 25010:2023 apresenta um modelo de qualidade composto por características, subdivididas em subcaracterísticas. Esse modelo serve como referência para especificar, medir e avaliar propriedades de qualidade de produtos de TIC e software.

### 1.1 Atributo de qualidade

Um atributo de qualidade é uma propriedade ou dimensão pela qual o comportamento ou a estrutura de um sistema pode ser observado e avaliado. Alguns exemplos são:

- desempenho: com que rapidez e capacidade o sistema realiza seu trabalho
- disponibilidade: por quanto tempo e em quais condições o serviço permanece acessível
- confiabilidade: com que consistência o sistema executa corretamente suas funções
- segurança: como o sistema protege informações, operações e recursos
- usabilidade: com que eficácia e facilidade as pessoas conseguem utilizar o produto
- modificabilidade: com que esforço o sistema pode ser alterado
- interoperabilidade: como o sistema troca informações e coopera com outros sistemas
- segurança operacional (safety): como o sistema evita consequências inaceitáveis para pessoas, patrimônio ou ambiente

Esses termos nomeiam aspectos da qualidade, mas ainda não dizem quanto de cada qualidade é necessário. "Desempenho" é um atributo. "Segurança" também é um atributo. Nenhum dos dois, isoladamente, constitui um requisito completo.

A distinção é importante porque duas organizações podem considerar o mesmo atributo relevante e, ainda assim, necessitar de comportamentos muito diferentes. Uma indisponibilidade de cinco minutos pode ser aceitável em um portal institucional e inaceitável em um sistema de controle hospitalar.

## 2. Do atributo ao requisito

Um requisito expressa uma necessidade, capacidade, condição ou restrição que o sistema deve satisfazer. Ele transforma expectativas gerais em algo que possa ser analisado, negociado, implementado e verificado.

Por exemplo, "o sistema deve permitir consultar o saldo" descreve uma capacidade funcional. Já "o sistema deve utilizar o provedor corporativo de identidade" estabelece uma restrição. Requisitos podem, portanto, tratar do que o sistema faz, das condições sob as quais opera ou dos limites que devem ser respeitados.

### 2.1 Onde se posiciona o requisito não funcional

Muitos alunos aprendem inicialmente a dividir os requisitos em dois grupos: requisitos funcionais, que descrevem serviços, comportamentos ou capacidades que o sistema deve oferecer, e requisitos não funcionais, que descrevem qualidades, condições, limites ou restrições associados ao funcionamento do sistema.

Essa divisão é útil como introdução. Nesse vocabulário, requisitos de desempenho, disponibilidade, segurança, usabilidade e modificabilidade normalmente são classificados como requisitos não funcionais.

Exemplos de classificação inicial:

| Requisito | Classificação inicial |
| --- | --- |
| O cliente deve conseguir consultar seu saldo | Requisito funcional, descreve uma capacidade |
| 95% das consultas de saldo devem responder em até 500 ms | Requisito não funcional de desempenho |
| O serviço deve permanecer disponível durante pelo menos 99,95% de cada mês | Requisito não funcional de disponibilidade |

Entretanto, a expressão "não funcional" é muito ampla. Ela informa principalmente que o requisito não descreve uma função de negócio, mas não esclarece qual propriedade de qualidade está sendo tratada, em que situação ela deve ser observada ou como será medida. Por isso, na análise de arquitetura, é mais útil identificar explicitamente o atributo envolvido e formular um requisito de atributo de qualidade verificável.

Também é comum colocar restrições dentro do conjunto dos requisitos não funcionais. "O sistema deve utilizar PostgreSQL", por exemplo, não descreve uma função nem necessariamente uma qualidade desejada, estabelece uma escolha tecnológica obrigatória. Dependendo da taxonomia adotada, requisitos não funcionais podem reunir tanto requisitos de qualidade quanto restrições. Por essa razão, requisito não funcional e requisito de atributo de qualidade não devem ser tratados como termos equivalentes.

Posicionamento dos conceitos:

| Conceito | Papel |
| --- | --- |
| Requisito funcional | Especifica uma capacidade ou comportamento oferecido pelo sistema |
| Requisito não funcional | Categoria ampla tradicional para qualidades, condições e, em algumas classificações, restrições |
| Requisito de atributo de qualidade | Especifica de modo contextualizado e verificável uma expectativa sobre uma qualidade |
| Restrição | Limita as alternativas possíveis, como tecnologia, plataforma, norma ou localização |

A ISO/IEC 25010:2023 contribui para tornar essa discussão mais precisa ao organizar propriedades de qualidade em características e subcaracterísticas que podem apoiar a especificação e a avaliação de requisitos. Em vez de manter uma lista genérica de "não funcionais", a equipe pode indicar qual característica está em jogo e qual comportamento mensurável é esperado.

### 2.2 Requisito de atributo de qualidade

Um requisito de atributo de qualidade declara o comportamento esperado do sistema em relação a uma característica de qualidade. Ele responde a uma pergunta mais concreta: que nível de desempenho, disponibilidade, segurança ou modificabilidade é necessário, em determinada situação?

Considere três formulações sucessivas sobre desempenho:

| Formulação | O que ela informa |
| --- | --- |
| "O sistema deve ser rápido" | Apenas uma intenção geral. Não há critério de verificação |
| "As consultas devem responder em até 500 ms" | Há uma medida, mas não se sabe para qual carga ou parcela das consultas |
| "Durante o pico mensal de 2.000 requisições por segundo, 95% das consultas autenticadas devem responder em até 500 ms e 99% em até 1 segundo" | Há contexto, carga e medidas que podem orientar análise e testes |

As três frases tratam de desempenho. Entretanto, somente a terceira fornece informação suficiente para orientar decisões com razoável precisão. O nome do atributo indica o que importa, o requisito descreve o que se espera que aconteça.

O mesmo raciocínio vale para segurança. Dizer que "o sistema deve ser seguro" não informa quais ativos devem ser protegidos, contra quais ameaças, em qual ambiente e com que resposta. Uma formulação mais útil seria:

Quando cinco tentativas inválidas de autenticação forem realizadas para a mesma conta em até dez minutos, o serviço de identidade deverá bloquear novas tentativas por quinze minutos, registrar o evento e notificar o usuário em até um minuto.

Agora existe um evento observável, uma parte afetada do sistema, uma resposta esperada e medidas de tempo.

### 2.3 Cenários de atributos de qualidade

O Software Engineering Institute utiliza cenários para tornar expectativas de qualidade mais concretas. O relatório público Quality Attribute Workshops (QAWs), Third Edition descreve o QAW como um método conduzido com os interessados para descobrir atributos de qualidade importantes e esclarecer requisitos antes mesmo de existir uma arquitetura detalhada.

Em vez de discutir somente palavras amplas como "rápido", "seguro" ou "flexível", um cenário procura esclarecer:

- quem ou o que produz o evento
- qual evento ocorre
- em quais condições ele acontece
- qual parte do sistema é afetada
- como o sistema deve responder
- como essa resposta será medida

O acervo público do QAW mantido pelo SEI explica que os interessados geram, consolidam, priorizam e refinam cenários representativos dos requisitos de atributos de qualidade. Esse trabalho também ajuda a revelar suposições e conflitos que permaneceriam ocultos em expressões genéricas.

## 3. Quando um requisito passa a ser uma questão de arquitetura

Nem todo requisito tem o mesmo efeito sobre a solução. Alguns podem ser implementados localmente, sem modificar a organização geral do sistema. Outros obrigam a rever componentes, distribuição de responsabilidades, mecanismos de comunicação, persistência, infraestrutura ou tecnologias.

Considere a inclusão de um novo campo opcional em uma tela já existente. Em muitos sistemas, essa mudança pode ser realizada em poucos componentes e não afeta decisões fundamentais. Agora considere a exigência de que o sistema permaneça disponível mesmo após a perda completa de uma região da nuvem. Essa exigência pode influenciar implantação, replicação de dados, comunicação entre serviços, tratamento de falhas, monitoramento e custos operacionais.

A arquitetura torna-se especialmente relevante quando uma necessidade tem efeitos amplos, envolve risco elevado ou exige escolhas difíceis de reverter.

### 3.1 Requisito arquiteturalmente significativo, ASR

Um requisito arquiteturalmente significativo, frequentemente abreviado como ASR, é um requisito cuja satisfação exerce influência importante sobre a arquitetura. Ele pode determinar estruturas, responsabilidades, interfaces, tecnologias, mecanismos, padrões de interação ou formas de implantação.

"Arquiteturalmente significativo" não designa uma nova categoria temática de requisito. É um juízo sobre o impacto que o requisito exerce sobre a arquitetura.

Um requisito tende a ser um ASR quando sua satisfação:

- força escolhas estruturais importantes
- afeta vários componentes ou equipes
- exige mecanismos arquiteturais específicos
- produz riscos técnicos relevantes
- envolve compromissos entre atributos de qualidade
- restringe tecnologias ou estilos arquiteturais
- tem alto custo de alteração tardia
- demanda experimentação, prototipação ou análise antecipada

O material público do SEI sobre Quality Attribute Workshops afirma que os direcionadores arquiteturais frequentemente incluem requisitos de alto nível, preocupações de negócio ou missão, objetivos e vários atributos de qualidade. Essa enumeração mostra que atributos de qualidade participam do conjunto de direcionadores, mas não esgotam esse conjunto.

### 3.2 Direcionador arquitetural

Um direcionador arquitetural (architectural driver) é um fator prioritário que orienta a formação ou avaliação da arquitetura. Dependendo do método e do autor, o termo pode incluir ASRs, objetivos de negócio, restrições e preocupações críticas. No processo QAW, o SEI inclui entre os direcionadores requisitos de alto nível, preocupações de negócio ou missão, objetivos e atributos de qualidade, e os interessados e facilitadores estabelecem consenso sobre quais são decisivos para o sistema.

Assim, requisito arquiteturalmente significativo e direcionador arquitetural também não são intercambiáveis. Um objetivo como "entrar em cinco países em doze meses" não é necessariamente um requisito de sistema já formulado, mas pode funcionar como direcionador de requisitos de configurabilidade, localização, conformidade e escalabilidade.

### 3.3 A relação entre atributo de qualidade e ASR

Um atributo de qualidade é uma propriedade, como desempenho ou disponibilidade. Um requisito de atributo de qualidade estabelece o comportamento esperado em relação a essa propriedade. Um ASR é um requisito que influencia materialmente a arquitetura.

Um requisito de atributo de qualidade pode ser arquiteturalmente significativo, mas não necessariamente será. Um ASR, por sua vez, não precisa ser um requisito de atributo de qualidade.

Muitos ASRs são requisitos de qualidade, tradicionalmente chamados de requisitos não funcionais, porque desempenho, disponibilidade, segurança e modificabilidade frequentemente exigem mecanismos presentes em várias partes do sistema. Entretanto, requisitos funcionais, restrições tecnológicas, obrigações regulatórias e objetivos de negócio também podem produzir efeitos arquiteturais relevantes. Portanto, "não funcional" e "arquiteturalmente significativo" são classificações diferentes: a primeira descreve a natureza do requisito, a segunda descreve seu impacto sobre a arquitetura.

## 4. O papel da ISO/IEC/IEEE 42010

A ISO/IEC/IEEE 42010:2022 especifica requisitos para a estrutura e a expressão de uma descrição de arquitetura. Ela distingue explicitamente a arquitetura da entidade da descrição de arquitetura que expressa essa arquitetura. Também declara que não especifica requisitos para a entidade de interesse ou para seu ambiente e não prescreve métodos, técnicas ou ferramentas de arquiteturação.

Essa delimitação é decisiva: a norma oferece uma estrutura para organizar e comunicar arquitetura, mas não estabelece que atributo de qualidade e ASR sejam sinônimos. A descrição arquitetural deve permitir tratar as preocupações relevantes dos interessados por meio de pontos de vista, visões, modelos e decisões apropriados. Um atributo de qualidade pode constituir uma preocupação central, sua significância arquitetural, entretanto, depende do contexto, da prioridade, dos cenários e das decisões que ele provoca.

No enquadramento da ISO/IEC/IEEE 42010, os interesses dos interessados devem ser tratados na descrição arquitetural. Nas práticas do SEI, requisitos de atributos de qualidade suficientemente importantes e influentes podem ser identificados como direcionadores ou requisitos arquiteturalmente significativos.

A ISO/IEC/IEEE 42010:2022 é a segunda edição publicada e substitui a edição de 2011.

## 5. Relação entre os conjuntos

Os conceitos podem ser vistos como conjuntos parcialmente sobrepostos, não coincidentes:

- existem requisitos de atributos de qualidade que são ASRs
- existem requisitos de atributos de qualidade que não são ASRs
- existem ASRs que são funcionais
- existem ASRs que são restrições
- existem requisitos funcionais comuns que não possuem significância arquitetural relevante

A significância arquitetural também não é uma propriedade absoluta e permanente do texto do requisito. O mesmo requisito pode ser significativo em um sistema e trivial em outro, porque a significância depende de escala, riscos, arquitetura existente, competências disponíveis, restrições e custo de mudança.

## 6. Exemplos analisados

### 6.1 Requisito de qualidade que é um ASR

"Após a indisponibilidade completa de uma região da nuvem, o serviço de pagamentos deve restaurar operações em outra região em até cinco minutos, com perda máxima de trinta segundos de transações confirmadas."

Esse requisito trata de disponibilidade e recuperabilidade. Ele provavelmente é um ASR porque pode exigir implantação multirregional, replicação de dados, mecanismos de consenso ou reconciliação, roteamento de tráfego, automação de recuperação, observabilidade e testes de recuperação. Também introduz uma possível tensão entre consistência, disponibilidade, complexidade operacional e custo.

### 6.2 Requisito de qualidade que pode não ser um ASR

"A página administrativa de consulta de feriados deve responder em até quatro segundos para até dez usuários simultâneos."

Esse é um requisito de desempenho. Contudo, em um sistema já capaz de suportar milhares de usuários e com o conjunto de feriados armazenado localmente, sua satisfação pode não demandar qualquer decisão arquitetural nova. O requisito continua sendo válido e testável, mas não necessariamente é arquiteturalmente significativo.

Se o contexto mudar, por exemplo se a consulta passar a agregar dados em tempo real de cinquenta serviços externos, o mesmo objetivo de resposta poderá adquirir significância arquitetural. A categoria do atributo não determina sozinha a significância.

### 6.3 Requisito funcional que é um ASR

"Para cada pagamento, o sistema deve escolher dinamicamente uma entre cinco adquirentes, considerando custo, disponibilidade, risco e regras contratuais, sem duplicar cobranças durante tentativas de contingência."

O núcleo do requisito é funcional: selecionar e executar uma rota de pagamento. Entretanto, ele pode exigir estratégias intercambiáveis, normalização de contratos, idempotência, gerenciamento de estado, tratamento de falhas parciais, auditoria e observabilidade distribuída. A funcionalidade, portanto, condiciona a arquitetura.

### 6.4 Restrição que é um ASR

"Dados pessoais de clientes brasileiros devem permanecer em infraestrutura localizada no Brasil e ser criptografados em repouso por serviço de chaves controlado pela organização."

Essa formulação combina restrição de localização e mecanismo de segurança. Pode condicionar provedor, regiões disponíveis, desenho de dados, replicação, recuperação de desastre e integração com o serviço de chaves.

### 6.5 Objetivo de negócio convertido em requisitos arquiteturais

"A empresa pretende disponibilizar o produto em cinco países nos próximos doze meses."

O objetivo, sozinho, ainda não especifica comportamento de software. Ele precisa ser decomposto em perguntas sobre idiomas distintos, moedas, regras fiscais, residência de dados, métodos de pagamento locais, calendários e níveis de disponibilidade. Do objetivo podem emergir ASRs de localização, configurabilidade, extensibilidade, conformidade e isolamento regional.

## 7. Cenários de atributos de qualidade, estrutura de seis elementos

Uma estrutura amplamente utilizada para cenário de qualidade contém:

| Elemento | Pergunta respondida |
| --- | --- |
| Fonte do estímulo | Quem ou o que provoca o evento |
| Estímulo | O que acontece |
| Ambiente | Sob quais condições |
| Artefato | Que parte do sistema é afetada |
| Resposta | O que o sistema deve fazer |
| Medida da resposta | Como se verificará o atendimento |

Exemplo de desempenho:

| Elemento | Especificação |
| --- | --- |
| Fonte | Usuários autenticados do aplicativo móvel |
| Estímulo | Submissão de consulta de saldo |
| Ambiente | Pico mensal de 2.000 requisições por segundo |
| Artefato | API de contas e dependências necessárias |
| Resposta | Validar a identidade, recuperar o saldo e devolver a resposta |
| Medida | p95 até 500 ms, p99 até 1 s, erros abaixo de 0,1% |

Exemplo de modificabilidade:

| Elemento | Especificação |
| --- | --- |
| Fonte | Equipe de produto |
| Estímulo | Solicitação de inclusão de novo adquirente |
| Ambiente | Sistema em evolução normal |
| Artefato | Componente de roteamento de pagamentos |
| Resposta | Implementar e ativar a nova integração sem alterar as integrações existentes |
| Medida | Até dez dias úteis, alterações limitadas ao adaptador, configuração e testes contratuais |

Esses cenários não são automaticamente ASRs apenas por estarem bem escritos. Depois de formulados, precisam ser priorizados e avaliados quanto ao impacto arquitetural.

## 8. Como decidir se um requisito é arquiteturalmente significativo

Um roteiro prático é perguntar:

1. Quais decisões mudariam? O requisito influencia decomposição, interfaces, comunicação, persistência, implantação ou tecnologias?
2. Qual é o alcance? Afeta um único componente ou atravessa vários elementos, serviços e equipes?
3. Qual é o risco? Há incerteza técnica, escala incomum, dependências frágeis ou consequências graves de falha?
4. Qual é o custo de adiamento? Uma decisão tardia provocaria reconstrução substancial?
5. Há compromisso entre qualidades? Melhorar segurança, consistência ou disponibilidade prejudica desempenho, usabilidade, custo ou modificabilidade?
6. É necessário validar hipóteses cedo? O requisito demanda protótipo, teste de carga, experimento ou prova de conceito?
7. Qual é a prioridade para os interessados? A exigência está ligada a objetivos de negócio ou missão realmente prioritários?

Uma heurística prática: se uma alteração relevante no requisito obrigaria a reconsiderar decisões fundamentais, caras ou transversais da solução, há boa evidência de significância arquitetural. Essa heurística não deve ser confundida com definição formal universal, porque significância envolve julgamento relativo ao sistema e ao estágio do ciclo de vida.

## 9. Erros conceituais frequentes

**Tratar todo requisito não funcional como ASR.** Nem todo requisito de qualidade altera a arquitetura. Alguns são satisfeitos por configuração local, implementação convencional ou capacidade já existente.

**Tratar todo ASR como requisito não funcional.** Funcionalidades, restrições regulatórias, padrões corporativos e integrações mandatórias também podem condicionar a arquitetura.

**Confundir nome do atributo com requisito.** "Disponibilidade", "segurança" e "escalabilidade" são rótulos insuficientes. A ISO/IEC 25010:2023 fornece um modelo de referência de características, que apoia a especificação e a avaliação, mas não substitui a definição contextual e mensurável do requisito.

**Atribuir à ISO 42010 uma taxonomia que ela não prescreve.** A ISO/IEC/IEEE 42010:2022 disciplina descrições de arquitetura. Ela não especifica requisitos para a entidade de interesse e não prescreve métodos de arquiteturação. Não deve ser apresentada como fonte de uma identidade conceitual entre atributo de qualidade e ASR.

**Escrever requisitos sem contexto e medida.** Expressões como "altamente disponível", "seguro", "escalável" e "fácil de manter" ocultam decisões e impedem validação.

## 10. Síntese conclusiva

Os conceitos em sequência lógica:

- **Atributo de qualidade**: dimensão ou propriedade segundo a qual o sistema é avaliado
- **Requisito não funcional**: categoria tradicional e ampla que costuma reunir requisitos de qualidade e, em algumas taxonomias, restrições
- **Requisito de atributo de qualidade**: expectativa concreta e mensurável sobre uma propriedade de qualidade
- **ASR**: requisito, de qualidade, funcional ou restritivo, que influencia materialmente a arquitetura
- **Direcionador arquitetural**: fator prioritário que orienta decisões de arquitetura, pode incluir ASRs, objetivos de negócio, restrições e preocupações críticas

Atributo de qualidade não é sinônimo de requisito arquiteturalmente significativo. Um atributo é uma propriedade, um requisito de qualidade especifica uma expectativa sobre essa propriedade, e um ASR é um requisito cuja satisfação influencia materialmente a arquitetura.

## Referências verificadas para uso na bibliografia do curso

- ISO/IEC/IEEE 42010:2022, segunda edição, substitui a edição de 2011, sobre descrição de arquitetura
- ISO/IEC 25010, modelo de qualidade de produto de software
- CMU/SEI-2003-TR-016, Quality Attribute Workshops (QAWs), Third Edition, Barbacci e outros, Software Engineering Institute, Carnegie Mellon University

## Itens NÃO verificados, não usar sem confirmação

- O número exato de características da ISO/IEC 25010:2023
- O DOI atribuído ao relatório CMU/SEI-2003-TR-016
- A existência de um item bibliográfico próprio chamado "Quality Attribute Workshop Collection", SEI, 2016
