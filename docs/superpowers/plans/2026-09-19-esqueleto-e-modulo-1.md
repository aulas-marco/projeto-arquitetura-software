# Site da disciplina Estratégias e Projeto de Arquitetura de Software, esqueleto e Módulo 1

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Converter o repositório de 21 arquivos Markdown soltos em um site MkDocs Material navegável, com o dossiê do caso ACME aprofundado e as quatro páginas de bloco do Módulo 1 escritas.

**Architecture:** MkDocs Material em português do Brasil, um diretório por módulo com quatro páginas de bloco mais índice e síntese, caso ACME em trilha separada das páginas de teoria, diagramas em Mermaid renderizados no cliente. Um validador de conteúdo em Python aplica mecanicamente as regras editoriais do professor, porque releitura manual já falhou repetidamente nessas mesmas regras.

**Tech Stack:** Python 3, mkdocs-material 9.7.6, Mermaid 11.12.2 via CDN, pymdownx superfences e details, unittest.

**Spec:** `docs/superpowers/specs/2026-09-19-estrutura-do-curso-design.md`

## Global Constraints

- Idioma: português do Brasil em todo o conteúdo, interface e mensagens do validador
- Dependência única: `mkdocs-material==9.7.6`, instalada em ambiente virtual local em `.venv`
- Mermaid: versão 11.12.2, importada de `https://cdn.jsdelivr.net/npm/mermaid@11.12.2/dist/mermaid.esm.min.mjs`
- Pontuação: zero ponto-e-vírgula em prosa, travessão apenas como aposto isolado e no máximo um por parágrafo
- Tom: expositivo e impessoal, definição formal antes do exemplo, sem abertura com cena, sem frase de efeito isolada, sem pergunta retórica, sem metáfora explicativa, sem fecho sentencioso
- Exemplos: ao menos dois domínios distintos por seção de conceito, sem repetir o mesmo domínio principal em blocos consecutivos
- Títulos: funcionais, sem subtítulo após travessão ou dois-pontos, sem abrir com "Por que"
- Datas visíveis ao leitor no formato DD/MM/AAAA
- Toda página é autocontida: o primeiro uso de ACME em qualquer página traz uma frase de reintrodução
- Anatomia fixa da página de bloco: oito seções na ordem definida na seção 5 do spec
- Nenhum enunciado de exercício manda o aluno abrir outra página para localizar informação

---

### Task 1: Esqueleto MkDocs que compila

**Files:**
- Create: `requirements.txt`
- Create: `mkdocs.yml`
- Create: `.gitignore`
- Create: `docs/index.md`
- Create: `docs/assets/javascripts/mermaid.mjs`
- Create: `docs/assets/stylesheets/extra.css`

**Interfaces:**
- Consumes: nada
- Produces: site que compila com `mkdocs build --strict`, diretório `docs/` como raiz do conteúdo, classes CSS `course-*` disponíveis para as tarefas seguintes

- [ ] **Step 1: Criar o ambiente virtual e a lista de dependências**

```bash
cd ~/code/projeto-arquitetura-software
python3 -m venv .venv
printf 'mkdocs-material==9.7.6\n' > requirements.txt
.venv/bin/pip install -r requirements.txt
```

- [ ] **Step 2: Criar o `.gitignore`**

```
.venv/
site/
__pycache__/
*.pyc
.DS_Store
```

- [ ] **Step 3: Criar `docs/assets/javascripts/mermaid.mjs`**

```javascript
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11.12.2/dist/mermaid.esm.min.mjs";

mermaid.initialize({
  startOnLoad: false,
  securityLevel: "strict",
  theme: "base",
  fontFamily: 'Inter, "Segoe UI", system-ui, sans-serif',
  themeVariables: {
    primaryColor: "#F2F6FB",
    primaryTextColor: "#16243A",
    primaryBorderColor: "#254DB8",
    lineColor: "#254DB8",
    secondaryColor: "#DDF3F6",
    tertiaryColor: "#FFF7E3",
  },
});

window.mermaid = mermaid;

async function renderMermaid(root = document) {
  const nodes = root.querySelectorAll("pre.mermaid:not([data-processed])");
  if (!nodes.length) return;
  await mermaid.run({ nodes });
}

function renderCurrentDocument(root) {
  renderMermaid(root).catch((error) => {
    console.error("Falha ao renderizar diagrama Mermaid", error);
  });
}

if (window.document$ && typeof window.document$.subscribe === "function") {
  document$.subscribe(({ body } = {}) => renderCurrentDocument(body || document));
} else {
  window.addEventListener(
    "DOMContentLoaded",
    () => renderCurrentDocument(document),
    { once: true },
  );
}
```

- [ ] **Step 4: Criar `docs/assets/stylesheets/extra.css` com a paleta do curso**

```css
:root {
  --course-ink: #16243A;
  --course-cobalt: #254DB8;
  --course-cyan: #5FC0D1;
  --course-paper: #F2F6FB;
  --course-white: #FFFFFF;
  --course-amber: #F2B84B;

  --md-primary-fg-color: var(--course-ink);
  --md-primary-fg-color--light: #293B57;
  --md-primary-fg-color--dark: #0D1727;
  --md-accent-fg-color: var(--course-cobalt);
  --md-typeset-a-color: var(--course-cobalt);
  --md-default-fg-color: var(--course-ink);
  --md-default-bg-color: var(--course-paper);
}

.md-typeset table:not([class]) {
  font-size: 0.75rem;
}

.md-typeset details {
  border-left: 0.2rem solid var(--course-cobalt);
}

.md-typeset .grade-tempo td:first-child {
  white-space: nowrap;
}
```

