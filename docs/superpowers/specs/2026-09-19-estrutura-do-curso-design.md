# Estrutura do site da disciplina Estratégias e Projeto de Arquitetura de Software

Data: 19/09/2026
Disciplina: IEC/PUC Minas, turmas Arq. Software Distribuído 10.1 e Arq. Soluções Digitais 1.1
Repositório: `~/code/projeto-arquitetura-software`

## 1. Objetivo

Converter o repositório atual, composto por 21 arquivos Markdown soltos e numerados de 1.0 a 4.4, em um site publicado com MkDocs Material que sirva simultaneamente como material do aluno e como roteiro de condução de seis aulas síncronas.

## 2. Restrições de formato

A aula ocorre das 19h00 às 22h30, com intervalo das 20h30 às 20h45 e encerramento do conteúdo até 22h10. O tempo útil é de 175 minutos. A unidade de condução é o bloco, composto por 25 minutos de conceito e 15 minutos de exercício, totalizando 40 minutos. Cabem quatro blocos por aula, restando 15 minutos para abertura, transições e fechamento. A disciplina tem seis aulas, portanto 24 blocos.

Datas das aulas: 21/09, 23/09, 28/09, 30/09, 05/10 e 15/10 de 2026.

## 3. Decisões de estrutura

As decisões abaixo foram tomadas pelo professor em 19/09/2026.

| Decisão | Escolha |
| --- | --- |
| Audiência do texto | Material do aluno, escrito com profundidade. Serve de roteiro porque o professor se orienta pelos temas e figuras. |
| Unidade do módulo | Um módulo por aula, com quatro blocos cada. |
| Localização do caso | Trilha própria no site. As páginas de bloco ficam em nível de teoria. |
| Exercícios | Produção de artefato sobre o caso comum, individuais, com gabarito no site. |
| Caso | ACME, aprofundado em relação à versão usada na disciplina irmã. |
| Figuras | Mermaid onde couber, imagem do professor apenas onde o desenho exigir expressão que Mermaid não oferece. |
| Tempos visíveis | Apenas no índice do módulo. As páginas de bloco não exibem cronômetro. |
| Conteúdo atual do repositório | Matéria-prima. Texto reescrito no padrão e no tom do curso. |

### 3.1 Justificativa da trilha separada para o caso

Duas regras de material didático estabelecidas anteriormente incidem sobre essa escolha. A primeira determina que caso aplicado não aparece em página de teoria pura. A segunda determina que toda página é autocontida, porque a navegação permite abrir qualquer página diretamente.

Manter o caso em trilha própria satisfaz as duas regras e dá ao dossiê da ACME o espaço necessário para o aprofundamento pedido. As páginas de bloco permanecem em nível conceitual, e cada exercício reintroduz a ACME em uma frase, trazendo embutido apenas o extrato de dados que aquele exercício exige.

## 4. Estrutura de diretórios

```
docs/
  index.md                     Apresentação da disciplina, uso do site, avaliação
  cronograma.md                As seis aulas, os 24 blocos, datas
  modulo-1-fundamentos/
    index.md                   Pergunta-guia, objetivos, grade de tempo dos quatro blocos
    bloco-1-arquitetura-e-papel-do-arquiteto.md
    bloco-2-qualidade-e-tipos-de-requisito.md
    bloco-3-cenarios-e-significancia-arquitetural.md
    bloco-4-estilos-arquiteturais.md
    sintese.md                 Checklist, autoavaliação, referências da aula
  modulo-2-plataforma-e-modelos/
  modulo-3-descoberta-e-riscos/
  modulo-4-dados-e-seguranca/
  modulo-5-blueprint-e-trm/
  modulo-6-evolucao-e-governanca/
  caso-acme/
    index.md                   A instituição, os atores, a pergunta central
    linha-de-base.md           Arquitetura atual em detalhe, dívida técnica quantificada
    dados-operacionais.md      Volumes, sazonalidade, incidentes, custos, contratos
    artefatos.md               O que cada aula acrescenta ao caso
  referencia/
    glossario.md
    bibliografia.md
  assets/
    images/
    stylesheets/
    javascripts/
```

## 5. Anatomia da página de bloco

Toda página de bloco segue oito seções, sempre na mesma ordem.

1. Título funcional, sem subtítulo e sem abrir em forma de pergunta
2. Uma linha de enquadramento, declarando a questão que o bloco responde
3. **Antes de começar**, com os termos necessários ligados ao glossário
4. **Conceito**, correspondente aos 25 minutos de exposição, em nível de teoria
5. **Uso pelo arquiteto**, ligando o conceito à prática profissional
6. **Exercício**, correspondente aos 15 minutos, com enunciado autocontido
7. **Gabarito**, em bloco colapsável, ou critério de avaliação quando a resposta for aberta
8. **Fontes**, referentes ao conteúdo daquele bloco

