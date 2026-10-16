---
secao: 0
titulo: A solução em uma página
modo: substitui
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| Para que serve | Quem decide sobre o projeto raramente lê o caderno inteiro. Este resumo de uma página dá a essa pessoa o essencial para apoiar o projeto ou questioná-lo. |
| Pergunta que responde | Se alguém lesse só esta página, entenderia o projeto? |
| O que você escreve | Seis parágrafos curtos: qual é o problema, que pergunta o projeto responde, qual é a decisão central, que requisito mais pesa no desenho, o que a ACME aceita perder em troca e em que pé está o trabalho. |
| Vem de onde | Das outras seções. O resumo só repete, em poucas linhas, o que o caderno já registra. |
| Quando se preenche | Ao fim de cada aula, nos exercícios 4, 8, 12, 16, 20 e 24. Cada versão substitui a anterior. |
<!--/orientacao-->

<!--ex n=4 titulo="Resumo ao fim da Aula 1"-->
<!--gabarito-->
**O problema.** A ACME é uma universidade privada com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, com núcleo em COBOL, que custa R$ 15,83 milhões por ano e leva 34 dias úteis para colocar uma mudança em produção. Dos 6 especialistas em COBOL, 2 se aposentam em 2027.

**A pergunta.** Como evoluir o sistema acadêmico de forma segura e incremental, com o núcleo em operação durante a transição e respeitando os contratos já assumidos.

**A decisão central.** Ainda não há. O processo está na fase de descoberta, e a Reitoria já descartou a substituição integral e a reescrita em entrega única.

**O requisito que guia o desenho.** A definir na Aula 2, quando os requisitos declarados forem classificados e medidos.

**O que a organização aceita em troca.** A definir, depois da escolha do estilo na Aula 3.

**Como está o trabalho.** As decisões D1 a D9 estão classificadas por nível, as decisões D2, D3, D5, D6, D8 e D9 e as sete premissas estão **propostas**, e a data de conclusão do ciclo depende da fase 7 do processo.
<!--/gabarito-->
<!--/ex-->

<!--ex n=8 titulo="Resumo ao fim da Aula 2"-->
<!--gabarito-->
**O problema.** A ACME é uma universidade privada com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, com núcleo em COBOL, que custa R$ 15,83 milhões por ano e leva 34 dias úteis para colocar uma mudança em produção. Dos 6 especialistas em COBOL, 2 se aposentam em 2027.

**A pergunta.** Como evoluir o sistema acadêmico de forma segura e incremental, com o núcleo em operação durante a transição e respeitando os contratos já assumidos.

**A decisão central.** Ainda não há. A Reitora pede resultado em 12 meses, e o primeiro ciclo já tem o escopo registrado na seção 2, com a lista dos elementos que mudam e dos que permanecem. A escolha do estilo fica para a Aula 3.

**O requisito que guia o desenho.** O R6, que exige 5.800 sessões simultâneas na abertura da matrícula com percentil 95 do tempo de confirmação em até 4 segundos. Os cenários do pico de matrícula e do incidente de sessão foram julgados significativos para a arquitetura, e o R7, que pede a nota no ambiente virtual em até 10 minutos, completa o par que mais pesa.

**O que a organização aceita em troca.** A definir, depois da escolha do estilo na Aula 3.

**Como está o trabalho.** Os direcionadores de mudança, os requisitos, os cenários, as restrições e as partes interessadas estão registrados. As decisões D2, D3, D5, D6, D8 e D9 e as sete premissas continuam **propostas**.
<!--/gabarito-->
<!--/ex-->

<!--ex n=12 titulo="Resumo ao fim da Aula 3"-->
<!--gabarito-->
**O problema.** A ACME é uma universidade privada com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, com núcleo em COBOL, que custa R$ 15,83 milhões por ano e leva 34 dias úteis para colocar uma mudança em produção. Dos 6 especialistas em COBOL, 2 se aposentam em 2027.

**A pergunta.** Como evoluir o sistema acadêmico de forma segura e incremental, com o núcleo em operação durante a transição e respeitando os contratos já assumidos.

