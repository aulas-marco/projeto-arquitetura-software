# Registro de decisão arquitetural

Este bloco conclui a cadeia de decisão da aula e responde como registrar a decisão construída nos blocos 1 a 3 de forma compreensível, rastreável e revisável por quem não participou dela.

## Antes de começar

- [ADR](../referencia/glossario.md#adr)
- [Racional arquitetural](../referencia/glossario.md#racional-arquitetural)
- [Princípio de design](../referencia/glossario.md#principio-de-design)

## Conceito

A distinção entre decisão de arquitetura de solução e decisão de arquitetura de software já foi estabelecida no [bloco 1 da Aula 1](../modulo-1-fundamentos/bloco-1-arquitetura-de-solucoes-e-de-software.md#o-que-e-arquitetura-de-solucao). Este bloco parte dessa distinção para tratar de como registrar uma decisão de forma rastreável.

Decisões arquiteturais são aquelas que afetam a estrutura, as características não funcionais, as dependências, as interfaces ou as técnicas de construção do sistema. A definição é operacional, ela permite separar o que merece registro do que não merece sem recorrer a julgamento de importância. Escolher a fronteira entre dois módulos é decisão arquitetural, porque altera a estrutura e as interfaces, enquanto a escolha do formatador de código do projeto fica fora do registro por não afetar nenhum desses cinco aspectos.

O registro de decisão ocupa um lugar preciso na cadeia desta aula. Os princípios do [bloco 1](bloco-1-principios-de-design.md) e os cenários da Aula 2 fornecem as forças que diferenciam as alternativas, a comparação de estilos do [bloco 2](bloco-2-estilos-arquiteturais.md) fornece as alternativas e a escolha, e o mapa de padrões do [bloco 3](bloco-3-padroes-arquiteturais-e-de-design.md) fornece as consequências e os custos aceitos. O ADR registra uma decisão com o seu racional, e o desenho lógico e o plano de implementação continuam sendo artefatos próprios, aos quais o registro remete sem reproduzi-los.

### O racional do arquiteto

Um dos maiores riscos no processo decisório arquitetural é a influência de preferências individuais ou vieses inconscientes, que levam à adoção de tecnologias inadequadas ou mais complexas do que o necessário. A escolha de uma tecnologia precisa ser guiada pelo que melhor atende ao contexto específico do sistema, com suas restrições de desempenho, escalabilidade, segurança e custo operacional. Quando a decisão é tomada com base em familiaridade com uma linguagem ou em entusiasmo por tecnologia emergente, a arquitetura corre o risco de se desconectar das demandas reais de negócio e de operação, o que compromete a sustentabilidade do sistema e gera custo oculto de longo prazo em manutenção e em adesão da equipe.

O **racional arquitetural** é a base intelectual que justifica as decisões de desenho em um sistema, conectando cada escolha às metas estratégicas, aos requisitos técnicos e às restrições de negócio. Ele exige que o arquiteto documente não apenas a escolha feita, mas também o raciocínio por trás dela, incluindo as alternativas consideradas, os critérios de seleção e os impactos esperados. O racional funciona também como controle contra viés, porque obriga a fundamentar a escolha na necessidade do problema e na limitação do ambiente, e a preferência de quem decide deixa de ser justificativa aceitável.

O efeito não é apenas individual. Envolver o time na elaboração do racional favorece um ambiente colaborativo e reduz a possibilidade de decisão unilateral, e o registro resultante fortalece a confiança da equipe e das partes interessadas no processo, estabelecendo base para a evolução do sistema no longo prazo. Um racional escrito sem a participação do time registra a decisão, mas deixa de produzir o acordo que sustenta a sua aplicação pelas equipes.

### Abordagem leve para registro de decisões

Em projetos ágeis, decisões emergem de forma iterativa, a partir de novos aprendizados ou de mudança de escopo. Abordagens tradicionais como o *Rational Unified Process*, descrito por Kruchten (2004), e o método *Views and Beyond*, de Clements et al. (2010), enfatizam documentação detalhada e extensa. O registro leve adota um caminho incremental e modular, com registros pequenos e acessíveis, escritos em Markdown dentro do próprio repositório do código, que a equipe consegue atualizar à medida que as decisões são tomadas, porque um volume único de documentação tende a ficar desatualizado rapidamente.

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

A categoria de consequência neutra é a que separa um registro honesto de uma justificativa, e vale conferir se ela foi preenchida. Nem todo efeito de uma decisão é ganho ou perda, alguns apenas deslocam trabalho de um lugar para outro, e nomeá-los evita que apareçam depois como surpresa.

O **MADR**, sigla de *Markdown Architectural Decision Records*, é uma especificação aberta mantida em [adr.github.io/madr](https://adr.github.io/madr/), na versão 4.0.0 de 17/09/2024. O título é o cabeçalho de primeiro nível do arquivo, e o bloco de metadados no topo traz cinco campos opcionais, `status`, `date`, `decision-makers`, `consulted` e `informed`, que nomeiam quem decidiu, quem foi consultado e quem foi informado. O corpo tem as seções Context and Problem Statement, Decision Drivers, Considered Options, Decision Outcome, Consequences, Confirmation, Pros and Cons of the Options e More Information, das quais apenas contexto e problema, opções consideradas e resultado da decisão são obrigatórias. A diferença prática está em Considered Options e Pros and Cons of the Options, que forçam o autor a nomear cada opção avaliada e a listar prós e contras de cada uma antes de justificar a escolhida.

O [template de ADR](https://marco-mendes.github.io/arquitetura-software/referencia/template-adr/) do material base do professor organiza a mesma informação em dez campos e é o formato que esta disciplina usa. Ele parte do formato de Nygard, onde Estado corresponde ao Status, e acrescenta cinco campos próprios, Data, Forças, Alternativas, Evidências e Revisão.

| Campo | O que registrar | Critério de qualidade | Erro frequente |
| --- | --- | --- | --- |
| Título | A sigla ADR, o número do registro e a decisão em uma frase | A decisão é identificável pelo título sem abrir o arquivo | Título que nomeia o problema e omite a escolha feita |
| Estado | Proposta, aceita, substituída ou rejeitada | O estado reflete a situação atual e só muda por novo registro ou por revisão declarada | Registro aceito que nunca foi implantado permanece como aceito |
| Data | No formato ano, mês e dia | A data é a da decisão | Data de criação do arquivo registrada como data da decisão |
| Contexto | A situação, os envolvidos, as restrições e o problema que exige decisão, delimitando o que fica dentro e fora do registro | Um leitor sem histórico no projeto entende por que a decisão precisou ser tomada naquele momento | Contexto redigido como argumento a favor da alternativa escolhida |
| Forças | Atributos de qualidade, necessidades funcionais, restrições técnicas e condições organizacionais que diferenciam as alternativas, em cenários mensuráveis quando possível | Cada força diferencia ao menos duas alternativas e remete a um princípio, cenário ou restrição | Força genérica que todas as alternativas atendem igualmente |
| Alternativas | Para cada alternativa viável, como funciona, quais forças atende, quais riscos introduz e quais suposições precisam ser confirmadas, incluindo a opção de manter a situação atual quando ela for legítima | Todas as alternativas são comparadas pelas mesmas forças | Alternativa listada apenas pelo nome |
| Decisão | A alternativa escolhida, com a justificativa conectada às forças, sem recorrer a familiaridade ou popularidade | A justificativa cita as forças listadas e o peso dado a cada uma | Justificativa apoiada em preferência da equipe ou em tendência de mercado |
| Consequências | Efeitos positivos, negativos e neutros, mais trabalho adicional, dependências, riscos aceitos e condições que podem exigir revisão | Há ao menos uma consequência de cada tipo, com o custo aceito declarado | Lista apenas de consequências positivas |
| Evidências | Testes, medições, experimentos, contratos, diagramas ou sinais operacionais que sustentam a decisão, e onde cada evidência pode ser reproduzida | Outra pessoa consegue reproduzir cada evidência a partir do local indicado | Evidência citada sem local, sem data ou sem método |
| Revisão | O evento ou a data que motivará nova avaliação, e o vínculo com o ADR que vier a substituir este | O gatilho é observável e tem valor ou prazo definido | Gatilho do tipo "revisar no futuro", que não obriga ninguém |

Entre os campos que o formato de Nygard não tem, Evidências e Revisão são os que mais alteram a qualidade do registro, porque o primeiro torna a justificativa verificável por outra pessoa e o segundo atribui à decisão uma condição objetiva de reavaliação, com valor ou prazo definidos.

### Um exemplo completo

O registro abaixo aplica o template de dez campos a uma decisão de infraestrutura. Ele aparece como o arquivo Markdown ficaria no repositório, que é a forma real do artefato.

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

Quatro práticas sustentam o uso de ADR ao longo do projeto. A integração ao repositório facilita o acesso e mantém o registro alinhado com o código que ele descreve, e o formato leve, em Markdown, reduz o esforço de atualização. A revisão contínua, em ciclo regular, preserva a relevância e a precisão de cada registro, e o registro das alternativas analisadas e rejeitadas permite que quem chega depois entenda a decisão sem repetir a análise.

Um ADR aceito não é editado para acomodar uma decisão nova. Quando o contexto muda, um registro novo é criado com a decisão atualizada, o registro anterior passa ao estado substituída com o vínculo para o novo, e o histórico das decisões permanece legível na ordem em que foram tomadas. A figura abaixo mostra esse ciclo de estados e a anatomia do registro nos dez campos do template.

<figure markdown="span">
![Diagrama do ciclo de vida e da anatomia de um ADR. À esquerda, os estados proposta, aceita, substituída e rejeitada, com setas de proposta para aceita, de proposta para rejeitada e de aceita para substituída, esta última com o vínculo para o registro que substitui o anterior. À direita, o arquivo do ADR com os dez campos agrupados em quatro partes, identificação com título, estado e data, contexto com contexto e forças, escolha com alternativas e decisão, e controle com consequências, evidências e revisão.](../assets/images/modulo-3-ciclo-de-vida-adr.svg){ .module-diagram }
</figure>

*Figura 1 — Estados de um ADR ao longo do tempo e agrupamento dos dez campos do template, em material do curso elaborado com base em Nygard (2011) e em Mendes (2026a).*

## Uso pelo arquiteto

O arquiteto escreve o ADR no momento da decisão, porque é nesse momento que as alternativas descartadas e o raciocínio que as eliminou ainda estão claros. Quem entra no projeto mais tarde não tem acesso a essa conversa, só ao registro, e um texto escrito de forma retrospectiva tende a simplificar o raciocínio original e a esconder justamente a alternativa que valeria reconsiderar se o contexto mudar.

Quando falta dado para preencher um campo, o caminho é registrar o ADR com estado proposta e listar ao final os campos que ficaram incompletos. Um registro incompleto que declara as próprias lacunas continua utilizável, enquanto um registro preenchido com dado inventado leva as decisões seguintes a partir de premissas que ninguém verificou.

## Exercício 12

Este exercício é realizado fora do horário de aula, como atividade de aplicação do conceito apresentado neste bloco ao caso da instituição fictícia ACME.

A ACME é a universidade privada brasileira em modernização incremental do sistema acadêmico, usada como caso desta disciplina. Os três exercícios anteriores desta aula produziram as entradas do registro, os princípios priorizados e o esboço lógico do [exercício 9](bloco-1-principios-de-design.md#exercicio-9), a comparação de três estilos com o estilo recomendado do [exercício 10](bloco-2-estilos-arquiteturais.md#exercicio-10) e o mapa de problema, padrão e consequência do [exercício 11](bloco-3-padroes-arquiteturais-e-de-design.md#exercicio-11). Escreva o ADR que registra o estilo escolhido e os padrões que materializam a estratégia de modernização, no template de dez campos apresentado no Conceito acima.

1. título, estado e data
2. contexto, descrevendo de forma neutra os dois cenários que motivaram a análise e delimitando o que fica fora do registro
3. forças, derivadas dos princípios priorizados no exercício 9 e dos cenários, com medida sempre que o caso fornecer
4. alternativas, com os dois estilos comparados e descartados no exercício 10, cada um avaliado pelas mesmas forças do item anterior
5. decisão, com o estilo escolhido e os padrões do exercício 11, conectando a justificativa às forças listadas
6. consequências, com ao menos uma positiva, uma negativa e uma neutra, incluindo o custo aceito de cada padrão
7. evidências, indicando onde cada uma poderia ser reproduzida
8. revisão, com um gatilho observável

As quatro frases abaixo servem de modelo para os campos que costumam sair fracos.

- Alternativa descartada, o estilo X atenderia a força Y, mas traria o risco Z, e foi descartado porque a evidência disponível é W, ou porque ela não existe.
- Consequência favorável, o efeito X, observável em Y.
- Consequência desfavorável, aceitamos o custo X enquanto a condição Y permanecer verdadeira.
- Gatilho de revisão, se a medida X ultrapassar o valor Y na janela Z, este registro é reaberto.

Uma alternativa listada só pelo nome não foi comparada, e um gatilho do tipo "revisar no futuro" não define quando a revisão ocorre. Se faltar dado para algum campo, registre o estado como proposta e liste os campos incompletos ao final.

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Nygard, M. (2011, 15 de novembro). *Documenting architecture decisions*. Cognitect Blog. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions (formato de cinco partes)
- MADR. (2024). *Markdown Architectural Decision Records* (Versão 4.0.0). https://adr.github.io/madr/ (campos do formato MADR)
- Mendes, M. (2026a). *Arquitetura de software* [Material de curso]. https://marco-mendes.github.io/arquitetura-software/ ([template de ADR](https://marco-mendes.github.io/arquitetura-software/referencia/template-adr/) de dez campos e o [estudo de caso do módulo 1](https://marco-mendes.github.io/arquitetura-software/modulo-1-visao-geral/estudo-de-caso/#exercicio-4-consequencias-e-adr-001))
- Mendes, M. (2026b). *Guias de projeto de arquitetura de software* [Material de curso, versão arquivada]. https://github.com/aulas-marco/projeto-arquitetura-software/tree/30f15cd (guia 2.1, fonte do racional do arquiteto, da abordagem leve, do exemplo do Kubernetes e das práticas recomendadas)
- Henderson, J. P. (n.d.). *Architecture decision record (ADR)* [Repositório de modelos e exemplos]. https://github.com/joelparkerhenderson/architecture-decision-record (coleção de exemplos e modelos)
- Kruchten, P. (2004). *The rational unified process: An introduction* (3rd ed.). Addison-Wesley. (contraponto de documentação extensa)
- Clements, P., Bachmann, F., Bass, L., Garlan, D., Ivers, J., Little, R., Merson, P., Nord, R., & Stafford, J. (2010). *Documenting software architectures: Views and beyond* (2nd ed.). Addison-Wesley. (contraponto de documentação extensa)

**Material do curso.** O bloco usa as entradas [ADR](../referencia/glossario.md#adr) e [racional arquitetural](../referencia/glossario.md#racional-arquitetural) do glossário, os produtos dos exercícios 9 a 11 desta aula e o dossiê da instituição fictícia [ACME](../caso-acme/index.md).
