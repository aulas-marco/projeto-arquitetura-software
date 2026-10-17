# Revisão pedagógica da linguagem e das conexões do curso

**Data:** 17/10/2026  
**Estado:** revisão editorial em aplicação. A Aula 1 foi revisada e a Aula 2 está em revisão; as propostas dos demais documentos permanecem como guia para as próximas alterações. Os templates, as entregas e a estrutura do curso foram preservados.

O objetivo é facilitar a produção de um **Projeto de Arquitetura de Solução completo**, preservando a espinha dorsal do curso, a sequência dos módulos, os 24 exercícios e a profundidade de todas as partes do template. O caderno arquitetural reúne o projeto construído ao longo da disciplina. A revisão deve ajudar o aluno a compreender, produzir, justificar e conectar essas partes.

## Material entregue

| Documento | Conteúdo | Uso |
| --- | --- | --- |
| [52 propostas de revisão textual](01-revisoes-textuais.md) | Trecho atual, localização, redação sugerida e conteúdo que deve ser preservado | Revisar a linguagem com exemplos concretos |
| [40 conexões contextuais](02-conexoes.md) | Origem, destino, expressão clicável e finalidade de cada link | Ligar explicação, decisão, modelo, evidência e entrega |
| [12 propostas de esquemas](03-esquemas.md) | Pergunta pedagógica, conteúdo, lugar de uso e relação com figuras existentes, com três esboços | Tornar relações visíveis sem substituir o detalhamento |
| [Inventário das 72 páginas](04-inventario.md) | Tratamento sugerido para cada página, incluindo os gabaritos cumulativos | Controlar a abrangência da revisão |
| [Pontos de coerência para conferência](05-coerencia.md) | Passagens cuja relação precisa ser esclarecida antes de reescrever | Evitar que uma redação mais fluente esconda uma ambiguidade do projeto |

## Limites que orientam esta proposta

1. **Manter os seis módulos e sua sequência.** A ordem sugerida para executar a revisão editorial não altera a ordem das aulas.
2. **Manter todas as entregas e sua profundidade.** Não retirar campos, tabelas, categorias, fases, critérios de aceitação, responsabilidades ou verificações.
3. **Preservar as onze seções do caderno, numeradas de 0 a 10.** Nenhum esquema proposto substitui o template.
4. **Simplificar a expressão, preservando a precisão.** Um termo técnico necessário recebe uma explicação clara e um exemplo. Continua disponível para o aluno reconhecer o vocabulário profissional.
5. **Conectar o projeto inteiro.** Requisitos, restrições, pessoas, processos, dados, aplicações, infraestrutura, tecnologia, segurança, custos, contratos e transição precisam permanecer relacionados.
6. **Usar exemplos como exemplos.** A trajetória de R6 ou R7 ajuda a mostrar relações, mas não representa sozinha o projeto.

## Diagnóstico

O material já possui uma base pedagógica importante: um caso comum aos exercícios, perguntas de aplicação, exemplos resolvidos, figuras, glossário e um caderno cumulativo. O problema principal identificado é a quantidade de informação que o leitor precisa manter em mente dentro da mesma passagem e a pouca explicitação de algumas relações entre as partes do projeto.

O inventário da fonte local encontrou **72 páginas publicáveis**, das quais **36 pertencem aos seis módulos**. As outras 36 cobrem início, cronograma, caso ACME, referências, caderno e gabaritos. Há **77 arquivos de imagem distintos referenciados** e **90 ocorrências de links de um módulo a outro**, distribuídas por 60 pares de página de origem e arquivo de destino. Esses números não incluem os diagramas Mermaid como arquivos de imagem.

Portanto, acrescentar imagens e links por quantidade não resolve o problema. O ganho está em tornar explícito o trabalho que cada recurso permite fazer: entender uma distinção, recuperar uma entrada, justificar uma decisão, localizar um impacto ou conferir a coerência do projeto.

