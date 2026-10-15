# Módulo 5, frameworks e tecnologias

**Data:** 15/10/2026

**Estado:** em revisão pelo professor

**Escopo:** produção dos blocos 1 e 3 da Aula 5, revisão dos blocos 2 e 4, índice, síntese e atualização das páginas de apoio

## 1. Objetivo

O módulo converte o desenho lógico da Aula 4 em tecnologia e verifica a segurança sobre a tecnologia escolhida. A progressão parte dos contêineres do exercício 16, rotulados com tecnologia a definir, passa pela escolha de serviço, de produto e de plataforma, avalia a segurança fim a fim e registra a decisão em ADR, com as lacunas de provisão que ela revela.

Ao final da aula, o aluno deverá conseguir:

- mapear um bloco de construção da solução em requisito de serviço de infraestrutura, em serviço e em categoria do modelo técnico de referência
- classificar tecnologias em verde, âmbar e vermelho e escolher entre alternativas aprovadas pelos seis critérios de seleção
- distinguir plataforma arquitetural de framework e relacionar a plataforma ao estilo escolhido na Aula 3
- descrever os pilares de uma zona de pouso em nuvem e as etiquetas obrigatórias
- classificar ativos de dado pela LGPD, corrigir uma grade de permissões e associar ameaças às categorias STRIDE
- classificar lacunas de provisão de serviço em nova, substituição, modificação ou remoção

## 2. Decisões de escopo

Decisões tomadas pelo professor em 15/10/2026:

- Os blocos 2 e 4, já publicados, são revisados e completados. Os blocos 1 e 3 são escritos do zero.
- O conteúdo de zona de pouso é dividido entre os blocos 2 e 3. O bloco 2 trata a zona de pouso como fundação da plataforma, e o bloco 3 trata ambientes separados, sub-rede privada e identidade centralizada como controles de segurança, com link ao bloco 2.
- O bloco 3 combina Lovatt (2021), a LGPD e a modelagem de ameaças STRIDE.
- Os seis critérios de seleção do bloco 1 substituem os sete fatores de adaptação ao contexto do bloco 2 atual.
- O material do EAD de Projeto de Arquitetura de Solução é de autoria do professor e serve de referência para esta aula. Os roteiros não são publicados, e as Fontes das páginas citam as fontes primárias que eles usam.

Não fazem parte deste módulo:

- IA no processo de arquitetura, roteiro de evolução e governança, que pertencem à Aula 6 ou ficam fora da disciplina síncrona
- configuração detalhada de zona de pouso por provedor
- topologia de regiões e zonas de disponibilidade e camadas de execução, já tratadas no [bloco 4 da Aula 4](../../modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md), referenciadas por link
- modelagem de ameaças completa de uma solução, limitada aqui a uma fronteira de confiança
- escrita de política de segurança

## 3. Base bibliográfica

O livro-texto Lovatt (2021) é a base de cada bloco, e o texto integral consultado está em `/Volumes/Marco-Dev/dev/projeto-arquitetura-solucao/docs/superpowers/plans/livro-lovatt.md`. As seções 2.9 e 4.6.7 não foram citadas nos módulos anteriores, e a seção 2.7.2 foi apenas listada na Aula 4, sem desenvolvimento do modelo técnico de referência.

| Bloco | Seções de Lovatt | Fonte complementar |
| --- | --- | --- |
| 1, definição tecnológica e TRM | 2.7.2, 7.1 a 7.4 | Orientações da disciplina sobre TRM, para a estrutura de cinco colunas e a nota de uso |
| 2, plataforma | 7.5, mais o texto atual | Documentação de zona de pouso da AWS e da Azure, Mendes (2026b) |
| 3, segurança fim a fim | 2.9, 4.6.7, 7.7 | Lei 13.709/2018, Shostack (2014), ISO/IEC 27001, OWASP Top 10 2021, CWE |
| 4, ADR e lacunas | 7.8, 7.9, mais o texto atual | Nenhuma |

