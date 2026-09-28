# Módulo 3, princípios de design, padrões e decisões

**Data:** 28/09/2026

**Estado:** aprovado para planejamento

**Escopo:** revisão e conclusão integral da Aula 3

## 1. Objetivo

O módulo conduz o aluno das entradas levantadas na Aula 2 até uma decisão de desenho justificável. A progressão adotada é uma cadeia de decisão: princípios de design orientam a escolha do estilo, o estilo delimita os problemas internos para os quais padrões são selecionados, e o conjunto das escolhas é registrado em ADR.

Ao final da aula, o aluno deverá conseguir:

- converter requisitos, atributos de qualidade e restrições em princípios de design
- distinguir desenho conceitual de desenho lógico
- comparar estilos arquiteturais por forças, riscos e compromissos
- distinguir estilo arquitetural, padrão arquitetural e padrão de design
- selecionar padrões em função de um problema e de um contexto
- registrar contexto, alternativas, decisão, consequências, evidências e revisão em ADR

## 2. Decisões de escopo

O escopo vigente do módulo é o definido no cronograma atual: princípios de design, estilos arquiteturais, padrões de design e registro de decisão arquitetural. A especificação histórica que associava a Aula 3 a descoberta e riscos está obsoleta e não orienta esta revisão.

Os quatro blocos serão tratados como uma unidade. Os blocos 1 e 3 serão criados. Os blocos 2 e 4 serão revisados e harmonizados, preservando o conteúdo tecnicamente válido já publicado. O índice será ampliado e uma página de síntese será criada.

Não fazem parte deste módulo:

- escolha de frameworks ou plataforma tecnológica, tratada na Aula 5
- detalhamento de protocolos, dados, infraestrutura ou implantação, tratado nas Aulas 4 e 5
- modelagem C4 completa, tratada na Aula 4
- análise de lacunas, roteiro de entrega e governança, tratados na Aula 6
- catálogo amplo de padrões GoF sem vínculo com decisões arquiteturais

## 3. Progressão pedagógica

Cada bloco consome o produto do anterior e produz uma entrada para o seguinte.

| Bloco | Pergunta orientadora | Produto do exercício |
| --- | --- | --- |
| 1. Princípios de design | Que regras devem orientar o desenho da solução? | Princípios priorizados e esboço lógico |
| 2. Estilos arquiteturais | Que organização estrutural sustenta melhor esses princípios e os cenários de qualidade? | Matriz comparativa e estilo recomendado |
| 3. Padrões | Que soluções recorrentes tratam problemas específicos dentro do estilo escolhido? | Mapa problema, padrão e consequência |
| 4. ADR | Como tornar a decisão compreensível, rastreável e revisável? | ADR completo |

Os exercícios continuam numerados de 9 a 12. Cada página reproduz todo dado necessário do caso ACME ou aponta com precisão para o produto que o próprio aluno construiu no bloco anterior. Nenhum exercício depende de localizar informação vaga em outra página.

## 4. Bloco 1, princípios de design e passagem ao lógico

### 4.1 Resultado de aprendizagem

O aluno transforma entradas arquiteturais em regras orientadoras e usa essas regras para produzir um primeiro desenho lógico, sem antecipar escolhas de produto ou tecnologia.

### 4.2 Conteúdo

O bloco distingue cinco conceitos:

| Conceito | Papel |
| --- | --- |
| Objetivo | Resultado de negócio pretendido |
| Requisito | Necessidade, capacidade, condição ou restrição verificável |
| Princípio | Regra durável que orienta um conjunto de decisões |
| Decisão | Escolha situada entre alternativas |
| Elemento lógico | Responsabilidade ou colaboração sem compromisso prematuro com tecnologia |

O repertório de princípios incluirá simplicidade, separação de responsabilidades, baixo acoplamento, alta coesão, encapsulamento, desenho para falha, observabilidade, segurança por desenho e evolução incremental. O texto deixará claro que uma lista genérica não constitui arquitetura. Cada princípio precisa de motivação, implicação prática e forma de verificar sua aplicação.

A passagem do conceitual ao lógico será apresentada como transformação progressiva:

1. identificar capacidades e responsabilidades
2. agrupar responsabilidades coesas
3. declarar interfaces e fluxos
4. aplicar restrições e princípios
5. localizar riscos e decisões pendentes

