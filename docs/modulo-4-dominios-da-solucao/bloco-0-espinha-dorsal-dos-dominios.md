# Os quatro domínios numa só solução

Este bloco apresenta, antes do detalhamento de cada domínio, o que o arquiteto de solução recebe, decide e entrega nos domínios de negócio, dados, aplicações e infraestrutura, e como a decisão tomada num domínio se torna a entrada do domínio seguinte.

## Antes de começar

- [Arquiteto de solução](../referencia/glossario.md#arquiteto-de-solucao)
- [Arquitetura de solução](../referencia/glossario.md#arquitetura-de-solucao)
- [Componentes da solução](../referencia/glossario.md#componentes-da-solucao)
- [ADR](../referencia/glossario.md#adr)

## O trabalho do arquiteto nos quatro domínios

O arquiteto de solução trabalha sobre uma única solução, delimitada pela declaração de escopo, e a detalha em quatro domínios, na ordem negócio, dados, aplicações e infraestrutura. Em cada domínio, ele consulta os modelos que a arquitetura corporativa e as áreas especialistas já mantêm, decide o que é próprio da solução e entrega ao domínio seguinte a decisão de que ele precisa, como parte do papel apresentado no [bloco 3 da Aula 1](../modulo-1-fundamentos/bloco-3-papel-do-arquiteto-de-solucao.md). O percurso parte do estilo e dos padrões registrados no [ADR da Aula 3](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md) e termina nas exigências que a definição tecnológica da Aula 5 recebe.

A Figura 1 organiza esse percurso em quatro camadas, cada uma com a forma curta da pergunta que o arquiteto responde, detalhada no roteiro da seção Uso pelo arquiteto, e três colunas. A coluna Recebe registra o que chega ao domínio e de quem, a coluna Decide registra o trabalho próprio do arquiteto, e a coluna Entrega registra o produto que segue para o domínio seguinte, indicado pelas setas que ligam a coluna Entrega de uma camada à coluna Recebe da camada abaixo.

<figure markdown="span">
![Quatro camadas empilhadas, negócio, dados, aplicações e infraestrutura, entre a faixa de entrada com o estilo e os padrões registrados em ADR na Aula 3 e a faixa de saída com a definição tecnológica da Aula 5. Cada camada traz a pergunta do arquiteto e as colunas recebe, decide e entrega, com a coluna decide em destaque, e setas ortogonais ligam a entrega de cada camada ao que a camada seguinte recebe. À esquerda, a hierarquia de serviços acompanha as camadas.](../assets/images/modulo-4-b0-espinha-dorsal.svg){ .module-diagram }
</figure>

*Figura 1 — O que o arquiteto de solução recebe, decide e entrega em cada domínio, com o encadeamento entre os domínios. Fonte: material do curso, com base em Lovatt (2021).*

### O que o arquiteto faz em cada domínio

A tabela detalha as três colunas da Figura 1 e acrescenta o limite do papel, isto é, o trabalho que o arquiteto de solução consulta ou solicita, sem assumir como tarefa própria.

| Domínio | Recebe, e de quem | Decide | Entrega | Trabalho que não assume |
| --- | --- | --- | --- | --- |
| Negócio | Mapa de capacidades, fluxo de valor e modelo de processo, da arquitetura corporativa e da análise de negócio | Capacidades, etapas e atividades em que a mudança incide | Capacidades, etapas e atividades afetadas | Modelagem de processos, que cabe à análise de negócio |
| Dados | Capacidades afetadas e modelo de dados corporativo, da arquitetura de dados | Dono, fonte de verdade, regime de consistência e obrigações de cada entidade | Grade dado × aplicação | Manutenção do modelo de dados corporativo, que cabe à arquitetura de dados |
| Aplicações | Grade dado × aplicação e portfólio de aplicações | Aplicações que mudam, interfaces, contratos e fronteira da solução | Diagramas de contexto e de contêineres e contratos de integração | Escolha de produto e de framework, que cabe à definição tecnológica da Aula 5 |
| Infraestrutura | Contêineres e relações, do domínio de aplicações | Modo, volume e latência de cada relação, camada de execução compatível e topologia | Diagrama de implantação e exigências para a definição tecnológica | Operação da plataforma, que cabe à área de infraestrutura |

Quando um insumo da coluna Recebe não existe, o arquiteto registra a ausência como risco e solicita o artefato à área responsável, procedimento que o [bloco 1](bloco-1-arquitetura-de-negocio.md) detalha para os modelos de negócio.

### A ordem dos domínios

Todos os componentes da solução sustentam, em última instância, um ou mais serviços de negócio. A hierarquia de serviços vai do serviço de negócio, realizado por processos de negócio, ao serviço de aplicação, oferecido por componentes de aplicação, e ao serviço de tecnologia, que executa esses componentes, e os dados atravessam a hierarquia como a informação que os serviços consomem e produzem. A ordem dos domínios acompanha essa hierarquia de cima para baixo, porque cada domínio se justifica pelo serviço que sustenta no domínio acima, e o [bloco 3](bloco-3-arquitetura-de-aplicacoes-e-integracao.md#hierarquia-de-servicos) retoma a hierarquia ao tratar dos contratos de integração.

## Uso pelo arquiteto

O arquiteto entra em cada domínio com uma pergunta, e a resposta de cada pergunta é a entrada da pergunta seguinte. Os blocos 1 a 4 retomam a pergunta do respectivo domínio, com a mesma redação.

1. Negócio: Que capacidades, etapas do fluxo de valor e atividades a solução altera, segundo os modelos que a arquitetura de negócio já mantém?
2. Dados: Que entidades sustentam as capacidades afetadas, quem é o dono de cada uma, onde fica a fonte de verdade, com que regime cada cópia a reflete e que obrigações o dado carrega?
3. Aplicações: Que aplicações mudam, por quais interfaces trocam essas entidades, que contrato governa cada interface e onde passa a fronteira da solução?
4. Infraestrutura: Em que nó cada contêiner executa, com que modo, volume e latência cada relação opera e o que fica como exigência para a definição tecnológica?

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seções 1.5 a 1.7, papel do arquiteto de solução, e seções 2.3 a 2.7, domínios da arquitetura)

**Material do curso.** O bloco usa as entradas [arquiteto de solução](../referencia/glossario.md#arquiteto-de-solucao), [arquitetura de solução](../referencia/glossario.md#arquitetura-de-solucao), [componentes da solução](../referencia/glossario.md#componentes-da-solucao) e [ADR](../referencia/glossario.md#adr) do glossário.
