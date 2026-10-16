# Síntese da Aula 3

Depois de quatro exercícios, a ACME tem uma decisão de desenho registrada, e esta página fecha a Aula 3 com quatro partes. A primeira é a lista do que o aluno deve reter depois da aula, a segunda é a cadeia da decisão construída nos exercícios, a terceira é uma autoavaliação, e a quarta reúne as fontes usadas nos quatro blocos.

## Checklist do que precisa permanecer

- A distinção entre objetivo, requisito, princípio, decisão e elemento lógico, com o papel de cada um na justificativa de uma escolha de desenho
- A anatomia de um princípio de design, com nome, motivação, implicação no desenho e evidência de aplicação, e o teste de perguntar que alternativa o princípio elimina
- A hierarquia do desenho conceitual ao lógico e os cinco passos da transformação, identificar responsabilidades, agrupar por coesão, declarar interfaces e fluxos, aplicar restrições e princípios, e localizar riscos e decisões pendentes
- Os sete estilos arquiteturais descritos pelos mesmos aspectos, com o atributo que cada um favorece, o que prejudica e o anti-padrão, que é o erro típico de aplicação do estilo e que denuncia seu uso inadequado
- A taxonomia de três níveis, estilo arquitetural, padrão arquitetural e padrão de design, com a pergunta que cada nível responde
- Os dez padrões do repertório, cada um com problema, contexto e forças, estrutura mínima, consequência favorável, custo e sinal de uso inadequado
- O template de ADR em dez campos, com o critério de qualidade e o erro frequente de cada um, e a prática de criar um registro novo e marcar o anterior como substituído quando a decisão muda
- O estado do [caderno arquitetural](../referencia/glossario.md#caderno-arquitetural) ao fim da Aula 3: a seção 6 com os princípios e o esboço lógico, e a seção 7 com a comparação de estilos, os padrões e o primeiro ADR

## Cadeia da decisão

A decisão da ACME não surgiu de uma vez, porque cada etapa da aula usou como ponto de partida o produto da etapa anterior, como mostra a sequência abaixo.

1. O objetivo de negócio define o resultado pretendido pela solução.
2. O requisito, com as restrições e os cenários de qualidade da Aula 2, torna esse objetivo verificável.
3. O princípio converte requisitos e restrições em regra que orienta um conjunto de decisões, produzido no exercício 9.
4. O estilo organiza o sistema inteiro de modo a sustentar os princípios e os cenários, escolhido no exercício 10.
5. O padrão resolve um problema específico dentro do estilo, com custo declarado, selecionado no exercício 11.
6. A decisão registrada em ADR reúne estilo e padrões com contexto, alternativas, consequências, evidências e gatilho de revisão, escrita no exercício 12.

Quem revisa o ADR meses depois, sem ter participado da decisão, reconhece um elo ausente da cadeia por três sinais, a força sem origem (um critério que não vem de nenhum princípio, cenário ou restrição), a alternativa sem comparação e a consequência sem custo.

## Autoavaliação

As afirmações abaixo servem para o aluno conferir o que reteve antes da Aula 4. Ele responde sozinho, porque as perguntas de autoavaliação não têm gabarito. Os exercícios têm, e a seção [Gabaritos](../gabaritos/index.md) mostra o caderno da ACME preenchido a cada exercício, para comparar com o seu.

1. Dado um princípio qualquer, eu indico que alternativa de desenho ele elimina e que evidência mostraria sua aplicação.
2. Eu produzo um esboço lógico em que nenhum elemento nomeia produto, linguagem, provedor de nuvem ou framework.
3. Para dois estilos arquiteturais, eu indico o atributo que cada um favorece, o que prejudica e o anti-padrão típico de cada um.
4. Dado um padrão qualquer do repertório, eu digo em que nível de decisão ele atua e descrevo o sinal de uso inadequado.
5. Eu escrevo um gatilho de revisão de ADR, que é a condição que reabre o registro, com medida, valor e janela de observação, como "se a taxa de erro da matrícula ultrapassar 1% durante uma semana, o registro é reaberto".

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
