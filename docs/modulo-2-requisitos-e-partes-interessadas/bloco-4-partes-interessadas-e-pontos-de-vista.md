# Partes interessadas, pontos de vista e escopo

Este bloco trata de quem decide sobre a solução, como essas pessoas são identificadas e avaliadas, como suas preocupações são tratadas por pontos de vista e visões, e como o escopo da mudança é declarado.

## Antes de começar

- [Parte interessada](../referencia/glossario.md#parte-interessada)
- [Ponto de vista](../referencia/glossario.md#ponto-de-vista)
- [Visão](../referencia/glossario.md#visao)
- [Bloco de construção da solução](../referencia/glossario.md#bloco-de-construcao-da-solucao)

## Conceito

As partes interessadas são a ligação entre a solução e o negócio. Escolhidas corretamente, elas representam o negócio e decidem em seu nome, de modo que uma solução que as satisfaça é a solução que o negócio quer. A norma ISO/IEC/IEEE 42010 define parte interessada como o indivíduo, a equipe, a organização ou a classe desses que tem interesse em um sistema.

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

A técnica que organiza esse tratamento tem dois termos que não são sinônimos. O **ponto de vista** define três coisas, o critério de seleção que filtra o que será extraído da descrição de arquitetura, a estrutura do artefato que organiza essa informação, e as instruções de apresentação que a tornam compreensível para aquela audiência. A **visão** é o resultado concreto de aplicar um ponto de vista à descrição de arquitetura.

A consequência prática aparece na validação do desenho. Aplicar o mesmo ponto de vista à arquitetura de linha de base e à arquitetura alvo produz duas visões comparáveis, e a comparação mostra o efeito da mudança sob a perspectiva daquela parte interessada, sem obrigá-la a ler o modelo inteiro.

### Definição do escopo

O escopo da solução é declarado em termos de componentes, e não de intenção. Entram na declaração os componentes de negócio, os de informação e tecnologia, e os blocos de construção, com a distinção entre bloco de construção de arquitetura, que é genérico e reutilizável, e bloco de construção da solução, que é a realização daquele bloco naquela solução. A declaração é documentada e aprovada formalmente, porque é ela que delimita o que será mudado e, por exclusão, o que permanece.

Na ACME, universidade privada brasileira fictícia com 38.400 alunos ativos e sistema acadêmico em operação desde 2004, a declaração de escopo precisa registrar que o ambiente virtual de aprendizagem e o ERP financeiro permanecem, por decisão da Reitoria de 12/03/2026, e que o trabalho sobre eles é de integração e de governança.

## Uso pelo arquiteto

O arquiteto usa a lista de quatro perguntas como verificação contra a omissão mais cara do processo, a parte interessada descoberta tarde. Quem tem autoridade sobre orçamento e quem responde por exigência regulatória costumam ser lembrados, e quem sustenta o sistema depois da implantação costuma ser esquecido até o momento em que a operação recusa o desenho.

Os pontos de vista servem para não travar a discussão em um modelo único. Apresentar o mesmo desenho a um diretor financeiro e a um gerente de sustentação produz duas conversas improdutivas, porque cada um precisa de um recorte diferente da mesma descrição de arquitetura.

## Exercício 8

A ACME é uma universidade privada brasileira fictícia, com 38.400 alunos ativos, 2.150 professores, 1.480 técnico-administrativos e 4 campi. O sistema acadêmico está em operação desde 2004 e é mantido por uma fábrica de software contratada, sob contrato de sustentação vigente até 30/09/2027.

O quadro abaixo reproduz o mapa de atores do caso, com o que cada papel quer e o que teme.

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

Responda às quatro perguntas abaixo.

1. Classifique os oito papéis nas categorias de parte interessada apresentadas no Conceito, e indique qual deles exerce o papel de patrocinador de negócio, com justificativa.
2. Identifique duas categorias da tabela do Conceito que não têm representante no mapa de atores da ACME, e explique que risco a ausência de cada uma introduz.
3. Escolha três papéis e defina, para cada um, um ponto de vista adequado às suas preocupações, declarando o critério de seleção, a estrutura do artefato e a forma de apresentação.
4. Escreva a declaração de escopo do primeiro ciclo de 12 meses, listando o que muda e o que permanece, e indicando a origem de cada exclusão.

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seções 6.1, 6.2, 6.3 e 6.5)
- International Organization for Standardization/International Electrotechnical Commission/Institute of Electrical and Electronics Engineers. (2022). *Systems and software engineering — Architecture description* (ISO/IEC/IEEE 42010:2022). (definições de parte interessada, ponto de vista e visão)
- Clements, P., Bachmann, F., Bass, L., Garlan, D., Ivers, J., Little, R., Merson, P., Nord, R., & Stafford, J. (2010). *Documenting software architectures: Views and beyond* (2nd ed.). Addison-Wesley. (visões e pontos de vista na documentação de arquitetura)

**Material do curso.** Glossário, entradas [parte interessada](../referencia/glossario.md#parte-interessada), [ponto de vista](../referencia/glossario.md#ponto-de-vista), [visão](../referencia/glossario.md#visao) e [bloco de construção da solução](../referencia/glossario.md#bloco-de-construcao-da-solucao). Dossiê da instituição fictícia [ACME](../caso-acme/index.md), mapa de atores, interesses em conflito e restrições fechadas.
