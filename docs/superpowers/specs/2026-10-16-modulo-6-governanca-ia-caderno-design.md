# Módulo 6, Aula 6: governança, aceleradores de IA e apresentação do caderno

Data: 16/10/2026. Estado: proposta para revisão do Marco.

## Objetivo

Escrever a Aula 6, que fecha a disciplina e o caderno arquitetural da ACME. A aula trata de três assuntos: a governança da mudança, os aceleradores de IA no trabalho do arquiteto e a apresentação do caderno completo. O texto aplica todas as regras de escrita que o Marco fixou durante a construção das Aulas 1 a 5.

## Decisões já tomadas pelo Marco

| Decisão | Origem |
| --- | --- |
| A aula passa de 4 para 3 blocos: Governança, Aceleradores de IA e Apresentação do Caderno. | Resposta à pergunta de estrutura |
| Os exercícios continuam a ser 24. O bloco 1 tem dois exercícios (21 e 22), e os blocos 2 e 3 têm um cada (23 e 24). | Resposta à pergunta sobre exercícios |
| "Aceleradores de IA" significa o uso da IA no processo de arquitetura, como no EAD: modelo como redator e como crítico, tarefas que exigem julgamento humano, verificação em três etapas, dado confidencial em prompt, prompt versionado. | Resposta à pergunta de conteúdo |
| O professor demonstra o caderno completo da ACME na aula. O aluno não apresenta ao patrocinador. | Resposta à pergunta sobre a apresentação |
| A aula tem um único Kahoot, logo depois do intervalo. A primeira metade da aula é de governança. | Mensagem de 16/10/2026 |
| A figura do ciclo ADM do TOGAF ilustra o papel do arquiteto de solução em governar a mudança, com destaque para as fases E, F, G e H. | Mensagem de 16/10/2026 |
| O bloco de inovação e tendências sai do plano. A fonte de tendências estava pendente e o EAD não traz esse tema. | Consequência da estrutura |

## Estrutura da aula

### Grade de tempo

| Horário | Atividade | Duração (min) |
| --- | --- | --- |
| 19h00–19h15 | Questões sobre a Aula 5 | 15 |
| 19h15–20h30 | Bloco 1, governança | 75 |
| 20h30–20h45 | Intervalo | 15 |
| 20h45–20h55 | Kahoot de revisão, com governança e as aulas anteriores | 10 |
| 20h55–21h28 | Bloco 2, aceleradores de IA | 33 |
| 21h28–22h00 | Bloco 3, apresentação do caderno arquitetural | 32 |
| 22h00–22h10 | Encerramento da disciplina | 10 |

A grade vale como proposta. O horário do bloco 1 (75 minutos) é o dobro dos demais porque ele contém dois exercícios e a figura do ciclo ADM.

### Blocos, exercícios e seções do caderno

| Bloco | Tema | Exercício | Seção do caderno | Fonte |
| --- | --- | --- | --- | --- |
| 1 | Governança da mudança: lacunas, roteiro em ondas, desvio arquitetural e mecanismos de controle, com o ciclo ADM do TOGAF (fases E, F, G e H) | 21, lacunas e roteiro em ondas. 22, desvio e mecanismos de governança | 4 (lacunas) e 9 (roteiro e governança) | EAD T-U1V8, T-U3V7 e M-U3V8. Lovatt 5.1 a 5.7, 6.7 e 8.1 a 8.6. TOGAF, fases E a H |
| 2 | Aceleradores de IA | 23, verificar uma saída de IA sobre um artefato do caderno e registrar a assistência | 9 (regras de uso de IA no projeto) | EAD T-U3V5 e M-U3V6. Böckeler, *Exploring generative AI* |
| 3 | Apresentação do caderno arquitetural | 24, conferência final do caderno, com a versão final do resumo e das pendências | 0 e 10 (versões finais) | Caderno completo do EAD e M-U3V8 (os 14 artefatos e o fio do requisito R6) |

### Conteúdo de cada bloco

**Bloco 1, governança.** O bloco abre com a pergunta que a ACME precisa responder antes de gastar o orçamento de R$ 6,2 milhões: o que separa o sistema atual do sistema desenhado, e quem garante que a entrega siga o desenho. Em seguida apresenta a figura do ciclo ADM, redesenhada para o site, e mostra o arquiteto de solução nas fases E (oportunidades e soluções), F (planejamento da migração), G (governança da implementação) e H (gestão da mudança). Cada fase recebe uma situação da ACME. O conteúdo técnico cobre o método de análise de lacunas, a ordem das ondas e o critério de conclusão de cada uma, o desvio arquitetural sob pressão de prazo, os cinco mecanismos contra o desvio, as funções de aptidão e a governança leve. O exercício 21 pede a classificação das lacunas e a ordenação das ondas a partir de artefatos fornecidos. O exercício 22 pede a associação de situações de desvio aos mecanismos de governança.

**Bloco 2, aceleradores de IA.** O bloco parte de uma situação concreta da ACME, um modelo de linguagem que redige o ADR com um cenário de carga já superado, e mostra por que o artefato plausível e errado é o risco central. O conteúdo cobre os casos de uso por fase do processo, os dois modos (redator e crítico), os quatro assistentes do arquiteto, as tarefas que exigem julgamento, a verificação em três etapas (rastreabilidade, checagem contra restrição e revisão por par), a classificação do conteúdo antes de entrar em um prompt e o prompt versionado com o registro da assistência no ADR. O exercício 23 fornece uma saída gerada por IA com erros plantados e pede que o aluno aplique as três verificações e registre a assistência.

