# Artefatos por aula

A ACME é uma universidade privada brasileira fictícia, com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, usado como caso único ao longo das seis aulas da disciplina. Esta página registra o que cada aula acrescenta ao dossiê do caso.

O dossiê é cumulativo. A maior parte dos exercícios produz um artefato que serve de entrada para a aula seguinte, de modo que o aluno termina a disciplina com um conjunto encadeado de decisões sobre o mesmo sistema, e não com exercícios isolados.

## Aula 1, fundamentos

A tabela abaixo cobre os quatro blocos da aula, três deles com artefato formal.

| Bloco | Artefato produzido | Entrada usada do dossiê | Critério de aceitação |
| --- | --- | --- | --- |
| 1 | Nenhum artefato formal de saída. O exercício produz leitura estruturada do contexto, em resposta a três perguntas interpretativas | Mapa de atores e restrições fechadas da [página inicial do caso](index.md) | A resposta liga cada restrição ao ator que a impôs, e nomeia ao menos um conflito de interesse com a autoridade que o resolve |
| 2 | Classificação das declarações em requisito funcional, requisito de atributo de qualidade ou restrição, que são as três categorias de trabalho, com reescrita de dois itens em forma mensurável | Requisitos R2, R3, R4, R5, R6, R10, R11 e R13 da [página inicial do caso](index.md) | Os oito itens classificados com justificativa de uma linha, e os dois requisitos de atributo de qualidade mal formulados reescritos em forma mensurável, com contexto, carga e medida |
| 3 | Dois cenários de atributo de qualidade no formato de seis elementos, com julgamento de significância arquitetural | Volumes, sazonalidade e incidentes dos [dados operacionais](dados-operacionais.md) | Cada cenário traz fonte do estímulo, estímulo, artefato, ambiente, resposta e medida da resposta, e a defesa da significância aplica o roteiro de sete perguntas |
| 4 | Comparação de três estilos arquiteturais candidatos contra os cenários escritos no bloco 3 | Cenários do bloco 3 e componentes da [arquitetura de linha de base](linha-de-base.md) | A comparação avalia cada estilo contra cada cenário, e a escolha declara o que é sacrificado |

A leitura interpretativa do bloco 1 e os três artefatos formais dos blocos 2 a 4 formam o enquadramento do problema. Eles respondem quem quer o quê, o que é exigência e o que é restrição, como medir a exigência e qual organização estrutural atende melhor às exigências medidas.

## Aulas 2 a 6

| Aula | Tema | Artefatos produzidos nos quatro exercícios |
| --- | --- | --- |
| 2 | Decisão arquitetural, plataforma e modelos | Registro de decisão sobre o estilo, quadro comparativo de plataformas candidatas, registro de decisão sobre a plataforma, e modelo C4 de contexto e de contêineres da ACME |
| 3 | Arquitetura de aplicação e serviços | Decomposição de um contêiner em componentes, recorte do núcleo em serviços com fronteira justificada, contrato de um dos serviços, e desenho da convivência entre o serviço extraído e o núcleo que permanece |
| 4 | Arquitetura de integração e de dados | Classificação das integrações atuais com indicação do que precisa mudar, redesenho do fluxo de nota para atender o R7, definição de dono para cada dado do recorte com tratamento dos pontos de acesso direto ao banco, e escolha de táticas de dados para o R7 e o R9 |
| 5 | Arquitetura de segurança e modelo técnico de referência | Desenho do fluxo de identidade que atende o R8, desenho dos controles para o R9 e o R14, classificação das tecnologias já nomeadas na taxonomia de serviços de plataforma, e o modelo técnico de referência da ACME |
| 6 | Mapa de riscos e provas de conceito | Levantamento e classificação dos riscos arquiteturais, plano de resposta para os dois riscos mais altos, conversão de um risco em pergunta com critério de sucesso mensurável, e desenho de duas provas de conceito com escopo, prazo e critério |

## Rastreabilidade entre artefatos

A dependência entre artefatos define a ordem em que eles podem ser produzidos. A cadeia da Aula 1 é linear a partir do bloco 2. O bloco 1 não produz artefato formal, mas prepara o terreno interpretativo do bloco 2, ao situar quem decide o quê e quais restrições já chegam fechadas, sem que a classificação de requisitos dependa formalmente de um artefato do bloco 1. Os cenários dependem da classificação, porque só requisito de atributo de qualidade vira cenário. A comparação de estilos depende dos cenários, porque estilo se avalia contra exigência medida, não contra exigência declarada em termos gerais.

Das aulas seguintes, a cadeia continua linear. O recorte em serviços da Aula 3 depende do estilo e da plataforma decididos na Aula 2 e do diagrama de contêineres desenhado ali, porque não se recorta em serviços um sistema cuja forma estrutural ainda não foi escolhida. O desenho de integração e a propriedade de dado da Aula 4 dependem desse recorte, já que só há integração a desenhar depois que existem partes separadas para conversar entre si. Os controles de segurança da Aula 5 recaem sobre os serviços e os fluxos já desenhados, e o modelo técnico de referência compila as tecnologias que os três domínios anteriores nomearam. O mapa de riscos da Aula 6 percorre tudo o que foi decidido nas aulas anteriores procurando o que ficou apoiado em suposição, e as provas de conceito atacam justamente os riscos mais altos desse mapa.

As restrições contratuais registradas nos [dados operacionais](dados-operacionais.md), em especial os prazos de 30/09/2027 e de 31/12/2028, delimitam o que pode ser decidido em cada aula, porque elas fecham alternativas antes de qualquer análise técnica.
