# Aula 2, entradas do processo, requisitos e partes interessadas

Antes de propor qualquer alternativa, o arquiteto da ACME precisa saber o que pressiona a universidade, o que se exige do sistema e quem tem interesse legítimo no resultado. A aula corresponde à fase de descoberta do processo apresentado na Aula 1 e responde à questão de o que entra no desenho de uma solução antes que qualquer alternativa seja proposta, e de quem tem interesse legítimo no resultado.

## Objetivos de aprendizagem

Ao final da aula, o aluno é capaz de

- diferenciar direcionador de mudança interno de externo e identificar ambos em um caso concreto
- diferenciar requisito funcional, requisito não funcional, requisito de atributo de qualidade e restrição
- converter uma declaração que chegou rotulada como não funcional em requisito de atributo de qualidade ou em restrição, que são as categorias com que o arquiteto trabalha
- escrever um cenário de atributo de qualidade no formato de seis elementos
- justificar, para um requisito dado, se ele constitui um requisito arquiteturalmente significativo
- identificar artefatos de linha de base e classificar restrições pela origem
- classificar partes interessadas por categoria e definir pontos de vista adequados às suas preocupações

## Grade de tempo

A aula ocorre das 19h00 às 22h30, com intervalo das 20h30 às 20h45, e o tempo de conteúdo encerra até as 22h10. Todo o tempo de aula é destinado à apresentação conceitual dos quatro blocos, e os exercícios são realizados fora do horário de aula. A tabela abaixo é o único lugar do site em que os minutos de cada bloco aparecem, porque as páginas de bloco não exibem cronômetro.

| Bloco | Conceito | Apresentação (min) |
| --- | --- | --- |
| 1 | Direcionadores de mudança, internos e externos | 40 |
| 2 | Qualidade e tipos de requisito | 40 |
| 3 | Cenários de qualidade, linha de base e restrições | 40 |
| 4 | Partes interessadas, pontos de vista e escopo | 40 |

Os quatro blocos somam 160 minutos. Os 15 minutos restantes do tempo útil de 175 minutos cobrem abertura, transições e fechamento.

## Roteiro da aula

A aula começa pelo [bloco 1](bloco-1-direcionadores-de-mudanca.md), que trata do que põe a solução em movimento, com as três fontes internas, estratégia de negócio, estratégia de TI e análise de negócio, e os direcionadores externos, tratados pela análise PESTLE. O exercício classifica os sete direcionadores do caso da instituição fictícia ACME, uma universidade que moderniza seu sistema acadêmico, em reativos e antecipatórios e aplica ao caso a análise PESTLE, uma lista de seis dimensões do ambiente externo.

Em seguida, o [bloco 2](bloco-2-qualidade-e-tipos-de-requisito.md) distingue requisito funcional, requisito não funcional, requisito de atributo de qualidade e restrição, mostrando que o rótulo não funcional serve apenas como ponto de partida do trabalho. Apresenta também as doze dimensões de preocupação que servem de lista de verificação contra omissão no levantamento. O exercício classifica oito declarações das partes interessadas da ACME nas três categorias de trabalho e completa contexto, carga e medida de duas delas, em reescritas mensuráveis que alimentam o bloco 3.

Com os requisitos classificados, o [bloco 3](bloco-3-cenarios-linha-de-base-e-restricoes.md) apresenta o formato de seis elementos de um cenário de atributo de qualidade, o julgamento de significância arquitetural, os artefatos de linha de base e a classificação de restrições pela origem. O exercício completa dois cenários da ACME, um sobre o pico de matrícula e outro sobre o incidente de 04/02/2026, defende a significância arquitetural de cada um e identifica os insumos já existentes no caso, como o inventário de componentes e as restrições fechadas. Os cenários escritos aqui são a entrada da comparação de estilos da Aula 3.

Por fim, o [bloco 4](bloco-4-partes-interessadas-e-pontos-de-vista.md) trata das categorias de parte interessada, dos quatro motivos de comunicação, do registro de preocupações, da distinção entre ponto de vista e visão, e da declaração de escopo por componentes da solução. O exercício classifica os oito papéis do mapa de atores da ACME, como a Reitora e o Diretor de TI, aponta as categorias de parte interessada sem representante, preenche pontos de vista para três papéis e marca, em dez elementos do sistema, o que muda e o que permanece no primeiro ciclo de 12 meses.

A [síntese](sintese.md) fecha o módulo com o checklist do que precisa permanecer, a autoavaliação e as fontes da aula inteira.

## O que a Aula 2 constrói no caderno

Na Aula 1 o caderno ganhou a seção 1, Contexto, com as restrições, as decisões, os componentes da solução e as tarefas do projeto. A Aula 2 parte dessa base, porque as restrições dizem o que já está decidido e as decisões dizem quem precisa ser ouvido, e acrescenta o que o arquiteto descobre antes de desenhar: as pressões que levaram à mudança, os requisitos e cenários de qualidade, o ponto de partida do sistema e as partes interessadas com o escopo do primeiro ciclo. O caderno que sai da Aula 2 é o do [gabarito do exercício 8](../gabaritos/gabarito-exercicio-08.md).

{{trilha:3}}

| Bloco | Exercício | O que entra no caderno | Gabarito |
| --- | --- | --- | --- |
| 1 | 5 | A resposta da ACME a cada um dos sete direcionadores de mudança, os fatores externos pelas seis dimensões da análise PESTLE e o efeito do contrato do mainframe na meta de custo, na seção 3 | [Gabarito 5](../gabaritos/gabarito-exercicio-05.md) |
| 2 | 6 | A categoria das oito declarações de requisito (R2 a R13) e as reescritas mensuráveis de duas delas, na seção 3 | [Gabarito 6](../gabaritos/gabarito-exercicio-06.md) |
| 3 | 7 | Os dois cenários de qualidade com o julgamento de significância e a origem das sete restrições, na seção 3, e os quatro artefatos de linha de base que os sustentam, na seção 4 | [Gabarito 7](../gabaritos/gabarito-exercicio-07.md) |
| 4 | 8 | A categoria dos oito papéis do mapa de atores, os pontos de vista de três deles e a declaração de escopo dos dez elementos (E1 a E10), na seção 2 | [Gabarito 8](../gabaritos/gabarito-exercicio-08.md) |

## Preparação para a Aula 3

A Aula 3 trata de princípios de design, estilos e padrões arquiteturais e do registro de decisão em ADR. Os cenários de qualidade e o julgamento de significância desta aula são o insumo direto daquela, porque estilo se compara contra exigência medida, e a primeira decisão registrada em ADR é a escolha de estilo. A declaração de escopo produzida no bloco 4 delimita sobre que parte do sistema essa escolha incide.
