# Partes interessadas, pontos de vista e escopo

Este bloco trata de quem decide sobre a solução, como essas pessoas são identificadas e avaliadas, como suas preocupações são tratadas por pontos de vista e visões, e como o escopo da mudança é declarado.

## Antes de começar

- [Parte interessada](../referencia/glossario.md#parte-interessada)
- [Ponto de vista](../referencia/glossario.md#ponto-de-vista)
- [Visão](../referencia/glossario.md#visao)
- [Bloco de construção da solução](../referencia/glossario.md#bloco-de-construcao-da-solucao)

## Conceito

As partes interessadas são a ligação entre a solução e o negócio. Escolhidas corretamente, elas representam o negócio e decidem em seu nome, de modo que uma solução que as satisfaça é a solução que o negócio quer. A norma ISO/IEC/IEEE 42010 define parte interessada como o indivíduo, a equipe, a organização ou a classe desses que tem interesse em um sistema, definição já adotada no [bloco 3 da Aula 1](../modulo-1-fundamentos/bloco-3-papel-do-arquiteto-de-solucao.md#conceito).

<figure markdown="span">
![Infográfico sobre partes interessadas, pontos de vista e escopo. À esquerda, as partes são agrupadas entre quem patrocina e decide, usa e opera, constrói e mantém, e regula e audita. Ao centro, o interesse da parte gera uma preocupação, que orienta um ponto de vista e resulta em uma visão. À direita, o escopo pergunta o que está dentro, o que fica fora e quais interfaces atravessam a fronteira.](../assets/images/modulo-2-partes-interessadas-pontos-vista.png){ .module-diagram }
</figure>

O critério prático de inclusão é uma lista de quatro perguntas. É parte interessada quem precisa de informação sobre a solução, quem fornece conhecimento essencial do negócio ou do domínio, quem tem autoridade sobre orçamento, recursos ou outras decisões organizacionais, e quem participa do desenho, da implementação ou da implantação.

A comunicação com essas pessoas existe por quatro motivos distintos, e confundi-los gera atrito. **Informação** mantém todos cientes do andamento, em fluxo predominantemente de mão única. **Consulta** captura conhecimento de negócio, é de mão dupla e exige registro para rastrear insumo e decisão. **Prestação de contas** registra a aprovação de decisões arquiteturais por pessoas determinadas. **Responsabilidade** aloca e acompanha tarefas atribuídas a partes interessadas.

### Categorias de parte interessada

| Categoria | Quem é | Preocupação típica |
| --- | --- | --- |
| Donos do negócio e gestores seniores | Quem responde em última instância pelo resultado da organização | Metas estratégicas, posição financeira e resiliência a mudança externa |
| Patrocinador de negócio | Responsável único pela solução, que decide a passagem de cada fase | Sucesso da solução dentro do prazo e do orçamento aprovados |
| Usuários finais e atores de negócio | Quem opera o processo alterado pela solução | Viabilidade da rotina nova e continuidade do trabalho |
| Clientes e usuários dos serviços | Quem recebe o serviço afetado | Qualidade percebida do serviço |
| Arquitetura corporativa e subdomínios | Quem responde pelos domínios de negócio, dados, aplicações, infraestrutura e segurança | Aderência às diretrizes e reúso do que já existe |
| Participantes do desenho | Quem desenha partes da solução | Consistência entre as partes desenhadas |
| Participantes da implantação | Quem constrói, implanta e sustenta | Exequibilidade do desenho e condições de sustentação |
| Fornecedores de produto e serviço | Quem provê tecnologia ou serviço contratado | Escopo contratual e continuidade da receita |
| Reguladores e entidades setoriais | Quem impõe exigência externa | Conformidade demonstrável |

A responsabilidade pela seleção correta é dos donos do negócio e dos gestores seniores, a quem cabe também atribuir papéis como o de patrocinador a pessoas com autoridade e capacidade para exercê-los. A identificação pode ocorrer em qualquer fase, e a atividade principal está na descoberta. A troca de representante ao longo do percurso é comum e indesejável, porque interrompe a relação construída entre a equipe de arquitetura e o negócio.

### Preocupações, pontos de vista e visões

Toda preocupação identificada é registrada em um registro de preocupações e ligada a uma ou mais partes interessadas. A equipe de arquitetura mantém esse registro, e o patrocinador responde por assegurar que as preocupações sejam levantadas e tratadas. As preocupações são atendidas por decisões de desenho, e é por isso que elas reaparecem nas reuniões de decisão.

A técnica que organiza esse tratamento tem dois termos que não são sinônimos, apresentados na fase de validação do [bloco 4 da Aula 1](../modulo-1-fundamentos/bloco-4-processo-de-definicao-da-arquitetura.md#as-oito-fases) e detalhados a seguir. O **ponto de vista** define três coisas, o critério de seleção que filtra o que será extraído da descrição de arquitetura, a estrutura do artefato que organiza essa informação, e as instruções de apresentação que a tornam compreensível para aquela audiência. A **visão** é o resultado concreto de aplicar um ponto de vista à descrição de arquitetura.

A consequência prática aparece na validação do desenho. Aplicar o mesmo ponto de vista à [arquitetura de linha de base](../referencia/glossario.md#arquitetura-de-linha-de-base) e à [arquitetura alvo](../referencia/glossario.md#arquitetura-alvo) produz duas visões comparáveis, e a comparação mostra o efeito da mudança sob a perspectiva daquela parte interessada, sem obrigá-la a ler o modelo inteiro.

### Pontos de vista na prática

As três visões a seguir descrevem aspectos da mesma solução, mas não são intercambiáveis. Cada uma seleciona elementos, relações e informações adequados a uma preocupação e a uma audiência. O que constitui detalhe indispensável para uma equipe pode ser ruído para outra.

#### Visão de contexto C1 para o patrocinador

O patrocinador precisa decidir sobre escopo, valor e dependências organizacionais. Por isso, o ponto de vista seleciona os usuários, o Sistema Acadêmico como uma única caixa e os sistemas externos com que ele se relaciona. O nível C1 da modelagem C4 responde quem usa a solução, qual é sua fronteira e de que outros sistemas ela depende. Portais, banco de dados e tecnologias internas ficam de fora porque não ajudam essa audiência a tomar a decisão em pauta. A legenda temporal identifica a visão como representação da linha de base atual da ACME em 2026, e não como arquitetura alvo.

<figure markdown="span">
![Visão de contexto C1 da ACME destinada ao patrocinador. Aluno, professor e gestão acadêmica interagem com o Sistema Acadêmico, apresentado como uma única caixa. O sistema troca informações com o ambiente virtual de aprendizagem, o ERP financeiro, os serviços institucionais e o órgão regulador.](../assets/images/modulo-2-visao-contexto-patrocinador.svg){ .module-diagram }
<figcaption>Visão C1 para o patrocinador, linha de base atual da ACME em 2026: fronteira, usuários e dependências externas, sem detalhe interno.</figcaption>
</figure>

#### Visão de segurança C2 para a equipe de segurança

A equipe de segurança precisa localizar superfícies expostas, dados pessoais, integrações frágeis e pontos onde os controles devem operar. O nível C2 da modelagem C4 decompõe o Sistema Acadêmico em contêineres e preserva sua fronteira de responsabilidade. As relações em laranja destacam exposições da linha de base, enquanto as relações verdes mostram controles requeridos. A tecnologia dos portais é identificada como Java legado com JSF 1.2 e EJB 2.0 para documentar a situação atual, não para recomendá-la. A trilha de auditoria aparece como controle exigido pelo requisito R9, e não como componente já existente.

<figure markdown="span">
![Visão de contêineres C2 da ACME destinada à equipe de segurança. Dentro da fronteira do Sistema Acadêmico aparecem os portais web, o núcleo COBOL sobre CICS, a integração em lote, o banco Oracle e a trilha de auditoria requerida. Relações destacam autenticação, acesso direto ao banco, conectores proprietários, arquivos posicionais e registro de acesso a dados pessoais.](../assets/images/modulo-2-visao-seguranca-c2.svg){ .module-diagram }
<figcaption>Visão C2 de segurança, linha de base atual da ACME em 2026: contêineres, fronteiras de confiança, riscos existentes e controles requeridos.</figcaption>
</figure>

#### Visão de rastreabilidade para o gestor

O gestor precisa saber se cada preocupação chegou a uma decisão acompanhável. Para essa audiência, uma planilha é mais útil do que um diagrama estrutural. O ponto de vista seleciona a origem da necessidade, o requisito que a formaliza, o elemento arquitetural afetado, a evidência esperada e a situação da decisão. A planilha permite localizar lacunas, como um requisito sem elemento responsável ou uma decisão sem forma de verificação.

<figure markdown="span">
![Visão de rastreabilidade da ACME em formato de planilha para o gestor. As linhas relacionam código, preocupação, parte interessada, requisito, elemento da visão, evidência ou decisão e situação. Os exemplos incluem matrícula no pico, propagação de notas, identidade aberta, auditoria de dados pessoais e residência de dados.](../assets/images/modulo-2-visao-rastreabilidade-gestor.svg){ .module-diagram }
<figcaption>Visão de rastreabilidade: da preocupação da parte interessada até a evidência que permite acompanhar a decisão.</figcaption>
</figure>

O contraste mostra que ponto de vista não é apenas nível de zoom. O patrocinador recebe um mapa de contexto, a equipe de segurança recebe uma decomposição orientada a controles, e o gestor recebe uma matriz de cobertura. As três visões podem derivar da mesma descrição de arquitetura sem apresentar a mesma informação.

### Definição do escopo

O escopo da solução é declarado em termos de componentes, e não de intenção. Entram na declaração os componentes de negócio, os de informação e tecnologia, e os blocos de construção, com a distinção entre bloco de construção de arquitetura, que é genérico e reutilizável, e bloco de construção da solução, que é a realização daquele bloco naquela solução. A declaração é documentada e aprovada formalmente, porque é ela que delimita o que será mudado e, por exclusão, o que permanece.

Na ACME, universidade privada brasileira fictícia com 38.400 alunos ativos e sistema acadêmico em operação desde 2004, a declaração de escopo precisa registrar que o ambiente virtual de aprendizagem e o ERP financeiro permanecem, por decisão da Reitoria de 12/03/2026, e que o trabalho sobre eles é de integração e de governança.

## Uso pelo arquiteto

O arquiteto usa a lista de quatro perguntas como verificação contra a omissão mais cara do processo, a parte interessada descoberta tarde. Quem tem autoridade sobre orçamento e quem responde por exigência regulatória costumam ser lembrados, e quem sustenta o sistema depois da implantação costuma ser esquecido até o momento em que a operação recusa o desenho.

Os pontos de vista servem para não travar a discussão em um modelo único. Apresentar o mesmo desenho a um diretor financeiro e a um gerente de sustentação produz duas conversas improdutivas, porque cada um precisa de um recorte diferente da mesma descrição de arquitetura.

## Exercício 8

A ACME é uma universidade privada brasileira fictícia, com 38.400 alunos ativos, 2.150 professores, 1.480 técnico-administrativos e 4 campi, cujo sistema acadêmico está em operação desde 2004 e é mantido por uma fábrica de software contratada, sob contrato de sustentação vigente até 30/09/2027. A declaração de escopo marcada no Item 4 é o ponto de partida do [exercício 13](../modulo-4-dominios-da-solucao/bloco-1-arquitetura-de-negocio.md#exercicio-13) da Aula 4.

### Item 1: Categoria de cada papel

O diagrama abaixo mostra os oito papéis do mapa de atores do caso, com a área a que cada um pertence, e o quadro seguinte reproduz o que cada papel quer e o que teme.

```mermaid
flowchart LR
    SA["Sistema acadêmico da ACME"]
    R["Reitora<br/>Reitoria"] --- SA
    PG["Pró-Reitora de Graduação<br/>Graduação"] --- SA
    TI["Diretor de TI<br/>Tecnologia da Informação"] --- SA
    FIN["Diretor Financeiro<br/>Administração e Finanças"] --- SA
    SA --- GS["Gerente de sustentação<br/>Fábrica de software contratada"]
    SA --- EAD["Coordenadora de Educação a Distância<br/>Educação a Distância"]
    SA --- DPO["Encarregada de proteção de dados<br/>Jurídico"]
    SA --- DCE["Representação discente<br/>Diretório Central dos Estudantes"]
```

| Papel | O que quer | O que teme |
| --- | --- | --- |
| Reitora | Resultado visível em 12 meses e aplicativo móvel do aluno em operação antes do vestibular de 2027 | Investimento de R$ 6,2 milhões sem efeito perceptível e queda de nota na avaliação regulatória |
| Pró-Reitora de Graduação | Matrícula sem falha e notas publicadas dentro do calendário | Repetição de incidente na janela de matrícula e nova prorrogação |
| Diretor de TI | Reduzir a dependência de especialistas em COBOL e o custo anual de manutenção | Perder os profissionais de COBOL e ficar sem quem sustente o núcleo |
| Diretor Financeiro | Preservar os contratos vigentes até o fim do prazo, já provisionados no plano plurianual | Desembolso duplicado, com legado e nuvem cobrados no mesmo exercício |
| Gerente de sustentação da fábrica | Manter o escopo e a previsibilidade do contrato até 30/09/2027 | Perder receita e escopo com a internalização do conhecimento do núcleo |
| Coordenadora de Educação a Distância | Notas e turmas propagadas ao ambiente virtual de aprendizagem em minutos | Continuar dependente do lote diário, com reclamação de aluno a cada fechamento |
| Encarregada de proteção de dados | Conformidade com a LGPD, base legal declarada e trilha de auditoria sobre dado pessoal | Transferência de dado de aluno para fora do território nacional sem amparo |
| Representação discente | Aplicativo móvel e matrícula que não falhe na abertura | Perda de vaga em disciplina por indisponibilidade do portal |

1. Classifique os oito papéis nas categorias de parte interessada apresentadas na seção [Categorias de parte interessada](#categorias-de-parte-interessada) deste bloco.
2. Indique qual dos oito papéis exerce o papel de patrocinador de negócio, com justificativa.

### Item 2: Categorias sem representante

O quadro abaixo lista as nove categorias de parte interessada, com uma coluna em branco para o papel do mapa de atores que representa cada uma.

| Categoria | Papel do mapa de atores que a representa |
| --- | --- |
| Donos do negócio e gestores seniores | |
| Patrocinador de negócio | |
| Usuários finais e atores de negócio | |
| Clientes e usuários dos serviços | |
| Arquitetura corporativa e subdomínios | |
| Participantes do desenho | |
| Participantes da implantação | |
| Fornecedores de produto e serviço | |
| Reguladores e entidades setoriais | |

1. Preencha a coluna com os papéis classificados no Item 1 e identifique duas categorias que ficaram sem representante.
2. Explique, em até três linhas por categoria, que risco a ausência de cada uma introduz no processo.

### Item 3: Ponto de vista para três papéis

Um [ponto de vista](../referencia/glossario.md#ponto-de-vista) declara o critério de seleção, a estrutura do artefato e a forma de apresentação, e a [visão](../referencia/glossario.md#visao) é o resultado de aplicá-lo à descrição de arquitetura. O quadro abaixo traz, na primeira linha, o exemplo do gestor descrito na seção [Pontos de vista na prática](#pontos-de-vista-na-pratica), e deixa três linhas em branco.

| Papel | Preocupação principal | Critério de seleção | Estrutura do artefato | Forma de apresentação |
| --- | --- | --- | --- | --- |
| Gestor (exemplo) | Saber se cada preocupação chegou a uma decisão acompanhável | Origem da necessidade, requisito, elemento afetado, evidência esperada e situação da decisão | Planilha de rastreabilidade | Uma linha por preocupação, com filtro por situação |
| | | | | |
| | | | | |
| | | | | |

1. Escolha três papéis do mapa de atores do Item 1 e preencha uma linha do quadro para cada um, seguindo o exemplo do gestor.

### Item 4: Declaração de escopo do primeiro ciclo

O quadro abaixo lista dez elementos do sistema acadêmico e do seu entorno, com duas colunas em branco. A declaração de escopo registra o que muda no primeiro ciclo de 12 meses e o que permanece, e cada exclusão precisa indicar de onde veio.

| Código | Elemento | Muda ou permanece | Origem da exclusão |
| --- | --- | --- | --- |
| E1 | Integração de notas e turmas com o ambiente virtual de aprendizagem | | |
| E2 | Ambiente virtual de aprendizagem | | |
| E3 | ERP financeiro | | |
| E4 | Programas COBOL do núcleo acadêmico | | |
| E5 | Portal do aluno, na renovação de matrícula pelo telefone celular | | |
| E6 | Autenticação de alunos e professores por padrões abertos | | |
| E7 | Trilha de auditoria de leitura de dado pessoal de aluno | | |
| E8 | Contrato de capacidade do mainframe | | |
| E9 | Região de implantação dos componentes em nuvem | | |
| E10 | Responsabilidade pela correção de dado cadastral de aluno | | |

1. Marque cada elemento como muda ou permanece no primeiro ciclo de 12 meses.
2. Indique, para cada elemento que permanece, a origem da exclusão, entre as restrições fechadas do caso, os contratos vigentes e as decisões de governança registradas no dossiê. O quadro marcado constitui a declaração de escopo do primeiro ciclo.

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seções 6.1, 6.2, 6.3 e 6.5)
- International Organization for Standardization/International Electrotechnical Commission/Institute of Electrical and Electronics Engineers. (2022). *Systems and software engineering — Architecture description* (ISO/IEC/IEEE 42010:2022). (definições de parte interessada, ponto de vista e visão)
- Clements, P., Bachmann, F., Bass, L., Garlan, D., Ivers, J., Little, R., Merson, P., Nord, R., & Stafford, J. (2010). *Documenting software architectures: Views and beyond* (2nd ed.). Addison-Wesley. (visões e pontos de vista na documentação de arquitetura)

**Material do curso.** Glossário, entradas [parte interessada](../referencia/glossario.md#parte-interessada), [ponto de vista](../referencia/glossario.md#ponto-de-vista), [visão](../referencia/glossario.md#visao) e [bloco de construção da solução](../referencia/glossario.md#bloco-de-construcao-da-solucao). Dossiê da instituição fictícia [ACME](../caso-acme/index.md), mapa de atores, interesses em conflito e restrições fechadas.
