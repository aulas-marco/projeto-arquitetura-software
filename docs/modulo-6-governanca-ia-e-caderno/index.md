# Aula 6, governança, aceleradores de IA e apresentação do caderno

Ao fim da Aula 5, a ACME tinha o caderno arquitetural quase completo e uma pergunta ainda sem resposta: como garantir que a obra, quando começar, siga o desenho que as aulas anteriores produziram? A Aula 6 fecha a disciplina respondendo a essa pergunta em três passos. O primeiro trata da governança da mudança, isto é, de medir a distância entre o sistema de hoje e o sistema desenhado, de ordenar as entregas em ondas e de vigiar a execução. O segundo apresenta os aceleradores de IA, que ajudam o arquiteto a produzir e a conferir artefatos mais depressa, sem lhe tirar a responsabilidade pela decisão. O terceiro percorre o caderno arquitetural completo da ACME e mostra como quem decide o lê.

## Objetivos de aprendizagem

Ao final da aula, o aluno é capaz de

- classificar lacunas entre a situação atual e a arquitetura alvo como técnicas ou organizacionais e ordenar as entregas em ondas pelo critério de conclusão de cada uma
- situar o arquiteto de solução nas fases E, F, G e H do ciclo ADM do TOGAF, em que ele governa a mudança
- associar situações de desvio arquitetural aos cinco mecanismos de governança e indicar quem decide cada pedido
- distinguir o uso do modelo de linguagem como redator e como crítico, e aplicar a verificação em três etapas a uma saída gerada por IA
- registrar a assistência de IA no ADR, com o prompt versionado e o revisor
- conferir a rastreabilidade de um caderno arquitetural e escrever as versões finais do resumo e das pendências

## Grade de tempo

A aula ocorre das 19h00 às 22h30, com intervalo das 20h30 às 20h45, e o tempo de conteúdo encerra até as 22h10. A primeira metade da aula é dedicada à governança, e há um único questionário Kahoot, logo depois do intervalo. Os exercícios são realizados fora do horário de aula, e a tabela abaixo é o único lugar do site em que os minutos de cada bloco aparecem, porque as páginas de bloco não exibem cronômetro.

| Horário | Atividade | Duração (min) |
| --- | --- | --- |
| 19h00–19h15 | Questões sobre a Aula 5 | 15 |
| 19h15–20h30 | Bloco 1, governança da mudança | 75 |
| 20h30–20h45 | Intervalo | 15 |
| 20h45–20h55 | Kahoot de revisão | 10 |
| 20h55–21h28 | Bloco 2, aceleradores de IA | 33 |
| 21h28–22h00 | Bloco 3, apresentação do caderno arquitetural | 32 |
| 22h00–22h10 | Encerramento da disciplina | 10 |

Os três blocos somam 140 minutos de apresentação conceitual, e as questões iniciais, o questionário e o encerramento ocupam os 35 minutos restantes do tempo útil de 175 minutos.

## Entrada recebida da Aula 5

