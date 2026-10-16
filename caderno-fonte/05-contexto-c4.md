---
secao: 5
titulo: Contexto do sistema (C4, nível 1)
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| Para que serve | Para que qualquer pessoa entenda a solução em um minuto, o arquiteto a desenha numa única figura, que mostra o que está dentro dela, quem a usa e com quais outros sistemas ela conversa. |
| Pergunta que responde | O que está dentro da solução, o que está fora e com quem ela se relaciona? |
| O que você escreve | Você desenha um diagrama de contexto no formato C4, nível 1, em que a solução aparece como uma caixa só, cercada por quem a usa e pelos outros sistemas com que ela conversa. Junto vão uma legenda e um parágrafo que explica por que cada sistema ficou dentro ou fora da solução. |
| Vem de onde | Das seções 2 e 4, porque as partes interessadas mostram quem usa a solução e o sistema atual mostra com quem ela conversa. |
| Quando se preenche | Você preenche esta seção na Aula 4, no exercício 15. |
<!--/orientacao-->

<!--ex n=15 titulo="Portfólio, contrato de notas e diagrama de contexto"-->
<!--campos-->
- **Classificação da aplicação:** diga se cada uma das onze aplicações do catálogo é verde (manter e evoluir), âmbar (manter por ora, com investimento restrito) ou vermelha (substituir ou retirar).
- **Justificativa da classificação:** escreva uma linha com o fato do caso que levou à cor, como o ano da aplicação, a tecnologia ou a decisão da Reitoria de mantê-la.
- **Contrato de integração de notas:** preencha, com resposta curta, os doze campos do contrato que leva a nota do sistema da ACME ao ambiente virtual de aprendizagem, de Origem até Nível de serviço.
- **Modo de comunicação:** diga se a integração é síncrona, quando quem pede espera a resposta, ou assíncrona, quando quem envia segue adiante, e justifique pelos padrões escolhidos no exercício 11.
- **Nota corrigida:** explique o que acontece quando o professor corrige uma nota que já foi enviada ao ambiente virtual.
- **Erros do diagrama:** aponte os dois erros de nível ou de fronteira que o diagrama de contexto do enunciado contém.
- **Correção de cada erro:** para cada erro, diga qual elemento está errado e onde ele deve ficar no diagrama.
<!--/campos-->
<!--gabarito-->
#### Portfólio de aplicações

Diante das onze aplicações do catálogo, a pergunta do arquiteto é qual delas ainda merece investimento e qual deve sair. Os quatro portais usam tecnologia que o fornecedor deixou de apoiar e por isso ficam em vermelho, o núcleo transacional, que é o sistema em COBOL onde se registram matrícula e nota, ainda sustenta a operação e continua sob contrato, o que o deixa em âmbar, e o ERP financeiro e o ambiente virtual ficam em verde por decisão da Reitoria. A tabela dá a cor de cada aplicação e o fato do caso que a sustenta.

| Aplicação | Cor | Justificativa |
| --- | --- | --- |
| Portal do Aluno | Vermelho | Tecnologia Java JSF 1.2 e EJB 2.0 de 2007, sobre servidor sem suporte desde 2018, sem versão responsiva, o que impede a renovação da matrícula pelo celular pedida pelo requisito R1, e com acesso direto ao banco |
| Portal do Professor | Vermelho | JSF 1.2 e EJB 2.0 de 2008, sobre o mesmo servidor sem suporte |
| Portal da Secretaria | Vermelho | JSF 1.2 e EJB 2.0 de 2008, sobre o mesmo servidor sem suporte |
| Portal do Gestor | Vermelho | JSF 1.2 e EJB 2.0 de 2009, sobre o mesmo servidor sem suporte, e com acesso direto ao banco |
| Núcleo transacional | Âmbar | Programas COBOL executados no servidor de transações CICS, com manutenção sob contrato até 30/09/2027. Vermelho também é aceito quando a resposta cita o horizonte de retirada |
| ERP financeiro | Verde | Permanece por decisão da Reitoria de 12/03/2026 |
| Ambiente virtual de aprendizagem | Verde | Permanece por decisão da Reitoria de 12/03/2026 |
| Data warehouse institucional | Âmbar | O data warehouse, que é o armazém de dados para análises, não tem ano nem tecnologia informados no dossiê, e a cópia integral de 140 tabelas por lote é o único dado disponível. A cor é provisória, e a Diretoria de TI precisa confirmá-la |
| Assinador digital ICP-Brasil | Verde | Serviço externo exigido pelo requisito R5, que pede histórico escolar com assinatura digital no padrão ICP-Brasil, a infraestrutura brasileira de certificados |
| Gateway de pagamento | Verde | Serviço externo chamado pelo Portal do Aluno, sem problema registrado no dossiê. A cor é provisória pelo mesmo motivo do data warehouse |
| Diretório corporativo | Âmbar | Autentica todos os perfis por LDAP, mas o requisito R8 pede padrões abertos de identidade, e o diretório atende só os portais atuais |

#### Contrato da integração de notas

