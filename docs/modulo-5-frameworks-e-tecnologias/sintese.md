# Síntese da Aula 5

Depois de cinco exercícios encadeados, o aluno tem a definição tecnológica da ACME montada passo a passo, e esta página fecha o módulo de frameworks e tecnologias com o que precisa permanecer depois da aula, a cadeia dos exercícios 16 a 20, uma autoavaliação e a lista das referências citadas nos quatro blocos.

## Checklist do que precisa permanecer

- A [definição tecnológica da solução](../referencia/glossario.md#definicao-tecnologica-da-solucao) como etapa que responde a três perguntas, que infraestrutura a solução exige, o que muda na infraestrutura atual e quanto custam essas mudanças, e os sete tipos de restrição tecnológica que reduzem as alternativas antes da comparação
- A cadeia que liga o [bloco de construção da solução](../referencia/glossario.md#bloco-de-construcao-da-solucao) ao requisito de serviço de infraestrutura, ao serviço do catálogo e ao componente, com a [lacuna de provisão](../referencia/glossario.md#lacuna-de-provisao) como saída quando o catálogo não traz o serviço
- O [modelo técnico de referência](../referencia/glossario.md#modelo-tecnico-de-referencia) em cinco colunas, a diferença entre ele e o blueprint lógico e a classificação das tecnologias em verde, âmbar e vermelho, com ADR para toda adoção fora dos exemplos aprovados
- Os seis critérios de seleção, aderência ao requisito, maturidade, suporte, custo total de propriedade, competência da equipe e portabilidade, organizados na matriz de avaliação, com a restrição que elimina alternativa declarada antes da comparação
- A [plataforma arquitetural](../referencia/glossario.md#plataforma-arquitetural) como concretização de um estilo, escolhida depois dele, com as quatro características e a composição em frameworks base, ferramentas de integração, ferramentas de monitoramento e bibliotecas
- A [zona de pouso](../referencia/glossario.md#zona-de-pouso) com os cinco pilares, a [infraestrutura como código](../referencia/glossario.md#infraestrutura-como-codigo) e as quatro etiquetas obrigatórias, projeto, ambiente, time e centro de custo
- A [dependência de fornecedor](../referencia/glossario.md#dependencia-de-fornecedor) em suas seis dimensões e o par de registros formado pelo ADR de estilo e pelo ADR de plataforma, com referência cruzada
- A classificação dos ativos de dado por confidencialidade, integridade e disponibilidade e pela LGPD, com a distinção entre [dado pessoal sensível](../referencia/glossario.md#dado-pessoal-sensivel) e dado pessoal
- A [grade de permissões](../referencia/glossario.md#grade-de-permissoes) preenchida pelo [menor privilégio](../referencia/glossario.md#menor-privilegio), com o tipo de acesso, a condição e o nível de segurança de cada recurso
- A [fronteira de confiança](../referencia/glossario.md#fronteira-de-confianca), as seis categorias do [STRIDE](../referencia/glossario.md#stride) com a propriedade que cada uma viola e o controle típico, e o [registro de decisões de segurança](../referencia/glossario.md#registro-de-decisoes-de-seguranca), com decisão, motivo, quem executa e como se verifica, revisado pela segurança contra as diretivas e o OWASP Top 10
- Os quatro tipos de lacuna de provisão, nova, substituição, modificação e remoção, a estimativa de tamanho, custo, recurso e tempo de cada uma e a entrada das lacunas confirmadas no roteiro de entrega da Aula 6
- O estado do caderno ao fim da aula: a seção 8 preenchida, com o modelo técnico aplicado aos contêineres, a plataforma e a zona de pouso, as decisões de segurança dos dados e o ADR de plataforma, pronta para a análise de lacunas e o roteiro de entrega da Aula 6

## Cadeia da definição tecnológica

A aula converte o desenho lógico em tecnologia por uma cadeia de cinco produtos, e cada exercício consome o produto do anterior.

1. O diagrama de contêineres do [exercício 16](../modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md#exercicio-16), recebido da Aula 4, mostra as partes executáveis da solução nova, como o serviço de matrícula e o banco do serviço de notas, com as relações rotuladas por modo de comunicação, volume e latência, e os contêineres novos ainda com o rótulo tecnologia a definir.
2. O [exercício 17](bloco-1-definicao-tecnologica-e-trm.md#exercicio-17) associa os contêineres às categorias do modelo técnico de referência, classifica seis tecnologias da linha de base em verde, âmbar ou vermelho e preenche a parte da matriz de seleção do provedor de identidade que o dossiê permite.
3. O [exercício 18](bloco-2-plataforma-arquitetural.md#exercicio-18) escolhe a plataforma para o estilo do exercício 10 pelo quadro comparativo dos seis critérios e avalia a zona de pouso quanto aos pilares e às etiquetas obrigatórias.
4. O [exercício 19](bloco-3-seguranca-ponta-a-ponta.md#exercicio-19) classifica os ativos de dado pela LGPD, corrige a grade de permissões pelo menor privilégio, associa as ameaças da fronteira do aplicativo do aluno às categorias STRIDE e aos controles e consolida os achados em cinco decisões de segurança, com executor e verificação.
5. O [exercício 20](bloco-4-adr-de-plataforma.md#exercicio-20) registra a plataforma em ADR encadeado ao ADR de estilo, com as consequências que os achados de segurança trazem, e classifica as lacunas de provisão da definição tecnológica considerada.

As lacunas classificadas no exercício 20 são a entrada que a análise de lacunas e o roteiro de entrega da Aula 6 recebem, e cada uma delas pode ser rastreada até uma exigência registrada nos exercícios 16 a 19.

## Autoavaliação

As perguntas abaixo servem para o aluno conferir o que ficou antes da Aula 6. Ele as responde sozinho, porque elas não têm gabarito, ao contrário dos exercícios: a seção [Gabaritos](../gabaritos/index.md) mostra o caderno arquitetural da ACME preenchido a cada exercício.

1. Dado um bloco de construção, é possível indicar o requisito de serviço de infraestrutura, o serviço do catálogo e a categoria do modelo técnico de referência que o realizam, e o que se registra quando o catálogo não traz o serviço.
2. Dadas duas alternativas aprovadas para a mesma categoria, é possível montar a matriz dos seis critérios com o dado que sustenta cada célula e declarar a restrição que elimina uma das alternativas.
3. Dado um estilo arquitetural, é possível indicar duas plataformas que o concretizam, nomear as ferramentas de cada uma e apontar a dependência de fornecedor que a escolha cria.
4. Dada uma grade de permissões, é possível apontar as células que violam o menor privilégio, dada uma ameaça numa fronteira de confiança, é possível indicar a categoria STRIDE e o controle que a trata, e dado esse controle, é possível registrar quem o executa e como se verifica.
5. Dado um item da definição tecnológica e a situação dele no catálogo atual, é possível classificar a lacuna em nova, substituição, modificação ou remoção e justificar com o dado da situação.

## Fontes da aula

As referências seguem o formato APA, 7ª edição. A lista completa está na [bibliografia](../referencia/bibliografia.md) do curso.

- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seção 2.7.2, modelo técnico de referência, seções 7.1 a 7.4, definição tecnológica, restrições e mapeamento dos blocos em serviços de infraestrutura, seção 7.5, infraestrutura de rede, seção 2.9, seção 4.6.7 e seção 7.7, segurança, seção 7.8, lacunas na provisão de serviços, e seção 7.9, validação da definição tecnológica)
- Mendes, M. (2026a). *Arquitetura de software* [Material de curso]. https://marco-mendes.github.io/arquitetura-software/ (template de ADR de dez campos e seção de custo e lock-in, dependência de fornecedor)
- Mendes, M. (2026b). *Guias de projeto de arquitetura de software* [Material de curso, versão arquivada]. https://github.com/aulas-marco/projeto-arquitetura-software/tree/30f15cd (guia 2.2, plataforma arquitetural)
- Ford, N., & Richards, M. (2020). *Fundamentals of software architecture*. O'Reilly. (comparação por atributo de qualidade, aplicada a plataformas)
- Amazon Web Services. (n.d.-d). *What is AWS Control Tower?* AWS Control Tower User Guide. Acesso em 15 de outubro de 2026. https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html
- Amazon Web Services. (n.d.-e). *Landing Zone Accelerator on AWS: Solution overview*. Landing Zone Accelerator on AWS Implementation Guide. Acesso em 15 de outubro de 2026. https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/solution-overview.html
- Microsoft. (2025). *What is an Azure landing zone?* Cloud Adoption Framework, Microsoft Learn. Acesso em 15 de outubro de 2026. https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018. Lei Geral de Proteção de Dados Pessoais (LGPD)*. https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm (art. 5º, I e II, art. 7º e art. 33)
- Shostack, A. (2014). *Threat modeling: Designing for security*. Acesso em 15 de outubro de 2026. https://shostack.org/books/threat-modeling-book (categorias STRIDE)
- OWASP Foundation. (2021). *OWASP Top 10:2021*. Acesso em 15 de outubro de 2026. https://top10.owasp.org/2021 (A01:2021, A03:2021 e A09:2021)
- MITRE Corporation. (n.d.). *Common Weakness Enumeration (CWE)*. Acesso em 15 de outubro de 2026. https://cwe.mitre.org/ (definição do CWE)
- International Organization for Standardization/International Electrotechnical Commission. (2022). *Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (ISO/IEC 27001:2022). Acesso em 15 de outubro de 2026. https://webstore.iec.ch/publication/79694 (escopo da norma)
- Nygard, M. (2011, 15 de novembro). *Documenting architecture decisions*. Cognitect Blog. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions (formato de cinco partes)
- MADR. (2024). *Markdown Architectural Decision Records* (Versão 4.0.0). https://adr.github.io/madr/ (campos do formato MADR)
