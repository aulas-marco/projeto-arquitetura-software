# Aula 2, plataforma e modelos

A aula responde à seguinte questão: como registrar uma decisão arquitetural de forma rastreável, e como escolher e representar a plataforma que sustenta o estilo já decidido.

## Objetivos de aprendizagem

Ao final da aula, o aluno é capaz de

- registrar uma decisão arquitetural em formato de ADR, citando contexto, decisão e consequências
- comparar plataformas candidatas para um estilo arquitetural já escolhido, a partir de critérios explícitos
- justificar a escolha de uma plataforma diante do estilo e dos requisitos já definidos
- modelar um sistema nos níveis de contexto e de contêineres do C4

## Grade de tempo

A aula ocorre das 19h00 às 22h30, com intervalo das 20h30 às 20h45. O tempo de conteúdo encerra até as 22h10. Os quatro blocos abaixo são o único lugar do site em que os minutos aparecem. As páginas de cada bloco não exibem cronômetro.

| Bloco | Conceito | Conceito (min) | Exercício (min) |
| --- | --- | --- | --- |
| 1 | Registro de decisão arquitetural, ADR, formatos de Nygard e MADR | 25 | 15 |
| 2 | Plataforma arquitetural e sua relação com o estilo já escolhido | 25 | 15 |
| 3 | ADR de plataforma | 25 | 15 |
| 4 | Representação de modelos e C4, níveis de contexto e de contêineres | 25 | 15 |

Os quatro blocos somam 160 minutos. Os 15 minutos restantes do tempo útil de 175 minutos cobrem abertura, transições e fechamento.

## Roteiro da aula

O [bloco 1](bloco-1-registro-de-decisao-arquitetural.md) expõe o conceito de registro de decisão arquitetural, o ADR, nos formatos de Nygard e de MADR. O exercício 5 desse bloco escreve o ADR que registra a escolha de estilo arquitetural já feita no exercício do [bloco 4 da Aula 1](../modulo-1-fundamentos/bloco-4-estilos-arquiteturais.md), sem introduzir extrato novo do caso. O produto desse exercício é um ADR completo sobre uma decisão que o aluno já tomou, o que libera o tempo do exercício para praticar o formato, não para reler dado do caso.

O [bloco 2](bloco-2-plataforma-arquitetural.md) expõe o conceito de plataforma arquitetural e sua relação com o estilo já escolhido. O exercício 6 compara plataformas candidatas para o estilo escolhido na Aula 1, a partir de critérios explícitos apresentados no Conceito desse bloco. A comparação produzida aqui alimenta o [bloco 3](bloco-3-adr-de-plataforma.md), porque o ADR de plataforma parte de uma escolha entre alternativas já justificada.

O [bloco 3](bloco-3-adr-de-plataforma.md) repete a prática de registrar uma decisão em formato de ADR, desta vez sobre a escolha de plataforma. O exercício 7 escreve o ADR que registra a escolha de plataforma feita no [exercício 6 do bloco 2](bloco-2-plataforma-arquitetural.md) desta aula, dando ao aluno uma segunda oportunidade de praticar o formato em contexto diferente do [bloco 1](bloco-1-registro-de-decisao-arquitetural.md).

O [bloco 4](bloco-4-representacao-de-modelos-e-c4.md) expõe a representação de modelos arquiteturais e o modelo C4, restrito aos níveis de contexto e de contêineres. O exercício 8 modela a ACME nesses dois níveis, a partir do estilo e da plataforma já decididos nos blocos anteriores desta aula.

A [síntese](sintese.md) fecha o módulo com o checklist do que precisa permanecer, a autoavaliação e as fontes da aula inteira.

## Preparação para a Aula 3

A Aula 3 trata de descoberta de requisitos e de riscos arquiteturais. A ADR e o modelo C4 produzidos nesta aula são o insumo dela, porque a avaliação de risco parte de uma decisão já registrada e de um modelo já desenhado, não de uma arquitetura ainda implícita na cabeça do arquiteto.