Toda fonte complementar é conferida na origem antes de entrar no texto e na bibliografia. A fonte que não puder ser conferida sai do texto, e o conceito correspondente passa a ser apresentado como convenção do curso. Isso vale em especial para os artigos da LGPD, para a descrição do STRIDE e para os nomes das estruturas oficiais de zona de pouso.

Termos e nomes de casos de fontes em inglês são vertidos ao português, e as organizações fictícias seguem o padrão ACME com qualificador de setor. O exemplo conceitual dos blocos 1 e 3 é o Hospital ACME, adaptado do caso do livro-texto, com a origem declarada apenas em Fontes.

| Original | Termo adotado |
| --- | --- |
| technical reference model (TRM) | modelo técnico de referência |
| solution technology definition | definição tecnológica da solução |
| infrastructure service gap | lacuna de provisão de serviço |
| landing zone | zona de pouso |
| infrastructure as code | infraestrutura como código |
| least privilege | menor privilégio |
| trust boundary | fronteira de confiança |
| security design authority | autoridade de design de segurança |
| vendor lock-in | dependência de fornecedor |

## 4. Progressão pedagógica

Cada bloco consome o produto do anterior e produz uma entrada para o seguinte.

| Bloco | Pergunta orientadora | Entrada | Produto do exercício |
| --- | --- | --- | --- |
| 1. Definição tecnológica e TRM | Que serviço e que tecnologia aprovada realizam cada contêiner? | Contêineres do exercício 16 | Contêineres associados a categoria e padrão, tecnologias classificadas e matriz de seleção preenchida (ex. 17) |
| 2. Plataforma | Sobre que plataforma e que fundação a solução executa? | ADR de estilo (ex. 12) e matriz do ex. 17 | Plataformas candidatas, quadro comparativo e pilares da zona de pouso (ex. 18) |
| 3. Segurança fim a fim | A tecnologia escolhida protege o que precisa proteger? | Contêineres do ex. 16 e zona de pouso do ex. 18 | Ativos classificados, grade de permissões corrigida e ameaças associadas a STRIDE (ex. 19) |
| 4. ADR e lacunas | O que fica registrado e o que falta prover? | Produtos dos ex. 17 a 19 | ADR de plataforma e lacunas classificadas (ex. 20) |

A Aula 5 não tem bloco 0. A grade de tempo mantém os quatro blocos de 32 ou 33 minutos, os três questionários Kahoot e as questões sobre a Aula 4 no início.

## 5. Regra dos exercícios

Os exercícios seguem a regra da Aula 4, segundo a qual o enunciado fornece o artefato já montado e o aluno classifica, marca, rotula, corrige ou responde perguntas curtas sobre ele. Nenhum exercício pede a construção, a partir do zero, de matriz, de grade de permissões, de modelo de ameaças ou de política de segurança.

- Cada exercício é dividido em itens com subtítulo `### Item N: assunto`, e cada item traz o próprio artefato seguido das suas perguntas.
- Cada exercício traz ao menos um visual em Mermaid no enunciado, porque os SVG dos módulos 3 e 4 não podem conter dado da ACME.
- O artefato fornecido não traz a resposta.
- O enunciado não repete a frase sobre realização fora do horário de aula, que fica nos índices das aulas.

## 6. Bloco 1, definição tecnológica e modelo técnico de referência (novo)

### 6.1 Resultado de aprendizagem

O aluno converte um bloco de construção em requisito de serviço de infraestrutura, identifica a categoria do modelo técnico de referência que o atende e escolhe entre alternativas aprovadas pelos seis critérios de seleção.

### 6.2 Conteúdo

