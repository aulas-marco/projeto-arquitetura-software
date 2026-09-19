# Arquitetura de software e o papel do arquiteto

Este bloco responde a uma pergunta anterior a qualquer decisão técnica, o que é arquitetura de software, o que cabe ao arquiteto decidir e como ele enquadra um problema antes de propor solução.

## Antes de começar

- [Arquitetura de software](../referencia/glossario.md#arquitetura-de-software)
- [Arquiteto de software](../referencia/glossario.md#arquiteto-de-software)
- [Restrição](../referencia/glossario.md#restricao)
- [Direcionador arquitetural](../referencia/glossario.md#direcionador-arquitetural)

## Conceito

**Arquitetura de software** é o conjunto das decisões estruturais fundamentais sobre um sistema, decisões difíceis de reverter depois de tomadas, que determinam como esse sistema se comporta além do que ele executa, em propriedades como o modo como ele escala, resiste a falha ou se adapta a mudança. Essas decisões definem os elementos que compõem o sistema, as conexões entre eles e as restrições que essa organização impõe às etapas seguintes do projeto.

A distinção entre decisão arquitetural e decisão de implementação está no custo de reversão e no alcance do efeito. Uma **decisão arquitetural** condiciona partes do sistema que ainda não existem e é cara de desfazer depois que o desenvolvimento avança sobre ela. Uma decisão de implementação afeta um trecho localizado de código e pode ser revista sem repercussão sobre o restante do sistema. Em um sistema de comércio eletrônico, decidir que o catálogo de produtos e o processamento de pedidos são serviços separados, comunicados por mensageria assíncrona, é decisão arquitetural, porque condiciona como cada parte pode escalar e falhar de forma independente. Escolher a estrutura de dados usada para ordenar os itens de uma página de resultado é decisão de implementação, porque pode ser trocada sem afetar a separação entre catálogo e pedidos. Em um sistema de controle industrial, decidir que os controladores de chão de fábrica se comunicam com a camada de supervisão por um protocolo com garantia de entrega e limite de latência é decisão arquitetural, porque qualquer componente futuro do sistema de supervisão herda essa restrição. Ajustar o intervalo de repetição de uma rotina de leitura de sensor é decisão de implementação, porque não altera o contrato entre as camadas.

O arquiteto de software é o profissional responsável por tomar e documentar essas decisões estruturais, conciliando demandas conflitantes de diferentes partes interessadas com os requisitos funcionais e as restrições de negócio do projeto. O arquiteto decide a organização geral do sistema, a divisão de responsabilidades entre seus elementos principais, as tecnologias e plataformas de base e os pontos de integração entre componentes internos e sistemas externos. Para tomar essas decisões, o arquiteto interage com as áreas de negócio interessadas no resultado do sistema, com os times de desenvolvimento que constroem sobre a estrutura definida e, quando o domínio exige, com especialistas em segurança, dados ou infraestrutura.

Não é responsabilidade do arquiteto definir o detalhe interno de cada módulo, escolher nomes de variáveis ou algoritmos locais, nem conduzir a gestão do cronograma do projeto. No sistema de comércio eletrônico com catálogo e pedidos separados, descrito no parágrafo anterior desta seção Conceito, cabe ao arquiteto decidir que catálogo e pedidos são serviços separados, e cabe ao time de desenvolvimento decidir como o serviço de catálogo indexa seus produtos internamente. No sistema de controle industrial, cabe ao arquiteto decidir o protocolo entre chão de fábrica e supervisão, e cabe à equipe de automação decidir o algoritmo de filtragem de ruído de um sensor específico.

A primeira atividade do processo de arquitetura é o **enquadramento do problema**, e não a escolha de uma solução. Enquadrar o problema significa identificar o que a organização busca com o sistema, quem tem autoridade para decidir cada tipo de questão e quais restrições já chegam fechadas, impostas por fatores fora do controle do arquiteto. No sistema de comércio eletrônico, a decisão de operar em um único provedor de nuvem já contratado pela organização é uma restrição que elimina alternativas de arquitetura multinuvem, antes mesmo de qualquer discussão sobre estilo. No sistema de controle industrial, a exigência regulatória de retenção de registros de operação por um número mínimo de anos restringe as opções de armazenamento antes de qualquer decisão sobre desempenho. Um **direcionador arquitetural**, seja de negócio ou técnico, orienta essas decisões antes de se traduzir em requisitos específicos, e reconhecê-lo cedo evita que o arquiteto avalie alternativas que a própria organização já descartou.

![Diagrama em três painéis conectados por setas, seguidos de uma barra final. O primeiro painel, Enquadrar o problema, lista objetivos de negócio, autoridade para decidir e restrições já definidas, com a nota de que direcionadores orientam as alternativas viáveis. O segundo, Decisões arquiteturais, mostra dois componentes, Catálogo e Pedidos, ligados por mensageria assíncrona, cada um com espaço para componentes futuros, ao lado dos atributos de qualidade escalabilidade, resiliência e adaptabilidade, com a etiqueta alto alcance e difícil de reverter. O terceiro, Implementação, mostra um trecho de código que ordena itens por preço, com a etiqueta efeito local e fácil de rever. A barra final resume o papel do arquiteto: organiza elementos, define integrações, documenta decisões, concilia necessidades, e não define detalhes internos, variáveis ou algoritmos locais.](../assets/images/bloco-1-ciclo-decisao-arquitetural.png)

*Figura 1 — O ciclo de enquadramento, decisão arquitetural e implementação, com o papel do arquiteto em cada etapa. Fonte: material do curso.*

A figura resume a distinção feita acima. O enquadramento identifica objetivos, autoridade e restrição antes de qualquer decisão. As decisões arquiteturais, como separar catálogo e pedidos por mensageria assíncrona, têm alto alcance e são difíceis de reverter. As decisões de implementação, como a estrutura interna de uma rotina de ordenação, têm efeito local e são fáceis de rever. O arquiteto atua nas duas primeiras etapas, organizando elementos, definindo integrações, documentando decisões e conciliando necessidades conflitantes, sem entrar no detalhe interno que a terceira etapa resolve.

## Uso pelo arquiteto

No dia a dia, o arquiteto aplica essa distinção para decidir onde investir tempo de análise, reservando profundidade de avaliação para as decisões estruturais difíceis de reverter e delegando ao time de desenvolvimento as decisões locais que a estrutura já comporta. Antes de propor qualquer solução, o arquiteto levanta quem decide o quê na organização e quais restrições já estão fechadas, para não gastar esforço em alternativas que nunca poderiam ser adotadas.

## Exercício 1

A ACME é uma universidade privada brasileira, de porte consolidado, cujo sistema acadêmico foi construído ao longo de duas décadas e sustenta matrícula, avaliação, emissão de documentos e integração financeira. A instituição está em processo de modernização desse sistema legado.

O quadro abaixo reproduz o mapa de atores da ACME, com o papel, o que cada um busca e o que teme.

| Papel | O que quer | O que teme |
| --- | --- | --- |
| Reitora | Resultado visível em 12 meses e aplicativo móvel do aluno em operação antes do vestibular de 2027 | Investimento de R$ 6,2 milhões sem efeito perceptível e queda de nota na avaliação regulatória |
| Pró-Reitora de Graduação | Matrícula sem falha e notas publicadas dentro do calendário | Repetição de incidente na janela de matrícula e nova prorrogação |
| Diretor de TI | Reduzir a dependência de especialistas em COBOL e o custo anual de manutenção do sistema | Perder os profissionais de COBOL e ficar sem quem sustente o núcleo |
| Diretor Financeiro | Preservar os contratos vigentes até o fim do prazo, já provisionados no plano plurianual | Desembolso duplicado, com legado e nuvem cobrados no mesmo exercício |
| Gerente de sustentação | Manter o escopo e a previsibilidade do contrato de sustentação até o fim de sua vigência | Perder receita e escopo com a internalização do conhecimento do núcleo |
| Coordenadora de Educação a Distância | Notas e turmas propagadas ao ambiente virtual de aprendizagem em minutos | Continuar dependente do lote diário, com reclamação de aluno a cada fechamento |
| Encarregada de proteção de dados | Conformidade com a LGPD, base legal declarada e trilha de auditoria sobre dado pessoal | Transferência de dado de aluno para fora do território nacional sem amparo |
| Representação discente | Aplicativo móvel e matrícula que não falhe na abertura | Perda de vaga em disciplina por indisponibilidade do portal |

As restrições abaixo chegam fechadas ao arquiteto, impostas por decisão anterior ao projeto.

| Restrição | Origem |
| --- | --- |
| O sistema acadêmico não pode parar em período letivo | Pró-Reitoria de Graduação |
| O ambiente virtual de aprendizagem e o ERP financeiro permanecem, o trabalho é de integração e governança, não de substituição | Reitoria |
| Apenas dois provedores de nuvem pré-aprovados podem ser usados | Conselho Universitário |
| Identidade e autorização seguem padrões abertos, não um produto proprietário | Comitê de Segurança da Informação |
| Dado pessoal de aluno é processado em território nacional | Jurídico |
| A manutenção do núcleo COBOL permanece sob contrato de sustentação até 30/09/2027 | Contrato de sustentação |
| O roteiro de evolução cabe em um orçamento de R$ 6,2 milhões para o primeiro ciclo de 12 meses | Reitoria |

Responda às três perguntas abaixo.

1. O que a instituição quer do sistema acadêmico, considerando os interesses que aparecem em mais de um papel.
2. Quem, entre os papéis listados, tem autoridade para decidir sobre orçamento, sobre padrão de identidade e sobre prazo de contrato de sustentação, e por quê.
3. Qual das sete restrições, isoladamente, elimina a alternativa de reescrever o sistema acadêmico inteiro em uma única entrega, e qual elimina a alternativa de substituí-lo por um produto de mercado.

## Fontes

Glossário do curso, entradas [arquitetura de software](../referencia/glossario.md#arquitetura-de-software), [arquiteto de software](../referencia/glossario.md#arquiteto-de-software) e [direcionador arquitetural](../referencia/glossario.md#direcionador-arquitetural). Bass, L., Clements, P. e Kazman, R., Software Architecture in Practice, listado na [bibliografia](../referencia/bibliografia.md). ISO/IEC/IEEE 42010:2022, listada na [bibliografia](../referencia/bibliografia.md). Dossiê da instituição fictícia [ACME](../caso-acme/index.md), mapa de atores e restrições fechadas.
