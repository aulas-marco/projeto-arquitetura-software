# Caderno arquitetural como fio condutor do curso

**Data:** 16/10/2026

**Estado:** em revisão pelo professor

**Escopo:** definição do caderno arquitetural da ACME como documento que amarra os módulos 1 a 6, com template no módulo 1, indicação da seção preenchida em cada bloco, exercícios orientados ao preenchimento e gabaritos cumulativos. Este documento fixa o desenho e a decomposição em sete partes, listadas na seção 8, e cada parte terá spec e plano próprios.

## 1. Objetivo

O aluno termina a disciplina com um documento de arquitetura da solução preenchido, e não com exercícios isolados. O módulo 1 apresenta o template do caderno com o que vai em cada seção. Cada bloco dos módulos seguintes declara a seção que preenche. Cada exercício pede o preenchimento de campos dessa seção. Cada gabarito é o caderno inteiro, acumulando o resultado dos exercícios anteriores, de modo que o aluno confere o próprio trabalho contra um documento coerente.

Conteúdo sem amarração ao caderno, ou inconsistente com ele, é removido ou alterado, conforme a auditoria da seção 7.

## 2. Decisões do professor

Decisões tomadas em 16/10/2026:

- Os gabaritos ficam no site, em seção própria, abertos desde a publicação. Isso revoga a seção 12.2 de `2026-09-19-estrutura-do-curso-design.md`, que levava o gabarito para fora do site.
- O template do caderno é o caderno pocket do EAD, e o caderno completo do EAD é a fonte de texto dos gabaritos. Os dois ficam em `~/pka/projects/aulas/iec-ead-2026-projeto-arquitetura-solucao/4-caderno/`.
- O material do EAD é de autoria do professor e pode ser reaproveitado sem tratamento de fonte de terceiros, conforme a memória `material-ead-arquitetura-solucao`.
- Cada exercício produz um gabarito, num total de 24 versões cumulativas.

## 3. Fatos verificados

| Fato | Fonte |
| --- | --- |
| O caderno é uma descrição de arquitetura (AD), composta por entregáveis, artefatos e entidades, e a análise de lacunas compara duas ADs, a de linha de base e a alvo | Lovatt (2021, seção 5.1.1), `livro-lovatt.md:3789-3811` |
| O pocket tem dez seções numeradas, precedidas de "A solução em uma página" | `4-caderno/pocket/caderno-pocket-acme.md`, linhas 15 a 221 |
| O caderno completo tem 22 capítulos em três partes e apêndices A a E, montados por `montar.py` com o marcador `{{include:...}}` | `4-caderno/caderno-arquitetural-acme.md:84,986,2146` e `4-caderno/montar.py` |
| O caderno completo coloca a análise de lacunas no capítulo 8, e este curso a trata na Aula 6 | `caderno-arquitetural-acme.md:903` e `docs/cronograma.md` |
| Existem 20 exercícios escritos, de 1 a 20. Os exercícios 21 a 24 só constam do índice da Aula 6, que não tem blocos | `docs/modulo-6-lacunas-e-governanca/index.md` |
| Os exercícios 1 a 4 não produzem artefato de projeto | `docs/caso-acme/artefatos.md`, abertura da seção da Aula 1 |
| O R6 e o R7 do caderno coincidem com os do dossiê do site | `docs/caso-acme/index.md:86-87` |
| A anatomia de bloco é validada em sete seções | `scripts/validate_content.py` e seção 12.1 da spec de estrutura |
| As cinco sínteses afirmam "sem gabarito público" | `docs/modulo-{1..5}-*/sintese.md` |

## 4. Estrutura do caderno

### 4.1 Seções

O template reproduz as dez seções do pocket. Onde o pocket não tem lugar para um exercício do curso, o template acrescenta subseção, e a lista abaixo é a única extensão ao pocket.

