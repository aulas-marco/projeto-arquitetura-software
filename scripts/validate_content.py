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
