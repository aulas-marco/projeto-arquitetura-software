# Caderno arquitetural, parte 2: módulo 1 e estilo visual Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fazer o módulo 1 construir o caderno arquitetural, com seção `No caderno arquitetural` em cada bloco, exercícios que preenchem campos, gabaritos 1 a 4 cumulativos e um estilo visual próprio para todas as páginas do caderno.

**Architecture:** O estilo vive num hook do MkDocs (`scripts/caderno_hooks.py`) que expande fichas de marcação (`{{ficha:N}}`, `{{folha:N}}`, `{{trilha:N}}`, `{{progresso:N}}`, `{{novo}}`) em HTML, e em CSS próprio, de modo que o gerador e os autores escrevem só Markdown e fichas. O texto dos gabaritos 1 a 4 entra em `caderno-fonte/`, e os quatro blocos do módulo 1 migram para a anatomia de oito seções.

**Tech Stack:** Python 3 (`unittest`), MkDocs Material 9.7.6 com `hooks`, CSS, Chromium headless do Playwright para conferir a renderização.

**Spec:** `docs/superpowers/specs/2026-10-16-caderno-arquitetural-design.md`, seções 4.3, 5 e 6, mais o desenho visual desta parte, registrado na tarefa 1.

## Global Constraints

- A suíte (`python3 -m unittest discover -s tests`), o validador (`python3 scripts/validate_content.py`) e `python3 scripts/gerar_caderno.py --check` ficam verdes ao fim de cada tarefa, e `mkdocs build --strict` termina com saída 0.
- Regras editoriais: sem ponto-e-vírgula em prosa, no máximo um travessão por parágrafo, sem a palavra "prosa", sem os marcadores TODO, TBD, PLACEHOLDER e PREENCHER em caixa alta, sem "Lovatt" nem "livro-texto" fora das Fontes, voz impessoal, termos em português, organizações fictícias com o nome ACME e nenhum parágrafo fechado por frase de efeito.
- O enunciado do exercício fornece o artefato pronto e pede classificação ou resposta simples, em itens `### Item N: assunto` autocontidos, sem repetir a frase "fora do horário de aula".
- Decisões do professor em 16/10/2026 e rulings desta parte: D1 a D9 permanecem nove e o gabarito as completa, marcadas como propostas. Os códigos C1 a C10 do exercício 2 passam a CP1 a CP10. O item 3 do exercício 3 vira campo da tabela de papéis. Os papéis ficam na seção 1.
- Commits em ASCII, `tipo(escopo): descricao`, terminados por `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`.

## Review Focus

1. Marcação `{{...}}` com número fora de 0 a 10, ou de 1 a 24, ou sem fechamento, deve falhar no teste, e nunca chegar ao HTML publicado.
2. A página precisa continuar legível sem o hook (prévia em editor), porque a ficha só acrescenta moldura.
3. Contraste e tamanho em tela estreita: a trilha de 11 etapas não pode estourar a largura em 390 px.
4. Os gabaritos 1 a 4 precisam conter exatamente os trechos dos exercícios menores ou iguais ao seu, com a seção 0 e a seção 10 em modo de substituição.
5. Cada link entre exercício e gabarito precisa existir nos dois sentidos.

---

### Task 1: Estilo visual do caderno

**Files:**
- Create: `scripts/caderno_hooks.py`
- Modify: `scripts/caderno_registro.py` (rótulos curtos), `scripts/gerar_caderno.py` (marcação), `docs/assets/stylesheets/extra.css`, `mkdocs.yml` (`hooks` e versão do CSS)
- Create: `tests/test_caderno_hooks.py`
- Modify: `tests/test_caderno_gerador.py`, `tests/test_caderno_site.py`

**Conceito visual.** O caderno ganha a identidade de folha de projeto, em contraste deliberado com o restante do site, que é claro e frio.

