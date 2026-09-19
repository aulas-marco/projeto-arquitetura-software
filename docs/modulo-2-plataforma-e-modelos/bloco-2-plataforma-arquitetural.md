# Plataforma arquitetural

Este bloco dá sequência à aula respondendo a uma pergunta que só faz sentido depois do estilo já decidido, qual conjunto de tecnologias concretiza esse estilo na prática de desenvolvimento e operação.

## Antes de começar

- [Plataforma arquitetural](../referencia/glossario.md#plataforma-arquitetural)

## Conceito

Uma **plataforma arquitetural** é o conjunto de frameworks, bibliotecas e ferramentas que concretiza, na prática de desenvolvimento e operação, um estilo arquitetural já decidido. A plataforma não escolhe o estilo, ela o executa. Por isso essa decisão vem depois da decisão de estilo, nunca antes ou junto — decidir framework, banco de dados ou orquestrador de execução antes de fixar o padrão estrutural do sistema inverte a ordem de dependência entre as duas decisões, porque a plataforma que serviria bem a um estilo pode servir mal a outro.

A relação entre estilo e plataforma não é de um para um. Uma mesma plataforma pode concretizar mais de um estilo, como um orquestrador de execução distribuída capaz de sustentar tanto uma arquitetura de microsserviços quanto uma arquitetura em camadas dividida em processos separados. E um mesmo estilo pode ser implementado por mais de uma plataforma candidata, como uma arquitetura orientada a eventos que aceita como intermediário tanto uma fila de mensagens quanto um barramento de streaming, cada um com maturidade, custo e curva de aprendizado próprios. É essa segunda situação, estilo já fixo e mais de uma plataforma capaz de sustentá-lo, que exige do arquiteto uma comparação explícita entre candidatas, não uma escolha por familiaridade ou por moda de mercado.

Cinco critérios organizam essa comparação de forma recorrente. Maturidade mede o tempo de uso da plataforma em produção e a estabilidade das suas versões majoritárias. Custo de licenciamento ou de operação cobre tanto a licença de software quanto o consumo de infraestrutura sob demanda. Disponibilidade de mão de obra qualificada pergunta se o mercado de trabalho local, ou a equipe já contratada, domina a plataforma candidata, porque uma plataforma tecnicamente superior que ninguém sabe operar tem custo real maior do que o preço de licença sugere. **Aderência ao estilo já escolhido** avalia se a plataforma exige extensão ou contorno para sustentar o padrão estrutural definido, ou se o implementa de forma direta. **Compatibilidade com o que já existe no ambiente** pesa a favor ou contra uma plataforma candidata conforme ela precise, ou não, coexistir com sistema legado em operação, caso mais visível no cenário de modernização incremental da ACME, cujo núcleo COBOL sobre CICS segue em produção durante toda a transição.

Um sistema de emissão de bilhetes para eventos que já decidiu por uma arquitetura orientada a eventos, para absorver o pico de venda na abertura de vendas de um show, ainda precisa escolher entre duas plataformas candidatas de mensageria com garantias de entrega diferentes, decisão que só faz sentido depois de o estilo estar fixo. Uma plataforma de telemedicina que optou por microsserviços para isolar consulta por vídeo, prontuário e agendamento enfrenta a mesma segunda decisão, entre um conjunto de frameworks e ferramentas de orquestração e outro, cada um aderente ao estilo de formas distintas e com custo de operação diferente. Em nenhum dos dois casos o nome de um produto específico substitui essa análise, o nome do produto é apenas o rótulo de uma opção concreta depois que os critérios acima já filtraram as candidatas viáveis.

## Uso pelo arquiteto

O arquiteto documenta essa comparação antes de decidir, em um **quadro comparativo** que lista as plataformas candidatas nas linhas e os critérios do Conceito nas colunas, com uma nota curta em cada célula sobre como aquela plataforma se sai naquele critério. Esse quadro entra no ADR de plataforma como evidência de que a escolha considerou alternativas reais, não apenas a plataforma mais familiar ao time, o que faz a decisão resistir a questionamento meses depois, quando quem pergunta por que aquela plataforma foi escolhida encontra o raciocínio registrado, não apenas o resultado.

## Exercício 6

A ACME é a universidade privada brasileira em modernização incremental do sistema acadêmico, cujo núcleo transacional em COBOL sobre o monitor CICS segue em operação durante toda a transição, com uma camada web em JSF e EJB e integrações com o ERP financeiro e o ambiente virtual de aprendizagem resolvidas por arquivo, em lote noturno.

Considerando o estilo arquitetural que você escolheu no exercício do [bloco 4 da Aula 1](../modulo-1-fundamentos/bloco-4-estilos-arquiteturais.md), levante duas plataformas candidatas capazes de concretizar esse estilo, considerando que o núcleo COBOL sobre CICS permanece em operação durante a transição.

1. Nomeie as duas plataformas candidatas.
2. Compare as duas por pelo menos três critérios, entre os apresentados no Conceito.
3. Escolha uma das duas e justifique a escolha considerando a restrição de convivência com o legado.

## Fontes

Glossário do curso, entrada [plataforma arquitetural](../referencia/glossario.md#plataforma-arquitetural). Ford e Richards (2020), listado na [bibliografia](../referencia/bibliografia.md), referência já usada na comparação de estilos por atributo de qualidade e igualmente pertinente à comparação de plataformas, porque a aderência ao estilo e o custo de operação, apresentados no Conceito, são também atributos de qualidade em jogo na escolha. Dossiê da instituição fictícia [ACME](../caso-acme/index.md) e [arquitetura de linha de base](../caso-acme/linha-de-base.md).
