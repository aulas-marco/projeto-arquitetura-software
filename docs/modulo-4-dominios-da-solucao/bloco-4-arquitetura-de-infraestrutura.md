# Representação de modelos e C4

Este bloco fecha a aula tratando de uma pergunta anterior às duas decisões já registradas, como representar o sistema de forma que estilo e plataforma fiquem visíveis num modelo, não apenas descritos em texto.

## Antes de começar

- [Modelo C4](../referencia/glossario.md#modelo-c4)

## Conceito

### Nível 2, diagrama de contêineres

O **diagrama de contêineres** detalha os principais contêineres que compõem o sistema, com suas responsabilidades e com a forma como interagem entre si e com os sistemas externos. Contêineres representam as aplicações, bancos de dados ou outros serviços que compõem o sistema, cada um com responsabilidade específica e tecnologia declarada. Sistemas externos e relações continuam presentes, com o mesmo significado do nível anterior.

![Diagrama de contêineres com o sistema principal decomposto em aplicação web, API e banco de dados, cada um com sua tecnologia, ligados entre si e ao sistema externo por relações rotuladas com protocolo.](../assets/images/c4-exemplo-conteineres.png)

*Diagrama de contêineres genérico, com a decomposição interna do sistema e a tecnologia de cada contêiner. Fonte: material base do professor.*

O roteiro aqui tem quatro etapas. Identifique os sistemas externos com que o sistema principal interage diretamente, que são os mesmos do nível 1. Defina os contêineres principais, como aplicação de interface, serviço de retaguarda ou banco de dados. Descreva as relações entre contêineres e entre eles e os sistemas externos, especificando protocolo e direção. Acrescente a cada contêiner uma descrição curta da responsabilidade e da tecnologia usada.

No nível de contêineres, o mesmo sistema se decompõe sem que os atores e os sistemas externos mudem.

```mermaid
graph TD
    PAC["Paciente"]
    REC["Recepção da clínica"]

    subgraph AGE["Sistema de agendamento odontológico"]
        APP["Aplicativo do paciente"]
        WEB["Painel da recepção"]
        API["Serviço de agenda"]
        BD[("Banco de agendamentos")]
    end

    CONV["Operadora de convênio"]
    SMS["Serviço de mensagens"]

    PAC --> APP
    REC --> WEB
    APP -->|"HTTPS"| API
    WEB -->|"HTTPS"| API
    API --> BD
    API -->|"HTTPS"| CONV
    API -->|"HTTPS"| SMS
```

Note que o par de sistemas externos, operadora de convênio e serviço de mensagens, é o mesmo nos dois níveis. Mudar esse conjunto entre um nível e outro quebra o princípio da coerência, e vale conferir isso sempre que os dois diagramas forem desenhados em momentos diferentes.

### Um exemplo completo nos dois níveis

O par de diagramas abaixo modela um sistema de internet banking, primeiro no nível de contexto e depois no de contêineres. Ele interessa a esta disciplina por um detalhe, o sistema mainframe bancário aparece como sistema externo, fora da caixa do sistema modelado.

![Diagrama de contexto do sistema de internet banking, com o cliente bancário como pessoa, o sistema de internet banking como sistema modelado, e o sistema mainframe bancário e o sistema de e-mail como sistemas externos, ligados por relações rotuladas.](../assets/images/c4-banking-contexto.png)

*Nível de contexto do sistema de internet banking, com o mainframe tratado como sistema externo. Fonte: material base do professor.*

![Diagrama de contêineres do mesmo sistema de internet banking, decomposto em aplicação web, aplicação de página única, aplicativo móvel, aplicação de API e banco de dados, cada um com sua tecnologia, mantendo o mainframe e o sistema de e-mail como sistemas externos.](../assets/images/c4-banking-conteineres.png)

*Nível de contêineres do mesmo sistema, com a tecnologia declarada em cada contêiner e os mesmos dois sistemas externos do nível anterior. Fonte: material base do professor.*

A decisão de colocar o mainframe fora da caixa é uma decisão de escopo, não uma regra do modelo. Ali, o banco tratou o mainframe como sistema de terceiro, mantido por outra equipe, com o qual o internet banking apenas conversa. Na ACME, o núcleo COBOL sobre CICS é mantido pela mesma organização e faz parte do sistema acadêmico, então ele fica dentro da caixa, como contêiner. O critério é a fronteira de responsabilidade sobre o sistema, não a idade nem a tecnologia do componente.

## Uso pelo arquiteto

O arquiteto escolhe o nível pela audiência, não pela quantidade de informação que gostaria de mostrar. Diante de uma parte interessada de negócio, que decide sobre escopo e sobre relação com terceiros, o diagrama de contexto é suficiente e o de contêineres é ruído, porque ninguém naquela mesa vai decidir sobre tecnologia interna. Diante da própria equipe técnica, que precisa saber onde um requisito será implementado, o diagrama de contexto é vago demais e o de contêineres é o mínimo útil.

O erro simétrico também existe. Levar o diagrama de contêineres a uma reunião de orçamento costuma deslocar a discussão para escolhas de tecnologia que não estavam em pauta, e levar o diagrama de contexto a uma reunião técnica costuma terminar com alguém desenhando o nível seguinte no quadro branco.

## Exercício 16

Este exercício é realizado fora do horário de aula, como atividade de aplicação do conceito apresentado neste bloco ao caso da instituição fictícia ACME.

A ACME é a universidade privada brasileira em modernização incremental do sistema acadêmico. O núcleo transacional em COBOL sobre o monitor CICS concentra as regras acadêmicas, uma camada web em JSF e EJB serve os portais de acesso, um banco Oracle guarda o estado, e as integrações com o ERP financeiro e com o ambiente virtual de aprendizagem são resolvidas por arquivo, em lote noturno, conforme a [arquitetura de linha de base](../caso-acme/linha-de-base.md).

1. Desenhe o diagrama de contexto da ACME, identificando o sistema acadêmico como caixa única, os atores humanos e os sistemas externos, seguindo as cinco etapas do roteiro apresentado no Conceito.
2. Desenhe o diagrama de contêineres, decompondo o sistema acadêmico nos contêineres que a linha de base descreve, com a tecnologia de cada um, seguindo as quatro etapas do roteiro. Mantenha os mesmos sistemas externos que você usou no item 1.
3. Justifique em uma frase por que uma parte interessada de negócio precisaria ver apenas o diagrama do item 1.

Entregue os dois diagramas em Mermaid ou em desenho livre, à sua escolha. Um erro comum no item 1 é detalhar contêiner interno, o que mistura os dois níveis. Se o núcleo COBOL aparecer no diagrama de contexto, o item está no nível errado.

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Brown, S. (n.d.). *The C4 model for visualising software architecture*. https://c4model.com (sítio oficial do modelo C4)
- Mendes, M. (2026b). *Guias de projeto de arquitetura de software* [Material de curso, versão arquivada]. https://github.com/aulas-marco/projeto-arquitetura-software/tree/30f15cd (guias 3.1, 3.2 e 3.3, fonte dos quatro níveis, dos princípios de abstração, dos elementos de cada diagrama, dos dois roteiros de montagem e das três figuras reproduzidas nesta página)

**Material do curso.** Glossário, entrada [modelo C4](../referencia/glossario.md#modelo-c4). Dossiê da instituição fictícia [ACME](../caso-acme/index.md) e [arquitetura de linha de base](../caso-acme/linha-de-base.md).