Quando o professor lança a nota, ela nasce no núcleo transacional, que é o dono da nota consolidada pela decisão do exercício 14. Hoje ela segue para o ambiente virtual num arquivo gerado às 05h10, e como a nota precisa chegar ao ambiente virtual em até 10 minutos (requisito R7), o contrato abaixo descreve a troca nova campo a campo, com o modo assíncrono.

| Campo | Resposta |
| --- | --- |
| Origem | Núcleo transacional, dono da nota consolidada, que publica pelo serviço de notas |
| Destino | Ambiente virtual de aprendizagem |
| Gatilho | Nota lançada ou alterada pelo professor |
| Itens trocados | Identificador do aluno, turma, avaliação, nota, situação, versão e data do lançamento |
| Sequência | Publicação do evento, recebimento pelo ambiente virtual e confirmação do processamento |
| Pré e pós-condições | Antes, o aluno está matriculado numa turma já enviada ao ambiente virtual. Depois, a nota está visível ao aluno no ambiente virtual |
| Protocolo | HTTPS ou mensageria, conforme o plano do ambiente virtual que oferece interfaces de programação, com acréscimo de 38% sobre o valor anual do contrato |
| Formato e esquema | Mensagem estruturada, com esquema versionado e descrito em AsyncAPI, a especificação que documenta o formato das mensagens |
| Semântica de erro | Aluno ou turma inexistente vai para uma fila de exceção, tratada pela Secretaria Acadêmica. Indisponibilidade do destino gera nova tentativa, com limite |
| Versionamento | Cada versão do esquema é compatível com a anterior, e uma mudança incompatível sai em versão nova |
| Garantia de entrega e idempotência | Entrega pelo menos uma vez, com chave de idempotência formada por aluno, avaliação e versão, de modo que a repetição de uma mensagem não duplica a nota |
| Nível de serviço | Até 10 minutos entre o lançamento e a visibilidade, conforme o requisito R7, com capacidade para 360.000 lançamentos na janela de fechamento |

A integração é assíncrona, porque a indisponibilidade do ambiente virtual não pode impedir o professor de lançar a nota. O padrão Transactional Outbox, que grava o evento numa tabela na mesma transação da nota, garante que um registro nunca exista sem o outro, e o consumidor idempotente, que ignora a mensagem recebida mais de uma vez, absorve a entrega repetida. A gravação do evento junto com a nota ocorre hoje dentro do programa COBOL de avaliação e notas, que só a fábrica pode alterar até 30/09/2027, e por isso a forma de capturá-la fica como decisão pendente, a definir com a fábrica contratada. O modo síncrono também é aceito quando a resposta declara tempo limite, nova tentativa com limite e Circuit Breaker, o mecanismo que interrompe as chamadas enquanto o destino falha.

Quando o professor corrige uma nota já enviada, o serviço publica uma nova versão da mesma nota, com a mesma chave de aluno e avaliação e uma versão maior. O ambiente virtual substitui o valor anterior pelo da versão mais recente.

#### Diagrama de contexto da solução

O diagrama do enunciado trazia dois erros. O primeiro era o banco de dados acadêmico desenhado como elemento externo, quando ele é um contêiner, parte interna do sistema, que só aparece no nível seguinte. O segundo era o ERP financeiro desenhado dentro da fronteira, quando ele permanece por decisão da Reitoria e é mantido por outra equipe, então precisa ficar fora da caixa. A correção do segundo erro também elimina a caixa duplicada do sistema acadêmico que existia dentro da fronteira.

![Diagrama de contexto corrigido do primeiro ciclo da ACME, com aluno, professor e secretaria acadêmica ligados ao sistema acadêmico, que é uma caixa única dentro da fronteira tracejada, e com seis sistemas externos fora dela: ERP financeiro, ambiente virtual de aprendizagem, assinador digital ICP-Brasil, gateway de pagamento, provedor de identidade e órgão regulador.](../assets/images/acme-ex15-contexto-corrigido.svg){ .module-diagram }

Para que quem lê o diagrama saiba por que cada elemento ficou onde está, a legenda abaixo diz, para cada um, se ele está dentro ou fora da solução e por quê.

| Elemento | Tipo | Posição | Motivo |
| --- | --- | --- | --- |
| Aluno, professor e secretaria acadêmica | Pessoa | Fora | Usam a solução e são mostrados no alto do diagrama |
| Sistema acadêmico, com o núcleo COBOL | Sistema da solução | Dentro | A ACME responde pela evolução e pela operação do núcleo, e a fábrica contratada só faz a manutenção dos programas |
| ERP financeiro | Sistema externo | Fora | Permanece por decisão da Reitoria de 12/03/2026, e a ACME apenas o integra |
| Ambiente virtual de aprendizagem | Sistema externo | Fora | Permanece pela mesma decisão e recebe as notas |
| Assinador digital ICP-Brasil | Sistema externo | Fora | Serviço que assina o histórico escolar, usado sem ser alterado |
| Gateway de pagamento | Sistema externo | Fora | Serviço que gera boleto e cobrança em cartão |
| Provedor de identidade | Sistema externo | Fora | A ACME usa o serviço para autenticar, e o produto só é escolhido na Aula 5 |
| Órgão regulador | Sistema externo | Fora | Recebe a extração anual do censo da educação superior |
<!--/gabarito-->
<!--/ex-->