- As três perguntas da definição tecnológica, quanto à infraestrutura necessária, às áreas que mudam e ao custo da mudança, e os sete tipos de restrição tecnológica, que reduzem as opções antes da comparação (Lovatt, 2021, seções 7.1 a 7.3).
- O mapeamento do bloco de construção em requisito de serviço com nível declarado, depois em serviço e em componente de infraestrutura. O requisito sem serviço correspondente gera lacuna, tratada no bloco 4 (seção 7.4, figura 7.1 redesenhada em SVG próprio).
- O modelo técnico de referência e sua diferença em relação ao blueprint lógico, que responde como a solução se organiza, enquanto o modelo técnico responde quais tecnologias são aprovadas.
- A estrutura em cinco colunas, camada, categoria, padrão ou protocolo, exemplos aprovados e exemplos não aprovados, as seções de princípios e de tecnologias descontinuadas, e a classificação em verde, âmbar e vermelho. A adoção fora da lista aprovada exige ADR com a justificativa do desvio.
- Os seis critérios de seleção, aderência ao requisito, maturidade, suporte, custo total de propriedade, competência da equipe e portabilidade, e a matriz de avaliação em que cada célula cita um dado verificável. Uma restrição pode eliminar alternativas antes da comparação, e o registro declara essa eliminação.
- Correspondência com os sete fatores usados antes na disciplina, em uma frase: requisitos funcionais, não funcionais e arquiteturais formam a aderência, o conhecimento do time é a competência, os custos formam o custo total e a confiabilidade do fornecedor é o suporte. A facilidade de uso sai da lista, e a portabilidade entra.
- Ligação com a [Aula 3](../../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md): a matriz preenchida alimenta o campo de alternativas do ADR.

O exemplo conceitual é o serviço de identidade do Hospital ACME, com requisito de logon único e operação contínua. O exemplo de portabilidade eliminando alternativas é a ferramenta de infraestrutura como código entre dois provedores de nuvem.

### 6.3 Exercício 17

- **Item 1, contêineres e categorias:** o enunciado traz um recorte do modelo técnico de referência da ACME com seis linhas, identidade, exposição de serviços, mensageria, infraestrutura como código, observabilidade e banco de serviço novo, e a lista dos contêineres do exercício 16. O aluno associa cada contêiner a uma categoria e ao padrão correspondente.
- **Item 2, tecnologias da linha de base:** o enunciado traz seis tecnologias, JSF 1.2 e EJB 2.0, Oracle 12c, acesso direto ao banco, COBOL sob CICS, diretório corporativo e arquivo posicional sem versão, com o dado de [linha de base](../../caso-acme/linha-de-base.md) de cada uma. O aluno classifica cada tecnologia em verde, âmbar ou vermelho e justifica em uma linha.
- **Item 3, matriz de seleção:** o enunciado traz a matriz do provedor de identidade com três alternativas e seis critérios, com a maior parte das células em branco. O aluno preenche três células com o dado do caso e indica a alternativa que a restrição de padrão aberto elimina.

## 7. Bloco 2, plataforma arquitetural (revisão)

### 7.1 Resultado de aprendizagem

O aluno relaciona a plataforma ao estilo arquitetural escolhido, compara plataformas candidatas pelos seis critérios e descreve a zona de pouso que recebe a solução.

### 7.2 Alterações sobre o texto publicado

- Mantêm-se a definição, as quatro características e a regra de que a decisão de estilo precede a de plataforma.
- Os nove exemplos de plataforma são reduzidos a três ou quatro, cada um ligado por link ao estilo da Aula 3 que concretiza. Os demais saem do texto.
- O quadro comparativo passa a usar os seis critérios do bloco 1, por link, e deixa de ter fatores próprios.
- Entra a seção de zona de pouso, com a função, os cinco pilares comuns às estruturas oficiais dos provedores, a infraestrutura como código e as etiquetas obrigatórias de projeto, ambiente, time e centro de custo. Ambientes separados e rede segmentada aparecem como pilares, e seu tratamento de segurança fica no bloco 3.
- Entra a observabilidade como camada transversal, com os três sinais e o OpenTelemetry como padrão de coleta.
- Região, zonas de disponibilidade e camadas de execução entram apenas por link ao bloco 4 da Aula 4.
- O bloco continua afirmando que a plataforma é a maior decisão tecnológica e deve ser registrada em ADR próprio, escrito no bloco 4.

### 7.3 Exercício 18

