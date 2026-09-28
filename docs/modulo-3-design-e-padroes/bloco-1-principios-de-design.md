# Princípios de design e passagem ao desenho lógico

Este bloco inicia a cadeia de decisão da aula e responde a uma pergunta anterior a qualquer escolha de estilo ou de tecnologia, que regras devem orientar o desenho da solução e como essas regras produzem um primeiro desenho lógico.

## Antes de começar

- [Princípio de design](../referencia/glossario.md#principio-de-design)
- [Desenho conceitual](../referencia/glossario.md#desenho-conceitual)
- [Desenho lógico](../referencia/glossario.md#desenho-logico)
- [Requisito de atributo de qualidade](../referencia/glossario.md#requisito-de-atributo-de-qualidade)
- [Restrição](../referencia/glossario.md#restricao)

## Princípios de design

A Aula 2 terminou com entradas arquiteturais já formuladas, os direcionadores de mudança, os requisitos classificados, os cenários de atributo de qualidade com medida e as restrições que chegam fechadas ao arquiteto. Nenhuma dessas entradas diz, sozinha, como a solução deve ser organizada. Entre a lista de exigências e o desenho existe uma etapa intermediária, na qual o arquiteto converte as entradas em regras que orientam muitas decisões ao mesmo tempo, e é essa etapa que este bloco trata.

### Do objetivo ao elemento lógico

Cinco conceitos aparecem juntos em qualquer discussão de desenho, e a confusão entre eles é a origem de boa parte das decisões mal justificadas. A tabela abaixo fixa o papel de cada um.

| Conceito | Papel |
| --- | --- |
| Objetivo | Resultado de negócio pretendido |
| Requisito | Necessidade, capacidade, condição ou restrição verificável |
| Princípio | Regra durável que orienta um conjunto de decisões |
| Decisão | Escolha situada entre alternativas |
| Elemento lógico | Responsabilidade ou colaboração sem compromisso prematuro com tecnologia |

Uma rede de clínicas com doze unidades ilustra o encadeamento. O objetivo é reduzir de 18% para 8% a taxa de pacientes que faltam à consulta agendada. Um requisito derivado desse objetivo é que o paciente receba lembrete 48 horas antes da consulta e possa confirmar ou cancelar pela mesma mensagem. Um princípio que orienta várias decisões a partir desse requisito é que a agenda de cada unidade seja a única fonte de verdade sobre horários, de modo que nenhum canal de comunicação mantenha cópia própria da disponibilidade. Uma decisão situada é devolver o horário cancelado à agenda da unidade no mesmo instante do cancelamento. O elemento lógico resultante é um serviço de agendamento que publica os horários disponíveis e recebe as confirmações, descrito apenas pela responsabilidade que assume e pelas interfaces que oferece, sem produto de mensageria nem banco de dados escolhidos.

### Anatomia de um princípio

Um **princípio de design** é uma regra durável, derivada de objetivos, requisitos e restrições, que orienta um conjunto de decisões de desenho e admite verificação da sua aplicação. Lovatt (2021, seção 2.2) observa que princípios, políticas e regras de negócio da arquitetura corporativa se aplicam a toda solução da organização, e que a exceção tática a essas diretrizes gera uma dívida estratégica a ser corrigida depois. Os princípios de uma solução específica ocupam o nível seguinte, porque refinam as diretrizes corporativas para o problema em análise sem contrariá-las.

Um princípio só cumpre essa função quando traz três complementos ao nome. A motivação liga o princípio à entrada que o originou, seja um objetivo, um cenário ou uma restrição, e é o que impede sua adoção por hábito. A implicação prática declara o que muda no desenho quando o princípio é seguido, incluindo o que passa a ser proibido. A forma de verificação indica que evidência mostraria que o princípio foi respeitado, como uma revisão de dependências, um teste automatizado ou uma métrica de operação.

Uma lista de princípios genéricos copiada de outra organização, sem motivação e sem implicação, não constitui arquitetura. Enunciados como "o sistema deve ser escalável" ou "usar boas práticas" não excluem nenhuma alternativa de desenho e, por isso, não orientam decisão alguma. O teste prático consiste em perguntar que alternativa o princípio elimina, e um princípio que não elimina nenhuma precisa ser reescrito ou retirado da lista.

### Repertório de princípios

A tabela abaixo reúne nove princípios recorrentes na literatura de arquitetura. Eles servem de repertório para a derivação e não como lista a adotar integralmente, porque cada solução seleciona e prioriza apenas os que suas entradas justificam.

| Princípio | Motivação típica | Implicação no desenho | Evidência de aplicação |
| --- | --- | --- | --- |
| Simplicidade | Custo de entendimento e de manutenção proporcional ao número de partes | Cada elemento novo precisa responder a uma exigência nomeada | Nenhum elemento sem requisito ou cenário associado |
| Separação de responsabilidades | Mudanças de natureza diferente ocorrem em ritmos diferentes | Regra de negócio, apresentação e integração ficam em elementos distintos | Alteração de regra sem mudança em interface de usuário |
| Baixo acoplamento | Falha ou mudança em uma parte não deve se propagar às demais | Elementos se comunicam por interfaces declaradas, sem acesso ao dado interno alheio | Grafo de dependências sem acesso direto a dado de outro elemento |
| Alta coesão | Responsabilidades relacionadas mudam juntas | Cada elemento reúne o que muda pelo mesmo motivo | Mudanças típicas contidas em um único elemento |
| Encapsulamento | Detalhe interno exposto torna-se dependência involuntária | O elemento expõe operações e oculta estrutura de dado e tecnologia | Consumidores sem referência a tabela ou formato interno |
| Desenho para falha | Toda dependência externa falha em algum momento | Cada interação declara tempo limite, comportamento degradado e recuperação | Teste de falha provocada com resposta dentro da medida do cenário |
| Observabilidade | Falha que não se vê não se diagnostica | Cada fluxo relevante emite métricas, registros e rastreamento correlacionáveis | Reconstrução de uma operação a partir dos registros |
| Segurança por desenho | Controle acrescentado depois tende a deixar lacunas | Identidade, autorização e proteção de dado são responsabilidades explícitas do desenho | Trilha de auditoria e matriz de acesso verificáveis |
| Evolução incremental | Mudança grande em uma única entrega concentra risco | O desenho admite substituição parte a parte, com convivência entre o antigo e o novo | Entregas parciais em produção sem interrupção do serviço |

Princípios entram em conflito, e a priorização faz parte do produto. No serviço municipal de licenciamento de uma prefeitura, que emite alvarás de funcionamento para cerca de 9.000 estabelecimentos por ano, a simplicidade favorece um único fluxo síncrono entre o pedido, a consulta aos cadastros da vigilância sanitária e do corpo de bombeiros e a emissão do documento. O desenho para falha, motivado pela indisponibilidade frequente do cadastro dos bombeiros, exige que o pedido seja registrado mesmo quando uma das consultas não responde, o que acrescenta estado intermediário e reprocessamento. A escolha entre os dois não é técnica em abstrato, ela depende de qual entrada tem prioridade para a prefeitura, e o registro dessa prioridade evita que a mesma discussão seja reaberta a cada decisão subsequente.

### Do conceitual ao lógico

Lovatt (2021, seções 3.5 e 3.7) descreve uma hierarquia de idealização que vai do conceitual ao lógico e deste ao físico. O **desenho conceitual** descreve a solução em termos de capacidades, responsabilidades e relações com o ambiente, em nível alto o suficiente para que as partes interessadas avaliem a abordagem sem que o desenho final fique restringido antes da análise. O **desenho lógico** descreve a solução em elementos lógicos com responsabilidades, interfaces e fluxos declarados, e Lovatt o caracteriza como lógico porque trata de componentes e de suas interações, e não da implementação física, que exige trabalho de engenharia posterior.

A passagem do conceitual ao lógico é uma transformação progressiva, que Lovatt (2021, seção 3.6) apoia na análise de blocos de construção e na análise de interfaces. O roteiro abaixo organiza essa transformação em cinco passos.

1. identificar capacidades e responsabilidades
2. agrupar responsabilidades coesas
3. declarar interfaces e fluxos
4. aplicar restrições e princípios
5. localizar riscos e decisões pendentes

No serviço municipal de licenciamento, o primeiro passo identifica as capacidades de receber pedido, verificar exigências sanitárias, verificar exigências de segurança contra incêndio, calcular taxa, emitir alvará e notificar o requerente. O segundo passo agrupa essas capacidades em quatro elementos lógicos, atendimento ao requerente, análise de exigências, cobrança e emissão, porque as duas verificações mudam pelo mesmo motivo, que é a alteração de norma técnica. O terceiro passo declara que o atendimento entrega o pedido à análise, que a análise consulta os dois cadastros externos e devolve um parecer, e que a emissão só ocorre depois da confirmação de pagamento pela cobrança. O quarto passo aplica o princípio de desenho para falha e acrescenta à análise a responsabilidade de manter o pedido pendente quando um cadastro não responde. O quinto passo registra como risco a indisponibilidade do cadastro dos bombeiros e como decisão pendente o prazo máximo de pendência antes de o requerente ser avisado. Em nenhum dos cinco passos aparece linguagem de programação, provedor de nuvem, banco de dados ou framework, porque essas escolhas pertencem às aulas 4 e 5.

<figure markdown="span">
![Diagrama da passagem das entradas arquiteturais ao desenho lógico. Na faixa superior, objetivo, requisito e restrição, princípio, decisão e elemento lógico aparecem ligados por setas da esquerda para a direita. Na faixa inferior, cinco etapas numeradas mostram a transformação do conceitual ao lógico, identificar responsabilidades, agrupar por coesão, declarar interfaces e fluxos, aplicar restrições e princípios, e localizar riscos e decisões pendentes.](../assets/images/modulo-3-principios-ao-desenho-logico.svg){ .module-diagram }
</figure>

*Figura 1 — Cadeia das entradas arquiteturais até o desenho lógico e os cinco passos da passagem do conceitual ao lógico. Fonte: material do curso, com base em Lovatt (2021, seções 3.5 a 3.7).*

### Aplicação à ACME

Na ACME, universidade privada brasileira fictícia usada como caso da disciplina, quatro entradas já levantadas na Aula 2 têm efeito direto sobre a distribuição de responsabilidades lógicas. A continuidade operacional exige que qualquer elemento novo conviva com o núcleo legado durante a transição. A residência de dados delimita onde cada responsabilidade que manipula dado pessoal de aluno pode ser executada. A redução da dependência do legado pede que responsabilidades hoje concentradas no núcleo possam ser assumidas por elementos novos, uma a uma. A propagação de notas em minutos coloca em questão a responsabilidade hoje atribuída ao lote noturno. O exercício deste bloco pede ao aluno que transforme essas quatro entradas em princípios e em um esboço lógico.

## Uso pelo arquiteto

O arquiteto usa princípios priorizados para tomar decisões sucessivas com o mesmo critério, sem reabrir a cada escolha a discussão sobre o que a solução deve privilegiar. Os mesmos princípios servem para revisar um desenho proposto por outra equipe, porque a pergunta passa a ser se o desenho respeita as regras acordadas e a evidência declarada, e não se agrada a quem revisa. O esboço lógico produzido a partir deles é o objeto sobre o qual o estilo arquitetural do bloco 2 e os padrões do bloco 3 serão escolhidos.

## Exercício 9

Este exercício é realizado fora do horário de aula, como atividade de aplicação do conceito apresentado neste bloco ao caso da instituição fictícia ACME.

A ACME é uma universidade privada brasileira com 38.400 alunos ativos, cujo sistema acadêmico, em operação desde 2004, passa por modernização incremental. As quatro entradas abaixo foram reproduzidas da [página inicial do caso](../caso-acme/index.md) e da [arquitetura de linha de base](../caso-acme/linha-de-base.md), com a origem de cada uma.

| Entrada | Conteúdo | Origem |
| --- | --- | --- |
| Continuidade operacional | O sistema acadêmico não pode parar em período letivo, e toda estratégia é incremental, com o legado em operação durante a transição | Pró-Reitoria de Graduação |
| Residência de dados | Dado pessoal de aluno processado em território nacional, o que restringe a região de implantação e o uso de serviços gerenciados | Jurídico, parecer de 28/04/2026 |
| Dependência do legado | Manutenção do núcleo COBOL sob contrato até 30/09/2027, com 6 especialistas, dos quais 2 se aposentam em 2027, e apenas 1 domina o módulo de matrícula | Contrato de sustentação e inventário técnico |
| Propagação de notas | R7, a nota lançada pelo professor chega ao ambiente virtual de aprendizagem em até 10 minutos, contra a exportação atual em lote diário iniciado às 05h10 | Educação a Distância |

1. Derive das quatro entradas entre três e cinco princípios de design. Para cada princípio, registre nome, motivação, implicação no desenho e evidência esperada de que o princípio foi aplicado.
2. Priorize os princípios e justifique, com base nas entradas, qual deles prevalece quando entra em conflito com os demais.
3. Produza um esboço lógico da solução, com os elementos lógicos e a responsabilidade de cada um, sem nomear produto, linguagem, provedor de nuvem ou framework.
4. Marque no esboço ao menos um risco e ao menos uma decisão pendente, indicando qual princípio cada um afeta.

Os princípios priorizados e o esboço lógico deste exercício são a entrada da comparação de estilos do exercício 10, no [bloco 2](bloco-2-estilos-arquiteturais.md).

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seção 2.2, diretrizes da arquitetura corporativa, seções 3.5 a 3.7, desenho conceitual, análise de blocos de construção e de interfaces, e desenho lógico)
- Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley. (atributos de qualidade como critério de desenho)
- Ford, N., & Richards, M. (2020). *Fundamentals of software architecture*. O'Reilly. (acoplamento, coesão e características arquiteturais)

**Material do curso.** O bloco usa as entradas [princípio de design](../referencia/glossario.md#principio-de-design), [desenho conceitual](../referencia/glossario.md#desenho-conceitual) e [desenho lógico](../referencia/glossario.md#desenho-logico) do glossário, além do dossiê da instituição fictícia [ACME](../caso-acme/index.md) e da sua [arquitetura de linha de base](../caso-acme/linha-de-base.md).
