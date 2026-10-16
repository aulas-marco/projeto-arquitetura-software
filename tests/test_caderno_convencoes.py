import importlib.util
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGINA = ROOT / "docs" / "caderno" / "convencoes.md"


def codigos():
    spec = importlib.util.spec_from_file_location("caderno_registro", ROOT / "scripts" / "caderno_registro.py")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.CODIGOS


class ConvencoesTest(unittest.TestCase):
    def test_cada_codigo_tem_linha_na_tabela(self):
        texto = PAGINA.read_text(encoding="utf-8")
        primeira_coluna = set(re.findall(r"(?m)^\| ([A-Z]{1,3}) \|", texto))
        self.assertEqual(set(codigos()), primeira_coluna)

    def test_define_os_marcadores_de_estado(self):
        texto = PAGINA.read_text(encoding="utf-8")
        self.assertIn("**proposto**", texto)
        self.assertIn("**a definir**", texto)
