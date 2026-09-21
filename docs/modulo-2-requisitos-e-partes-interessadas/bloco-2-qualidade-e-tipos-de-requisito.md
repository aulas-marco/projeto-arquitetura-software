# Qualidade em software e os tipos de requisito

Este bloco responde a uma pergunta que antecede qualquer especificação de sistema, o que se quer dizer com qualidade em software e como essa noção se traduz em requisito passível de análise e verificação.

## Antes de começar

- [Atributo de qualidade](../referencia/glossario.md#atributo-de-qualidade)
- [Requisito funcional](../referencia/glossario.md#requisito-funcional)
- [Requisito não funcional](../referencia/glossario.md#requisito-nao-funcional)
- [Requisito de atributo de qualidade](../referencia/glossario.md#requisito-de-atributo-de-qualidade)

## Conceito

Em linguagem cotidiana, qualidade costuma significar que alguma coisa é boa. Em engenharia de software essa formulação é insuficiente, porque sistemas diferentes precisam ser bons de maneiras diferentes. Um aplicativo bancário precisa proteger dados e transações. Um sistema hospitalar precisa permanecer disponível mesmo em condições adversas, porque uma indisponibilidade de cinco minutos, tolerável em um portal institucional, pode ser inaceitável em um sistema de controle hospitalar. Segurança e disponibilidade são aspectos diferentes da qualidade, e nenhum dos dois sozinho descreve o outro. Por isso a qualidade de um sistema não deve ser tratada como uma propriedade única, ela é observada por meio de diversas características. A ISO/IEC 25010 apresenta um modelo de qualidade composto por características e subcaracterísticas, usado como referência para especificar, medir e avaliar propriedades de produtos de TIC e software.

Um **atributo de qualidade** é uma propriedade ou dimensão pela qual o comportamento ou a estrutura de um sistema pode ser observado e avaliado. Entre os exemplos mais comuns estão o desempenho, com que rapidez e capacidade o sistema realiza seu trabalho, a disponibilidade, por quanto tempo e em quais condições o serviço permanece acessível, a confiabilidade, com que consistência o sistema executa corretamente suas funções, a segurança, como o sistema protege informações, operações e recursos, a usabilidade, com que eficácia as pessoas conseguem utilizar o produto, e a modificabilidade, com que esforço o sistema pode ser alterado. Esses termos nomeiam aspectos da qualidade, mas ainda não dizem quanto de cada qualidade é necessário. Desempenho é um atributo, segurança também é um atributo, e nenhum dos dois, isoladamente, constitui um requisito completo. Duas organizações podem considerar o mesmo atributo relevante e, ainda assim, necessitar de comportamentos muito diferentes, como no contraste entre o portal institucional e o sistema hospitalar apresentado no parágrafo de abertura desta seção Conceito.

Um **requisito** expressa uma necessidade, capacidade, condição ou restrição que o sistema deve satisfazer, transformando expectativas gerais em algo que possa ser analisado, negociado, implementado e verificado. Dizer que um aplicativo bancário deve permitir consultar o saldo descreve uma capacidade funcional. Dizer que esse mesmo aplicativo deve utilizar o provedor corporativo de identidade estabelece uma restrição. Requisitos podem, portanto, tratar do que o sistema faz, das condições sob as quais opera ou dos limites que devem ser respeitados.

Muitos alunos aprendem inicialmente a dividir requisitos em dois grupos, os **requisitos funcionais**, que descrevem serviços, comportamentos ou capacidades que o sistema deve oferecer, e os **requisitos não funcionais**, que descrevem qualidades, condições, limites ou restrições associados ao funcionamento do sistema. Nesse vocabulário, requisitos de desempenho, disponibilidade, segurança, usabilidade e modificabilidade normalmente são classificados como não funcionais, como mostra o quadro abaixo.

| Requisito | Classificação inicial |
| --- | --- |
| O cliente deve conseguir consultar seu saldo | Requisito funcional, descreve uma capacidade |
| 95% das consultas de saldo devem responder em até 500 ms | Requisito não funcional de desempenho |
| O serviço deve permanecer disponível durante pelo menos 99,95% de cada mês | Requisito não funcional de disponibilidade |

Essa divisão em dois grupos é útil como introdução, mas a expressão não funcional é muito ampla. Ela informa principalmente que o requisito não descreve uma função de negócio, sem esclarecer qual propriedade de qualidade está em jogo, em que situação ela deve ser observada ou como será medida. É comum, além disso, colocar restrições dentro do conjunto dos requisitos não funcionais. Dizer que um sistema hospitalar deve usar determinado padrão de banco de dados não descreve uma função nem uma qualidade desejada, estabelece uma escolha tecnológica obrigatória. Por essa razão requisito não funcional e requisito de atributo de qualidade não devem ser tratados como termos equivalentes, e o quadro a seguir posiciona os quatro termos que circulam nessa discussão.

| Termo | Papel |
| --- | --- |
| Requisito funcional | Especifica uma capacidade ou comportamento oferecido pelo sistema |
| Requisito não funcional | Categoria ampla tradicional para qualidades, condições e, em algumas classificações, restrições |
| Requisito de atributo de qualidade | Especifica de modo contextualizado e verificável uma expectativa sobre uma qualidade |
| Restrição | Limita as alternativas possíveis, como tecnologia, plataforma, norma ou localização |

Dos quatro termos, apenas três servem para classificar. Requisito não funcional é o rótulo com que o aluno chega e com que as partes interessadas falam, e por isso precisa ser reconhecido, mas ele é ponto de partida do trabalho e não resultado dele. Dizer que um requisito é não funcional não permite testá-lo, priorizá-lo nem saber quando foi atendido. O trabalho consiste justamente em pegar o que chegou com esse rótulo e decidir o que aquilo é de fato, um requisito de atributo de qualidade, que precisa ganhar contexto, carga e medida para virar verificável, ou uma restrição, que fecha alternativas e não se negocia por medida nenhuma. É essa conversão que transforma uma expectativa vaga em instrumento de decisão.

Um **requisito de atributo de qualidade** declara o comportamento esperado do sistema em relação a uma característica de qualidade, respondendo a uma pergunta mais concreta, que nível de desempenho, disponibilidade ou segurança é necessário, em determinada situação. O quadro seguinte contrasta três formulações sucessivas sobre desempenho, aplicadas a uma plataforma de vídeo.

| Formulação | O que ela informa |
| --- | --- |
| O sistema deve ser rápido | Apenas uma intenção geral. Não há critério de verificação |
| As consultas devem responder em até 500 ms | Há uma medida, mas não se sabe para qual carga ou parcela das consultas |
| Durante o pico mensal de 2.000 requisições por segundo, 95% das consultas autenticadas devem responder em até 500 ms e 99% em até 1 segundo | Há contexto, carga e medidas que podem orientar análise e testes |

Somente a terceira formulação fornece informação suficiente para orientar decisões com razoável precisão. O nome do atributo indica o que importa, o requisito descreve o que se espera que aconteça. O mesmo raciocínio vale para segurança. Dizer que um sistema deve ser seguro não informa quais ativos devem ser protegidos, contra quais ameaças, em qual ambiente e com que resposta. Uma formulação mais útil, aplicada a um sistema hospitalar, seria a seguinte. Quando cinco tentativas inválidas de autenticação forem realizadas para a mesma conta em até dez minutos, o serviço de identidade deverá bloquear novas tentativas por quinze minutos, registrar o evento e notificar o usuário em até um minuto. Nessa formulação existe um evento observável, uma parte afetada do sistema, uma resposta esperada e medidas de tempo.

### Doze dimensões de preocupação arquitetural

A classificação acima responde a uma pergunta sobre natureza, se aquela declaração é função, qualidade ou restrição. Existe um segundo eixo, complementar, que responde a outra pergunta, sobre qual dimensão de preocupação a declaração toca. Ele não substitui o primeiro e não serve para classificar. A função dele é reduzir omissão, porque na entrevista com as partes interessadas o risco maior não é classificar errado, é não perguntar. Percorrer as doze dimensões antes de encerrar o levantamento torna explícito o que influencia a arquitetura e que ninguém levantou espontaneamente.

| Dimensão | O que ela cobra da estrutura | Exemplo |
| --- | --- | --- |
| Funcionalidade arquitetural | Componentes transversais, serviços compartilhados ou infraestrutura especializada para funções que não cabem numa regra de negócio isolada | Auditoria e rastreabilidade, que exige armazenamento estruturado de eventos, correlação de registros e política de retenção |
| Usabilidade | Escolha de framework de interface, estrutura de navegação, estratégia de cache no cliente e telemetria de uso | A aplicação deve atender ao padrão de acessibilidade WCAG nível AA |
| Confiabilidade | Topologia de implantação, replicação de dados, estratégia de cópia de segurança, monitoramento ativo e políticas de nova tentativa | Tempo de recuperação de 15 minutos e perda máxima de dados de 5 minutos |
| Desempenho | Estratégia de cache, balanceamento de carga, modelagem de dados e uso de filas e processamento assíncrono | Latência de percentil 95 abaixo de 200 ms nas operações críticas, com capacidade de absorver carga de dez vezes em campanha |
| Sustentação e evolução | Estrutura de código, estratégia de testes, observabilidade e esteira de entrega contínua | Implantação contínua sem indisponibilidade, por liberação paralela ou gradual |
| Restrições de projeto | A forma estrutural da solução, fechando alternativas antes da análise | Separação obrigatória entre camada de domínio e camada de infraestrutura |
| Restrições de implementação | Limites tecnológicos específicos, que reduzem flexibilidade e podem gerar dependência de fornecedor | A esteira deve gerar inventário de componentes de software e executar análise de vulnerabilidades |
| Interface | Estrutura de APIs, versionamento, compatibilidade retroativa e segurança da integração | APIs em padrão OpenAPI versionado, com autenticação OAuth2 e escopos definidos |
| Físicos e de infraestrutura | Topologia e replicação, por imposição do ambiente onde o sistema executa | Residência obrigatória de dados em território nacional |
| Segurança | Autenticação, autorização, proteção contra ataque, gestão de segredos e conformidade regulatória, com efeito transversal | Criptografia de dados em repouso e em trânsito, com segregação de ambientes por política de acesso |
| Sustentabilidade operacional | Decisões de capacidade e de elasticidade, pelo custo financeiro e ambiental do consumo de recursos | Desligamento automático de ambientes não produtivos fora do horário de uso |
| Inteligência artificial e aprendizado de máquina | Pipeline de dados, armazenamento especializado e monitoramento adicional | Versionamento de modelos, monitoramento de desvio de comportamento em produção e rastreabilidade dos dados de treinamento |

Três observações sobre essa lista. A primeira dimensão é a menos intuitiva, porque funcionalidade costuma ser associada apenas a regra de negócio. Algumas funções, porém, exigem mecanismo estrutural dedicado e por isso são arquiteturalmente significativas. Relatório analítico complexo pode exigir separação entre banco transacional e banco analítico. Fluxo de aprovação demanda modelagem de estados, persistência de histórico e motor de regras. API pública oferecida como produto implica gateway, versionamento, limitação de taxa e monitoramento. Nenhuma dessas é apenas mais uma funcionalidade, todas moldam a estrutura do sistema.

A segunda observação é que as duas últimas dimensões não aparecem nas taxonomias clássicas. Sustentabilidade operacional entrou na lista porque consumo de recurso virou custo relevante e critério de decisão de capacidade. Inteligência artificial entrou porque modelo em produção introduz um objeto que envelhece sozinho, sem que o código mude, o que exige monitoramento de desvio e atualização controlada, coisas que nenhuma dimensão anterior cobre.

A terceira observação é de vocabulário e merece atenção. O material base do professor, de onde vem esta lista, a apresenta como classificação de requisitos, e duas das doze entradas são restrições, de projeto e de implementação. Este bloco não trata restrição como espécie de requisito, trata como conceito vizinho, conforme o quadro anterior. As duas leituras convivem porque os eixos fazem coisas diferentes. O primeiro eixo diz o que a declaração é, e ali restrição se separa de requisito. O segundo diz sobre o que a declaração recai, e ali restrição aparece como dimensão a cobrir na entrevista, como as outras onze, porque esquecer de perguntar sobre tecnologia homologada ou sobre separação obrigatória de camadas custa tão caro quanto esquecer de perguntar sobre desempenho.

## Uso pelo arquiteto

O arquiteto separa requisito não funcional de requisito de atributo de qualidade porque a especificação de um sistema precisa de critério verificável, não de rótulo. Um requisito arquivado apenas como não funcional de desempenho ou de disponibilidade ainda não diz o que testar, o que priorizar diante de conflito entre qualidades, nem quando considerar o requisito satisfeito. Reescrever a expectativa como requisito de atributo de qualidade, com contexto, carga e medida, é o que permite negociar prazo, orçar esforço e decidir entre soluções concorrentes com base em evidência, e não em impressão.

As doze dimensões entram em outro momento do trabalho. Elas não servem para rotular o requisito depois de escrito, servem como lista de verificação antes de encerrar o levantamento. O arquiteto percorre as doze e pergunta, para cada uma, se aquela dimensão foi discutida com alguém. As que ninguém mencionou são o material da próxima entrevista, e costumam ser justamente as caras de corrigir depois, como residência de dados, tempo de recuperação e compatibilidade retroativa de integração.

## Exercício 6

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

1. Classifique cada uma das oito declarações em uma das três categorias de trabalho, requisito funcional, requisito de atributo de qualidade ou restrição, justificando em uma frase. Nenhuma delas deve ser classificada como requisito não funcional, porque esse rótulo é o ponto de partida do trabalho e não o resultado dele. Para as que forem requisito de atributo de qualidade, indique se estão bem ou mal formuladas.
2. Escolha dois requisitos de atributo de qualidade mal formulados e reescreva cada um em forma mensurável, seguindo o padrão de contexto, carga e medida usado no exemplo de desempenho da plataforma de vídeo, apresentado na seção Conceito acima. Se alguma parte da declaração original não puder ser reescrita por não nomear atributo algum, diga isso em vez de inventar uma medida.

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- International Organization for Standardization/International Electrotechnical Commission/Institute of Electrical and Electronics Engineers. (2022). *Systems and software engineering — Architecture description* (ISO/IEC/IEEE 42010:2022). (definições de arquitetura e de requisito)
- International Organization for Standardization. (2023). *Systems and software engineering — Systems and software quality requirements and evaluation (SQuaRE) — Product quality model* (ISO/IEC 25010:2023). (modelo de qualidade de produto)
- Barbacci, M., Ellison, R., Lattanze, A., Stafford, J., Weinstock, C., & Wood, W. (2003). *Quality attribute workshops (QAWs), third edition* (CMU/SEI-2003-TR-016). Software Engineering Institute, Carnegie Mellon University. (atributos de qualidade e cenários)
- Mendes, M. (2026b). *Guias de projeto de arquitetura de software* [Material de curso, versão arquivada]. https://github.com/aulas-marco/projeto-arquitetura-software/tree/30f15cd (guia 1.1.1, seção 2, fonte das doze categorias de requisito arquitetural e dos exemplos reproduzidos nesta página)
- Eeles, P. (2001). *Capturing architectural requirements*. Rational Software Corporation. (método de captura citado por Mendes (2026b))

**Material do curso.** Glossário, entradas [atributo de qualidade](../referencia/glossario.md#atributo-de-qualidade), [requisito funcional](../referencia/glossario.md#requisito-funcional), [requisito não funcional](../referencia/glossario.md#requisito-nao-funcional) e [requisito de atributo de qualidade](../referencia/glossario.md#requisito-de-atributo-de-qualidade). Dossiê da instituição fictícia [ACME](../caso-acme/index.md), requisitos declarados pelas partes interessadas.