- [ ] **Step 5: Criar `mkdocs.yml` com a navegação completa das seis aulas**

```yaml
site_name: Estratégias e Projeto de Arquitetura de Software
site_description: Material da disciplina do IEC/PUC Minas, turmas Arq. Software Distribuído 10.1 e Arq. Soluções Digitais 1.1
use_directory_urls: true
exclude_docs: |
  superpowers/**

theme:
  name: material
  language: pt-BR
  font: false
  palette:
    scheme: default
    primary: custom
    accent: custom
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.indexes
    - navigation.top
    - navigation.footer
    - content.code.copy
    - search.suggest

extra_css:
  - assets/stylesheets/extra.css

extra_javascript:
  - assets/javascripts/mermaid.mjs

markdown_extensions:
  - toc:
      permalink: true
  - tables
  - footnotes
  - attr_list
  - md_in_html
  - pymdownx.details
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format

nav:
  - Início: index.md
  - Cronograma: cronograma.md
  - "Aula 1 — Fundamentos":
      - Visão geral: modulo-1-fundamentos/index.md
      - "Bloco 1: arquitetura e papel do arquiteto": modulo-1-fundamentos/bloco-1-arquitetura-e-papel-do-arquiteto.md
      - "Bloco 2: qualidade e tipos de requisito": modulo-1-fundamentos/bloco-2-qualidade-e-tipos-de-requisito.md
      - "Bloco 3: cenários e significância arquitetural": modulo-1-fundamentos/bloco-3-cenarios-e-significancia-arquitetural.md
      - "Bloco 4: estilos arquiteturais": modulo-1-fundamentos/bloco-4-estilos-arquiteturais.md
      - Síntese: modulo-1-fundamentos/sintese.md
  - "Aula 2 — Plataforma e modelos":
      - Visão geral: modulo-2-plataforma-e-modelos/index.md
  - "Aula 3 — Descoberta e riscos":
      - Visão geral: modulo-3-descoberta-e-riscos/index.md
  - "Aula 4 — Dados e segurança":
      - Visão geral: modulo-4-dados-e-seguranca/index.md
  - "Aula 5 — Blueprint e TRM":
      - Visão geral: modulo-5-blueprint-e-trm/index.md
  - "Aula 6 — Evolução e governança":
      - Visão geral: modulo-6-evolucao-e-governanca/index.md
  - Caso ACME:
      - Visão e contexto: caso-acme/index.md
      - Arquitetura de linha de base: caso-acme/linha-de-base.md
      - Dados operacionais: caso-acme/dados-operacionais.md
      - Artefatos por aula: caso-acme/artefatos.md
  - Referência:
      - Glossário: referencia/glossario.md
      - Bibliografia: referencia/bibliografia.md
```

- [ ] **Step 6: Criar `docs/index.md` provisório, substituído na Task 3**

```markdown
# Estratégias e Projeto de Arquitetura de Software

Material da disciplina do IEC/PUC Minas para as turmas Arq. Software Distribuído 10.1 e Arq. Soluções Digitais 1.1.
```

- [ ] **Step 7: Verificar que a compilação falha por páginas ausentes**

Run: `.venv/bin/mkdocs build --strict`
Expected: FAIL, com aviso de que os arquivos listados no `nav` não existem

- [ ] **Step 8: Criar os arquivos restantes do `nav` com uma linha de título cada**

```bash
cd ~/code/projeto-arquitetura-software
mkdir -p docs/modulo-1-fundamentos docs/modulo-2-plataforma-e-modelos \
  docs/modulo-3-descoberta-e-riscos docs/modulo-4-dados-e-seguranca \
  docs/modulo-5-blueprint-e-trm docs/modulo-6-evolucao-e-governanca \
  docs/caso-acme docs/referencia

printf '# Cronograma\n' > docs/cronograma.md
printf '# Aula 1, fundamentos\n' > docs/modulo-1-fundamentos/index.md
for b in bloco-1-arquitetura-e-papel-do-arquiteto bloco-2-qualidade-e-tipos-de-requisito \
         bloco-3-cenarios-e-significancia-arquitetural bloco-4-estilos-arquiteturais sintese; do
  printf '# %s\n' "$b" > "docs/modulo-1-fundamentos/$b.md"
done
printf '# Aula 2, plataforma e modelos\n' > docs/modulo-2-plataforma-e-modelos/index.md
printf '# Aula 3, descoberta e riscos\n' > docs/modulo-3-descoberta-e-riscos/index.md
printf '# Aula 4, dados e segurança\n' > docs/modulo-4-dados-e-seguranca/index.md
printf '# Aula 5, blueprint e TRM\n' > docs/modulo-5-blueprint-e-trm/index.md
printf '# Aula 6, evolução e governança\n' > docs/modulo-6-evolucao-e-governanca/index.md
printf '# Caso ACME\n' > docs/caso-acme/index.md
printf '# Arquitetura de linha de base\n' > docs/caso-acme/linha-de-base.md
printf '# Dados operacionais\n' > docs/caso-acme/dados-operacionais.md
printf '# Artefatos por aula\n' > docs/caso-acme/artefatos.md
printf '# Glossário\n' > docs/referencia/glossario.md
printf '# Bibliografia\n' > docs/referencia/bibliografia.md
```

