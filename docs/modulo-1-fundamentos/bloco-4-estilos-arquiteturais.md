# Estilos arquiteturais e sua relação com atributo de qualidade

Este bloco fecha a aula respondendo a uma pergunta que depende de tudo o que veio antes, qual padrão de organização estrutural sustenta melhor os atributos de qualidade que um cenário já revelou como significativos.

## Antes de começar

- [Estilo arquitetural](../referencia/glossario.md#estilo-arquitetural)

## Conceito

Um estilo arquitetural é um padrão de organização estrutural de um sistema, que define tipos de componentes, formas de conexão entre eles e restrições sobre essa organização. A definição tem três partes que merecem exame separado. Tipos de componentes significa que o estilo nomeia categorias recorrentes de elemento, como camada, serviço ou produtor de evento, não instâncias específicas de um sistema. Formas de conexão significa que o estilo fixa como esses elementos se comunicam, de forma síncrona ou assíncrona, direta ou mediada por um intermediário. Restrições sobre essa organização significa que o estilo proíbe certas relações, como uma camada inferior chamar uma camada superior, ou um serviço acessar diretamente o banco de outro serviço. Um estilo arquitetural descreve, portanto, a forma macro de um sistema inteiro, e não a organização interna de uma única camada ou de um único componente.

A escolha de estilo está entre as decisões de maior impacto sobre a arquitetura porque ela define, de antemão, quais atributos de qualidade o sistema consegue sustentar com naturalidade e quais exigirão esforço extra ou mecanismo compensatório. Um estilo que concentra processamento em um único processo favorece consistência transacional e simplicidade operacional, mas tende a limitar a escalabilidade independente de partes do sistema com carga desigual. Um estilo que distribui processamento em unidades independentes favorece escalabilidade seletiva e implantação isolada, mas introduz consistência eventual, latência de rede e superfície maior de falha parcial. Ford e Richards descrevem essa comparação de estilos por atributo de qualidade como o instrumento central da decisão, porque nenhum estilo maximiza todos os atributos ao mesmo tempo, e a escolha declara, de forma implícita, quais atributos o arquiteto está disposto a sacrificar em favor de outros.

O quadro abaixo apresenta quatro estilos, os tipos de componente que cada um define, a forma de comunicação entre eles e os atributos de qualidade que cada um tende a favorecer ou a prejudicar.

| Estilo | Componentes | Comunicação | Favorece | Prejudica |
| --- | --- | --- | --- | --- |
| Arquitetura em camadas | Camadas horizontais com responsabilidade fixa, como apresentação, negócio e persistência | Síncrona, sempre da camada superior para a imediatamente inferior | Simplicidade de raciocínio, manutenibilidade dentro de cada camada, curva de aprendizado baixa para equipe nova | Escalabilidade independente de partes do sistema, porque a unidade de implantação costuma ser o sistema inteiro |
| Arquitetura de microsserviços | Serviços autônomos, cada um dono de seu próprio dado e implantado de forma independente | Síncrona por chamada de rede ou assíncrona por mensageria, sempre entre processos distintos | Escalabilidade seletiva, implantação independente, isolamento de falha entre serviços | Consistência transacional entre serviços, complexidade operacional, latência de comunicação entre processos |
| Arquitetura orientada a eventos | Produtores e consumidores de evento, conectados por um intermediário que distribui a mensagem | Assíncrona, mediada por um barramento ou tópico, sem acoplamento direto entre quem publica e quem consome | Desacoplamento temporal entre componentes, absorção de pico de carga por enfileiramento, extensibilidade por novo consumidor sem alterar o produtor | Rastreabilidade do fluxo completo de processamento, consistência imediata, previsibilidade de ordem de entrega |
| Arquitetura microkernel | Um núcleo mínimo com as regras essenciais e plugins que estendem funcionalidade sem alterar o núcleo | O núcleo expõe pontos de extensão fixos, e cada plugin se conecta a esses pontos sem se comunicar diretamente com outro plugin | Extensibilidade controlada, isolamento de funcionalidade opcional, ciclo de liberação independente para cada plugin | Desempenho quando o volume de plugins ativos cresce, coordenação de comportamento que atravessa vários plugins ao mesmo tempo |

A arquitetura em camadas é o estilo mais direto de descrever e o mais frequente em sistema corporativo de escopo estável. Em um sistema de gestão de estoque industrial, a camada de apresentação exibe posição de inventário e ordem de reposição, a camada de negócio aplica regra de ponto de pedido e rateio entre depósitos, e a camada de persistência grava o saldo por item e por local. A dependência entre camadas segue sempre a mesma direção, o que simplifica o raciocínio sobre o sistema, mas concentra a implantação em uma unidade só, de modo que um pico de consulta de estoque em um único depósito força escalar o sistema inteiro, mesmo que os demais depósitos operem em carga normal.

A arquitetura de microsserviços resolve exatamente essa limitação ao custo de outra. Em uma plataforma de streaming de música, o catálogo de faixas, o motor de recomendação e o processamento de pagamento de assinatura podem ser serviços separados, cada um escalado de acordo com sua própria demanda, o motor de recomendação crescendo em época de lançamento de grandes artistas sem exigir que o serviço de pagamento cresça junto. O preço dessa independência é a ausência de uma transação única que atravesse os três serviços, o que obriga a tratar inconsistência temporária entre catálogo e recomendação como situação normal, não como falha.

A arquitetura orientada a eventos favorece situação de pico e de integração entre partes que não precisam saber umas das outras. Em um sistema de reservas de companhia aérea, o serviço de reserva publica um evento de confirmação de assento, e os serviços de emissão de bilhete, de acúmulo de milhas e de notificação ao passageiro consomem esse evento de forma independente, sem que o serviço de reserva conheça a existência deles. O diagrama abaixo mostra essa estrutura.

```mermaid
graph TD
    RES["Serviço de Reserva"]
    PAG["Serviço de Pagamento"]
    BUS(["Barramento de eventos"])
    EMI["Serviço de Emissão de Bilhete"]
    MIL["Serviço de Acúmulo de Milhas"]
    NOT["Serviço de Notificação ao Passageiro"]

    RES -->|"publica ReservaConfirmada"| BUS
    PAG -->|"publica PagamentoAprovado"| BUS
    BUS -->|"consome ReservaConfirmada"| EMI
    BUS -->|"consome ReservaConfirmada"| MIL
    BUS -->|"consome PagamentoAprovado"| NOT
```

O barramento absorve variação de carga entre produtor e consumidor, porque o evento fica retido até que cada consumidor tenha capacidade de processá-lo, o que favorece um pico de reservas na abertura de uma nova rota sem que o serviço de reserva espere a conclusão da emissão de bilhete. O custo aparece quando é preciso reconstruir, depois do fato, a sequência exata de eventos que levou a um estado incorreto, porque a ordem de entrega entre tópicos diferentes não é garantida e o fluxo completo está disperso entre vários consumidores.

A arquitetura microkernel serve bem quando a maior parte do sistema é estável e uma parte pequena precisa variar por cliente ou por mercado. Um sistema de gestão de estoque industrial que atende clientes com regras fiscais diferentes por estado pode manter o núcleo de controle de saldo fixo e tratar cada regra fiscal como um plugin acionado no momento da baixa de estoque. O ganho é liberar um plugin novo sem tocar no núcleo nem nos demais plugins. A limitação aparece quando duas regras fiscais de plugins diferentes precisam ser aplicadas na mesma operação em uma ordem específica, porque o núcleo não foi desenhado para coordenar plugins entre si.

## Uso pelo arquiteto

O arquiteto usa essa comparação de estilo por atributo de qualidade para defender uma escolha diante de partes interessadas com prioridades diferentes, traduzindo uma preferência técnica em uma tabela de trocas explícitas. Em vez de afirmar que um estilo é melhor em abstrato, o arquiteto mostra qual atributo o estilo escolhido favorece, qual ele sacrifica, e associa cada um desses atributos ao cenário de qualidade que a organização já reconheceu como prioritário, o que torna a decisão auditável e reduz a chance de reabri-la sem novo dado.

## Exercício

A ACME é uma universidade privada brasileira cujo sistema acadêmico legado sustenta um núcleo transacional em COBOL sobre o monitor CICS, uma camada web em JSF e EJB e integrações por arquivo em lote com o ERP financeiro e o ambiente virtual de aprendizagem, em processo de modernização incremental.

Os dois cenários abaixo já foram formulados no formato de seis elementos. Se o aluno já escreveu seus próprios cenários no bloco 3, pode usá-los no lugar destes, que servem de versão de referência para quem ainda não os tem.

**Cenário 1, pico de sazonalidade**

| Elemento | Especificação |
| --- | --- |
| Fonte | Alunos veteranos e ingressantes da ACME |
| Estímulo | Acesso simultâneo ao Portal do Aluno para confirmar matrícula |
| Ambiente | Abertura da janela de matrícula, pico de 5.800 sessões simultâneas nos 30 minutos iniciais, razão de 7,1 sobre a média anual ponderada de 815 sessões |
| Artefato | Portal do Aluno e núcleo transacional |
| Resposta | Processar as tentativas de confirmação sem degradar acima de um limite aceitável de erro |
| Medida | Taxa de erro abaixo de 1%, contra os 6,3% observados atualmente no mesmo intervalo |

**Cenário 2, incidente de 04/02/2026**

| Elemento | Especificação |
| --- | --- |
| Fonte | Sessões web abandonadas pelo aluno sem encerramento explícito |
| Estímulo | Transação do monitor CICS permanece aberta após o abandono do navegador, sem tempo limite de sessão configurado |
| Ambiente | Abertura da matrícula de 04/02/2026, sob o mesmo pico de 5.800 sessões simultâneas |
| Artefato | Monitor CICS e núcleo transacional |
| Resposta | Encerrar a transação por tempo limite de sessão antes de esgotar o limite de tarefas concorrentes do CICS |
| Medida | Indisponibilidade contida dentro dos 43 minutos tolerados por mês pelo acordo de nível de serviço, contra os 260 minutos consumidos no incidente registrado, com 62% de erro nas tentativas de matrícula e 9.400 alunos sem inscrição concluída no dia |

Escolha três dos estilos apresentados no Conceito e compare cada um contra os dois cenários acima. Para cada estilo, avalie se ele sustentaria a resposta e a medida descritas, considerando o núcleo COBOL sobre CICS como parte que permanece em operação durante a transição. Ao final, defenda qual dos três estilos se ajusta melhor a um contexto de modernização incremental de um sistema legado crítico, justificando a escolha por atributo de qualidade favorecido e por atributo de qualidade prejudicado.

## Gabarito

<details>
<summary>Critério de avaliação</summary>

A comparação admite defesa razoável de mais de um estilo, porque a ênfase escolhida entre os atributos em jogo, absorção de pico, isolamento de falha ou simplicidade de coordenação, muda qual estilo parece superior. Não há resposta única correta, o critério está na qualidade do argumento, não na coincidência com uma escolha de referência.

Uma comparação bem argumentada trata os dois cenários separadamente antes de concluir. Para o cenário de pico, uma resposta forte reconhece que a arquitetura orientada a eventos absorve a variação entre os 815 sessões da média anual e os 5.800 do pico ao enfileirar a submissão de matrícula diante de um núcleo que não pode ser reescrito de imediato, evitando que a razão de 7,1 se traduza diretamente em sobrecarga do CICS. Uma resposta que defenda microsserviços para o mesmo cenário precisa reconhecer que extrair um serviço de matrícula do núcleo COBOL é trabalho de mais de um ciclo, e que o ganho de escalabilidade seletiva só aparece depois dessa extração, não no estado atual do sistema.

Para o cenário de incidente, uma resposta forte identifica que o problema, ausência de tempo limite de sessão liberando a tarefa do CICS, é um defeito pontual de gestão de sessão na camada web, e não uma evidência de que o estilo inteiro do sistema precisa mudar. Uma resposta forte também nota que a própria arquitetura em camadas já existente, com um mecanismo explícito de expiração de sessão na camada web, resolveria o incidente sem exigir mudança de estilo, o que é um argumento válido contra a necessidade de adotar microsserviços ou eventos só por causa desse cenário isolado.

Uma defesa final consistente amarra a escolha aos dois cenários juntos e ao contexto declarado de modernização incremental de sistema legado crítico, reconhecendo que o núcleo COBOL sobre CICS não pode ser substituído de uma vez. Uma resposta forte tende a favorecer a arquitetura orientada a eventos como camada de amortecimento entre a demanda variável e o núcleo estável, sem descartar que uma correção pontual de sessão na camada web já existente resolve o segundo cenário isoladamente. Uma resposta fraca escolhe um estilo sem examinar os dois cenários separadamente, ou recomenda substituição completa do núcleo como se fosse uma opção disponível no primeiro ciclo, contrariando as restrições de contrato de sustentação já registradas no caso.

</details>

## Fontes

Glossário do curso, entrada [estilo arquitetural](../referencia/glossario.md#estilo-arquitetural). Ford, N. e Richards, M., obra de referência sobre comparação de estilos arquiteturais por atributo de qualidade, listada na [bibliografia](../referencia/bibliografia.md). Bass, L., Clements, P. e Kazman, R., Software Architecture in Practice, listado na [bibliografia](../referencia/bibliografia.md). Dossiê da instituição fictícia [ACME](../caso-acme/index.md), [arquitetura de linha de base](../caso-acme/linha-de-base.md) e [dados operacionais](../caso-acme/dados-operacionais.md).
