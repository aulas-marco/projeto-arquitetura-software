# Bloco 0 da Aula 4, espinha dorsal dos domínios — Plano de implementação

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Acrescentar à Aula 4 um bloco 0 conceitual que mostra o que o arquiteto de solução recebe, decide e entrega em cada domínio, e fazer os blocos 1 a 4 retomarem esse modelo.

**Architecture:** Uma página nova (`bloco-0-espinha-dorsal-dos-dominios.md`) com uma figura central em SVG e um roteiro de quatro perguntas. Quatro figuras reduzidas, geradas pelo mesmo script, abrem os blocos 1 a 4. O validador passa a dispensar a seção Exercício apenas em páginas `bloco-0-*`, e a grade da aula ganha a linha do bloco 0.

**Tech Stack:** MkDocs Material, Markdown, SVG gerado por script Python (`scripts/figuras_bloco_0.py`), testes `unittest` executados com `python3 -m pytest -q`, validador `scripts/validate_content.py`, Playwright para conferência visual.

**Spec:** `docs/superpowers/specs/2026-10-03-modulo-4-bloco-0-espinha-dorsal-design.md`

## Global Constraints

- Texto em português do Brasil com acentuação completa, registro impessoal.
- Proibido: neologismo, metáfora, idiomatismo, antítese ("não é X, é Y", "em vez de", "menos X e mais Y", "ao contrário de", "X, mas não Y"), parágrafo terminando em frase de efeito, ponto e vírgula em prosa, mais de um travessão por parágrafo, negrito espalhado.
- "Lovatt" e "livro-texto" só nas seções Fontes e nas legendas `*Figura N — ...*` (teste `SelfContainedTextTest`).
- O bloco 0 não contém "ACME", "Hospital", "Clínica", "COBOL" nem "matrícula".
- SVGs `modulo-4-*.svg`: `<title>` com 5 ou mais caracteres, `<desc>` com 20 ou mais, `font-size:Npx` declarado em `<style>` com mínimo de 16, sem "ACME", "COBOL", "CICS", "matrícula", "Matrícula", e todo SVG usado por alguma página do módulo 4.
- A soma dos blocos 0 a 4 na grade da Aula 4 é 130 minutos, com três Kahoots.
- O termo "espinha dorsal" aparece só no nome do arquivo, no glossário e no título da entrada do glossário. O título da página e o texto usam "os quatro domínios numa só solução".
- Conceito já apresentado em outro bloco ou aula recebe link para o local de origem.

## Review Focus

- Página `bloco-0-*` sem a seção "Uso pelo arquiteto" ou sem "Fontes": o validador deve continuar acusando a falta, porque só o Exercício é dispensado (teste na Tarefa 1).
- Página `bloco-1-*` sem Exercício: o validador deve continuar acusando a falta (teste na Tarefa 1).
- Grade da Aula 3, que não tem bloco 0: o teste da grade deve continuar aceitando quatro blocos somando 130 (Tarefa 5).
- Figura reduzida esquecida em algum bloco ou apontando para o domínio errado: cada bloco deve usar exatamente o mapa do seu domínio (teste na Tarefa 4).
- Pergunta do roteiro reescrita num bloco com redação diferente da do bloco 0: a redação deve ser idêntica (teste na Tarefa 4).

---

## Mapa de arquivos

| Arquivo | Responsabilidade |
| --- | --- |
| `scripts/validate_content.py` | Regra de anatomia: dispensa do Exercício em `bloco-0-*` |
| `tests/test_content_contract.py` | Testes da regra de anatomia |
| `scripts/figuras_bloco_0.py` | Gera a figura central e as quatro reduzidas |
| `docs/assets/images/modulo-4-b0-espinha-dorsal.svg` | Figura central |
| `docs/assets/images/modulo-4-b0-mapa-{negocio,dados,aplicacoes,infraestrutura}.svg` | Figuras reduzidas |
| `docs/modulo-4-dominios-da-solucao/bloco-0-espinha-dorsal-dos-dominios.md` | Página do bloco 0 |
| `mkdocs.yml` | Navegação |
| `docs/modulo-4-dominios-da-solucao/bloco-{1,2,3,4}-*.md` | Retomadas |
| `docs/modulo-4-dominios-da-solucao/index.md`, `sintese.md`, `docs/cronograma.md`, `docs/referencia/glossario.md` | Grade, roteiro, cadeia, glossário |
| `tests/test_modulo_4_contract.py`, `tests/test_exercicios_fora_da_sala.py` | Contrato do bloco 0, retomadas e grade |

---

### Task 1: Validador dispensa o Exercício só no bloco 0

**Files:**
- Modify: `scripts/validate_content.py` (função `check_block_anatomy`, perto da linha 184)
- Test: `tests/test_content_contract.py` (classe que contém `test_validator_allows_block_page_with_all_sections_in_order`)

**Interfaces:**
- Consumes: nada.
- Produces: `check_block_anatomy(path, text)` aceita página cujo nome começa com `bloco-0-` sem `## Exercício N`, mantendo as demais seções obrigatórias e a ordem.

- [ ] **Step 1: Escrever os testes que falham**

Acrescente à mesma classe de `test_validator_allows_block_page_with_all_sections_in_order`:

