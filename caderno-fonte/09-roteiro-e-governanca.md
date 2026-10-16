---
secao: 9
titulo: Roteiro e governança
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| Para que serve | Uma boa solução falha quando é entregue na ordem errada ou sem acompanhamento. Esta seção define a ordem das entregas e a forma de vigiar a arquitetura, para que a obra não se afaste do desenho. |
| Pergunta que responde | Em que ordem as lacunas serão fechadas, e como evitar que a obra se afaste do que foi desenhado? |
| O que você escreve | Você divide o roteiro em ondas, que são etapas de entrega, e dá a cada uma as suas entregas e o critério para considerá-la concluída. Depois descreve a rotina de revisão da arquitetura, os testes automáticos que avisam quando uma decisão deixa de ser cumprida e o registro dos atalhos aceitos, que se chama dívida técnica. Por fim, você registra as regras de uso de IA no projeto, isto é, como cada saída de modelo é verificada e como a assistência é anotada no registro de decisão. |
| Vem de onde | Da seção 4, porque as lacunas confirmadas são a matéria das ondas. |
| Quando se preenche | Você preenche esta seção na Aula 6, nos exercícios 21, 22 e 23. |
<!--/orientacao-->

<!--ex n=21 titulo="Ordem das ondas e critério de conclusão"-->
<!--campos-->
- **Ordem das ondas:** coloque as três entregas do enunciado na ordem das ondas 1, 2 e 3.
- **Justificativa pelo critério de conclusão:** para cada onda, escreva em uma frase a dependência ou o critério de conclusão que justifica a posição.
- **Entrega que depende do fim da exclusividade da fábrica:** diga qual das três entregas só pode alterar o núcleo depois de 30/09/2027.
- **Ondas do primeiro ciclo:** diga quais ondas formam o primeiro ciclo de 12 meses e que orçamento elas respeitam.
<!--/campos-->
<!--gabarito-->
#### Ordem das ondas e critério de conclusão

A ordem das ondas da ACME acompanha as dependências técnicas, e o critério de conclusão de cada entrega diz o que precisa estar em produção, validado e operando antes de a onda seguinte começar. Com as três entregas do enunciado, a sequência é a entrega C na onda 1, a A na onda 2 e a B na onda 3.

| Onda | Entrega do enunciado | Por que nessa posição |
| --- | --- | --- |
| 1 | C, zona de pouso, logon único, gateway de APIs, camada anticorrupção e portal básico do aluno | É a base de que as outras duas dependem, e o critério pede o portal básico em produção, a autenticação por OpenID Connect e a consulta ao núcleo pela camada anticorrupção, sem acesso direto ao banco |
| 2 | A, matrícula digital, aplicativo móvel mínimo viável e integração automatizada com o ERP financeiro | O critério exige a matrícula digital operando numa janela real com o R6 medido em produção, e isso só é possível sobre o logon único, o gateway e a camada anticorrupção da onda 1 |
| 3 | B, migração das regras de negócio do COBOL | O critério pede as regras migradas cobertas por teste automatizado, e a cobertura do núcleo hoje é de 0%, de modo que a onda também espera o fim da exclusividade da fábrica |

Duas perguntas de calendário completam a resposta. A primeira trata da entrega que mexe no núcleo, e a segunda do orçamento do primeiro ciclo.

| Pergunta | Resposta |
| --- | --- |
| Que entrega depende do fim da exclusividade da fábrica | A B, porque a equipe interna não pode alterar o núcleo antes de 30/09/2027, e retirar carga do núcleo só reduz o desembolso a partir de 2029, depois do contrato de grande porte que termina em 31/12/2028 |
| Que ondas formam o primeiro ciclo de 12 meses | As ondas 1 e 2, que precisam caber no orçamento de R$ 6,2 milhões aprovado pela Reitoria |
<!--/gabarito-->
<!--/ex-->

