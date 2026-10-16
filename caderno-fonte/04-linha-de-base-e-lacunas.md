---
secao: 4
titulo: Linha de base e lacunas
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| Para que serve | Uma mudança só pode ser planejada quando se conhece o ponto de partida, e na ACME esse ponto é o sistema atual, com as suas fragilidades. Esta seção descreve esse sistema e o que o separa da solução desenhada, e linha de base é o nome da situação atual. |
| Pergunta que responde | Onde o sistema atual é frágil, e o que é preciso mudar para chegar ao que se quer construir? |
| O que você escreve | Você descreve o sistema atual, com as camadas que o formam, as integrações com outros sistemas e os incidentes que já aconteceram. Depois lista as lacunas, e cada uma é uma diferença entre o sistema atual e o que foi desenhado, acompanhada da forma de fechá-la. |
| Vem de onde | Do dossiê e da seção 3 para a descrição do sistema atual, e das seções 5 a 8, que descrevem a solução desenhada, para a lista de lacunas. |
| Quando se preenche | Você descreve o sistema atual na Aula 2, no exercício 7, e só depois, na Aula 6, no exercício 21, lista as lacunas. |
<!--/orientacao-->


<!--ex n=7 titulo="Artefatos de linha de base que sustentam os cenários"-->
<!--campos-->
- **Artefato de linha de base:** escolha quatro dos seis artefatos do enunciado que sustentam os dois cenários de qualidade.
- **Dado que o artefato fornece:** diga qual informação do artefato aparece no cenário.
- **Efeito de um dado desatualizado:** diga o que aconteceria com o cenário se esse dado estivesse desatualizado.
<!--/campos-->
<!--gabarito-->
#### Artefatos de linha de base dos cenários

Os cenários do pico de matrícula, com 5.800 sessões simultâneas, e do incidente de 04/02/2026 só são confiáveis se os números que os sustentam estiverem corretos, e esses números vêm dos artefatos da linha de base, os documentos e as medições que descrevem o sistema atual. Quatro dos seis artefatos (L1, L2, L5 e L6) sustentam os cenários, mas o prazo de 34 dias úteis (L3) e o custo anual de R$ 15,83 milhões (L4) não aparecem em nenhum deles.

| Artefato | Dado que fornece | Efeito de um dado desatualizado |
| --- | --- | --- |
| L6, série de medição de sessões simultâneas e de taxa de erro do portal | A média anual de 815 sessões, o pico de 5.800 e a taxa de erro de 6,3% no pico | A razão de 7,1 entre o pico e a média e a meta de erro ficariam erradas, e o teste de carga simularia um pico diferente do real |
| L2, registro dos três incidentes graves dos últimos 18 meses | A sequência do incidente de 04/02/2026, com 4h20 de duração e 62% das tentativas com erro | O cenário do incidente trataria uma causa que não aconteceu, e a medida de 260 minutos de indisponibilidade perderia o ponto de comparação |
| L1, inventário de componentes do sistema acadêmico | O monitor CICS, o limite de tarefas e as camadas que o estímulo atravessa | O campo Artefato apontaria uma parte do sistema que já mudou, e a resposta seria desenhada para o lugar errado |
| L5, contratos de sustentação e de capacidade | O prazo de 30/09/2027 para qualquer alteração no núcleo COBOL | A resposta poderia prever alteração no núcleo sem que o contrato permita, e o tempo limite teria de ficar na camada web |
<!--/gabarito-->
<!--/ex-->

<!--ex n=21 titulo="Lacunas por domínio e tipo"-->
<!--campos-->
- **Domínio da lacuna:** para cada uma das oito lacunas do enunciado, escolha um dos sete domínios do relatório de lacunas.
- **Tipo da lacuna:** diga se a lacuna é técnica ou organizacional.
- **Justificativa da classificação:** cite, em uma frase, o dado do caso que sustenta o tipo escolhido.
- **Forma de fechar a lacuna organizacional:** para cada lacuna organizacional, diga se ela pede capacitação, mudança de processo ou decisão de contrato.
<!--/campos-->
<!--gabarito-->
#### Lacunas por domínio e tipo

