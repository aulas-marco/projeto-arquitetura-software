# Pontos de coerência para conferir antes da reescrita

Estes itens não propõem alterar a espinha dorsal do curso nem decidir a resposta de conteúdo por conta própria. São relações que merecem uma frase de esclarecimento, uma indicação de estado ou uma conferência da fonte antes de simplificar a redação. Caso contrário, uma formulação mais curta pode esconder uma ambiguidade que o aluno perceberá entre explicação, exercício e gabarito.

## Estados de decisão, hipótese e pendência

| ID | Onde aparece | O que precisa ficar inequívoco | Tratamento editorial proposto |
| --- | --- | --- | --- |
| C01 | Módulos 3 a 6, caderno e gabaritos | A referência apresenta algumas escolhas como “a ACME adota”, mas o ADR correspondente está em estado **proposto** e tem decisor ou data pendente | Usar “a resposta de referência propõe” ou “o ADR registra como proposta” até que a aceitação esteja evidenciada. Manter a diferença entre decisão adotada no exercício e aprovação pela autoridade do caso. |
| C02 | `caderno-fonte/10-pendencias.md`, exercícios 4 a 24 | A lista final preserva pendências cuja data de resolução foi uma fase anterior, como descoberta ou definição do esboço | Identificar explicitamente que são pendências deliberadamente abertas no caso didático, se esse for o objetivo. Caso contrário, reclassificar o estado ou ajustar o marco sem remover a pendência. |
| C03 | Módulo 6, bloco de IA | O modelo pode rascunhar uma decisão, mas não possui autoridade para aprová-la | Manter essa regra no texto, nos exemplos e no registro de assistência. Distinguir organização de argumentos, recomendação, aprovação e responsabilidade. |

## Origem de restrições e categorias

| ID | Onde aparece | O que precisa ficar inequívoco | Tratamento editorial proposto |
| --- | --- | --- | --- |
| C04 | Módulo 2, bloco 1; caso ACME; gabarito do exercício 14 | A exigência de processamento em território nacional é descrita ora como fator Legal, ora como decisão institucional apoiada em parecer jurídico, e o gabarito afirma que não é exigência direta da LGPD | Escolher e repetir uma formulação precisa: uma política/restrição institucional apoiada em parecer jurídico, ou outra origem sustentada por fonte. Na PESTLE, explicar por que ela é analisada como pressão legal sem afirmar que a lei exige residência nacional. |
| C05 | Módulo 2, blocos 3 e 4; caso ACME | Restrição, requisito e decisão de projeto têm autoridades e formas de revisão diferentes | Em cada passagem, usar uma frase-padrão: “quem impôs”, “quem pode rever” e “o que a equipe pode decidir dentro desse limite”. Isso é especialmente importante para contratos, orçamento e políticas. |
| C06 | Módulo 4, dados; glossário | “Dono do dado”, “fonte de verdade”, “sistema de registro” e permissão técnica de gravação podem ser interpretados como a mesma coisa | Manter a diferenciação textual: responsabilidade pelo dado, registro oficial e mecanismo técnico de escrita. O exercício pode continuar usando a regra de um único responsável, desde que explique o sentido adotado. |

## Dependências e sequências do projeto

| ID | Onde aparece | O que precisa ficar inequívoco | Tratamento editorial proposto |
| --- | --- | --- | --- |
| C07 | Módulo 1, bloco 1, exercício 1; caderno-fonte/01-contexto.md | O reenvio com intervalo crescente (D3) é apresentado como dependente da decisão de enviar nota em até dez minutos (D2) | Explicar que a dependência existe porque o caso passa a tratar envios individuais e confirmação de recebimento. Não sugerir que um mecanismo de reenvio jamais possa existir para um lote. |
| C08 | Módulo 4, bloco 0 | A ordem negócio, dados, aplicações e infraestrutura é apresentada como percurso de detalhamento | Manter a ordem didática e de rastreabilidade, mas deixar explícito que ela não impede retornos e ajustes entre domínios quando uma descoberta posterior exige revisão. Isso é coerente com a realimentação já apresentada no processo da Aula 1. |
| C09 | Módulo 6, roteiro e governança | O roteiro em ondas, o cronograma e o primeiro ciclo de 12 meses têm níveis de detalhe distintos | Repetir a distinção: roteiro mostra entregas e dependências; cronograma detalha tarefas, datas e pessoas; ciclo é o recorte de investimento e resultado aprovado. |

