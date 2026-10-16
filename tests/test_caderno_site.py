"""Páginas do caderno e dos gabaritos entram no site e coincidem com a fonte."""

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def gerador():
    spec = importlib.util.spec_from_file_location("gerar_caderno", ROOT / "scripts" / "gerar_caderno.py")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


class SiteDoCadernoTest(unittest.TestCase):
    def test_paginas_geradas_coincidem_com_a_fonte(self):
        ger = gerador()
        self.assertEqual([], ger.divergencias(ger.saidas(ger.carregar())))

    def test_nav_lista_as_paginas_do_caderno_e_cada_gabarito(self):
        nav = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
        for pagina in ("caderno/template.md", "caderno/convencoes.md", "caderno/mapa.md", "gabaritos/index.md"):
            with self.subTest(pagina=pagina):
                self.assertIn(pagina, nav)
                self.assertTrue((DOCS / pagina).is_file())
        for gabarito in sorted((DOCS / "gabaritos").glob("gabarito-exercicio-*.md")):
            with self.subTest(gabarito=gabarito.name):
                self.assertIn(f"gabaritos/{gabarito.name}", nav)

    def test_estilo_do_destaque_existe_e_o_css_tem_versao_nova(self):
        css = (DOCS / "assets" / "stylesheets" / "extra.css").read_text(encoding="utf-8")
        for classe in (".caderno-ficha", ".caderno-trilha", ".caderno-folha", ".caderno-progresso", ".caderno-novo"):
            with self.subTest(classe=classe):
                self.assertIn(classe, css)
        self.assertIn("scripts/caderno_hooks.py", (ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
        self.assertIn("extra.css?v=20261016-2", (ROOT / "mkdocs.yml").read_text(encoding="utf-8"))

    def test_pagina_inicial_apresenta_o_caderno(self):
        texto = (DOCS / "index.md").read_text(encoding="utf-8")
        self.assertIn("## O caderno arquitetural", texto)
        self.assertIn("caderno/template.md", texto)
