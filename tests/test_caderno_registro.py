"""O registro fixa seções, exercícios e códigos do caderno."""

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def carregar():
    spec = importlib.util.spec_from_file_location(
        "caderno_registro", ROOT / "scripts" / "caderno_registro.py"
    )
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


class RegistroTest(unittest.TestCase):
    def setUp(self):
        self.reg = carregar()

    def test_onze_secoes_numeradas_de_zero_a_dez(self):
        self.assertEqual(list(range(11)), sorted(self.reg.TITULOS_SECAO))

    def test_vinte_e_quatro_exercicios_com_plano(self):
        self.assertEqual(list(range(1, 25)), sorted(self.reg.EXERCICIOS))
        self.assertEqual(sorted(self.reg.EXERCICIOS), sorted(self.reg.PLANO))

    def test_plano_so_usa_secoes_que_acumulam(self):
        for n, secoes in self.reg.PLANO.items():
            for secao in secoes:
                with self.subTest(exercicio=n, secao=secao):
                    self.assertIn(secao, self.reg.TITULOS_SECAO)
                    self.assertNotIn(secao, self.reg.SUBSTITUI)

    def test_secoes_que_substituem_so_aceitam_o_fim_de_cada_aula(self):
        for secao, exercicios in self.reg.SUBSTITUI.items():
            self.assertEqual((4, 8, 12, 16, 20, 24), exercicios, secao)

    def test_os_vinte_primeiros_exercicios_apontam_para_blocos_existentes(self):
        for n in range(1, 21):
            _, arquivo, _ = self.reg.EXERCICIOS[n]
            with self.subTest(exercicio=n):
                texto = (DOCS / arquivo).read_text(encoding="utf-8")
                self.assertRegex(texto, rf"(?m)^## Exerc[ií]cio {n}\s*$")

    def test_codigos_de_artefato(self):
        self.assertEqual(
            ("D", "PR", "RT", "R", "RD", "CQ", "LB", "L", "P", "DD", "DL", "B", "I", "ADR", "C", "DS", "LG", "FA", "CP", "N", "T", "A"),
            self.reg.CODIGOS,
        )
