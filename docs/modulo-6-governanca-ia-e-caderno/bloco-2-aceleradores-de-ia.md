# Aceleradores de IA

Um modelo de linguagem é um programa que recebe um texto e devolve outro, e por isso consegue rascunhar em poucos minutos os documentos estruturados que o arquiteto produz, como o catálogo de requisitos, o cenário de qualidade e o ADR, o registro de decisão arquitetural. A rapidez traz um risco, porque o rascunho chega com a estrutura completa e a linguagem correta mesmo quando o conteúdo está errado. Este bloco mostra em que ponto de cada fase do trabalho o modelo ajuda, quais tarefas o arquiteto não pode delegar, como conferir cada saída em três etapas, o que não pode entrar em uma instrução enviada ao modelo e como registrar no próprio ADR que houve assistência. O exercício do bloco usa o caso da ACME, a universidade privada fictícia descrita no [dossiê do caso](../caso-acme/index.md).

## Antes de começar

- [ADR](../referencia/glossario.md#adr)
- [Cenário de atributo de qualidade](../referencia/glossario.md#cenario-de-atributo-de-qualidade)
- [Restrição](../referencia/glossario.md#restricao)
- [Dado pessoal sensível](../referencia/glossario.md#dado-pessoal-sensivel)

## Conceito

Para levar ao Diretor de TI o registro da decisão sobre a fila na entrada da matrícula, o arquiteto da ACME pediu a um modelo de linguagem o rascunho do ADR e anexou ao pedido as atas das entrevistas, o formato de dez campos e um documento de orientação do projeto. Em poucos minutos voltou um texto com todos os campos preenchidos, escrito com a segurança de quem conhece o caso. O arquiteto quase o aprovou, mas ao reler o contexto estranhou que o portal precisasse atender 4.000 usuários simultâneos com tempo médio de confirmação de até 3 segundos, porque o requisito vigente da Diretoria de TI, registrado no dossiê como R6, pede 5.800 sessões simultâneas e percentil 95 do tempo de confirmação em até 4 segundos. Os dois números errados vinham de uma versão antiga do documento de orientação, que estava entre os anexos.

A releitura revelou ainda outros dois defeitos. O campo de consequências citava só ganhos, como o núcleo deixar de receber a rajada direta, e omitia que o aluno deixaria de receber a confirmação da matrícula na hora. O campo de estado dizia Aceita, embora a decisão ainda dependesse do Diretor de TI. Uma saída com estrutura completa, linguagem correta e conteúdo incorreto, inventado ou incompatível com a fonte chama-se **saída plausível e errada**, e ela é o risco central do uso de IA no trabalho do arquiteto, porque a aparência de completude é o sinal que um revisor usa para concluir que o texto pode seguir para a fase seguinte.

Os registros que o aluno já escreveu mostram por que esse erro custa caro. O ADR do exercício 12, na seção 7 do caderno, tem como contexto as 5.800 sessões da abertura e o incidente de 04/02/2026, e o ADR de plataforma do exercício 20, na seção 8, cita esse registro pelo título. Se o número de 4.000 usuários tivesse entrado no primeiro, passaria para as forças, para o teste de carga planejado e para o acordo de nível de serviço, e o segundo herdaria o erro pela referência cruzada. A seção 9, que este bloco preenche, é o lugar onde o caderno fixa as regras de uso de IA no projeto para que isso seja evitado.

### Onde o modelo entra em cada fase

O processo de definição da arquitetura produz e consome texto estruturado em quase todas as fases, e por isso cada fase tem um uso de IA ligado à saída que ela precisa entregar. Um catálogo de requisitos tem código, declaração e origem, o cenário de qualidade tem seis elementos fixos e o ADR tem dez campos, de modo que o formato diz ao modelo o que produzir e diz ao revisor o que procurar. A tabela mostra o uso de cada fase, e a distribuição por fase é proposta do curso, porque os usos conhecidos não vêm atribuídos a uma fase específica.

| Fase | Uso do modelo | Modo |
| --- | --- | --- |
| Iniciação e descoberta | Consolidar entradas e entrevistas num registro de motivadores, restrições e partes interessadas, com a entrevista de origem de cada linha | Redator |
| Esboço da solução | Confrontar a direção candidata com as restrições declaradas pela organização | Crítico |
| Análise | Rascunhar o catálogo de requisitos, converter requisito vago em cenário de qualidade e procurar lacuna esquecida no relatório de lacunas | Redator e crítico |
| Projeto lógico | Rascunhar o ADR com alternativas e o esqueleto da especificação de contrato | Redator |
| Validação | Criticar o desenho lógico contra os atributos de qualidade priorizados | Crítico |
| Roteiro e governança | Conferir uma proposta nova contra as decisões já registradas | Crítico |

Em todas as fases, o modelo ajuda a produzir o material, e quem responde diante do patrocinador à pergunta de saída da fase continua sendo o arquiteto de solução.

### O modelo como redator e como crítico

A tabela abaixo compara os dois modos, e o pedido do arquiteto da ACME ilustra o primeiro, porque o modelo recebeu material bruto e o formato do artefato e devolveu um rascunho. Depois da correção, ele usou o modelo no segundo modo, entregando-lhe o ADR revisado, o catálogo de requisitos e as restrições do caso e pedindo a lista dos pontos em que o texto se afasta deles.

| Modo | O que o modelo recebe | O que devolve | O que o arquiteto confere |
| --- | --- | --- | --- |
| Redator | Material bruto e o formato do artefato | Um rascunho | Cada elemento do rascunho contra a fonte |
| Crítico | Um artefato pronto, o requisito e a restrição que ele deve atender | Uma lista de desvios, cada um com o trecho e o critério envolvidos | Cada desvio contra o artefato e contra o critério citado |

O crítico trabalha sobre um texto que pode ter sido escrito por uma pessoa ou pelo próprio modelo, e sua saída é uma lista de suspeitas. Num exemplo da ACME, o crítico recebeu o relatório de lacunas e apontou dois itens. O primeiro, a ausência de aviso ao fornecedor do ambiente virtual quando o leiaute do arquivo de notas muda, procede, porque essa falha causou o incidente de 09/07/2026. O segundo sugere substituir o ERP financeiro, e a Reitoria decidiu em 12/03/2026 que ele permanece. Um item falso custa alguns minutos de conferência, e um item verdadeiro evita que o desvio chegue à validação com as partes interessadas. O pedido ao crítico precisa trazer o critério declarado, porque sem o requisito e as restrições ele devolve observações genéricas, que nenhum arquiteto consegue aplicar à confirmação de uma matrícula.

### Os quatro assistentes do arquiteto

A ACME organizou o uso do modelo em quatro assistentes, e cada um é descrito em um arquivo com identidade, missão, regras críticas, entregável e métrica de sucesso. O arquivo fica versionado no repositório de arquitetura, e a cada sessão muda apenas a tarefa pedida. A tabela mostra a fase em que cada assistente trabalha e como sua saída é conferida.

| Assistente | Fase | O que faz | Como a saída é conferida |
| --- | --- | --- | --- |
| Entrevistador Arquiteto | Iniciação e descoberta | Conduz a entrevista com uma pergunta por vez e nunca responde no lugar da parte interessada. Na ACME, ele ajuda a fechar com a Coordenadora de Educação a Distância o percentil e a carga de referência do prazo de 10 minutos para a nota chegar ao ambiente virtual | A resposta registrada é da parte interessada, e a ata comprova |
| Gerador de Cenários de Atributos de Qualidade | Análise | Escreve os seis elementos do cenário usando só os fatos fornecidos e cita a fonte de cada número. Na ACME, o exemplo é a disponibilidade de 99,9% na janela de matrícula, com 43 minutos de indisponibilidade tolerados por mês | Cada número aponta para o requisito ou para o dado de origem |
| Revisor Crítico de Arquitetura | Validação | Aponta desvios contra critérios declarados, sem reescrever o artefato, sob uma de três lentes, a de arquitetura, a de back-end e a de front-end, cada uma com a sua lista de cobranças | O par humano confirma cada desvio a partir da fonte citada, e desvio sem fonte é descartado |
| Desenhador de Modelos em PlantUML | Projeto lógico | Converte as tabelas de contêineres e de ligações em código de diagrama no [modelo C4](../referencia/glossario.md#modelo-c4) e devolve a lista do que desenhou | A lista é comparada com as tabelas, porque elemento a mais é invenção e elemento a menos é omissão |

### O que o arquiteto não delega

Quando a Coordenadora de Educação a Distância pede a nota no ambiente virtual em minutos e o Diretor Financeiro responde pelo acréscimo de 38% no valor anual do contrato, nenhum texto entregue ao modelo contém a informação que decide, que é a disposição do patrocinador e o orçamento do próximo exercício. O modelo pode organizar os argumentos dos dois lados e listar o que falta saber para a reunião. O ADR então fica em estado de proposta, com o campo de decisão vazio, até que o Diretor Financeiro decida e tenha o nome registrado.

Esse caso ilustra uma das quatro tarefas que exigem julgamento do arquiteto e não se delegam ao modelo.

1. Priorizar atributos de qualidade em conflito, como o desempenho no pico contra o custo de operação.
2. Aceitar um risco, o que significa que alguém com autoridade declara que a organização convive com uma consequência negativa conhecida.
3. Escolher entre alternativas de custo comparável, quando a análise deixa duas opções equivalentes.
4. Negociar com as partes interessadas.

As quatro têm em comum o fato de que a informação que decide está fora do texto e de que existe um responsável que responde pela consequência perante a organização.

### A saída plausível e errada, quatro vezes

O erro plausível aparece em qualquer artefato, e a tabela traz quatro casos da ACME com o fato que revela cada um. Em todos, o formato está completo e o defeito só surge quando alguém compara o conteúdo com a fonte.

| Artefato | Erro plausível | Fato que o revela |
| --- | --- | --- |
| Cenário de qualidade | Medida pela média de 3 segundos, quando o requisito fixa o percentil 95 em até 4 segundos | O requisito vigente, de 5.800 sessões simultâneas |
| ADR | Só vantagens, sem consequência negativa | O modelo de dez campos exige ao menos uma consequência negativa |
| Relatório de lacunas | Proposta de substituir o ERP financeiro | A decisão da Reitoria de 12/03/2026 de manter o ERP |
| Contrato do serviço de matrícula | Operação de cancelar matrícula | Nenhum dos 15 requisitos do catálogo pede cancelamento |

O custo do erro cresce com a distância entre a fase em que ele entra e a fase em que é encontrado. O número de 3 segundos, se aceito no cenário da análise, passaria para as forças do ADR no projeto lógico, para o contrato do serviço de matrícula e para o acordo de nível de serviço, e uma descoberta na validação obrigaria a refazer o trabalho das fases intermediárias.

### A verificação em três etapas

A resposta ao risco é um procedimento aplicado a toda saída do modelo, sem exceção para o texto que parece correto. Cada etapa faz uma pergunta diferente, e a terceira cabe a uma pessoa que não participou do pedido.

| Etapa | Pergunta | O que encontrou na ACME |
| --- | --- | --- |
| Rastreabilidade até a fonte | De onde vem cada número, nome e decisão do texto? Cada elemento se liga ao requisito, à entrevista ou ao dado que o justifica | O número superado no cenário e no contrato, e a operação sem requisito no contrato |
| Checagem contra a restrição declarada | O texto respeita as restrições, as decisões já registradas e o modelo do artefato? | O custo omitido no ADR e a sugestão de trocar o ERP |
| Revisão por par | Alguém que não escreveu o pedido e conhece o contexto confirma que cada correção tem fonte registrada? | Vale para as quatro saídas da tabela anterior |

O ponto de concentração muda conforme o artefato. No ADR, a rastreabilidade liga cada força a um cenário, a um princípio ou a uma restrição, e a checagem confirma que as alternativas foram comparadas pelas mesmas forças e que existe ao menos uma consequência negativa declarada. Na especificação de contrato, cada operação se liga a um requisito, e o documento passa por um validador da especificação antes da revisão por par.

### O que classificar antes de enviar ao modelo

A ata da entrevista com a Representação discente cita nomes e matrículas de alunos, e o requisito de que nenhum dado pessoal de aluno seja processado fora do território nacional, registrado no dossiê como R14, vale para todo o projeto. Todo texto colocado em um prompt, que é a instrução enviada ao modelo, sai do documento de origem e passa a ser processado pelo serviço que executa o modelo, que pode estar fora do país. Por isso o arquiteto classifica o conteúdo antes de enviá-lo e usa apenas um modelo aprovado pela área de segurança.

| Conteúdo | Tratamento antes do envio |
| --- | --- |
| Dado pessoal de aluno, professor ou funcionário | Substituir por dado fictício ou por rótulo genérico |
| Dado pessoal sensível | Excluir |
| Cláusula contratual com fornecedor | Resumir sem valores e sem nomes |
| Credencial de acesso | Nunca incluir |

A Lei Geral de Proteção de Dados Pessoais, a LGPD, distingue o dado pessoal do dado pessoal sensível no artigo 5º e limita o tratamento ao mínimo necessário para a finalidade no artigo 6º, inciso III, como a [tabela de exigências da Aula 4](../modulo-4-dominios-da-solucao/bloco-2-arquitetura-de-dados.md) detalha. Uma ata com nomes de alunos excede o necessário para gerar um cenário de qualidade. A lei não exige que o dado fique no território nacional, e a exigência vem, na ACME, do parecer do Jurídico de 28/04/2026, registrado como restrição da solução.

### O prompt versionado e o registro da assistência

Com o conteúdo classificado, o cuidado seguinte é com o próprio prompt, que passa a ser um artefato com versão, revisão e reuso, guardado no repositório de arquitetura ao lado dos ADRs. Sabendo a versão, a equipe descobre qual prompt produziu cada artefato, submete a mudança do prompt à mesma revisão por par de uma mudança de código e reaproveita o prompt em decisão semelhante. A tabela mostra um exemplo de arquivo de prompt, o do crítico do contrato de matrícula, em que R1 a R15 são os quinze requisitos do catálogo da ACME.

| Campo | Exemplo |
| --- | --- |
| Versão | critico-contrato 1.2 |
| Entrada esperada | Especificação do serviço de matrícula, catálogo de requisitos de R1 a R15, cenário de qualidade da abertura da matrícula e os ADRs já registrados |
| Formato de saída | Lista de desvios, cada um com o trecho do contrato, o requisito ou a decisão envolvida e a gravidade |
| Critério de verificação | Cada desvio é conferido contra a fonte citada, e desvio sem fonte é descartado |

O último cuidado é o registro, no próprio ADR, de que houve assistência de IA. A proposta do curso é usar o campo de evidências, que já reúne o que sustenta a decisão, para abrir a subseção Assistência de IA, com as partes rascunhadas pelo modelo, o prompt e a versão usados, as verificações aplicadas e o nome do revisor. Esse registro serve a quem lê o ADR depois da decisão e responde, numa auditoria futura, se algum dado pessoal foi enviado a um modelo durante o projeto.

## Uso pelo arquiteto

O arquiteto consulta a verificação de três etapas no momento em que um rascunho de modelo chega às suas mãos, antes de copiar qualquer trecho para o caderno. A dúvida que ela resolve é se o texto, que parece completo, pode seguir para a fase seguinte. Quando o arquiteto da ACME rastreou o número de 4.000 usuários e não encontrou um requisito vigente que o sustentasse, descartou o trecho antes que ele chegasse às forças do ADR, e levou ao Diretor de TI um registro com as 5.800 sessões do requisito vigente (R6). Se tivesse aceitado o rascunho, o número errado passaria às forças do ADR e ao teste de carga planejado.

A classificação do conteúdo e o registro da assistência atendem a outro interlocutor, a encarregada de proteção de dados e quem audita o projeto. O arquiteto classifica o material antes de montar o prompt para poder afirmar à encarregada que nenhuma ata com nome de aluno saiu da rede da ACME, e usa a subseção de assistência do ADR para provar o que foi gerado, com qual prompt e quem conferiu. Sem esse registro, uma pergunta de auditoria sobre dado pessoal enviado a um modelo só teria resposta pela memória de quem trabalhou no projeto.

As quatro tarefas de julgamento delimitam o que o arquiteto leva a quem decide. O modelo prepara o material de uma escolha como a do plano superior do ambiente virtual, com os argumentos de cada lado e a lista do que falta saber, e o arquiteto o apresenta ao Diretor Financeiro com o ADR em estado de proposta. Se o arquiteto deixasse o texto do modelo marcar a decisão como tomada, o ADR registraria uma aprovação que ninguém deu.

## No caderno arquitetural

{{ficha:9}}

**Para que serve.** Quando a ACME for auditada, ou quando um novo arquiteto herdar o caderno, alguém vai perguntar quais textos do projeto foram rascunhados por um modelo de linguagem e quem os conferiu. A seção 9 do caderno guarda as regras de uso de IA no projeto, com os erros que a verificação encontrou e o registro da assistência, e por isso a resposta continua disponível mesmo depois que a equipe original deixar o projeto.

**O que você faz neste exercício.** Você recebe um trecho do registro de decisão sobre a fila na entrada da matrícula (o ADR 001), rascunhado por um modelo de linguagem, com os dados corretos do caso numa tabela ao lado, e aplica as três verificações do Conceito. No item 1 você confere cada afirmação do contexto contra a fonte vigente. No item 2 você aponta a consequência omitida e o estado que não cabia ao modelo definir. No item 3 você escreve o registro da assistência, com a ferramenta, o prompt, as verificações e o revisor.

| Campo do caderno | Como preencher | Item |
| --- | --- | --- |
| Verificação de rastreabilidade | Diga, para cada afirmação do contexto gerado, se ela tem origem em dado vigente e corrija a que não tem, citando a fonte | 1 |
| Consequência omitida | Escreva as consequências negativas que o rascunho não traz, com o dado do enunciado que as comprova | 2 |
| Decisão que volta à autoridade | Corrija o estado e a data do registro e diga quem decide | 2 |
| Registro da assistência de IA | Escreva a ferramenta, as partes rascunhadas, o prompt e a versão, as verificações aplicadas e o revisor | 3 |

**O que você já tem.** O registro de decisão sobre a fila na entrada da matrícula (ADR 001), do exercício 12, na seção 7, e o ADR de plataforma do exercício 20, na seção 8, que o trecho gerado do enunciado reproduz em parte, além dos requisitos da seção 3.

**Quando está pronto.** Cada erro do trecho gerado está apontado com a fonte da correção, as consequências omitidas estão escritas, o estado e a data voltaram a quem decide, e o registro da assistência traz os cinco dados pedidos.

[Ver esta seção no template](../caderno/template.md#9-roteiro-e-governanca){ .caderno-botao }
[Ver o gabarito do exercício 23](../gabaritos/gabarito-exercicio-23.md){ .caderno-botao }

{{/ficha}}

## Exercício 23

A ACME é a universidade privada brasileira em modernização incremental do sistema acadêmico, usada como caso desta disciplina. Este exercício treina a conferência de um texto escrito por modelo de linguagem, porque o arquiteto que aceita um rascunho sem conferir leva o erro a todos os registros que dependem dele. O arquiteto da ACME pediu a um modelo, aprovado pela área de segurança, o rascunho do registro de decisão sobre a fila entre o portal e o núcleo na entrada da matrícula, o ADR 001 do [exercício 12](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md#exercicio-12), e anexou ao pedido as atas das entrevistas, o formato de dez campos e um documento de orientação do projeto.

O enunciado traz duas tabelas. A primeira reproduz parte do que o modelo devolveu, e a segunda reúne oito dados vigentes do caso, que servem de fonte para a conferência. O exercício tem três itens, e em cada um você aplica uma das verificações do Conceito. Nos enunciados, um código formado por R e um número, como R6, identifica um requisito do dossiê da ACME, a exigência que a solução precisa cumprir.

| Campo | Texto gerado pelo modelo |
| --- | --- |
| Estado | Aceita |
| Data | 14/09/2026 |
| Contexto | Na abertura da matrícula, o portal precisa atender 4.000 usuários simultâneos, com confirmação em tempo médio de até 3 segundos. A taxa de erro nessa abertura chega a 6,3%, contra a meta de 1%. Em 04/02/2026, o portal ficou indisponível por 4h20. O núcleo COBOL não pode ser alterado durante a transição |
| Decisão | Adotar a arquitetura orientada a eventos na entrada da matrícula, com fila entre o portal e o núcleo. A decisão foi aprovada pelo Diretor de TI |
| Consequências | O núcleo deixa de receber a rajada direta e processa no ritmo que sustenta. A taxa de erro na janela de matrícula cai. A equipe ganha isolamento entre o portal e o núcleo |

| Nº | Dado vigente | Valor | Origem |
| --- | --- | --- | --- |
| 1 | Pico na abertura da matrícula | 5.800 sessões simultâneas, com percentil 95 do tempo de confirmação em até 4 segundos | Requisito R6, da Diretoria de TI |
| 2 | Sessões simultâneas em média no ano | 815 | [Dados operacionais](../caso-acme/dados-operacionais.md) |
| 3 | Taxa de erro na abertura da matrícula | 6,3%, e a meta registrada no ADR é de 1% | Dados operacionais e ADR do exercício 12 |
| 4 | Incidente de 04/02/2026 | 4h20 de indisponibilidade e 62% das tentativas de matrícula com erro | Dados operacionais |
| 5 | Documento de orientação anexado ao pedido | Versão anterior, que registrava 4.000 usuários simultâneos e tempo médio de até 3 segundos | Anexo do pedido ao modelo |
| 6 | Estado e data do ADR 001 | Proposta, com data a definir junto ao Diretor de TI | ADR do exercício 12 |
| 7 | Consequências negativas do ADR 001 | O aluno deixa de receber a confirmação da matrícula na hora. A equipe passa a operar um componente assíncrono, em que quem envia segue adiante sem esperar resposta. Os seis padrões exigem manter duas implementações e ajustar limites sem teste de carga. A mensagem pode ser entregue mais de uma vez | ADR do exercício 12 |
| 8 | Exigência do modelo de ADR | Ao menos uma consequência positiva, uma negativa e uma neutra | Template de dez campos, no [bloco 4 da Aula 3](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md) |

### Item 1: Rastreabilidade até a fonte

A primeira verificação pergunta de onde vem cada afirmação, e por isso este item confere as quatro afirmações do campo de contexto contra os dados vigentes da segunda tabela. As quatro são, na ordem do texto gerado, os 4.000 usuários simultâneos, o tempo médio de até 3 segundos, o erro de 6,3% contra a meta de 1% e as 4h20 de indisponibilidade em 04/02/2026.

1. Para cada uma das quatro afirmações, diga se ela tem origem em um dado vigente da segunda tabela e cite o número do dado.
2. Para a afirmação que não tem origem vigente, escreva o valor correto e diga de onde o valor errado veio.

Sua resposta vira o campo Verificação de rastreabilidade, na seção 9 do caderno.

### Item 2: Checagem contra a restrição e a decisão que pertence a quem tem autoridade

A segunda verificação compara o texto com o que já está registrado e com o modelo do artefato, e este item pede duas conferências sobre os campos de consequências e de estado. A primeira procura o que o rascunho deixou de dizer, e a segunda procura o que o modelo afirmou sem ter autoridade para afirmar.

1. Diga qual exigência do modelo de ADR (dado 8 da segunda tabela) o campo de consequências gerado não cumpre e escreva duas das consequências negativas do dado 7 que o rascunho omite, indicando qual delas o aluno percebe na matrícula.
2. Diga que estado e que data o ADR deve ter segundo o dado 6 da segunda tabela, quem decide e a qual das quatro tarefas que não se delegam ao modelo corresponde a aceitação das consequências negativas.

Suas respostas viram os campos Consequência omitida e Decisão que volta à autoridade, na seção 9 do caderno.

### Item 3: Registro da assistência

A terceira etapa é a revisão por par, e depois dela o ADR precisa registrar o que aconteceu para que o leitor futuro saiba o que o modelo escreveu. O registro vai na subseção Assistência de IA do campo de evidências, e os fatos da sessão do arquiteto da ACME estão na lista abaixo.

- Ferramenta: modelo de linguagem aprovado pela área de segurança, sem dado pessoal no pedido, porque as atas foram tratadas antes do envio.
- Pedido: arquivo de prompt redator-adr, versão 1.0, do repositório de arquitetura.
- Partes rascunhadas pelo modelo: contexto, forças, decisão e consequências.
- Verificações aplicadas: as três etapas do Conceito, com os dados da segunda tabela.
- Revisão por par: o segundo arquiteto da equipe, que não escreveu o pedido e conhece o contexto da solução, com o nome a preencher.

Escreva o registro da assistência, com os cinco dados pedidos pelo campo (ferramenta, partes rascunhadas, prompt e versão, verificações aplicadas e revisor), em uma frase ou linha para cada um.

Sua resposta vira o campo Registro da assistência de IA, na seção 9 do caderno.

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Fowler, M. (n.d.). *Exploring generative AI* [Série de artigos de vários autores, entre eles Birgitta Böckeler, sobre o uso de IA generativa no desenvolvimento de software]. martinfowler.com. Acesso em 16 de outubro de 2026. https://martinfowler.com/articles/exploring-gen-ai.html
- Mendes, M. (2026a). *Arquitetura de software* [Material de curso]. https://marco-mendes.github.io/arquitetura-software/ ([template de ADR](https://marco-mendes.github.io/arquitetura-software/referencia/template-adr/) de dez campos, em que a subseção de assistência de IA se apoia)

**Material do curso.** A tabela de exigências da LGPD vem do [bloco 2 da Aula 4](../modulo-4-dominios-da-solucao/bloco-2-arquitetura-de-dados.md), o glossário traz as entradas [ADR](../referencia/glossario.md#adr), [cenário de atributo de qualidade](../referencia/glossario.md#cenario-de-atributo-de-qualidade), [restrição](../referencia/glossario.md#restricao) e [dado pessoal sensível](../referencia/glossario.md#dado-pessoal-sensivel), e o dossiê da instituição fictícia [ACME](../caso-acme/index.md) fornece os requisitos, as restrições e os [dados operacionais](../caso-acme/dados-operacionais.md). A divisão em redator e crítico, os quatro assistentes, as três verificações e a proposta de registrar a assistência no campo de evidências do ADR vêm do material do curso a distância da disciplina e não têm fonte externa.
