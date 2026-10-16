# Os quatro domínios numa só solução

Quando uma universidade decide modernizar o sistema acadêmico, o arquiteto de solução precisava responder a quatro perguntas: o que muda no trabalho da universidade, que dados sustentam essa mudança, que aplicações a realizam e onde elas executam. Este bloco apresenta, antes do detalhamento, o que o arquiteto recebe, decide e entrega nos domínios de negócio, dados, aplicações e infraestrutura, e como a decisão tomada num domínio se torna a entrada do domínio seguinte. Um domínio é uma área de trabalho da arquitetura, com perguntas e produtos próprios. O bloco não tem exercício, e os quatro blocos seguintes detalham um domínio cada, com um exercício sobre o caso do curso, que é o de uma universidade fictícia.

## Antes de começar

- [Arquiteto de solução](../referencia/glossario.md#arquiteto-de-solucao)
- [Arquitetura de solução](../referencia/glossario.md#arquitetura-de-solucao)
- [Componentes da solução](../referencia/glossario.md#componentes-da-solucao)
- [ADR](../referencia/glossario.md#adr)

## O trabalho do arquiteto nos quatro domínios

O arquiteto de solução trabalha sobre uma única solução, delimitada pela declaração de escopo, o quadro do exercício 8 que registra o que muda e o que permanece no primeiro ciclo. Como não consegue decidir tudo de uma vez, ele detalha a solução em quatro domínios, na ordem negócio, dados, aplicações e infraestrutura, e em cada um consulta os modelos que a arquitetura corporativa e as áreas especialistas já mantêm, decide o que é próprio da solução e entrega ao domínio seguinte a decisão de que ele precisa, como parte do papel apresentado no [bloco 3 da Aula 1](../modulo-1-fundamentos/bloco-3-papel-do-arquiteto-de-solucao.md). O percurso parte do estilo e dos padrões registrados no [ADR da Aula 3](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md) e termina nas exigências que a definição tecnológica da Aula 5 recebe.

A Figura 1 organiza esse percurso em quatro camadas, cada uma com a forma curta da pergunta que o arquiteto responde, detalhada no roteiro da seção Uso pelo arquiteto, e três colunas. A coluna Recebe registra o que chega ao domínio e de quem, a coluna Decide registra o trabalho próprio do arquiteto, e a coluna Entrega registra o produto que segue para o domínio seguinte, indicado pelas setas que ligam a coluna Entrega de uma camada à coluna Recebe da camada abaixo.

<figure markdown="span">
![Quatro camadas empilhadas, negócio, dados, aplicações e infraestrutura, entre a faixa de entrada com o estilo e os padrões registrados em ADR na Aula 3 e a faixa de saída com a definição tecnológica da Aula 5. Cada camada traz a pergunta do arquiteto e as colunas recebe, decide e entrega, com a coluna decide em destaque, e setas ortogonais ligam a entrega de cada camada ao que a camada seguinte recebe. À esquerda, a hierarquia de serviços acompanha as camadas.](../assets/images/modulo-4-b0-espinha-dorsal.svg){ .module-diagram }
</figure>

*Figura 1 — O que o arquiteto de solução recebe, decide e entrega em cada domínio, com o encadeamento entre os domínios. Fonte: material do curso, com base em Lovatt (2021).*

### O que o arquiteto faz em cada domínio

A tabela detalha as três colunas da Figura 1 e acrescenta o limite do papel, isto é, o trabalho que o arquiteto de solução consulta ou solicita, sem assumir como tarefa própria. Ela usa termos que o bloco de cada domínio define com calma, e um resumo ajuda a ler as linhas. Uma capacidade é o que a organização precisa conseguir fazer, uma etapa é cada passo do fluxo de valor pelo qual o cliente recebe o serviço e uma atividade é cada tarefa de um processo. Nos dados, o dono é quem tem autorização para gravar uma entidade, a fonte de verdade é o lugar em que a entidade é registrada com autoridade e o regime de consistência é o atraso com que uma cópia reflete a fonte, e nas aplicações o contêiner é cada aplicação, serviço ou banco de dados executável que compõe o sistema.

| Domínio | Recebe, e de quem | Decide | Entrega | Trabalho que não assume |
| --- | --- | --- | --- | --- |
| Negócio | Mapa de capacidades, fluxo de valor e modelo de processo, da arquitetura corporativa e da análise de negócio | Capacidades, etapas e atividades em que a mudança incide | Capacidades, etapas e atividades afetadas | Modelagem de processos, que cabe à análise de negócio |
| Dados | Capacidades afetadas e modelo de dados corporativo, da arquitetura de dados | Dono, fonte de verdade, regime de consistência e obrigações de cada entidade | Grade dado × aplicação | Manutenção do modelo de dados corporativo, que cabe à arquitetura de dados |
| Aplicações | Grade dado × aplicação e portfólio de aplicações | Aplicações que mudam, interfaces, contratos e fronteira da solução | Diagramas de contexto e de contêineres e contratos de integração | Escolha de produto e de framework, que cabe à definição tecnológica da Aula 5 |
| Infraestrutura | Contêineres e relações, do domínio de aplicações | Modo, volume e latência de cada relação, camada de execução compatível e topologia | Diagrama de implantação e exigências para a definição tecnológica | Operação da plataforma, que cabe à área de infraestrutura |

Quando um insumo da coluna Recebe não existe, o arquiteto registra a ausência como risco e solicita o artefato à área responsável, procedimento que o [bloco 1](bloco-1-arquitetura-de-negocio.md) detalha para os modelos de negócio.

O encadeamento fica concreto no caso da nota que o professor lança. O bloco 1 localiza o lançamento de nota como uma atividade afetada pela modernização, e por isso o bloco 2 precisa decidir quem é o dono da entidade nota. Com o dono decidido, o bloco 3 escreve o contrato da integração que leva a nota ao ambiente virtual de aprendizagem, a plataforma de ensino a distância da universidade, e o bloco 4 rotula essa relação com o prazo de 10 minutos que o requisito de propagação da nota, pedido pela área de Educação a Distância, exige para a nota chegar a essa plataforma.

### A ordem dos domínios

A ordem negócio, dados, aplicações e infraestrutura tem uma razão, que é o fato de todos os componentes da solução (pessoas, estruturas organizacionais, processos, informação e tecnologia) sustentarem, em última instância, um ou mais serviços de negócio. A hierarquia de serviços vai do serviço de negócio, realizado por processos de negócio, ao serviço de aplicação, oferecido por componentes de aplicação, e ao serviço de tecnologia, que executa esses componentes, e os dados atravessam a hierarquia como a informação que os serviços consomem e produzem. A ordem dos domínios acompanha essa hierarquia de cima para baixo, porque cada domínio se justifica pelo serviço que sustenta no domínio acima, e o [bloco 3](bloco-3-arquitetura-de-aplicacoes-e-integracao.md#hierarquia-de-servicos) retoma a hierarquia ao tratar dos contratos de integração.

## Uso pelo arquiteto

O arquiteto não pergunta por dados antes de saber que capacidades mudam, nem por infraestrutura antes de saber que aplicações trocam informação, e por isso cada domínio abre com uma pergunta cuja resposta é a entrada da pergunta seguinte. Os blocos 1 a 4 retomam a pergunta do respectivo domínio, com a mesma redação.

1. Negócio: Que capacidades, etapas do fluxo de valor e atividades a solução altera, segundo os modelos que a arquitetura de negócio já mantém?
2. Dados: Que entidades sustentam as capacidades afetadas, quem é o dono de cada uma, onde fica a fonte de verdade, com que regime cada cópia a reflete e que obrigações o dado carrega?
3. Aplicações: Que aplicações mudam, por quais interfaces trocam essas entidades, que contrato governa cada interface e onde passa a fronteira da solução?
4. Infraestrutura: Em que nó cada contêiner executa, com que modo, volume e latência cada relação opera e o que fica como exigência para a definição tecnológica?

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seções 1.5 a 1.7, papel do arquiteto de solução, e seções 2.3 a 2.7, domínios da arquitetura)

**Material do curso.** O bloco usa as entradas [arquiteto de solução](../referencia/glossario.md#arquiteto-de-solucao), [arquitetura de solução](../referencia/glossario.md#arquitetura-de-solucao), [componentes da solução](../referencia/glossario.md#componentes-da-solucao) e [ADR](../referencia/glossario.md#adr) do glossário.