O enunciado do exercício nunca instrui o aluno a abrir outra página para localizar informação. O extrato do caso necessário à resolução aparece no próprio enunciado.

## 6. Mapeamento dos blocos

### 6.1 Aula 1, em 21/09

Ementa definida pelo professor: enquadramento do problema, conceito de atributos de qualidade, exercício de escrita de atributos de qualidade, revisão do conceito de estilo arquitetural, exercício de comparação de estilos.

| Bloco | Conceito | Exercício |
| --- | --- | --- |
| 1 | Arquitetura, papel do arquiteto e enquadramento do problema | Identificar, no caso ACME, o que a instituição quer, quem decide e quais restrições chegam fechadas |
| 2 | Qualidade em software, atributo de qualidade, e a distinção entre requisito funcional, requisito não funcional, requisito de atributo de qualidade e restrição | Classificar requisitos da ACME nas quatro categorias e reescrever dois deles em forma mensurável |
| 3 | Cenários de atributos de qualidade no formato de seis elementos e julgamento de significância arquitetural | Escrever dois cenários para a ACME e defender quais constituem ASR, aplicando o roteiro de sete perguntas |
| 4 | Estilos arquiteturais e a relação entre estilo e atributo de qualidade | Comparar três estilos candidatos contra os cenários escritos no bloco 3 |

A leitura do caso não ocupa tempo de aula. Ela é aplicada dentro dos exercícios.

### 6.2 Aula 2, em 23/09

Ementa definida pelo professor: conceito de plataforma arquitetural, exercício de comparação de plataformas, ADR de plataforma, representação de modelos, revisão de modelagem arquitetural, modelagem C4 níveis 1 e 2, exercícios.

Com a saída do ADR da Aula 1, esta aula acumula cinco temas para quatro blocos: conceito de ADR, plataforma arquitetural, ADR de plataforma, representação de modelos e C4. A partição fica pendente de decisão do professor.

### 6.3 Aulas 3 a 6

Temas herdados das Orientações da Disciplina v4, deslizados uma posição em 19/09/2026. A partição em blocos será definida quando a ementa de cada uma for revista.

| Aula | Data | Tema |
| --- | --- | --- |
| 3 | 28/09 | Descoberta detalhada, arquitetura de linha de base e riscos sistêmicos |
| 4 | 30/09 | Requisitos avançados, arquitetura de dados e arquitetura de segurança |
| 5 | 05/10 | Blueprint da solução, modelo técnico de referência e infraestrutura alvo |
| 6 | 15/10 | Análise de lacunas, compromissos arquiteturais, roteiro de evolução e governança |

Os arquivos `4.3 Riscos Arquiteturais.md` e `4.4 Plano de Resposta de Riscos de Arquitetura.md` do repositório atual servem à Aula 3. O arquivo `1.1.1 Como capturar requisitos arquiteturais.md` serve à Aula 4.

## 7. Texto de referência sobre qualidade

O professor forneceu em 19/09/2026 um texto de dez seções sobre atributos de qualidade e requisitos arquiteturalmente significativos. Esse texto tem dois papéis.

O primeiro é de conteúdo. As seções 1 e 2 compõem a teoria do bloco 2 da Aula 1. As seções 2.3, 3, 7 e 8 compõem a teoria do bloco 3. As seções 9 e 10 se distribuem entre os dois, como erros frequentes e síntese.

O segundo é de tom. O registro daquele texto define o padrão de escrita de todo o material: expositivo, impessoal, com definição formal antes do exemplo, exemplos analisados como casos rotulados, e contraste feito por formulações sucessivas do mesmo requisito. Não há abertura com imagem ou cena, frase de efeito isolada, pergunta retórica, metáfora explicativa ou fecho sentencioso.

As regras de pontuação do professor prevalecem sobre a pontuação do texto-fonte. O material não usa ponto-e-vírgula, e o travessão aparece apenas como aposto isolado, no máximo uma vez por parágrafo.

### 7.1 Exemplos ilustrativos diversos

Condição estabelecida pelo professor na aprovação desta especificação em 19/09/2026: cada conceito é tornado concreto por exemplos de domínios variados, não por um único domínio repetido.

O texto de referência já opera assim. Ele usa aplicativo bancário para segurança, plataforma de transmissão de vídeo para escala, portal institucional e sistema de controle hospitalar para contrastar tolerância a indisponibilidade, serviço de pagamentos para recuperação regional e roteamento entre adquirentes, página administrativa de consulta de feriados para o caso de requisito de qualidade sem significância arquitetural, e expansão para cinco países como objetivo de negócio convertido em requisitos.

