---
secao: 8
titulo: Tecnologia e plataforma
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| Para que serve | Só depois de tomadas as decisões estruturais faz sentido escolher a tecnologia. Esta seção mostra com que produtos e plataforma a solução será construída e como ela será protegida contra ameaças. |
| Pergunta que responde | Que produtos e que plataforma atendem às decisões já tomadas, e que riscos de segurança precisam de resposta? |
| O que você escreve | Você lista as tecnologias aprovadas, proibidas e em avaliação e compara as alternativas por seis critérios. Depois registra a plataforma e a zona de pouso escolhidas, que é a base em nuvem onde a solução roda, classifica os dados por sensibilidade e relaciona cada ameaça de segurança aos controles contra ela. A seção termina com o registro da decisão sobre a plataforma. |
| Vem de onde | Das seções 5 e 7, porque o desenho e as decisões já tomadas mostram o que a tecnologia precisa fazer. |
| Quando se preenche | Você preenche esta seção na Aula 5, nos exercícios 17, 18, 19 e 20. |
<!--/orientacao-->

<!--ex n=17 titulo="Modelo técnico, tecnologias da linha de base e provedor de identidade"-->
<!--campos-->
- **Linha do modelo e candidatos por bloco:** para cada bloco do catálogo, exceto o núcleo transacional que permanece, diga qual linha do modelo técnico de referência vale, qual padrão ela exige e quais exemplos aprovados da linha são os produtos candidatos, ou escreva candidato a levantar quando não houver linha.
- **Linhas válidas para todos os contêineres:** indique as duas linhas do recorte que valem para qualquer contêiner novo, qualquer que seja a função dele, e explique em uma frase.
- **Classificação da tecnologia:** classifique cada tecnologia da linha de base em verde, âmbar ou vermelho e justifique em uma linha com o dado da tabela.
- **Tecnologias sob plano de migração:** entre as vermelhas, diga quais continuam em uso hoje e só podem ficar enquanto houver plano de migração documentado.
- **Aderência e portabilidade das alternativas:** para cada forma de obter o provedor de identidade (A, B e C), escreva o dado do caso que sustenta a aderência ao requisito e a portabilidade, citando o código do requisito ou da restrição.
- **Dado que falta por critério:** para maturidade, suporte, custo total de propriedade e competência da equipe, diga qual informação o caso não traz e precisa ser levantada.
- **Regra de eliminação pela restrição:** escolha R8 ou R14, diga qual condição elimina uma candidata e qual documento pediria para comprovar atendimento. Não descarte A, B ou C apenas pela forma de contratação.
<!--/campos-->
<!--gabarito-->
#### Blocos do catálogo e linhas do modelo técnico de referência

Cada equipe da ACME precisa saber qual padrão respeitar antes de escolher um produto, e a linha do modelo técnico que trata da função do bloco diz exatamente isso. O provedor de identidade segue a linha de identidade e acesso, que exige o OpenID Connect, protocolo aberto de autenticação, e o evento de nota segue a de mensageria, que exige um contrato AsyncAPI, a especificação das mensagens trocadas. Os candidatos de cada bloco são os exemplos aprovados da linha, e a tabela repete os produtos da tabela de ABB para SBB do bloco 1 da Aula 5, de modo que o gabarito e o bloco apresentam a mesma lista.