Mantêm-se os itens 1 e 2, com o quadro comparativo reescrito nos seis critérios. O item 3 é novo. O enunciado traz a zona de pouso da ACME em dois provedores de nuvem, com contas por ambiente, rede, identidade e uma lista de recursos com suas etiquetas. O aluno marca qual pilar cada elemento realiza e indica qual etiqueta obrigatória falta em cada recurso.

## 8. Bloco 3, segurança fim a fim (novo)

### 8.1 Resultado de aprendizagem

O aluno classifica ativos de dado pela LGPD, identifica erros numa grade de permissões pelo princípio do menor privilégio e associa ameaças às categorias STRIDE e a controles.

### 8.2 Conteúdo

- Segurança da informação e cibersegurança, e a distinção entre arquitetura de segurança, voltada à mudança, e operações de segurança, voltadas ao dia a dia. Os quatro objetivos da arquitetura de segurança (Lovatt, 2021, seção 2.9).
- As quatro formas de especificar segurança numa solução, requisito funcional, requisito não funcional, diretiva corporativa e padrão técnico, com link ao [bloco 2 da Aula 2](../../modulo-2-requisitos-e-partes-interessadas/bloco-2-qualidade-e-tipos-de-requisito.md) e ao padrão técnico definido no [bloco 3 da Aula 4](../../modulo-4-dominios-da-solucao/bloco-3-arquitetura-de-aplicacoes-e-integracao.md) (seção 7.7).
- Ativo e classificação por confidencialidade, integridade e disponibilidade. Complemento brasileiro: dado pessoal, dado pessoal sensível, base legal e transferência internacional pela LGPD, com artigos conferidos no texto oficial.
- Grade de permissões que cruza entidade e recurso, com tipo de acesso, condição e nível de segurança, sob o princípio do menor privilégio (seção 4.6.7).
- Controles da zona de pouso tratados como segurança: ambientes separados como fronteira de permissão, de conformidade e de efeito, sub-rede privada para serviços de retaguarda e bancos de dados, e identidade centralizada por padrão aberto. Cada um liga ao bloco 2.
- Modelagem de ameaças com STRIDE: fronteira de confiança, as seis categorias e o controle típico de cada uma, aplicados a uma única fronteira.
- Autoridade de design de segurança e seus dois testes, conformidade com as diretivas, com a ISO/IEC 27001 como exemplo, e teste de vulnerabilidade com OWASP Top 10 e CWE. A matriz RACI da atividade é apresentada (seção 7.7).

O exemplo conceitual é o portal de preferências de contato do paciente do Hospital ACME, adaptado de Lovatt (2021, seção 7.7), com achados de conformidade e três vulnerabilidades: acesso além do necessário, injeção e registro insuficiente.

### 8.3 Exercício 19

- **Item 1, ativos:** o enunciado traz seis ativos de dado da ACME, nota, histórico escolar, CPF, dados socioeconômicos de bolsa, laudo de necessidade educacional específica e oferta de turmas. O aluno classifica cada ativo em não pessoal, pessoal ou pessoal sensível, atribui o nível de confidencialidade e responde em uma linha qual ativo a restrição de transferência internacional da encarregada de proteção de dados impede de sair do território nacional.
- **Item 2, grade de permissões:** o enunciado traz uma grade de perfis e serviços sobre os recursos de nota e de matrícula, com três erros de privilégio. O aluno aponta cada erro e o corrige pelo menor privilégio.
- **Item 3, STRIDE:** o enunciado traz a fronteira entre o aplicativo do aluno e o serviço de matrícula, retirada do diagrama do exercício 16, e seis ameaças descritas. O aluno classifica cada ameaça numa categoria STRIDE e escolhe o controle correspondente numa lista fornecida.

## 9. Bloco 4, ADR de plataforma e lacunas (revisão)

### 9.1 Resultado de aprendizagem

O aluno registra a decisão de plataforma em ADR encadeado ao ADR de estilo, avalia a dependência de fornecedor e classifica as lacunas de provisão de serviço.

