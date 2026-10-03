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
        out.append(f'  <text x="520" y="{y + 28}" class="q">{pergunta}</text>')
        cell(out, 206, y + 48, 290, 86, recebe, "#F2F6FB", "#9AA9BC")
        cell(out, 520, y + 48, 320, 86, decide, "#FFF1D6", "#F2B84B")
        cell(out, 864, y + 48, 300, 86, entrega, "#F2F6FB", "#9AA9BC")
        out.append(f'  <rect x="20" y="{y + 30}" width="140" height="90" rx="12" fill="#D8E9FF" stroke="#254DB8" stroke-width="2"/>')
        top = y + 75 - (len(eixo) - 1) * 10 + 6
        for i, line in enumerate(eixo):
            out.append(f'  <text x="90" y="{top + i * 20:.0f}" text-anchor="middle" class="ax">{line}</text>')
        if y != ys[-1]:
            out.append(f'  <path d="M90 {y + 120}V{y + 198}" stroke="#254DB8" stroke-width="2.5" fill="none" marker-end="url(#a)"/>')
    out.append('  <path d="M450 100V206" stroke="#52657E" stroke-width="2.5" fill="none" marker-end="url(#a)"/>')
    for y in ys[:-1]:
        out.append(f'  <path d="M1014 {y + 134}V{y + 160}H450V{y + 216}" stroke="#52657E" stroke-width="2.5" fill="none" marker-end="url(#a)"/>')
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
