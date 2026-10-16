# Aula 3, princípios de design, padrões e registro de decisão

Ao fim da Aula 2, a ACME tinha em mãos as exigências sobre o novo sistema acadêmico, entre elas a de que a matrícula não pare em período letivo, mas ainda não tinha uma decisão de desenho. Esta aula conduz o aluno desse ponto até uma decisão que ele consegue justificar a outra pessoa, e o caminho tem quatro etapas encadeadas. Primeiro, princípios de design, que são regras de desenho derivadas das exigências, orientam a escolha do estilo arquitetural, que é a forma geral de organizar o sistema. Depois, o estilo delimita os problemas para os quais se selecionam padrões, que são soluções conhecidas para problemas que se repetem. Por fim, o conjunto das escolhas é registrado em um ADR (registro de decisão arquitetural), um texto curto que guarda o que foi decidido, as alternativas descartadas e o motivo.

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

O [bloco 1](bloco-1-principios-de-design.md) começa pela pergunta que a ACME enfrenta ao sair da Aula 2, a de como transformar exigências em regras de desenho. Para respondê-la, ele distingue objetivo, requisito, princípio, decisão e elemento lógico, apresenta a anatomia de um princípio e um repertório de nove princípios, e descreve os cinco passos da passagem do desenho conceitual ao desenho lógico. No exercício 9, o aluno recebe quatro exigências do caso ACME, como a de que o sistema acadêmico não pare durante o período letivo, e oito responsabilidades que a solução precisa cumprir, como registrar a nota lançada pelo professor. Com elas, entrega princípios priorizados e um esboço lógico, que é um primeiro desenho do sistema em elementos com responsabilidades, sem produto nem tecnologia escolhidos.

Com os princípios definidos, a ACME precisa escolher a forma geral do sistema, e o [bloco 2](bloco-2-estilos-arquiteturais.md) compara sete estilos arquiteturais pelos mesmos aspectos, forma estrutural, comunicação, atributos favorecidos e prejudicados, quando usar, quando evitar e anti-padrão, ligando cada estilo aos princípios que ele tende a sustentar. O exercício 10 parte dos princípios do exercício 9 e dos dois cenários de qualidade da Aula 2, o pico de matrícula e o incidente de 04/02/2026. O aluno compara três estilos à sua escolha e entrega uma matriz comparativa com o estilo recomendado.

Escolhido o estilo, restam problemas concretos que ele não resolve sozinho, e o [bloco 3](bloco-3-padroes-arquiteturais-e-de-design.md) organiza os padrões em três níveis de decisão para tratá-los. Ele descreve dez padrões de modernização, integração, resiliência e consistência distribuída pelo problema, pelas forças, pela estrutura, pela consequência, pelo custo e pelo sinal de uso inadequado. O exercício 11 parte do estilo recomendado no exercício 10 e traz três problemas da ACME, a coexistência entre o sistema legado e a solução nova, a proteção contra falha de integração e a publicação confiável de mudança acadêmica, e o aluno entrega um mapa que liga cada problema ao padrão escolhido e à consequência dessa escolha.

Por fim, a decisão precisa sobreviver a quem a tomou, e o [bloco 4](bloco-4-registro-de-decisao-arquitetural.md) trata do racional arquitetural, da abordagem leve de registro, dos formatos Nygard e MADR e do template de dez campos adotado pela disciplina, com critério de qualidade e erro frequente de cada campo. No exercício 12, o aluno reúne os produtos dos exercícios 9 a 11 e entrega o ADR, um documento curto com dez campos, que registra o estilo e os padrões escolhidos e o motivo de cada escolha.

A [síntese](sintese.md) fecha o módulo com o checklist do que precisa permanecer, a cadeia da decisão construída na aula, a autoavaliação e as fontes da aula inteira.

## Adições no Caderno Arquitetural da Aula 3

A Aula 2 deixou o caderno com os requisitos, os cenários de qualidade e as restrições da ACME, e agora é hora de usá-los para desenhar. Os quatro exercícios desta aula preenchem a seção 6, Princípios, e abrem a seção 7, Decisões, porque o desenho nasce das regras e termina numa escolha registrada. A seção 6 recebe os princípios e o esboço lógico do exercício 9, e a seção 7 acumula a comparação de estilos (10), os padrões para os três problemas (11) e o ADR do estilo (12). O caderno que sai da Aula 3 é o do [gabarito do exercício 12](../gabaritos/gabarito-exercicio-12.md).

{{trilha:7:3}}

| Bloco | Exercício | O que entra no caderno | Gabarito |
| --- | --- | --- | --- |
| 1 | 9 | Quatro princípios de design em ordem de prioridade e o esboço lógico com cinco elementos para as oito responsabilidades (RS1 a RS8), com um risco e uma decisão pendente | [Gabarito 9](../gabaritos/gabarito-exercicio-09.md) |
| 2 | 10 | A comparação de três estilos diante dos dois cenários de qualidade, com risco, mecanismo compensatório e o estilo recomendado | [Gabarito 10](../gabaritos/gabarito-exercicio-10.md) |
| 3 | 11 | Um padrão para cada um dos três problemas da ACME, com nível, elemento afetado, consequência favorável, custo aceito e os padrões descartados | [Gabarito 11](../gabaritos/gabarito-exercicio-11.md) |
| 4 | 12 | O ADR do estilo e dos padrões, nos dez campos do modelo, com estado proposta | [Gabarito 12](../gabaritos/gabarito-exercicio-12.md) |

## Preparação para a Aula 4

A Aula 4 detalha a solução nos domínios de negócio, dados, aplicações e infraestrutura. Ela parte da declaração de escopo do exercício 8, do esboço lógico do exercício 9, dos padrões do exercício 11 e do ADR do exercício 12, e termina na representação da arquitetura alvo em modelos C4, uma notação de diagramas em quatro níveis de detalhe, dos quais a aula usa os de contexto e de contêineres. As escolhas de produto, framework e plataforma continuam fora de escopo até a Aula 5, e o [cronograma](../cronograma.md) traz a sequência completa das seis aulas.