| Seção | Conteúdo | Exercícios |
| --- | --- | --- |
| A solução em uma página | Problema, pergunta, decisão central, requisito guia, compromisso aceito e estado | escrita ao fim, revisada a cada aula, fechada no 24 |
| 1. Contexto | Instituição, números, restrições fechadas, respostas excluídas. Subseções acrescentadas: decisões por nível de arquitetura, componentes da solução, papéis, e o mapa das seções do caderno nas fases do processo | 1, 2, 3, 4 |
| 2. Partes interessadas | Papéis, o que querem, o que temem, tratamento, conflitos | 8 |
| 3. Requisitos | Catálogo com tipo, medida e prioridade, cenário de qualidade. Subseção acrescentada: direcionadores de mudança | 5, 6, 7 |
| 4. Linha de base e lacunas | Camadas, integrações, incidentes, lacunas principais | linha de base no 7, lacunas no 21 |
| 5. Contexto do sistema (C4, nível 1) | Diagrama de contexto e fronteira | 15 |
| 6. Princípios | Princípio e o que ele proíbe | 9 |
| 7. Decisões | Desenho, legado e dados, registros de decisão. Subseções acrescentadas: negócio, dados, aplicações e integração, infraestrutura | 10, 11, 12, 13, 14, 16 |
| 8. Tecnologia e plataforma | Modelo técnico de referência, seleção, plataforma, zona de pouso. Subseção acrescentada: segurança fim a fim | 17, 18, 19, 20 |
| 9. Roteiro e governança | Ondas, critérios de conclusão, conselho, funções de aptidão | 22, 23 |
| 10. O que ainda falta decidir | Pendências e quem decide | atualizada a cada aula, fechada no 24 |

O mapeamento é provisório. A auditoria da seção 7 o confirma linha a linha, porque o pocket foi lido por inteiro, mas os exercícios 11 a 16 não foram comparados com o texto dos capítulos 10 a 15 do caderno completo.

### 4.2 Páginas

Uma nova seção do site, **Caderno arquitetural**, traz três páginas.

1. `caderno/template.md`: o caderno vazio, com, em cada seção, o que vai nela, a pergunta que responde, o artefato que a preenche, os códigos de artefato e a seção anterior de que depende.
2. `caderno/convencoes.md`: códigos D, PR, RT, R, RD, CQ, L, P, DD, DL, B, I, ADR, C, LG e FA, os marcadores "proposto" e "a definir", e as regras de rastreabilidade do requisito à decisão.
3. `caderno/mapa.md`: tabela de seção, aula, bloco e exercício, que substitui `docs/caso-acme/artefatos.md`.

### 4.3 Módulo 1

A Aula 1 tem quatro blocos de 40 minutos e não comporta bloco novo. O bloco 4, processo de definição da arquitetura, ganha seção que apresenta o caderno e liga cada seção às oito fases do processo. O índice da Aula 1 aponta para `caderno/template.md`.

## 5. Alterações nos módulos

### 5.1 Anatomia do bloco

A página de bloco passa de sete para oito seções, com `## No caderno arquitetural` entre `## Uso pelo arquiteto` e `## Exercício N`. A seção nova traz:

1. a seção do caderno que o bloco preenche, com link
2. os campos a preencher, em lista
3. a entrada, isto é, a seção anterior de que o bloco depende
4. o critério de seção completa

O validador exige a seção apenas nos blocos listados em `CADERNO_BLOCKS`, que cada parte da decomposição amplia, e rejeita a seção fora de ordem em qualquer bloco.

### 5.2 Exercícios

- Cada item de exercício pede o preenchimento de um campo ou de uma coluna da seção, e o título do item nomeia o campo.
- Permanecem as regras vigentes: o enunciado fornece o artefato, pede classificação ou resposta simples, divide-se em itens autocontidos com `### Item N: assunto` e traz ao menos um visual.
- No fim do exercício, um link leva ao gabarito correspondente.
- O exercício 4 passa a associar cada seção do caderno à fase do processo que a produz.
- O exercício 3, atribuição de dez tarefas aos três níveis de arquitetura, não preenche campo de seção. A auditoria propõe a reformulação como preenchimento da subseção de papéis.

### 5.3 Sínteses, índices e glossário

- Cada síntese troca "sem gabarito público" por link à seção de gabaritos e passa a listar o estado do caderno ao fim da aula.
- Cada índice de aula traz a seção do caderno que a aula preenche.
- O glossário ganha os termos descrição de arquitetura, entregável, artefato, entidade e caderno arquitetural, com a definição de Lovatt (2021, seção 5.1.1) reescrita sem citar o autor no corpo.

## 6. Gabaritos

### 6.1 Fonte única

- O texto vive em `caderno-fonte/`, um arquivo por seção, com cada trecho marcado pelo exercício que o produz. A fonte fica fora de `docs/` porque o MkDocs a publicaria e o validador resolveria os links relativos a partir da pasta errada.
- As seções 0 e 10 têm modo de substituição, e a página de gabarito N mostra só a versão mais recente com exercício menor ou igual a N. As demais seções acumulam.
- O script `scripts/gerar_gabaritos.py` gera `docs/gabaritos/gabarito-exercicio-NN.md`, com todos os trechos de exercício menor ou igual a NN e o trecho de NN em destaque.
- As páginas geradas são versionadas no repositório, porque o MkDocs as lê direto da pasta `docs/`.
- A mesma fonte gera `caderno/template.md`, com os trechos substituídos por orientação de preenchimento.

