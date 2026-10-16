# Apresentação do caderno arquitetural

No fim do primeiro ciclo, a Reitoria, a Diretoria de TI e a fábrica de software da ACME recebem o mesmo documento, o caderno arquitetural, e cada uma o abre para resolver uma dúvida diferente. A Reitoria quer saber se pode apoiar o projeto depois de poucos minutos de leitura, a Diretoria de TI quer saber por que cada decisão foi tomada, e a fábrica quer saber o que o desenho exige dela e até quando. Neste bloco, o professor percorre o caderno completo da ACME, seção por seção, e o aluno compara cada seção com a que escreveu nos exercícios 1 a 23. O bloco ensina o que cada leitor procura em cada seção, como os catorze artefatos do ciclo se encadeiam, como um único requisito atravessa o caderno inteiro e qual regra de rastreabilidade mantém o caderno confiável, e o exercício 24 pede a conferência final com as versões finais do resumo e das pendências.

## Antes de começar

- [Caderno arquitetural](../referencia/glossario.md#caderno-arquitetural)
- [Artefato de arquitetura](../referencia/glossario.md#artefato-de-arquitetura)
- [Restrição](../referencia/glossario.md#restricao)
- [ADR](../referencia/glossario.md#adr)

## Conceito

### Um caderno, três leitores

Quando o caderno chega às mãos de quem decide, nenhum dos três leitores o lê do começo ao fim. A Reitoria abre a primeira página e decide se continua. A Diretoria de TI, que pediu que o portal sustente 5.800 sessões simultâneas na abertura da matrícula, procura a decisão que atende a esse pedido e a medida que mostrará se ele foi cumprido. A fábrica de software, que mantém o núcleo COBOL, procura o que lhe cabe construir e a data em que o contrato de sustentação termina. Como cada leitor busca uma resposta diferente, o caderno se organiza por pergunta, e cada uma das onze seções responde a uma delas, como mostra a tabela.

| Seção do caderno | Pergunta que responde | Quem procura a resposta |
| --- | --- | --- |
| 0. A solução em uma página | Se alguém lesse só esta página, entenderia o projeto? | A Reitoria, que decide se apoia o projeto |
| 1. Contexto | Que organização é esta, que problema ela quer resolver e o que já está decidido antes do desenho? | Qualquer leitor novo no projeto, e a Reitoria, dona de restrições como o orçamento de R$ 6,2 milhões |
| 2. Partes interessadas | Quem precisa participar das decisões e onde os interesses entram em conflito? | O patrocinador, que precisa saber quem consultar |
| 3. Requisitos | O que a solução precisa entregar e como saberemos que entregou? | A Diretoria de TI, dona do pedido de 5.800 sessões simultâneas |
| 4. Linha de base e lacunas | Onde o sistema atual é frágil e o que é preciso mudar? | A Diretoria de TI e a fábrica, que conhecem o núcleo |
| 5. Contexto do sistema | O que está dentro da solução, o que está fora e com quem ela se relaciona? | A Coordenação de Educação a Distância, que depende do envio da nota ao ambiente virtual |
| 6. Princípios | Que regras o desenho precisa respeitar para que uma proposta possa ser recusada por quebrá-las? | As equipes que constroem a solução |
| 7. Decisões | O que foi decidido, que requisito cada decisão atende e que consequências ela traz? | A Diretoria de TI, que responde pelas decisões |
| 8. Tecnologia e plataforma | Que produtos e que plataforma atendem às decisões e que riscos de segurança precisam de resposta? | A fábrica, a equipe Java e o Comitê de Segurança da Informação |
| 9. Roteiro e governança | Em que ordem as lacunas serão fechadas e como evitar que a obra se afaste do desenho? | A Reitoria, que financia o primeiro ciclo, e a Diretoria de TI, que acompanha a execução |
| 10. O que ainda falta decidir | O que ainda impede o projeto de seguir e quem resolve? | Cada responsável nomeado, que descobre ali o que lhe cabe e até quando |

Quem tem poucos minutos lê as seções 0 e 10, porque a primeira diz o que o projeto decidiu e a última diz o que ainda não decidiu. Quem precisa defender uma decisão sai da seção 7 e chega ao requisito na seção 3. A ordem das seções acompanha a ordem em que o desenho foi construído, e por isso o aluno reconhece em cada uma o exercício que a produziu: a seção 1 veio da Aula 1, as seções 2 e 3 da Aula 2, a seção 6 da Aula 3, as seções 5 e 7 das Aulas 3 e 4, a seção 8 da Aula 5 e a seção 9 desta Aula 6. A seção 4 nasceu na Aula 2 e recebeu as lacunas no [bloco 1](bloco-1-governanca-da-mudanca.md) desta aula.

### Os catorze artefatos do ciclo

Ao longo das seis aulas, a ACME produziu catorze artefatos, que são os documentos, as tabelas e os diagramas entregues pelos exercícios, e cada um só pôde ser feito porque recebeu pronto o que o anterior produziu. O mapa de partes interessadas, por exemplo, só ficou completo depois das entradas do processo, porque cada direcionador de mudança e cada restrição tem um dono na organização. A tabela lista, para cada artefato, o que ele precisa receber pronto e a seção do caderno em que aparece.

| Nº | Artefato | O que recebe pronto | Seção do caderno |
| --- | --- | --- | --- |
| 1 | Entradas do processo: direcionadores, restrições e linha de base | O problema reformulado | 1 e 4 |
| 2 | Mapa de partes interessadas | As entradas | 2 |
| 3 | Catálogo de requisitos com cenários de qualidade | O mapa de partes interessadas | 3 |
| 4 | Relatório de lacunas | A linha de base e o catálogo de requisitos | 4 |
| 5 | Desenho lógico, com blocos de construção e interfaces | O catálogo e o relatório, porque cada bloco atende a um requisito ou fecha uma lacuna | 6 e 7 |
| 6 | ADRs de estilo e de padrões | Os cenários, que fornecem as forças, e o desenho lógico | 7 |
| 7 | Contratos de integração | As relações entre blocos que atravessam a fronteira de uma equipe ou de um sistema | 5 |
| 8 | Diagramas de contexto e de contêineres | A fronteira e os contêineres do desenho lógico | 5 e 7 |
| 9 | Modelo técnico de referência (TRM) | O desenho lógico e os contêineres | 8 |
| 10 | Matriz de seleção com ADR | O modelo técnico de referência | 8 |
| 11 | Zona de pouso | A seleção e os cenários de qualidade, que definem a topologia de disponibilidade | 8 |
| 12 | Uso verificado de IA | Os artefatos anteriores, porque o modelo no modo crítico precisa de requisito, restrição e decisão registrada para conferir uma proposta | 9 |
| 13 | Roteiro em ondas | A arquitetura alvo, o relatório de lacunas e a definição tecnológica | 9 |
| 14 | Modelo de governança | Todas as decisões registradas | 9 |

Os artefatos 1 a 4 vieram das Aulas 1 e 2, os artefatos 5 a 8 das Aulas 3 e 4, os artefatos 9 a 11 da Aula 5 e os artefatos 12 a 14 desta Aula 6. A dependência entre eles tem uma consequência prática: quando o roteiro mostra que uma onda não cabe no prazo, a alteração volta ao patrocinador e às partes interessadas do mapa que abriu o processo, o que fecha o ciclo no artefato 2.

### O fio de um requisito pelo caderno inteiro

Para mostrar o encadeamento, o professor acompanha na aula um único pedido da ACME, da primeira seção à última. Na abertura da matrícula, o Portal do Aluno chega a 5.800 sessões simultâneas, com 6,3% de erro, e a Diretoria de TI pediu que o portal sustente esse pico e confirme 95% das matrículas em até 4 segundos. O pedido tem o código R6 no dossiê, que é a descrição do caso ACME usada pelo curso, e nasceu de uma queixa vaga da representação discente, a de que o tempo de resposta precisava ser bom, registrada no dossiê como requisito R3. A tabela mostra o que acontece com o R6 em cada artefato.

| Etapa | O que acontece com o pedido | Seção do caderno |
| --- | --- | --- |
| Requisito | A Diretoria de TI declara o pedido, e a queixa registrada como R3 é reescrita com a carga de 5.800 sessões e a medida de 4 segundos | 3 |
| Cenário de qualidade | O pico de matrícula é descrito em seis partes, com taxa de erro abaixo de 1% verificada em teste de carga | 3 |
| Lacuna | A diferença entre o portal atual, que erra 6,3% no pico, e o que o desenho exige é registrada para fechar em onda | 4 |
| Decisão | O registro de decisão ADR 001 coloca uma fila entre o portal e o núcleo COBOL para absorver o pico sem alterar o núcleo | 7 |
| Contêiner | O serviço de matrícula e as relações 1, 3, 5 e 8 do diagrama de contêineres formam o caminho da confirmação | 7 |
| Tecnologia | A plataforma de microsserviços na variante Java, com barramento de eventos, concretiza a fila | 8 |
| Onda | O critério de conclusão da segunda onda exige a matrícula digital operando numa janela real, com o desempenho do R6 medido em produção | 9 |
| Controle | Uma função de aptidão, teste automático que avisa quando uma decisão deixa de ser cumprida, roda o teste de carga com 5.800 sessões antes de cada janela de matrícula, a função de aptidão FA2 do caderno | 9 |

A leitura em sentido inverso serve a quem propõe uma mudança. Se alguém sugerir ao conselho de revisão, apresentado no [bloco 1](bloco-1-governanca-da-mudanca.md), que a fila seja retirada para reduzir a latência, o arquiteto parte do teste de carga, passa pela decisão que o teste protege, pelo contêiner, pela lacuna e pelo cenário, e chega à Diretoria de TI, que declarou o pedido. Em cada parada ele encontra o que a proposta coloca em risco e quem precisa ser consultado antes da votação.

### A regra de rastreabilidade

O percurso do R6 só pode ser refeito porque cada ligação foi registrada. Rastreabilidade é a possibilidade de seguir, em qualquer direção, a ligação entre um requisito, a decisão que o atende, o ponto do desenho em que a decisão aparece e a pessoa responsável por ela. O caderno da ACME cumpre três regras, que a página de [convenções](../caderno/convencoes.md#como-uma-decisao-se-liga-ao-requisito) já apresentava desde a Aula 1.

1. Toda decisão cita o requisito ou a restrição que a motivou. Uma decisão sem origem fica sem justificativa, e ninguém consegue dizer depois se ela ainda faz sentido.
2. Todo requisito cita a decisão que o atende. Um requisito sem decisão é uma lacuna ainda não tratada, que precisa entrar na seção 4 e, depois, no roteiro.
3. Toda pendência tem responsável e prazo. Uma pendência sem responsável permanece parada, porque ninguém sabe a quem cobrar.

Na conferência final, o arquiteto monta uma tabela com uma linha por decisão, requisito ou pendência e a lê com uma pergunta para cada regra. Quando a resposta a uma pergunta é nenhuma, a linha tem uma inconsistência, e a correção segue o tipo dela: registrar a origem da decisão ou rever se ela deve existir, registrar a decisão que falta ou anotar a falta como lacuna, e nomear o responsável e o prazo da pendência. Uma restrição, como o contrato de sustentação do núcleo COBOL, vale como origem tanto quanto um requisito, porque também motiva decisões.

## Uso pelo arquiteto

O arquiteto da ACME usa o caderno completo no dia em que apresenta o projeto à Reitoria e à Diretoria de TI, e nesse dia as perguntas chegam de lados diferentes. A Reitoria pergunta se pode apoiar o projeto e lê a seção 0, enquanto a Diretoria de TI pergunta por que existe uma fila na frente do núcleo e segue da seção 7 até o requisito na seção 3. Como o caderno cumpre a regra de rastreabilidade, o arquiteto responde apontando a seção, sem reconstruir o raciocínio de memória, e leva a cada leitor apenas o trecho de que ele precisa. Sem a conferência final, a primeira pergunta que o caderno não souber responder, como a de quem decide o ensaio de carga com 5.800 sessões, expõe uma decisão sem dono diante de quem aprova o orçamento.

A conferência também orienta o trabalho depois da apresentação. A seção 10 diz à fábrica de software o que ainda depende dela, como gravar o registro do evento da nota na mesma transação que grava a nota, dentro do programa COBOL, e diz à Diretoria de TI o que ela precisa resolver antes de aceitar os registros de decisão. Se a seção estiver incompleta, cada responsável só descobre o que lhe cabe quando o prazo já passou.

## No caderno arquitetural

{{ficha:0:6}}

**Para que serve.** Quando a Reitoria abre o caderno, a primeira página decide se ela continua a leitura. O resumo da seção 0 reúne em seis parágrafos o problema, a pergunta, a decisão, o que mais pesa no desenho, as consequências e o estado do trabalho, e por isso é a única parte que todos os leitores percorrem. Esta é a sexta e última versão do resumo, e ela substitui a da Aula 5 porque o caderno agora tem roteiro em ondas, governança e uma conferência final de rastreabilidade.

**O que você faz neste exercício.** O enunciado traz uma tabela de rastreabilidade da ACME com oito linhas, e você aponta as inconsistências dela no item 1. No item 2, você escreve o resumo final em seis parágrafos curtos, apoiado no seu caderno completo. Cada parágrafo precisa se entender sozinho, de modo que um leitor que veja só esta página compreenda o projeto sem consultar as outras seções.

| Campo do caderno | Como preencher | Item |
| --- | --- | --- |
| O problema | Conte a situação da ACME e por que ela exige mudança, com os números do caso | 2 |
| A pergunta | Escreva a pergunta que o projeto responde | 2 |
| A decisão | Diga a decisão central do projeto e o estado dela, proposta ou aceita | 2 |
| O que mais pesa no desenho | Diga qual exigência mais pesa, escrevendo o conteúdo e a medida antes do código | 2 |
| Consequências | Diga o que a decisão custa à ACME, com ao menos uma consequência para a equipe | 2 |
| Como está o trabalho | Diga o que está decidido, o que está proposto e o que falta, incluindo o roteiro em ondas e a conferência final | 2 |

**O que você já tem.** As cinco versões anteriores do resumo, escritas nos exercícios 4, 8, 12, 16 e 20, e a seção 9 preenchida nos exercícios 21 a 23.

**Quando está pronto.** Os seis parágrafos existem, cada um se entende sem as outras seções, nenhum cita um código sem dizer o que ele significa, e o último diz o estado do roteiro e das pendências.

[Ver esta seção no template](../caderno/template.md#a-solucao-em-uma-pagina){ .caderno-botao }
[Ver o gabarito do exercício 24](../gabaritos/gabarito-exercicio-24.md){ .caderno-botao }

{{/ficha}}

{{ficha:10:6}}

**Para que serve.** Nem tudo no projeto está decidido, e a Diretoria de TI precisa saber o que ainda impede a ACME de seguir e quem resolve cada ponto. A seção 10 guarda essa lista, e nesta versão final ela recebe também a conferência do caderno, que aponta a decisão sem requisito de origem, o requisito sem decisão e a pendência sem responsável. Sem a conferência, a lista pode conter um ponto sem dono, e esse ponto permanece parado até alguém perguntar por ele.

**O que você faz neste exercício.** No item 1, você registra as inconsistências que encontrou na tabela do enunciado e a regra que cada uma viola. No item 3, você reúne as pendências do seu caderno, acrescenta as que a conferência revela e escreve para cada uma quem decide e quando se resolve, de modo que toda linha da lista final tenha responsável e prazo.

| Campo do caderno | Como preencher | Item |
| --- | --- | --- |
| Inconsistência apontada | Indique a linha da tabela que viola uma regra e diga o que falta nela | 1 |
| Regra violada | Diga qual das três regras de rastreabilidade a linha viola | 1 |
| Pendência | Escreva cada pendência em uma frase que se entenda sozinha | 3 |
| Quem decide | Nomeie o responsável por resolver a pendência | 3 |
| Quando se resolve | Diga o marco ou a data em que a pendência deve estar resolvida | 3 |

**O que você já tem.** A lista de pendências do exercício 20 e a tabela do enunciado, que traz uma inconsistência de cada tipo.

**Quando está pronto.** Cada inconsistência da tabela tem a linha, o que falta e a regra violada, e cada pendência da lista final tem quem decide e quando se resolve.

[Ver esta seção no template](../caderno/template.md#10-o-que-ainda-falta-decidir){ .caderno-botao }
[Ver o gabarito do exercício 24](../gabaritos/gabarito-exercicio-24.md){ .caderno-botao }

{{/ficha}}

## Exercício 24

A ACME chega ao fim da disciplina com um caderno de onze seções, e antes de entregá-lo à Reitoria o arquiteto confere se ele cumpre as três regras de rastreabilidade apresentadas no Conceito. O enunciado traz a tabela de rastreabilidade que a equipe montou para essa conferência, com oito linhas numeradas de 1 a 8, e o exercício tem três itens. No item 1, o aluno aponta as inconsistências da tabela. No item 2, escreve a versão final do resumo de uma página, a seção 0 do caderno. No item 3, escreve a versão final das pendências, a seção 10.

Os dados da tabela vêm dos gabaritos dos exercícios 1 a 20 e do [dossiê da ACME](../caso-acme/index.md), e a tabela foi alterada de propósito para conter erros. Nela, um código formado por R e um número identifica um requisito do dossiê, a exigência que a solução precisa cumprir, como o R6, o portal sustentar 5.800 sessões simultâneas na abertura da matrícula. Um código formado por RT e um número identifica uma restrição, como o RT6, a manutenção do núcleo COBOL sob contrato da fábrica, e um código formado por D e um número identifica uma das nove decisões levantadas na [Aula 1](../modulo-1-fundamentos/bloco-1-arquitetura-de-solucoes-e-de-software.md). ADR é o registro de decisão arquitetural, como o escrito no [Exercício 12](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md#exercicio-12) e o escrito no [Exercício 20](../modulo-5-frameworks-e-tecnologias/bloco-4-adr-de-plataforma.md#exercicio-20).

### Item 1: Conferência da tabela de rastreabilidade

Uma tabela de rastreabilidade só ajuda quem decide se cada linha diz de onde a decisão veio, onde ela aparece no desenho e quem responde por ela. A tabela abaixo reúne oito linhas da ACME, e uma célula escrita como "em branco" indica que a informação falta na tabela. Cada linha traz a decisão ou a pendência, o requisito ou a restrição que a motivou, o ponto do desenho em que aparece, que pode ser um contêiner ou uma relação do [diagrama de contêineres do Exercício 16](../modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md#exercicio-16), e o responsável.

| Linha | Decisão ou pendência | Requisito ou restrição de origem | Onde aparece no desenho | Responsável |
| --- | --- | --- | --- | --- |
| 1 | Fila entre o portal e o núcleo COBOL na entrada da matrícula, registrada no ADR 001 | O portal sustentar 5.800 sessões simultâneas na abertura da matrícula, com percentil 95 de até 4 segundos (R6) | Serviço de matrícula na frente do núcleo, relações 1 e 3 do diagrama de contêineres | Diretor de TI |
| 2 | O índice de busca de disciplinas do portal passa a ficar em memória (D6) | Em branco | Funcionamento interno do portal, sem relação própria no diagrama de contêineres | Arquiteto de software |
| 3 | A propagação da nota ao ambiente virtual de aprendizagem passa do lote diário a até 10 minutos (D2) | A nota lançada pelo professor chegar ao ambiente virtual em até 10 minutos (R7) | Serviço de notas, relações 2, 4 e 6 do diagrama de contêineres | Reitoria |
| 4 | Pendência: ensaio de carga com 5.800 sessões em ambiente equivalente ao de produção, a resolver antes de aceitar o ADR 001 | O portal sustentar 5.800 sessões simultâneas (R6) | Ambiente de teste de carga, que a ACME ainda não tem | Em branco |
| 5 | Gravação da tabela de saída do padrão Transactional Outbox na mesma transação da nota, dentro do programa COBOL | A nota chegar ao ambiente virtual em até 10 minutos (R7) e a restrição de manutenção do núcleo COBOL sob contrato da fábrica até 30/09/2027 (RT6) | Relação 4, do serviço de notas ao núcleo | Fábrica de software |
| 6 | Nenhuma decisão registrada | O custo anual de propriedade cair de R$ 15,83 milhões para R$ 11,0 milhões até o fim de 2029 (R15) | Nenhum contêiner nem relação do diagrama | Diretoria de TI |
| 7 | Nenhum dado pessoal de aluno é processado fora do território nacional (D4) | O parecer do Jurídico de 28/04/2026, restrição RT5 | Região nacional de implantação dos contêineres em nuvem, na zona de pouso | Jurídico |
| 8 | Plataforma de microsserviços na variante Java, com o Kafka, produto de mensageria, como barramento de eventos (ADR de plataforma) | As 5.800 sessões simultâneas (R6), a nota em até 10 minutos (R7) e a restrição dos dois provedores de nuvem pré-aprovados (RT3) | Serviços de matrícula e de notas do diagrama de contêineres | Diretor de TI |

A tabela traz uma inconsistência de cada um dos três tipos, e as outras cinco linhas estão corretas, inclusive as que citam uma restrição como origem, porque a restrição motiva decisões tanto quanto um requisito.

1. Aponte a linha de cada inconsistência e diga o que falta nela.
2. Diga, para cada uma, qual das três regras de rastreabilidade ela viola: toda decisão cita o requisito ou a restrição que a motivou, todo requisito cita a decisão que o atende, ou toda pendência tem responsável e prazo.

Suas respostas viram os campos Inconsistência apontada e Regra violada, na seção 10 do caderno.

### Item 2: Resumo final de uma página

O resumo da seção 0 é a página que a Reitoria lê antes de qualquer outra, e por isso retoma em poucos parágrafos o que o caderno já registra, sem trazer informação nova. A tabela abaixo diz, para cada um dos seis parágrafos, que pergunta ele responde e em que seção do seu caderno você encontra a resposta, e a versão final se escreve depois de todas as seções porque depende delas.

| Parágrafo | Pergunta que responde | Onde buscar no seu caderno |
| --- | --- | --- |
| O problema | Qual é a situação da ACME e por que ela exige mudança? | Seção 1 |
| A pergunta | Que pergunta o projeto responde? | Seção 1 |
| A decisão | Qual é a decisão central do projeto e em que estado ela está? | Seções 7 e 8 |
| O que mais pesa no desenho | Que exigência pesa mais e com que medida? | Seção 3 |
| Consequências | O que a decisão custa à ACME? | Seções 7 e 8 |
| Como está o trabalho | O que está decidido, o que está proposto e o que falta? | Seções 9 e 10 |

1. Escreva os seis parágrafos do resumo, cada um em frases que se entendam sozinhas, com o conteúdo dito em palavras antes de qualquer código. Use como ponto de partida a versão do Exercício 20 e acrescente o roteiro em ondas, a governança e as pendências que a conferência do item 1 revelou.

Suas respostas viram os campos O problema, A pergunta, A decisão, O que mais pesa no desenho, Consequências e Como está o trabalho, na seção 0 do caderno.

### Item 3: Pendências finais

Cada pendência do caderno precisa dizer quem a resolve e quando, porque uma pendência sem responsável permanece parada. Um exemplo já presente na lista do [Exercício 20](../modulo-5-frameworks-e-tecnologias/bloco-4-adr-de-plataforma.md#exercicio-20) é a data e os decisores do registro que coloca a fila entre o portal e o núcleo (ADR 001), que o Diretor de TI define antes da aprovação do registro. O item pede a lista final, que reúne as pendências do seu caderno com as que a conferência do item 1 acrescenta.

1. Escreva a lista final de pendências em uma tabela, com uma frase que se entenda sozinha para cada pendência, o responsável por resolvê-la e o marco ou a data em que deve estar resolvida.

Suas respostas viram os campos Pendência, Quem decide e Quando se resolve, na seção 10 do caderno.

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seção 3.5.3, grade de rastreabilidade entre os elementos do desenho e a visão original da solução, e seção 7.6, teste estático do desenho por rastreabilidade e matriz de rastreabilidade dos requisitos)

**Material do curso.** O glossário traz as entradas [caderno arquitetural](../referencia/glossario.md#caderno-arquitetural), [artefato de arquitetura](../referencia/glossario.md#artefato-de-arquitetura), [restrição](../referencia/glossario.md#restricao) e [ADR](../referencia/glossario.md#adr), a página de [convenções](../caderno/convencoes.md) explica como uma decisão se liga ao requisito, e o dossiê da instituição fictícia [ACME](../caso-acme/index.md) fornece os requisitos, as restrições e a lista de [artefatos por aula](../caso-acme/artefatos.md).
