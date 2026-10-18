---
secao: 0
titulo: A solução em uma página
modo: substitui
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| Para que serve | Quem decide sobre o projeto da ACME raramente lê o caderno inteiro e, mesmo assim, precisa apoiá-lo ou questioná-lo depois de poucos minutos de leitura. Por isso este resumo de uma página reúne o essencial, e a decisão pode ser tomada sem percorrer as outras seções. |
| Pergunta que responde | Se alguém lesse só esta página, entenderia o projeto? |
| O que você escreve | Você escreve seis parágrafos curtos, que contam nesta ordem qual é o problema, que pergunta o projeto responde, qual é a decisão central, que exigência mais pesa no desenho, quais são as consequências da decisão para a ACME e em que estágio está o trabalho. |
| Vem de onde | O resumo não traz informação nova, porque retoma em poucas linhas o que as outras seções já registram, e por isso ele é escrito depois delas. |
| Quando se preenche | Ao fim de cada aula você reescreve o resumo, nos exercícios 4, 8, 12, 16, 20 e 24, e cada versão substitui a anterior. |
<!--/orientacao-->

<!--ex n=4 titulo="Resumo ao fim da Aula 1"-->
<!--gabarito-->
**O problema.** A ACME é uma universidade privada com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, com núcleo em COBOL, que custa R$ 15,83 milhões por ano e leva 34 dias úteis para colocar uma mudança em produção. A situação se agrava porque, dos 6 especialistas em COBOL que o sustentam, 2 se aposentam em 2027.

**A pergunta.** Diante desse quadro, o projeto pergunta como evoluir o sistema acadêmico de forma segura e incremental, com o núcleo em operação durante a transição e respeitando os contratos já assumidos.

**A decisão.** Ainda não há. O processo está na fase de descoberta, e a Reitoria já descartou a substituição integral e a reescrita em entrega única.

**O que mais pesa no desenho.** A definir na Aula 2, quando as exigências do projeto forem classificadas e medidas.

**Consequências.** A definir, depois da escolha do estilo de arquitetura na Aula 3.

**Como está o trabalho.** As nove decisões levantadas estão classificadas por nível. Seis delas, assim como as sete premissas, ainda são propostas e precisam de validação das partes interessadas. A data de conclusão do ciclo depende da fase 7 do processo.
<!--/gabarito-->
<!--/ex-->

<!--ex n=8 titulo="Resumo ao fim da Aula 2"-->
<!--gabarito-->
**O problema.** A ACME é uma universidade privada com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, com núcleo em COBOL, que custa R$ 15,83 milhões por ano e leva 34 dias úteis para colocar uma mudança em produção. A situação se agrava porque, dos 6 especialistas em COBOL que o sustentam, 2 se aposentam em 2027.

**A pergunta.** Diante desse quadro, o projeto pergunta como evoluir o sistema acadêmico de forma segura e incremental, com o núcleo em operação durante a transição e respeitando os contratos já assumidos.

**A decisão.** Ainda não há. A Reitora pede resultado em 12 meses, e o primeiro ciclo já tem o escopo registrado na seção 2, com a lista do que muda e do que permanece. A escolha do estilo de arquitetura fica para a Aula 3.

**O que mais pesa no desenho.** A matrícula. Na abertura, o Portal do Aluno precisa sustentar 5.800 sessões simultâneas, com o tempo de confirmação em até 4 segundos para 95% das requisições (o requisito R6 do dossiê). O segundo ponto de atenção é a nota: o professor lança e o aluno precisa vê-la no ambiente virtual de aprendizagem em até 10 minutos (o R7). Os cenários do pico de matrícula e do incidente de sessão foram julgados significativos para a arquitetura.

**Consequências.** A definir, depois da escolha do estilo de arquitetura na Aula 3.

**Como está o trabalho.** Os direcionadores de mudança, os requisitos, os cenários, as restrições e as partes interessadas estão registrados. As nove decisões levantadas na Aula 1 e as sete premissas continuam propostas.
<!--/gabarito-->
<!--/ex-->

<!--ex n=12 titulo="Resumo ao fim da Aula 3"-->
<!--gabarito-->
**O problema.** A ACME é uma universidade privada com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, com núcleo em COBOL, que custa R$ 15,83 milhões por ano e leva 34 dias úteis para colocar uma mudança em produção. A situação se agrava porque, dos 6 especialistas em COBOL que o sustentam, 2 se aposentam em 2027.