- **Ficha** (`{{ficha:N}}` … `{{/ficha}}`), no fim de cada bloco: painel azul-noite com quadrícula de projeto, numeral gigante da seção em contorno ciano, título, etiquetas de aula e exercícios e a trilha das onze seções com a atual em âmbar. A tabela de campos e os botões de gabarito ficam dentro.
- **Trilha** (`{{trilha:N}}`, ou `{{trilha:todas}}`): onze nós ligados por uma linha, os anteriores preenchidos em ciano, o atual âmbar com halo, os seguintes vazados. Rola na horizontal em tela estreita.
- **Folha** (`{{folha:N}}` … `{{/folha}}`), nas seções do template: cartão com numeral grande na margem, filete de cor por parte (I enquadrar, II desenhar, III concretizar) e a tabela de orientação como ficha técnica.
- **Progresso** (`{{progresso:N}}`), no topo de cada gabarito: 24 segmentos em seis grupos de aula, os feitos preenchidos, o atual âmbar e a legenda "Exercício N de 24".
- **Novo** (`{{novo}}` … `{{/novo}}`): moldura âmbar com a etiqueta "Novo neste exercício".
- Paleta: azul-noite `#0E1A2E`, ciano `#5FC0D1`, âmbar `#F2B84B`, papel `#F2F6FB`, tinta `#16243A`. Tipografia do sistema, com `ui-monospace` nos numerais e nos códigos.

**Interfaces:**
- Produces: `expandir(markdown: str) -> str` em `caderno_hooks.py`, que o MkDocs chama por `on_page_markdown`, e `ROTULOS_CURTOS: dict[int, str]` e `PARTES: dict[int, str]` em `caderno_registro.py`. A gramática das fichas é `{{(ficha|folha|trilha):(\d+|todas)}}`, `{{progresso:\d+}}`, `{{/ficha}}`, `{{/folha}}`, `{{novo}}` e `{{/novo}}`.

- [ ] **Step 1: Teste do hook, que deve falhar**

```python
"""Hook que expande a marcação do caderno em HTML."""

import importlib.util
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def carregar():
    spec = importlib.util.spec_from_file_location("caderno_hooks", ROOT / "scripts" / "caderno_hooks.py")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


class HooksTest(unittest.TestCase):
    def setUp(self):
        self.h = carregar()

    def test_trilha_tem_onze_nos_e_marca_a_atual(self):
        html = self.h.expandir("{{trilha:3}}")
        self.assertEqual(11, html.count("<li"))
        self.assertEqual(1, html.count('aria-current="step"'))
        self.assertEqual(3, html.count('class="feito"'))
        self.assertIn("Seção 3 de 10", html)

    def test_trilha_todas_nao_marca_atual(self):
        html = self.h.expandir("{{trilha:todas}}")
        self.assertEqual(11, html.count("<li"))
        self.assertNotIn("aria-current", html)

    def test_ficha_abre_com_cabecalho_e_fecha(self):
        html = self.h.expandir("{{ficha:1}}\n\ncorpo\n\n{{/ficha}}")
        self.assertIn('<div class="caderno-ficha" markdown="1">', html)
        self.assertIn("Contexto", html)
        self.assertIn("Aula 1", html)
        self.assertIn("Exercícios 1, 2, 3 e 4", html)
        self.assertTrue(html.rstrip().endswith("</div>"))

    def test_folha_traz_numeral_e_parte(self):
        html = self.h.expandir("{{folha:7}}\n\ncorpo\n\n{{/folha}}")
        self.assertIn('data-secao="7"', html)
        self.assertIn('data-parte="II"', html)

    def test_progresso_tem_vinte_e_quatro_segmentos(self):
        html = self.h.expandir("{{progresso:5}}")
        self.assertEqual(24, html.count("<span class=\"seg"))
        self.assertEqual(4, html.count("seg feito"))
        self.assertEqual(1, html.count("seg atual"))
        self.assertIn("Exercício 5 de 24", html)

    def test_novo_abre_e_fecha(self):
        html = self.h.expandir("{{novo}}\n\ncorpo\n\n{{/novo}}")
        self.assertIn('<div class="caderno-novo" markdown="1">', html)
        self.assertTrue(html.rstrip().endswith("</div>"))

    def test_numero_fora_da_faixa_e_rejeitado(self):
        for entrada in ("{{trilha:11}}", "{{ficha:12}}", "{{progresso:0}}", "{{progresso:25}}"):
            with self.subTest(entrada=entrada):
                with self.assertRaises(ValueError):
                    self.h.expandir(entrada)

    def test_marcacao_desconhecida_e_rejeitada(self):
        with self.assertRaises(ValueError):
            self.h.expandir("{{ficha}}")

    def test_toda_marcacao_do_repositorio_e_valida(self):
        for caminho in sorted(DOCS.rglob("*.md")):
            if "superpowers" in caminho.parts:
                continue
            texto = caminho.read_text(encoding="utf-8")
            if "{{" not in texto:
                continue
            with self.subTest(pagina=str(caminho.relative_to(DOCS))):
                self.assertNotIn("{{", self.h.expandir(texto))

    def test_ficha_aberta_sem_fechamento_e_rejeitada(self):
        with self.assertRaises(ValueError):
            self.h.expandir("{{ficha:1}}\n\ncorpo")
```