Na fonte examinada, o Módulo 1 não tem links Markdown explícitos para os demais módulos. Já o Módulo 5 concentra 36 das 90 ocorrências intermodulares. Isso não é uma medida isolada de qualidade, mas indica uma oportunidade: ajudar o aluno, desde o começo, a reconhecer onde os conceitos iniciais serão aplicados. A navegação gerada pelo tema e pelos hooks do caderno não foi contabilizada nessa métrica.

### O que torna a leitura pesada

| Padrão observado | Efeito no aluno | Tratamento editorial |
| --- | --- | --- |
| Definição, ressalva, exemplo e consequência unidos por várias orações | O aluno perde a pergunta principal antes de chegar ao fim | Dividir em frases e parágrafos, mantendo todas as informações |
| Substantivos abstratos em sequência, como definição, realização, provimento e racionalização | O texto não mostra quem faz o quê | Nomear a pessoa, a ação, o objeto e o resultado |
| Termos formais explicados por outros termos formais | O glossário não resolve a dúvida inicial | Acrescentar explicação cotidiana, exemplo e link de aplicação |
| Explicações repetidas de noções básicas de software | O texto fica longo sem ajudar na dificuldade principal do público | Preservar o dado e concentrar a explicação no significado para o projeto |
| Relações descritas apenas como “o bloco anterior” e “a próxima aula” | O aluno sabe a ordem, mas não sabe por que reutiliza aquele resultado | Nomear a entrada concreta e criar um link para ela |
| Repetição extensa do contexto em exercícios | O que deve ser feito se perde entre dados conhecidos | Destacar visualmente dados usados, tarefa e critério, mantendo o enunciado autossuficiente |
| Muitas classificações sem uma pergunta prática ao lado | O aluno memoriza rótulos, mas tem dificuldade para projetar | Explicar que decisão cada classificação ajuda a tomar |
| “Obra”, “vigiar” e outras metáforas recorrentes | A governança parece uma fiscalização distante da prática da equipe | Usar implementação, revisão, aprovação, registro e acompanhamento |
| Exemplos de várias organizações chamadas ACME | Pode parecer que fatos do hospital, banco e universidade pertencem ao mesmo caso | Identificar claramente o contexto de cada exemplo, mantendo todos eles |

Essas observações são uma avaliação editorial do site. Não houve comparação textual com o livro de Mark Lovatt para estabelecer a origem de cada expressão. A bibliografia local identifica o livro como *Solution architecture foundations*.

## Linguagem simples com profundidade preservada

O critério não é reduzir o número de conceitos nem estabelecer uma meta de corte de palavras. Uma explicação pode ficar maior quando um exemplo é necessário. O ganho esperado é diminuir o esforço para compreender cada conceito e relacioná-lo ao projeto.

Para cada passagem revisada:

- Manter a definição, suas condições, exceções e consequências.
- Preferir “quem decide”, “quem executa”, “o que muda” e “como conferir” quando esses sujeitos estavam ocultos.
- Dividir parágrafos densos sem eliminar os encadeamentos causais.
- Explicar o termo formal no ponto em que ele é usado. O glossário complementa essa explicação.
- Distinguir fato do caso, hipótese do aluno, alternativa considerada, proposta e decisão aprovada.
- Manter números, unidades, datas, condições de medição e referências.
- Usar links para aprofundar ou recuperar contexto, sem exigir que o aluno percorra várias páginas para entender uma frase.

### Vocabulário de apoio

As expressões à direita ajudam a explicar o termo. Não são substituições automáticas válidas para qualquer ocorrência.

