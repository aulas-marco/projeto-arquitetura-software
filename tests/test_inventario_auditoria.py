"""Inventário de auditoria: cada página, exercício, item, termo e item de síntese vira uma linha."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def carregar():
    spec = importlib.util.spec_from_file_location(
        "inventario_auditoria", ROOT / "scripts" / "inventario_auditoria.py"
    )
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


class InventarioTest(unittest.TestCase):
    def setUp(self):
        self.inv = carregar()

    def test_lista_os_vinte_exercicios_e_o_glossario_inteiro(self):
        linhas = self.inv.inventariar(ROOT / "docs")
        exercicios = [l for l in linhas if l[0] == "exercício"]
        # Uma linha por página de bloco com exercício: 20 das Aulas 1 a 5 e 3 da Aula 6.
        self.assertEqual(23, len(exercicios))
        termos = [l for l in linhas if l[0] == "termo"]
        glossario = (ROOT / "docs/referencia/glossario.md").read_text(encoding="utf-8")
        self.assertEqual(glossario.count("\n## "), len(termos))

    def test_ignora_superpowers_caderno_e_gabaritos(self):
        linhas = self.inv.inventariar(ROOT / "docs")
        for _, local, _ in linhas:
            self.assertFalse(local.startswith(("superpowers/", "caderno/", "gabaritos/")), local)

    def test_item_de_exercicio_e_item_de_sintese_tem_local_com_ancora(self):
        linhas = self.inv.inventariar(ROOT / "docs")
        itens = [l for l in linhas if l[0] == "item"]
        self.assertTrue(all("#exercicio-" in l[1] for l in itens))
        self.assertGreaterEqual(len(itens), 40)
        sintese = [l for l in linhas if l[0] == "síntese"]
        self.assertGreaterEqual(len(sintese), 40)

    def test_renderizar_gera_tabela_com_colunas_de_decisao(self):
        texto = self.inv.renderizar([("página", "index.md", "Início")])
        self.assertIn("| Tipo | Local | Rótulo | Seção do caderno | Decisão | Justificativa |", texto)
        self.assertIn("| página | index.md | Início |  |  |  |", texto)

    def test_exercicio_em_pagina_temporaria(self):
        with tempfile.TemporaryDirectory() as tmp:
            docs = Path(tmp)
            (docs / "modulo-9").mkdir()
            (docs / "modulo-9" / "bloco-1.md").write_text(
                "# Bloco\n\n## Exercício 3\n\n### Item 1: A\n\ntexto\n\n### Item 2: B\n\n## Fontes\n",
                encoding="utf-8",
            )
            linhas = self.inv.inventariar(docs)
        tipos = [l[0] for l in linhas]
        self.assertEqual(["página", "exercício", "item", "item"], tipos)