### 6.2 Origem do texto

Cada trecho parte do capítulo correspondente do caderno completo do EAD e é recortado ao que o exercício pede. O texto é reescrito para cumprir as regras de `scripts/validate_content.py`: sem ponto-e-vírgula em prosa, travessão dentro do limite, autor só nas Fontes e termos em português. O recorte fica rastreável por comentário com o capítulo de origem, que o script remove da página gerada.

### 6.3 Testes

- A versão N contém a versão N-1.
- Cada exercício aponta para um gabarito existente, e cada gabarito aponta de volta.
- Todo campo que a seção `No caderno arquitetural` lista existe no template e no gabarito.
- As páginas geradas coincidem com a saída do script, de modo que edição manual de página gerada falha o teste.

## 7. Auditoria de consistência

Primeiro entregável da parte 1, com remoção condicionada à aprovação do professor sobre a matriz. A matriz classifica cada página, bloco, exercício, item de síntese e termo de glossário como mantém, altera, move ou remove, com a seção do caderno a que se liga e a justificativa de cada classificação.

Verificações obrigatórias:

- cada conceito apresentado nos blocos tem seção do caderno que o use, ou é marcado como apoio sem seção
- cada seção do caderno tem bloco que a ensine
- os códigos de requisito, de decisão e de artefato são os mesmos nos blocos, no dossiê e no caderno
- a ordem das seções respeita a ordem das aulas, com as lacunas na Aula 6 e a diferença em relação ao caderno completo registrada
- os capítulos do caderno completo sem aula correspondente, como IA no processo de arquitetura e interoperabilidade, ficam fora do template e dos gabaritos

Candidatos já visíveis: `docs/caso-acme/artefatos.md`, o exercício 3 e as sínteses.

## 8. Decomposição

| Parte | Entrega | Depende de |
| --- | --- | --- |
| 1 | Auditoria, caderno-template, fonte única, script, navegação, validador e testes, glossário | nenhuma |
| 2 | Módulo 1 e gabaritos 1 a 4 | 1 |
| 3 | Módulo 2 e gabaritos 5 a 8 | 2 |
| 4 | Módulo 3 e gabaritos 9 a 12 | 3 |
| 5 | Módulo 4 e gabaritos 13 a 16 | 4 |
| 6 | Módulo 5 e gabaritos 17 a 20 | 5 |
| 7 | Módulo 6, com blocos, exercícios e gabaritos 21 a 24 | 6 |

A ordem segue a do caderno, porque o gabarito N depende do N-1. A parte 7 reaproveita o capítulo 8, e os capítulos 20 a 22, do caderno completo.

## 9. Revogações

| Documento | Revogação |
| --- | --- |
| `2026-09-19-estrutura-do-curso-design.md`, seção 12.1 | Anatomia de sete seções passa a oito |
| `2026-09-19-estrutura-do-curso-design.md`, seção 12.2 | Gabarito volta ao site |
| `docs/modulo-{1..5}-*/sintese.md` | Frase "sem gabarito público" |
| `tests/test_content_contract.py` e `tests/test_modulo_{3,4,5}_contract.py` | Anatomia e ausência de gabarito |

## 10. Riscos e perguntas em aberto

- A seção 4.1 acrescenta quatro subseções ao pocket. Se o professor preferir o pocket sem acréscimo, os exercícios 3, 13, 14, 16 e 19 ficam sem lugar de preenchimento.
- Os exercícios 21 a 24 e os gabaritos correspondentes dependem de a Aula 6 ser escrita, e o caderno só fecha na parte 7.
- A matriz de auditoria pode apontar mais remoções do que o professor deseja. A decisão final é dele, item a item.
- O caderno completo está com status `pending_review` no EAD. O texto que migra para os gabaritos herda esse estado até a revisão.
- Páginas geradas versionadas aumentam o tamanho dos commits. O teste de coincidência com a saída do script limita o risco de divergência.

## 11. Fora de escopo

- IA no processo de arquitetura e interoperabilidade, capítulos do caderno completo sem aula correspondente
- publicação do caderno em Word ou PDF, que o `montar.py` do EAD já produz
- alteração das datas e dos números do dossiê ACME
- reescrita dos conceitos dos blocos além do necessário para amarrar ao caderno
