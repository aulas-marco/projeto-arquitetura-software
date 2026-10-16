"""Hook do MkDocs que expande a marcação do caderno arquitetural em HTML.

Gramática: {{ficha:N}} e {{/ficha}}, {{folha:N}} e {{/folha}}, {{trilha:N}} ou
{{trilha:todas}}, {{progresso:N}}, {{novo}} e {{/novo}}.
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from caderno_registro import EXERCICIOS, PARTES, PLANO, ROTULOS_CURTOS, SUBSTITUI, TITULOS_SECAO  # noqa: E402

TOKEN = re.compile(r"\{\{(/?)([a-z]+)(?::([^}]*))?\}\}")
ABERTOS = ("ficha", "folha", "novo")


def _secao(valor):
    if valor is None or not valor.isdigit() or not 0 <= int(valor) <= 10:
        raise ValueError(f"número de seção inválido: {valor!r}")
    return int(valor)


def _exercicios_da_secao(secao):
    if secao in SUBSTITUI:
        return list(SUBSTITUI[secao])
    return sorted(n for n, secoes in PLANO.items() if secao in secoes)


def _lista_de_exercicios(numeros):
    if len(numeros) == 1:
        return f"Exercício {numeros[0]}"
    corpo = ", ".join(str(n) for n in numeros[:-1]) + f" e {numeros[-1]}"
    return f"Exercícios {corpo}"


def trilha(ativa, solta=False):
    itens = []
    for numero in range(11):
        classe = "feito" if ativa is not None and numero < ativa else ("atual" if numero == ativa else "")
        atual = ' aria-current="step"' if numero == ativa else ""
        itens.append(
            f'<li class="{classe}"{atual} title="{numero}. {TITULOS_SECAO[numero]}"><span class="no">{numero}</span>'
            f'<span class="rotulo">{ROTULOS_CURTOS[numero]}</span></li>'
        )
    rotulo = f"Seção {ativa} de 10" if ativa is not None else "As onze seções do caderno"
    classe_nav = "caderno-trilha solta" if solta else "caderno-trilha"
    return f'<nav class="{classe_nav}" aria-label="{rotulo}"><ol>{"".join(itens)}</ol></nav>'


def progresso(n):
    segmentos = []
    for i in range(1, 25):
        classe = "seg feito" if i < n else ("seg atual" if i == n else "seg")
        segmentos.append(f'<span class="{classe}" title="Exercício {i}"></span>')
    grupos = ["".join(segmentos[k:k + 4]) for k in range(0, 24, 4)]
    corpo = "".join(f'<span class="aula">{g}</span>' for g in grupos)
    return (
        f'<div class="caderno-progresso" role="img" aria-label="Exercício {n} de 24">{corpo}'
        f'<p class="legenda">Exercício {n} de 24</p></div>'
    )


def _ficha(secao):
    exercicios = _exercicios_da_secao(secao)
    aula = EXERCICIOS[exercicios[0]][0]
    titulo = TITULOS_SECAO[secao]
    return (
        '<div class="caderno-ficha" markdown="1">\n\n'
        f'<div class="cabeca"><span class="numero">{secao}</span><div class="titulo">'
        f'<p class="marca">Seção do caderno</p><p class="nome">{titulo}</p>'
        f'<p class="etiquetas"><span>Aula {aula}</span><span>{_lista_de_exercicios(exercicios)}</span></p>'
        f'</div></div>\n\n{trilha(secao)}\n\n'
    )


def _folha(secao):
    return f'<div class="caderno-folha" data-secao="{secao}" data-parte="{PARTES[secao]}" markdown="1">\n\n'


def expandir(markdown):
    pilha = []

    def trocar(achado):
        fecha, nome, valor = achado.group(1), achado.group(2), achado.group(3)
        if fecha:
            if nome not in ABERTOS or not pilha or pilha.pop() != nome:
                raise ValueError(f"fechamento sem abertura: {achado.group(0)}")
            return "\n\n</div>\n"
        if nome == "ficha":
            pilha.append(nome)
            return _ficha(_secao(valor))
        if nome == "folha":
            pilha.append(nome)
            return _folha(_secao(valor))
        if nome == "novo":
            pilha.append(nome)
            return '<div class="caderno-novo" markdown="1">\n\n'
        if nome == "trilha":
            return trilha(None if valor == "todas" else _secao(valor), solta=True)
        if nome == "progresso":
            if valor is None or not valor.isdigit() or not 1 <= int(valor) <= 24:
                raise ValueError(f"número de exercício inválido: {valor!r}")
            return progresso(int(valor))
        raise ValueError(f"marcação desconhecida: {achado.group(0)}")

    resultado = TOKEN.sub(trocar, markdown)
    if pilha:
        raise ValueError(f"marcação sem fechamento: {pilha[-1]}")
    return resultado


def on_page_markdown(markdown, **kwargs):
    return expandir(markdown)
