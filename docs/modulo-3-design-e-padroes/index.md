# Aula 3, princípios de design, padrões e registro de decisão

A aula conduz o aluno das exigências levantadas na Aula 2 até uma decisão de desenho que pode ser justificada a outra pessoa. A decisão é construída em quatro etapas encadeadas. Primeiro, princípios de design, que são regras de desenho derivadas das exigências, orientam a escolha do estilo arquitetural, que é a forma geral de organizar o sistema. Depois, o estilo delimita os problemas para os quais se selecionam padrões, que são soluções conhecidas para problemas que se repetem. Por fim, o conjunto das escolhas é registrado em um ADR (registro de decisão arquitetural), um texto curto que guarda o que foi decidido, as alternativas descartadas e o motivo.

## Objetivos de aprendizagem

Ao final da aula, o aluno é capaz de

- converter requisitos, atributos de qualidade (como desempenho e disponibilidade) e restrições em princípios de design, cada um com motivação, implicação e evidência
- distinguir desenho conceitual de desenho lógico e produzir um esboço lógico sem compromisso com tecnologia
- comparar estilos arquiteturais por forças, riscos e compromissos diante de cenários de qualidade
- distinguir estilo arquitetural, padrão arquitetural e padrão de design pelo alcance da decisão
- selecionar padrões em função de um problema e de um contexto, declarando o custo aceito
- registrar contexto, alternativas, decisão, consequências, evidências e revisão em um ADR

## Grade de tempo

A aula ocorre das 19h00 às 22h30, com intervalo das 20h30 às 20h45, e o tempo de conteúdo encerra até as 22h10. O tempo de aula é dividido entre a apresentação dos quatro blocos, as questões sobre a aula anterior e três questionários Kahoot, e os exercícios são realizados fora do horário de aula. Os minutos de cada bloco aparecem somente na tabela abaixo, porque as páginas de bloco não exibem cronômetro.

| Horário | Atividade | Duração (min) |
| --- | --- | --- |
| 19h00–19h15 | Questões sobre a Aula 2 | 15 |
| 19h15–19h25 | Kahoot de revisão da Aula 2 | 10 |
| 19h25–19h58 | Bloco 1, princípios de design e passagem do conceitual ao lógico | 33 |
| 19h58–20h30 | Bloco 2, estilos arquiteturais, forças e compromissos | 32 |
| 20h30–20h45 | Intervalo | 15 |
| 20h45–20h55 | Kahoot dos blocos 1 e 2 | 10 |
| 20h55–21h28 | Bloco 3, padrões arquiteturais e padrões de design | 33 |
| 21h28–22h00 | Bloco 4, registro de decisão arquitetural | 32 |
| 22h00–22h10 | Kahoot dos blocos 3 e 4 | 10 |

Os quatro blocos somam 130 minutos de apresentação conceitual, e os três questionários e as questões iniciais ocupam os 45 minutos restantes do tempo útil de 175 minutos.

## Entrada recebida da Aula 2

A aula parte de quatro produtos da Aula 2, todos aplicados à ACME, a universidade privada fictícia que serve de caso à disciplina. A classificação de requisitos do [bloco 2](../modulo-2-requisitos-e-partes-interessadas/bloco-2-qualidade-e-tipos-de-requisito.md) separa o que o sistema deve fazer, o que ele deve atingir em qualidade e o que já vem imposto. Os dois cenários de qualidade do [bloco 3](../modulo-2-requisitos-e-partes-interessadas/bloco-3-cenarios-linha-de-base-e-restricoes.md) descrevem uma situação com medida a cumprir, e os estilos são comparados contra essa medida. O primeiro cenário trata do pico de acessos na abertura da matrícula, e o segundo trata do incidente de 04/02/2026, em que sessões abandonadas esgotaram a capacidade do núcleo do sistema e deixaram a matrícula indisponível por 4h20. As restrições classificadas no mesmo bloco já vêm impostas e eliminam alternativas antes da análise. A declaração de escopo do [bloco 4](../modulo-2-requisitos-e-partes-interessadas/bloco-4-partes-interessadas-e-pontos-de-vista.md) delimita a parte do sistema sobre a qual as decisões desta aula incidem.

## Roteiro da aula

O [bloco 1](bloco-1-principios-de-design.md) distingue objetivo, requisito, princípio, decisão e elemento lógico, apresenta a anatomia de um princípio e um repertório de nove princípios, e descreve os cinco passos da passagem do desenho conceitual ao desenho lógico. O exercício 9 fornece quatro exigências do caso ACME, como a de que o sistema acadêmico não pare durante o período letivo, e oito responsabilidades que a solução precisa cumprir, como registrar a nota lançada pelo professor. O aluno entrega princípios priorizados e um esboço lógico, que é um primeiro desenho do sistema em elementos com responsabilidades, sem produto nem tecnologia escolhidos.

O [bloco 2](bloco-2-estilos-arquiteturais.md) compara sete estilos arquiteturais pelos mesmos aspectos, forma estrutural, comunicação, atributos favorecidos e prejudicados, quando usar, quando evitar e anti-padrão, e liga cada estilo aos princípios que ele tende a sustentar. O exercício 10 parte dos princípios do exercício 9 e dos dois cenários de qualidade da Aula 2, o pico de matrícula e o incidente de 04/02/2026. O aluno compara três estilos à sua escolha e entrega uma matriz comparativa com o estilo recomendado.

O [bloco 3](bloco-3-padroes-arquiteturais-e-de-design.md) organiza os padrões em três níveis de decisão e descreve dez padrões de modernização, integração, resiliência e consistência distribuída pelo problema, pelas forças, pela estrutura, pela consequência, pelo custo e pelo sinal de uso inadequado. O exercício 11 parte do estilo recomendado no exercício 10. O enunciado descreve três problemas da ACME, a coexistência entre o sistema legado e a solução nova, a proteção contra falha de integração e a publicação confiável de mudança acadêmica, e o aluno entrega um mapa que liga cada problema ao padrão escolhido e à consequência dessa escolha.

O [bloco 4](bloco-4-registro-de-decisao-arquitetural.md) trata do racional arquitetural, da abordagem leve de registro, dos formatos Nygard e MADR e do template de dez campos adotado pela disciplina, com critério de qualidade e erro frequente de cada campo. O exercício 12 reúne os produtos dos exercícios 9 a 11, e o aluno entrega o ADR, um documento curto com dez campos, que registra o estilo e os padrões escolhidos e o motivo de cada escolha.

A [síntese](sintese.md) fecha o módulo com o checklist do que precisa permanecer, a cadeia da decisão construída na aula, a autoavaliação e as fontes da aula inteira.

## Preparação para a Aula 4

A Aula 4 detalha a solução nos domínios de negócio, dados, aplicações e infraestrutura. Ela parte da declaração de escopo do exercício 8, do esboço lógico do exercício 9, dos padrões do exercício 11 e do ADR do exercício 12, e termina na representação da arquitetura alvo em modelos C4, uma notação de diagramas em quatro níveis de detalhe, dos quais a aula usa os de contexto e de contêineres. As escolhas de produto, framework e plataforma continuam fora de escopo até a Aula 5, e o [cronograma](../cronograma.md) traz a sequência completa das seis aulas.
