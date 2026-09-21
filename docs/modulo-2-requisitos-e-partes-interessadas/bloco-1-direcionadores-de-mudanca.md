# Direcionadores de mudança

Este bloco trata do que põe uma solução em movimento, os direcionadores internos e externos que levam a organização a agir, e o que deles chega ao arquiteto como insumo do desenho.

## Antes de começar

- [Direcionador de mudança](../referencia/glossario.md#direcionador-de-mudanca)
- [Arquitetura de solução](../referencia/glossario.md#arquitetura-de-solucao)
- [Artefato de linha de base](../referencia/glossario.md#artefato-de-linha-de-base)

## Conceito

Direcionador é a força que faz a organização sentir pressão para mudar parte do negócio, mudança que pode ser alcançada com uma solução nova ou modificada. No início do ciclo de vida, o negócio entrega à equipe de arquitetura três coisas, a declaração do problema contida na declaração de visão da solução, qualquer documentação existente que ajude a entender a situação, e a autorização para investigar, contida no documento de iniciação da arquitetura.

### Direcionadores internos

Três fontes internas alimentam o desenho. A **estratégia de negócio** define a direção e as prioridades da operação, e descreve por que as coisas precisam mudar e em que parte do negócio a ação deve se concentrar. Dela vêm requisitos de negócio, objetivos e metas, resultados de investigações anteriores e artefatos como planos, mapas, modelos e cadeias de valor. A estratégia também é fonte de restrição, sobretudo quando um plano já em curso se sobrepõe ao problema em análise.

A **estratégia de TI** está necessariamente ligada à estratégia de negócio, porque a finalidade da tecnologia é sustentar os objetivos da organização. Nem toda ideia de mudança nasce do negócio, e a disponibilidade de tecnologia nova ou a evolução da existente criam oportunidades e desafios com impacto relevante sobre a operação. Quase toda estratégia de TI contém um esforço de racionalização do parque instalado em direção a padrões, sistemas e componentes preferidos, muitas vezes organizado em um radar tecnológico que classifica tecnologias por grau de adoção recomendada. Decisões registradas na estratégia de TI viram requisitos técnicos da solução, e o calendário de implantação de um componente novo pode restringir o calendário da solução.

A **análise de negócio** é a terceira fonte. O ciclo de mudança de negócio usado por essa disciplina tem cinco estágios, alinhar, definir, desenhar, implementar e realizar. O estágio de alinhar examina o ambiente externo e o interno em busca de desalinhamentos, e é nele que as ideias de mudança aparecem. Definir e desenhar são os estágios em que a arquitetura de solução concentra seu trabalho. Implementar e realizar ficam com a gestão de projetos e com as equipes de entrega, com a arquitetura respondendo pela governança.

### Direcionadores externos

Alguns direcionadores têm causa externa inequívoca, como mudança de legislação ou ação de concorrente. Outros são mais sutis, como decisões estratégicas de dirigentes que respondem em parte a eventos externos. A lista abaixo reúne os de componente externa forte.

| Direcionador | Exemplo de manifestação |
| --- | --- |
| Finanças | Disponibilidade de capital, termos de contrato, relação com bancos e com o poder público |
| Acionistas e órgãos de governo | Pedido de mudança vindo de instância superior de governança |
| Exigência regulatória | Alteração de regime regulatório aplicável ao setor |
| Concorrentes | Movimento de quem atua no mesmo ambiente de negócio |
| Retorno de clientes | Reclamação recorrente ou pesquisa de satisfação |
| Legislação | Lei nova ou alterada que muda obrigações da organização |

A resposta a esses direcionadores é reativa quando eles já se tornaram problema. Para agir de forma antecipada, a organização precisa prever a mudança externa, determinar seu impacto e decidir que ações cabem. A análise PESTLE apoia esse trabalho ao dividir o ambiente em seis categorias, política, econômica, sociocultural, tecnológica, legal e ambiental, e ao provocar a mesma pergunta em seis pontos de vista diferentes, se existe algo naquela categoria capaz de afetar o negócio.

### Os direcionadores da ACME

A ACME é uma universidade privada brasileira fictícia, com 38.400 alunos ativos, 2.150 professores e 4 campi em 3 cidades, cujo sistema acadêmico está em operação desde 2004. A tabela abaixo organiza o que o dossiê do caso registra.

| Direcionador | Natureza | Evidência no caso |
| --- | --- | --- |
| Custo de propriedade do sistema acadêmico | Interno, estratégia de negócio | R$ 15,83 milhões por ano, com meta declarada de R$ 11,0 milhões até o fim de 2029 |
| Lentidão de resposta a pedido de mudança | Interno, operação | 34 dias úteis entre pedido aprovado e entrega em produção |
| Risco de perda de competência | Interno, pessoas | 6 especialistas em COBOL na sustentação, 2 deles com aposentadoria prevista para 2027 |
| Exigência de proteção de dado pessoal | Externo, legislação | Parecer jurídico de 28/04/2026 exigindo processamento em território nacional |
| Avaliação regulatória | Externo, regulação | Preocupação declarada da Reitoria com queda de nota na avaliação |
| Expectativa do aluno | Externo, retorno de clientes | Demanda por aplicativo móvel e por matrícula que não falhe na abertura |
| Disponibilidade de nuvem contratável | Externo, tecnologia | Dois provedores pré-aprovados pelo Conselho Universitário em 12/03/2026 |

A leitura conjunta mostra por que o problema não é apenas técnico. Três direcionadores são internos e apontam para custo, prazo e competência, e quatro são externos e apontam para conformidade, reputação e expectativa. Uma solução que trate só dos internos deixa de responder ao que pressiona a instituição de fora.

## Uso pelo arquiteto

O arquiteto levanta os direcionadores antes de discutir alternativa, porque eles determinam o que conta como solução aceitável. Um direcionador externo de natureza legal costuma fechar alternativas de forma definitiva, enquanto um direcionador interno de custo costuma apenas ordenar preferências, e confundir os dois leva a descartar cedo demais uma opção que ainda era viável.

O registro dos direcionadores também protege o projeto quando a liderança muda. Uma solução cujo motivo declarado esteja documentado sobrevive à troca de patrocinador, e uma solução cujo motivo só existia na conversa inicial costuma ser questionada desde o começo a cada mudança de interlocutor.

## Exercício 5

A ACME é uma universidade privada brasileira fictícia, com 38.400 alunos ativos, dos quais 10.200 na graduação a distância, e um sistema acadêmico em operação desde 2004 que sustenta matrícula, avaliação, emissão de documentos e integração com o ERP financeiro. A modernização foi autorizada com orçamento de R$ 6,2 milhões para o primeiro ciclo de 12 meses. O custo anual de propriedade do sistema é de R$ 15,83 milhões, o prazo médio de entrega de uma mudança é de 34 dias úteis, e dois dos três incidentes graves dos últimos 18 meses ocorreram na janela de matrícula.

Responda às três perguntas abaixo.

1. Classifique os sete direcionadores listados na seção Conceito em reativos e antecipatórios, justificando cada classificação pela evidência do caso.
2. Aplique a análise PESTLE ao caso da ACME e proponha, para cada uma das seis categorias, um fator externo plausível que possa afetar a instituição nos próximos três anos. Indique quais dos seis fatores o dossiê do caso já registra e quais são acréscimo seu.
3. A meta de reduzir o custo anual de propriedade para R$ 11,0 milhões até o fim de 2029 convive com um contrato de capacidade de mainframe vigente até 31/12/2028, com piso de volume contratado. Explique, em até cinco linhas, o efeito dessa combinação sobre o que pode ser prometido no primeiro ciclo de 12 meses.

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seções 4.1 e 4.2)

**Material do curso.** Glossário, entradas [direcionador de mudança](../referencia/glossario.md#direcionador-de-mudanca), [arquitetura de solução](../referencia/glossario.md#arquitetura-de-solucao) e [artefato de linha de base](../referencia/glossario.md#artefato-de-linha-de-base). Dossiê da instituição fictícia [ACME](../caso-acme/index.md), pergunta central, restrições fechadas e [dados operacionais](../caso-acme/dados-operacionais.md).