- [ ] **Step 2: Rodar e conferir a falha**

Run: `python3 -m unittest tests.test_caderno_hooks -v`
Expected: FAIL, `scripts/caderno_hooks.py` não existe.

- [ ] **Step 3: Acrescentar ao registro**

Em `scripts/caderno_registro.py`, ao fim:

```python
ROTULOS_CURTOS = {
    0: "Resumo", 1: "Contexto", 2: "Partes", 3: "Requisitos", 4: "Linha de base",
    5: "Contexto C4", 6: "Princípios", 7: "Decisões", 8: "Tecnologia",
    9: "Roteiro", 10: "Pendências",
}

# Parte do caderno a que cada seção pertence: I enquadrar, II desenhar, III concretizar.
PARTES = {
    0: "I", 1: "I", 2: "I", 3: "I", 4: "I",
    5: "II", 6: "II", 7: "II",
    8: "III", 9: "III", 10: "III",
}
```

- [ ] **Step 4: Implementar o hook**

```python
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
ABERTOS = {"ficha": "caderno-ficha", "folha": "caderno-folha", "novo": "caderno-novo"}


def _secao(valor: str | None) -> int:
    if valor is None or not valor.isdigit() or not 0 <= int(valor) <= 10:
        raise ValueError(f"número de seção inválido: {valor!r}")
    return int(valor)


def _exercicios_da_secao(secao: int) -> list[int]:
    if secao in SUBSTITUI:
        return list(SUBSTITUI[secao])
    return sorted(n for n, secoes in PLANO.items() if secao in secoes)


def _lista_de_exercicios(numeros: list[int]) -> str:
    if len(numeros) == 1:
        return f"Exercício {numeros[0]}"
    corpo = ", ".join(str(n) for n in numeros[:-1]) + f" e {numeros[-1]}"
    return f"Exercícios {corpo}"


def trilha(ativa: int | None) -> str:
    itens = []
    for numero in range(11):
        classe = "feito" if ativa is not None and numero < ativa else ("atual" if numero == ativa else "")
        atual = ' aria-current="step"' if numero == ativa else ""
        itens.append(
            f'<li class="{classe}"{atual}><span class="no">{numero}</span>'
            f'<span class="rotulo">{ROTULOS_CURTOS[numero]}</span></li>'
        )
    rotulo = f"Seção {ativa} de 10" if ativa is not None else "As onze seções do caderno"
    return f'<nav class="caderno-trilha" aria-label="{rotulo}"><ol>{"".join(itens)}</ol></nav>'


def progresso(n: int) -> str:
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


def _ficha(secao: int) -> str:
    exercicios = _exercicios_da_secao(secao)
    aula = EXERCICIOS[exercicios[0]][0]
    titulo = TITULOS_SECAO[secao]
    return (
        '<div class="caderno-ficha" markdown="1">\n\n'
        f'<div class="cabeca"><span class="numero">{secao}</span><div class="titulo">'
        f'<p class="marca">No caderno arquitetural</p><p class="nome">{titulo}</p>'
        f'<p class="etiquetas"><span>Aula {aula}</span><span>{_lista_de_exercicios(exercicios)}</span></p>'
        f'</div></div>\n\n{trilha(secao)}\n\n'
    )


def _folha(secao: int) -> str:
    return (
        f'<div class="caderno-folha" data-secao="{secao}" data-parte="{PARTES[secao]}" markdown="1">\n\n'
    )


def expandir(markdown: str) -> str:
    pilha: list[str] = []

    def trocar(achado: re.Match) -> str:
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
            return trilha(None if valor == "todas" else _secao(valor))
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
```

