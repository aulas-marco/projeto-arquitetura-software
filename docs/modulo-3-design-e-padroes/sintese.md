# Síntese da Aula 3

Esta página fecha o módulo de princípios de design, padrões e registro de decisão com o que precisa permanecer depois da aula, a cadeia da decisão construída nos quatro exercícios, uma autoavaliação e as fontes usadas nos quatro blocos.

## Checklist do que precisa permanecer

- A distinção entre objetivo, requisito, princípio, decisão e elemento lógico, com o papel de cada um na justificativa de uma escolha de desenho
- A anatomia de um princípio de design, com nome, motivação, implicação no desenho e evidência de aplicação, e o teste de perguntar que alternativa o princípio elimina
- A hierarquia do desenho conceitual ao lógico e os cinco passos da transformação, identificar responsabilidades, agrupar por coesão, declarar interfaces e fluxos, aplicar restrições e princípios, e localizar riscos e decisões pendentes
- Os sete estilos arquiteturais descritos pelos mesmos aspectos, com o atributo que cada um favorece, o que prejudica e o anti-padrão que denuncia seu uso inadequado
- A taxonomia de três níveis, estilo arquitetural, padrão arquitetural e padrão de design, com a pergunta que cada nível responde
- Os dez padrões do repertório, cada um com problema, contexto e forças, estrutura mínima, consequência favorável, custo e sinal de uso inadequado
- O template de ADR em dez campos, com o critério de qualidade e o erro frequente de cada um, e a prática de criar um registro novo e marcar o anterior como substituído quando a decisão muda

## Cadeia da decisão

A aula constrói uma única decisão por etapas, e cada etapa consome o produto da anterior.

1. O objetivo de negócio define o resultado pretendido pela solução.
2. O requisito, com as restrições e os cenários de qualidade da Aula 2, torna esse objetivo verificável.
3. O princípio converte requisitos e restrições em regra que orienta um conjunto de decisões, produzido no exercício 9.
4. O estilo organiza o sistema inteiro de modo a sustentar os princípios e os cenários, escolhido no exercício 10.
5. O padrão resolve um problema específico dentro do estilo, com custo declarado, selecionado no exercício 11.
6. A decisão registrada em ADR reúne estilo e padrões com contexto, alternativas, consequências, evidências e gatilho de revisão, escrita no exercício 12.

Um elo ausente nessa cadeia aparece no ADR como força sem origem, alternativa sem comparação ou consequência sem custo, e é por esses três sinais que um registro pode ser revisado por quem não participou da decisão.

## Autoavaliação

As perguntas abaixo são para o aluno responder a si mesmo, sem gabarito público, como verificação de retenção antes da Aula 4.

1. Dado um princípio qualquer, eu indico que alternativa de desenho ele elimina e que evidência mostraria sua aplicação.
2. Eu produzo um esboço lógico em que nenhum elemento nomeia produto, linguagem, provedor de nuvem ou framework.
3. Para dois estilos arquiteturais, eu indico o atributo que cada um favorece, o que prejudica e o anti-padrão típico de cada um.
4. Dado um padrão qualquer do repertório, eu digo em que nível de decisão ele atua e descrevo o sinal de uso inadequado.
5. Eu escrevo um gatilho de revisão de ADR com medida, valor e janela de observação.

## Fontes da aula

As referências seguem o formato APA, 7ª edição. A lista completa está na [bibliografia](../referencia/bibliografia.md) do curso.

- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seções 2.2 e 3.5 a 3.7, base do bloco 1 e da definição de padrão do bloco 3)
- Ford, N., & Richards, M. (2020). *Fundamentals of software architecture*. O'Reilly. (comparação de estilos e distinção entre estilo e padrão)
- Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley. (relação entre estilo e atributo de qualidade)
- Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). *Design patterns: Elements of reusable object-oriented software*. Addison-Wesley. (definição de padrão e padrão Adapter)
- Evans, E. (2003). *Domain-driven design: Tackling complexity in the heart of software*. Addison-Wesley. (Anti-Corruption Layer)
- Fowler, M. (2024, 22 de agosto). *Strangler fig*. martinfowler.com. https://martinfowler.com/bliki/StranglerFigApplication.html (padrão Strangler Fig)
- Richardson, C. (2018). *Microservices patterns*. Manning. (API Gateway, Saga e Transactional Outbox)
- Nygard, M. (2018). *Release it! Design and deploy production-ready software* (2nd ed.). The Pragmatic Programmers. (Timeout, Circuit Breaker e Bulkhead)
- Nygard, M. (2011, 15 de novembro). *Documenting architecture decisions*. Cognitect Blog. https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions (formato de ADR de cinco partes)
- MADR. (2024). *Markdown Architectural Decision Records* (Versão 4.0.0). https://adr.github.io/madr/ (campos do formato MADR)
- Vernon, V. (2013). *Implementing domain-driven design*. Addison-Wesley. (arquitetura hexagonal)
- Hohpe, G., & Woolf, B. (2003). *Enterprise integration patterns: Designing, building, and deploying messaging solutions*. Addison-Wesley. (pipes and filters)
- Mendes, M. (2026a). *Arquitetura de software* [Material de curso]. https://marco-mendes.github.io/arquitetura-software/ (template de ADR e catálogo de padrões)
- Mendes, M. (2026b). *Guias de projeto de arquitetura de software* [Material de curso, versão arquivada]. https://github.com/aulas-marco/projeto-arquitetura-software/tree/30f15cd (guias 1.3 e 2.1)
