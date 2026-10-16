"""A Aula 6 (governança, aceleradores de IA e apresentação do caderno) preenche as seções finais do caderno."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
M6 = "modulo-6-governanca-ia-e-caderno"

# bloco -> (exercícios, fichas esperadas)
BLOCOS = {
    f"{M6}/bloco-1-governanca-da-mudanca.md": ((21, 22), ["{{ficha:4:6}}", "{{ficha:9}}", "{{ficha:9}}"]),
    f"{M6}/bloco-2-aceleradores-de-ia.md": ((23,), ["{{ficha:9}}"]),
    f"{M6}/bloco-3-apresentacao-do-caderno.md": ((24,), ["{{ficha:0:6}}", "{{ficha:10:6}}"]),
}


def texto(bloco):
    return (DOCS / bloco).read_text(encoding="utf-8")


def itens(pagina):
    inicio = re.search(r"(?m)^## Exerc[ií]cio \d+\s*$", pagina).end()
    fim = pagina.index("\n## Fontes")
    partes = re.split(r"(?m)^### (Item \d+: .+)$", pagina[inicio:fim])
    return list(zip(partes[1::2], partes[2::2]))


class Modulo6Test(unittest.TestCase):
    def test_secao_no_caderno_fica_entre_uso_e_exercicio(self):
        for bloco, (ns, _) in BLOCOS.items():
            pagina = texto(bloco)
            with self.subTest(bloco=bloco):
                uso = pagina.index("## Uso pelo arquiteto")
                caderno = pagina.index("## No caderno arquitetural")
                primeiro = re.search(rf"(?m)^## Exerc[ií]cio {ns[0]}\s*$", pagina).start()
                self.assertLess(uso, caderno)
                self.assertLess(caderno, primeiro)

    def test_cada_exercicio_do_bloco_tem_sua_secao(self):
        for bloco, (ns, _) in BLOCOS.items():
            pagina = texto(bloco)
            for n in ns:
                with self.subTest(bloco=bloco, exercicio=n):
                    self.assertRegex(pagina, rf"(?m)^## Exerc[ií]cio {n}\s*$")

    def test_fichas_esperadas_abertas_e_fechadas(self):
        for bloco, (_, fichas) in BLOCOS.items():
            pagina = texto(bloco)
            with self.subTest(bloco=bloco):
                for ficha in set(fichas):
                    self.assertGreaterEqual(pagina.count(ficha), fichas.count(ficha))
                self.assertEqual(len(fichas), pagina.count("{{/ficha}}"))

    def test_cada_ficha_explica_antes_de_pedir_e_aponta_template_e_gabarito(self):
        for bloco, (ns, _) in BLOCOS.items():
            pagina = texto(bloco)
            with self.subTest(bloco=bloco):
                for n in ns:
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

    def test_bloco_1_usa_a_figura_do_adm_com_as_fases_e_a_h(self):
        pagina = texto(f"{M6}/bloco-1-governanca-da-mudanca.md")
        self.assertIn("modulo-6-adm-governar-a-mudanca.svg", pagina)
        alt = re.search(r"!\[([^\]]+)\]\([^)]*modulo-6-adm-governar-a-mudanca\.svg\)", pagina)
        self.assertIsNotNone(alt)
        self.assertIn("fases E, F, G e H", alt.group(1))
        self.assertTrue((DOCS / "assets" / "images" / "modulo-6-adm-governar-a-mudanca.svg").is_file())

    def test_indice_da_aula_6_diz_o_que_a_aula_constroi_no_caderno(self):
        pagina = (DOCS / M6 / "index.md").read_text(encoding="utf-8")
        self.assertIn("## Adições no Caderno Arquitetural da Aula 6", pagina)
        self.assertIn("{{trilha:", pagina)
        self.assertIn("../gabaritos/", pagina)

    def test_indice_traz_a_grade_com_um_unico_kahoot_depois_do_intervalo(self):
        pagina = (DOCS / M6 / "index.md").read_text(encoding="utf-8")
        grade = pagina[pagina.index("## Grade de tempo"):]
        grade = grade[: grade.index("\n## ", 5)] if "\n## " in grade[5:] else grade
        linhas = [l for l in grade.splitlines() if l.startswith("| ") and "Kahoot" in l]
        self.assertEqual(1, len(linhas))
        self.assertLess(grade.index("Intervalo"), grade.index(linhas[0]))

    def test_sintese_aponta_para_os_gabaritos(self):
        pagina = (DOCS / M6 / "sintese.md").read_text(encoding="utf-8")
        self.assertNotIn("sem gabarito público", pagina)
        self.assertIn("../gabaritos/index.md", pagina)

    def test_gabaritos_21_a_24_existem_como_paginas(self):
        for n in (21, 22, 23, 24):
            with self.subTest(exercicio=n):
                self.assertTrue((DOCS / "gabaritos" / f"gabarito-exercicio-{n:02d}.md").is_file())


if __name__ == "__main__":
    unittest.main()
