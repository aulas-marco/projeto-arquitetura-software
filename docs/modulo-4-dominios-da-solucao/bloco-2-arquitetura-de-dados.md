# Arquitetura de dados da solução

Este bloco identifica os dados que sustentam a mudança localizada no bloco 1 e responde a quem pertence cada entidade, onde ela é registrada com autoridade e com que atraso cada cópia pode refleti-la.

## Antes de começar

- [Arquitetura de dados](../referencia/glossario.md#arquitetura-de-dados)
- [Propriedade do dado](../referencia/glossario.md#propriedade-do-dado)
- [Fonte de verdade](../referencia/glossario.md#fonte-de-verdade)
- [Regime de consistência](../referencia/glossario.md#regime-de-consistencia)
- Capacidades afetadas, produzidas no [exercício 13](bloco-1-arquitetura-de-negocio.md#exercicio-13)

## Dados na solução

A **arquitetura de dados** é um subdomínio da arquitetura corporativa que trata dos dados, dos metadados e da informação usados na organização, e tem no modelo corporativo de dados seu artefato de visão geral (Lovatt, 2021, seção 2.5). Toda solução tem uma arquitetura de dados própria, e Lovatt exige que ela seja consistente com a arquitetura de dados da organização em que a solução vai operar, porque a inconsistência na definição ou no uso do dado produz erro em serviço de negócio ou faz a organização perder uma oportunidade.

O caso da produtora de vídeo, apresentado por Lovatt, mostra essa inconsistência. A produtora mantém o cadastro dos autores do conteúdo, funcionários ou contratados externos, e a área comercial mantém o cadastro de clientes. Alguns contratados externos também são clientes, mas as definições de cliente e de autor são diferentes e incompatíveis, de modo que a mudança de endereço informada por essa pessoa é registrada como cliente ou como autor, nunca nos dois, e a produtora passa a contatá-la com dados errados. A regra que Lovatt extrai do caso é que toda solução nova recebe como entrada os componentes relevantes da arquitetura de dados corporativa, e todo dado novo que ela cria é integrado a essa arquitetura o quanto antes, mesmo em caráter provisório.

### Dado, informação e metadado

Lovatt adota as definições da norma ISO/IEC 2382 de vocabulário de tecnologia da informação. Dado é a representação reinterpretável de informação, em forma adequada à comunicação, à interpretação ou ao processamento. Informação é o conhecimento sobre objetos, fatos, eventos, processos ou ideias que tem significado dentro de um contexto. Metadado é a categoria intermediária, o dado sobre o dado, que reúne descrições, regras, restrições e ligações entre itens de dado. O livro trata dado, informação e metadado numa única arquitetura de dados, sem negar a diferença entre eles, porque os três estão ligados de forma estreita na prática.

### Objetivos, atividades e artefatos

Os objetivos da arquitetura de dados que se sobrepõem aos da arquitetura de solução são atender às necessidades de dado e de informação do negócio, promover o entendimento do dado na organização, garantir consistência de uso e eliminar a duplicação de definições, cumprir a legislação e a regulação aplicáveis e governar o desenvolvimento de soluções novas (Lovatt, 2021, seção 2.5.1).

Os artefatos que entram na arquitetura de solução como insumo são os modelos e esquemas de dados, inclusive de mensagens e fluxos, as definições de dado, os dicionários e catálogos, e os projetos de bases de dados (Lovatt, 2021, seção 2.5.3). Entre eles, Lovatt destaca a grade, uma tabela que cruza entidades de dado com outros componentes, como funções de negócio ou aplicações, e que torna visível, durante a análise de impacto, quais componentes são atingidos por uma mudança em uma entidade.

### Entidade, generalização e especialização

O dado é uma abstração do mundo real e guarda só os detalhes que interessam ao negócio, restritos ainda pela legislação de dados pessoais, que exige necessidade de negócio e consentimento para o tratamento. Lovatt (2021, seção 2.5.5) descreve três operações de abstração com o Hospital Vale do Pousio, que quer convidar pacientes a comparecer a consultas.

| Operação | Definição | Exemplo no Hospital Vale do Pousio |
| --- | --- | --- |
| Entidade | Modelar uma coisa do mundo real como entidade de dado | Paciente, convite, clínica, consulta e profissional de saúde |
| Generalização | Reunir entidades distintas numa entidade mais abstrata | Paciente e profissional de saúde generalizados em pessoa |
| Especialização | Modelar uma entidade mais específica quando há diferença real de estrutura ou comportamento | Profissional de saúde especializado em enfermeiro especialista e médico |

A generalização tem efeito prático na solução, porque ajuda a reconhecer que uma entidade já existe na arquitetura corporativa com outro nome e pode ser reaproveitada, em vez de ser definida de novo.

### Fonte de verdade e regime de consistência

Kleppmann (2017) distingue dois tipos de sistema que guardam dado. O sistema de registro guarda a versão autoritativa do dado, e é nele que o dado é escrito primeiro. O sistema de dado derivado guarda dado transformado ou processado a partir do sistema de registro, como um cache, um índice de busca ou uma base analítica, e pode ser reconstruído a partir da origem. Nesta disciplina, o termo **fonte de verdade** designa o lugar em que a entidade é registrada com autoridade, e toda outra ocorrência da entidade é cópia derivada.

Cada cópia derivada precisa de um **regime de consistência** declarado, que diz quando a cópia reflete a fonte de verdade. O regime é forte quando a cópia reflete a fonte imediatamente, e eventual quando reflete dentro de um prazo declarado, por exemplo cinco minutos ou um dia. Um regime eventual sem prazo declarado não pode ser verificado, e por isso não é aceito como decisão.

### Propriedade do dado

A **propriedade do dado** atribui cada entidade a um único responsável, que é a parte autorizada a gravá-la. As demais partes leem a entidade pela interface que o responsável oferece ou a recebem por evento publicado por ele. Dehghani (2022) aplica o mesmo princípio ao dado analítico, atribuindo a propriedade ao domínio de negócio mais próximo da origem do dado, como um dos quatro princípios da malha de dados, tema que esta disciplina apenas menciona.

O banco compartilhado entre aplicações contraria a propriedade do dado. Quando duas aplicações leem e gravam as mesmas tabelas, cada mudança de estrutura passa a exigir alteração coordenada em dois códigos-fonte, frequentemente mantidos por equipes distintas, e nenhuma das duas pode evoluir o modelo de dados sem a outra. O custo aparece no prazo de entrega de qualquer mudança que toque essas tabelas e na impossibilidade de extrair uma parte do sistema sem reescrever a outra.

<figure markdown="span">
![Grade genérica que cruza três entidades, cliente, pedido e fatura, com três aplicações, loja virtual, logística e faturamento. Cada célula indica se a aplicação grava, lê por interface ou recebe por evento. Uma coluna destacada indica o dono de cada entidade e outra coluna indica o regime de consistência de cada consumidor, forte ou eventual com prazo de cinco minutos.](../assets/images/modulo-4-grade-dado-aplicacao.svg){ .module-diagram }
</figure>

*Figura 1 — Grade dado × aplicação com dono, consumidores e regime de consistência. Fonte: material do curso, com base em Lovatt (2021, seção 2.5.3).*

## Uso pelo arquiteto

O arquiteto usa a grade dado × aplicação para localizar o impacto de mudar uma entidade e para revelar entidades sem dono declarado ou com mais de uma aplicação que as grava. A grade também prepara o bloco 3, porque o dono de cada entidade é a origem natural das interfaces que a expõem, e o regime de consistência de cada consumidor é a exigência que o contrato de integração precisa garantir.

## Exercício 14

Este exercício é realizado fora do horário de aula, como atividade de aplicação do conceito apresentado neste bloco ao caso da instituição fictícia ACME.

A ACME é uma universidade privada brasileira com 38.400 alunos ativos, cujo sistema acadêmico, em operação desde 2004, passa por modernização incremental. O exercício parte das capacidades marcadas como afetadas no [exercício 13](bloco-1-arquitetura-de-negocio.md#exercicio-13) e dos fatos abaixo, reproduzidos da [arquitetura de linha de base](../caso-acme/linha-de-base.md).

- O banco Oracle, com 740 tabelas, é compartilhado entre o núcleo COBOL e a camada Java, sem separação de esquema por responsabilidade.
- Existem 2.300 pontos no código Java que leem ou gravam tabelas do núcleo diretamente, contornando as transações do núcleo, e o inventário não registra a distribuição desses pontos por entidade.
- Toda troca com o ERP financeiro e com o ambiente virtual de aprendizagem ocorre por arquivo, em lote noturno.

| Lote | Horário | Sentido | Conteúdo |
| --- | --- | --- | --- |
| Exportação de lançamentos financeiros | 23h10 | ACME para ERP | Mensalidade, multa e desconto do dia |
| Extração para o data warehouse | 02h30 | Oracle para data warehouse | Cópia integral de 140 tabelas |
| Carga de turmas e matrículas | 04h00 | ACME para ambiente virtual | Turma, matrícula e vínculo docente |
| Exportação de notas consolidadas | 05h10 | ACME para ambiente virtual | Nota consolidada e situação por disciplina |
| Retorno de baixas de pagamento | 05h30 | ERP para ACME | Confirmação de pagamento e inadimplência |
| Retorno de notas e frequência de atividades | 06h15 | Ambiente virtual para ACME | Nota de atividade avaliativa e presença |

O artefato fornecido é a grade dado × aplicação da linha de base, montada pelo material do curso a partir desses fatos, sem a coluna de dono.

| Entidade | Núcleo transacional | Portais Java | ERP financeiro | Ambiente virtual | Data warehouse |
| --- | --- | --- | --- | --- | --- |
| Aluno | Grava | Lê e grava, por conector e por acesso direto ao banco | Não registrado | Não registrado | Recebe por lote às 02h30 |
| Matrícula | Grava | Lê e grava, por conector e por acesso direto ao banco | Não registrado | Recebe por lote às 04h00 | Recebe por lote às 02h30 |
| Nota | Grava a nota consolidada | Lê e grava, por conector e por acesso direto ao banco | Não registrado | Recebe por lote às 05h10 e devolve nota de atividade às 06h15 | Recebe por lote às 02h30 |
| Lançamento financeiro | Grava | Lê, por conector e por acesso direto ao banco | Recebe por lote às 23h10 e devolve baixa às 05h30 | Não registrado | Recebe por lote às 02h30 |
| Turma | Grava | Lê, por conector e por acesso direto ao banco | Não registrado | Recebe por lote às 04h00 | Recebe por lote às 02h30 |

1. Marque, para cada uma das cinco entidades, a aplicação que deve ser a dona na arquitetura alvo, com uma linha de justificativa.
2. Marque, para cada consumidor de cada entidade, o regime de consistência exigido, forte ou eventual com o prazo, usando os requisitos R6 e R7 da [página inicial do caso](../caso-acme/index.md) quando se aplicarem.
3. Indique qual capacidade marcada como afetada no exercício 13 depende de cada entidade.
4. Responda, em até três linhas, por que os 2.300 acessos diretos ao banco contrariam a propriedade do dado.

O dono marcado para a entidade nota é a origem do contrato de integração do exercício 15, no [bloco 3](bloco-3-arquitetura-de-aplicacoes-e-integracao.md).

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seção 2.5, arquitetura de dados corporativa e de solução, definições de dado, informação e metadado, objetivos, atividades, artefatos e grade de análise de impacto, generalização e especialização. O Hospital Vale do Pousio é a versão em português do caso Fallowdale Hospital, usado ao longo do livro)
- Kleppmann, M. (2017). *Designing data-intensive applications: The big ideas behind reliable, scalable, and maintainable systems*. O'Reilly Media. (parte III, sistemas de registro e dado derivado)
- Dehghani, Z. (2022). *Data mesh: Delivering data-driven value at scale*. O'Reilly Media. (princípio da propriedade do dado pelo domínio)

**Material do curso.** O bloco usa as entradas [arquitetura de dados](../referencia/glossario.md#arquitetura-de-dados), [propriedade do dado](../referencia/glossario.md#propriedade-do-dado), [fonte de verdade](../referencia/glossario.md#fonte-de-verdade) e [regime de consistência](../referencia/glossario.md#regime-de-consistencia) do glossário, além do dossiê da instituição fictícia [ACME](../caso-acme/index.md) e da sua [arquitetura de linha de base](../caso-acme/linha-de-base.md).