| Bloco do catálogo | Linha do modelo técnico | Padrão ou protocolo obrigatório | SBBs candidatos | Origem do candidato |
| --- | --- | --- | --- | --- |
| Interface do aplicativo do aluno | Sem linha no recorte | Não há | React Native | Exemplo a avaliar, fora do recorte |
| Portal do Professor | Sem linha no recorte | Não há | React para web | Exemplo a avaliar, fora do recorte, e só entra se o plano de migração trocar o portal |
| Portal da Secretaria | Sem linha no recorte | Não há | React para web | Exemplo a avaliar, fora do recorte, e só entra se o plano de migração trocar o portal |
| Provedor de identidade | Segurança transversal, identidade e acesso | OpenID Connect obrigatório, com OAuth 2.0 e SAML 2.0 | Keycloak operado pela ACME, Auth0 contratado, Azure AD B2C gerenciado | Exemplos aprovados da linha |
| Serviço de matrícula | API e integração, exposição de serviços | REST com OpenAPI 3.x | Spring Boot, FastAPI, NestJS | Exemplos aprovados da linha |
| Serviço de notas | API e integração, exposição de serviços | REST com OpenAPI 3.x | Spring Boot, FastAPI, NestJS | Exemplos aprovados da linha |
| Banco do serviço de matrícula | Dados, banco de serviço novo | SQL, um banco por serviço e região nacional | PostgreSQL em região nacional | Exemplo aprovado da linha |
| Banco do serviço de notas | Dados, banco de serviço novo | SQL, um banco por serviço e região nacional | PostgreSQL em região nacional | Exemplo aprovado da linha |
| Evento de nota, que atende a nota em até 10 minutos (R7) | API e integração, mensageria | Tópico com retenção e contrato AsyncAPI | Kafka ou compatível, RabbitMQ | Exemplos aprovados da linha |
| Camada anticorrupção | Sem linha no recorte | Não há | Candidato a levantar | O recorte e o dossiê não trazem produto |
| Observabilidade | Infraestrutura, observabilidade | OpenTelemetry | Coletores compatíveis com OpenTelemetry | Exemplo aprovado da linha |

React Native e React para web ficam fora das seis linhas do recorte, e por isso a resposta “sem linha no recorte, candidato a levantar” é aceita para os três blocos de interface. O núcleo transacional COBOL sob CICS permanece e não recebe candidato. A comparação pelos seis critérios é feita neste exercício só para o provedor de identidade, e para os demais blocos a lista acima é o ponto de partida.

Duas linhas valem para todos os contêineres novos, a de infraestrutura como código, que descreve a infraestrutura em arquivos versionados e aprova Terraform, AWS CDK e Bicep, e a de observabilidade, que mede e registra o que o serviço faz em operação, porque toda implantação e toda operação passam por elas, e por isso nenhuma equipe pode dispensá-las. As demais dependem do que o serviço faz: só quem autentica usa a linha de identidade, só quem expõe interface usa a de exposição, só quem publica evento usa a de mensageria e só quem guarda dado usa a de banco.

#### Classificação das tecnologias da linha de base

Para decidir a cor de cada tecnologia, o arquiteto lê o dado da linha de base e o recorte do modelo técnico. O COBOL sob CICS não aparece no recorte e o dossiê não traz plano de migração para ele, de modo que a permanência dele se explica pelo contrato de manutenção, que vale até 30/09/2027.

| Tecnologia | Cor | Justificativa |
| --- | --- | --- |
| JSF 1.2 e EJB 2.0 | Vermelho | 410.000 linhas de 2007 a 2009 sobre servidor sem suporte do fornecedor desde 2018, com 220 telas em quatro aplicações que precisam de plano de migração |
| Oracle 12c Release 2 | Âmbar | O recorte só aceita Oracle em projeto novo com um registro de decisão arquitetural (ADR) de desvio, que justifica o uso de tecnologia fora do padrão, e os 11 TB e as 740 tabelas seguem em uso, com suporte estendido encerrado em 31/03/2022 |
| Acesso direto ao banco | Vermelho | 2.300 pontos de código contornam as transações do CICS e impedem a extração por partes |
| COBOL sob CICS | Vermelho em projeto novo, com permanência por contrato | Manutenção sob contrato exclusivo até 30/09/2027, com 6 especialistas e 2 aposentadorias previstas para 2027 |
| Diretório corporativo | Âmbar | A autenticação de todos os perfis por LDAP, protocolo de consulta ao diretório de usuários, de forma síncrona e com tempo limite de 10 s, permanece até o último portal migrar para o provedor de identidade |
| Arquivo posicional sem versão | Vermelho | O arquivo posicional grava cada campo em posições fixas da linha, e a mudança de layout causou o incidente de 09/07/2026, com 61.400 lançamentos de nota que não chegaram ao ambiente virtual |

Entre as vermelhas, continuam em uso e só ficam sob plano de migração documentado o JSF e o EJB (as 220 telas ainda atendem os usuários), o acesso direto ao banco (os 2.300 pontos ainda existem no código Java) e o arquivo posicional (o lote de exportação de notas ainda o utiliza).

#### Matriz de seleção do provedor de identidade

A Universidade ACME compara três formas de obter o serviço de identidade. O dossiê informa o que ele deve cumprir, mas não apresenta produtos, contratos ou medições de A, B e C. Por isso a matriz registra as verificações necessárias. Nenhuma alternativa recebe uma vantagem sem evidência.