**A pergunta.** Diante desse quadro, o projeto pergunta como evoluir o sistema acadêmico de forma segura e incremental, com o núcleo em operação durante a transição e respeitando os contratos já assumidos.

**A decisão.** A ACME adota a arquitetura orientada a eventos na entrada da matrícula, com uma fila entre a entrada da matrícula e o núcleo COBOL. Para a convivência com o sistema antigo e para a falha de integração, a decisão traz seis padrões de projeto, listados no registro ADR 001, que está em estado de proposta.

**O que mais pesa no desenho.** A abertura da matrícula. O Portal do Aluno recebe em média 815 sessões simultâneas e chega a 5.800, 7,1 vezes a média, com erro de 6,3% contra a meta de 1%. A fila absorve esse pico sem alterar o núcleo.

**Consequências.** A confirmação da matrícula deixa de ser imediata para o aluno, porque o pedido entra na fila e o núcleo o processa depois. A equipe também passa a operar uma fila e os seis padrões, o que exige manter duas implementações, ajustar limites sem teste de carga e tratar mensagens entregues mais de uma vez.

**Como está o trabalho.** O estilo e os padrões estão decididos como proposta. Faltam a data e os decisores do ADR 001, e a ACME ainda não tem ambiente para um ensaio de carga com 5.800 sessões.
<!--/gabarito-->
<!--/ex-->

<!--ex n=16 titulo="Resumo ao fim da Aula 4"-->
<!--gabarito-->
**O problema.** A ACME é uma universidade privada com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, com núcleo em COBOL, que custa R$ 15,83 milhões por ano e leva 34 dias úteis para colocar uma mudança em produção. A situação se agrava porque, dos 6 especialistas em COBOL que o sustentam, 2 se aposentam em 2027.

**A pergunta.** Diante desse quadro, o projeto pergunta como evoluir o sistema acadêmico de forma segura e incremental, com o núcleo em operação durante a transição e respeitando os contratos já assumidos.

**A decisão.** A mesma do ADR 001, a arquitetura orientada a eventos na entrada da matrícula. Esta versão acrescenta o efeito da solução nos quatro domínios de arquitetura: o negócio, os dados, as aplicações com suas integrações e a infraestrutura, com o diagrama de contexto e o de contêineres da arquitetura alvo.

**O que mais pesa no desenho.** A matrícula, com 5.800 sessões simultâneas na abertura, e a nota, que precisa chegar ao ambiente virtual em até 10 minutos. Por isso o envio da nota entre o serviço de notas e o ambiente virtual é assíncrono. O núcleo COBOL permanece como sistema de registro, porque a equipe da ACME não pode alterá-lo até 30/09/2027.

**Consequências.** A confirmação da matrícula continua assíncrona. Além disso, para publicar o evento da nota na mesma transação em que ela é gravada, a ACME depende da fábrica de software, a única que pode alterar o programa COBOL de avaliação e notas.

**Como está o trabalho.** Os domínios de negócio, de dados, de aplicações e de integração estão registrados, e o de infraestrutura já tem o diagrama de contêineres. A tecnologia de cada contêiner ainda está por definir, e os pontos sem informação no dossiê constam na seção de pendências.
<!--/gabarito-->
<!--/ex-->

<!--ex n=20 titulo="Resumo ao fim da Aula 5"-->
<!--gabarito-->
**O problema.** A ACME é uma universidade privada com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, com núcleo em COBOL, que custa R$ 15,83 milhões por ano e leva 34 dias úteis para colocar uma mudança em produção. A situação se agrava porque, dos 6 especialistas em COBOL que o sustentam, 2 se aposentam em 2027.

**A pergunta.** Diante desse quadro, o projeto pergunta como evoluir o sistema acadêmico de forma segura e incremental, com o núcleo em operação durante a transição e respeitando os contratos já assumidos.

**A decisão.** Há duas decisões em estado de proposta. A primeira, o ADR 001, adota a arquitetura orientada a eventos na entrada da matrícula. A segunda, o ADR de plataforma, escolhe a plataforma de microsserviços na variante Java, com o Kafka como barramento de eventos, porque a ACME já tem 9 pessoas na camada Java e porque essa plataforma convive com o núcleo pelas transações CICS existentes.