## Consistência entre modelos e evidências

| ID | Onde aparece | O que precisa ficar inequívoco | Tratamento editorial proposto |
| --- | --- | --- | --- |
| C10 | Módulo 4, aplicações e infraestrutura; exercícios 15 e 16 | Um diagrama C4 de contexto mostra fronteira e relações de alto nível; o diagrama de contêineres detalha partes executáveis | Nas legendas e nos exercícios, reforçar que banco e contêiner não pertencem ao nível de contexto. Manter a explicação da fronteira de responsabilidade, inclusive para o núcleo mantido por fornecedor. |
| C11 | Módulo 4, dados; exercício 14 | O prazo “até um dia” é uma suposição adotada quando o dossiê não apresenta exigência | Rotular visualmente como hipótese de referência, com responsável pela confirmação. Não deixá-lo parecer dado medido do caso. |
| C12 | Módulos 3 a 5; ADRs | Teste de carga, prova de conceito e outras evidências podem estar ausentes, desejáveis ou disponíveis | Padronizar os estados “disponível”, “a produzir” e “não aplicável”. Evitar que uma evidência desejada pareça resultado obtido. |
| C13 | Módulo 5, blocos 1 e 4 | Matriz de seleção compara alternativas com dados incompletos; o ADR registra a decisão de referência | Em cada critério sem dados, registrar o que falta, quem fornece e o efeito sobre a confiança da comparação. Manter a possibilidade de resultado diferente quando a evidência real mudar. |
| C14 | Módulo 4, exercício 16, caderno e Módulo 5 | O catálogo de ABBs precisa refletir o C4 do primeiro ciclo e separar responsabilidades lógicas de dependências externas | Aplicado em 17/10/2026: os três pontos agora usam os mesmos 12 blocos. Portal do Professor e Portal da Secretaria entram como blocos modificados. Evento de nota, camada anticorrupção e observabilidade são transversais e não exigem caixas próprias no C4. Ambiente virtual, gateway, ERP, assinador e órgão regulador ficam como dependências externas. |

## Terminologia que merece estabilização

| Termo ou relação | Orientação |
| --- | --- |
| Projeto de Arquitetura de Solução e caderno arquitetural | O projeto é o trabalho e o conjunto de decisões, modelos e planejamento produzidos pelo aluno. O caderno é o documento que reúne e comunica esse projeto. Usar os dois termos sem fazer um parecer o outro. |
| Arquitetura de solução e arquitetura de software | Repetir o critério do alcance da decisão. Não usar “mais alto” como sinônimo de melhor nem assumir que a execução técnica deixa de ser uma preocupação da arquitetura de solução. |
| Parte interessada, patrocinador e autoridade | Uma parte interessada pode informar, usar, sustentar ou ser afetada. Patrocínio e aprovação exigem autoridade atribuída. Não inferir autoridade apenas por interesse ou cargo. |
| Padrão técnico, padrão arquitetural e padrão de design | Preservar a distinção já ensinada. Inserir explicação curta antes de usar “padrão” isoladamente em uma frase que possa gerar ambiguidade. |
| Proposta, aceita, rejeitada e pendente | Sempre apresentar o estado quando a passagem descreve uma decisão do caso, um ADR ou uma recomendação de gabarito. |
| Exemplo ACME | Hospital ACME, Banco ACME e outros exemplos devem ser identificados como cenários distintos da Universidade ACME, para que números, restrições e decisões não sejam misturados. |

## Conferência mínima após cada lote de edição

- A explicação do bloco, o exercício, a orientação do caderno, o gabarito e o glossário continuam usando a mesma definição.
- Um link novo aponta à âncora que responde à pergunta apresentada pelo texto de origem.
- A mudança não converte hipótese em fato, proposta em decisão aceita ou restrição em requisito negociável.
- Números, unidades, condições, datas, responsabilidades e fontes permanecem preservados.
- A revisão não remove nenhuma seção, item, campo, critério de aceitação, exemplo ou entrega do Projeto de Arquitetura de Solução.
