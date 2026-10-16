"""Gera o template, o mapa e os gabaritos cumulativos do caderno arquitetural.

A fonte fica em caderno-fonte/. Uso:
    python3 scripts/gerar_caderno.py          grava as páginas em docs/
    python3 scripts/gerar_caderno.py --check  falha se alguma página diverge da fonte
"""

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from caderno_registro import EXERCICIOS, PLANO, SUBSTITUI, TITULOS_SECAO  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
FONTE = ROOT / "caderno-fonte"

FRONT = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
ORIENTACAO = re.compile(r"<!--orientacao-->[ \t]*\n(.*?)<!--/orientacao-->", re.DOTALL)
FRAGMENTO = re.compile(
    r'<!--ex[ \t]+n=(\d+)[ \t]+titulo="([^"]+)"[ \t]*-->[ \t]*\n(.*?)<!--/ex-->', re.DOTALL
)
CAMPOS = re.compile(r"<!--campos-->[ \t]*\n(.*?)<!--/campos-->", re.DOTALL)
GABARITO = re.compile(r"<!--gabarito-->[ \t]*\n(.*?)<!--/gabarito-->", re.DOTALL)
CERCA = re.compile(r"^\s*(```|~~~)")

INTRO_TEMPLATE = (
    "O caderno arquitetural é o documento de arquitetura da solução da ACME. Ele reúne, em dez "
    "seções, as decisões que o curso ensina a tomar, cada uma ligada ao requisito que a motivou. "
    "A tabela de cada seção indica o que vai nela, a pergunta que responde, os artefatos que a "
    "compõem, a entrada de que depende e o exercício que a preenche. As "
    "[convenções](convencoes.md) definem os códigos dos artefatos, e o [mapa](mapa.md) relaciona "
    "seção, bloco e exercício."
)


@dataclass(frozen=True)
class Fragmento:
    n: int
    titulo: str
    campos: str
    gabarito: str


@dataclass(frozen=True)
class Secao:
    numero: int
    titulo: str
    modo: str
    orientacao: str
    fragmentos: tuple[Fragmento, ...]


def _extrair(padrao: re.Pattern, texto: str) -> str:
    achado = padrao.search(texto)
    return achado.group(1) if achado else ""


def carregar(fonte: Path = FONTE) -> list[Secao]:
    secoes: list[Secao] = []
    for caminho in sorted(fonte.glob("[0-9][0-9]-*.md")):
        texto = caminho.read_text(encoding="utf-8")
        front = FRONT.match(texto)
        if front is None:
            raise ValueError(f"{caminho.name}: falta o cabeçalho de metadados")
        meta = dict(linha.split(": ", 1) for linha in front.group(1).splitlines())
        if "secao" not in meta or "titulo" not in meta:
            raise ValueError(f"{caminho.name}: o cabeçalho precisa de secao e titulo")
        corpo = texto[front.end():]
        if corpo.count("<!--ex") != corpo.count("<!--/ex-->"):
            raise ValueError(f"{caminho.name}: marcador ex sem fechamento")
        if corpo.count("<!--ex") != len(FRAGMENTO.findall(corpo)):
            raise ValueError(
                f"{caminho.name}: marcador ex mal formado, o formato é "
                '<!--ex n=NN titulo="Título"--> com aspas duplas'
            )
        orientacao = _extrair(ORIENTACAO, corpo).strip()
        if not orientacao:
            raise ValueError(f"{caminho.name}: falta a orientação da seção")
        fragmentos: list[Fragmento] = []
        vistos: set[int] = set()
        for achado in FRAGMENTO.finditer(corpo):
            n = int(achado.group(1))
            if n in vistos:
                raise ValueError(f"{caminho.name}: exercício {n} repetido na seção")
            vistos.add(n)
            for marcador in ("campos", "gabarito"):
                abre = achado.group(3).count(f"<!--{marcador}-->")
                fecha = achado.group(3).count(f"<!--/{marcador}-->")
                if abre != fecha:
                    raise ValueError(
                        f"{caminho.name}: marcador {marcador} sem fechamento no exercício {n}"
                    )
            gabarito = _extrair(GABARITO, achado.group(3)).strip()
            # O gabarito usa títulos de nível 4 ou maior. Linhas dentro de cerca de
            # código (``` ou ~~~) não contam, porque o # delas é comentário.
            dentro_da_cerca = False
            for linha in gabarito.splitlines():
                if CERCA.match(linha):
                    dentro_da_cerca = not dentro_da_cerca
                    continue
                if not dentro_da_cerca and re.match(r"#{1,3}\s", linha):
                    raise ValueError(
                        f"{caminho.name}: título de nível 1 a 3 no gabarito do exercício {n}"
                    )
            fragmentos.append(
                Fragmento(n, achado.group(2), _extrair(CAMPOS, achado.group(3)).strip(), gabarito)
            )
        secoes.append(
            Secao(int(meta["secao"]), meta["titulo"], meta.get("modo", "acumula"),
                  orientacao, tuple(fragmentos))
        )
    return sorted(secoes, key=lambda s: s.numero)