| Termo encontrado no curso | Explicação de apoio |
| --- | --- |
| Granularidade | Alcance ou nível de detalhe, conforme o contexto |
| Enquadramento | Compreender e delimitar o problema e o contexto |
| Direcionador de mudança | Fato, necessidade ou oportunidade que leva a organização a mudar |
| Modelo operacional | Como a organização distribui e realiza o trabalho |
| Alinhamento estratégico | Como o projeto contribui para os objetivos da organização |
| Capacidade | O que a organização precisa saber fazer |
| Fluxo de valor | Etapas pelas quais uma pessoa recebe o resultado do serviço |
| Processo de negócio | Atividades, decisões e responsabilidades para realizar o trabalho |
| Parte interessada | Pessoa ou grupo que decide, usa, sustenta ou é afetado pela solução |
| Patrocinador | Quem apoia a iniciativa e tem a autoridade atribuída para viabilizá-la |
| Ponto de vista | Regras para preparar uma representação adequada a certas preocupações |
| Visão | Representação produzida seguindo essas regras |
| Artefato | Documento, tabela, diagrama ou modelo usado no trabalho |
| Entregável | Resultado preparado para quem vai avaliar ou utilizar o trabalho |
| Linha de base | Descrição de referência da situação atual |
| Arquitetura alvo | Descrição da solução que se pretende alcançar |
| Lacuna | Diferença que precisa ser tratada entre a situação atual e a pretendida |
| Bloco de construção | Parte da solução descrita por sua responsabilidade ou capacidade |
| Racional arquitetural | Explicação do raciocínio que sustenta a decisão |
| Forças | Fatores que pesam na comparação entre alternativas |
| Mecanismo compensatório | Recurso para reduzir um risco ou uma desvantagem da alternativa |
| Propriedade do dado | Responsabilidade definida sobre o dado, explicitando o sentido organizacional ou técnico usado |
| Fonte de verdade | Registro reconhecido como referência oficial para aquele dado |
| Regime de consistência | Garantias sobre a atualização e a leitura das diferentes versões do dado |
| Modelo técnico de referência | Referência da organização para categorias, padrões e opções de tecnologia |
| Lacuna de provisão | Diferença entre o serviço de infraestrutura necessário e o disponível |
| Zona de pouso | Base compartilhada de nuvem preparada para receber as aplicações |
| Governança | Regras, papéis e rotinas para decidir, acompanhar e tratar mudanças |
| Desvio arquitetural | Diferença entre a implementação e uma decisão de arquitetura vigente |
| Onda de entrega | Grupo de entregas com dependências e critério de conclusão |
| Rastreabilidade | Relações registradas que permitem seguir a origem e os efeitos de cada parte do projeto |

## Contribuição de cada módulo para o projeto

Esta tabela explicita a função do conteúdo atual. Não redistribui temas nem altera o que o aluno entrega.

| Módulo | Contribuição preservada | Foco da revisão de linguagem | Conexões a tornar mais visíveis |
| --- | --- | --- | --- |
| 1 · Fundamentos | Contexto, níveis e componentes da solução, papéis e processo | Explicar alcance, responsabilidade e fases por ações concretas | Contexto com pessoas envolvidas, processo com as entregas posteriores |
| 2 · Requisitos e partes interessadas | Direcionadores, requisitos, cenários, linha de base, restrições e escopo | Explicar o efeito de cada conceito na decisão do projeto | Requisitos com critérios de escolha, atores com autoridade, escopo com domínios |
| 3 · Design e padrões | Princípios, esboço lógico, comparação de estilos e padrões, ADR | Tornar claros critérios, alternativas, custos e justificativas | Decisões com entradas da Aula 2, modelos da Aula 4 e revisões da Aula 6 |
| 4 · Domínios | Negócio, dados, aplicações, integração e infraestrutura | Ajudar a ler e relacionar os diferentes modelos | Capacidades e processos com dados, contratos com interfaces, topologia com cenários |
| 5 · Tecnologia | Definição tecnológica, TRM, plataforma, zona de pouso, segurança e ADR | Explicar escolha, operação, custo, responsabilidade e evidência | Tecnologias com desenho, controles com dados e papéis, lacunas com roteiro |
| 6 · Governança e fechamento | Lacunas, ondas, governança, uso de IA e apresentação do caderno | Mostrar ações concretas de revisão, aprovação e verificação | Todas as seções do projeto com decisões, responsáveis, evidências e pendências |