O exemplo aplicado usará a ACME para mostrar como continuidade operacional, residência de dados, redução de dependência do legado e propagação de notas orientam responsabilidades lógicas sem escolher linguagem, nuvem ou framework.

### 4.3 Exercício 9

O aluno derivará de quatro entradas da ACME um conjunto pequeno de princípios. Para cada princípio, registrará nome, motivação, implicação no desenho e evidência esperada. Em seguida, produzirá um esboço lógico que distribua responsabilidades sem nomear produtos tecnológicos.

## 5. Bloco 2, estilos arquiteturais

### 5.1 Resultado de aprendizagem

O aluno compara organizações estruturais por sua capacidade de sustentar princípios e cenários de qualidade, reconhecendo que todo estilo introduz compromissos.

### 5.2 Harmonização do conteúdo existente

O repertório atual de sete estilos será preservado:

- arquitetura em camadas
- microsserviços
- arquitetura orientada a eventos
- microkernel
- arquitetura hexagonal
- pipes and filters
- arquitetura orientada a APIs

A exposição será padronizada para cada estilo:

1. forma estrutural
2. componentes e comunicação
3. atributos favorecidos
4. atributos prejudicados
5. quando usar
6. quando evitar
7. anti-padrão e heurística de alerta

Repetições serão reduzidas sem remover o rigor. A Lei de Conway permanecerá apenas onde explicar uma consequência organizacional concreta. A tabela comparativa ganhará ligação explícita com os princípios do bloco 1.

### 5.3 Exercício 10

O exercício atual será mantido como base. O aluno comparará três estilos contra os cenários de matrícula e contra os princípios produzidos no exercício 9. A resposta deverá separar adequação, risco introduzido e mecanismo compensatório necessário.

## 6. Bloco 3, padrões arquiteturais e padrões de design

### 6.1 Resultado de aprendizagem

O aluno reconhece o nível de decisão de cada padrão e seleciona uma solução recorrente porque ela responde a um problema explícito, não por popularidade ou familiaridade.

### 6.2 Taxonomia adotada

O módulo usará três níveis:

| Nível | Pergunta | Exemplos |
| --- | --- | --- |
| Estilo arquitetural | Como o sistema inteiro se organiza? | Camadas, eventos, microsserviços |
| Padrão arquitetural | Como uma preocupação transversal ou de integração é resolvida? | API Gateway, Strangler Fig, Anti-Corruption Layer, Saga |
| Padrão de design | Como responsabilidades colaboram dentro de uma parte do sistema? | Adapter, Strategy, Observer |

Strangler Fig será tratado como padrão de modernização, não como estilo. DDD poderá aparecer como abordagem de modelagem e delimitação, não como padrão isolado nem como estilo arquitetural.

### 6.3 Repertório principal

O repertório será limitado aos padrões que ajudam a discutir a ACME e os atributos já levantados:

- Strangler Fig
- Anti-Corruption Layer
- Adapter
- API Gateway
- Timeout
- Retry com limite
- Circuit Breaker
- Bulkhead
- Transactional Outbox
- Saga

Cada padrão terá problema, contexto, forças, estrutura mínima, consequência favorável, custo e sinal de uso inadequado. Combinações serão apresentadas apenas quando resolverem problemas distintos. O texto advertirá contra complexidade acidental e contra a adoção de padrões sem evidência de necessidade.

### 6.4 Exercício 11

Partindo do estilo recomendado no exercício 10, o aluno selecionará padrões para três problemas da modernização da ACME: coexistência entre legado e solução nova, proteção contra falha de integração e publicação confiável de mudança acadêmica. Para cada escolha, registrará problema, padrão, elemento afetado, consequência favorável e custo aceito.

## 7. Bloco 4, registro de decisão arquitetural

### 7.1 Resultado de aprendizagem

O aluno registra uma decisão de forma suficiente para que outra pessoa compreenda o contexto, as alternativas, o racional, as consequências, as evidências e as condições de revisão.

### 7.2 Harmonização do conteúdo existente

O bloco preservará:

- distinção entre decisão e racional
- abordagem leve de registro
- formatos Nygard, MADR e template completo do curso
- exemplo completo
- práticas de estado, imutabilidade histórica e substituição

A revisão reduzirá sobreposição, alinhará os termos aos blocos anteriores e deixará explícito que o ADR registra uma decisão, não substitui o desenho nem o plano de implementação.

O template completo continuará com título, estado, data, contexto, forças, alternativas, decisão, consequências, evidências e revisão. Cada campo terá critério de qualidade e erro frequente.