**O que mais pesa no desenho.** A matrícula (5.800 sessões simultâneas) e a nota (10 minutos até o ambiente virtual), com uma restrição do Jurídico. Nenhum dado pessoal de aluno pode ser processado fora do território nacional, e por isso a região escolhida para a nuvem precisa ficar no Brasil.

**Consequências.** A confirmação da matrícula continua assíncrona. A equipe Java precisará de capacitação em tecnologias cuja experiência o dossiê não registra. Além disso, a plataforma nova aumenta o que a equipe precisa observar em produção, e o mesmo time absorve esse trabalho.

**Como está o trabalho.** A tecnologia, a plataforma, as decisões de segurança dos dados e o registro da plataforma estão decididos como proposta. Restam as pendências da seção 10, entre elas o ensaio de carga com 5.800 sessões e a data dos dois registros.
<!--/gabarito-->
<!--/ex-->

<!--ex n=24 titulo="Resumo final do caderno"-->
<!--campos-->
- **O problema:** conte a situação da ACME e por que ela exige mudança, com os números do caso.
- **A pergunta:** escreva a pergunta que o projeto responde.
- **A decisão:** diga a decisão central do projeto e o estado dela, proposta ou aceita.
- **O que mais pesa no desenho:** diga qual exigência mais pesa, escrevendo o conteúdo e a medida antes do código.
- **Consequências:** diga o que a decisão custa à ACME, com ao menos uma consequência para a equipe.
- **Como está o trabalho:** diga o que está decidido, o que está proposto e o que falta, incluindo o roteiro em ondas e a conferência final.
<!--/campos-->
<!--gabarito-->
**O problema.** A ACME é uma universidade privada com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, com núcleo em COBOL, que custa R$ 15,83 milhões por ano e leva 34 dias úteis para colocar uma mudança em produção. A situação se agrava porque, dos 6 especialistas em COBOL que o sustentam, 2 se aposentam em 2027.

**A pergunta.** Diante desse quadro, o projeto pergunta como evoluir o sistema acadêmico de forma segura e incremental, com o núcleo em operação durante a transição e respeitando os contratos já assumidos.

**A decisão.** A ACME adota duas decisões, ambas em estado de proposta. A primeira, o ADR 001, coloca uma fila entre a entrada da matrícula e o núcleo COBOL na entrada da matrícula. A segunda, o ADR de plataforma, escolhe a plataforma de microsserviços na variante Java, com o Kafka como barramento de eventos. A entrega segue em três ondas: primeiro a base de acesso (zona de pouso, logon único, gateway de APIs, camada anticorrupção e portal básico do aluno), depois a matrícula digital com o aplicativo móvel e, por último, a migração das regras de negócio do COBOL, que só começa depois de 30/09/2027. O primeiro ciclo de 12 meses cobre as duas primeiras ondas, dentro do orçamento de R$ 6,2 milhões.

**O que mais pesa no desenho.** Duas exigências pesam mais no desenho, a da matrícula e a da nota. Na abertura, o Portal do Aluno precisa sustentar 5.800 sessões simultâneas, com o tempo de confirmação em até 4 segundos para 95% das requisições (registrado no dossiê do caso como requisito R6), e a nota lançada pelo professor precisa chegar ao ambiente virtual de aprendizagem em até 10 minutos (requisito R7). Uma restrição do Jurídico acompanha os dois: nenhum dado pessoal de aluno pode ser processado fora do território nacional, e a região escolhida para a nuvem fica no Brasil.

**Consequências.** A confirmação da matrícula deixa de ser imediata para o aluno, porque o pedido entra na fila e o núcleo o processa depois. A equipe Java precisa aprender Kafka, o produto de mensageria, e Kubernetes, que executa os contêineres, e a ACME passa a monitorar mais peças em produção. Para a obra não se afastar do desenho, testes automáticos avisam quando uma decisão deixa de ser cumprida, e todo uso de IA no projeto passa por verificação em três etapas e fica registrado no ADR.

**Como está o trabalho.** O caderno tem as onze seções preenchidas, e a conferência de rastreabilidade apontou três lacunas: uma decisão sem requisito de origem, um requisito de custo sem decisão e uma pendência sem responsável. As duas decisões continuam propostas, e as pendências da seção 10 dizem quem resolve cada ponto e quando.
<!--/gabarito-->
<!--/ex-->
