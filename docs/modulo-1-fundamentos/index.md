# Aula 1, fundamentos de arquitetura de software

A aula responde à seguinte questão: o que um arquiteto de software decide, a partir de qual entendimento de qualidade, e com base em qual repertório de estilos.

## Objetivos de aprendizagem

Ao final da aula, o aluno é capaz de

- descrever o papel do arquiteto de software e distingui-lo de outros papéis técnicos de decisão
- diferenciar requisito funcional, requisito não funcional, requisito de atributo de qualidade e restrição
- classificar um requisito declarado por uma parte interessada em uma dessas quatro categorias
- escrever um cenário de atributo de qualidade no formato de seis elementos
- justificar, para um requisito dado, se ele constitui um requisito arquiteturalmente significativo
- comparar estilos arquiteturais candidatos a partir de sua adequação a cenários de qualidade

## Grade de tempo

A aula ocorre em 21/09/2026, das 19h00 às 22h30, com intervalo das 20h30 às 20h45. O tempo de conteúdo encerra até as 22h10. Os quatro blocos abaixo são o único lugar do site em que os minutos aparecem. As páginas de cada bloco não exibem cronômetro.

| Bloco | Conceito | Conceito (min) | Exercício (min) |
| --- | --- | --- | --- |
| 1 | Arquitetura, papel do arquiteto e enquadramento do problema | 25 | 15 |
| 2 | Qualidade em software, atributo de qualidade e tipos de requisito | 25 | 15 |
| 3 | Cenários de atributos de qualidade e significância arquitetural | 25 | 15 |
| 4 | Estilos arquiteturais e sua relação com atributo de qualidade | 25 | 15 |

Os quatro blocos somam 160 minutos. Os 15 minutos restantes do tempo útil de 175 minutos cobrem abertura, transições e fechamento.

## Roteiro da aula

O [bloco 1](bloco-1-arquitetura-e-papel-do-arquiteto.md) expõe o conceito de arquitetura de software e o papel do arquiteto. O exercício desse bloco parte do dossiê da instituição fictícia ACME, caso corporativo usado em toda a disciplina, e pede a identificação do que a instituição quer, quem decide e quais restrições chegam fechadas ao arquiteto. O produto desse exercício é uma leitura estruturada do contexto de decisão, sem artefato formal que alimente o bloco seguinte.

O [bloco 2](bloco-2-qualidade-e-tipos-de-requisito.md) expõe o conceito de qualidade em software e distingue requisito funcional, requisito não funcional, requisito de atributo de qualidade e restrição. O exercício classifica os requisitos declarados pela ACME nessas quatro categorias e reescreve dois deles em forma mensurável. As reescritas mensuráveis produzidas aqui alimentam o bloco 3, porque um cenário de atributo de qualidade parte de um requisito já expresso de forma verificável.

O [bloco 3](bloco-3-cenarios-e-significancia-arquitetural.md) expõe o formato de seis elementos de um cenário de atributo de qualidade e o julgamento de significância arquitetural. O exercício escreve dois cenários para a ACME, a partir das reescritas do bloco 2, e defende quais deles constituem requisito arquiteturalmente significativo. Os cenários escritos aqui alimentam o bloco 4, que compara estilos contra eles.

O [bloco 4](bloco-4-estilos-arquiteturais.md) expõe o conceito de estilo arquitetural e sua relação com atributo de qualidade. O exercício compara três estilos candidatos contra os cenários escritos no bloco 3, avaliando qual estilo atende melhor a cada cenário.

A [síntese](sintese.md) fecha o módulo com o checklist do que precisa permanecer, a autoavaliação e as fontes da aula inteira.

## Preparação para a Aula 2

A Aula 2, em 23/09/2026, trata de plataforma arquitetural, registro de decisão de arquitetura, representação de modelos e modelagem C4 nos níveis 1 e 2. Os cenários de qualidade e o julgamento de significância arquitetural desta aula são o insumo da Aula 2, porque a escolha de plataforma e a primeira decisão registrada em ADR partem dos requisitos arquiteturalmente significativos identificados aqui. A leitura de estilo arquitetural do bloco 4 também é pré-condição, porque o nível 2 do C4 detalha os componentes internos de um sistema já situado dentro de um estilo escolhido.