```python
    def test_validator_allows_block_zero_without_exercise(self):
        allowed = DOCS / "modulo-1-fundamentos" / "bloco-0-teste-sem-exercicio.md"
        allowed.write_text(
            "# Bloco teste\n\n"
            "## Antes de começar\n\nTexto.\n\n"
            "## Conceito\n\nTexto.\n\n"
            "## Uso pelo arquiteto\n\nTexto.\n\n"
            "## Fontes\n\nTexto.\n",
            encoding="utf-8",
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertNotIn("bloco-0-teste-sem-exercicio", result.stdout)
        finally:
            allowed.unlink()

    def test_validator_still_requires_other_sections_in_block_zero(self):
        offender = DOCS / "modulo-1-fundamentos" / "bloco-0-teste-sem-uso.md"
        offender.write_text(
            "# Bloco teste\n\n"
            "## Antes de começar\n\nTexto.\n\n"
            "## Conceito\n\nTexto.\n\n"
            "## Fontes\n\nTexto.\n",
            encoding="utf-8",
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertIn("bloco-0-teste-sem-uso.md: falta a secao Uso pelo arquiteto", result.stdout)
        finally:
            offender.unlink()

    def test_validator_still_requires_exercise_in_block_one(self):
        offender = DOCS / "modulo-1-fundamentos" / "bloco-1-teste-sem-exercicio.md"
        offender.write_text(
            "# Bloco teste\n\n"
            "## Antes de começar\n\nTexto.\n\n"
            "## Conceito\n\nTexto.\n\n"
            "## Uso pelo arquiteto\n\nTexto.\n\n"
            "## Fontes\n\nTexto.\n",
            encoding="utf-8",
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertIn("bloco-1-teste-sem-exercicio.md: falta a secao Exercício", result.stdout)
        finally:
            offender.unlink()
```

- [ ] **Step 2: Rodar e ver falhar**

Run: `python3 -m pytest -q tests/test_content_contract.py -k "block_zero or block_one"`
Expected: `test_validator_allows_block_zero_without_exercise` FAIL, porque o validador acusa "falta a secao Exercício", e os outros dois PASS.

- [ ] **Step 3: Implementar**

Em `check_block_anatomy`, troque o laço `for section in BLOCK_SECTIONS:` pelo uso de uma tupla filtrada e atualize a docstring:

```python
def check_block_anatomy(path: Path, text: str) -> list[str]:
    """Paginas de bloco precisam das cinco secoes nomeadas, na ordem.

    "Exercicio" e caso especial: o cabecalho precisa trazer um numero
    inteiro (## Exercicio N), nao apenas o nome da secao. A pagina de
    bloco 0 (bloco-0-*) e a abertura conceitual da aula e nao tem
    exercicio, por isso so ela e dispensada dessa secao.
    """
    if not path.name.startswith("bloco-"):
        return []
    sections = BLOCK_SECTIONS
    if path.name.startswith("bloco-0-"):
        sections = tuple(s for s in BLOCK_SECTIONS if s != "Exercício")
    positions = []
    for section in sections:
```

O restante da função fica igual.

- [ ] **Step 4: Rodar e ver passar**

Run: `python3 -m pytest -q tests/test_content_contract.py && python3 scripts/validate_content.py | tail -1`
Expected: todos PASS e `Resumo: 0 violacao(oes).`

- [ ] **Step 5: Commit**