- [ ] **Step 5: Rodar o teste do hook**

Run: `python3 -m unittest tests.test_caderno_hooks -v`
Expected: PASS nos dez testes. Se `test_trilha_tem_onze_nos_e_marca_a_atual` falhar na contagem de `class="feito"`, imprimir o HTML e conferir que `ativa=3` marca os nós 0, 1 e 2 como feitos.

- [ ] **Step 6: Gerador e testes passam a usar a marcação**

Em `scripts/gerar_caderno.py`:
1. `render_template`: envolver cada seção, com `{{folha:N}}` antes do cabeçalho e `{{/folha}}` depois do último conteúdo da seção, e abrir a página com `{{trilha:todas}}` logo depois da introdução.
2. `render_gabarito`: logo depois do `# Gabarito do exercício N`, inserir `{{progresso:N}}`, e trocar o `<div class="caderno-novo" markdown="1">` por `{{novo}}` e o `</div>` por `{{/novo}}`.

Em `tests/test_caderno_gerador.py`, trocar a asserção do destaque por:

```python
        self.assertIn("{{novo}}\n\nTexto do gabarito seis.", texto)
        self.assertNotIn("{{novo}}\n\nTexto do gabarito cinco", texto)
        self.assertIn("{{progresso:6}}", texto)
```

e acrescentar em `test_template_traz_orientacao_e_campos_sem_gabarito`:

```python
        self.assertIn("{{folha:3}}", texto)
        self.assertIn("{{trilha:todas}}", texto)
```

Run: `python3 -m unittest tests.test_caderno_gerador -v`
Expected: FAIL antes da edição do gerador e PASS depois.

- [ ] **Step 7: CSS**

Acrescentar a `docs/assets/stylesheets/extra.css`, substituindo o bloco `.caderno-novo` anterior:

