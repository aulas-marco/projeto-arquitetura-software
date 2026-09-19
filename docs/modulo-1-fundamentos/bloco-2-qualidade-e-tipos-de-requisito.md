# Qualidade em software e os tipos de requisito

Este bloco responde a uma pergunta que antecede qualquer especificação de sistema, o que se quer dizer com qualidade em software e como essa noção se traduz em requisito passível de análise e verificação.

## Antes de começar

- [Atributo de qualidade](../referencia/glossario.md#atributo-de-qualidade)
- [Requisito funcional](../referencia/glossario.md#requisito-funcional)
- [Requisito não funcional](../referencia/glossario.md#requisito-nao-funcional)
- [Requisito de atributo de qualidade](../referencia/glossario.md#requisito-de-atributo-de-qualidade)

## Conceito

Em linguagem cotidiana, qualidade costuma significar que alguma coisa é boa. Em engenharia de software essa formulação é insuficiente, porque sistemas diferentes precisam ser bons de maneiras diferentes. Um aplicativo bancário precisa proteger dados e transações. Um sistema hospitalar precisa permanecer disponível mesmo em condições adversas, porque uma indisponibilidade de cinco minutos, tolerável em um portal institucional, pode ser inaceitável em um sistema de controle hospitalar. Segurança e disponibilidade são aspectos diferentes da qualidade, e nenhum dos dois sozinho descreve o outro. Por isso a qualidade de um sistema não deve ser tratada como uma propriedade única, ela é observada por meio de diversas características. A ISO/IEC 25010 apresenta um modelo de qualidade composto por características e subcaracterísticas, usado como referência para especificar, medir e avaliar propriedades de produtos de TIC e software.

Um **atributo de qualidade** é uma propriedade ou dimensão pela qual o comportamento ou a estrutura de um sistema pode ser observado e avaliado. Entre os exemplos mais comuns estão o desempenho, com que rapidez e capacidade o sistema realiza seu trabalho, a disponibilidade, por quanto tempo e em quais condições o serviço permanece acessível, a confiabilidade, com que consistência o sistema executa corretamente suas funções, a segurança, como o sistema protege informações, operações e recursos, a usabilidade, com que eficácia as pessoas conseguem utilizar o produto, e a modificabilidade, com que esforço o sistema pode ser alterado. Esses termos nomeiam aspectos da qualidade, mas ainda não dizem quanto de cada qualidade é necessário. Desempenho é um atributo, segurança também é um atributo, e nenhum dos dois, isoladamente, constitui um requisito completo. Duas organizações podem considerar o mesmo atributo relevante e, ainda assim, necessitar de comportamentos muito diferentes, como no contraste entre o portal institucional e o sistema hospitalar citado acima.

Um **requisito** expressa uma necessidade, capacidade, condição ou restrição que o sistema deve satisfazer, transformando expectativas gerais em algo que possa ser analisado, negociado, implementado e verificado. Dizer que um aplicativo bancário deve permitir consultar o saldo descreve uma capacidade funcional. Dizer que esse mesmo aplicativo deve utilizar o provedor corporativo de identidade estabelece uma restrição. Requisitos podem, portanto, tratar do que o sistema faz, das condições sob as quais opera ou dos limites que devem ser respeitados.

Muitos alunos aprendem inicialmente a dividir requisitos em dois grupos, os **requisitos funcionais**, que descrevem serviços, comportamentos ou capacidades que o sistema deve oferecer, e os **requisitos não funcionais**, que descrevem qualidades, condições, limites ou restrições associados ao funcionamento do sistema. Nesse vocabulário, requisitos de desempenho, disponibilidade, segurança, usabilidade e modificabilidade normalmente são classificados como não funcionais, como mostra o quadro abaixo.

| Requisito | Classificação inicial |
| --- | --- |
| O cliente deve conseguir consultar seu saldo | Requisito funcional, descreve uma capacidade |
| 95% das consultas de saldo devem responder em até 500 ms | Requisito não funcional de desempenho |
| O serviço deve permanecer disponível durante pelo menos 99,95% de cada mês | Requisito não funcional de disponibilidade |

Essa divisão em dois grupos é útil como introdução, mas a expressão não funcional é muito ampla. Ela informa principalmente que o requisito não descreve uma função de negócio, sem esclarecer qual propriedade de qualidade está em jogo, em que situação ela deve ser observada ou como será medida. É comum, além disso, colocar restrições dentro do conjunto dos requisitos não funcionais. Dizer que um sistema hospitalar deve usar determinado padrão de banco de dados não descreve uma função nem uma qualidade desejada, estabelece uma escolha tecnológica obrigatória. Por essa razão requisito não funcional e requisito de atributo de qualidade não devem ser tratados como termos equivalentes, e o quadro a seguir posiciona os quatro conceitos que interessam a este bloco.

| Conceito | Papel |
| --- | --- |
| Requisito funcional | Especifica uma capacidade ou comportamento oferecido pelo sistema |
| Requisito não funcional | Categoria ampla tradicional para qualidades, condições e, em algumas classificações, restrições |
| Requisito de atributo de qualidade | Especifica de modo contextualizado e verificável uma expectativa sobre uma qualidade |
| Restrição | Limita as alternativas possíveis, como tecnologia, plataforma, norma ou localização |

Um **requisito de atributo de qualidade** declara o comportamento esperado do sistema em relação a uma característica de qualidade, respondendo a uma pergunta mais concreta, que nível de desempenho, disponibilidade ou segurança é necessário, em determinada situação. O quadro seguinte contrasta três formulações sucessivas sobre desempenho, aplicadas a uma plataforma de vídeo.

| Formulação | O que ela informa |
| --- | --- |
| O sistema deve ser rápido | Apenas uma intenção geral. Não há critério de verificação |
| As consultas devem responder em até 500 ms | Há uma medida, mas não se sabe para qual carga ou parcela das consultas |
| Durante o pico mensal de 2.000 requisições por segundo, 95% das consultas autenticadas devem responder em até 500 ms e 99% em até 1 segundo | Há contexto, carga e medidas que podem orientar análise e testes |

Somente a terceira formulação fornece informação suficiente para orientar decisões com razoável precisão. O nome do atributo indica o que importa, o requisito descreve o que se espera que aconteça. O mesmo raciocínio vale para segurança. Dizer que um sistema deve ser seguro não informa quais ativos devem ser protegidos, contra quais ameaças, em qual ambiente e com que resposta. Uma formulação mais útil, aplicada a um sistema hospitalar, seria a seguinte. Quando cinco tentativas inválidas de autenticação forem realizadas para a mesma conta em até dez minutos, o serviço de identidade deverá bloquear novas tentativas por quinze minutos, registrar o evento e notificar o usuário em até um minuto. Nessa formulação existe um evento observável, uma parte afetada do sistema, uma resposta esperada e medidas de tempo.

## Uso pelo arquiteto

O arquiteto separa requisito não funcional de requisito de atributo de qualidade porque a especificação de um sistema precisa de critério verificável, não de rótulo. Um requisito arquivado apenas como não funcional de desempenho ou de disponibilidade ainda não diz o que testar, o que priorizar diante de conflito entre qualidades, nem quando considerar o requisito satisfeito. Reescrever a expectativa como requisito de atributo de qualidade, com contexto, carga e medida, é o que permite negociar prazo, orçar esforço e decidir entre soluções concorrentes com base em evidência, e não em impressão.

## Exercício 2

A ACME, universidade privada brasileira cujo sistema acadêmico está em modernização, levantou os requisitos abaixo em entrevistas com as partes interessadas, sem depuração editorial.

| Código | Declaração |
| --- | --- |
| R2 | A matrícula não pode cair |
| R3 | O tempo de resposta precisa ser bom |
| R4 | A solução opera em um dos dois provedores de nuvem aprovados em 12/03/2026 |
| R5 | O sistema emite histórico escolar com assinatura digital no padrão ICP-Brasil |
| R6 | O portal sustenta 5.800 sessões simultâneas na abertura da matrícula, com percentil 95 do tempo de confirmação em até 4 segundos |
| R10 | A manutenção dos programas COBOL do núcleo permanece sob o contrato da fábrica até 30/09/2027 |
| R11 | O sistema precisa ser moderno e escalável |
| R13 | O aluno consulta o resultado da solicitação de aproveitamento de disciplina pelo portal |

1. Classifique cada um dos oito requisitos em uma das quatro categorias, requisito funcional, requisito não funcional, requisito de atributo de qualidade ou restrição, justificando em uma frase.
2. Escolha dois requisitos que sejam requisitos de atributo de qualidade mal formulados e reescreva cada um em forma mensurável, seguindo o padrão de contexto, carga e medida usado no exemplo de desempenho da plataforma de vídeo, apresentado na seção Conceito acima.

## Fontes

Glossário do curso, entradas [atributo de qualidade](../referencia/glossario.md#atributo-de-qualidade), [requisito funcional](../referencia/glossario.md#requisito-funcional), [requisito não funcional](../referencia/glossario.md#requisito-nao-funcional) e [requisito de atributo de qualidade](../referencia/glossario.md#requisito-de-atributo-de-qualidade). ISO/IEC/IEEE 42010:2022. ISO/IEC 25010. CMU/SEI-2003-TR-016, Quality Attribute Workshops (QAWs), Third Edition, Barbacci e outros, Software Engineering Institute, Carnegie Mellon University. Dossiê da instituição fictícia [ACME](../caso-acme/index.md), requisitos declarados pelas partes interessadas.
