---
secao: 2
titulo: Partes interessadas
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| Para que serve | As decisões de um projeto dependem de pessoas, e na ACME a Reitora quer resultado em 12 meses, o Diretor Financeiro teme pagar o legado e a nuvem no mesmo ano e o Gerente de sustentação da fábrica teme perder o contrato. Esta seção registra quem são essas pessoas, o que cada uma espera e teme e como o arquiteto vai lidar com cada uma, e assim os conflitos aparecem cedo. |
| Pergunta que responde | Quem precisa participar das decisões e onde os interesses entram em conflito? |
| O que você escreve | Você monta primeiro uma tabela com o que cada pessoa ou grupo quer, o que teme e como o arquiteto vai tratá-lo: envolver nas decisões, consultar ou apenas manter informado. Depois escreve os pontos de vista de cada grupo, que são as preocupações que o desenho precisa mostrar, e a declaração de escopo, que diz o que muda no primeiro ciclo, o que fica como está e por que cada item ficou de fora. |
| Vem de onde | Da seção 1 e do mapa de atores do dossiê, que dizem quem são as pessoas envolvidas no projeto. |
| Quando se preenche | Você preenche esta seção na Aula 2, no exercício 8. |
<!--/orientacao-->


<!--ex n=8 titulo="Partes interessadas, pontos de vista e escopo do primeiro ciclo"-->
<!--campos-->
- **Categoria:** diga a que categoria de parte interessada cada um dos oito papéis pertence, entre as nove apresentadas no bloco 4, e indique qual papel exerce o patrocínio do negócio.
- **Papel que representa a categoria:** para cada uma das nove categorias, escreva o papel do mapa de atores que a representa. Se nenhum papel serve, deixe a categoria sem representante.
- **Risco da ausência:** nas categorias sem representante, explique o que pode dar errado no processo quando ninguém fala por elas.
- **Preocupação principal:** para cada um dos três papéis escolhidos, escreva a principal preocupação, partindo do que o papel teme.
- **Critério de seleção:** diga o que entra no recorte da arquitetura que o papel recebe, ou seja, quais partes do desenho interessam a ele.
- **Estrutura do artefato:** diga em que formato o documento é entregue ao papel, como uma tabela, um fluxo ou uma lista.
- **Forma de apresentação:** diga como a informação é mostrada ao papel, por exemplo lado a lado com outro dado ou com marcações.
- **Muda ou permanece:** para cada um dos dez elementos da declaração de escopo, diga se ele muda ou fica como está nos 12 meses do primeiro ciclo.
- **Origem da exclusão:** para cada elemento que permanece, diga qual restrição, contrato ou decisão de governança o manteve fora da mudança.
<!--/campos-->
<!--gabarito-->
#### Categoria de cada papel

A Reitora quer resultado em 12 meses, o Diretor Financeiro teme pagar duas vezes e o Gerente de sustentação teme perder o contrato. Para saber como falar com cada um, o arquiteto enquadrou os oito papéis nas nove categorias de parte interessada, e os papéis que acumulam funções aparecem com uma observação.

| Papel | Categoria | Observação |
| --- | --- | --- |
| Reitora | Donos do negócio e gestores seniores | Exerce o patrocínio do negócio |
| Pró-Reitora de Graduação | Donos do negócio e gestores seniores | Responde pelo processo acadêmico afetado e tem atores de negócio sob sua responsabilidade |
| Diretor de TI | Arquitetura corporativa e subdomínios | Também participa do desenho, e esse acúmulo de papéis precisa ser declarado |
| Diretor Financeiro | Donos do negócio e gestores seniores | Decide sobre o desembolso, e não sobre o desenho |
| Gerente de sustentação da fábrica | Fornecedores de produto e serviço | Tem interesse comercial contrário à internalização do conhecimento do núcleo |
| Coordenadora de Educação a Distância | Usuários finais e atores de negócio | Opera o processo afetado |
| Encarregada de proteção de dados | Reguladores e entidades setoriais | Função de conformidade, que responde dentro da instituição por uma exigência vinda de fora |
| Representação discente | Clientes e usuários dos serviços | Recebe o serviço afetado |

A patrocinadora de negócio é a Reitora, porque tem a autoridade sobre os R$ 6,2 milhões, tomou a decisão de 12/03/2026 que fechou duas alternativas e responde pelo resultado na avaliação regulatória.

#### Categorias sem representante