```css
/* Caderno arquitetural: identidade de folha de projeto */
:root {
  --caderno-noite: #0E1A2E;
  --caderno-ciano: #5FC0D1;
  --caderno-ambar: #F2B84B;
  --caderno-mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace;
}

.md-typeset .caderno-ficha {
  position: relative;
  margin: 2rem 0 3rem;
  padding: 1.6rem 1.8rem 1.2rem;
  border-radius: 1.1rem;
  color: #EAF1FA;
  background-color: var(--caderno-noite);
  background-image:
    linear-gradient(rgb(95 192 209 / 9%) 1px, transparent 1px),
    linear-gradient(90deg, rgb(95 192 209 / 9%) 1px, transparent 1px);
  background-size: 1.5rem 1.5rem;
  box-shadow: 0 1rem 2.4rem rgb(14 26 46 / 28%);
  overflow: hidden;
}
.md-typeset .caderno-ficha::after {
  content: "";
  position: absolute;
  inset: 0 auto 0 0;
  width: 0.3rem;
  background: linear-gradient(var(--caderno-ciano), var(--caderno-ambar));
}
.md-typeset .caderno-ficha .cabeca { display: flex; align-items: center; gap: 1.4rem; }
.md-typeset .caderno-ficha .numero {
  font: 800 5.4rem/1 var(--caderno-mono);
  color: transparent;
  -webkit-text-stroke: 2px var(--caderno-ciano);
  letter-spacing: -0.04em;
}
.md-typeset .caderno-ficha .marca {
  margin: 0;
  font: 700 0.62rem/1 var(--caderno-mono);
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--caderno-ciano);
}
.md-typeset .caderno-ficha .nome { margin: 0.35rem 0 0.5rem; font-size: 1.5rem; font-weight: 700; color: #FFFFFF; line-height: 1.15; }
.md-typeset .caderno-ficha .etiquetas { margin: 0; display: flex; flex-wrap: wrap; gap: 0.4rem; }
.md-typeset .caderno-ficha .etiquetas span {
  padding: 0.12rem 0.65rem;
  border: 1px solid rgb(95 192 209 / 55%);
  border-radius: 99px;
  font: 600 0.66rem/1.6 var(--caderno-mono);
  color: #CFE6EC;
}
.md-typeset .caderno-ficha table:not([class]) {
  display: table;
  width: 100%;
  margin: 1rem 0;
  color: #EAF1FA;
  background: rgb(255 255 255 / 4%);
  border: 1px solid rgb(95 192 209 / 28%);
  border-radius: 0.6rem;
  overflow: hidden;
}
.md-typeset .caderno-ficha table:not([class]) th {
  background: rgb(95 192 209 / 16%);
  color: var(--caderno-ciano);
  font: 700 0.62rem/1.4 var(--caderno-mono);
  letter-spacing: 0.1em;
  text-transform: uppercase;
}
.md-typeset .caderno-ficha table:not([class]) td,
.md-typeset .caderno-ficha table:not([class]) th { border-color: rgb(95 192 209 / 22%); }
.md-typeset .caderno-ficha a { color: var(--caderno-ambar); }
.md-typeset .caderno-ficha .caderno-botao,
.md-typeset a.caderno-botao {
  display: inline-block;
  margin: 0.2rem 0.5rem 0.2rem 0;
  padding: 0.35rem 0.95rem;
  border-radius: 99px;
  background: var(--caderno-ambar);
  color: var(--course-ink);
  font: 700 0.72rem/1.4 var(--caderno-mono);
  letter-spacing: 0.04em;
  text-decoration: none;
}
.md-typeset .caderno-ficha .caderno-botao:hover { background: #FFD27A; color: var(--course-ink); }

.md-typeset .caderno-trilha { margin: 1rem 0 0.4rem; overflow-x: auto; padding-bottom: 0.4rem; }
.md-typeset .caderno-trilha ol {
  display: flex;
  min-width: 41rem;
  margin: 0;
  padding: 0;
  list-style: none;
  position: relative;
}
.md-typeset .caderno-trilha ol::before {
  content: "";
  position: absolute;
  top: 0.85rem;
  left: 1rem;
  right: 1rem;
  height: 2px;
  background: rgb(95 192 209 / 30%);
}
.md-typeset .caderno-trilha li { flex: 1; margin: 0; text-align: center; position: relative; }
.md-typeset .caderno-trilha .no {
  display: grid;
  place-items: center;
  width: 1.7rem;
  height: 1.7rem;
  margin: 0 auto 0.3rem;
  border: 2px solid var(--caderno-ciano);
  border-radius: 50%;
  background: var(--caderno-noite);
  font: 700 0.66rem/1 var(--caderno-mono);
  color: var(--caderno-ciano);
}
.md-typeset .caderno-trilha .feito .no { background: var(--caderno-ciano); color: var(--caderno-noite); }
.md-typeset .caderno-trilha .atual .no {
  background: var(--caderno-ambar);
  border-color: var(--caderno-ambar);
  color: var(--caderno-noite);
  box-shadow: 0 0 0 0.3rem rgb(242 184 75 / 28%);
}
.md-typeset .caderno-trilha .rotulo { font-size: 0.58rem; color: #9FB8C8; line-height: 1.2; }
.md-typeset .caderno-trilha .atual .rotulo { color: var(--caderno-ambar); font-weight: 700; }

.md-typeset .caderno-folha {
  position: relative;
  margin: 2.4rem 0;
  padding: 1.2rem 1.4rem 0.6rem 5.6rem;
  background: #FFFFFF;
  border: 1px solid #D8E5F1;
  border-left: 0.35rem solid var(--course-cobalt);
  border-radius: 0.8rem;
  box-shadow: 0 0.5rem 1.4rem rgb(22 36 58 / 8%);
}
.md-typeset .caderno-folha[data-parte="II"] { border-left-color: var(--caderno-ciano); }
.md-typeset .caderno-folha[data-parte="III"] { border-left-color: var(--caderno-ambar); }
.md-typeset .caderno-folha::before {
  content: attr(data-secao);
  position: absolute;
  top: 0.6rem;
  left: 1.1rem;
  font: 800 3.4rem/1 var(--caderno-mono);
  color: transparent;
  -webkit-text-stroke: 1.5px var(--course-cobalt);
  opacity: 0.55;
}
.md-typeset .caderno-folha[data-secao="0"]::before { content: "·"; }
.md-typeset .caderno-folha h2 { margin-top: 0; }
.md-typeset .caderno-folha table:not([class]) { display: table; width: 100%; }
.md-typeset .caderno-folha table:not([class]) td:first-child {
  width: 11rem;
  background: #EEF4FA;
  font-weight: 700;
  color: var(--course-ink);
}

.md-typeset .caderno-progresso { margin: 1.2rem 0 1.6rem; }
.md-typeset .caderno-progresso { display: flex; flex-wrap: wrap; gap: 0.6rem; align-items: center; }
.md-typeset .caderno-progresso .aula { display: flex; gap: 0.2rem; padding: 0.25rem; border-radius: 0.5rem; background: #E6EEF7; }
.md-typeset .caderno-progresso .seg { width: 0.9rem; height: 1.3rem; border-radius: 0.2rem; background: #FFFFFF; border: 1px solid #B9CBE0; }
.md-typeset .caderno-progresso .seg.feito { background: var(--course-cobalt); border-color: var(--course-cobalt); }
.md-typeset .caderno-progresso .seg.atual { background: var(--caderno-ambar); border-color: var(--caderno-ambar); box-shadow: 0 0 0 0.2rem rgb(242 184 75 / 35%); }
.md-typeset .caderno-progresso .legenda { margin: 0 0 0 0.4rem; font: 700 0.7rem/1 var(--caderno-mono); color: var(--course-ink); }

.md-typeset .caderno-novo {
  position: relative;
  margin: 2rem 0 1.2rem;
  padding: 1.4rem 1.2rem 0.4rem;
  border: 2px solid var(--caderno-ambar);
  border-radius: 0.8rem;
  background: linear-gradient(180deg, #FFF8E8, #FFFFFF 3rem);
}
.md-typeset .caderno-novo::before {
  content: "Novo neste exercício";
  position: absolute;
  top: -0.8rem;
  left: 1rem;
  padding: 0.15rem 0.8rem;
  border-radius: 99px;
  background: var(--caderno-ambar);
  color: var(--caderno-noite);
  font: 800 0.62rem/1.6 var(--caderno-mono);
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

@media (max-width: 44.9375em) {
  .md-typeset .caderno-ficha { padding: 1.2rem 1rem 1rem; }
  .md-typeset .caderno-ficha .numero { font-size: 3.6rem; }
  .md-typeset .caderno-ficha .nome { font-size: 1.15rem; }
  .md-typeset .caderno-folha { padding: 3.6rem 1rem 0.6rem; }
  .md-typeset .caderno-folha::before { top: 0.6rem; left: 1rem; font-size: 2.2rem; }
  .md-typeset .caderno-folha table:not([class]) td:first-child { width: auto; }
}
```

