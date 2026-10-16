import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TERMOS = (
    "Descrição de arquitetura",
    "Entregável de arquitetura",
    "Artefato de arquitetura",
    "Entidade de arquitetura",
    "Caderno arquitetural",
)


class GlossarioDoCadernoTest(unittest.TestCase):
    def test_termos_do_caderno_estao_no_glossario(self):
        texto = (ROOT / "docs/referencia/glossario.md").read_text(encoding="utf-8")
        for termo in TERMOS:
            with self.subTest(termo=termo):
                self.assertIn(f"\n## {termo}\n", texto)

    def test_corpo_nao_cita_o_livro_texto(self):
        texto = (ROOT / "docs/referencia/glossario.md").read_text(encoding="utf-8")
        self.assertNotIn("Lovatt", texto)