Para planejar o fechamento das lacunas, o relatório da ACME agrupa cada diferença entre o sistema atual e o sistema desenhado em um dos sete domínios e diz se ela é técnica ou organizacional, porque a resposta decide se a lacuna segue para o desenho da solução ou para o roteiro de entrega. As oito lacunas analisadas se dividem em quatro técnicas e quatro organizacionais.

| Lacuna | Domínio | Tipo | Justificativa |
| --- | --- | --- | --- |
| Falta de ambiente de teste de carga | Infraestrutura | Técnica | A ACME só tem os ambientes de produção e de homologação, e sem ambiente de teste de carga o pico de 5.800 sessões só se mostra em produção |
| Acesso direto ao banco do núcleo | Dados ou integração | Técnica | Os 2.300 pontos do código Java que leem ou gravam o banco do núcleo se fecham com projeto de software, por contenção e por inventário das entidades |
| Autenticação pelo diretório corporativo por LDAP, sem logon único | Segurança | Técnica | O provedor de identidade com padrões abertos, exigido pelo requisito R8, substitui a autenticação atual por uma solução de tecnologia |
| Troca de dados com o ERP financeiro por arquivos em lote | Integração | Técnica | A troca por arquivos, às 23h10 e às 05h30, faz o pagamento aparecer na situação do aluno cerca de 30 horas depois, e o evento com adaptador a substitui |
| Regra de prioridade de vaga dominada por uma só pessoa | Competência das equipes | Organizacional | Só 1 dos 6 especialistas em COBOL domina a regra, e 2 deles se aposentam em 2027, de modo que a lacuna está no conhecimento das pessoas |
| Implantação mensal, com 34 dias úteis por mudança | Processo | Organizacional | A janela de implantação é no terceiro sábado de cada mês, e a cobertura de teste automatizado é de 0% no núcleo e de 7% na camada Java, de modo que a lacuna está na forma de trabalhar |
| Equipe interna sem experiência registrada nos serviços novos | Competência das equipes | Organizacional | O dossiê não registra experiência da equipe em operar serviços distribuídos, provedor de identidade, mensageria e observabilidade |
| Contrato de sustentação do núcleo que termina em 30/09/2027 sem decisão sobre o que vem depois | Processo | Organizacional | A exclusividade da fábrica sobre os programas COBOL termina nessa data, e a decisão de renovar, reduzir ou internalizar pertence a quem responde pelo contrato |

A classificação do domínio admite variação dentro do mesmo grupo, porque o acesso direto ao banco pode ser lido como dado ou como integração, e as duas leituras são técnicas. O tipo é o que a resposta precisa acertar, pois ele define o destino da lacuna.

#### Como fechar as lacunas organizacionais

Uma lacuna organizacional não se fecha com programa, e por isso o relatório registra a decisão que cabe a quem responde pela área afetada. As quatro lacunas organizacionais pedem três formas de decisão.

| Lacuna organizacional | Forma de fechar | Como o relatório registra |
| --- | --- | --- |
| Regra de prioridade de vaga dominada por uma só pessoa | Capacitação | Formar uma segunda pessoa com domínio da regra antes das aposentadorias de 2027 e registrar a regra em testes de caracterização, que comparam o comportamento do núcleo com o esperado |
| Implantação mensal, com 34 dias úteis por mudança | Mudança de processo | Adotar esteira de integração com testes e implantação automatizada para os componentes novos, já na primeira onda |
| Equipe interna sem experiência registrada nos serviços novos | Capacitação | Capacitar, contratar ou contratar suporte, decidindo caso a caso para cada componente novo antes de ele entrar em operação |
| Contrato de sustentação do núcleo que termina em 30/09/2027 | Decisão de contrato | Decidir entre renovar, reduzir ou internalizar a sustentação e registrar a escolha em um ADR, com a Reitoria e o Diretor de TI |
<!--/gabarito-->
<!--/ex-->