## Como executar a revisão

Aplicar cada lote sobre a explicação, o exercício, a orientação do template, o gabarito e o glossário relacionados. Isso evita que o aluno leia uma definição simples e encontre uma formulação incompatível quando precisa usá-la.

1. **Fixar as convenções de redação.** Usar o vocabulário de apoio e as restrições de preservação acima. Acompanhar a revisão pelo inventário das 72 páginas.
2. **Revisar os trechos com maior distância da experiência do analista.** Priorizar fundamentos, partes interessadas, negócio e governança, mantendo todos os assuntos e a sequência atual.
3. **Revisar as passagens técnicas e os apoios.** Tornar explícitas as implicações organizacionais e manter os detalhes técnicos necessários para produzir o projeto.
4. **Acrescentar as conexões no ponto de uso.** Usar o mapa de links, preservando as âncoras e os vínculos existentes.
5. **Ajustar os esquemas junto com as passagens que explicam.** Manter as tabelas e descrições que carregam informação não representada na figura.
6. **Conferir a coerência do conjunto.** Revisar as relações entre seções e os pontos listados no documento de conferência.

Os textos dos gabaritos e parte das orientações vêm de `caderno-fonte/`. Uma revisão posterior deve ser feita na fonte e propagada pelo gerador, preservando os marcadores dos exercícios e os modos de acumulação e substituição. Não editar isoladamente as 24 cópias cumulativas. As introduções geradas que estejam no script também precisam ser revistas na sua origem.

## Critérios para aceitar uma revisão

| Critério | Como conferir |
| --- | --- |
| Estrutura preservada | Mesmos módulos, exercícios, seções, campos e critérios de aceitação |
| Profundidade preservada | Todas as definições, distinções, condições, exceções e consequências da passagem original continuam presentes |
| Clareza | O leitor consegue explicar quem faz o quê e para que o conceito serve no projeto |
| Aplicação | O aluno encontra a orientação necessária para produzir a mesma entrega exigida antes da revisão |
| Conexão | É possível localizar as entradas usadas e as partes afetadas pela decisão |
| Fidelidade ao caso | Números, unidades, datas e estados de aprovação não mudaram por simplificação |
| Coerência | Explicação, exercício, template, gabarito e glossário usam as mesmas distinções |
| Navegação | Links abrem a página e a seção previstas, sem quebrar endereços anteriores |
| Visual | A figura responde a uma pergunta definida, tem legenda e descrição textual e não depende só de cores |

Uma verificação pedagógica útil é pedir a um aluno que explique uma decisão do próprio projeto e mostre suas relações com pessoas, processos, modelos, tecnologia e planejamento. Dúvidas observadas nessa tarefa ajudam a ajustar a redação. Este levantamento não realizou teste com alunos, portanto não declara ganho de aprendizagem já medido.

## Abrangência e verificações

A base foi o repositório local em 17/10/2026. Houve inventário estrutural de todas as páginas publicáveis, leitura dirigida de conceitos e trechos dos seis módulos, análise de exercícios e de suas fontes de gabarito, consulta ao caso, glossário e mecanismo de geração. As propostas visuais se baseiam nas figuras referenciadas, legendas e descrições da fonte. Não houve inspeção visual de todos os arquivos de imagem nem conferência página a página da versão publicada.

Esta é uma revisão editorial de largo espectro com intervenções concretas, não uma afirmação de revisão linha a linha de todo o texto. O inventário distingue conteúdo autoral, índices, sínteses e saídas geradas. Planos históricos em `docs/superpowers/` não são material publicado do aluno e não entram nas 72 páginas.

Antes da produção deste relatório, `python3 scripts/gerar_caderno.py --check` retornou **0 divergências**, e `python3 scripts/validate_content.py` retornou **0 violações**. Esses resultados verificam sincronização e regras mecânicas, não a clareza pedagógica nem a validade de todas as afirmações técnicas. A revisão proposta permanece fora da navegação do aluno, na área de auditoria excluída da publicação.