```bash
git add scripts/validate_content.py tests/test_content_contract.py
git commit -m "test(validador): bloco 0 dispensado da secao de exercicio

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 2: Figuras do bloco 0

**Files:**
- Create: `scripts/figuras_bloco_0.py`
- Create (gerados): `docs/assets/images/modulo-4-b0-espinha-dorsal.svg`, `docs/assets/images/modulo-4-b0-mapa-negocio.svg`, `docs/assets/images/modulo-4-b0-mapa-dados.svg`, `docs/assets/images/modulo-4-b0-mapa-aplicacoes.svg`, `docs/assets/images/modulo-4-b0-mapa-infraestrutura.svg`

**Interfaces:**
- Consumes: nada.
- Produces: os cinco SVGs acima, referenciados pelas Tarefas 3 e 4 com esses nomes exatos.

Os testes de figura do módulo 4 já existentes (`test_all_modulo_4_visuals_are_accessible_legible_and_generic` e `test_every_module_4_visual_is_used_by_a_page`) cobrem estes SVGs. O segundo só passa depois das Tarefas 3 e 4, por isso esta tarefa não roda a suíte inteira e confere os SVGs diretamente.

- [ ] **Step 1: Criar o script**

```python
"""Gera a figura central do bloco 0 da Aula 4 e as quatro figuras reduzidas.

Uso: python3 scripts/figuras_bloco_0.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "docs" / "assets" / "images"
STYLE = ("<style>text{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;fill:#16243A}"
         ".h{font-size:28px;font-weight:700}.d{font-size:20px;font-weight:700}.q{font-size:17px;font-style:italic;fill:#52657E}"
         ".c{font-size:16px}.ch{font-size:17px;font-weight:700;fill:#52657E}.w{fill:white}.b{font-size:18px;font-weight:700}"
         ".ax{font-size:16px;fill:#16243A}.axh{font-size:17px;font-weight:700;fill:#254DB8}</style>")
ARROW = ('<marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">'
         '<path d="M0 0L10 5L0 10z" fill="#52657E"/></marker>')

DOMINIOS = [
    ("negocio", "Negócio", "Onde a mudança incide no negócio?",
     ["Mapa de capacidades, fluxo", "de valor e modelo de processo"],
     ["Onde a mudança incide nas", "capacidades, etapas e atividades"],
     ["Capacidades, etapas e", "atividades afetadas"],
     ["Serviço de negócio", "e processo"]),
    ("dados", "Dados", "A quem pertence cada dado e com que atraso cada cópia o reflete?",
     ["Capacidades afetadas e", "modelo de dados corporativo"],
     ["Dono, fonte de verdade, regime", "de consistência e obrigações"],
     ["Grade dado × aplicação"],
     ["Informação que", "sustenta os serviços"]),
    ("aplicacoes", "Aplicações", "Que aplicações mudam e como trocam dados?",
     ["Grade dado × aplicação e", "portfólio de aplicações"],
     ["Aplicações que mudam, interfaces,", "contratos e fronteira"],
     ["Diagramas de contexto e de", "contêineres e contratos"],
     ["Serviço de aplicação", "e componente"]),
    ("infraestrutura", "Infraestrutura", "Onde cada contêiner executa e com que exigências?",
     ["Contêineres e relações"],
     ["Modo, volume e latência, camada", "de execução e topologia"],
     ["Diagrama de implantação e", "exigências para a Aula 5"],
     ["Serviço de", "tecnologia"]),
]


def cell(out, x, y, w, h, lines, fill, stroke):
    out.append(f'  <rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="2"/>')
    top = y + h / 2 - (len(lines) - 1) * 11 + 6
    for i, line in enumerate(lines):
        out.append(f'  <text x="{x + w / 2}" y="{top + i * 22:.0f}" text-anchor="middle" class="c">{line}</text>')


def central():
    w, h = 1200, 900
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
           '  <title id="title">O que o arquiteto de solução recebe, decide e entrega em cada domínio</title>'
           '<desc id="desc">Quatro camadas empilhadas, negócio, dados, aplicações e infraestrutura, entre uma faixa de entrada, '
           'estilo e padrões registrados em ADR na Aula 3, e uma faixa de saída, definição tecnológica na Aula 5. Cada camada traz a '
           'pergunta que o arquiteto responde e três colunas, recebe, decide e entrega, com a coluna decide em destaque. Setas '
           'ortogonais ligam a coluna entrega de cada camada à coluna recebe da camada seguinte. À esquerda, a hierarquia de serviços '
           'acompanha as camadas, do serviço de negócio e processo à informação que sustenta os serviços, ao serviço de aplicação e '
           'componente e ao serviço de tecnologia.</desc>',
           f'  <defs>{STYLE}{ARROW}</defs>',
           f'  <rect width="{w}" height="{h}" rx="24" fill="#F2F6FB"/>',
           '  <text x="24" y="40" class="h">O trabalho do arquiteto nos quatro domínios</text>',
           '  <rect x="190" y="58" width="990" height="42" rx="21" fill="#16243A"/>',
           '  <text x="685" y="85" text-anchor="middle" class="b w">Aula 3: estilo e padrões registrados em ADR</text>',
           '  <text x="350" y="130" text-anchor="middle" class="ch">Recebe</text>',
           '  <text x="680" y="130" text-anchor="middle" class="ch">Decide</text>',
           '  <text x="1010" y="130" text-anchor="middle" class="ch">Entrega</text>',
           '  <text x="90" y="130" text-anchor="middle" class="axh">Hierarquia</text>',
           '  <text x="90" y="150" text-anchor="middle" class="axh">de serviços</text>']
    ys = [160, 330, 500, 670]
    for (key, nome, pergunta, recebe, decide, entrega, eixo), y in zip(DOMINIOS, ys):
        out.append(f'  <rect x="190" y="{y}" width="990" height="150" rx="14" fill="white" stroke="#9AA9BC" stroke-width="2"/>')
        out.append(f'  <text x="206" y="{y + 28}" class="d">{nome}</text>')
        out.append(f'  <text x="{206 + len(nome) * 12 + 18}" y="{y + 28}" class="q">{pergunta}</text>')
        cell(out, 206, y + 48, 290, 86, recebe, "#F2F6FB", "#9AA9BC")
        cell(out, 520, y + 48, 320, 86, decide, "#FFF1D6", "#F2B84B")
        cell(out, 864, y + 48, 300, 86, entrega, "#F2F6FB", "#9AA9BC")
        out.append(f'  <rect x="20" y="{y + 30}" width="140" height="90" rx="12" fill="#D8E9FF" stroke="#254DB8" stroke-width="2"/>')
        top = y + 75 - (len(eixo) - 1) * 10 + 6
        for i, line in enumerate(eixo):
            out.append(f'  <text x="90" y="{top + i * 20:.0f}" text-anchor="middle" class="ax">{line}</text>')
        if y != ys[-1]:
            out.append(f'  <path d="M90 {y + 120}V{y + 198}" stroke="#254DB8" stroke-width="2.5" fill="none" marker-end="url(#a)"/>')
    out.append('  <path d="M351 100V206" stroke="#52657E" stroke-width="2.5" fill="none" marker-end="url(#a)"/>')
    for y in ys[:-1]:
        out.append(f'  <path d="M1014 {y + 134}V{y + 160}H351V{y + 216}" stroke="#52657E" stroke-width="2.5" fill="none" marker-end="url(#a)"/>')
    out.append(f'  <path d="M1014 {ys[-1] + 134}V{ys[-1] + 168}" stroke="#52657E" stroke-width="2.5" fill="none" marker-end="url(#a)"/>')
    out.append('  <rect x="190" y="840" width="990" height="42" rx="21" fill="#16243A"/>')
    out.append('  <text x="685" y="867" text-anchor="middle" class="b w">Aula 5: definição tecnológica</text>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


def mapa(ativo):
    w, h = 1200, 300
    nome_ativo = next(n for k, n, *_ in DOMINIOS if k == ativo)
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
           f'  <title id="title">Mapa do bloco 0 com o domínio de {nome_ativo.lower()} em destaque</title>'
           f'<desc id="desc">Quatro faixas empilhadas com os domínios negócio, dados, aplicações e infraestrutura e o que o '
           f'arquiteto decide em cada um. A faixa do domínio de {nome_ativo.lower()} aparece em destaque e as demais aparecem '
           f'esmaecidas.</desc>',
           f'  <defs>{STYLE}</defs>',
           f'  <rect width="{w}" height="{h}" rx="20" fill="#F2F6FB"/>']
    for i, (key, nome, _p, _r, decide, _e, _x) in enumerate(DOMINIOS):
        y = 20 + i * 66
        on = key == ativo
        fill, stroke, op = ("#FFF1D6", "#F2B84B", "") if on else ("white", "#9AA9BC", ' opacity="0.45"')
        out.append(f'  <g{op}><rect x="20" y="{y}" width="1160" height="56" rx="12" fill="{fill}" stroke="{stroke}" stroke-width="{4 if on else 2}"/>')
        out.append(f'  <text x="44" y="{y + 36}" class="d">{nome}</text>')
        out.append(f'  <text x="260" y="{y + 36}" class="c" style="font-size:19px">Decide: {" ".join(decide)}</text></g>')
    out.append("</svg>")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    (OUT / "modulo-4-b0-espinha-dorsal.svg").write_text(central(), encoding="utf-8")
    for key, *_ in DOMINIOS:
        (OUT / f"modulo-4-b0-mapa-{key}.svg").write_text(mapa(key), encoding="utf-8")
    print("ok")
```

- [ ] **Step 2: Gerar e conferir os SVGs**

Run:
```bash
python3 scripts/figuras_bloco_0.py
python3 - <<'EOF'
import re
from pathlib import Path
for p in sorted(Path("docs/assets/images").glob("modulo-4-b0-*.svg")):
    t = p.read_text()
    sizes = [int(s) for s in re.findall(r"font-size:(\d+)px", t)]
    assert re.search(r"<title[^>]*>[^<]{5,}</title>", t), p
    assert re.search(r"<desc[^>]*>[^<]{20,}</desc>", t), p
    assert sizes and min(sizes) >= 16, p
    for term in ("ACME", "COBOL", "CICS", "matrícula", "Matrícula"):
        assert term not in t, (p, term)
    print("ok", p.name)
EOF
```
Expected: `ok` do script e uma linha `ok modulo-4-b0-...svg` para cada um dos cinco arquivos.

- [ ] **Step 3: Conferir a renderização a 688 px**

Abra cada SVG numa página HTML com `<img style="width:688px">` e capture com Playwright (ou com `qlmanage -t -s 1200` no macOS). Verifique: nenhum texto sai da sua caixa, nenhuma seta cruza texto, as perguntas cabem na linha da camada. Se a pergunta de uma camada ultrapassar x = 1160, quebre-a em duas linhas no script, ajustando a coordenada y.

- [ ] **Step 4: Commit**

```bash
git add scripts/figuras_bloco_0.py docs/assets/images/modulo-4-b0-*.svg
git commit -m "feat(aula-4): figuras do bloco 0

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 3: Página do bloco 0 e navegação

**Files:**
- Create: `docs/modulo-4-dominios-da-solucao/bloco-0-espinha-dorsal-dos-dominios.md`
- Modify: `mkdocs.yml` (linha com `- Visão geral: modulo-4-dominios-da-solucao/index.md`)
- Test: `tests/test_modulo_4_contract.py`

**Interfaces:**
- Consumes: `modulo-4-b0-espinha-dorsal.svg` (Tarefa 2), dispensa do Exercício no validador (Tarefa 1).
- Produces: a página `bloco-0-espinha-dorsal-dos-dominios.md` com a seção "Uso pelo arquiteto" contendo as quatro perguntas exatas listadas no Step 3, que a Tarefa 4 copia para os blocos 1 a 4.

- [ ] **Step 1: Escrever os testes que falham**

Em `tests/test_modulo_4_contract.py`, logo após a definição de `BLOCKS`, acrescente:

```python
B0 = "bloco-0-espinha-dorsal-dos-dominios.md"

ROTEIRO = {
    B1: "Que capacidades, etapas do fluxo de valor e atividades a solução altera, segundo os modelos que a arquitetura de negócio já mantém?",
    B2: "Que entidades sustentam as capacidades afetadas, quem é o dono de cada uma, onde fica a fonte de verdade, com que regime cada cópia a reflete e que obrigações o dado carrega?",
    B3: "Que aplicações mudam, por quais interfaces trocam essas entidades, que contrato governa cada interface e onde passa a fronteira da solução?",
    B4: "Em que nó cada contêiner executa, com que modo, volume e latência cada relação opera e o que fica como exigência para a definição tecnológica?",
}
```

E, antes de `class ExerciseRuleTest`, a classe:

```python
class BlockZeroTest(unittest.TestCase):
    """Bloco 0 de 03/10/2026: o trabalho do arquiteto nos quatro dominios."""

    def test_page_exists_and_is_in_nav(self):
        self.assertTrue((MODULE / B0).is_file())
        nav = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        self.assertIn(f"modulo-4-dominios-da-solucao/{B0}", nav)
        self.assertLess(nav.index(f"modulo-4-dominios-da-solucao/{B0}"),
                        nav.index(f"modulo-4-dominios-da-solucao/{B1}"))

    def test_page_is_conceptual_and_has_no_exercise(self):
        text = read(B0)
        self.assertNotRegex(text, r"(?m)^## Exerc[ií]cio")
        for term in ("ACME", "Hospital", "Clínica", "COBOL", "matrícula"):
            with self.subTest(term=term):
                self.assertNotIn(term, text)

    def test_page_covers_the_four_domains_and_the_three_columns(self):
        body = without_sources(read(B0)).lower()
        for term in ("negócio", "dados", "aplicações", "infraestrutura", "recebe", "decide", "entrega"):
            with self.subTest(term=term):
                self.assertIn(term, body)

    def test_page_shows_the_central_figure(self):
        self.assertRegex(
            read(B0),
            r"!\[[^\]]{40,}\]\(\.\./assets/images/modulo-4-b0-espinha-dorsal\.svg\)\{ \.module-diagram \}",
        )

    def test_page_lists_the_four_questions(self):
        uso = section(read(B0), "Uso pelo arquiteto")
        for name, question in ROTEIRO.items():
            with self.subTest(block=name):
                self.assertIn(question, uso)
```

- [ ] **Step 2: Rodar e ver falhar**

Run: `python3 -m pytest -q tests/test_modulo_4_contract.py -k BlockZeroTest`
Expected: FAIL nos cinco testes (arquivo inexistente).

- [ ] **Step 3: Criar a página**

Conteúdo integral de `docs/modulo-4-dominios-da-solucao/bloco-0-espinha-dorsal-dos-dominios.md`:

````markdown
# Os quatro domínios numa só solução

Este bloco apresenta, antes do detalhamento de cada domínio, o que o arquiteto de solução recebe, decide e entrega nos domínios de negócio, dados, aplicações e infraestrutura, e como a decisão tomada num domínio se torna a entrada do domínio seguinte.

## Antes de começar

- [Arquiteto de solução](../referencia/glossario.md#arquiteto-de-solucao)
- [Arquitetura de solução](../referencia/glossario.md#arquitetura-de-solucao)
- [Componentes da solução](../referencia/glossario.md#componentes-da-solucao)
- [ADR](../referencia/glossario.md#adr)

## O trabalho do arquiteto nos quatro domínios

O arquiteto de solução trabalha sobre uma única solução, delimitada pela declaração de escopo, e a detalha em quatro domínios, na ordem negócio, dados, aplicações e infraestrutura. Em cada domínio, ele consulta os modelos que a arquitetura corporativa e as áreas especialistas já mantêm, decide o que é próprio da solução e entrega ao domínio seguinte a decisão de que ele precisa, como parte do papel apresentado no [bloco 3 da Aula 1](../modulo-1-fundamentos/bloco-3-papel-do-arquiteto-de-solucao.md). O percurso parte do estilo e dos padrões registrados no [ADR da Aula 3](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md) e termina nas exigências que a definição tecnológica da Aula 5 recebe.

A Figura 1 organiza esse percurso em quatro camadas, cada uma com a pergunta que o arquiteto responde e três colunas. A coluna Recebe registra o que chega ao domínio e de quem, a coluna Decide registra o trabalho próprio do arquiteto, e a coluna Entrega registra o produto que segue para o domínio seguinte, indicado pelas setas que ligam a coluna Entrega de uma camada à coluna Recebe da camada abaixo.

<figure markdown="span">
![Quatro camadas empilhadas, negócio, dados, aplicações e infraestrutura, entre a faixa de entrada com o estilo e os padrões registrados em ADR na Aula 3 e a faixa de saída com a definição tecnológica da Aula 5. Cada camada traz a pergunta do arquiteto e as colunas recebe, decide e entrega, com a coluna decide em destaque, e setas ortogonais ligam a entrega de cada camada ao que a camada seguinte recebe. À esquerda, a hierarquia de serviços acompanha as camadas.](../assets/images/modulo-4-b0-espinha-dorsal.svg){ .module-diagram }
</figure>

*Figura 1 — O que o arquiteto de solução recebe, decide e entrega em cada domínio, com o encadeamento entre os domínios. Fonte: material do curso, com base em Lovatt (2021).*

### O que o arquiteto faz em cada domínio

A tabela detalha as três colunas da Figura 1 e acrescenta o limite do papel, isto é, o trabalho que o arquiteto de solução consulta ou solicita, sem assumir como tarefa própria.

| Domínio | Recebe, e de quem | Decide | Produz | Trabalho que não assume |
| --- | --- | --- | --- | --- |
| Negócio | Mapa de capacidades, fluxo de valor e modelo de processo, da arquitetura corporativa e da análise de negócio | Capacidades, etapas e atividades em que a mudança incide | Recorte dos modelos de negócio com a mudança localizada | Modelagem de processos, que cabe à análise de negócio |
| Dados | Capacidades afetadas e modelo de dados corporativo, da arquitetura de dados | Dono, fonte de verdade, regime de consistência e obrigações de cada entidade | Grade dado × aplicação | Manutenção do modelo de dados corporativo, que cabe à arquitetura de dados |
| Aplicações | Grade dado × aplicação e portfólio de aplicações | Aplicações que mudam, interfaces, contratos e fronteira da solução | Diagramas de contexto e de contêineres e contratos de integração | Escolha de produto e de framework, que cabe à definição tecnológica da Aula 5 |
| Infraestrutura | Contêineres e relações, do domínio de aplicações | Modo, volume e latência de cada relação, camada de execução e topologia | Diagrama de implantação e exigências para a definição tecnológica | Operação da plataforma, que cabe à área de infraestrutura |

Quando um insumo da coluna Recebe não existe, o arquiteto registra a ausência como risco e solicita o artefato à área responsável, procedimento que o [bloco 1](bloco-1-arquitetura-de-negocio.md) detalha para os modelos de negócio.

### A ordem dos domínios

Todos os componentes da solução sustentam, em última instância, um ou mais serviços de negócio. A hierarquia de serviços vai do serviço de negócio, realizado por processos de negócio, ao serviço de aplicação, oferecido por componentes de aplicação, e ao serviço de tecnologia, que executa esses componentes, e os dados atravessam a hierarquia como a informação que os serviços consomem e produzem. A ordem dos domínios acompanha essa hierarquia de cima para baixo, porque cada domínio se justifica pelo serviço que sustenta no domínio acima, e o [bloco 3](bloco-3-arquitetura-de-aplicacoes-e-integracao.md#hierarquia-de-servicos) retoma a hierarquia ao tratar dos contratos de integração.

## Uso pelo arquiteto

O arquiteto entra em cada domínio com uma pergunta, e a resposta de cada pergunta é a entrada da pergunta seguinte. Os blocos 1 a 4 retomam a pergunta do respectivo domínio, com a mesma redação.

1. Negócio: Que capacidades, etapas do fluxo de valor e atividades a solução altera, segundo os modelos que a arquitetura de negócio já mantém?
2. Dados: Que entidades sustentam as capacidades afetadas, quem é o dono de cada uma, onde fica a fonte de verdade, com que regime cada cópia a reflete e que obrigações o dado carrega?
3. Aplicações: Que aplicações mudam, por quais interfaces trocam essas entidades, que contrato governa cada interface e onde passa a fronteira da solução?
4. Infraestrutura: Em que nó cada contêiner executa, com que modo, volume e latência cada relação opera e o que fica como exigência para a definição tecnológica?

## Fontes

As referências seguem o formato APA, 7ª edição, e constam da [bibliografia](../referencia/bibliografia.md) do curso. O trecho consultado aparece entre parênteses ao fim de cada entrada.

- Lovatt, M. (2021). *Solution architecture foundations*. BCS, The Chartered Institute for IT. (seções 1.5 a 1.7, papel do arquiteto de solução, e seções 2.3 a 2.7, domínios da arquitetura)

**Material do curso.** O bloco usa as entradas [arquiteto de solução](../referencia/glossario.md#arquiteto-de-solucao), [arquitetura de solução](../referencia/glossario.md#arquitetura-de-solucao), [componentes da solução](../referencia/glossario.md#componentes-da-solucao) e [ADR](../referencia/glossario.md#adr) do glossário.
````

Antes de salvar, confirme no glossário que as âncoras `arquiteto-de-solucao`, `arquitetura-de-solucao`, `componentes-da-solucao` e `adr` existem (`grep -n "^## Arquiteto de solução\|^## Arquitetura de solução\|^## Componentes da solução\|^## ADR" docs/referencia/glossario.md`) e que o bloco 3 tem o título `### Hierarquia de serviços`.

- [ ] **Step 4: Navegação**

Em `mkdocs.yml`, logo depois de `      - Visão geral: modulo-4-dominios-da-solucao/index.md`, acrescente:

```yaml
      - "Bloco 0: os quatro domínios numa só solução": modulo-4-dominios-da-solucao/bloco-0-espinha-dorsal-dos-dominios.md
```

- [ ] **Step 5: Rodar e ver passar**

Run: `python3 -m pytest -q tests/test_modulo_4_contract.py -k "BlockZeroTest or SelfContained" && python3 scripts/validate_content.py | tail -1`
Expected: PASS e `Resumo: 0 violacao(oes).`

- [ ] **Step 6: Commit**

```bash
git add docs/modulo-4-dominios-da-solucao/bloco-0-espinha-dorsal-dos-dominios.md mkdocs.yml tests/test_modulo_4_contract.py
git commit -m "feat(aula-4): bloco 0, os quatro dominios numa so solucao

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 4: Retomadas nos blocos 1 a 4

**Files:**
- Modify: `docs/modulo-4-dominios-da-solucao/bloco-1-arquitetura-de-negocio.md`, `bloco-2-arquitetura-de-dados.md`, `bloco-3-arquitetura-de-aplicacoes-e-integracao.md`, `bloco-4-arquitetura-de-infraestrutura.md`
- Test: `tests/test_modulo_4_contract.py`

**Interfaces:**
- Consumes: `ROTEIRO` e `B0` (Tarefa 3), figuras `modulo-4-b0-mapa-*.svg` (Tarefa 2).
- Produces: nada consumido por tarefas seguintes.

- [ ] **Step 1: Escrever os testes que falham**

Acrescente à classe `BlockZeroTest`:

```python
    MAPAS = {B1: "negocio", B2: "dados", B3: "aplicacoes", B4: "infraestrutura"}

    def test_each_block_opens_with_its_own_map(self):
        for name, key in self.MAPAS.items():
            body = concept(read(name))
            with self.subTest(page=name):
                self.assertIn(B0, body)
                self.assertRegex(
                    body,
                    rf"!\[[^\]]{{40,}}\]\(\.\./assets/images/modulo-4-b0-mapa-{key}\.svg\)\{{ \.module-diagram \}}",
                )
                for other in set(self.MAPAS.values()) - {key}:
                    self.assertNotIn(f"modulo-4-b0-mapa-{other}.svg", body)

    def test_each_block_repeats_its_question_verbatim(self):
        for name, question in ROTEIRO.items():
            with self.subTest(page=name):
                self.assertIn(question, section(read(name), "Uso pelo arquiteto"))

    def test_block_3_hierarchy_points_back_to_block_0(self):
        text = read(B3)
        start = text.index("### Hierarquia de serviços")
        self.assertIn(B0, text[start:start + 1500])

    def test_synthesis_chain_points_to_block_0(self):
        self.assertIn(B0, section(read("sintese.md"), "Cadeia dos domínios"))
```

- [ ] **Step 2: Rodar e ver falhar**

Run: `python3 -m pytest -q tests/test_modulo_4_contract.py -k BlockZeroTest`
Expected: FAIL nos quatro testes novos.

- [ ] **Step 3: Abertura de cada bloco**

Bloco 1: substitua o primeiro parágrafo depois de `## Modelos de arquitetura de negócio` (o que começa com "A Aula 3 terminou com uma decisão estrutural registrada em [ADR]") pelo trecho:

````markdown
<figure markdown="span">
![Mapa do bloco 0 com quatro faixas empilhadas, negócio, dados, aplicações e infraestrutura, e o que o arquiteto decide em cada uma, com a faixa do negócio em destaque e as demais esmaecidas.](../assets/images/modulo-4-b0-mapa-negocio.svg){ .module-diagram }
</figure>

No mapa do [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md), este bloco trata do domínio de negócio, o primeiro dos quatro. O arquiteto recebe o mapa de capacidades, o fluxo de valor e o modelo de processo mantidos pela arquitetura corporativa e pela análise de negócio, decide em que capacidades, etapas e atividades a mudança incide e entrega ao bloco 2 as capacidades afetadas, sobre a forma estrutural registrada no [ADR](../modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md) da Aula 3.
````

Bloco 2: insira, logo depois de `## Dados na solução` e antes do parágrafo que começa com "A DAMA International", o trecho:

````markdown
<figure markdown="span">
![Mapa do bloco 0 com quatro faixas empilhadas, negócio, dados, aplicações e infraestrutura, e o que o arquiteto decide em cada uma, com a faixa de dados em destaque e as demais esmaecidas.](../assets/images/modulo-4-b0-mapa-dados.svg){ .module-diagram }
</figure>

No mapa do [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md), este bloco trata do domínio de dados. O arquiteto recebe as capacidades afetadas, localizadas no [bloco 1](bloco-1-arquitetura-de-negocio.md), e o modelo de dados corporativo, decide o dono, a fonte de verdade, o regime de consistência e as obrigações de cada entidade e entrega ao bloco 3 a grade dado × aplicação.
````

Bloco 3: insira, logo depois de `## Aplicações, interfaces e contexto` e antes do parágrafo que começa com "A arquitetura de aplicações é o subdomínio", o trecho:

````markdown
<figure markdown="span">
![Mapa do bloco 0 com quatro faixas empilhadas, negócio, dados, aplicações e infraestrutura, e o que o arquiteto decide em cada uma, com a faixa de aplicações em destaque e as demais esmaecidas.](../assets/images/modulo-4-b0-mapa-aplicacoes.svg){ .module-diagram }
</figure>

No mapa do [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md), este bloco trata do domínio de aplicações. O arquiteto recebe a grade dado × aplicação, produzida no [bloco 2](bloco-2-arquitetura-de-dados.md), e o portfólio de aplicações, decide que aplicações mudam, por quais interfaces e contratos elas trocam dados e onde passa a fronteira da solução, e entrega ao bloco 4 os diagramas de contexto e de contêineres e os contratos de integração.
````

Bloco 4: insira, logo depois de `## Infraestrutura e contêineres` e antes do parágrafo que começa com "A **arquitetura de infraestrutura**", o trecho:

````markdown
<figure markdown="span">
![Mapa do bloco 0 com quatro faixas empilhadas, negócio, dados, aplicações e infraestrutura, e o que o arquiteto decide em cada uma, com a faixa de infraestrutura em destaque e as demais esmaecidas.](../assets/images/modulo-4-b0-mapa-infraestrutura.svg){ .module-diagram }
</figure>

No mapa do [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md), este bloco trata do domínio de infraestrutura, o último dos quatro. O arquiteto recebe os contêineres e as relações definidos no [bloco 3](bloco-3-arquitetura-de-aplicacoes-e-integracao.md), decide o modo, o volume e a latência de cada relação, a camada de execução e a topologia, e entrega o diagrama de implantação e as exigências que a definição tecnológica da Aula 5 recebe.
````

- [ ] **Step 4: Pergunta no "Uso pelo arquiteto" de cada bloco**

Em cada bloco, insira como primeiro parágrafo da seção `## Uso pelo arquiteto` a frase abaixo, com a pergunta exata do `ROTEIRO` correspondente:

- Bloco 1: `A pergunta do arquiteto neste domínio, no roteiro do [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md), é a seguinte. Que capacidades, etapas do fluxo de valor e atividades a solução altera, segundo os modelos que a arquitetura de negócio já mantém?`
- Bloco 2: `A pergunta do arquiteto neste domínio, no roteiro do [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md), é a seguinte. Que entidades sustentam as capacidades afetadas, quem é o dono de cada uma, onde fica a fonte de verdade, com que regime cada cópia a reflete e que obrigações o dado carrega?`
- Bloco 3: `A pergunta do arquiteto neste domínio, no roteiro do [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md), é a seguinte. Que aplicações mudam, por quais interfaces trocam essas entidades, que contrato governa cada interface e onde passa a fronteira da solução?`
- Bloco 4: `A pergunta do arquiteto neste domínio, no roteiro do [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md), é a seguinte. Em que nó cada contêiner executa, com que modo, volume e latência cada relação opera e o que fica como exigência para a definição tecnológica?`

- [ ] **Step 5: Hierarquia de serviços no bloco 3 e síntese**

No bloco 3, troque o início do primeiro parágrafo depois de `### Hierarquia de serviços`, "As relações entre os domínios se organizam numa hierarquia de camadas, em que cada camada depende apenas da imediatamente inferior.", por "A hierarquia de serviços apresentada no [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md#a-ordem-dos-dominios) organiza as relações entre os domínios em camadas, em que cada camada depende apenas da imediatamente inferior." O restante do parágrafo fica igual.

Na `sintese.md`, troque a frase de abertura da seção `## Cadeia dos domínios`, "A aula detalha uma única solução por domínios, e cada exercício consome o produto do anterior.", por "A aula detalha uma única solução por domínios, no encadeamento apresentado no [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md), e cada exercício consome o produto do anterior."

- [ ] **Step 6: Rodar e ver passar**

Run: `python3 -m pytest -q && python3 scripts/validate_content.py | tail -1`
Expected: todos PASS e `Resumo: 0 violacao(oes).`

- [ ] **Step 7: Commit**

```bash
git add docs/modulo-4-dominios-da-solucao tests/test_modulo_4_contract.py
git commit -m "feat(aula-4): blocos 1 a 4 retomam o mapa do bloco 0

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 5: Grade, roteiro, cronograma e glossário

**Files:**
- Modify: `docs/modulo-4-dominios-da-solucao/index.md`, `docs/cronograma.md`, `docs/referencia/glossario.md`
- Test: `tests/test_exercicios_fora_da_sala.py`, `tests/test_modulo_4_contract.py`

**Interfaces:**
- Consumes: página do bloco 0 (Tarefa 3).
- Produces: nada.

- [ ] **Step 1: Escrever os testes que falham**

Em `tests/test_exercicios_fora_da_sala.py`, dentro de `test_time_grids_have_no_exercise_minutes`, troque as três linhas do ramo `if "| Horário | Atividade |" in text:` por:

```python
                    # Grade com Kahoot, adotada a partir da Aula 3: 130 minutos de blocos,
                    # contando o bloco 0 quando a aula tem abertura conceitual.
                    rows = re.findall(r"^\| [\dh–]+ \| Bloco [0-4],.*\| (\d+) \|\s*$", text, re.MULTILINE)
                    has_zero = re.search(r"^\| [\dh–]+ \| Bloco 0,", text, re.MULTILINE) is not None
                    self.assertEqual(5 if has_zero else 4, len(rows))
                    self.assertEqual(130, sum(int(r) for r in rows))
                    self.assertEqual(3, len(re.findall(r"^\| [\dh–]+ \| Kahoot", text, re.MULTILINE)))
```

Em `tests/test_modulo_4_contract.py`, acrescente à classe `BlockZeroTest`:

```python
    def test_index_schedule_and_route_include_block_0(self):
        text = read("index.md")
        self.assertRegex(text, r"(?m)^\| 19h25–19h35 \| Bloco 0, os quatro domínios numa só solução \| 10 \|\s*$")
        self.assertIn(B0, section(text, "Roteiro da aula"))

    def test_schedule_page_lists_block_0(self):
        text = (DOCS / "cronograma.md").read_text(encoding="utf-8")
        aula4 = re.search(r"### Aula 4.*?(?=### Aula 5)", text, re.DOTALL).group(0)
        self.assertRegex(aula4, r"(?m)^\| 0 \| ")

    def test_glossary_defines_the_backbone(self):
        text = (DOCS / "referencia" / "glossario.md").read_text(encoding="utf-8")
        self.assertRegex(text, r"(?m)^## Espinha dorsal dos domínios\s*$")
```

- [ ] **Step 2: Rodar e ver falhar**

Run: `python3 -m pytest -q tests/test_exercicios_fora_da_sala.py tests/test_modulo_4_contract.py -k "time_grids or index_schedule or schedule_page or glossary_defines_the_backbone"`
Expected: `test_time_grids_have_no_exercise_minutes` PASS (a grade ainda não tem bloco 0) e os três testes de `BlockZeroTest` FAIL.

- [ ] **Step 3: Grade e roteiro no índice da Aula 4**

Em `docs/modulo-4-dominios-da-solucao/index.md`, substitua as três linhas da grade

```
| 19h25–19h58 | Bloco 1, arquitetura de negócio da solução | 33 |
| 19h58–20h30 | Bloco 2, arquitetura de dados da solução | 32 |
```

por

```
| 19h25–19h35 | Bloco 0, os quatro domínios numa só solução | 10 |
| 19h35–20h03 | Bloco 1, arquitetura de negócio da solução | 28 |
| 20h03–20h30 | Bloco 2, arquitetura de dados da solução | 27 |
```

Na seção `## Objetivos de aprendizagem`, acrescente como primeiro item da lista:

```
- descrever, para cada domínio da solução, o que o arquiteto de solução recebe, decide e entrega, e o que o domínio seguinte consome
```

Na seção `## Roteiro da aula`, acrescente como primeiro parágrafo:

```
O [bloco 0](bloco-0-espinha-dorsal-dos-dominios.md) abre a aula com o modelo que os blocos seguintes detalham, em que cada domínio aparece com o que o arquiteto de solução recebe, decide e entrega, e com a pergunta que ele responde. A abertura não tem exercício, e os blocos 1 a 4 começam pela mesma figura, com o próprio domínio em destaque.
```

Se o texto da seção `## Grade de tempo` mencionar a duração ou a quantidade de blocos ("quatro blocos"), ajuste para "o bloco 0 e os quatro blocos".

- [ ] **Step 4: Cronograma e glossário**

Em `docs/cronograma.md`, na tabela de `### Aula 4, domínios da arquitetura de solução`, acrescente antes da linha do bloco 1:

```
| 0 | Os quatro domínios numa só solução, com o que o arquiteto recebe, decide e entrega | Sem exercício |
```

Em `docs/referencia/glossario.md`, acrescente depois da entrada `## Arquitetura de solução` e do seu parágrafo:

```
## Espinha dorsal dos domínios

Modelo apresentado no bloco 0 da Aula 4 que mostra, para os domínios de negócio, dados, aplicações e infraestrutura, o que o arquiteto de solução recebe, decide e entrega, e como a entrega de cada domínio se torna a entrada do domínio seguinte.
```

- [ ] **Step 5: Rodar e ver passar**

Run: `python3 -m pytest -q && python3 scripts/validate_content.py | tail -1 && DISABLE_MKDOCS_2_WARNING=true mkdocs build --strict -d /tmp/site-bloco-0 2>&1 | grep -i "error\|built"`
Expected: todos PASS, `Resumo: 0 violacao(oes).` e `Documentation built`.

- [ ] **Step 6: Commit**

```bash
git add docs/modulo-4-dominios-da-solucao/index.md docs/cronograma.md docs/referencia/glossario.md tests/test_exercicios_fora_da_sala.py tests/test_modulo_4_contract.py
git commit -m "feat(aula-4): grade, roteiro e glossario com o bloco 0

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Task 6: Conferência visual e revisão final

**Files:**
- Nenhum arquivo novo. Ajustes pontuais em `scripts/figuras_bloco_0.py` e nos SVGs gerados, se a conferência apontar problema.

**Interfaces:**
- Consumes: tudo das Tarefas 1 a 5.
- Produces: nada.

- [ ] **Step 1: Gerar o site e capturar as figuras**

```bash
DISABLE_MKDOCS_2_WARNING=true mkdocs build -q -d /tmp/site-bloco-0
(cd /tmp/site-bloco-0 && python3 -m http.server 8765 >/dev/null 2>&1 &)
```

Com Playwright (Chromium), abra a 1424 px de largura as páginas `modulo-4-dominios-da-solucao/bloco-0-espinha-dorsal-dos-dominios/` e `bloco-1` a `bloco-4`, e capture cada `img.module-diagram` cujo `src` contenha `modulo-4-b0-`.

- [ ] **Step 2: Verificar**

Para cada captura: texto legível na coluna de 688 px, nenhum texto fora da caixa, nenhuma seta sobre texto, a figura reduzida de cada bloco com o domínio certo em destaque. Corrija no script, regenere com `python3 scripts/figuras_bloco_0.py` e repita até passar.

- [ ] **Step 3: Revisão de texto**

Leia a página do bloco 0 e as quatro frases de abertura procurando as construções proibidas listadas em Global Constraints. Corrija o que encontrar.

- [ ] **Step 4: Verificação final e commit**

Run: `python3 -m pytest -q && python3 scripts/validate_content.py | tail -1 && DISABLE_MKDOCS_2_WARNING=true mkdocs build --strict -d /tmp/site-bloco-0 2>&1 | grep -i "error\|built"`
Expected: todos PASS, `Resumo: 0 violacao(oes).` e `Documentation built`.

```bash
git add -A scripts/figuras_bloco_0.py docs
git commit -m "fix(aula-4): ajustes visuais e de texto do bloco 0

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

Se nada mudou nos Steps 2 e 3, não há commit nesta tarefa.
