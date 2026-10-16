"""Contrato da fonte do caderno e dos gabaritos publicados."""

import importlib.util
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CAMPOS_DA_TABELA = ("Para que serve", "Pergunta que responde", "O que você escreve", "Vem de onde", "Quando se preenche")


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

    def test_exercicios_1_a_4_tem_gabarito_e_as_secoes_de_substituicao_tem_a_versao_4(self):
        por_numero = {s.numero: s for s in self.secoes}
        com_gabarito = {f.n for f in por_numero[1].fragmentos if f.gabarito}
        self.assertEqual({1, 2, 3, 4}, com_gabarito)
        for numero in (0, 10):
            with self.subTest(secao=numero):
                versoes = {f.n for f in por_numero[numero].fragmentos if f.gabarito}
                self.assertIn(4, versoes)

    def test_gabaritos_1_a_4_existem_como_paginas(self):
        for n in (1, 2, 3, 4):
            with self.subTest(exercicio=n):
                self.assertTrue((DOCS / "gabaritos" / f"gabarito-exercicio-{n:02d}.md").is_file())

    def test_todo_campo_da_ficha_de_um_bloco_existe_no_template(self):
        """Spec 6.3: o campo que a seção No caderno arquitetural lista existe nos campos da fonte."""
        validador = carregar("validate_content")
        por_arquivo = {Path(arquivo).name: n for n, (_, arquivo, _) in self.reg.EXERCICIOS.items()}
        for nome in sorted(validador.CADERNO_BLOCKS):
            n = por_arquivo[nome]
            pagina = next((DOCS).glob(f"modulo-*/{nome}")).read_text(encoding="utf-8")
            ficha = pagina[pagina.index("{{ficha:"):pagina.index("{{/ficha}}")]
            campos_da_ficha = [
                linha.split("|")[1].strip()
                for linha in ficha.splitlines()
                if linha.startswith("| ") and not linha.startswith(("| Campo", "| ---"))
            ]
            campos_da_fonte = " ".join(
                f.campos for secao in self.secoes for f in secao.fragmentos if f.n == n
            ).casefold()
            with self.subTest(bloco=nome):
                self.assertGreaterEqual(len(campos_da_ficha), 3)
                for campo in campos_da_ficha:
                    with self.subTest(campo=campo):
                        self.assertIn(campo.casefold(), campos_da_fonte)