| Alternativa | Aderência ao requisito | Portabilidade |
| --- | --- | --- |
| A, instalado e operado pela equipe | Confirmar OpenID Connect (R8), processamento nacional de dados, cópias e suporte (R14), teste de carga para o pico (R6) e capacidade de operação para o R12 | Verificar instalação e recuperação nos dois provedores aprovados, exportação de dados e esforço de migração. A confirmar |
| B, serviço de terceiro | Pedir documentação de OpenID Connect (R8), contrato e locais de processamento (R14), limites de capacidade (R6) e acordo de disponibilidade (R12) | Verificar exportação, substituição por outro serviço e mudanças necessárias nas aplicações. A confirmar |
| C, gerenciado da nuvem | Pedir documentação de OpenID Connect (R8), locais de processamento de todos os dados (R14), quotas e teste de carga (R6), acordo e desenho de disponibilidade (R12) | Verificar como substituir o serviço no outro provedor aprovado, incluindo migração de usuários, credenciais e configuração. A confirmar |

Os outros quatro critérios ficam sem valor, porque o dossiê não traz dado sobre eles, e por isso o caderno registra o que precisa ser levantado antes da comparação.

| Critério | Dado que falta e precisa ser levantado |
| --- | --- |
| Maturidade | Tempo em produção e estabilidade da interface entre versões de cada produto |
| Suporte | Quem responde pela falha e em que prazo, entre fornecedor, comunidade ou equipe |
| Custo total de propriedade | Licença ou assinatura, operação, treinamento e custo de saída |
| Competência da equipe | Quantas pessoas conhecem o produto e o protocolo, dado que o dossiê não registra para identidade |

Escolha uma das regras abaixo. Ela só elimina uma candidata quando há evidência de descumprimento. Sem documento ou medição, registre a pendência e peça comprovação. A, B e C podem atender ou falhar, dependendo da oferta concreta.

| Restrição | Regra de eliminação | Documento que comprova |
| --- | --- | --- |
| R8, lido como exigência do protocolo aberto OpenID Connect | A alternativa cujo produto não implementa o protocolo | Declaração de conformidade do produto com o OpenID Connect |
| R14, nenhum dado pessoal de aluno fora do território nacional | A alternativa que processa dado fora do território nacional | Cláusula contratual da região de processamento e relação de regiões do provedor |
<!--/gabarito-->
<!--/ex-->

<!--ex n=18 titulo="Plataforma escolhida e zona de pouso"-->
<!--campos-->
- **Plataformas candidatas e ferramentas:** indique duas plataformas capazes de concretizar o estilo recomendado no exercício 10 e liste as ferramentas concretas de cada uma.
- **Comparação pelos critérios com dado:** para aderência ao requisito, custo total de propriedade, competência da equipe e portabilidade, diga qual plataforma atende melhor, ou se empatam, explicando por que em uma linha.
- **Dado que falta em maturidade e suporte:** escreva qual informação falta nesses dois critérios e quem poderia fornecê-la, sem dar valor às plataformas.
- **Plataforma escolhida:** escolha uma das duas e justifique pela convivência com o sistema antigo.
- **Pilar de cada elemento da zona de pouso:** ligue cada elemento do diagrama ao pilar da zona de pouso que ele realiza.
- **Etiquetas que faltam:** para cada recurso da tabela, diga quais das quatro etiquetas obrigatórias (projeto, ambiente, time e centro de custo) estão ausentes.
- **Requisito da conta de segurança e registros:** diga em uma linha qual requisito justifica a existência dessa conta.
<!--/campos-->
<!--gabarito-->
#### Plataformas candidatas para o estilo escolhido

O estilo de referência vem do exercício 10, eventos na borda com o núcleo COBOL preservado, mas quem recomendou outro estilo naquele exercício escolhe candidatas coerentes com o dele. Para o estilo de eventos, duas plataformas servem, e cada uma se descreve pelas ferramentas que a compõem.

| Plataforma candidata | Ferramentas |
| --- | --- |
| Plataforma orientada a eventos | Apache Kafka como fluxo de eventos, Kafka Streams para processamento contínuo, Apache Camel como mediador de integração e gateway de API, que é a porta de entrada das chamadas |
| Plataforma de microsserviços, variante Java | Spring Boot, Spring Cloud Config, Spring Cloud Gateway, Keycloak para identidade, Kubernetes, Docker, Kafka como barramento de eventos, Prometheus, Grafana e OpenTelemetry na observabilidade |