Regra de aplicação: cada seção de conceito apresenta ao menos dois exemplos de domínios distintos. Os domínios circulam ao longo do curso e nenhum deles se repete como exemplo principal em blocos consecutivos.

Essa regra não conflita com a separação entre teoria e caso descrita em 3.1. Exemplo ilustrativo é uma frase ou um parágrafo que torna um conceito concreto, e pertence à página de conceito. Caso aplicado é a ACME, com seus dados, atores e artefatos acumulados, e pertence à trilha própria e aos exercícios.

### 7.2 Distinção conceitual adotada

O curso trata atributo de qualidade e requisito arquiteturalmente significativo como conceitos distintos, conforme o texto de referência. Atributo de qualidade é propriedade pela qual o sistema é avaliado. Requisito de atributo de qualidade é a expectativa concreta e mensurável sobre essa propriedade. ASR é o requisito cuja satisfação influencia materialmente a arquitetura, podendo ser de qualidade, funcional ou restritivo.

Essa posição contraria o que os arquivos atuais afirmam. O arquivo `1.2 Requisitos Não-Funcionais.md` abre declarando que requisitos não funcionais são também chamados de atributos de qualidade. A reescrita corrige essa equivalência.

### 7.3 Verificações pendentes antes da publicação

Os itens abaixo aparecem no texto de referência e não foram verificados em fonte aberta.

- O número de nove características da ISO/IEC 25010:2023
- O DOI atribuído ao relatório CMU/SEI-2003-TR-016
- A existência da "Quality Attribute Workshop Collection", SEI, 2016, como item bibliográfico próprio

As duas fórmulas em notação LaTeX da seção 5 do texto chegaram quebradas e serão convertidas em prosa. As tabelas chegaram achatadas e serão remontadas.

## 8. Migração do conteúdo atual

Os 21 arquivos servem de matéria-prima e têm o texto reescrito. Três problemas técnicos exigem tratamento.

As figuras estão hospedadas em `user-attachments` do GitHub, fora do repositório, e dependem da conta que as publicou. Cada uma vira diagrama Mermaid ou arquivo local em `docs/assets/images`.

A formatação é inconsistente, com mistura de níveis de cabeçalho, HTML solto e marcadores irregulares.

Quatro arquivos estão praticamente vazios, com 119 bytes cada: os três de modelagem de microsserviços e o de exemplo C1, C2 e C3 de internet banking, com 369 bytes.

## 9. Aparato técnico

A configuração segue o padrão já validado na disciplina irmã em `~/code/projeto-arquitetura-solucao`: MkDocs Material em português do Brasil, tema com paleta custom, Mermaid por `pymdownx.superfences`, `pymdownx.details` para os gabaritos colapsáveis, `md_in_html` e `attr_list`.

A suíte de testes de conteúdo e o validador daquele repositório serão adaptados, não copiados sem revisão, porque as asserções atuais refletem a estrutura de oito páginas por módulo, diferente da estrutura de blocos adotada aqui.

## 10. Escopo da primeira rodada

Configuração do MkDocs, navegação das seis aulas, dossiê da ACME aprofundado e as quatro páginas do Módulo 1, mais o índice e a síntese daquele módulo. Os módulos 2 a 6 ficam como esqueleto navegável.

## 11. Pendências

1. Partição da Aula 2 em quatro blocos, com cinco temas a acomodar
2. Ementa e partição das Aulas 3 a 6
3. Verificação das três referências listadas em 7.3
4. Definição do método de avaliação da disciplina, que a página inicial precisa declarar

## 12. Revisão 1, 19/09/2026

O professor revisou o Módulo 1 publicado e determinou as mudanças abaixo. Elas alteram decisões tomadas nas seções anteriores e têm precedência sobre elas.

### 12.1 Anatomia da página de bloco, revista

A página de bloco passa a ter **sete seções**, não oito. O Gabarito sai da anatomia pública.

1. Título de nível 1, funcional
2. Linha de enquadramento
3. `## Antes de começar`
4. `## Conceito`
5. `## Uso pelo arquiteto`
6. `## Exercício N`, com N o número sequencial do exercício ao longo de toda a disciplina (Aula 1: 1 a 4, Aula 2 continua de 5, e assim por diante)
7. `## Fontes`

O validador de conteúdo (`scripts/validate_content.py`) e seus testes precisam refletir essa anatomia de sete seções, sem exigir Gabarito, e passam a exigir que o cabeçalho de Exercício traga um número.

### 12.2 Gabarito sai do site, entra na narrativa do PKA

Nenhuma página pública contém gabarito, resposta ou critério de avaliação fechado. Esse conteúdo é reescrito com mais profundidade do que tinha no site e passa a viver em `~/pka/projects/aulas/PRJ-aulas-iec-asd-10-estrategias-e-projeto-de-arquitetura-de-software.md`, arquivo de narrativa do projeto no PKA do professor, fora deste repositório.

