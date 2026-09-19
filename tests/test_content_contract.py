import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ContentContractTest(unittest.TestCase):
    def test_validator_exists_and_runs(self):
        result = subprocess.run(
            ["python3", "scripts/validate_content.py"],
            cwd=ROOT, text=True, capture_output=True,
        )
        self.assertIn(result.returncode, (0, 1), result.stderr)

    def test_validator_declares_the_six_modules(self):
        text = (ROOT / "scripts/validate_content.py").read_text(encoding="utf-8")
        for slug in (
            "modulo-1-fundamentos",
            "modulo-2-plataforma-e-modelos",
            "modulo-3-descoberta-e-riscos",
            "modulo-4-dados-e-seguranca",
            "modulo-5-blueprint-e-trm",
            "modulo-6-evolucao-e-governanca",
        ):
            self.assertIn(f'"{slug}"', text, slug)

    def test_validator_declares_the_named_block_sections(self):
        text = (ROOT / "scripts/validate_content.py").read_text(encoding="utf-8")
        # Seis das oito secoes da anatomia sao cabecalhos. As outras duas,
        # titulo e linha de enquadramento, nao sao verificaveis por nome.
        for section in ("Antes de começar", "Conceito", "Uso pelo arquiteto",
                        "Exercício", "Gabarito", "Fontes"):
            self.assertIn(section, text, section)

    def test_validator_rejects_forbidden_editorial_markers(self):
        text = (ROOT / "scripts/validate_content.py").read_text(encoding="utf-8")
        for marker in ("TODO", "TBD", "PLACEHOLDER", "PREENCHER"):
            self.assertIn(marker, text, marker)

    def test_validator_does_not_flag_portuguese_words_as_markers(self):
        """"todo" e "preencher" sao palavras correntes em portugues."""
        page = ROOT / "docs" / "_teste_portugues.md"
        page.write_text(
            "# Teste\n\nTodo o material precisa preencher o criterio.\n",
            encoding="utf-8",
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertNotIn("_teste_portugues", result.stdout)
        finally:
            page.unlink()

    def test_validator_catches_a_semicolon_in_prose(self):
        offender = ROOT / "docs" / "_teste_temporario.md"
        offender.write_text("# Teste\n\nUma frase; outra frase.\n", encoding="utf-8")
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertEqual(1, result.returncode)
            self.assertIn("ponto-e-virgula", result.stdout)
        finally:
            offender.unlink()

    def test_validator_ignores_semicolon_inside_code_fence(self):
        allowed = ROOT / "docs" / "_teste_codigo.md"
        allowed.write_text(
            "# Teste\n\n```javascript\nconst a = 1;\n```\n", encoding="utf-8"
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertNotIn("_teste_codigo", result.stdout)
        finally:
            allowed.unlink()


if __name__ == "__main__":
    unittest.main()