#### Quadro comparativo e plataforma escolhida

O quadro usa só o dado que o dossiê traz. O orçamento de R$ 6,2 milhões e o licenciamento Oracle pesam do mesmo modo nas duas plataformas, então o desempate vem da competência da equipe.

| Critério | Leitura |
| --- | --- |
| Aderência ao requisito | Empate. As duas operam em um dos dois provedores de nuvem aprovados (R4), e o desempate quanto às 5.800 sessões simultâneas (R6) exige um teste de carga que o dossiê não registra |
| Custo total de propriedade | Empate. O orçamento de R$ 6,2 milhões e o licenciamento Oracle por núcleos físicos pesam igualmente enquanto o banco compartilhado existir |
| Competência da equipe | Microsserviços na variante Java, porque a camada web tem 9 pessoas em Java sem escassez, e o dossiê não registra experiência em Kafka nem em Kubernetes, e sem dado de competência em Python ou em TypeScript |
| Portabilidade | Empate. Kafka, Kubernetes e OpenID Connect são abertos, e as decisões precisam ser portáveis entre os dois provedores pré-aprovados |
| Maturidade e suporte | Sem valor. Falta saber há quanto tempo cada plataforma está em produção e quem responde por falhas, o que o fornecedor de cada produto, a comunidade ou a equipe de plataforma pode informar |

A plataforma escolhida é a de microsserviços na variante Java, porque os serviços de matrícula e de notas acessam o núcleo pelas transações CICS existentes, sem alterar programa COBOL, convivem com o Oracle compartilhado e com os lotes noturnos durante o primeiro ciclo e aproveitam a competência Java já existente. A escolha da plataforma orientada a eventos também é aceita quando a justificativa cita a convivência com os lotes e a publicação da nota em até 10 minutos exigida pelo R7.

Os produtos que realizam blocos do catálogo vêm da tabela de ABB para SBB do bloco 1 da Aula 5. Na variante Java, o Spring Boot realiza o serviço de matrícula e o de notas, e o Kafka realiza o evento de nota. O FastAPI e o NestJS, aprovados na mesma linha de exposição de serviços, ficam fora da escolha porque o dossiê registra 9 pessoas em Java e traz competência em Python ou em TypeScript apenas como dado ausente, o que pesa no critério de competência da equipe. O RabbitMQ continua como alternativa para o evento de nota, porque o dossiê não traz dado de volume, de retenção ou de reentrega que o distinga do Kafka, e a escolha do Kafka decorre da plataforma e precisa de confirmação em prova de conceito. O Keycloak aparece entre as ferramentas da variante, mas o provedor de identidade segue aberto entre A, B e C, como no exercício 17. Kubernetes, Docker, Prometheus, Grafana e as demais ferramentas compõem a plataforma do bloco 2 e ficam fora do catálogo, e a observabilidade do catálogo tem como candidato os coletores compatíveis com OpenTelemetry.

#### Zona de pouso: pilares, etiquetas e requisito

A zona de pouso é a base em nuvem, organizada com contas, rede, identidade e regras antes de a solução rodar nela. Cada elemento do diagrama realiza um dos cinco pilares da zona de pouso, e a topologia hub-spoke é uma rede central ligada às redes de cada ambiente, mas alguns não têm pilar próprio, como a organização na nuvem, que só agrupa as contas.

| Elemento do diagrama | Pilar |
| --- | --- |
| Contas de desenvolvimento, homologação e produção | Contas ou assinaturas por ambiente |
| Conta de rede central, rede da produção e ligação híbrida | Rede em topologia hub-spoke |
| Acesso da equipe por perfil, com credencial única | Identidade centralizada |
| Regras aplicadas a todas as contas | Políticas automatizadas |
| Consulta de custo e conta de segurança e registros | Monitoramento com faturamento consolidado |
| Organização da ACME na nuvem | Estrutura que agrupa as contas e recebe as regras, sem pilar próprio |
| Centro de dados da ACME, ligado pela conta de rede central | Rede em topologia hub-spoke pela ligação híbrida, ou sem pilar próprio |
| Recursos da produção | Base comum de infraestrutura como código e etiquetas |