<!--ex n=22 titulo="Desvio, mecanismos de governança e quem decide"-->
<!--campos-->
- **Mecanismo contra o desvio:** associe cada uma das cinco situações do enunciado a um dos cinco mecanismos e diga o que o mecanismo faz nela.
- **Quem decide:** para cada pedido do enunciado, diga o tipo da decisão e quem a aprova.
- **Regra que vira função de aptidão:** marque quais das quatro regras podem ser verificadas por um teste automático e diga quando o teste roda.
- **Decisão protegida pela função de aptidão:** para cada regra marcada, diga qual decisão registrada ela protege.
<!--/campos-->
<!--gabarito-->
#### Mecanismo contra cada situação de desvio

Cada situação de desvio da ACME pede o mecanismo de governança que a contém no ponto certo, antes da implantação, na hora de pedir uma exceção ou depois de aceita. As cinco situações se associam a um mecanismo cada.

| Situação | Mecanismo | O que ele faz na situação |
| --- | --- | --- |
| S1, a esteira interrompe a conexão direta com o banco do núcleo | Função de aptidão | Reprova a mudança na esteira de integração antes da implantação, sem depender de revisão humana |
| S2, a equipe escreve um pedido que cita o registro afetado | Processo de proposta e aprovação | Define como a decisão nova é proposta, revisada e aprovada, no formato de pedido de comentários |
| S3, a arquiteta recém-chegada encontra no repositório o motivo da regra | ADR versionado junto ao código | Guarda a decisão com contexto e consequências, de modo que a resposta não dependa de quem decidiu |
| S4, o grupo examina as propostas 30 dias antes da janela de matrícula | Conselho de revisão | Reúne os decisores em datas fixas e examina as decisões que mudam a estrutura da solução |
| S5, o atalho aceito é anotado com risco, prazo e onda de correção | Gestão de dívida técnica | Registra o desvio aceito para que ele entre no roteiro como item a corrigir |

#### Quem decide cada pedido

Os quatro pedidos do enunciado pertencem a tipos de decisão diferentes, e cada tipo tem um aprovador definido na matriz de responsabilidades. O tipo de estrutura da solução não aparece em nenhum pedido.

| Pedido | Tipo da decisão | Quem decide |
| --- | --- | --- |
| P1, usar banco que não consta do modelo técnico de referência | Exceção ao modelo técnico de referência | Conselho de revisão |
| P2, alterar o formato de um evento de modo incompatível | Mudança incompatível de contrato de integração | Conselho de revisão |
| P3, contratar o plano superior do ambiente virtual, 38% mais caro por ano | Contrato com fornecedor ou acréscimo de custo | Diretor Financeiro, com o material preparado pelo arquiteto de solução |
| P4, prioridades diferentes da Graduação e da Educação a Distância | Prioridade de atributo de qualidade em conflito | Patrocinador |

#### Regras que viram função de aptidão

Uma regra só vira função de aptidão quando um programa consegue conferi-la sozinho, e as outras seguem para a revisão humana. Das quatro regras do enunciado, duas viram teste automático.

| Regra | Vira função de aptidão | Decisão protegida e momento em que roda |
| --- | --- | --- |
| V1, nenhum serviço novo abre conexão com o banco do núcleo | Sim | Protege a decisão de acessar o núcleo pela camada anticorrupção e roda a cada mudança |
| V2, percentil 95 da confirmação em até 4 segundos com 5.800 sessões | Sim | Protege o cenário de qualidade da matrícula, o requisito R6, e roda no ambiente de teste de carga antes de cada janela de matrícula |
| V3, decidir se renova, reduz ou internaliza a sustentação do núcleo | Não | É decisão de contrato, que exige julgamento de quem responde por ele |
| V4, duas pessoas capazes de explicar a regra de prioridade de vaga | Não | Depende de pessoas e de capacitação, e nenhum teste automático confere conhecimento |
<!--/gabarito-->
<!--/ex-->
<!--ex n=23 titulo="Verificação de uma saída de IA e registro da assistência"-->
<!--campos-->
- **Verificação de rastreabilidade:** diga, para cada afirmação do contexto gerado, se ela tem origem em dado vigente e corrija a que não tem, citando a fonte.
- **Consequência omitida:** escreva as consequências negativas que o rascunho não traz, com o dado do enunciado que as comprova.
- **Decisão que volta à autoridade:** corrija o estado e a data do registro e diga quem decide.
- **Registro da assistência de IA:** escreva a ferramenta, as partes rascunhadas, o prompt e a versão, as verificações aplicadas e o revisor.
<!--/campos-->
<!--gabarito-->
#### Verificação do rascunho do ADR 001 gerado por modelo de linguagem

