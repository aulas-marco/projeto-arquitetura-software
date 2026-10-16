import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOCO = ROOT / "docs" / "modulo-1-fundamentos" / "bloco-9-teste.md"

BASE = """# Bloco

## Antes de começar

- termo

## Conceito

Texto.

## Uso pelo arquiteto

Texto.

{caderno}## Exercício 9

### Item 1: A

Texto.

## Fontes

- Fonte.
"""
SECAO = "## No caderno arquitetural\n\nSeção 1.\n\n"


def validador():
    spec = importlib.util.spec_from_file_location("validate_content", ROOT / "scripts" / "validate_content.py")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


class AnatomiaComCadernoTest(unittest.TestCase):
    def setUp(self):
        self.v = validador()

    def test_bloco_fora_do_conjunto_nao_precisa_da_secao(self):
        self.assertEqual([], self.v.check_block_anatomy(BLOCO, BASE.format(caderno="")))

    def test_bloco_no_conjunto_exige_a_secao(self):
        self.v.CADERNO_BLOCKS = {"bloco-9-teste.md"}
        erros = self.v.check_block_anatomy(BLOCO, BASE.format(caderno=""))
        self.assertEqual(1, len(erros))
        self.assertIn("No caderno arquitetural", erros[0])

    def test_bloco_no_conjunto_com_a_secao_na_posicao_certa_passa(self):
        self.v.CADERNO_BLOCKS = {"bloco-9-teste.md"}
        self.assertEqual([], self.v.check_block_anatomy(BLOCO, BASE.format(caderno=SECAO)))

    def test_secao_fora_de_ordem_e_rejeitada_mesmo_fora_do_conjunto(self):
        texto = BASE.format(caderno="").replace("## Uso pelo arquiteto", SECAO + "## Uso pelo arquiteto")
        erros = self.v.check_block_anatomy(BLOCO, texto)
        self.assertEqual(1, len(erros))
        self.assertIn("fora da ordem", erros[0])

    def test_module_aceita_caderno_e_gabaritos(self):
        self.assertIn("caderno", self.v.EXTRA_SECTIONS)
        self.assertIn("gabaritos", self.v.EXTRA_SECTIONS)