| Recurso | Etiquetas que faltam |
| --- | --- |
| Serviço de matrícula | Centro de custo |
| Banco do serviço de matrícula | Ambiente |
| Gateway de APIs | Projeto |
| Serviço de notas | Nenhuma |
| Fila de eventos de notas | Time e centro de custo |
| Bucket de trilha de auditoria | Time |

A conta de segurança e registros existe por causa do requisito R9, que exige trilha de auditoria de toda leitura de dado pessoal, com retenção de 5 anos, guardada fora da conta de produção. O requisito de região nacional (R14) e o de provedor aprovado (R4) não explicam essa conta.
<!--/gabarito-->
<!--/ex-->

<!--ex n=19 titulo="Segurança dos dados, permissões e ameaças"-->
<!--campos-->
- **Classificação LGPD do ativo:** classifique cada um dos seis ativos em não pessoal, pessoal ou pessoal sensível, conforme o art. 5º da Lei Geral de Proteção de Dados (LGPD).
- **Nível de confidencialidade:** atribua nível baixo, médio ou alto a cada ativo e justifique em uma linha o nível do ativo pessoal sensível.
- **Ativos restritos pelo R14:** diga quais ativos não podem ser processados fora do território nacional, conforme a exigência R14, e qual sistema externo recebe hoje um deles.
- **Células que violam o menor privilégio:** aponte as três células da grade de permissões que dão acesso maior que o necessário, com o perfil e o recurso.
- **Acesso correto:** escreva o acesso correto de cada uma das três células, com a condição quando houver.
- **Categoria STRIDE da ameaça:** classifique cada ameaça, de T1 a T6, em uma das seis categorias do STRIDE, modelo que classifica ameaças em falsificação, adulteração, repúdio, divulgação de informação, negação de serviço e elevação de privilégio.
- **Controle da ameaça:** associe a cada ameaça a letra do controle que a trata.
- **Controle que também atende ao R9:** indique qual dos seis controles também atende ao requisito de trilha de auditoria (R9).
<!--/campos-->
<!--gabarito-->
#### Classificação dos ativos de dado

Todo ativo ligado a um aluno identificado é dado pessoal, e só o laudo, por tratar de saúde, é pessoal sensível, conforme o art. 5º da LGPD. O nível de confidencialidade é de referência, então qualquer nível com justificativa é aceito, exceto o do laudo e o dos dados socioeconômicos de bolsa, que precisam ser altos.

| Ativo | Classificação LGPD | Confidencialidade | Justificativa |
| --- | --- | --- | --- |
| A1, nota | Pessoal | Média | Informação ligada a aluno identificado, art. 5º, I |
| A2, histórico escolar | Pessoal | Alta | Reúne identificação e todo o percurso acadêmico, e a emissão tem valor documental |
| A3, CPF | Pessoal | Alta | Identificador único, que pode ser usado em fraude de identidade |
| A4, dados socioeconômicos de bolsa | Pessoal | Alta | Revelam renda e situação familiar e não constam da lista do art. 5º, II |
| A5, laudo de necessidade educacional específica | Pessoal sensível | Alta | Dado referente à saúde, art. 5º, II, cuja violação expõe o titular a discriminação |
| A6, oferta de turmas | Não pessoal | Baixa | Informação institucional, sem vínculo a pessoa natural |

A exigência de dado pessoal de aluno em território nacional (R14) impede o processamento fora do país de A1 a A5, e só a oferta de turmas fica livre. O sistema externo do diagrama do exercício 16 que recebe hoje um desses ativos é o ambiente virtual de aprendizagem, que recebe a nota consolidada no lote das 05h10. O dossiê não registra a região de processamento do fornecedor do ambiente virtual, e por isso essa verificação fica como lacuna a conferir no contrato.

#### Grade de permissões corrigida

Três células concedem mais acesso do que o trabalho exige, o que contraria o princípio do menor privilégio, pelo qual cada perfil recebe só o acesso de que precisa. Na grade, L significa leitura. As demais têm necessidade de negócio no dossiê, porque o aluno que grava a própria matrícula pelo telefone (requisito R1, renovação pelo celular) e a secretaria acadêmica que lê e grava matrícula e histórico para o ajuste de vaga e a emissão.

| Perfil e recurso | Problema | Acesso correto |
| --- | --- | --- |
| Aluno, nota consolidada | Permite gravar nota | L, somente a própria |
| Professor, matrícula | Lê a matrícula de todas as turmas | L, nas turmas que leciona |
| Ambiente virtual de aprendizagem, nota consolidada | Permite gravar nota consolidada | L |