O rascunho do ADR 001 que o modelo devolveu tinha os dez campos e linguagem correta, e a conferência contra as fontes vigentes do caderno encontrou três erros. A primeira verificação, a rastreabilidade até a fonte, separa a afirmação que tem origem vigente da que veio de um documento superado.

| Afirmação do contexto gerado | Origem vigente | Resultado | Correção |
| --- | --- | --- | --- |
| 4.000 usuários simultâneos na abertura da matrícula | Nenhuma. O requisito vigente pede 5.800 sessões simultâneas | Sem origem vigente | Escrever 5.800 sessões simultâneas, requisito R6 da Diretoria de TI |
| Tempo médio de confirmação de até 3 segundos | Nenhuma. O requisito vigente fixa o percentil 95 em até 4 segundos | Sem origem vigente | Escrever percentil 95 do tempo de confirmação em até 4 segundos, requisito R6 |
| Erro de 6,3% contra a meta de 1% | Dados operacionais da ACME e meta registrada no ADR do exercício 12 | Rastreável | Manter |
| 4h20 de indisponibilidade em 04/02/2026 | Incidente registrado nos dados operacionais | Rastreável | Manter |

Os dois valores errados vinham de uma versão anterior do documento de orientação do projeto, que o arquiteto anexou ao pedido, e o modelo os repetiu com a mesma segurança dos dados corretos.

#### Consequência omitida e decisão que volta a quem tem autoridade

A segunda verificação compara o texto com o modelo de dez campos e com o ADR já registrado. O rascunho cita só ganhos, e o modelo do ADR exige ao menos uma consequência negativa, além da positiva e da neutra. A mesma comparação mostra que o campo de estado afirma uma aprovação que ninguém deu.

| Ponto | O que o rascunho diz | O que o caderno registra | Quem decide |
| --- | --- | --- | --- |
| Consequência negativa omitida | Só ganhos, como o isolamento entre o portal e o núcleo | O aluno deixa de receber a confirmação da matrícula na hora, e a equipe passa a operar um componente assíncrono, com duas implementações a manter e limites ajustados sem teste de carga. O que o aluno percebe na matrícula é a confirmação que deixa de ser imediata | Quem aceita o risco é o Diretor de TI, e a aceitação de um risco é uma das quatro tarefas de julgamento que não se delegam ao modelo |
| Estado | Aceita | Proposta | Diretor de TI |
| Data | 14/09/2026 | A definir, junto ao Diretor de TI | Diretor de TI |
| Frase da decisão | A decisão foi aprovada pelo Diretor de TI | Retirar a frase, pois nenhuma fonte registra a aprovação | Diretor de TI |

#### Registro da assistência de IA no ADR 001

A terceira etapa, a revisão por par, fecha com o registro na subseção Assistência de IA, dentro do campo de evidências do ADR 001. O registro permite a quem lê o ADR saber o que o modelo escreveu, com qual prompt e quem conferiu.

| Dado do registro | Conteúdo |
| --- | --- |
| Ferramenta | Modelo de linguagem aprovado pela área de segurança, sem dado pessoal no pedido, porque as atas foram tratadas antes do envio |
| Partes rascunhadas pelo modelo | Contexto, forças, decisão e consequências |
| Prompt e versão | redator-adr, versão 1.0, do repositório de arquitetura |
| Verificações aplicadas | Rastreabilidade até a fonte, checagem contra a restrição e o modelo do ADR, e revisão por par, com os dados vigentes do caso. Foram corrigidos o número de sessões, a medida do tempo de confirmação, o estado e a data, e foram acrescentadas as consequências negativas |
| Revisor | O segundo arquiteto da equipe, que não escreveu o pedido e conhece o contexto da solução. Nome a definir |

A decisão do ADR 001 continua com o Diretor de TI, e o nome de quem a tomar entra no registro quando ela acontecer.
<!--/gabarito-->
<!--/ex-->