def _rotulo(numero: int) -> str:
    return TITULOS_SECAO[numero] if numero == 0 else f"{numero}. {TITULOS_SECAO[numero]}"


def _cabecalho(secao: Secao) -> str:
    return f"## {_rotulo(secao.numero)}"


def _visiveis(secao: Secao, n: int) -> list[Fragmento]:
    visiveis = [f for f in secao.fragmentos if f.gabarito and f.n <= n]
    if secao.modo == "substitui" and visiveis:
        ultimo = max(f.n for f in visiveis)
        visiveis = [f for f in visiveis if f.n == ultimo]
    return visiveis


def _pagina(n: int, docs: Path) -> str | None:
    arquivo = EXERCICIOS[n][1]
    return arquivo if (docs / arquivo).exists() else None


def render_template(secoes: list[Secao]) -> str:
    partes = ["# Template do caderno arquitetural", "", INTRO_TEMPLATE, "", "{{trilha:todas}}", ""]
    for secao in secoes:
        partes += [f"{{{{folha:{secao.numero}}}}}", "", _cabecalho(secao), "", secao.orientacao, ""]
        if secao.modo == "acumula":
            for i, fragmento in enumerate(secao.fragmentos, start=1):
                partes += [f"### {secao.numero}.{i} {fragmento.titulo}", "",
                           f"Preenchida no exercício {fragmento.n}.", ""]
                if fragmento.campos:
                    partes += ["Campos a preencher:", "", fragmento.campos, ""]
        partes += ["{{/folha}}", ""]
    return "\n".join(partes).rstrip() + "\n"


def render_gabarito(secoes: list[Secao], n: int, docs: Path = DOCS) -> str:
    partes = [f"# Gabarito do exercício {n}", "", f"{{{{progresso:{n}}}}}", ""]
    intro = (
        f"O caderno abaixo reúne o resultado dos exercícios 1 a {n}, e o trecho em destaque é o "
        f"que o exercício {n} preenche."
    )
    pagina = _pagina(n, docs)
    if pagina:
        intro += f" O [enunciado do exercício {n}](../{pagina}#exercicio-{n}) está na página do bloco."
    partes += [intro, ""]
    pendentes: list[str] = []
    for secao in secoes:
        visiveis = _visiveis(secao, n)
        if not visiveis:
            pendentes.append(_rotulo(secao.numero))
            continue
        partes += [_cabecalho(secao), ""]
        for i, fragmento in enumerate(secao.fragmentos, start=1):
            if fragmento not in visiveis:
                continue
            if secao.modo == "acumula":
                partes += [f"### {secao.numero}.{i} {fragmento.titulo}", ""]
            if fragmento.n == n:
                partes += ["{{novo}}", "", fragmento.gabarito, "", "{{/novo}}", ""]
            else:
                partes += [fragmento.gabarito, ""]
    if pendentes:
        partes += ["Seções que os exercícios seguintes preenchem: " + ", ".join(pendentes), ""]
    return "\n".join(partes).rstrip() + "\n"


def _com_gabarito(secoes: list[Secao]) -> set[int]:
    return {f.n for s in secoes for f in s.fragmentos if f.gabarito}


