# Registro de decisão arquitetural

Este bloco abre a aula respondendo a uma pergunta prática, como registrar uma decisão arquitetural já tomada de forma que ela sobreviva à saída de quem a tomou.

## Antes de começar

- [ADR](../referencia/glossario.md#adr)
- [Racional arquitetural](../referencia/glossario.md#racional-arquitetural)

## Conceito

A distinção entre decisão arquitetural e decisão de implementação já foi estabelecida na seção Conceito do [bloco 1 da Aula 1](../modulo-1-fundamentos/bloco-1-arquitetura-e-papel-do-arquiteto.md#conceito). Este bloco parte dessa distinção para tratar de como registrar a primeira de forma rastreável.

Decisões arquiteturais são aquelas que afetam a estrutura, as características não funcionais, as dependências, as interfaces ou as técnicas de construção do sistema. A definição é operacional, ela permite separar o que merece registro do que não merece sem recorrer a julgamento de importância. Escolher a fronteira entre dois módulos é decisão arquitetural. Escolher o formatador de código do projeto não é.

### O racional do arquiteto

Um dos maiores riscos no processo decisório arquitetural é a influência de preferências individuais ou vieses inconscientes, que levam à adoção de tecnologias inadequadas ou mais complexas do que o necessário. A escolha de uma tecnologia precisa ser guiada pelo que melhor atende ao contexto específico do sistema, com suas restrições de desempenho, escalabilidade, segurança e custo operacional. Quando a decisão é tomada com base em familiaridade com uma linguagem ou em entusiasmo por tecnologia emergente, a arquitetura corre o risco de se desconectar das demandas reais de negócio e de operação, o que compromete a sustentabilidade do sistema e gera custo oculto de longo prazo em manutenção e em adesão da equipe.

O **racional arquitetural** é a base intelectual que justifica as decisões de desenho em um sistema, conectando cada escolha às metas estratégicas, aos requisitos técnicos e às restrições de negócio. Ele exige que o arquiteto documente não apenas a escolha feita, mas também o raciocínio por trás dela, incluindo as alternativas consideradas, os critérios de seleção e os impactos esperados. Mais do que artefato técnico, o racional funciona como ferramenta contra viés, porque obriga a fundamentar a escolha na necessidade do problema e na limitação do ambiente, não na preferência de quem decide.

### Abordagem leve para registro de decisões

Em projetos ágeis, decisões emergem de forma iterativa, a partir de novos aprendizados ou de mudança de escopo. Abordagens tradicionais como o *Rational Unified Process*, descrito por Kruchten (2004), e o método *Views and Beyond*, de Clements et al. (2010), enfatizam documentação detalhada e extensa. O registro leve adota o caminho oposto, incremental e modular. Em vez de um volume monolítico que se torna obsoleto rapidamente, o foco está em registros pequenos e acessíveis, que a equipe consegue atualizar, escritos em Markdown dentro do próprio repositório do código.

Duas regras sustentam essa abordagem. A primeira é manter o documento dentro do próprio repositório, em formato leve. A segunda é mantê-lo curto o bastante para que o time de desenvolvimento consiga mantê-lo. Nem todas as decisões serão tomadas de uma vez, nem todas no início do projeto, e documentos pequenos e modulares têm ao menos a chance de serem atualizados.

Manter o registro próximo do código, e não em ferramenta externa ou documento estático, permite que ele funcione como **artefato vivo** da arquitetura. Isso reduz a barreira para atualizá-lo, evita divergência entre o código implementado e a decisão documentada, e registra também as alternativas descartadas e os motivos da rejeição, o que impede que erros passados sejam repetidos.

### Três formatos, do mais enxuto ao mais completo

Um registro de decisão arquitetural, ou **ADR**, é um arquivo de texto curto. A prática tem um formato de origem, um formato de especificação aberta e o formato adotado por esta disciplina, e os três diferem em quanto exigem do autor.

Michael Nygard propôs o formato original em Nygard (2011), com cinco partes fixas.

| Parte | Conteúdo |
| --- | --- |
| Título | Frase curta e clara, como "Adoção do .NET Core 9" |
| Contexto | Descrição neutra das forças em jogo, sejam requisitos técnicos, sociais, políticos ou organizacionais |
| Decisão | Explicação objetiva da escolha, em linguagem ativa, do tipo "nós decidimos adotar" |
| Status | Estágio da decisão, proposta, aceita ou substituída |
| Consequências | Resultados esperados, incluindo pontos positivos, negativos e neutros |

A categoria de consequência neutra costuma ser a mais esquecida e é a que separa um registro honesto de uma justificativa. Nem todo efeito de uma decisão é ganho ou perda, alguns apenas deslocam trabalho de um lugar para outro, e nomeá-los evita que apareçam depois como surpresa.

O **MADR**, sigla de *Markdown Architectural Decision Records*, é uma especificação aberta mantida em [adr.github.io/madr](https://adr.github.io/madr/), na versão 4.0.0 de 17/09/2024. O cabeçalho traz `title`, além dos campos opcionais `status`, `date`, `decision-makers`, `consulted` e `informed`, que nomeiam quem decidiu, quem foi consultado e quem foi informado. O corpo tem as seções Context and Problem Statement, Decision Drivers, Considered Options, Decision Outcome, Consequences, Confirmation, Pros and Cons of the Options e More Information, das quais apenas contexto e problema, opções consideradas e resultado da decisão são obrigatórias. A diferença prática está em Considered Options e Pros and Cons of the Options, que forçam o autor a nomear cada opção avaliada e a listar prós e contras de cada uma antes de justificar a escolhida.

O [template de ADR](https://marco-mendes.github.io/arquitetura-software/referencia/template-adr/) do material base do professor organiza a mesma informação em nove campos e é o formato que esta disciplina usa. Ele parte do formato de Nygard e acrescenta quatro seções próprias, Forças, Alternativas, Evidências e Revisão.

| Campo | O que registrar |
| --- | --- |
| Título | A sigla ADR, o número do registro e a decisão em uma frase |
| Estado | Proposta, aceita, substituída ou rejeitada |
| Data | No formato ano, mês e dia |
| Contexto | A situação, os envolvidos, as restrições e o problema que exige decisão, delimitando o que fica dentro e fora do registro |
| Forças | Atributos de qualidade, necessidades funcionais, restrições técnicas e condições organizacionais que diferenciam as alternativas, em cenários mensuráveis quando possível |
| Alternativas | Para cada alternativa viável, como funciona, quais forças atende, quais riscos introduz e quais suposições precisam ser confirmadas, incluindo a opção de manter a situação atual quando ela for legítima |
| Decisão | A alternativa escolhida, com a justificativa conectada às forças, sem recorrer a familiaridade ou popularidade |
| Consequências | Efeitos positivos, negativos e neutros, mais trabalho adicional, dependências, riscos aceitos e condições que podem exigir revisão |
| Evidências | Testes, medições, experimentos, contratos, diagramas ou sinais operacionais que sustentam a decisão, e onde cada evidência pode ser reproduzida |
| Revisão | O evento ou a data que motivará nova avaliação, e o vínculo com o ADR que vier a substituir este |

Os dois campos que o formato de Nygard não tem e que mais mudam a qualidade do registro são Evidências e Revisão. Evidências transforma a justificativa em algo verificável por outra pessoa. Revisão transforma a decisão em hipótese com prazo, em vez de verdade permanente.

### Um exemplo completo

O registro abaixo aplica o template de nove campos a uma decisão de infraestrutura. Ele aparece como o arquivo Markdown ficaria no repositório, que é a forma real do artefato.

```markdown
# ADR 5, adoção do Kubernetes para gerenciamento de infraestrutura e aplicações

Estado: aceita
Data: 2024-12-01

## Contexto

A empresa enfrenta indisponibilidade recorrente em aplicações críticas. As
aplicações monolíticas hospedadas em máquinas virtuais estão sujeitas a ponto
único de falha, o escalonamento de recursos é manual e responde em minutos ou
horas, insuficiente para o pico de tráfego, a implantação e a recuperação
dependem de scripts manuais desatualizados, as atualizações parciais causam
indisponibilidade temporária por ausência de estratégia de atualização
progressiva, e o monitoramento é inconsistente entre aplicações e
infraestrutura. Fica fora deste registro a escolha do provedor de nuvem.

## Forças

- Alta disponibilidade e resiliência, sem ponto único de falha
- Automação de provisionamento, de escalonamento e de gestão de carga
- Observabilidade com métricas unificadas entre infraestrutura e aplicações
- Portabilidade entre provedores, para evitar dependência de um só fornecedor

## Alternativas

- Docker Swarm. Simples e rápido de começar, atende parcialmente a automação,
  mas é limitado em alta disponibilidade, em escalabilidade e em suporte da
  comunidade.
- Serviços gerenciados específicos de nuvem. Atendem bem disponibilidade e
  automação, porém prendem parcialmente a operação a um único provedor, o que
  contraria a força de portabilidade.
- Servidor dedicado com Rancher. Integra bem e preserva portabilidade, mas tem
  custo e complexidade de gerenciamento elevados frente ao Kubernetes puro.
- Manter a situação atual. Não é alternativa legítima aqui, porque nenhuma das
  quatro forças é atendida hoje.

## Decisão

Nós decidimos adotar o Kubernetes como solução principal de gerenciamento de
infraestrutura e aplicações. Ele atende alta disponibilidade por replicação de
pods, agrupamento de nós e verificação de saúde, atende automação por
orquestração nativa de implantação, escalonamento e recuperação, atende
observabilidade por integração com as ferramentas de métricas já usadas, e
atende portabilidade por abstrair o provedor, permitindo execução em nuvem
pública ou em infraestrutura local.

## Consequências

Positivas. Redução do tempo de indisponibilidade com recuperação automática,
resposta mais rápida à variação de tráfego e melhor capacidade de identificar
problemas em produção.

Negativas. Curva de aprendizado que exige capacitação da equipe, custo inicial
de treinamento e de ferramental associado, e complexidade operacional de manter
esteiras de integração e implantação alinhadas ao Kubernetes.

Neutra. A migração de aplicações legadas varia entre fácil, quando a aplicação
já está em contêiner, e complexa, quando é monolítica.

## Evidências

- Prova de conceito em agrupamento de teste local, com o roteiro de execução
  versionado no repositório de infraestrutura
- Medição de tempo de recuperação antes e depois, reproduzível pelo mesmo
  roteiro

## Revisão

Este registro é reaberto se o custo mensal de operação do agrupamento
ultrapassar o orçamento aprovado por dois ciclos seguidos, ou se a equipe
capacitada cair abaixo de duas pessoas.
```

### Práticas recomendadas

Quatro práticas sustentam o uso de ADR ao longo do projeto. A integração ao repositório facilita o acesso e garante alinhamento com o código. O formato leve, em Markdown, reduz a barreira e incentiva a atualização. A revisão contínua, em ciclo regular, preserva relevância e precisão. O registro de alternativas analisadas e rejeitadas enriquece o entendimento da decisão para quem chega depois.

## Uso pelo arquiteto

O arquiteto escreve o ADR no momento da decisão, não depois, porque é nesse momento que as alternativas descartadas e o raciocínio que as eliminou ainda estão claros. Quem entra no projeto mais tarde não tem acesso a essa conversa, só ao registro, e um texto escrito de forma retrospectiva tende a simplificar o raciocínio original e a esconder justamente a alternativa que valeria reconsiderar se o contexto mudar.

Quando falta dado para preencher um campo, o caminho é registrar o ADR com estado proposta e listar ao final os campos que ficaram incompletos. Um registro incompleto e honesto continua utilizável. Um registro completo por invenção contamina todas as decisões que vierem depois dele.

## Exercício 5

A ACME é a universidade privada brasileira em modernização incremental do sistema acadêmico, usada como caso desta disciplina. No exercício do [bloco 4 da Aula 1](../modulo-1-fundamentos/bloco-4-estilos-arquiteturais.md), você comparou três estilos arquiteturais contra os dois cenários da ACME e defendeu um deles. Escreva o ADR que registra essa decisão, no template de nove campos apresentado no Conceito acima.

1. título, estado e data
2. contexto, descrevendo de forma neutra os dois cenários que motivaram a análise e delimitando o que fica fora do registro
3. forças, ligando cada uma a um atributo de qualidade dos cenários, com medida sempre que o caso fornecer
4. alternativas, com pelo menos dois estilos além do escolhido, cada um com a força que atenderia e o risco que traria
5. decisão, conectando a justificativa às forças que você listou
6. consequências, com ao menos uma positiva, uma negativa e uma neutra
7. evidências, indicando onde cada uma poderia ser reproduzida
8. revisão, com um gatilho observável

As quatro frases abaixo servem de modelo para os campos que costumam sair fracos.

- Alternativa descartada, o estilo X atenderia a força Y, mas traria o risco Z, e foi descartado porque a evidência disponível é W, ou porque ela não existe.
- Consequência favorável, o efeito X, observável em Y.
- Consequência desfavorável, aceitamos o custo X enquanto a condição Y permanecer verdadeira.
- Gatilho de revisão, se a medida X ultrapassar o valor Y na janela Z, este registro é reaberto.

Alternativa listada só pelo nome não foi comparada, e um gatilho do tipo "revisar no futuro" não obriga ninguém a nada. Se faltar dado para algum campo, registre o estado como proposta e liste os campos incompletos ao final.

## Fontes

Glossário do curso, entradas [ADR](../referencia/glossario.md#adr) e [racional arquitetural](../referencia/glossario.md#racional-arquitetural).

Material base do professor, guia [Registro de Decisões Arquiteturais (ADR)](https://github.com/aulas-marco/projeto-arquitetura-software/blob/main/2.1%20ADR.md), de onde vêm o racional do arquiteto, a abordagem leve, o exemplo do Kubernetes e as práticas recomendadas. [Template de ADR](https://marco-mendes.github.io/arquitetura-software/referencia/template-adr/) do site base do professor, fonte dos nove campos e do texto de orientação de cada um. Estudo de caso do [Módulo 1 do site base](https://marco-mendes.github.io/arquitetura-software/modulo-1-visao-geral/estudo-de-caso/#exercicio-4-consequencias-e-adr-001), fonte das quatro frases-modelo e da regra de registrar como proposta quando faltar dado.

Nygard (2011), fonte do formato de cinco partes. Especificação [MADR 4.0.0](https://adr.github.io/madr/), fonte dos campos do formato citados no Conceito. Coleção de exemplos e modelos de ADR mantida por [Henderson (n.d.)](https://github.com/joelparkerhenderson/architecture-decision-record). Kruchten (2004) e Clements et al. (2010), citados na abordagem leve como contraponto de documentação extensa. As referências com autor e ano estão listadas na [bibliografia](../referencia/bibliografia.md).
