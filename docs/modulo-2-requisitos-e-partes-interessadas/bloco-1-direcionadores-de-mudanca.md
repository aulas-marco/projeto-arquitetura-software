# Direcionadores de mudança

Este bloco trata do que põe uma solução em movimento, os direcionadores internos e externos que levam a organização a agir, e o que deles chega ao arquiteto como insumo do desenho.

## Antes de começar

- [Direcionador de mudança](../referencia/glossario.md#direcionador-de-mudanca)
- [Arquitetura de solução](../referencia/glossario.md#arquitetura-de-solucao)
- [Artefato de linha de base](../referencia/glossario.md#artefato-de-linha-de-base)

## Conceito

Direcionador é a força que faz a organização sentir pressão para mudar parte do negócio, mudança que pode ser alcançada com uma solução nova ou modificada. No início do ciclo de vida, o negócio entrega à equipe de arquitetura três coisas, a declaração do problema contida na declaração de visão da solução, qualquer documentação existente que ajude a entender a situação, e a autorização para investigar, contida no documento de iniciação da arquitetura.

<figure markdown="span">
![Infográfico sobre direcionadores de mudança. À esquerda, os direcionadores internos estratégia de negócio, estratégia de TI e análise de negócio. Ao centro, a pressão para mudar passa pela análise e orienta decisões arquiteturais. À direita, a análise do macroambiente é organizada nas seis dimensões PESTLE, política, econômica, sociocultural, tecnológica, legal e ambiental.](../assets/images/modulo-2-direcionadores-mudanca.png){ .module-diagram }
</figure>

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

A resposta a esses direcionadores é reativa quando eles já se tornaram problema. Para agir de forma antecipada, a organização precisa prever a mudança externa, determinar seu impacto e decidir que ações cabem.

### Análise PESTLE

PESTLE é uma técnica de análise do macroambiente, isto é, das condições externas amplas que a organização não controla, mas que podem criar oportunidades, ameaças ou restrições. O nome é um acrônimo formado pelas iniciais de seis lentes. Usá-las como roteiro reduz o risco de observar apenas os fatores mais familiares à equipe, como tecnologia e legislação, e ignorar mudanças sociais, econômicas ou ambientais capazes de alterar o problema.

| Dimensão | Pergunta orientadora | Exemplo para uma instituição de ensino |
| --- | --- | --- |
| **Política** | Que prioridades, políticas públicas ou decisões governamentais podem mudar o setor? | Mudança em programas públicos de financiamento estudantil |
| **Econômica** | Que condições de renda, crédito, inflação ou custo podem afetar demanda e operação? | Redução da capacidade de pagamento dos alunos |
| **Sociocultural** | Que mudanças de comportamento, expectativa ou perfil demográfico influenciam o serviço? | Preferência crescente por jornadas móveis e flexíveis |
| **Tecnológica** | Que tecnologias emergentes, obsolescentes ou mais acessíveis alteram as possibilidades? | Oferta de serviços de nuvem previamente homologados |
| **Legal** | Que leis, normas ou decisões regulatórias criam obrigações? | Exigência de residência de dados em território nacional |
| **Ambiental** | Que condições ambientais ou compromissos de sustentabilidade afetam a operação? | Eventos climáticos que interrompem o acesso a um campus |

PESTLE não produz requisitos automaticamente e não serve para prever o futuro com certeza. Ela organiza a investigação. Para cada fator relevante, a equipe registra a evidência, estima o possível impacto, identifica o horizonte de tempo e decide se deve monitorar o sinal, formular um requisito ou reconhecer uma restrição.

No caso da ACME, a análise pode começar com fatos já documentados. A dimensão legal aparece na exigência de processamento de dados no Brasil, a tecnológica aparece nos provedores de nuvem pré-aprovados e a sociocultural aparece na expectativa por acesso móvel. As outras dimensões exigem pesquisa adicional. Essa distinção é importante, porque um fator plausível levantado numa oficina ainda é hipótese, enquanto uma condição apoiada por fonte verificável pode orientar uma decisão.

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

### Fontes práticas de pesquisa para o arquiteto

A análise PESTLE exige evidência verificável para cada fator, e as dimensões tecnológica e econômica dependem de informação sobre maturidade de tecnologias e sobre mercados de fornecedores que a equipe raramente produz sozinha. Empresas de pesquisa e consultoria em tecnologia publicam relatórios recorrentes com essa informação, e três deles aparecem com frequência em discussões de arquitetura, o Hype Cycle e o Magic Quadrant, ambos do Gartner, e o Forrester Wave, da Forrester Research. O acesso ao conteúdo completo desses relatórios costuma depender de assinatura, enquanto as metodologias que os definem estão descritas publicamente nos sites das duas empresas.

O **Hype Cycle** representa a trajetória das expectativas sobre uma inovação ao longo do tempo. Segundo o Gartner, o eixo vertical mede as expectativas e o eixo horizontal as relaciona ao valor comprovado da inovação à medida que o tempo passa, e a travessia do ciclo leva com frequência entre três e cinco anos, com parte das inovações abandonada antes de chegar ao fim. A tabela abaixo descreve as cinco fases do ciclo, com a tradução adotada nesta disciplina e o nome original usado pelo Gartner em inglês.

| Fase | Nome original | O que caracteriza a fase |
| --- | --- | --- |
| Gatilho da inovação | Innovation Trigger | Um avanço técnico ou o lançamento de um produto passa a atrair atenção |
| Pico das expectativas infladas | Peak of Inflated Expectations | O uso cresce, mas ainda há mais expectativa do que prova de que a inovação entrega o que promete |
| Vale da desilusão | Trough of Disillusionment | O interesse diminui quando experimentos e implantações não entregam o resultado esperado |
| Rampa do esclarecimento | Slope of Enlightenment | Os primeiros adotantes obtêm benefícios e outras organizações entendem como adaptar a inovação |
| Platô da produtividade | Plateau of Productivity | Mais usuários obtêm benefício real e a inovação passa ao uso corrente |

Para o arquiteto, o Hype Cycle ajuda a estimar o horizonte de tempo de um fator tecnológico da análise PESTLE e o risco de adotar uma tecnologia que ainda está no pico das expectativas, quando o custo de ser um dos primeiros adotantes tende a ser maior. A posição de uma tecnologia no ciclo descreve a expectativa do mercado em geral, e a adequação dessa tecnologia ao problema da organização continua dependendo dos requisitos e das restrições do caso.

O **Magic Quadrant** compara fornecedores de um mesmo mercado em dois critérios, a capacidade de execução, Ability to Execute, e a abrangência da visão, Completeness of Vision. O cruzamento dos dois critérios define quatro quadrantes.

| Quadrante | Nome original | Descrição resumida do Gartner |
| --- | --- | --- |
| Líderes | Leaders | Oferta madura que atende à demanda do mercado, com visão demonstrada para sustentar a posição à medida que os requisitos evoluem |
| Desafiantes | Challengers | Forte capacidade de execução, mas talvez sem plano que mantenha proposta de valor forte para clientes novos |
| Visionários | Visionaries | Alinhados à visão do Gartner sobre a evolução do mercado, com capacidade de entrega ainda menos comprovada |
| Participantes de nicho | Niche Players | Bom desempenho em um segmento do mercado, por foco em uma funcionalidade ou região, ou por serem entrantes recentes |

O próprio Gartner declara, no aviso que acompanha as publicações do Magic Quadrant, que não endossa fornecedor, produto ou serviço representado em sua pesquisa e que não recomenda selecionar apenas os fornecedores com as avaliações mais altas, porque suas publicações expressam a opinião da sua organização de pesquisa. Um participante de nicho pode ser a melhor escolha quando o nicho coincide com o problema da organização, e essa é a leitura que o arquiteto precisa fazer antes de usar o quadrante como lista de candidatos.

O **Forrester Wave** é descrito pela Forrester Research como um guia para compradores que avaliam opções em um mercado de tecnologia, baseado na análise e na opinião da empresa. A avaliação combina a oferta atual do fornecedor, Current Offering, e a sua estratégia, Strategy, e desde 01/07/2024 o gráfico apresenta a avaliação de clientes, Customer Feedback, no lugar da antiga presença de mercado. Na mesma revisão, a classificação passou a ter três categorias, Leaders, Strong Performers e Contenders. O nome da empresa é Forrester Research, e a grafia Forrester Group, que aparece em algumas referências informais, não corresponde à razão social.

Os três instrumentos respondem a perguntas diferentes e entram em momentos diferentes do processo, e a tabela abaixo resume essa correspondência.

| Instrumento | Pergunta respondida | Uso no processo de arquitetura | Cuidado na leitura |
| --- | --- | --- | --- |
| Hype Cycle | Em que estágio de maturidade e de expectativa está uma tecnologia? | Horizonte de tempo e risco de adoção de um fator tecnológico na análise PESTLE | A posição reflete a expectativa do mercado e não a adequação ao caso |
| Magic Quadrant | Como os fornecedores de um mercado se comparam em execução e visão? | Lista inicial de candidatos antes da comparação de plataformas, tratada na Aula 5 | O recorte do mercado definido pelo Gartner pode diferir do problema da organização |
| Forrester Wave | Como os fornecedores se comparam em oferta atual, estratégia e avaliação de clientes? | Segunda opinião sobre o mesmo mercado, útil para confrontar com o Magic Quadrant | Os critérios e os pesos pertencem à Forrester Research e podem divergir das forças do caso |

Nenhum dos três relatórios substitui a evidência produzida pela própria organização, como prova de conceito, contato com clientes do fornecedor e verificação de aderência às restrições. Ao citar qualquer um deles em uma análise PESTLE ou em um registro de decisão, o arquiteto registra o título, a edição, a data de publicação e o mercado avaliado, porque os relatórios são revistos com frequência e uma posição de dois anos antes pode não valer mais. Na ACME, por exemplo, um Magic Quadrant de plataformas de nuvem pode informar a comparação entre os dois provedores pré-aprovados pelo Conselho Universitário em 12/03/2026, mas não reabre a restrição que limita a escolha a esses dois.

## Uso pelo arquiteto

O arquiteto levanta os direcionadores antes de discutir alternativa, porque eles determinam o que conta como solução aceitável. Um direcionador externo de natureza legal costuma fechar alternativas de forma definitiva, enquanto um direcionador interno de custo costuma apenas ordenar preferências, e confundir os dois leva a descartar cedo demais uma opção que ainda era viável.

O registro dos direcionadores também protege o projeto quando a liderança muda. Uma solução cujo motivo declarado esteja documentado sobrevive à troca de patrocinador, e uma solução cujo motivo só existia na conversa inicial costuma ser questionada desde o começo a cada mudança de interlocutor.

## Exercício 5

Este exercício é realizado fora do horário de aula, como atividade de aplicação do conceito apresentado neste bloco ao caso da instituição fictícia ACME.

A ACME é uma universidade privada brasileira fictícia, com 38.400 alunos ativos, dos quais 10.200 na graduação a distância, e um sistema acadêmico em operação desde 2004 que sustenta matrícula, avaliação, emissão de documentos e integração com o ERP financeiro. A modernização foi autorizada com orçamento de R$ 6,2 milhões para o primeiro ciclo de 12 meses. O custo anual de propriedade do sistema é de R$ 15,83 milhões, o prazo médio de entrega de uma mudança é de 34 dias úteis, e dois dos três incidentes graves dos últimos 18 meses ocorreram na janela de matrícula.

Responda às três perguntas abaixo.

1. Classifique os sete direcionadores listados na seção Conceito em reativos e antecipatórios, justificando cada classificação pela evidência do caso.
2. Aplique a análise PESTLE ao caso da ACME e proponha, para cada uma das seis categorias, um fator externo plausível que possa afetar a instituição nos próximos três anos. Indique quais dos seis fatores o dossiê do caso já registra e quais são acréscimo seu.
3. A meta de reduzir o custo anual de propriedade para R$ 11,0 milhões até o fim de 2029 convive com um contrato de capacidade de mainframe vigente até 31/12/2028, com piso de volume contratado. Explique, em até cinco linhas, o efeito dessa combinação sobre o que pode ser prometido no primeiro ciclo de 12 meses.

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seções 4.1 e 4.2)
- Gartner. (n.d.). *Gartner Hype Cycle research methodology*. https://www.gartner.com/en/research/methodologies/gartner-hype-cycle (eixos e cinco fases do Hype Cycle)
- Gartner. (n.d.). *Magic Quadrant research methodology*. https://www.gartner.com/en/research/methodologies/magic-quadrants-research (critérios e quadrantes do Magic Quadrant)
- Forrester Research. (n.d.). *The Forrester Wave methodology*. https://www.forrester.com/policies/forrester-wave-methodology/ (dimensões e categorias do Forrester Wave, revisão de 01/07/2024)

**Material do curso.** Glossário, entradas [direcionador de mudança](../referencia/glossario.md#direcionador-de-mudanca), [arquitetura de solução](../referencia/glossario.md#arquitetura-de-solucao) e [artefato de linha de base](../referencia/glossario.md#artefato-de-linha-de-base). Dossiê da instituição fictícia [ACME](../caso-acme/index.md), pergunta central, restrições fechadas e [dados operacionais](../caso-acme/dados-operacionais.md).
