"""Contrato da fonte do caderno e dos gabaritos publicados."""

import importlib.util
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CAMPOS_DA_TABELA = ("O que vai", "Pergunta que responde", "Artefatos", "Entrada", "Preenchida em")


def carregar(nome):
    spec = importlib.util.spec_from_file_location(nome, ROOT / "scripts" / f"{nome}.py")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


class ContratoDoCadernoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ger = carregar("gerar_caderno")
        cls.reg = carregar("caderno_registro")
        cls.secoes = cls.ger.carregar()

    def test_fonte_tem_as_onze_secoes_com_o_titulo_do_registro(self):
        self.assertEqual(sorted(self.reg.TITULOS_SECAO), [s.numero for s in self.secoes])
        for secao in self.secoes:
            with self.subTest(secao=secao.numero):
                self.assertEqual(self.reg.TITULOS_SECAO[secao.numero], secao.titulo)

    def test_secoes_que_substituem_sao_as_do_registro(self):
        for secao in self.secoes:
            esperado = "substitui" if secao.numero in self.reg.SUBSTITUI else "acumula"
            with self.subTest(secao=secao.numero):
                self.assertEqual(esperado, secao.modo)

    def test_orientacao_traz_as_cinco_linhas_da_tabela(self):
        for secao in self.secoes:
            for campo in CAMPOS_DA_TABELA:
                with self.subTest(secao=secao.numero, campo=campo):
                    self.assertRegex(secao.orientacao, rf"(?m)^\| {re.escape(campo)}")

    def test_fragmentos_respeitam_o_plano(self):
        for secao in self.secoes:
            for fragmento in secao.fragmentos:
                with self.subTest(secao=secao.numero, exercicio=fragmento.n):
                    if secao.modo == "substitui":
                        self.assertIn(fragmento.n, self.reg.SUBSTITUI[secao.numero])
                    else:
                        self.assertIn(secao.numero, self.reg.PLANO[fragmento.n])

    def test_cada_gabarito_publicado_tem_enunciado_que_aponta_de_volta(self):
        for caminho in sorted((DOCS / "gabaritos").glob("gabarito-exercicio-*.md")):
            n = int(re.search(r"(\d+)\.md$", caminho.name).group(1))
            _, arquivo, _ = self.reg.EXERCICIOS[n]
            with self.subTest(exercicio=n):
                pagina = (DOCS / arquivo).read_text(encoding="utf-8")
                self.assertIn(f"gabaritos/{caminho.name}", pagina)

    def test_gabaritos_cumulativos_a_versao_n_contem_os_trechos_anteriores(self):
        existentes = sorted({f.n for s in self.secoes for f in s.fragmentos if f.gabarito})
        for anterior, seguinte in zip(existentes, existentes[1:]):
            texto_n = self.ger.render_gabarito(self.secoes, seguinte, DOCS)
            for secao in self.secoes:
                if secao.modo != "acumula":
                    continue
                for fragmento in secao.fragmentos:
                    if fragmento.gabarito and fragmento.n <= anterior:
                        with self.subTest(de=anterior, para=seguinte, secao=secao.numero):
                            self.assertIn(fragmento.gabarito, texto_n)
