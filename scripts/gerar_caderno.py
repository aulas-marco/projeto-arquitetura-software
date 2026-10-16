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
    "Ao longo do curso, a arquitetura da solução da ACME vai sendo registrada num único documento, "
    "seção por seção, e esse documento é o caderno arquitetural. Cada seção responde a uma pergunta e é "
    "preenchida por um ou mais exercícios, e por isso a trilha abaixo mostra as onze partes, com uma "
    "ficha que diz o que entra em cada seção, de onde vêm as informações e quando ela é preenchida. "
    "Quem encontrar um código como D1 ou R6 sem saber o que significa pode consultar a página de "
    "[convenções](convencoes.md), e o [mapa](mapa.md) mostra qual exercício preenche cada seção."
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
                           f"Esta parte é preenchida no exercício {fragmento.n}.", ""]
                if fragmento.campos:
                    partes += ["Você escreve:", "", fragmento.campos, ""]
        partes += ["{{/folha}}", ""]
    return "\n".join(partes).rstrip() + "\n"


def render_gabarito(secoes: list[Secao], n: int, docs: Path = DOCS) -> str:
    partes = [f"# Gabarito do exercício {n}", "", f"{{{{progresso:{n}}}}}", ""]
    if n == 1:
        intro = (
            "Ao terminar o exercício 1, o caderno da ACME ganhou as suas primeiras respostas, e a moldura âmbar "
            "marca o que foi acrescentado. Compare com o seu caderno para ver onde as suas respostas diferem."
        )
    else:
        intro = (
            f"Depois do exercício {n}, o caderno da ACME reúne o que os exercícios 1 a {n} produziram, "
            f"e a moldura âmbar marca o que o exercício {n} acrescentou. Compare com o seu caderno para ver "
            "onde as suas respostas diferem."
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
        novos = any(f.n == n for f in visiveis)
        partes += [_cabecalho(secao), ""]
        aviso = (
            "Atualizada neste exercício"
            if novos
            else f"Construída {_onde(sorted({f.n for f in visiveis}))}. Clique para abrir"
        )
        partes += [f'<details class="caderno-secao" markdown="1"{" open" if novos else ""}>',
                   f"<summary>{aviso}</summary>", ""]
        for i, fragmento in enumerate(secao.fragmentos, start=1):
            if fragmento not in visiveis:
                continue
            if secao.modo == "acumula":
                partes += [f"### {secao.numero}.{i} {fragmento.titulo}", ""]
            if fragmento.n == n:
                partes += ["{{novo}}", "", fragmento.gabarito, "", "{{/novo}}", ""]
            elif novos:
                partes += ['<details class="caderno-secao" markdown="1">',
                           f"<summary>Construída {_onde([fragmento.n])}. Clique para abrir</summary>", "",
                           fragmento.gabarito, "", "</details>", ""]
            else:
                partes += [fragmento.gabarito, ""]
        partes += ["</details>", ""]
    if pendentes:
        partes += ["Ainda em branco, para os próximos exercícios: " + ", ".join(pendentes), ""]
    return "\n".join(partes).rstrip() + "\n"


def _onde(ns: list[int]) -> str:
    if len(ns) == 1:
        return f"no exercício {ns[0]}"
    return "nos exercícios " + ", ".join(str(x) for x in ns[:-1]) + f" e {ns[-1]}"


def _com_gabarito(secoes: list[Secao]) -> set[int]:
    return {f.n for s in secoes for f in s.fragmentos if f.gabarito}


def render_mapa(secoes: list[Secao], existentes: set[int], docs: Path = DOCS) -> str:
    linhas = [
        "# Mapa do caderno arquitetural",
        "",
        "Para saber onde cada seção do caderno é preenchida, a tabela mostra o bloco que ensina o assunto, "
        "o exercício que preenche a seção e o gabarito em que o resultado aparece. As seções 0 e 10 são "
        "exceção, porque são revistas ao fim de cada aula, nos exercícios 4, 8, 12, 16, 20 e 24.",
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
            f"[Gabarito {n}](../gabaritos/gabarito-exercicio-{n:02d}.md)" if n in existentes else "Ainda não publicado"
        )
        linhas.append(f"| {_rotulo(secao)} | Aula {aula} | {bloco} | {exercicio} | {gabarito} |")
    return "\n".join(linhas) + "\n"


def render_indice(existentes: set[int]) -> str:
    partes = [
        "# Gabaritos",
        "",
        "O caderno arquitetural é o documento em que a arquitetura da solução da ACME vai sendo registrada "
        "ao longo do curso, e a [Aula 1](../modulo-1-fundamentos/index.md#o-fio-condutor-do-curso-o-caderno-arquitetural) "
        "explica o que ele é e para que serve cada seção. Depois de cada exercício o caderno está num estado "
        "diferente, com as respostas dos exercícios anteriores já escritas e o trecho do exercício atual em "
        "destaque, e cada gabarito mostra exatamente esse estado. Para ver o caderno vazio, use o "
        "[template](../caderno/template.md), e para saber qual exercício preenche cada seção, use o "
        "[mapa](../caderno/mapa.md).",
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