### 7.3 Exercício 12

O exercício atual será ampliado para consumir os produtos dos três blocos anteriores. O ADR registrará o estilo escolhido e os padrões que materializam a estratégia de modernização. As alternativas deverão ser comparadas pelas forças derivadas dos princípios, e o gatilho de revisão deverá ser observável.

## 8. Índice e síntese

O índice do módulo terá:

- objetivos de aprendizagem em verbos observáveis
- grade de tempo com quatro blocos
- roteiro causal da aula
- indicação da entrada recebida da Aula 2
- preparação para a Aula 4

A síntese terá:

- checklist dos conceitos essenciais
- cadeia objetivo, requisito, princípio, estilo, padrão e decisão
- autoavaliação
- fontes da aula

## 9. Estratégia visual

Cada bloco terá ao menos um infográfico principal no padrão visual dos módulos 1 e 2. Os visuais não poderão resolver diretamente os exercícios.

| Bloco | Visual principal |
| --- | --- |
| 1 | Cadeia das entradas arquiteturais até o desenho lógico |
| 2 | Matriz de estilos por força e compromisso |
| 3 | Mapa de níveis, estilo, padrão arquitetural e padrão de design |
| 4 | Ciclo de vida de uma decisão e anatomia do ADR |

Diagramas estruturais simples serão produzidos como SVG ou PlantUML quando precisão e editabilidade forem mais importantes que ilustração. Infográficos editoriais poderão ser PNG quando a composição exigir maior densidade visual.

## 10. Regras editoriais

Cada página seguirá a anatomia vigente:

1. título funcional
2. linha de enquadramento
3. Antes de começar
4. Conceito
5. Uso pelo arquiteto
6. Exercício numerado
7. Fontes

O texto manterá o padrão do curso: definição antes do exemplo, exemplos de domínios variados, aplicação da ACME concentrada no exercício e nos trechos explicitamente aplicados, negrito parcimonioso, referências precisas e ausência de gabarito público.

Os exemplos principais não repetirão o mesmo domínio em blocos consecutivos. Termos do glossário serão ligados no primeiro uso. Toda fonte será listada em APA 7 e adicionada à bibliografia geral quando ainda não existir.

## 11. Arquivos previstos

Arquivos novos:

- `docs/modulo-3-design-e-padroes/bloco-1-principios-de-design.md`
- `docs/modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md`
- `docs/modulo-3-design-e-padroes/sintese.md`
- quatro imagens principais em `docs/assets/images/`
- fontes editáveis de diagramas em `docs/assets/diagrams/`, quando aplicável

Arquivos revisados:

- `docs/modulo-3-design-e-padroes/index.md`
- `docs/modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md`
- `docs/modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md`
- `docs/referencia/glossario.md`
- `docs/referencia/bibliografia.md`
- `mkdocs.yml`
- testes de contrato de conteúdo

## 12. Validação e critérios de aceite

O módulo estará concluído quando:

- os quatro blocos, índice e síntese estiverem publicados e navegáveis
- os exercícios 9 a 12 formarem uma cadeia coerente de produtos
- estilo, padrão arquitetural e padrão de design forem distinguidos sem contradição
- os blocos 2 e 4 estiverem harmonizados com os blocos novos
- todo bloco tiver ao menos um visual descritivo e acessível
- nenhum visual ou texto entregar a resposta fechada do exercício
- links, âncoras, fontes e imagens locais forem válidos
- o validador editorial não registrar violações
- a suíte de testes estiver verde
- `mkdocs build --strict` concluir sem erro
- os quatro blocos forem inspecionados visualmente no site gerado

## 13. Riscos e controles

| Risco | Controle |
| --- | --- |
| Módulo extenso demais | Limitar repertórios e remover repetição entre tabela e narrativa |
| Confusão entre estilo e padrão | Usar a taxonomia da seção 6 em texto, visual e exercícios |
| Padrões apresentados como receita | Exigir problema, forças, custo e sinal de inadequação |
| Exercícios desconectados | Fazer cada produto alimentar explicitamente o bloco seguinte |
| ADR virar formulário burocrático | Relacionar cada campo à decisão real construída na aula |
| Imagens entregarem o exercício | Usar exemplos genéricos nos visuais e reservar os dados decisórios para o enunciado |
| Regressão editorial | Criar testes antes da produção e rodar validação completa ao final |
