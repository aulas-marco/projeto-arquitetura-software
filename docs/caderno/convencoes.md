# Convenções do caderno arquitetural

O caderno usa códigos curtos para que uma decisão, um requisito e uma lacuna possam ser citados de qualquer seção sem ambiguidade. Esta página define os códigos, os marcadores de estado e a regra de rastreabilidade que liga uma decisão ao requisito que a motivou.

## Códigos de artefato

Cada código é a inicial do artefato seguida de um número sequencial dentro do caderno, como R6 para o sexto requisito declarado.

| Código | Artefato | Seção |
| --- | --- | --- |
| D | Decisão classificada por nível de arquitetura | 1 |
| PR | Premissa adotada na ausência de dado | 1 |
| RT | Restrição que chega fechada | 1 |
| R | Requisito declarado pelas partes interessadas | 3 |
| RD | Requisito derivado de outro requisito ou de uma restrição | 3 |
| CQ | Cenário de atributo de qualidade | 3 |
| L | Lacuna entre a linha de base e a arquitetura alvo | 4 |
| P | Princípio de design | 6 |
| DD | Decisão de design | 7 |
| DL | Decisão de legado e de dados | 7 |
| B | Bloco de construção da solução | 7 |
| I | Interface entre blocos | 7 |
| ADR | Registro de decisão arquitetural | 7 e 8 |
| C | Controle de segurança | 8 |
| LG | Ligação entre contêineres, com protocolo e contrato | 7 |
| FA | Função de aptidão que verifica uma decisão na esteira | 9 |

## Marcadores de estado

Uma decisão ou um artefato que ainda depende de validação com as partes interessadas recebe o marcador **proposto**. Um valor que o caso não registra recebe o marcador **a definir**, com a pessoa que o fornece. Os dois marcadores saem quando a validação ocorre, e a seção 10 do caderno lista tudo o que ainda os carrega.

## Rastreabilidade

Toda decisão das seções 6 a 8 cita o requisito ou a restrição que a motivou, e todo requisito da seção 3 aponta a decisão que o atende e a medida que verifica o atendimento. A leitura de uma decisão sem requisito de origem indica decisão sem justificativa, e a leitura de um requisito sem decisão indica lacuna a registrar na seção 4.
