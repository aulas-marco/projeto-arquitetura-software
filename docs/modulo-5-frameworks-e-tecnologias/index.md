# Aula 5, frameworks e tecnologias

A aula converte o [desenho lógico](../referencia/glossario.md#desenho-logico) produzido nas Aulas 3 e 4 em escolha de tecnologia, indo do [bloco de construção da solução](../referencia/glossario.md#bloco-de-construcao-da-solucao) ao serviço de infraestrutura que o realiza e ao modelo técnico de referência que classifica esses serviços. A mesma aula trata da plataforma e dos frameworks, verifica a segurança da solução sobre a tecnologia escolhida e registra a decisão de plataforma em [ADR](../referencia/glossario.md#adr), com as lacunas de provisão de serviço que a decisão revela.

## Objetivos de aprendizagem

Ao final da aula, o aluno é capaz de

- mapear um bloco de construção da solução em requisito de serviço de infraestrutura, em serviço e em categoria do modelo técnico de referência
- classificar tecnologias em verde, âmbar e vermelho e escolher entre alternativas aprovadas pelos seis critérios de seleção
- distinguir plataforma arquitetural de framework e relacionar a plataforma ao estilo escolhido na Aula 3
- descrever os pilares de uma zona de pouso em nuvem e as etiquetas obrigatórias
- classificar ativos de dado pela LGPD, corrigir uma grade de permissões e associar ameaças às categorias STRIDE
- classificar lacunas de provisão de serviço em nova, substituição, modificação ou remoção

## Grade de tempo

A aula ocorre das 19h00 às 22h30, com intervalo das 20h30 às 20h45, e o tempo de conteúdo encerra até as 22h10. O tempo de aula é dividido entre a apresentação conceitual dos quatro blocos, as questões sobre a aula anterior e três questionários Kahoot, e os exercícios são realizados fora do horário de aula. A tabela abaixo é o único lugar do site em que os minutos de cada bloco aparecem, porque as páginas de bloco não exibem cronômetro.

| Horário | Atividade | Duração (min) |
| --- | --- | --- |
| 19h00–19h15 | Questões sobre a Aula 4 | 15 |
| 19h15–19h25 | Kahoot de revisão da Aula 4 | 10 |
| 19h25–19h58 | Bloco 1, definição tecnológica e modelo técnico de referência | 33 |
| 19h58–20h30 | Bloco 2, plataforma arquitetural | 32 |
| 20h30–20h45 | Intervalo | 15 |
| 20h45–20h55 | Kahoot dos blocos 1 e 2 | 10 |
| 20h55–21h28 | Bloco 3, segurança fim a fim | 33 |
| 21h28–22h00 | Bloco 4, ADR de plataforma e lacunas | 32 |
| 22h00–22h10 | Kahoot dos blocos 3 e 4 | 10 |

Os quatro blocos somam 130 minutos de apresentação conceitual, e os três questionários e as questões iniciais ocupam os 45 minutos restantes do tempo útil de 175 minutos.

## Entrada recebida da Aula 4

A aula parte de dois produtos das aulas anteriores. O diagrama de contêineres do [exercício 16](../modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md#exercicio-16), com as relações rotuladas por modo de comunicação, volume e latência, traz os contêineres novos com o rótulo tecnologia a definir, e a definição tecnológica deste módulo converte esse rótulo em escolha. O estilo registrado no ADR do [exercício 12](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md#exercicio-12) é a decisão que a plataforma do bloco 2 concretiza e à qual o ADR de plataforma do bloco 4 se encadeia.

## Roteiro da aula

O [bloco 1](bloco-1-definicao-tecnologica-e-trm.md) apresenta a definição tecnológica da solução, os sete tipos de restrição tecnológica, a cadeia que liga o bloco de construção ao requisito de serviço, ao serviço de infraestrutura e ao componente, o modelo técnico de referência em cinco colunas, a classificação em verde, âmbar e vermelho e os seis critérios de seleção organizados numa matriz de avaliação, com o exemplo do serviço de identidade do Hospital ACME. O exercício 17 fornece os contêineres do exercício 16 e um recorte do modelo técnico da ACME e pede ao aluno, em três itens, que associe os contêineres às categorias do modelo, que classifique seis tecnologias da linha de base em verde, âmbar ou vermelho e que preencha a parte da matriz de seleção do provedor de identidade que o dossiê permite.

O [bloco 2](bloco-2-plataforma-arquitetural.md) define plataforma arquitetural como a concretização de um estilo, apresenta quatro exemplos de plataforma por estilo e trata a zona de pouso como a fundação em nuvem da plataforma, com os cinco pilares, a infraestrutura como código, as etiquetas obrigatórias e a observabilidade. O exercício 18 pede, em três itens, duas plataformas candidatas para o estilo do exercício 10, o quadro comparativo pelos seis critérios sobre dados do dossiê e a leitura de um diagrama de zona de pouso quanto aos pilares, às etiquetas que faltam em seis recursos e ao requisito que justifica a conta de segurança e registros.

O [bloco 3](bloco-3-seguranca-fim-a-fim.md), Segurança fim a fim, trata a segurança como passo final da definição tecnológica, com a classificação de ativos pelos três atributos de confidencialidade, integridade e disponibilidade, com nível para cada ativo, e pela LGPD, a grade de permissões e o menor privilégio, os controles da zona de pouso, a fronteira de confiança com as seis categorias STRIDE e a autoridade de design de segurança. O exercício 19 pede, em três itens, a classificação de seis ativos de dado, a identificação das células de uma grade de permissões que violam o menor privilégio e a associação de seis ameaças à fronteira do aplicativo do aluno a categorias STRIDE e a controles.

O [bloco 4](bloco-4-adr-de-plataforma.md) apresenta o ADR de plataforma como segundo registro do par iniciado na Aula 3, as seis dimensões de dependência de fornecedor, a classificação das lacunas de provisão em quatro tipos e a validação da definição tecnológica com as partes interessadas. O exercício 20 pede, em quatro itens, o encadeamento do ADR com o ADR de estilo, as forças e a dependência de fornecedor, as consequências, as evidências e o gatilho de revisão, e a classificação de seis itens da definição tecnológica considerada como lacuna nova, substituição, modificação ou remoção.

A [síntese](sintese.md) fecha o módulo com o checklist do que precisa permanecer, a cadeia dos exercícios 16 a 20, a autoavaliação e a lista das referências citadas nos quatro blocos.

## Preparação para a Aula 6

A Aula 6 compara a arquitetura de linha de base com a arquitetura alvo definida nas aulas anteriores e usa as lacunas de provisão classificadas no exercício 20 como entrada do roteiro de entrega. A mesma aula trata de governança e de inovação em soluções tecnológicas, e o [cronograma](../cronograma.md) traz a sequência completa das seis aulas.