Depois de classificar os papéis, o arquiteto fez o caminho inverso e perguntou quem fala por cada categoria. Duas categorias ficaram sem ninguém, e a segunda tabela mostra o que isso custa ao processo.

| Categoria | Papel do mapa de atores que a representa |
| --- | --- |
| Donos do negócio e gestores seniores | Reitora, Pró-Reitora de Graduação e Diretor Financeiro |
| Patrocinador de negócio | Reitora |
| Usuários finais e atores de negócio | Coordenadora de Educação a Distância |
| Clientes e usuários dos serviços | Representação discente |
| Arquitetura corporativa e subdomínios | Diretor de TI, que acumula esse papel porque a ACME não tem uma arquitetura corporativa formal no mapa |
| Participantes do desenho | Diretor de TI |
| Participantes da implantação | Sem representante |
| Fornecedores de produto e serviço | Gerente de sustentação da fábrica |
| Reguladores e entidades setoriais | Sem representante externo, porque a Encarregada de proteção de dados fala só pela instituição e o órgão que conduz a avaliação do curso não aparece no mapa |

| Categoria sem representante | Risco da ausência |
| --- | --- |
| Participantes da implantação | O desenho pode sair sem quem o construa e o sustente depois da internalização, e a operação só recusa o que foi desenhado quando já é tarde para mudar |
| Reguladores e entidades setoriais | A exigência externa chega depois da decisão, quando o custo de mudar o desenho já é alto |

#### Pontos de vista de três papéis

O Diretor Financeiro, a Pró-Reitora e o Gerente de sustentação olham para o mesmo sistema com medos diferentes, e por isso cada um recebe um recorte próprio da descrição de arquitetura. A preocupação principal de cada um vem da coluna O que teme do mapa de atores.

| Papel | Preocupação principal | Critério de seleção | Estrutura do artefato | Forma de apresentação |
| --- | --- | --- | --- | --- |
| Diretor Financeiro | Pagar o legado e a nuvem no mesmo exercício | Componentes com custo e contrato associados | Tabela de desembolso por exercício | Comparação com o plano plurianual já provisionado |
| Pró-Reitora de Graduação | Repetir o incidente na janela de matrícula e prorrogar de novo o prazo | Componentes que estão no caminho crítico da matrícula | Fluxo do processo com os pontos de falha marcados | Duas versões comparáveis, a atual e a pretendida |
| Gerente de sustentação da fábrica | Perder receita e escopo com a internalização do conhecimento do núcleo | Programas sob contrato e interfaces afetadas | Lista de programas com as chamadas que mudam | Marcação do que muda antes e depois de 30/09/2027 |

#### Declaração de escopo do primeiro ciclo

Para o primeiro ciclo caber nos R$ 6,2 milhões e nos 12 meses, o arquiteto separou o que a mudança toca do que ela deixa como está, e anotou quem decidiu cada exclusão para que ninguém a reabra sem saber de onde veio. A correção do dado cadastral de aluno (E10) muda porque a Aula 1 decidiu, na decisão D5, passá-la da equipe de sustentação à Secretaria Acadêmica.

| Código | Elemento | Muda ou permanece | Origem da exclusão |
| --- | --- | --- | --- |
| E1 | Integração de notas e turmas com o ambiente virtual de aprendizagem | Muda, desde que a Reitoria aprove o plano superior do ambiente virtual, que traz as interfaces de programação | Não se aplica |
| E2 | Ambiente virtual de aprendizagem | Permanece | Restrição RT2, decisão da Reitoria de 12/03/2026 |
| E3 | ERP financeiro | Permanece | Restrição RT2, decisão da Reitoria de 12/03/2026 |
| E4 | Programas COBOL do núcleo acadêmico | Permanece | Restrição RT6, contrato de sustentação até 30/09/2027 |
| E5 | Portal do aluno, na renovação de matrícula pelo telefone celular | Muda | Não se aplica |
| E6 | Autenticação de alunos e professores por padrões abertos | Muda | Não se aplica |
| E7 | Trilha de auditoria de leitura de dado pessoal de aluno | Muda | Não se aplica |
| E8 | Contrato de capacidade do mainframe | Permanece | Contrato de capacidade, com piso de volume, até 31/12/2028 |
| E9 | Região de implantação dos componentes em nuvem | Permanece | Restrição RT5, parecer do Jurídico de 28/04/2026, que exige território nacional |
| E10 | Responsabilidade pela correção de dado cadastral de aluno | Muda | Não se aplica |
<!--/gabarito-->
<!--/ex-->