Em `mkdocs.yml`: adicionar `hooks:\n  - scripts/caderno_hooks.py` depois de `exclude_docs`, e trocar `extra.css?v=20261016-1` por `extra.css?v=20261016-2`. Atualizar `tests/test_caderno_site.py` para a nova versão do CSS e para exigir `caderno_hooks.py` em `mkdocs.yml`.

- [ ] **Step 8: Conferir a renderização**

```bash
/Volumes/Marco-Dev/dev/projeto-arquitetura-software/.venv/bin/mkdocs build --strict -d /tmp/claude-501/site-p2
(cd /tmp/claude-501/site-p2 && python3 -m http.server 8765 >/dev/null 2>&1 &)
CH=$(ls -d ~/Library/Caches/ms-playwright/chromium_headless_shell-1223/*/chrome-headless-shell-mac-arm64/chrome-headless-shell | head -1)
"$CH" --no-sandbox --hide-scrollbars --window-size=1280,2400 --screenshot=/tmp/claude-501/shot-template.png http://localhost:8765/caderno/template/
"$CH" --no-sandbox --hide-scrollbars --window-size=390,2400 --screenshot=/tmp/claude-501/shot-template-m.png http://localhost:8765/caderno/template/
```

Abrir as imagens com Read e conferir: numeral, trilha, folha, contraste, rolagem horizontal só dentro da trilha. Ajustar o CSS até que as duas capturas estejam limpas.

