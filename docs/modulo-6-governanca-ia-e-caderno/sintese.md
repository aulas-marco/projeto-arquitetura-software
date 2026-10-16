# Síntese da Aula 6

Depois de quatro exercícios encadeados, o aluno fecha o caderno arquitetural da ACME, e esta página encerra o módulo com o que precisa permanecer depois da aula, a cadeia dos exercícios 21 a 24, uma autoavaliação e a lista das referências citadas nos três blocos.

## Checklist do que precisa permanecer

- A [análise de lacunas](../referencia/glossario.md#analise-de-lacunas) como comparação entre a linha de base e a arquitetura alvo, com a distinção entre lacuna técnica e lacuna organizacional e a forma de fechar cada uma
- O ciclo ADM do TOGAF e as fases E, F, G e H, em que o arquiteto de solução escolhe entre soluções, ordena a migração, vigia a implementação e gere a mudança
- O roteiro de entrega em ondas, com a ordem justificada pela dependência técnica, o critério de conclusão de cada onda e o calendário preso aos contratos, como o da fábrica de software até 30/09/2027
- O desvio arquitetural sob pressão de prazo, os cinco mecanismos de governança contra ele e a definição de quem decide cada tipo de pedido
- As funções de aptidão, testes automáticos que avisam quando uma decisão deixa de ser cumprida, e a governança leve, que só interrompe a obra quando uma regra é violada
- O modelo de linguagem como redator e como crítico, as tarefas que exigem julgamento do arquiteto e a saída plausível e errada como risco central do uso de IA
- A verificação em três etapas, rastreabilidade até a fonte, checagem contra a restrição e revisão por par, a classificação do conteúdo antes de entrar em um prompt e o registro da assistência no ADR
- A regra de rastreabilidade do caderno: toda decisão cita o requisito ou a restrição que a motivou, todo requisito cita a decisão que o atende e toda pendência tem responsável e prazo
- O estado do caderno ao fim da disciplina: as onze seções preenchidas, com o resumo de uma página e as pendências em versão final

## Cadeia da governança e do fechamento do caderno

A aula fecha o caderno por uma cadeia de quatro produtos, e cada exercício consome o produto do anterior.

1. A linha de base e as lacunas de provisão, recebidas das Aulas 2 e 5, dão ao [exercício 21](bloco-1-governanca-da-mudanca.md#exercicio-21) as lacunas a classificar e as entregas a ordenar em ondas.
2. O [exercício 22](bloco-1-governanca-da-mudanca.md#exercicio-22) protege o roteiro em ondas com os mecanismos de governança, a decisão sobre quem aprova cada pedido e as regras que viram função de aptidão.
3. O [exercício 23](bloco-2-aceleradores-de-ia.md#exercicio-23) usa o ADR 001 da Aula 3 para verificar uma saída de IA e registra a assistência, que passa a ser regra de uso de IA no projeto.
4. O [exercício 24](bloco-3-apresentacao-do-caderno.md#exercicio-24) confere o caderno inteiro pela regra de rastreabilidade e escreve as versões finais do resumo e das pendências.

## Autoavaliação

As perguntas abaixo servem para o aluno conferir o que ficou ao fim da disciplina. Ele as responde sozinho, porque elas não têm gabarito, ao contrário dos exercícios: a seção [Gabaritos](../gabaritos/index.md) mostra o caderno arquitetural da ACME preenchido a cada exercício.

1. Dada uma lista de lacunas, é possível separar as técnicas das organizacionais e dizer como fechar cada organizacional.
2. Dadas três entregas e um contrato que impede alterar o núcleo até uma data, é possível ordená-las em ondas e justificar a ordem pelo critério de conclusão.
3. Dada uma situação de desvio sob pressão de prazo, é possível indicar o mecanismo de governança que a trata e quem decide.
4. Dada uma saída de um modelo de linguagem, é possível aplicar as três verificações, apontar o que não tem origem vigente e escrever o registro da assistência.
5. Dada uma tabela de rastreabilidade, é possível apontar a decisão sem origem, o requisito sem decisão e a pendência sem responsável.

## Fontes da aula

As referências seguem o formato APA, 7ª edição. A lista completa está na [bibliografia](../referencia/bibliografia.md) do curso, com a exceção do TOGAF, cuja edição aguarda confirmação.
- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seções 5.1 a 5.7, análise de lacunas, seção 6.7, governança e autoridade de desenho, e seções 8.1 a 8.6, roteiro de entrega, acompanhamento da entrega e apoio à mudança)
- The Open Group. TOGAF Standard, ciclo ADM (fases E a H, fonte conceitual da Figura 1)
- Fowler, M. (n.d.). *Exploring generative AI* [Série de artigos de vários autores, entre eles Birgitta Böckeler, sobre o uso de IA generativa no desenvolvimento de software]. martinfowler.com. Acesso em 16 de outubro de 2026. https://martinfowler.com/articles/exploring-gen-ai.html
- Mendes, M. (2026a). *Arquitetura de software* [Material de curso]. https://marco-mendes.github.io/arquitetura-software/ ([template de ADR](https://marco-mendes.github.io/arquitetura-software/referencia/template-adr/) de dez campos, em que a subseção de assistência de IA se apoia)
- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seção 3.5.3, grade de rastreabilidade entre os elementos do desenho e a visão original da solução, e seção 7.6, teste estático do desenho por rastreabilidade e matriz de rastreabilidade dos requisitos)
