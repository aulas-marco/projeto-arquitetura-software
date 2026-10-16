"""Gera o inventário de auditoria do conteúdo do curso para a matriz do caderno.

Uso: python3 scripts/inventario_auditoria.py [--escrever]
Sem --escrever, imprime a tabela. Com --escrever, grava a matriz em
docs/superpowers/auditoria/ e se recusa a sobrescrever matriz já preenchida.
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MATRIZ = DOCS / "superpowers" / "auditoria" / "2026-10-16-matriz-caderno.md"
IGNORADAS = ("superpowers", "caderno", "gabaritos")


def _slug(titulo: str) -> str:
    spec = importlib.util.spec_from_file_location(
        "validate_content", ROOT / "scripts" / "validate_content.py"
    )
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo._slugify_heading(titulo)


def _primeiro_titulo(texto: str) -> str:
    achado = re.search(r"^# (.+)$", texto, re.MULTILINE)
    return achado.group(1) if achado else ""


def _secao(texto: str, titulo_regex: str) -> str:
    achado = re.search(rf"^## {titulo_regex}.*$", texto, re.MULTILINE)
    if achado is None:
        return ""
    resto = texto[achado.end():]
    proximo = re.search(r"^## ", resto, re.MULTILINE)
    return resto[: proximo.start()] if proximo else resto


def inventariar(docs: Path = DOCS) -> list[tuple[str, str, str]]:
    linhas: list[tuple[str, str, str]] = []
    for caminho in sorted(docs.rglob("*.md")):
        relativo = caminho.relative_to(docs)
        if relativo.parts[0] in IGNORADAS:
            continue
        texto = caminho.read_text(encoding="utf-8")
        linhas.append(("página", str(relativo), _primeiro_titulo(texto)))
        if caminho.name == "glossario.md":
            for achado in re.finditer(r"^## (.+)$", texto, re.MULTILINE):
                linhas.append(("termo", f"{relativo}#{_slug(achado.group(1))}", achado.group(1)))
        if caminho.name == "sintese.md":
            bloco = _secao(texto, "Checklist")
            for item in re.finditer(r"^- (.+)$", bloco, re.MULTILINE):
                resumo = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", item.group(1))
                linhas.append(("síntese", f"{relativo}#checklist", resumo[:90]))
        exercicio = re.search(r"^## (Exercício \d+)\s*$", texto, re.MULTILINE)
        if exercicio:
            ancora = _slug(exercicio.group(1))
            linhas.append(("exercício", f"{relativo}#{ancora}", exercicio.group(1)))
            for item in re.finditer(r"^### (Item \d+: .+)$", _secao(texto, "Exercício \\d+"), re.MULTILINE):
                linhas.append(("item", f"{relativo}#{ancora}", item.group(1)))
    return linhas


def renderizar(linhas: list[tuple[str, str, str]]) -> str:
    cabecalho = [
        "| Tipo | Local | Rótulo | Seção do caderno | Decisão | Justificativa |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    corpo = [f"| {tipo} | {local} | {rotulo.replace('|', '/')} |  |  |  |" for tipo, local, rotulo in linhas]
    return "\n".join(cabecalho + corpo) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Inventário de auditoria do caderno")
    parser.add_argument("--escrever", action="store_true")
    args = parser.parse_args()
    tabela = renderizar(inventariar())
    if not args.escrever:
        print(tabela)
        return 0
    if MATRIZ.exists():
        print(f"{MATRIZ.relative_to(ROOT)} já existe e não será sobrescrita", file=sys.stderr)
        return 1
    MATRIZ.parent.mkdir(parents=True, exist_ok=True)
    cabecalho = (
        "# Matriz de auditoria do conteúdo à luz do caderno arquitetural\n\n"
        "**Data:** 16/10/2026\n\n**Estado:** inventário gerado, decisões pendentes\n\n"
        "Decisões possíveis: mantém, altera, move, remove. Seção do caderno é o número da "
        "seção em `caderno-fonte/`, ou `apoio` para conceito sem seção própria que sustenta "
        "conceito que a tem.\n\n"
    )
    MATRIZ.write_text(cabecalho + tabela, encoding="utf-8")
    print(f"gravado {MATRIZ.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
