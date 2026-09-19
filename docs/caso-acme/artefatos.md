# Artefatos por aula

A ACME é uma universidade privada brasileira fictícia, com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, usado como caso único ao longo das seis aulas da disciplina. Esta página registra o que cada aula acrescenta ao dossiê do caso.

O dossiê é cumulativo. Cada exercício produz um artefato que serve de entrada para a aula seguinte, de modo que o aluno termina a disciplina com um conjunto encadeado de decisões sobre o mesmo sistema, e não com exercícios isolados.

## Aula 1, fundamentos

A ementa da Aula 1 está definida. Os quatro artefatos abaixo correspondem aos quatro blocos da aula, realizados em 21/09/2026.

| Bloco | Artefato produzido | Entrada usada do dossiê | Critério de aceitação |
| --- | --- | --- | --- |
| 1 | Nenhum artefato formal de saída. O exercício produz leitura estruturada do contexto, em resposta a três perguntas interpretativas | Mapa de atores e restrições fechadas da [página inicial do caso](index.md) | A resposta liga cada restrição ao ator que a impôs, e nomeia ao menos um conflito de interesse com a autoridade que o resolve |
| 2 | Classificação dos requisitos declarados em requisito funcional, requisito de atributo de qualidade, requisito não funcional de outra natureza e restrição, com reescrita de dois itens em forma mensurável | Requisitos R2, R3, R4, R5, R6, R10, R11 e R13 da [página inicial do caso](index.md) | Os oito itens classificados com justificativa de uma linha, e os dois requisitos de atributo de qualidade mal formulados reescritos em forma mensurável, com contexto, carga e medida |
| 3 | Dois cenários de atributo de qualidade no formato de seis elementos, com julgamento de significância arquitetural | Volumes, sazonalidade e incidentes dos [dados operacionais](dados-operacionais.md) | Cada cenário traz fonte do estímulo, estímulo, artefato, ambiente, resposta e medida da resposta, e a defesa da significância aplica o roteiro de sete perguntas |
| 4 | Comparação de três estilos arquiteturais candidatos contra os cenários escritos no bloco 3 | Cenários do bloco 3 e componentes da [arquitetura de linha de base](linha-de-base.md) | A comparação avalia cada estilo contra cada cenário, e a escolha declara o que é sacrificado |

A leitura interpretativa do bloco 1 e os três artefatos formais dos blocos 2 a 4 formam o enquadramento do problema. Eles respondem quem quer o quê, o que é exigência e o que é restrição, como medir a exigência e qual organização estrutural atende melhor às exigências medidas.

## Aulas 2 a 6

A partição em blocos das aulas seguintes depende da definição da ementa de cada uma. A coluna de artefato registra o previsto na estrutura da disciplina e está sujeita a revisão.

| Aula | Data | Tema | Artefato previsto, sujeito à definição da ementa |
| --- | --- | --- | --- |
| 2 | 23/09/2026 | Plataforma arquitetural e modelos | Registro de decisão de arquitetura sobre a plataforma, e modelo C4 de contexto e de contêineres da ACME |
| 3 | 28/09/2026 | Descoberta detalhada, linha de base e riscos | Relatório de lacunas entre a linha de base e a arquitetura pretendida, e plano de resposta aos riscos arquiteturais |
| 4 | 30/09/2026 | Requisitos avançados, dados e segurança | Modelo de dados de destino, estratégia de convivência entre o banco compartilhado e os novos serviços, e desenho dos controles de segurança e privacidade |
| 5 | 05/10/2026 | Blueprint da solução e modelo técnico de referência | Blueprint da solução alvo, modelo técnico de referência e desenho da infraestrutura pretendida |
| 6 | 15/10/2026 | Evolução e governança | Roteiro de evolução em ondas, compromissos arquiteturais declarados e modelo de governança das decisões |

## Rastreabilidade entre artefatos

A dependência entre artefatos define a ordem em que eles podem ser produzidos. A cadeia da Aula 1 é linear a partir do bloco 2. O bloco 1 não produz artefato formal, mas prepara o terreno interpretativo do bloco 2, ao situar quem decide o quê e quais restrições já chegam fechadas, sem que a classificação de requisitos dependa formalmente de um artefato do bloco 1. Os cenários dependem da classificação, porque só requisito de atributo de qualidade vira cenário. A comparação de estilos depende dos cenários, porque estilo se avalia contra exigência medida, não contra exigência declarada em termos gerais.

Das aulas seguintes, o relatório de lacunas da Aula 3 depende do blueprint parcial que a Aula 2 inicia e da linha de base descrita neste dossiê. O roteiro de evolução da Aula 6 depende do relatório de lacunas e das restrições contratuais registradas nos [dados operacionais](dados-operacionais.md), em especial dos prazos de 30/09/2027 e de 31/12/2028, que delimitam o que pode ser feito em cada onda.