- [ ] **Step 9: Rodar tudo e commitar**

```bash
python3 -m unittest discover -s tests 2>&1 | tail -3
python3 scripts/validate_content.py | tail -1
python3 scripts/gerar_caderno.py && python3 scripts/gerar_caderno.py --check | tail -1
git add scripts tests docs mkdocs.yml
git commit -m "feat(caderno): estilo de folha de projeto com ficha, trilha, folha, progresso e destaque

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
```

---

### Task 2: Fonte dos gabaritos 1 a 4

**Files:**
- Modify: `caderno-fonte/00-resumo.md`, `01-contexto.md`, `10-pendencias.md`
- Modify: `tests/test_caderno_contrato.py` (cobertura dos exercícios 1 a 4)
- Regenerate: `docs/caderno/template.md`, `docs/caderno/mapa.md`, `docs/gabaritos/*`

**Conteúdo.** Cada trecho nasce do capítulo 2 do caderno completo do EAD (`4-caderno/caderno-arquitetural-acme.md:147-250`), recortado ao que o exercício pede e reescrito nas regras editoriais.

- Seção 1, fragmento do exercício 1, "Instituição, restrições e decisões por nível": tabela de porte, restrições fechadas, respostas excluídas, e a tabela D1 a D9 com nível, justificativa, componente não tecnológico afetado e dependência. D1 a D3 vêm do caderno, D4 a D9 seguem o critério de alcance do bloco 1 e levam o marcador **proposto**.
- Seção 1, fragmento do exercício 2, "Componentes da solução do R7": tabela CP1 a CP10 com tipo, mais N1 a N6 com o nível de sistema.
- Seção 1, fragmento do exercício 3, "Papéis e responsabilidades": tabela T1 a T10 com nível de arquitetura, grupo de competência e, em T10, o benefício que a justifica.
- Seção 1, fragmento do exercício 4, "Artefatos nas fases do processo": tabela A1 a A10 com fase, papel e seção do caderno, mais as premissas PR1 a PR7 e as exclusões do escopo.
- Seção 10, versão do exercício 4: pendências abertas ao fim da Aula 1, entre elas a data de conclusão do ciclo, que depende da fase 7, e a nomeação do patrocinador.
- Seção 0, versão do exercício 4: resumo de uma página com o problema, a pergunta reformulada e o estado.

- [ ] **Step 1:** Escrever primeiro o teste que exige os quatro gabaritos: em `tests/test_caderno_contrato.py`, `test_exercicios_1_a_4_tem_gabarito` deve afirmar que os exercícios 1, 2, 3 e 4 têm fragmento com gabarito na seção 1 e que as seções 0 e 10 têm versão 4. Rodar e ver falhar.
- [ ] **Step 2:** Escrever os fragmentos nos arquivos da fonte, no formato `<!--ex n=N titulo="..."-->` com `<!--campos-->` e `<!--gabarito-->`, sem título de nível 1 a 3 no corpo.
- [ ] **Step 3:** `python3 scripts/gerar_caderno.py`, conferir as páginas geradas e rodar o teste, que passa.
- [ ] **Step 4:** Rodar suíte, validador e `mkdocs build --strict`, e commitar.

---

### Task 3: Blocos 1 a 4 do módulo 1

