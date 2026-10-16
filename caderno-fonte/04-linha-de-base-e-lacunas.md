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

Os cenários do pico e do incidente só são confiáveis se os números que os sustentam estiverem corretos, e esses números vêm dos artefatos da linha de base, os documentos e as medições que descrevem o sistema atual. Quatro dos seis artefatos sustentam os cenários, mas o L3, o prazo de 34 dias úteis, e o L4, o custo de R$ 15,83 milhões, não aparecem em nenhum deles.

| Artefato | Dado que fornece | Efeito de um dado desatualizado |
| --- | --- | --- |
| L6, série de medição de sessões simultâneas e de taxa de erro do portal | A média anual de 815 sessões, o pico de 5.800 e a taxa de erro de 6,3% no pico | A razão de 7,1 e a meta de erro ficariam erradas, e o teste de carga simularia um pico diferente do real |
| L2, registro dos três incidentes graves dos últimos 18 meses | A sequência do incidente de 04/02/2026, com 4h20 de duração e 62% das tentativas com erro | O cenário do incidente trataria uma causa que não aconteceu, e a medida de 260 minutos perderia o ponto de comparação |
| L1, inventário de componentes do sistema acadêmico | O monitor CICS, o limite de tarefas e as camadas que o estímulo atravessa | O campo Artefato apontaria uma parte do sistema que já mudou, e a resposta seria desenhada para o lugar errado |
| L5, contratos de sustentação e de capacidade | O prazo de 30/09/2027 para qualquer alteração no núcleo COBOL | A resposta poderia prever alteração no núcleo sem que o contrato permita, e o tempo limite teria de ficar na camada web |
<!--/gabarito-->
<!--/ex-->
