"""Hook que expande a marcação do caderno em HTML."""

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def carregar():
    spec = importlib.util.spec_from_file_location("caderno_hooks", ROOT / "scripts" / "caderno_hooks.py")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


class HooksTest(unittest.TestCase):
    def setUp(self):
        self.h = carregar()

    def test_trilha_tem_onze_nos_e_marca_a_atual(self):
        html = self.h.expandir("{{trilha:3}}")
        self.assertEqual(11, html.count("<li"))
        self.assertEqual(1, html.count('aria-current="step"'))
        self.assertEqual(3, html.count('class="feito"'))
        self.assertIn("Seção 3 de 10", html)

    def test_trilha_todas_nao_marca_atual(self):
        html = self.h.expandir("{{trilha:todas}}")
        self.assertEqual(11, html.count("<li"))
        self.assertNotIn("aria-current", html)

    def test_ficha_abre_com_cabecalho_e_fecha(self):
        html = self.h.expandir("{{ficha:1}}\n\ncorpo\n\n{{/ficha}}")
        self.assertIn('<div class="caderno-ficha" markdown="1">', html)
        self.assertIn("Contexto", html)
        self.assertIn("Aula 1", html)
        self.assertIn("Exercícios 1, 2, 3 e 4", html)
        self.assertTrue(html.rstrip().endswith("</div>"))

    def test_folha_traz_numeral_e_parte(self):
        html = self.h.expandir("{{folha:7}}\n\ncorpo\n\n{{/folha}}")
        self.assertIn('data-secao="7"', html)
        self.assertIn('data-parte="II"', html)

    def test_progresso_tem_vinte_e_quatro_segmentos(self):
        html = self.h.expandir("{{progresso:5}}")
        self.assertEqual(24, html.count('<span class="seg'))
        self.assertEqual(4, html.count("seg feito"))
        self.assertEqual(1, html.count("seg atual"))
        self.assertIn("Exercício 5 de 24", html)

    def test_novo_abre_e_fecha(self):
        html = self.h.expandir("{{novo}}\n\ncorpo\n\n{{/novo}}")
        self.assertIn('<div class="caderno-novo" markdown="1">', html)
        self.assertTrue(html.rstrip().endswith("</div>"))

    def test_numero_fora_da_faixa_e_rejeitado(self):
        for entrada in ("{{trilha:11}}", "{{ficha:12}}", "{{progresso:0}}", "{{progresso:25}}"):
            with self.subTest(entrada=entrada):
                with self.assertRaises(ValueError):
                    self.h.expandir(entrada)

    def test_marcacao_desconhecida_e_rejeitada(self):
        with self.assertRaises(ValueError):
            self.h.expandir("{{ficha}}")

    def test_toda_marcacao_do_repositorio_e_valida(self):
        for caminho in sorted(DOCS.rglob("*.md")):
            if "superpowers" in caminho.parts:
                continue
            texto = caminho.read_text(encoding="utf-8")
            if "{{" not in texto:
                continue
            with self.subTest(pagina=str(caminho.relative_to(DOCS))):
                self.assertNotIn("{{", self.h.expandir(texto))

    def test_ficha_aberta_sem_fechamento_e_rejeitada(self):
        with self.assertRaises(ValueError):
            self.h.expandir("{{ficha:1}}\n\ncorpo")