#### Ameaças na fronteira do aplicativo do aluno

Cada ameaça pertence a uma categoria do STRIDE e é tratada por um dos seis controles, o que mostra onde o desenho precisa de defesa.

| Ameaça | Categoria STRIDE | Controle |
| --- | --- | --- |
| T1, dados do pedido lidos na rede | Divulgação de informação | (c) criptografia em trânsito e em repouso |
| T2, senha de outro aluno | Falsificação de identidade | (d) autenticação forte por OpenID Connect |
| T3, milhares de pedidos por segundo | Negação de serviço | (a) limite de taxa e reserva de capacidade |
| T4, aluno nega o cancelamento | Repúdio | (e) registro de auditoria imutável |
| T5, parâmetro trocado para executar ajuste de vaga | Elevação de privilégio | (b) autorização por papel no serviço de matrícula |
| T6, lista de turmas alterada no caminho | Adulteração | (f) assinatura e verificação de integridade |

O controle que também atende ao requisito de trilha de auditoria (R9) é o (e), registro de auditoria imutável, porque ele guarda o autor e o horário de cada acesso. A retenção de 5 anos exigida pelo R9 é um parâmetro a configurar nesse controle.
<!--/gabarito-->
<!--/ex-->

<!--ex n=20 titulo="ADR de plataforma e lacunas de provisão"-->
<!--campos-->
- **Título, estado e data:** escreva o título do ADR, o estado (proposto) e a data do registro.
- **Contexto:** descreva a situação que levou à decisão, citando pelo título o ADR de estilo do exercício 12.
- **Alternativas:** transporte o quadro comparativo do exercício 18, com as plataformas avaliadas pelos seis critérios do exercício 17.
- **Forças:** liste as pressões que pesam na escolha, com pelo menos três critérios de seleção e uma dimensão de dependência de fornecedor, cada uma com o dado do caso.
- **Decisão:** nomeie a plataforma escolhida e ligue a justificativa às forças.
- **Consequências:** escreva ao menos uma consequência positiva, uma negativa e uma neutra, considerando os achados de segurança do exercício 19.
- **Evidências:** diga o que sustentaria a escolha e onde poderia ser reproduzido, nomeando a evidência desejável que não existe.
- **Revisão:** escreva um gatilho observável, ligado à convivência com o núcleo COBOL sobre CICS, que indique a hora de reavaliar a plataforma.
- **Tipo da lacuna de provisão:** classifique cada um dos seis itens da definição tecnológica como lacuna nova, substituição, modificação ou remoção, com o dado da coluna de situação.
- **Lacuna que reduz custo recorrente:** indique qual item reduz custo recorrente já registrado nos dados operacionais e cite o dado.
<!--/campos-->
<!--gabarito-->
#### ADR de plataforma

O ADR de plataforma usa os dez campos do ADR de estilo e se apoia nos exercícios anteriores: o contexto cita o ADR de estilo que o aluno escreveu no exercício 12, para o qual a referência adota a arquitetura orientada a eventos na borda com o núcleo preservado, e as alternativas trazem o quadro do exercício 18. Os valores de gatilho abaixo são propostas de referência, sem fonte no dossiê, por isso qualquer gatilho observável ligado à convivência com o núcleo é aceito.