### 9.2 Alterações sobre o texto publicado

- Mantêm-se os efeitos da decisão de plataforma nos campos de forças, alternativas e consequências, as seis dimensões de dependência de fornecedor e o par de registros.
- O campo de alternativas recebe a matriz dos seis critérios do bloco 1, com link, no lugar do quadro dos sete fatores.
- Entra a seção de lacunas na provisão de serviços, que compara a definição tecnológica com o catálogo de infraestrutura e classifica cada lacuna em nova, substituição, modificação ou remoção. Cada lacuna entra no custo e no roteiro de entrega, com remissão à Aula 6 (Lovatt, 2021, seção 7.8).
- Entra, em seção curta, a validação da definição tecnológica com as partes interessadas (seção 7.9).

### 9.3 Exercício 20

Mantêm-se os itens 1 a 3. O item 4 é novo. O enunciado traz seis requisitos de serviço da ACME, entre eles provedor de identidade, mensageria, banco de serviço novo, diretório corporativo e extração noturna. O aluno classifica cada requisito num dos quatro tipos de lacuna e indica qual deles tende a reduzir o custo recorrente.

## 10. Índice, síntese e páginas de apoio

- **Índice:** objetivos em verbos observáveis, grade de tempo no formato da Aula 4 com questões sobre a Aula 4, três Kahoots e quatro blocos de 32 ou 33 minutos, roteiro causal da aula, entrada recebida da Aula 4 e preparação para a Aula 6. O parágrafo que anuncia a publicação futura dos blocos 1 e 3 é removido.
- **Síntese:** checklist dos conceitos essenciais, cadeia dos exercícios 16 a 20 com o produto de cada um, autoavaliação sem gabarito público e fontes da aula.
- **Glossário:** entram modelo técnico de referência, definição tecnológica da solução, lacuna de provisão, zona de pouso, infraestrutura como código, grade de permissões, menor privilégio, fronteira de confiança, STRIDE, autoridade de design de segurança e dado pessoal sensível, sem duplicar entrada existente.
- **Bibliografia:** entram ISO/IEC 27001, OWASP Top 10 2021, CWE, Lei 13.709/2018, Shostack (2014) e a documentação de zona de pouso da AWS e da Azure, em APA, cada uma conferida na origem.
- **Cronograma, artefatos por aula e `mkdocs.yml`:** recebem a navegação dos blocos 1 e 3 e da síntese e os produtos dos exercícios 17 a 20.

## 11. Estratégia visual

Cada bloco tem ao menos um SVG conceitual com a classe `module-diagram`, sem dado da ACME e sem resolver exercício, conferido renderizado a 688 px de coluna.

| Bloco | Figuras |
| --- | --- |
| 1 | Mapeamento do bloco de construção ao componente, com a saída para lacuna, e o modelo técnico de referência em cinco colunas |
| 2 | Os cinco pilares da zona de pouso |
| 3 | Fronteira de confiança com as seis categorias STRIDE, e grade de permissões |
| 4 | Os quatro tipos de lacuna |

Figura de exercício que precise de SVG usa o prefixo `acme-`. Figura com conteúdo alterado recebe nome de arquivo novo.

## 12. Testes

O arquivo `tests/test_modulo_5_contract.py` segue o modelo de `tests/test_modulo_4_contract.py` e verifica:

- a existência das seis páginas do módulo, índice, quatro blocos e síntese
- a ausência de "ACME" nos SVG do módulo
- a ausência de "Lovatt" e "livro-texto" fora das Fontes
- o formato `### Item N:` em cada exercício e a numeração dos exercícios 17 a 20
- a presença de ao menos um visual em cada exercício

A suíte completa, o validador `scripts/validate_content.py --all` e `mkdocs build --strict` passam antes de cada commit.

## 13. Fora da conferência automática

Três pontos exigem conferência humana e não entram nos testes: a correção dos artigos da LGPD e da descrição do STRIDE contra a fonte, a legibilidade dos diagramas na tela e a ausência de resposta do exercício dentro do artefato fornecido.