- [ ] **Step 9: Verificar que a compilação passa**

Run: `.venv/bin/mkdocs build --strict`
Expected: PASS, sem avisos

- [ ] **Step 10: Commit**

```bash
git add requirements.txt mkdocs.yml .gitignore docs/
git commit -m "feat(site): esqueleto MkDocs com navegacao das seis aulas"
```

---

### Task 2: Validador de conteúdo e testes do contrato editorial

**Files:**
- Create: `scripts/validate_content.py`
- Create: `tests/course_assertions.py`
- Create: `tests/test_content_contract.py`

**Interfaces:**
- Consumes: estrutura de diretórios da Task 1
- Produces: `python3 scripts/validate_content.py` retornando 0 quando o conteúdo cumpre as regras e 1 quando não, com mensagem no formato `caminho:linha regra`. As tarefas 3 a 9 rodam esse comando antes de cada commit.

Este validador existe porque as regras editoriais do professor já falharam em releitura manual mais de uma vez. A checagem é mecânica.

- [ ] **Step 1: Escrever o teste do contrato antes do validador**

```python
# tests/test_content_contract.py
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ContentContractTest(unittest.TestCase):
    def test_validator_exists_and_runs(self):
        result = subprocess.run(
            ["python3", "scripts/validate_content.py"],
            cwd=ROOT, text=True, capture_output=True,
        )
        self.assertIn(result.returncode, (0, 1), result.stderr)

    def test_validator_declares_the_six_modules(self):
        text = (ROOT / "scripts/validate_content.py").read_text(encoding="utf-8")
        for slug in (
            "modulo-1-fundamentos",
            "modulo-2-plataforma-e-modelos",
            "modulo-3-descoberta-e-riscos",
            "modulo-4-dados-e-seguranca",
            "modulo-5-blueprint-e-trm",
            "modulo-6-evolucao-e-governanca",
        ):
            self.assertIn(f'"{slug}"', text, slug)

    def test_validator_declares_the_named_block_sections(self):
        text = (ROOT / "scripts/validate_content.py").read_text(encoding="utf-8")
        # Seis das oito secoes da anatomia sao cabecalhos. As outras duas,
        # titulo e linha de enquadramento, nao sao verificaveis por nome.
        for section in ("Antes de começar", "Conceito", "Uso pelo arquiteto",
                        "Exercício", "Gabarito", "Fontes"):
            self.assertIn(section, text, section)

    def test_validator_rejects_forbidden_editorial_markers(self):
        text = (ROOT / "scripts/validate_content.py").read_text(encoding="utf-8")
        for marker in ("TODO", "TBD", "PLACEHOLDER", "PREENCHER"):
            self.assertIn(marker, text, marker)

    def test_validator_does_not_flag_portuguese_words_as_markers(self):
        """"todo" e "preencher" sao palavras correntes em portugues."""
        page = ROOT / "docs" / "_teste_portugues.md"
        page.write_text(
            "# Teste\n\nTodo o material precisa preencher o criterio.\n",
            encoding="utf-8",
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertNotIn("_teste_portugues", result.stdout)
        finally:
            page.unlink()

    def test_validator_catches_a_semicolon_in_prose(self):
        offender = ROOT / "docs" / "_teste_temporario.md"
        offender.write_text("# Teste\n\nUma frase; outra frase.\n", encoding="utf-8")
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertEqual(1, result.returncode)
            self.assertIn("ponto-e-virgula", result.stdout)
        finally:
            offender.unlink()

    def test_validator_ignores_semicolon_inside_code_fence(self):
        allowed = ROOT / "docs" / "_teste_codigo.md"
        allowed.write_text(
            "# Teste\n\n```javascript\nconst a = 1;\n```\n", encoding="utf-8"
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertNotIn("_teste_codigo", result.stdout)
        finally:
            allowed.unlink()


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Rodar o teste e verificar que falha**

Run: `python3 -m unittest discover -s tests -v`
Expected: FAIL, porque `scripts/validate_content.py` não existe

- [ ] **Step 3: Escrever o validador**

```python
# scripts/validate_content.py
"""Aplica mecanicamente as regras editoriais do curso sobre docs/.

Retorna 0 quando o conteudo cumpre as regras e 1 quando encontra violacao.
Cada violacao e impressa como caminho:linha regra.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

MODULES = (
    "modulo-1-fundamentos",
    "modulo-2-plataforma-e-modelos",
    "modulo-3-descoberta-e-riscos",
    "modulo-4-dados-e-seguranca",
    "modulo-5-blueprint-e-trm",
    "modulo-6-evolucao-e-governanca",
)

# Secoes do site que nao sao modulos de aula, mas que --module aceita filtrar
EXTRA_SECTIONS = ("caso-acme", "referencia")

BLOCK_SECTIONS = (
    "Antes de começar",
    "Conceito",
    "Uso pelo arquiteto",
    "Exercício",
    "Gabarito",
    "Fontes",
)

FORBIDDEN_MARKERS = ("TODO", "TBD", "PLACEHOLDER", "PREENCHER")

EM_DASH = "—"


def strip_code_fences(lines: list[str]) -> list[tuple[int, str]]:
    """Devolve (numero_da_linha, texto) apenas para linhas fora de blocos de codigo."""
    out: list[tuple[int, str]] = []
    inside = False
    for number, line in enumerate(lines, start=1):
        if line.lstrip().startswith("```"):
            inside = not inside
            continue
        if inside:
            continue
        out.append((number, line))
    return out


def check_semicolons(path: Path, prose: list[tuple[int, str]]) -> list[str]:
    return [
        f"{path.relative_to(ROOT)}:{number} ponto-e-virgula proibido em prosa"
        for number, line in prose
        if ";" in re.sub(r"`[^`]*`", "", line)
        and not re.search(r"&[a-z]+;|&#\d+;", line)
    ]


def check_em_dashes(path: Path, prose: list[tuple[int, str]]) -> list[str]:
    offenders = []
    for number, line in prose:
        if line.lstrip().startswith("|"):
            continue
        if line.count(EM_DASH) > 1:
            offenders.append(
                f"{path.relative_to(ROOT)}:{number} mais de um travessao no paragrafo"
            )
    return offenders


def check_markers(path: Path, prose: list[tuple[int, str]]) -> list[str]:
    """Casa apenas a forma em caixa alta, como palavra inteira.

    Comparar em maiusculas daria falso positivo em portugues corrente:
    "todo o material" viraria TODO, e "preencher o formulario" viraria
    PREENCHER. O marcador editorial e sempre escrito em caixa alta.
    """
    offenders = []
    for number, line in prose:
        for marker in FORBIDDEN_MARKERS:
            if re.search(rf"\b{marker}\b", line):
                offenders.append(
                    f"{path.relative_to(ROOT)}:{number} marcador editorial {marker}"
                )
    return offenders


def check_headings(path: Path, prose: list[tuple[int, str]]) -> list[str]:
    offenders = []
    for number, line in prose:
        if not line.startswith("#"):
            continue
        title = line.lstrip("#").strip()
        if re.match(r"^Por que\b", title, re.IGNORECASE):
            offenders.append(
                f"{path.relative_to(ROOT)}:{number} titulo abre com Por que"
            )
        if EM_DASH in title:
            offenders.append(
                f"{path.relative_to(ROOT)}:{number} titulo com subtitulo apos travessao"
            )
    return offenders


def check_block_anatomy(path: Path, text: str) -> list[str]:
    """Paginas de bloco precisam das seis secoes nomeadas, na ordem."""
    if not path.name.startswith("bloco-"):
        return []
    positions = []
    for section in BLOCK_SECTIONS:
        match = re.search(rf"^##\s+{re.escape(section)}", text, re.MULTILINE)
        if match is None:
            return [f"{path.relative_to(ROOT)}: falta a secao {section}"]
        positions.append(match.start())
    if positions != sorted(positions):
        return [f"{path.relative_to(ROOT)}: secoes fora da ordem definida"]
    return []


def check_relative_links(path: Path, text: str) -> list[str]:
    offenders = []
    for match in re.finditer(r"\]\((?!https?://|#|mailto:)([^)]+)\)", text):
        target = match.group(1).split("#")[0]
        if not target:
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            line = text[: match.start()].count("\n") + 1
            offenders.append(
                f"{path.relative_to(ROOT)}:{line} link relativo quebrado {target}"
            )
    return offenders


def check_module_structure() -> list[str]:
    offenders = []
    for slug in MODULES:
        folder = DOCS / slug
        if not folder.is_dir():
            offenders.append(f"docs/{slug}: diretorio do modulo ausente")
            continue
        if not (folder / "index.md").exists():
            offenders.append(f"docs/{slug}/index.md ausente")
    return offenders


def validate(module: str | None = None) -> list[str]:
    offenders = check_module_structure()
    for path in sorted(DOCS.rglob("*.md")):
        if "superpowers" in path.parts:
            continue
        if module and module not in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        prose = strip_code_fences(text.splitlines())
        offenders += check_semicolons(path, prose)
        offenders += check_em_dashes(path, prose)
        offenders += check_markers(path, prose)
        offenders += check_headings(path, prose)
        offenders += check_block_anatomy(path, text)
        offenders += check_relative_links(path, text)
    return offenders


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida o conteudo do curso")
    parser.add_argument("--module", choices=MODULES + EXTRA_SECTIONS, default=None)
    args = parser.parse_args()
    offenders = validate(args.module)
    for line in offenders:
        print(line)
    print(f"\nResumo: {len(offenders)} violacao(oes).")
    return 1 if offenders else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Criar `tests/course_assertions.py` com as constantes compartilhadas**

```python
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

MODULES = (
    "modulo-1-fundamentos",
    "modulo-2-plataforma-e-modelos",
    "modulo-3-descoberta-e-riscos",
    "modulo-4-dados-e-seguranca",
    "modulo-5-blueprint-e-trm",
    "modulo-6-evolucao-e-governanca",
)

BLOCK_PAGES = (
    "bloco-1-arquitetura-e-papel-do-arquiteto",
    "bloco-2-qualidade-e-tipos-de-requisito",
    "bloco-3-cenarios-e-significancia-arquitetural",
    "bloco-4-estilos-arquiteturais",
)
```

- [ ] **Step 5: Rodar os testes e verificar que passam**

Run: `python3 -m unittest discover -s tests -v`
Expected: PASS em todos os casos

- [ ] **Step 6: Rodar o validador contra o esqueleto**

Run: `python3 scripts/validate_content.py`
Expected: relatório de violações apenas para as páginas de bloco que ainda não têm as seis seções, já que elas são esqueleto. Anotar a saída, que deve zerar ao fim da Task 9.

- [ ] **Step 7: Commit**

```bash
git add scripts/validate_content.py tests/
git commit -m "feat(validacao): validador de contrato editorial e testes"
```

---

### Task 3: Páginas de navegação e referência

**Files:**
- Modify: `docs/index.md`
- Modify: `docs/cronograma.md`
- Modify: `docs/referencia/glossario.md`
- Modify: `docs/referencia/bibliografia.md`
- Modify: `docs/modulo-2-plataforma-e-modelos/index.md` até `docs/modulo-6-evolucao-e-governanca/index.md`

**Interfaces:**
- Consumes: estrutura da Task 1, validador da Task 2
- Produces: `docs/referencia/glossario.md` com âncoras de termo no formato `#nome-do-termo`, usadas pelos links da seção "Antes de começar" das tarefas 6 a 9

- [ ] **Step 1: Escrever `docs/index.md`**

Conteúdo obrigatório: identificação da disciplina e das duas turmas, o que o site contém, como o material se organiza em seis aulas de quatro blocos, e a orientação de que o caso ACME é consultado na trilha própria. O método de avaliação fica registrado como pendência do professor na seção 11 do spec e não é inventado aqui. Se o professor não tiver informado até a execução, a página declara que a avaliação será divulgada em aula, sem descrever critério algum.

- [ ] **Step 2: Escrever `docs/cronograma.md`**

Tabela com as seis aulas, datas 21/09, 23/09, 28/09, 30/09, 05/10 e 15/10 de 2026, tema de cada uma e os quatro blocos da Aula 1 nomeados. As aulas 2 a 6 aparecem com o tema, sem partição em blocos, porque ela ainda não foi definida.

- [ ] **Step 3: Escrever `docs/referencia/glossario.md` com as entradas usadas no Módulo 1**

Entradas mínimas, cada uma com definição do curso em uma frase: arquitetura de software, arquiteto de software, atributo de qualidade, requisito funcional, requisito não funcional, requisito de atributo de qualidade, restrição, requisito arquiteturalmente significativo, direcionador arquitetural, cenário de atributo de qualidade, estilo arquitetural, plataforma arquitetural, ADR.

A entrada de requisito não funcional registra explicitamente que o curso não a trata como sinônimo de atributo de qualidade, porque os arquivos antigos do repositório afirmavam isso.

- [ ] **Step 4: Escrever `docs/referencia/bibliografia.md`**

Registrar apenas o que foi verificado. As três referências listadas na seção 7.3 do spec entram somente depois de conferidas. Se a conferência não tiver ocorrido, a página lista as fontes confirmadas e informa que a bibliografia está em construção, sem usar nenhum dos marcadores proibidos pelo validador.

- [ ] **Step 5: Escrever os cinco índices de módulo em esqueleto**

Cada um com título funcional, uma frase dizendo o tema da aula, a data no formato DD/MM/AAAA e a informação de que a partição em blocos será publicada antes da aula.

- [ ] **Step 6: Rodar validador e compilação**

Run: `python3 scripts/validate_content.py && .venv/bin/mkdocs build --strict`
Expected: nenhuma violação nas páginas desta tarefa, compilação sem avisos

- [ ] **Step 7: Commit**

```bash
git add docs/index.md docs/cronograma.md docs/referencia/ docs/modulo-*/index.md
git commit -m "docs(navegacao): inicio, cronograma, glossario e indices de modulo"
```

---

### Task 4: Dossiê do caso ACME

**Files:**
- Modify: `docs/caso-acme/index.md`
- Modify: `docs/caso-acme/linha-de-base.md`
- Modify: `docs/caso-acme/dados-operacionais.md`
- Modify: `docs/caso-acme/artefatos.md`

**Interfaces:**
- Consumes: validador da Task 2
- Produces: os dados que os exercícios das tarefas 6 a 9 citam em extrato. Os quatro exercícios do Módulo 1 dependem desta tarefa: o bloco 1 usa atores e restrições, o bloco 2 usa a lista de requisitos, o bloco 3 usa volumes e incidentes, o bloco 4 usa os cenários derivados.

A versão usada na disciplina irmã tem 5.260 caracteres e números redondos. O professor pediu um caso mais profundo e realista. Esta tarefa produz isso.

- [ ] **Step 1: Escrever `docs/caso-acme/index.md`**

A instituição, seu porte, a pergunta central que organiza o caso e o mapa de atores com nome de papel, área e o que cada um quer. Mínimo de seis papéis, incluindo ao menos um com interesse conflitante com outro, porque o bloco 1 pede identificação de quem decide.

- [ ] **Step 2: Escrever `docs/caso-acme/linha-de-base.md`**

A arquitetura atual em detalhe: núcleo COBOL sobre CICS com banco Oracle, camada web em JSF e EJB 2.0, integrações por troca de arquivos com o ERP financeiro e com o ambiente virtual de aprendizagem. Acrescentar o que falta na versão atual: quantidade de módulos, linhas de código estimadas, idade de cada componente, quantas pessoas sustentam cada parte, quais integrações são síncronas e quais são em lote, e a janela em que cada lote roda.

Incluir um diagrama Mermaid da linha de base, com os componentes e o tipo de cada integração.

- [ ] **Step 3: Escrever `docs/caso-acme/dados-operacionais.md`**

Volumes por período, calendário acadêmico com as janelas críticas de matrícula e fechamento de notas, sazonalidade com a razão entre pico e média, histórico de três incidentes com data, duração, causa e impacto, custo atual de infraestrutura, e os contratos vigentes com prazo e cláusula relevante.

Os números precisam ser internamente consistentes: o pico de matrícula declarado aqui é o mesmo citado nos exercícios dos blocos 2 e 3.

- [ ] **Step 4: Escrever `docs/caso-acme/artefatos.md`**

Tabela do que cada aula acrescenta ao caso. Para a Aula 1, os quatro artefatos são o mapa de atores e restrições, a classificação de requisitos, os cenários de qualidade com o julgamento de significância, e a comparação de estilos. Para as aulas 2 a 6, apenas o previsto, marcado como sujeito à definição da ementa.

- [ ] **Step 5: Verificar a consistência numérica entre as páginas**

Run: `grep -rn "matrícula\|pico\|simultâne" docs/caso-acme/`
Expected: os números de pico aparecem com o mesmo valor em todas as ocorrências

- [ ] **Step 6: Rodar validador e compilação**

Run: `python3 scripts/validate_content.py --module caso-acme && .venv/bin/mkdocs build --strict`
Expected: zero violações, compilação sem avisos

- [ ] **Step 7: Commit**

```bash
git add docs/caso-acme/
git commit -m "docs(caso): dossie ACME com linha de base e dados operacionais"
```

---

### Task 5: Índice e síntese do Módulo 1

**Files:**
- Modify: `docs/modulo-1-fundamentos/index.md`
- Modify: `docs/modulo-1-fundamentos/sintese.md`

**Interfaces:**
- Consumes: Task 3 para os links de glossário, Task 4 para a referência ao caso
- Produces: a grade de tempo que é o único lugar do site onde os minutos aparecem, conforme decisão registrada na seção 3 do spec

- [ ] **Step 1: Escrever `docs/modulo-1-fundamentos/index.md`**

Título funcional. Uma linha com a questão que a aula responde. Objetivos de aprendizagem em verbos observáveis. A grade de tempo em tabela, com os quatro blocos, o conceito de cada um e a marcação de 25 e 15 minutos. Um roteiro ligando cada bloco à página correspondente. Uma seção curta dizendo como esta aula prepara a Aula 2.

- [ ] **Step 2: Escrever `docs/modulo-1-fundamentos/sintese.md`**

Checklist do que precisa permanecer, autoavaliação com perguntas que o aluno responde a si mesmo, e as fontes da aula inteira.

- [ ] **Step 3: Rodar validador e compilação**

Run: `python3 scripts/validate_content.py --module modulo-1-fundamentos && .venv/bin/mkdocs build --strict`
Expected: violações apenas nas quatro páginas de bloco, que ainda são esqueleto

- [ ] **Step 4: Commit**

```bash
git add docs/modulo-1-fundamentos/index.md docs/modulo-1-fundamentos/sintese.md
git commit -m "docs(modulo-1): indice com grade de tempo e sintese"
```

---

### Task 6: Bloco 1, arquitetura e papel do arquiteto

**Files:**
- Modify: `docs/modulo-1-fundamentos/bloco-1-arquitetura-e-papel-do-arquiteto.md`
- Source: `1.0 O que é arquitetura e quem e o arquiteto.md` na raiz do repositório

**Interfaces:**
- Consumes: glossário da Task 3, dossiê da Task 4
- Produces: o artefato de mapa de atores e restrições, consumido pelo exercício do bloco 2

- [ ] **Step 1: Ler a fonte e listar o que aproveitar**

Run: `cat "1.0 O que é arquitetura e quem e o arquiteto.md"`
O texto é reescrito, não copiado. Manter a sequência de ideias que funcionar e descartar o resto.

- [ ] **Step 2: Escrever a página com as oito seções**

Título funcional. Linha de enquadramento. Seção "Antes de começar" com os termos ligados ao glossário. Seção "Conceito" com a definição de arquitetura de software, o que o arquiteto decide e o que não decide, e o enquadramento do problema. Seção "Uso pelo arquiteto". Seção "Exercício". Seção "Gabarito". Seção "Fontes".

Exemplos de ao menos dois domínios distintos, e nenhum deles pode ser o domínio principal do bloco 2. O caso ACME aparece apenas no exercício, com frase de reintrodução.

- [ ] **Step 3: Escrever o exercício com enunciado autocontido**

O enunciado traz embutido o extrato do dossiê necessário: a lista de papéis e as restrições que chegam fechadas. O aluno identifica o que a instituição quer, quem decide cada tipo de questão, e qual restrição elimina alternativas. Gabarito em bloco `<details>`.

- [ ] **Step 4: Verificar a autocontenção**

Ler o parágrafo de abertura inteiro. Se alguém abrisse só esta página, teria contexto suficiente? A primeira menção a ACME traz reintrodução em uma frase?

- [ ] **Step 5: Rodar validador e compilação**

Run: `python3 scripts/validate_content.py --module modulo-1-fundamentos && .venv/bin/mkdocs build --strict`
Expected: nenhuma violação nesta página

- [ ] **Step 6: Commit**

```bash
git add docs/modulo-1-fundamentos/bloco-1-arquitetura-e-papel-do-arquiteto.md
git commit -m "docs(modulo-1): bloco 1 sobre arquitetura e papel do arquiteto"
```

---

### Task 7: Bloco 2, qualidade e tipos de requisito

**Files:**
- Modify: `docs/modulo-1-fundamentos/bloco-2-qualidade-e-tipos-de-requisito.md`
- Source: texto de referência do professor, seções 1 e 2
- Source: `1.1 Requisitos Arquiteturais.md` e `1.2 Requisitos Não-Funcionais.md` na raiz

**Interfaces:**
- Consumes: mapa de atores do bloco 1
- Produces: a classificação de requisitos da ACME, consumida pelo exercício do bloco 3

Este bloco incorpora as seções 1 e 2 do texto de referência fornecido pelo professor em 19/09/2026. O conteúdo é dele. A adaptação se limita a pontuação, formatação de tabelas e conversão das listas que usam ponto-e-vírgula.

- [ ] **Step 1: Transcrever as seções 1 e 2 do texto de referência**

Cobrir, na ordem do original: o que significa qualidade em software, atributo de qualidade com a lista de oito exemplos, do atributo ao requisito, onde se posiciona o requisito não funcional, a tabela de classificação inicial, e a tabela que posiciona os quatro conceitos.

- [ ] **Step 2: Converter as listas com ponto-e-vírgula**

As listas das seções 1.1 e 2.1 do original usam ponto-e-vírgula ao final de cada item. Converter para itens sem pontuação final, conforme a regra do curso.

- [ ] **Step 3: Remontar as duas tabelas**

A tabela de classificação inicial, com três requisitos de exemplo, e a tabela conceito contra papel, com requisito funcional, requisito não funcional, requisito de atributo de qualidade e restrição. Ambas chegaram achatadas no texto-fonte.

- [ ] **Step 4: Escrever o exercício**

O enunciado traz uma lista de oito requisitos da ACME, extraídos do dossiê e reproduzidos no próprio enunciado. O aluno classifica cada um nas quatro categorias e reescreve dois deles em forma mensurável, com contexto, carga e medida. Gabarito em bloco `<details>`, justificando cada classificação.

- [ ] **Step 5: Verificar a cobertura de domínios**

O texto de referência usa aplicativo bancário, plataforma de vídeo, portal institucional e sistema hospitalar. Confirmar que ao menos dois aparecem e que nenhum deles será o domínio principal do bloco 3.

- [ ] **Step 6: Rodar validador e compilação**

Run: `python3 scripts/validate_content.py --module modulo-1-fundamentos && .venv/bin/mkdocs build --strict`
Expected: nenhuma violação nesta página

- [ ] **Step 7: Commit**

```bash
git add docs/modulo-1-fundamentos/bloco-2-qualidade-e-tipos-de-requisito.md
git commit -m "docs(modulo-1): bloco 2 sobre qualidade e tipos de requisito"
```

---

### Task 8: Bloco 3, cenários e significância arquitetural

**Files:**
- Modify: `docs/modulo-1-fundamentos/bloco-3-cenarios-e-significancia-arquitetural.md`
- Source: texto de referência do professor, seções 2.3, 3, 7, 8 e 9

**Interfaces:**
- Consumes: a classificação de requisitos produzida no bloco 2
- Produces: os cenários de qualidade da ACME, consumidos pelo exercício do bloco 4

- [ ] **Step 1: Transcrever as seções 2.3, 3, 7 e 8 do texto de referência**

Cobrir: cenários de atributos de qualidade e os seis elementos, quando um requisito passa a ser questão de arquitetura, requisito arquiteturalmente significativo com a lista de oito condições, direcionador arquitetural, a relação entre atributo de qualidade e ASR, as duas tabelas de cenário do original, e o roteiro de sete perguntas para decidir significância.

- [ ] **Step 2: Converter a notação quebrada da seção 5 do original**

As duas fórmulas em LaTeX chegaram quebradas. Substituir por prosa que diga o mesmo: existem requisitos de atributo de qualidade que são ASR e outros que não são, existem ASR funcionais e ASR que são restrições, e portanto os dois conjuntos se cruzam sem coincidir.

- [ ] **Step 3: Remontar as duas tabelas de cenário**

A tabela de elementos com a pergunta que cada um responde, e as duas tabelas de exemplo, uma de desempenho e outra de modificabilidade.

- [ ] **Step 4: Incluir os erros conceituais da seção 9**

Os cinco erros, nomeados, sem ironia: tratar todo requisito não funcional como ASR, tratar todo ASR como requisito não funcional, confundir nome do atributo com requisito, atribuir à ISO 42010 taxonomia que ela não prescreve, e escrever requisitos sem contexto e medida.

- [ ] **Step 5: Escrever o exercício**

O enunciado traz o extrato de volumes e incidentes do dossiê. O aluno escreve dois cenários no formato de seis elementos para a ACME e defende quais constituem ASR, aplicando o roteiro de sete perguntas. Como a resposta é aberta, o bloco de gabarito traz critério de avaliação, não resposta única.

- [ ] **Step 6: Rodar validador e compilação**

Run: `python3 scripts/validate_content.py --module modulo-1-fundamentos && .venv/bin/mkdocs build --strict`
Expected: nenhuma violação nesta página

- [ ] **Step 7: Commit**

```bash
git add docs/modulo-1-fundamentos/bloco-3-cenarios-e-significancia-arquitetural.md
git commit -m "docs(modulo-1): bloco 3 sobre cenarios e significancia arquitetural"
```

---

### Task 9: Bloco 4, estilos arquiteturais

**Files:**
- Modify: `docs/modulo-1-fundamentos/bloco-4-estilos-arquiteturais.md`
- Source: `1.3 Estilos Arquiteturais.md` na raiz do repositório

**Interfaces:**
- Consumes: os cenários produzidos no bloco 3
- Produces: a comparação de estilos, que a Aula 2 retoma ao tratar de plataforma arquitetural

O arquivo-fonte tem 17.515 caracteres e duas figuras hospedadas em `user-attachments` do GitHub. As figuras não podem ser referenciadas por aquela URL.

- [ ] **Step 1: Ler a fonte e inventariar as figuras**

Run: `grep -n "img\|user-attachments" "1.3 Estilos Arquiteturais.md"`
Cada figura vira diagrama Mermaid ou arquivo local em `docs/assets/images`.

- [ ] **Step 2: Escrever a seção de conceito**

Definição de estilo arquitetural, a relação entre estilo e atributo de qualidade, e os estilos que a disciplina compara. Para cada estilo, quais atributos ele favorece e quais ele prejudica, porque o exercício depende dessa relação.

- [ ] **Step 3: Substituir as figuras externas por Mermaid**

Cada estilo apresentado ganha um diagrama Mermaid mostrando sua estrutura. Se algum exigir expressão que Mermaid não oferece, registrar o arquivo esperado em `docs/assets/images` com legenda e texto alternativo escritos, para o professor produzir.

- [ ] **Step 4: Escrever o exercício**

O enunciado reproduz dois cenários de qualidade da ACME já formulados, para o aluno não depender do que produziu no bloco anterior. O aluno compara três estilos contra esses cenários e defende uma escolha. Critério de avaliação no bloco colapsável.

- [ ] **Step 5: Verificar que nenhuma URL de user-attachments sobreviveu**

Run: `grep -rn "user-attachments" docs/`
Expected: nenhum resultado

- [ ] **Step 6: Rodar validador e compilação**

Run: `python3 scripts/validate_content.py && .venv/bin/mkdocs build --strict`
Expected: zero violações em todo o site, compilação sem avisos

- [ ] **Step 7: Commit**

```bash
git add docs/modulo-1-fundamentos/bloco-4-estilos-arquiteturais.md docs/assets/
git commit -m "docs(modulo-1): bloco 4 sobre estilos arquiteturais"
```

---

### Task 10: Verificação final do Módulo 1

**Files:**
- Modify: nenhum, salvo correções encontradas

**Interfaces:**
- Consumes: tudo das tarefas 1 a 9
- Produces: relatório de conformidade

- [ ] **Step 1: Rodar a suíte completa**

Run: `python3 -m unittest discover -s tests -v && python3 scripts/validate_content.py && .venv/bin/mkdocs build --strict`
Expected: testes passando, zero violações, compilação sem avisos

- [ ] **Step 2: Conferir a contagem de travessões por página**

Run: `for f in docs/modulo-1-fundamentos/*.md; do echo "$f: $(grep -o '—' "$f" | wc -l)"; done`
Verificar manualmente qualquer página com contagem alta, porque o validador só pega mais de um travessão na mesma linha.

- [ ] **Step 3: Conferir a diversidade de domínios entre blocos consecutivos**

Listar o domínio principal de cada bloco e confirmar que blocos vizinhos não repetem o mesmo.

- [ ] **Step 4: Ler o parágrafo de abertura de cada uma das quatro páginas de bloco**

Regra de autocontenção. Cada abertura precisa fazer sentido para quem abriu só aquela página.

- [ ] **Step 5: Verificar que o tempo declarado aparece apenas no índice do módulo**

Run: `grep -rn "minuto" docs/modulo-1-fundamentos/`
Expected: ocorrências apenas em `index.md`

- [ ] **Step 6: Servir o site e conferir a renderização dos diagramas**

Run: `.venv/bin/mkdocs serve`
Abrir cada página do Módulo 1 e confirmar que os diagramas Mermaid renderizam e que os blocos de gabarito abrem e fecham.

- [ ] **Step 7: Commit final**

```bash
git add -A
git commit -m "chore(modulo-1): verificacao final do esqueleto e da primeira aula"
```

---

## Pendências herdadas do spec

Estas não são tarefas deste plano. Ficam registradas para a rodada seguinte.

1. Partição da Aula 2 em quatro blocos, com cinco temas a acomodar
2. Ementa e partição das Aulas 3 a 6
3. Verificação das três referências da seção 7.3 do spec, que só entram na bibliografia depois de conferidas
4. Método de avaliação da disciplina, necessário para fechar `docs/index.md`
5. Os quatro arquivos praticamente vazios do repositório, os três de modelagem de microsserviços com 119 bytes e o de exemplo C1 a C3 com 369 bytes, citados na seção 8 do spec. Eles pertencem à Aula 2 e não entram nesta rodada.