### 12.3 Enunciado de exercício em lista numerada, não em prosa

A palavra "prosa" não aparece em lugar nenhum do site. Onde um enunciado de exercício traz mais de uma pergunta ou instrução, elas aparecem como lista numerada (`1.`, `2.`, `3.`), não emendadas num parágrafo corrido. Os dados do caso continuam em tabela, como já estava.

### 12.4 Datas reais removidas, cronograma genérico

Nenhuma data de calendário real (DD/MM/AAAA de 2026) aparece fora da trilha do caso ACME. O cronograma e os índices de módulo passam a falar em "Aula 1", "Aula 2" e assim por diante, sem data. O horário de aula (19h00 às 22h30, intervalo 20h30 às 20h45) permanece, por ser estrutura de bloco, não data de calendário.

As datas fictícias do caso ACME (calendário acadêmico, incidentes) **não são tocadas** por esta regra. Pertencem ao universo do caso, não ao calendário real da oferta.

A página inicial (`docs/index.md`) perde o parágrafo de abertura que descrevia a disciplina e suas duas funções, por decisão editorial do professor.

### 12.5 Bibliografia em formato APA

`docs/referencia/bibliografia.md` e as citações nas seções Fontes das páginas de bloco seguem o formato APA 7. Dados confirmados para as cinco referências já em uso:

- International Organization for Standardization/International Electrotechnical Commission/Institute of Electrical and Electronics Engineers. (2022). *Systems and software engineering — Architecture description* (ISO/IEC/IEEE 42010:2022).
- International Organization for Standardization. (2023). *Systems and software engineering — Systems and software quality requirements and evaluation (SQuaRE) — Product quality model* (ISO/IEC 25010:2023).
- Barbacci, M., Ellison, R., Lattanze, A., Stafford, J., Weinstock, C., & Wood, W. (2003). *Quality attribute workshops (QAWs), third edition* (CMU/SEI-2003-TR-016). Software Engineering Institute, Carnegie Mellon University.
- Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley.
- Ford, N., & Richards, M. (2020). *Fundamentals of software architecture*. O'Reilly.

Os dados de Bass, Clements e Kazman (4ª edição, 2021, Addison-Wesley) foram confirmados na bibliografia publicada de `marco-mendes.github.io/arquitetura-software`, do próprio professor. As duas lacunas antes registradas na seção 7.3 (número de características da 25010:2023, DOI do relatório do SEI, e a "Quality Attribute Workshop Collection" de 2016) continuam sem entrar na bibliografia, porque não foram verificadas.

### 12.6 Aprofundamento do bloco de cenários e QAW

O bloco que trata de cenários de atributo de qualidade e significância arquitetural (hoje `bloco-3-cenarios-e-significancia-arquitetural.md`) ganha tratamento mais rigoroso do método Quality Attribute Workshop: mais exemplos de cenário, além dos dois já usados, e descrição mais completa do processo de elicitação do QAW junto às partes interessadas, mantendo a base no texto de referência do professor (`docs/superpowers/specs/2026-09-19-texto-referencia-atributos-qualidade.md`).

### 12.7 Aprofundamento do bloco de estilos, com o material de base do professor

O bloco que trata de estilos arquiteturais (hoje `bloco-4-estilos-arquiteturais.md`) ganha tratamento muito mais profundo, inspirado no rigor do material de base do professor em `marco-mendes.github.io/arquitetura-software` (repositório `marco-mendes/arquitetura-software`, arquivos `docs/modulo-1-visao-geral/conceitos.md` e `padroes-e-decisoes.md`): tabela de forças, anti-padrão e quando usar/evitar para cada estilo comparado, heurística prática por estilo (por exemplo a regra do sumidouro, quando mais de 80% das chamadas apenas repassam sem decidir), e referência à Lei de Conway quando pertinente.

Isso **não reabre** a decisão da seção 9 sobre MVC, MVVM, DDD e Strangler não serem estilos arquiteturais para este curso. O professor confirmou manter a exclusão em 19/09/2026, mesmo o material de base dele os tratando como parte de uma taxonomia mais ampla de famílias arquiteturais. Os quatro estilos comparados no exercício continuam sendo camadas, microsserviços, orientado a eventos e microkernel.

A obra do próprio professor entra na bibliografia como material de curso, em formato APA de página web:

- Mendes, M. (2026). *Arquitetura de software* [Material de curso]. https://marco-mendes.github.io/arquitetura-software/

### 12.8 Negrito parcimonioso

Os termos centrais de cada conceito, no primeiro uso dentro da seção Conceito, podem receber destaque em negrito, no máximo três a cinco por página de bloco. Negrito não é usado em frase inteira, em dado numérico, nem em mais de uma ocorrência do mesmo termo na mesma página.
