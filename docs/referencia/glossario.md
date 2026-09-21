# Glossário

Este glossário reúne os termos usados nas páginas de conceito do curso, com a definição adotada pela disciplina. Cada entrada corresponde a uma âncora, referenciada pela seção "Antes de começar" das páginas de bloco.

## Arquitetura de solução

Disciplina responsável pela produção e pela gestão do plano de uma solução completa, que atende a uma necessidade, um problema ou uma oportunidade de negócio e se integra ao negócio em alinhamento com a estratégia, minimizando impactos negativos. O plano descreve a estrutura e o comportamento da solução em alto nível, antes da escolha dos produtos que a realizam.

## Arquiteto de solução

Profissional que conduz a definição de uma solução inteira, investiga o problema, levanta as partes interessadas, compara alternativas e responde pela integridade do desenho até a entrega. Decide sobre os cinco tipos de componente da solução, não apenas sobre software.

## Arquitetura corporativa

Disciplina que emite diretrizes, princípios e modelos válidos para a organização inteira, organizados nos domínios de negócio, aplicações, dados, infraestrutura e segurança. Opera no nível de granularidade mais alto, acima de qualquer solução isolada.

## Componentes da solução

Os cinco tipos de elemento que compõem uma solução, usados como lista de verificação para que nenhum deles fique de fora do desenho: pessoas, estruturas organizacionais, processos, informação e tecnologia.

## Bloco de construção da solução

Unidade lógica do desenho, que representa uma capacidade necessária à solução antes de estar decidido qual produto ou serviço a realiza. Um bloco de granularidade grossa agrupa vários blocos de granularidade fina.

## Direcionador de mudança

Fator que leva a organização a buscar uma solução. É interno quando nasce da própria operação, como custo, risco ou limitação de capacidade, e externo quando vem de fora, como exigência regulatória, movimento de concorrente ou mudança de expectativa do usuário.

## Parte interessada

Pessoa, papel ou área com interesse legítimo no resultado da solução, seja porque decide sobre ela, porque a usa, porque a sustenta ou porque é afetada por ela.

## Ponto de vista

Conjunto de convenções que define como construir e ler um tipo de representação da arquitetura, escolhido em função das preocupações de uma parte interessada.

## Visão

Representação concreta da arquitetura construída segundo um ponto de vista, que responde às preocupações às quais aquele ponto de vista se dirige.

## Arquitetura de linha de base

Descrição da arquitetura como ela é hoje, com os componentes existentes, suas idades, seus responsáveis e suas integrações. É o ponto de partida da comparação com a arquitetura alvo.

## Arquitetura alvo

Descrição da arquitetura pretendida ao fim de um ciclo de evolução. A diferença entre ela e a arquitetura de linha de base é o objeto da análise de lacunas.

## Artefato de linha de base

Documento ou modelo já existente que descreve parte da situação atual e entra como insumo do processo de definição da arquitetura, em vez de ser produzido do zero.

## Fase do processo de definição da arquitetura

Etapa do ciclo de vida que organiza o trabalho do arquiteto de solução, com entrada, atividades e saída próprias. O curso adota o ciclo de oito fases, de iniciação a conclusão.

## Arquitetura de software

Conjunto das decisões estruturais fundamentais sobre um sistema, difíceis de reverter depois de tomadas, que determinam sua capacidade de satisfazer os atributos de qualidade exigidos.

## Arquiteto de software

Profissional responsável por tomar e documentar as decisões estruturais de um sistema, balanceando atributos de qualidade concorrentes, requisitos funcionais e restrições de negócio.

## Atributo de qualidade

Propriedade pela qual um sistema é avaliado, como desempenho, disponibilidade, segurança ou capacidade de manutenção.

## Requisito funcional

Expectativa sobre o que o sistema faz, descrita como uma função, um comportamento ou uma resposta a um estímulo específico.

## Requisito não funcional

Categoria tradicional e mais ampla de requisito, que em diversas taxonomias reúne tanto requisitos de atributo de qualidade quanto restrições. O curso não trata requisito não funcional como sinônimo de atributo de qualidade. Atributo de qualidade é a propriedade avaliada, requisito não funcional é a categoria que agrupa essa e outras expectativas não funcionais, incluindo restrições.

## Requisito de atributo de qualidade

Expectativa concreta e mensurável sobre um atributo de qualidade, expressa em termos de estímulo, resposta e medida da resposta.

## Restrição

Decisão ou condição imposta ao sistema a partir de fora do processo de projeto, que limita as alternativas disponíveis ao arquiteto sem ser negociável por ele.

## Requisito arquiteturalmente significativo

Requisito cuja satisfação influencia materialmente a arquitetura do sistema, podendo ser de qualidade, funcional ou restritivo.

## Direcionador arquitetural

Fator, de negócio ou técnico, que orienta as decisões de arquitetura antes de se traduzir em requisitos específicos.

## Cenário de atributo de qualidade

Descrição estruturada de um requisito de qualidade em seis elementos, fonte do estímulo, estímulo, artefato afetado, ambiente, resposta e medida da resposta.

## Estilo arquitetural

Padrão de organização estrutural de um sistema, que define tipos de componentes, formas de conexão entre eles e restrições sobre essa organização.

## Plataforma arquitetural

Conjunto estruturado e consistente de ferramentas, frameworks, bibliotecas e práticas de desenho, organizadas para implementar um ou mais estilos arquiteturais, cobrindo desenvolvimento, integração, implantação e manutenção. Adotada como decisão arquitetural própria, posterior à decisão de estilo.

## ADR

Registro de decisão de arquitetura, do inglês Architecture Decision Record, documento curto que descreve uma decisão arquitetural, o contexto que a motivou e suas consequências.

## Racional arquitetural

Base intelectual que justifica as decisões de desenho de um sistema, conectando cada escolha às metas estratégicas, aos requisitos técnicos e às restrições de negócio. Registra não apenas a escolha feita, mas o raciocínio por trás dela, as alternativas consideradas, os critérios de seleção e os impactos esperados.

## Dependência de fornecedor

Dificuldade de trocar ou negociar uma dependência técnica ou organizacional adotada pelo sistema. Precisa ficar explícita no registro de decisão em seis dimensões, API proprietária, formato de dados, identidade, observabilidade, custo de saída de dados e habilidades da equipe.

## Modelo C4

Notação para representar a arquitetura de um sistema em quatro níveis de abstração progressiva, Contexto, Contêineres, Componentes e Código, cada nível com nome próprio, o modelo inteiro chamado C4 por ter quatro níveis.