| Campo | Conteúdo |
| --- | --- |
| Título, estado e data | ADR de plataforma, escolha da plataforma de microsserviços na variante Java. Estado proposto. Data a definir pelo arquiteto, no dia do registro |
| Contexto | O ADR de estilo, adoção de arquitetura orientada a eventos na borda com o núcleo preservado, fixou o estilo. Falta escolher a plataforma que o concretiza, com o núcleo COBOL sobre CICS em operação durante toda a transição |
| Alternativas | A plataforma orientada a eventos e a de microsserviços na variante Java, avaliadas pelos seis critérios no quadro da seção anterior, com empate em aderência, custo e portabilidade e vantagem de microsserviços em competência da equipe. Dentro da variante Java, FastAPI e NestJS, também aprovados na linha de exposição de serviços, ficam fora da escolha porque o dossiê registra 9 pessoas em Java e traz competência em Python ou em TypeScript apenas como dado ausente, e o RabbitMQ segue como alternativa ao Kafka até a prova de conceito |
| Forças | Aderência ao requisito, com as 5.800 sessões simultâneas (R6) e a nota em até 10 minutos (R7). Competência da equipe, com 9 pessoas na camada Java sem escassez. Portabilidade, com dois provedores aprovados e decisões portáveis entre eles. Dependência de fornecedor em duas dimensões: a interface proprietária, pelo conector transacional do CICS com tempo limite de 30 s, e as habilidades da equipe, pelos 6 especialistas COBOL com 2 aposentadorias em 2027. O dossiê não registra ferramenta de observabilidade, e isso fica como lacuna |
| Decisão | Adotar a plataforma de microsserviços na variante Java, com Spring Boot nos serviços de matrícula e de notas e Kafka como barramento de eventos, porque aproveita a competência Java existente e convive com o núcleo pelas transações CICS atuais |
| Consequências | Positiva: a camada Java existente opera a plataforma, e a grade de permissões corrigida entra como requisito dos serviços novos. Negativa: as 9 pessoas da camada Java precisam aprender Kafka e Kubernetes, porque o dossiê não registra experiência com essas ferramentas, o que torna necessário treinar a equipe. Neutra: a ACME passa a monitorar mais peças, como o barramento de eventos e os serviços novos, e a equipe existente assume esse trabalho. Como consequências de implementação entram o registro de auditoria imutável, que atende a trilha exigida pelo R9, e a identidade por OpenID Connect, que atende os padrões abertos do R8 |
| Evidências | Desejáveis e inexistentes: um teste de carga com 5.800 sessões em ambiente a criar. Disponível: uma prova de conceito de publicação de nota contra uma transação CICS de teste, reproduzível em homologação, único ambiente além de produção |
| Revisão | Reabrir quando o tempo limite de 30 s do conector for atingido com a plataforma em operação, quando o percentil 95 do intervalo entre lançamento e chegada da nota ao ambiente virtual passar de 10 minutos por duas semanas seguidas, ou ao se aproximar 30/09/2027, fim da exclusividade da fábrica |

#### Lacunas de provisão da definição tecnológica

Para medir o tamanho do trabalho, cada item da definição tecnológica considerada se compara com o que a linha de base já oferece, e o resultado cai em um de quatro tipos: a lacuna é nova quando o serviço não existe, é substituição quando um serviço existente dá lugar a outro, é modificação quando o existente precisa mudar e é remoção quando ele deixa de existir.

| Item da definição tecnológica | Tipo | Justificativa pela situação atual |
| --- | --- | --- |
| Provedor de identidade com OpenID Connect | Nova | Existe só o diretório por LDAP, e nenhum provedor implementa os padrões abertos de identidade exigidos pelo R8 |
| Troca de notas em até 10 minutos | Substituição | O lote das 05h10 por arquivo posicional dá lugar à publicação a cada lançamento, como pede o requisito R7 de 10 minutos |
| Autenticação dos portais pelo provedor de identidade | Modificação | O diretório continua existindo atrás do provedor e passa a ser reconfigurado como fonte de identidade |
| Acesso ao núcleo por camada anticorrupção | Remoção | Os 2.300 pontos de acesso direto da camada Java ao banco deixam de existir, e a camada anticorrupção, que traduz as chamadas ao núcleo, passa a ser o único caminho |
| Capacidade para 5.800 sessões | Modificação | A camada web e o CICS existem e precisam de capacidade ampliada, e em 04/02/2026 o limite de tarefas concorrentes foi atingido |
| Observabilidade de ponta a ponta | Nova | O dossiê não registra ferramenta de observabilidade |

Para o custo recorrente, as respostas mais defensáveis são o acesso ao núcleo por camada anticorrupção e a troca de notas. Os dados operacionais registram o custo anual por contrato, com sustentação de R$ 3,60 milhões, pessoal interno de R$ 2,79 milhões e licenciamento Oracle de R$ 2,10 milhões, e não trazem o custo do reprocessamento manual do incidente de 09/07/2026, então quem responde precisa declarar que esse valor não consta. A remoção dos 2.300 acessos diretos reduz o esforço de sustentação dos 15 internos e da fábrica, e a troca de notas elimina o reprocessamento manual dos 61.400 lançamentos. Qualquer das duas escolhas vale, desde que cite o dado do dossiê.
<!--/gabarito-->
<!--/ex-->
