# ADR de plataforma

Este bloco fecha o par de decisões da aula respondendo a uma pergunta que só se coloca depois do bloco anterior, como registrar a escolha de plataforma feita ali, de um jeito que sobreviva à saída de quem a tomou.

## Antes de começar

- [ADR](../referencia/glossario.md#adr)
- [Plataforma arquitetural](../referencia/glossario.md#plataforma-arquitetural)

## Conceito

Um **ADR de plataforma** é o segundo ADR do par ensinado nesta aula, escrito no mesmo formato apresentado no [bloco 1](bloco-1-registro-de-decisao-arquitetural.md) desta aula, título, contexto, decisão, status e consequências, mas aplicado a uma decisão de natureza diferente da primeira. O ADR do bloco 1 registra a escolha de um estilo arquitetural, o ADR deste bloco registra a escolha de uma das plataformas candidatas capazes de concretizar esse estilo, comparação que o [bloco 2](bloco-2-plataforma-arquitetural.md) desta aula já ensinou a montar.

O formato não muda entre as duas ADRs, o conteúdo de cada seção muda. O contexto de um ADR de estilo descreve forças ligadas à forma estrutural do sistema, como a necessidade de isolar partes que escalam de maneira diferente. O contexto de um ADR de plataforma descreve forças ligadas à execução concreta dessa forma, como maturidade, custo de operação e convivência com o que já está em produção, os mesmos critérios apresentados no Conceito do [bloco 2](bloco-2-plataforma-arquitetural.md). A diferença mais visível aparece nas consequências. Reverter uma decisão de estilo tende a cobrar **custo de reestruturação de componentes**, porque a fronteira entre as partes do sistema muda. Reverter uma decisão de plataforma tende a cobrar **custo de treinamento e de migração de código**, porque a equipe precisa aprender uma API diferente e o código escrito contra a plataforma anterior precisa ser reescrito contra a nova, mesmo quando o estilo arquitetural permanece o mesmo dos dois lados da troca.

Uma seguradora que já decidiu por uma arquitetura orientada a eventos para separar emissão de apólice, análise de risco e abertura de sinistro enfrenta essa segunda decisão ao escolher entre duas plataformas de mensageria candidatas para ligar esses três serviços. Se a seguradora troca de plataforma depois que os três serviços já estão em produção, o custo recai sobre o time que precisa reaprender a API de publicação e consumo de eventos e sobre o código de cada serviço, que precisa ser adaptado à nova plataforma, o estilo orientado a eventos em si não muda. Uma operação de logística de última milha que decidiu por microsserviços para isolar roteamento, despacho e rastreamento de entrega enfrenta a mesma segunda decisão ao escolher entre dois orquestradores de execução candidatos. Trocar de orquestrador depois da adoção cobra da equipe de operação o aprendizado de um modelo de implantação diferente e a reescrita dos scripts de infraestrutura já feitos para o orquestrador anterior, novamente sem alterar a divisão em serviços que define o estilo escolhido.

## Uso pelo arquiteto

O arquiteto que já escreveu o ADR de estilo do [bloco 1](bloco-1-registro-de-decisao-arquitetural.md) consolida o hábito de registro ao escrever este segundo ADR logo depois de fechar a comparação de plataformas do [bloco 2](bloco-2-plataforma-arquitetural.md), no mesmo momento em que as candidatas descartadas e o critério que as eliminou ainda estão claros. Os dois ADRs não vivem isolados um do outro, o ADR de plataforma faz uma **referência cruzada** ao título do ADR de estilo no seu campo de contexto, porque a plataforma só faz sentido como resposta a um estilo já fixado, e um leitor que chega ao ADR de plataforma sem ter lido o ADR de estilo precisa encontrar esse encadeamento no próprio texto, não em uma conversa que não está mais disponível. Quando a prática se firma, o próprio ADR de estilo passa a citar, na seção de consequências, o ADR de plataforma que veio depois, fechando o par nos dois sentidos.

## Exercício 7

Escreva o ADR que registra a escolha de plataforma que você fez no exercício do [bloco 2](bloco-2-plataforma-arquitetural.md) desta aula, no mesmo formato de Nygard usado no [bloco 1](bloco-1-registro-de-decisao-arquitetural.md).

O ADR precisa conter

1. título
2. contexto
3. decisão, nomeando a plataforma escolhida e a plataforma alternativa descartada
4. status
5. consequências, com ao menos uma positiva e uma negativa

O campo de contexto precisa referenciar, pelo título, o ADR de estilo que você escreveu no exercício do [bloco 1](bloco-1-registro-de-decisao-arquitetural.md). O campo de decisão precisa citar o quadro comparativo que você montou no Exercício 6 como evidência de que a escolha considerou alternativas reais, não apenas a plataforma mais familiar.

## Fontes

Glossário do curso, entradas [ADR](../referencia/glossario.md#adr) e [plataforma arquitetural](../referencia/glossario.md#plataforma-arquitetural). Nygard (2011), listado na [bibliografia](../referencia/bibliografia.md). MADR (sem data), listado na [bibliografia](../referencia/bibliografia.md).