**Bloco 3, apresentação do caderno.** O professor percorre o caderno completo da ACME, seção por seção, e mostra o fio que liga o requisito R6 às decisões, aos contêineres, às ondas e aos controles. A aula apresenta os 14 artefatos do ciclo e a regra de rastreabilidade que o caderno cumpre. O exercício 24 fornece o caderno da ACME com pontos de inconsistência (decisão sem requisito de origem, requisito sem decisão, pendência sem responsável) e pede que o aluno marque cada ponto e escreva as versões finais do resumo (seção 0) e das pendências (seção 10).

## Mudanças no sistema do caderno

| Arquivo | Mudança |
| --- | --- |
| `scripts/caderno_registro.py` | `EXERCICIOS` 21 a 24 passam a apontar para os três blocos novos (21 e 22 no bloco 1, 23 no bloco 2, 24 no bloco 3). `PLANO`: 21 preenche as seções 4 e 9, 22 e 23 preenchem a seção 9, 24 preenche as seções 0 e 10. |
| `caderno-fonte/` | Fragmentos de gabarito 21 a 24 nas seções 4, 9, 0 e 10. A orientação da seção 10 deixa de prever "avaliação de uma tendência tecnológica" e passa a prever a conferência final do caderno. |
| `docs/modulo-6-lacunas-e-governanca/` | Três blocos, índice com a seção "Adições no Caderno Arquitetural da Aula 6" e síntese, no formato dos módulos 1 a 5. |
| `docs/cronograma.md`, `docs/index.md`, `docs/caderno/mapa.md`, `docs/caso-acme/artefatos.md` | Textos e tabelas da Aula 6 e do caderno atualizados. |
| `docs/assets/images/` | Figura do ciclo ADM redesenhada em SVG, com texto alternativo e legenda que cite o TOGAF. |
| `docs/referencia/glossario.md` | Verbetes novos: governança de arquitetura, desvio arquitetural, onda de entrega, função de aptidão, ciclo ADM, saída plausível e errada. |
| `mkdocs.yml`, `scripts/validate_content.py`, `tests/` | Navegação com os três blocos e os gabaritos 21 a 24. O validador e os testes passam a cobrir o módulo 6 como cobrem os módulos 2 a 5. |

## Regras de escrita aplicadas a tudo

Estas regras vêm das críticas do Marco nas Aulas 1 a 5 e valem para todo texto novo e para todo gabarito.

1. Cada trecho conta uma pequena história com situação da ACME, tensão, ação e motivo, em frases ligadas por causa e consequência. Texto curto é permitido, texto seco não.
2. O objetivo da seção ou do exercício e a origem dos itens vêm antes do comando. O aluno não conhece o caso, os códigos nem a estrutura do site.
3. Todo código (R6, D5, RT5, L5, E9 e semelhantes) aparece depois do conteúdo dito em palavras. Nenhum título abre com código solto.
4. Um caso particular usado como ilustração é dito como exemplo, com contexto antes dos detalhes.
5. "Componente" sozinho designa peça de TI. No sentido amplo escreve-se "componente da solução", com os tipos entre parênteses. A coluna de tipo se chama "Tipo do componente da solução" e fica logo depois do código.
6. A seção "Uso pelo arquiteto" trata da utilidade da informação: que dúvida ela resolve, quando e como o arquiteto a usa, a quem a leva e o que acontece sem ela.
7. Os exercícios são simples: o enunciado fornece o artefato e o aluno classifica, associa ou responde perguntas curtas.
8. O texto é autocontido. O autor do livro-texto aparece só nas Fontes, e a primeira menção de cada termo técnico o explica.
9. Cada bloco ganha a ficha "No caderno arquitetural". O índice da aula tem a seção "Adições no Caderno Arquitetural da Aula 6". Os gabaritos são cumulativos e recolhíveis, com o que é novo aberto.
10. Sem antítese de efeito, sem idiomas e metáforas da lista do Marco, sem ponto-e-vírgula, no máximo um travessão por parágrafo, média mínima de 14 palavras por frase e parágrafo sem frase de efeito no fim. A grafia é "reuso".
11. Nenhum fato novo entra sem fonte. Respostas de gabarito sem base direta no enunciado, no dossiê ou nos gabaritos do professor são sinalizadas no relatório do agente.
12. A crítica feita sobre um trecho vale para o site inteiro.

## Verificação

- `python3 scripts/gerar_caderno.py --check` sem divergências.
- `python3 scripts/validate_content.py` sem violações, com o módulo 6 incluído.
- Suíte completa de testes e `mkdocs build --strict`.
- Revisão de narrativa e de autocontenção por agentes, em paralelo, depois de cada bloco escrito.
- Captura de tela da figura do ciclo ADM e de uma página de gabarito.

## Pontos em aberto

| Ponto | Situação |
| --- | --- |
| Figura do ciclo ADM | O desenho oficial do TOGAF tem direitos autorais. A proposta é redesenhar o ciclo em SVG e citar o TOGAF. Se o Marco tiver a figura que quer usar, ela substitui o desenho. |
| Edição do TOGAF | O TOGAF ainda não consta da bibliografia conferida do site. A edição precisa ser confirmada antes de a referência entrar. |
| Fonte de IA | O EAD cita Böckeler (martinfowler.com). A data de acesso precisa ser verificada antes de a referência entrar na bibliografia. |
| Grade de horário | A tabela acima é uma proposta. |
| Gabaritos 21 a 24 | Sem gabarito prévio do professor. As respostas serão derivadas do caderno completo do EAD e sinalizadas como tal. |