**Files:**
- Modify: `docs/modulo-1-fundamentos/bloco-1-arquitetura-de-solucoes-e-de-software.md`, `bloco-2-a-solucao-como-sistema.md`, `bloco-3-papel-do-arquiteto-de-solucao.md`, `bloco-4-processo-de-definicao-da-arquitetura.md`
- Modify: `scripts/validate_content.py` (`CADERNO_BLOCKS`)
- Create: `tests/test_modulo_1_caderno.py`

**Em cada bloco:** inserir `## No caderno arquitetural` entre `## Uso pelo arquiteto` e `## Exercício N`, com `{{ficha:1}}`, a tabela de campos, a entrada, o critério de seção completa e os botões de template e de gabarito, fechada por `{{/ficha}}`. Os itens dos exercícios passam a nomear o campo no título.

| Bloco | Campos que a ficha lista | Mudança no exercício |
| --- | --- | --- |
| 1 | Nível, justificativa, componente não tecnológico afetado e dependência de cada decisão D1 a D9 | Itens 1 a 3 renomeados pelo campo |
| 2 | Tipo de cada componente CP1 a CP10 e nível de cada elemento N1 a N6 | C1 a C10 passam a CP1 a CP10 |
| 3 | Nível de arquitetura, grupo de competência e benefício de cada tarefa T1 a T10 | Item 3 vira o campo Benefício de T10 |
| 4 | Fase, papel e seção do caderno de cada artefato A1 a A10, e a pendência da data de conclusão | Item 1 ganha a coluna Seção do caderno, item 2 vira pendência da seção 10 |

O bloco 4 ganha também a seção `### O caderno arquitetural`, dentro do conceito, que apresenta o template, mostra `{{trilha:todas}}` e liga cada seção do caderno à fase do processo que a produz.

- [ ] **Step 1:** Escrever `tests/test_modulo_1_caderno.py`, que exige em cada um dos quatro blocos: a seção `## No caderno arquitetural` entre `Uso pelo arquiteto` e `Exercício`, uma ficha `{{ficha:1}}` fechada, o link `../gabaritos/gabarito-exercicio-0N.md`, o link `../caderno/template.md#1-contexto` e, no bloco 2, a ausência de `C1` a `C10` como código de componente e a presença de `CP10`. No bloco 4, exige `### O caderno arquitetural` e `{{trilha:todas}}`. Rodar e ver falhar.
- [ ] **Step 2:** Editar os quatro blocos conforme a tabela, preservando o artefato fornecido e as perguntas simples dos exercícios.
- [ ] **Step 3:** Acrescentar os quatro nomes de arquivo a `CADERNO_BLOCKS` em `scripts/validate_content.py`, rodar os testes de módulo, o validador e corrigir o que acusarem.
- [ ] **Step 4:** Commitar.

---

### Task 4: Índice, síntese, navegação e página inicial

**Files:**
- Modify: `docs/modulo-1-fundamentos/index.md`, `sintese.md`, `docs/index.md`, `mkdocs.yml`, `docs/caso-acme/artefatos.md` (nota de remissão ao mapa)

- [ ] **Step 1:** No índice da Aula 1, acrescentar a seção do caderno que a aula preenche, a trilha e os links para o template. Na síntese, trocar a frase "sem gabarito público" por link à seção Gabaritos e acrescentar o estado do caderno ao fim da aula.
- [ ] **Step 2:** Acrescentar à navegação os quatro gabaritos, `gabaritos/gabarito-exercicio-01.md` a `04`, e trocar o parágrafo da página inicial por texto que diga que o caderno tem, por ora, os exercícios 1 a 4.
- [ ] **Step 3:** Rodar suíte, validador, `--check` e `mkdocs build --strict`, conferir as capturas de tela do bloco 1, do gabarito 4 e do template, e commitar.

---

### Task 5: Revisão final e integração

- [ ] **Step 1:** Rodar o pacote de revisão e um revisor independente sobre o ramo inteiro, tratar os achados Critical e Important com teste que falha antes, e registrar os Minor.
- [ ] **Step 2:** Integrar à `main` e publicar somente com a ordem expressa do professor.