**A decisão central.** Adotar a arquitetura orientada a eventos na entrada da matrícula, com fila entre o portal e o núcleo, e Strangler Fig, Anti-Corruption Layer, Timeout, Circuit Breaker, Bulkhead e Transactional Outbox como padrões. O registro é o ADR 001, em estado de proposta.

**O requisito que guia o desenho.** O R6. O Portal do Aluno chega a 5.800 sessões simultâneas, 7,1 vezes a média de 815, com erro de 6,3% contra a meta de 1%, e a fila absorve esse pico sem alterar o núcleo.

**O que a organização aceita em troca.** A confirmação da matrícula deixa de ser síncrona para o aluno, e a equipe passa a operar um componente assíncrono, com os custos de cada padrão e a entrega ao menos uma vez.

**Como está o trabalho.** O estilo e os padrões estão decididos como proposta. Faltam a data e os decisores do ADR 001, e não existe ensaio de carga com 5.800 sessões.
<!--/gabarito-->
<!--/ex-->

<!--ex n=16 titulo="Resumo ao fim da Aula 4"-->
<!--gabarito-->
**O problema.** A ACME é uma universidade privada com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, com núcleo em COBOL, que custa R$ 15,83 milhões por ano e leva 34 dias úteis para colocar uma mudança em produção. Dos 6 especialistas em COBOL, 2 se aposentam em 2027.

**A pergunta.** Como evoluir o sistema acadêmico de forma segura e incremental, com o núcleo em operação durante a transição e respeitando os contratos já assumidos.

**A decisão central.** A do ADR 001, a arquitetura orientada a eventos na entrada da matrícula. Os domínios de negócio, de dados, de aplicações e de integração já têm o efeito do primeiro ciclo registrado, com o diagrama de contexto e o de contêineres da arquitetura alvo.

**O requisito que guia o desenho.** O R6 para a matrícula e o R7 para a nota. A relação entre o serviço de notas e o ambiente virtual é assíncrona, e o núcleo COBOL, que a equipe da ACME não pode alterar até 30/09/2027, permanece como sistema de registro.

**O que a organização aceita em troca.** A confirmação assíncrona da matrícula e a dependência da fábrica de software para gravar o evento junto com a nota no programa COBOL.

**Como está o trabalho.** A arquitetura de negócio, de dados, de aplicações e de integração está registrada. Faltam a infraestrutura e a tecnologia, e os pontos sem informação no dossiê constam como pendências.
<!--/gabarito-->
<!--/ex-->

<!--ex n=20 titulo="Resumo ao fim da Aula 5"-->
<!--gabarito-->
**O problema.** A ACME é uma universidade privada com 38.400 alunos ativos e um sistema acadêmico em operação desde 2004, com núcleo em COBOL, que custa R$ 15,83 milhões por ano e leva 34 dias úteis para colocar uma mudança em produção. Dos 6 especialistas em COBOL, 2 se aposentam em 2027.

**A pergunta.** Como evoluir o sistema acadêmico de forma segura e incremental, com o núcleo em operação durante a transição e respeitando os contratos já assumidos.

**A decisão central.** Duas decisões em estado de proposta. O ADR 001 adota a arquitetura orientada a eventos na entrada da matrícula, e o ADR de plataforma adota a plataforma de microsserviços na variante Java, com Kafka como barramento de eventos, por aproveitar a camada Java já existente.

**O requisito que guia o desenho.** O R6 e o R7, com o R14 como limite: nenhum dado pessoal de aluno é processado fora do território nacional, e a zona de pouso na nuvem precisa respeitar essa região.

**O que a organização aceita em troca.** A confirmação assíncrona da matrícula, a capacitação da equipe em componentes que o dossiê não registra e uma superfície de observação maior, absorvida pelo mesmo time.

**Como está o trabalho.** A tecnologia, a plataforma, a segurança e o registro da plataforma estão decididos como proposta. Restam as pendências da seção 10, entre elas o ensaio de carga com 5.800 sessões e a data dos dois registros.
<!--/gabarito-->
<!--/ex-->
