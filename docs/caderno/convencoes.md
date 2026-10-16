# Convenções do caderno arquitetural

Quando uma seção do caderno precisa citar um item de outra, como o sexto requisito, ela usa um código curto, no caso R6. Esta página lista os códigos, explica os dois marcadores de estado e mostra como uma decisão se liga ao requisito que a motivou.

## Códigos

Cada código é a inicial do item seguida de um número, na ordem em que o item aparece no caderno, de modo que D2 é a segunda decisão registrada.

| Código | O que identifica | Seção |
| --- | --- | --- |
| D | Uma decisão, classificada pelo nível de arquitetura de quem a toma | 1 |
| PR | Uma premissa: algo que o projeto assume como verdadeiro sem ter confirmado | 1 |
| RT | Uma restrição: decisão tomada fora do projeto, que o arquiteto não pode mudar | 1 |
| R | Um requisito declarado pelas pessoas envolvidas | 3 |
| RD | Um requisito derivado de outro requisito ou de uma restrição | 3 |
| CQ | Um cenário de qualidade: uma situação de uso descrita em seis partes, com meta que dá para medir | 3 |
| L | Uma lacuna entre o sistema atual e o que se quer construir | 4 |
| P | Um princípio de design: regra que as decisões precisam respeitar | 6 |
| DD | Uma decisão de design, como o estilo da solução ou os padrões adotados | 7 |
| DL | Uma decisão sobre o sistema antigo e sobre os dados | 7 |
| B | Um bloco de construção da solução | 7 |
| I | Uma interface entre dois blocos | 7 |
| ADR | Um registro de decisão arquitetural: texto curto com o contexto, as alternativas e as consequências de uma escolha | 7 e 8 |
| C | Um controle de segurança | 8 |
| LG | Uma ligação entre duas partes executáveis da solução, com protocolo e contrato | 7 |
| FA | Uma função de aptidão: teste automático que avisa quando uma decisão deixa de ser cumprida | 9 |
| CP | Um candidato a componente da solução, classificado por tipo | 1 |
| N | Um elemento da situação atual, lido nos três níveis de sistema | 1 |
| T | Uma tarefa do ciclo de modernização, atribuída a um papel | 1 |
| A | Um artefato do caso, ligado a uma fase, a um papel e a uma seção | 1 |

Na seção 1, os exercícios numeram os seus itens com CP, N, T e A. A letra C já pertence aos controles de segurança, e por isso os componentes da solução usam CP.

## Marcadores de estado

Nem tudo no caderno está confirmado, e dois marcadores mostram o que ainda falta. O marcador **proposto** aparece numa decisão ou num artefato que ainda precisa ser validado por quem tem autoridade para aprová-lo, e o marcador **a definir** aparece num valor que o caso ainda não traz, junto com a pessoa que pode informá-lo. Quando a validação acontece, o marcador sai, e a seção 10 do caderno lista tudo o que ainda o carrega.

## Como uma decisão se liga ao requisito

Uma decisão tomada sem que ninguém saiba a razão não permite saber se ela ainda faz sentido. Para evitar isso, toda decisão das seções 6 a 8 diz qual requisito ou restrição a motivou, e todo requisito da seção 3 diz qual decisão o atende e como se mede esse atendimento. Uma decisão sem requisito de origem não tem justificativa, e um requisito sem decisão é uma lacuna que deve entrar na seção 4.
