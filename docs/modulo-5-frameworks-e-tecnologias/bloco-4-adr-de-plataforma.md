# ADR de plataforma

Este bloco fecha o par de decisões da aula respondendo a uma pergunta que só se coloca depois do bloco anterior, como registrar a escolha de plataforma feita ali, de um jeito que sobreviva à saída de quem a tomou.

## Antes de começar

- [ADR](../referencia/glossario.md#adr)
- [Plataforma arquitetural](../referencia/glossario.md#plataforma-arquitetural)
- [Dependência de fornecedor](../referencia/glossario.md#dependencia-de-fornecedor)

## Conceito

Um **ADR de plataforma** é o segundo ADR do par ensinado na disciplina, escrito no mesmo template de dez campos apresentado no [bloco 4 da Aula 3](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md), mas aplicado a uma decisão de natureza diferente da primeira. Aquele ADR registra a escolha de um estilo arquitetural. O ADR deste bloco registra a escolha de uma das plataformas candidatas capazes de concretizar esse estilo, comparação que o [bloco 2](bloco-2-plataforma-arquitetural.md) desta aula já ensinou a montar.

O template não muda entre os dois. O conteúdo de cada campo muda, e três campos mudam de forma característica.

### O que muda no campo de forças

Em um ADR de estilo, as forças são atributos de qualidade do sistema, como absorver pico de carga ou isolar falha. Em um ADR de plataforma, elas incluem esses atributos e acrescentam os sete fatores de adaptação ao contexto apresentados no Conceito do [bloco 2](bloco-2-plataforma-arquitetural.md), entre eles conhecimento técnico do time, custo de aquisição e renovação e confiabilidade dos fornecedores.

A essas forças soma-se uma que só aparece na decisão de plataforma. A **dependência de fornecedor** é a dificuldade de trocar ou negociar uma dependência, técnica ou organizacional. Serviços gerenciados podem ser escolhas excelentes quando reduzem risco operacional, mas precisam ficar explícitos no ADR em seis dimensões.

1. API proprietária
2. formato de dados
3. identidade
4. observabilidade
5. custo de saída de dados
6. habilidades da equipe

Abstrair tudo antecipadamente para fugir dessa dependência cria uma plataforma paralela, que é um custo novo. O caminho é preferir contratos de domínio, exportação testada, infraestrutura declarativa e uma condição mensurável de saída. A dependência de fornecedor é aceitável quando o benefício específico é conhecido e a decisão é revisável.

### O que muda no campo de alternativas

Em um ADR de plataforma, o campo de alternativas já vem pronto do bloco anterior. O quadro comparativo montado no [Exercício 18](bloco-2-plataforma-arquitetural.md#exercicio-18), com as plataformas candidatas nas linhas e os fatores nas colunas, é exatamente o que o campo pede, cada alternativa com as forças que atende e os riscos que introduz. Transportar o quadro para o registro é o que impede que a alternativa descartada apareça só pelo nome, sem ter sido comparada de fato.

### O que muda no campo de consequências

Reverter uma decisão de estilo cobra custo de reestruturação de componentes, porque a fronteira entre as partes do sistema muda. Reverter uma decisão de plataforma cobra custo de treinamento e de migração de código, porque a equipe precisa aprender uma API diferente e o código escrito contra a plataforma anterior precisa ser reescrito contra a nova, mesmo quando o estilo arquitetural permanece o mesmo dos dois lados da troca.

Uma seguradora que já decidiu por uma arquitetura orientada a eventos para separar emissão de apólice, análise de risco e abertura de sinistro enfrenta essa segunda decisão ao escolher entre duas plataformas de mensageria candidatas. Se ela troca de plataforma depois que os três serviços já estão em produção, o custo recai sobre o time, que precisa reaprender a API de publicação e consumo, e sobre o código de cada serviço, que precisa ser adaptado. O estilo orientado a eventos em si não muda. Uma operação de logística de última milha que decidiu por microsserviços para isolar roteamento, despacho e rastreamento enfrenta a mesma segunda decisão ao escolher entre dois orquestradores de execução, e trocar de orquestrador depois da adoção cobra da equipe de operação o aprendizado de um modelo de implantação diferente e a reescrita dos scripts de infraestrutura, novamente sem alterar a divisão em serviços que define o estilo.

### O par de registros

Os dois ADRs não vivem isolados um do outro. O ADR de plataforma faz uma **referência cruzada** ao título do ADR de estilo no seu campo de contexto, porque a plataforma só faz sentido como resposta a um estilo já fixado, e um leitor que chega ao ADR de plataforma sem ter lido o ADR de estilo precisa encontrar esse encadeamento no próprio texto. Quando a prática se firma, o ADR de estilo passa a citar, no campo de revisão, o ADR de plataforma que veio depois, fechando o par nos dois sentidos.

## Uso pelo arquiteto

O arquiteto escreve este segundo registro logo depois de fechar a comparação de plataformas, no mesmo momento em que as candidatas descartadas e o critério que as eliminou ainda estão claros. O campo de evidências é o que mais se beneficia desse momento, porque é quando ainda existem o teste de carga, a prova de conceito ou a medição que sustentaram a escolha, e é trivial anotar onde cada um pode ser reproduzido. Meses depois, essa informação já se perdeu, e o registro fica com uma justificativa que ninguém consegue verificar.

## Exercício 20

Escreva o ADR que registra a escolha de plataforma que você fez no [Exercício 18](bloco-2-plataforma-arquitetural.md#exercicio-18) do bloco anterior, no mesmo template de dez campos usado no [bloco 4 da Aula 3](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md).

1. título, estado e data
2. contexto, referenciando pelo título o ADR de estilo que você escreveu no [Exercício 12](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md#exercicio-12)
3. forças, com pelo menos três dos sete fatores de adaptação ao contexto do bloco 2, mais ao menos uma das seis dimensões de dependência de fornecedor listadas no Conceito acima
4. alternativas, transportando o quadro comparativo que você montou no Exercício 18
5. decisão, nomeando a plataforma escolhida e conectando a justificativa às forças
6. consequências, com ao menos uma positiva, uma negativa e uma neutra
7. evidências, indicando o que sustentaria a escolha e onde poderia ser reproduzido
8. revisão, com um gatilho observável ligado à convivência com o núcleo COBOL sobre CICS

O campo de evidências é o mais difícil neste exercício, porque a ACME não tem ambiente de teste de carga, conforme registra a [arquitetura de linha de base](../caso-acme/linha-de-base.md). Nomear a evidência que você gostaria de ter, e que não existe, é resposta melhor do que inventar uma medição.

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Mendes, M. (2026a). *Arquitetura de software* [Material de curso]. https://marco-mendes.github.io/arquitetura-software/ ([template de ADR](https://marco-mendes.github.io/arquitetura-software/referencia/template-adr/) de dez campos e a seção [custo e lock-in](https://marco-mendes.github.io/arquitetura-software/modulo-6-nuvem/padroes-e-decisoes/), fonte da definição de dependência de fornecedor e das seis dimensões)
- Nygard, M. (2011, 15 de novembro). *Documenting architecture decisions*. Cognitect Blog. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions (formato de cinco partes)
- MADR. (2024). *Markdown Architectural Decision Records* (Versão 4.0.0). https://adr.github.io/madr/ (campos do formato MADR)

**Material do curso.** Glossário, entradas [ADR](../referencia/glossario.md#adr), [plataforma arquitetural](../referencia/glossario.md#plataforma-arquitetural) e [dependência de fornecedor](../referencia/glossario.md#dependencia-de-fornecedor). Dossiê da instituição fictícia [ACME](../caso-acme/index.md) e [arquitetura de linha de base](../caso-acme/linha-de-base.md).
