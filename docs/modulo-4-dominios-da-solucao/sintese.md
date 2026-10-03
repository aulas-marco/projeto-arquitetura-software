# Síntese da Aula 4

Esta página fecha o módulo de domínios da arquitetura de solução com o que precisa permanecer depois da aula, a cadeia dos domínios construída nos quatro exercícios, uma autoavaliação e as fontes principais da aula, e as demais constam das Fontes de cada bloco e da bibliografia.

## Checklist do que precisa permanecer

- As quatro perguntas que decidem se um problema admite tratamento por arquitetura de solução, e a redução de escopo como resposta ao problema grande demais
- Os quatro modelos de arquitetura de negócio, mapa de [capacidades](../referencia/glossario.md#capacidade), [fluxo de valor](../referencia/glossario.md#fluxo-de-valor), decomposição funcional e modelo de processo, com a pergunta que cada um responde e a regra de que o arquiteto os consulta sem modelá-los
- A exigência de consistência entre a arquitetura de dados da solução e o [modelo de dados corporativo](../referencia/glossario.md#modelo-de-dados-corporativo), do qual a solução recebe um recorte e ao qual devolve a diferença que cria
- O estilo de [dado mestre](../referencia/glossario.md#dados-mestres) das entidades compartilhadas e as obrigações da LGPD sobre o dado pessoal, traduzidas em classificação, retenção e trilha de auditoria
- A grade dado × aplicação, com dono, consumidores e [regime de consistência](../referencia/glossario.md#regime-de-consistencia), e o banco compartilhado como contrário da [propriedade do dado](../referencia/glossario.md#propriedade-do-dado)
- A hierarquia que vai do serviço de negócio ao serviço de tecnologia, a classificação do portfólio em vermelho, âmbar e verde e os três tipos de aplicação
- Os seis atributos de interface e os seis campos que completam um [contrato de integração](../referencia/glossario.md#contrato-de-integracao)
- A distinção entre padrão técnico, protocolo, especificação de interface e contrato de integração, com padrão técnico como tradução de *standard*
- O [modelo C4](../referencia/glossario.md#modelo-c4) como notação de modelagem da aula, com o diagrama de contexto, o diagrama de contêineres, a coerência dos sistemas externos entre os dois níveis e a escolha do nível pela audiência
- As camadas de execução, a topologia com regiões e zonas de disponibilidade e o diagrama de implantação, que liga cada instância de contêiner ao nó de implantação em que executa

## Cadeia dos domínios

A aula detalha uma única solução por domínios, e cada exercício consome o produto do anterior.

1. O domínio de negócio localiza a mudança nas capacidades, nas etapas do fluxo de valor e nas atividades do processo, no exercício 13.
2. O domínio de dados atribui a cada entidade que sustenta as capacidades afetadas um dono e um regime de consistência por consumidor, no exercício 14.
3. O domínio de aplicações classifica o portfólio, especifica o contrato da integração de notas a partir do dono da entidade nota e corrige a fronteira da solução no diagrama de contexto, no exercício 15.
4. O domínio de infraestrutura recebe o diagrama de contêineres fornecido, coerente com o contexto corrigido, rotula cada relação com modo, volume e latência, liga as relações aos requisitos R6 e R7 e posiciona o núcleo transacional, no exercício 16.

As relações rotuladas no exercício 16 são a lista de exigências que a definição tecnológica da Aula 5 recebe, e cada uma delas pode ser rastreada até uma capacidade marcada no exercício 13.

## Autoavaliação

As perguntas abaixo são para o aluno responder a si mesmo, sem gabarito público, como verificação de retenção antes da Aula 5.

1. Dado um problema de negócio, eu aplico as quatro perguntas de aplicabilidade e indico se a arquitetura de solução é o método adequado.
2. Para uma entidade de dado qualquer, eu indico a fonte de verdade, o dono e o regime de consistência de cada consumidor com prazo declarado.
3. Eu separo, num exemplo de integração, o que é padrão técnico, o que é protocolo, o que é especificação e o que é garantia do contrato.
4. Eu identifico num diagrama de contexto um elemento que pertence ao nível de contêineres e explico a correção.
5. Eu rotulo uma relação entre contêineres com modo de comunicação, volume e latência a partir de dados operacionais.

## Fontes da aula

As referências seguem o formato APA, 7ª edição. A lista completa está na [bibliografia](../referencia/bibliografia.md) do curso.

- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seções 2.3 a 2.8, domínios de negócio, dados, aplicações, infraestrutura e software, seção 3.6.4, análise de interfaces, seção 4.3.1, padrões técnicos, e seção 7.5, solução como grafo)
- Kleppmann, M. (2017). *Designing data-intensive applications: The big ideas behind reliable, scalable, and maintainable systems*. O'Reilly Media. (sistemas de registro e dado derivado)
- Dehghani, Z. (2022). *Data mesh: Delivering data-driven value at scale*. O'Reilly Media. (propriedade do dado pelo domínio)
- Fielding, R., Nottingham, M., & Reschke, J. (Eds.). (2022). *HTTP semantics* (RFC 9110). RFC Editor. https://www.rfc-editor.org/rfc/rfc9110 (semântica do HTTP)
- OpenAPI Initiative. (2026). *OpenAPI specification* (Versão 3.2.1). https://spec.openapis.org/oas/latest.html (descrição de interface HTTP)
- AsyncAPI Initiative. (n.d.). *AsyncAPI specification* (Versão 3.1.0). https://www.asyncapi.com/docs/reference/specification/latest (descrição de interface orientada a mensagens)
- *Sistema Nota Fiscal Eletrônica: Manual de orientação do contribuinte, visão geral* (Versão 7.00). (2020). https://www.confaz.fazenda.gov.br/legislacao/arquivo-manuais/moc7-visao-geral.pdf (exemplo de padrão técnico, protocolo e especificação)
- Brown, S. (n.d.). *The C4 model for visualising software architecture*. https://c4model.com (modelo C4)
- Mendes, M. (2026b). *Guias de projeto de arquitetura de software* [Material de curso, versão arquivada]. https://github.com/aulas-marco/projeto-arquitetura-software/tree/30f15cd (guias 3.1, 3.2 e 3.3)
