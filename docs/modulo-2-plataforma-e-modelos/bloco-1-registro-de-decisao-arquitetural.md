# Registro de decisão arquitetural

Este bloco abre a aula respondendo a uma pergunta prática, como registrar uma decisão arquitetural já tomada de forma que ela sobreviva à saída de quem a tomou.

## Antes de começar

- [ADR](../referencia/glossario.md#adr)

## Conceito

A distinção entre decisão arquitetural e decisão de implementação já foi estabelecida na seção Conceito do [bloco 1 da Aula 1](../modulo-1-fundamentos/bloco-1-arquitetura-e-papel-do-arquiteto.md#conceito). Decisão arquitetural condiciona partes do sistema que ainda não existem e é cara de reverter depois que o desenvolvimento avança sobre ela, decisão de implementação afeta um trecho localizado e pode ser revista sem repercussão sobre o restante do sistema. Este bloco parte dessa distinção para tratar de como registrar a primeira de forma rastreável.

Um **ADR**, sigla de Architecture Decision Record, é um documento curto que descreve uma decisão arquitetural, o contexto que a motivou e suas consequências. O documento não registra apenas a escolha final, registra também o problema que a provocou e as alternativas que ficaram de fora, para que quem ler o ADR meses depois entenda por que aquele caminho foi preferido e não outro.

Michael Nygard propôs o formato mais citado para esse documento, com cinco partes fixas. **Título** nomeia a decisão em frase curta, como "Adoção de arquitetura orientada a eventos para o módulo de admissão do sistema de gestão de leitos hospitalares". **Contexto** descreve de forma neutra as forças em jogo, como o requisito técnico, organizacional ou de negócio que tornou a decisão necessária, por exemplo a exigência de que uma plataforma de agendamento de serviços absorva picos de solicitação sem perder requisições. **Decisão** registra a escolha em linguagem ativa, do tipo "decidimos adotar", incluindo pelo menos uma alternativa considerada e descartada. **Status** indica o estágio da decisão, proposta, aceita ou substituída por outra ADR mais recente. **Consequências** lista os resultados esperados, com pelo menos um efeito positivo e um negativo, porque toda decisão arquitetural troca um atributo de qualidade por outro.

O **MADR**, Markdown Architectural Decision Records, é um formato alternativo mais estruturado, com campos adicionais para requisitos considerados, opções avaliadas lado a lado e critérios de comparação explícitos entre elas. Onde o formato de Nygard cabe em um parágrafo por seção, o MADR força o autor a nomear cada opção descartada antes de justificar a escolhida, o que ajuda quando o número de alternativas é maior que duas.

A prática recomendada mantém o ADR versionado junto do código-fonte, no mesmo repositório, em vez de um documento externo em ferramenta de gestão de conteúdo. Um ADR versionado junto do código muda quando o código muda, é revisado no mesmo fluxo de pull request e nunca fica desatualizado em relação à decisão que descreve. Um documento externo estático tende a divergir do sistema real assim que a primeira decisão nele registrada é revista sem que alguém lembre de atualizá-lo.

## Uso pelo arquiteto

O arquiteto escreve o ADR no momento da decisão, não depois, porque é nesse momento que as alternativas descartadas e o raciocínio que as eliminou ainda estão claros na cabeça de quem decidiu. Quem entra no projeto mais tarde não tem acesso a essa conversa, só ao ADR, e um registro escrito depois de forma retrospectiva tende a simplificar o raciocínio original e a esconder justamente a alternativa que valeria a pena reconsiderar se o contexto mudar.

## Exercício 5

A ACME é a universidade privada brasileira em modernização incremental do sistema acadêmico, usada como caso desta disciplina. No exercício do [bloco 4 da Aula 1](../modulo-1-fundamentos/bloco-4-estilos-arquiteturais.md), você comparou três estilos arquiteturais contra os dois cenários da ACME e defendeu um deles. Escreva a ADR que registra essa decisão, no formato de Nygard.

A ADR precisa conter

1. título
2. contexto, citando os dois cenários que motivaram a análise
3. decisão, nomeando o estilo escolhido e ao menos um estilo alternativo descartado
4. status
5. consequências, com ao menos uma positiva e uma negativa

## Fontes

Glossário do curso, entrada [ADR](../referencia/glossario.md#adr). Nygard (2011), listado na [bibliografia](../referencia/bibliografia.md). MADR (sem data), listado na [bibliografia](../referencia/bibliografia.md).
