"""Os blocos dos módulos 2 a 5 preenchem seções do caderno arquitetural."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

M2, M3 = "modulo-2-requisitos-e-partes-interessadas", "modulo-3-design-e-padroes"
M4, M5 = "modulo-4-dominios-da-solucao", "modulo-5-frameworks-e-tecnologias"

# bloco -> (exercício, fichas esperadas, âncoras do template esperadas)
BLOCOS = {
    f"{M2}/bloco-1-direcionadores-de-mudanca.md": (5, ["{{ficha:3}}"]),
    f"{M2}/bloco-2-qualidade-e-tipos-de-requisito.md": (6, ["{{ficha:3}}"]),
    f"{M2}/bloco-3-cenarios-linha-de-base-e-restricoes.md": (7, ["{{ficha:3}}", "{{ficha:4:2}}"]),
    f"{M2}/bloco-4-partes-interessadas-e-pontos-de-vista.md": (8, ["{{ficha:2}}"]),
    f"{M3}/bloco-1-principios-de-design.md": (9, ["{{ficha:6}}"]),
    f"{M3}/bloco-2-estilos-arquiteturais.md": (10, ["{{ficha:7:3}}"]),
    f"{M3}/bloco-3-padroes-arquiteturais-e-de-design.md": (11, ["{{ficha:7:3}}"]),
    f"{M3}/bloco-4-registro-de-decisao-arquitetural.md": (12, ["{{ficha:7:3}}"]),
    f"{M4}/bloco-1-arquitetura-de-negocio.md": (13, ["{{ficha:7:4}}"]),
    f"{M4}/bloco-2-arquitetura-de-dados.md": (14, ["{{ficha:7:4}}"]),
    f"{M4}/bloco-3-arquitetura-de-aplicacoes-e-integracao.md": (15, ["{{ficha:5}}"]),
    f"{M4}/bloco-4-arquitetura-de-infraestrutura.md": (16, ["{{ficha:7:4}}"]),
    f"{M5}/bloco-1-definicao-tecnologica-e-trm.md": (17, ["{{ficha:8}}"]),
    f"{M5}/bloco-2-plataforma-arquitetural.md": (18, ["{{ficha:8}}"]),
    f"{M5}/bloco-3-seguranca-fim-a-fim.md": (19, ["{{ficha:8}}"]),
    f"{M5}/bloco-4-adr-de-plataforma.md": (20, ["{{ficha:8}}"]),
}
MODULOS = {M2: 2, M3: 3, M4: 4, M5: 5}


def texto(bloco):
    return (DOCS / bloco).read_text(encoding="utf-8")


def itens(pagina):
    inicio = re.search(r"(?m)^## Exerc[ií]cio \d+\s*$", pagina).end()
    fim = pagina.index("\n## Fontes")
    partes = re.split(r"(?m)^### (Item \d+: .+)$", pagina[inicio:fim])
    return list(zip(partes[1::2], partes[2::2]))


class ModulosDoisACincoTest(unittest.TestCase):
    def test_secao_no_caderno_fica_entre_uso_e_exercicio(self):
        for bloco, (n, _) in BLOCOS.items():
            pagina = texto(bloco)
            with self.subTest(bloco=bloco):
                self.assertIn("## No caderno arquitetural", pagina)
                uso = pagina.index("## Uso pelo arquiteto")
                caderno = pagina.index("## No caderno arquitetural")
                exercicio = re.search(rf"(?m)^## Exerc[ií]cio {n}\s*$", pagina).start()
                self.assertLess(uso, caderno)
                self.assertLess(caderno, exercicio)

    def test_fichas_esperadas_abertas_e_fechadas(self):
        for bloco, (_, fichas) in BLOCOS.items():
            pagina = texto(bloco)
            with self.subTest(bloco=bloco):
                for ficha in fichas:
                    self.assertIn(ficha, pagina)
                self.assertEqual(len(fichas), pagina.count("{{/ficha}}"))

    def test_cada_ficha_explica_antes_de_pedir_e_aponta_template_e_gabarito(self):
        for bloco, (n, fichas) in BLOCOS.items():
            pagina = texto(bloco)
            with self.subTest(bloco=bloco):
                self.assertIn(f"gabaritos/gabarito-exercicio-{n:02d}.md", pagina)
                self.assertIn("caderno/template.md#", pagina)
                self.assertGreaterEqual(pagina.count("{ .caderno-botao }"), 2)
                for trecho in re.findall(r"\{\{ficha:.*?\{\{/ficha\}\}", pagina, re.DOTALL):
                    serve = trecho.index("**Para que serve.**")
                    faz = trecho.index("**O que você faz neste exercício.**")
                    tabela = trecho.index("| Campo do caderno | Como preencher | Item |")
                    self.assertLess(serve, faz)
                    self.assertLess(faz, tabela)
                    self.assertGreater(len(trecho[serve:faz].split()), 35)
                    self.assertGreater(len(trecho[faz:tabela].split()), 35)

    def test_cada_item_diz_qual_campo_do_caderno_a_resposta_preenche(self):
        for bloco in BLOCOS:
            for titulo, corpo in itens(texto(bloco)):
                with self.subTest(bloco=bloco, item=titulo):
                    self.assertRegex(corpo, r"(Sua resposta vira|Suas respostas viram)")
                    self.assertIn("caderno", corpo)

    def test_indice_de_cada_modulo_diz_o_que_a_aula_constroi_no_caderno(self):
        for modulo, aula in MODULOS.items():
            pagina = (DOCS / modulo / "index.md").read_text(encoding="utf-8")
            with self.subTest(modulo=modulo):
                self.assertIn(f"## Adições no Caderno Arquitetural da Aula {aula}", pagina)
                self.assertIn("{{trilha:", pagina)
                self.assertIn("../gabaritos/", pagina)

    def test_sintese_de_cada_modulo_aponta_para_os_gabaritos(self):
        for modulo in MODULOS:
            pagina = (DOCS / modulo / "sintese.md").read_text(encoding="utf-8")
            with self.subTest(modulo=modulo):
                self.assertNotIn("sem gabarito público", pagina)
                self.assertIn("../gabaritos/index.md", pagina)