def render_mapa(secoes: list[Secao], existentes: set[int], docs: Path = DOCS) -> str:
    linhas = [
        "# Mapa do caderno arquitetural",
        "",
        "A tabela relaciona cada seção do caderno ao bloco que a ensina, ao exercício que a "
        "preenche e ao gabarito em que o resultado aparece. As seções 0 e 10 são revistas ao fim "
        "de cada aula, nos exercícios 4, 8, 12, 16, 20 e 24.",
        "",
        "| Seção | Aula | Bloco | Exercício | Gabarito |",
        "| --- | --- | --- | --- | --- |",
    ]
    pares = {(s, n) for n, ss in PLANO.items() for s in ss}
    pares |= {(s, n) for s, ns in SUBSTITUI.items() for n in ns}
    for secao, n in sorted(pares):
        aula, arquivo, titulo = EXERCICIOS[n]
        numero_bloco = re.search(r"bloco-(\d)", arquivo).group(1)
        existe = (docs / arquivo).exists()
        bloco = f"[Bloco {numero_bloco}, {titulo}](../{arquivo})" if existe else f"Bloco {numero_bloco}, {titulo}"
        exercicio = f"[Exercício {n}](../{arquivo}#exercicio-{n})" if existe else f"Exercício {n}"
        gabarito = (
            f"[Gabarito {n}](../gabaritos/gabarito-exercicio-{n:02d}.md)" if n in existentes else "A publicar"
        )
        linhas.append(f"| {_rotulo(secao)} | Aula {aula} | {bloco} | {exercicio} | {gabarito} |")
    return "\n".join(linhas) + "\n"


def render_indice(existentes: set[int]) -> str:
    partes = [
        "# Gabaritos",
        "",
        "Cada gabarito é o caderno arquitetural da ACME com o resultado dos exercícios até aquele "
        "ponto, e o trecho que o exercício preenche aparece em destaque. O "
        "[template](../caderno/template.md) mostra o caderno vazio, e o "
        "[mapa](../caderno/mapa.md) relaciona seção, bloco e exercício.",
        "",
    ]
    if not existentes:
        partes.append("Nenhum gabarito foi publicado até o momento.")
    else:
        partes += ["| Exercício | Gabarito |", "| --- | --- |"]
        for n in sorted(existentes):
            partes.append(f"| Exercício {n}, {EXERCICIOS[n][2]} | [Gabarito {n}](gabarito-exercicio-{n:02d}.md) |")
    return "\n".join(partes).rstrip() + "\n"


def saidas(secoes: list[Secao], docs: Path = DOCS) -> dict[Path, str]:
    existentes = _com_gabarito(secoes)
    resultado = {
        docs / "caderno" / "template.md": render_template(secoes),
        docs / "caderno" / "mapa.md": render_mapa(secoes, existentes, docs),
        docs / "gabaritos" / "index.md": render_indice(existentes),
    }
    for n in sorted(existentes):
        resultado[docs / "gabaritos" / f"gabarito-exercicio-{n:02d}.md"] = render_gabarito(secoes, n, docs)
    return resultado


def divergencias(saidas_: dict[Path, str], docs: Path = DOCS) -> list[str]:
    problemas = []
    for caminho, texto in saidas_.items():
        if not caminho.exists() or caminho.read_text(encoding="utf-8") != texto:
            problemas.append(f"{caminho.name} diverge da fonte")
    for caminho in sorted((docs / "gabaritos").glob("gabarito-exercicio-*.md")):
        if caminho not in saidas_:
            problemas.append(f"{caminho.name} sobra, sem trecho na fonte")
    return problemas


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera as páginas do caderno arquitetural")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    gerado = saidas(carregar())
    if args.check:
        problemas = divergencias(gerado)
        for problema in problemas:
            print(problema)
        print(f"\nResumo: {len(problemas)} divergência(s).")
        return 1 if problemas else 0
    for caminho, texto in gerado.items():
        caminho.parent.mkdir(parents=True, exist_ok=True)
        caminho.write_text(texto, encoding="utf-8")
    for caminho in (DOCS / "gabaritos").glob("gabarito-exercicio-*.md"):
        if caminho not in gerado:
            caminho.unlink()
    print(f"gravadas {len(gerado)} páginas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