A aula parte do caderno que a Aula 5 deixou pronto: as seções 1 a 8 preenchidas, com a tecnologia e a plataforma escolhidas, a segurança dos dados e o [ADR de plataforma](../modulo-5-frameworks-e-tecnologias/bloco-4-adr-de-plataforma.md#exercicio-20) em estado de proposta. As lacunas de provisão classificadas no exercício 20 entram como matéria-prima da análise de lacunas, e o diagrama de contêineres do [exercício 16](../modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md#exercicio-16) serve de referência para dizer onde cada decisão aparece no desenho.

## Roteiro da aula

A primeira dúvida da ACME é quanto a obra distancia o sistema de hoje do sistema desenhado e em que ordem fechar essa distância, e o [bloco 1](bloco-1-governanca-da-mudanca.md), Governança da mudança, responde a ela com a análise de lacunas, o ciclo ADM do TOGAF e as fases em que o arquiteto de solução governa a mudança, o roteiro em ondas com o critério de conclusão de cada uma, o desvio arquitetural sob pressão de prazo, os cinco mecanismos de governança, as funções de aptidão e a governança leve. No exercício 21, o aluno classifica oito lacunas, define como fechar as organizacionais e ordena três entregas em ondas. No exercício 22, associa cinco situações de desvio aos mecanismos, indica quem decide quatro pedidos e separa as regras que viram função de aptidão.

A produção dos artefatos consome tempo do arquiteto, e o [bloco 2](bloco-2-aceleradores-de-ia.md), Aceleradores de IA, mostra onde um modelo de linguagem ajuda e onde ele erra com aparência de acerto. O bloco apresenta o modelo como redator e como crítico, as tarefas que exigem julgamento do arquiteto, a saída plausível e errada, a verificação em três etapas, o cuidado com dado confidencial em prompt e o registro da assistência no ADR. O exercício 23 entrega um rascunho de ADR gerado por IA com erros plantados, e o aluno verifica o texto, aponta a consequência omitida, corrige o que pertence à autoridade e escreve o registro da assistência.

Por fim, o caderno precisa chegar a quem decide, e o [bloco 3](bloco-3-apresentacao-do-caderno.md), Apresentação do caderno arquitetural, percorre as onze seções do caderno completo da ACME, mostra o que cada leitor procura, apresenta os catorze artefatos do ciclo e segue o requisito R6 do portal ao controle da obra. O exercício 24 entrega a tabela de rastreabilidade da ACME com inconsistências, e o aluno as aponta, escreve a versão final do resumo de uma página e fecha a lista de pendências.

A [síntese](sintese.md) fecha o módulo com o checklist do que precisa permanecer, a cadeia dos exercícios 21 a 24, a autoavaliação e a lista das referências citadas nos três blocos.

## Adições no Caderno Arquitetural da Aula 6

Ao fim da Aula 5, o caderno da ACME dizia o que construir, com que tecnologia e como proteger o resultado, mas não dizia em que ordem entregar, quem vigia a obra nem como usar IA no projeto. Os quatro exercícios desta aula fecham essas lacunas: as lacunas e o roteiro em ondas entram nas seções 4 e 9, a governança do desvio e as regras de uso de IA entram na seção 9, e a conferência final reescreve o resumo de uma página e as pendências, nas seções 0 e 10. O caderno que sai da Aula 6 é o do [gabarito do exercício 24](../gabaritos/gabarito-exercicio-24.md), o caderno completo da disciplina.

{{trilha:9}}

| Bloco | Exercício | O que entra no caderno | Gabarito |
| --- | --- | --- | --- |
| 1 | 21 | A classificação de oito lacunas por domínio e tipo, a forma de fechar as organizacionais e a ordem das três ondas com o critério de conclusão | [Gabarito 21](../gabaritos/gabarito-exercicio-21.md) |
| 1 | 22 | O mecanismo contra cada situação de desvio, quem decide cada pedido e as regras que viram função de aptidão | [Gabarito 22](../gabaritos/gabarito-exercicio-22.md) |
| 2 | 23 | A verificação do rascunho de ADR gerado por IA, a consequência omitida, a correção do estado e da data e o registro da assistência | [Gabarito 23](../gabaritos/gabarito-exercicio-23.md) |
| 3 | 24 | A conferência de rastreabilidade, o resumo final de uma página e a lista final de pendências | [Gabarito 24](../gabaritos/gabarito-exercicio-24.md) |

## Encerramento da disciplina

Com o exercício 24, o caderno arquitetural da ACME está completo, e os 24 exercícios formam um único documento, da instituição e do problema na seção 1 até as pendências finais na seção 10. O [mapa do caderno](../caderno/mapa.md) mostra qual exercício preencheu cada seção, e o [cronograma](../cronograma.md) traz a sequência das seis aulas e a distribuição de pontos.
