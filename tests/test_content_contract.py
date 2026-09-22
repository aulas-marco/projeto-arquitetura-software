import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


class ContentContractTest(unittest.TestCase):
    def test_module_one_visuals_are_anchored_in_the_acme_case(self):
        """As figuras da Aula 1 precisam ensinar usando conceitos e artefatos do caso."""
        expected_terms = {
            "modulo-1-visao-da-solucao.svg": ("ACME", "Escopo", "Processo"),
            "modulo-1-arquitetura-corporativa-togaf.svg": (
                "TOGAF", "D1", "transversal", "Arquitetura de solução · D2",
                "Arquitetura de software · D3",
            ),
            "modulo-1-solucao-como-sistema.svg": (
                "R7", "lote diário", "10 minutos", "AVA", "Confirmação",
            ),
            "modulo-1-papel-arquiteto.svg": ("T1", "T10", "Tecnologia"),
            "modulo-1-processo-definicao-arquitetura.svg": ("A1", "A10", "Linha de base"),
            "modulo-1-sintese-fundamentos.svg": ("ACME", "R7", "A1"),
        }
        for filename, terms in expected_terms.items():
            with self.subTest(image=filename):
                image = (DOCS / "assets" / "images" / filename).read_text(encoding="utf-8")
                for term in terms:
                    self.assertIn(term, image)

    def test_module_one_pages_have_descriptive_illustrations(self):
        """Cada página da Aula 1 deve conter ao menos um diagrama local com alt text."""
        module = DOCS / "modulo-1-fundamentos"
        for page in sorted(module.glob("*.md")):
            with self.subTest(page=page.name):
                text = page.read_text(encoding="utf-8")
                self.assertRegex(
                    text,
                    r"!\[[^\]]+\]\(\.\./assets/images/modulo-1-[^)]+\.svg\)",
                )

    def test_block_one_includes_togaf_enterprise_architecture_diagram(self):
        page = DOCS / "modulo-1-fundamentos" / "bloco-1-arquitetura-de-solucoes-e-de-software.md"
        self.assertIn(
            "../assets/images/modulo-1-arquitetura-corporativa-togaf.svg",
            page.read_text(encoding="utf-8"),
        )

    def test_r7_figure_follows_its_case_context(self):
        """O diagrama R7 só faz sentido depois de o requisito ter sido apresentado."""
        page = DOCS / "modulo-1-fundamentos" / "bloco-2-a-solucao-como-sistema.md"
        text = page.read_text(encoding="utf-8")
        self.assertLess(
            text.index("registrado como R7 no dossiê do caso"),
            text.index("../assets/images/modulo-1-solucao-como-sistema.svg"),
        )

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
            "modulo-2-requisitos-e-partes-interessadas",
            "modulo-3-design-e-padroes",
            "modulo-4-protocolos-e-representacao",
            "modulo-5-frameworks-e-tecnologias",
            "modulo-6-lacunas-e-governanca",
        ):
            self.assertIn(f'"{slug}"', text, slug)

    def test_validator_declares_the_named_block_sections(self):
        text = (ROOT / "scripts/validate_content.py").read_text(encoding="utf-8")
        # Cinco das sete secoes da anatomia sao cabecalhos. As outras duas,
        # titulo e linha de enquadramento, nao sao verificaveis por nome.
        for section in ("Antes de começar", "Conceito", "Uso pelo arquiteto",
                        "Exercício", "Fontes"):
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

    def test_validator_catches_two_em_dashes_in_same_paragraph_across_lines(self):
        offender = ROOT / "docs" / "_teste_travessao_paragrafo.md"
        offender.write_text(
            "# Teste\n\n"
            "Uma frase — com aposto isolado na primeira linha\n"
            "e outra linha — com outro aposto no mesmo paragrafo.\n",
            encoding="utf-8",
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertEqual(1, result.returncode)
            self.assertIn("mais de um travessao no paragrafo", result.stdout)
        finally:
            offender.unlink()

    def test_validator_exempts_bibliografia_from_em_dash_limit(self):
        """Titulo oficial de norma tecnica usa travessao duplo por convencao.

        A bibliografia e o unico arquivo isento dessa checagem, porque cita
        titulos oficiais (por exemplo ISO/IEC 25010) que o curso nao pode
        truncar sem alterar o dado bibliografico.
        """
        target = ROOT / "docs" / "referencia" / "bibliografia.md"
        original = target.read_text(encoding="utf-8")
        try:
            target.write_text(
                "# Bibliografia\n\n"
                "- Norma X. *Titulo A — Titulo B — Titulo C*.\n",
                encoding="utf-8",
            )
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertNotIn("mais de um travessao no paragrafo", result.stdout)
        finally:
            target.write_text(original, encoding="utf-8")

    def test_validator_allows_single_em_dash_split_across_two_lines(self):
        allowed = ROOT / "docs" / "_teste_travessao_unico.md"
        allowed.write_text(
            "# Teste\n\n"
            "Uma frase — com aposto isolado que continua\n"
            "na segunda linha do mesmo paragrafo sem outro travessao.\n",
            encoding="utf-8",
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertNotIn("_teste_travessao_unico", result.stdout)
        finally:
            allowed.unlink()

    def test_validator_exempts_fontes_section_from_em_dash_limit(self):
        """A secao Fontes lista referencias em APA, com titulos oficiais de norma."""
        allowed = DOCS / "modulo-1-fundamentos" / "bloco-9-teste-fontes.md"
        allowed.write_text(
            "# Bloco teste\n\n"
            "## Antes de começar\n\nTexto.\n\n"
            "## Conceito\n\nTexto.\n\n"
            "## Uso pelo arquiteto\n\nTexto.\n\n"
            "## Exercício 1\n\nTexto.\n\n"
            "## Fontes\n\n"
            "- Norma X. *Titulo A — Titulo B — Titulo C*.\n",
            encoding="utf-8",
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertNotIn("bloco-9-teste-fontes", result.stdout)
        finally:
            allowed.unlink()

    def test_validator_still_counts_em_dashes_outside_fontes(self):
        offender = DOCS / "modulo-1-fundamentos" / "bloco-9-teste-conceito.md"
        offender.write_text(
            "# Bloco teste\n\n"
            "## Antes de começar\n\nTexto.\n\n"
            "## Conceito\n\nUma frase — com aposto — e outro aposto.\n\n"
            "## Uso pelo arquiteto\n\nTexto.\n\n"
            "## Exercício 1\n\nTexto.\n\n"
            "## Fontes\n\nTexto.\n",
            encoding="utf-8",
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertEqual(1, result.returncode)
            self.assertIn("mais de um travessao no paragrafo", result.stdout)
        finally:
            offender.unlink()

    def test_validator_catches_heading_opening_with_por_que(self):
        offender = ROOT / "docs" / "_teste_titulo_por_que.md"
        offender.write_text("# Por que isso importa\n\nTexto qualquer.\n", encoding="utf-8")
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertEqual(1, result.returncode)
            self.assertIn("titulo abre com Por que", result.stdout)
        finally:
            offender.unlink()

    def test_validator_allows_functional_heading(self):
        allowed = ROOT / "docs" / "_teste_titulo_funcional.md"
        allowed.write_text("# Requisitos de qualidade\n\nTexto qualquer.\n", encoding="utf-8")
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertNotIn("_teste_titulo_funcional", result.stdout)
        finally:
            allowed.unlink()

    def test_validator_catches_heading_with_subtitle_after_em_dash(self):
        offender = ROOT / "docs" / "_teste_titulo_subtitulo.md"
        offender.write_text("# Requisitos — o que sao\n\nTexto qualquer.\n", encoding="utf-8")
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertEqual(1, result.returncode)
            self.assertIn("titulo com subtitulo apos travessao", result.stdout)
        finally:
            offender.unlink()

    def test_validator_catches_broken_relative_link(self):
        offender = ROOT / "docs" / "_teste_link_quebrado.md"
        offender.write_text(
            "# Teste\n\nVeja [aqui](./nao-existe.md) para mais detalhes.\n",
            encoding="utf-8",
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertEqual(1, result.returncode)
            self.assertIn("link relativo quebrado", result.stdout)
        finally:
            offender.unlink()

    def test_validator_allows_relative_link_to_existing_file(self):
        allowed = ROOT / "docs" / "_teste_link_ok.md"
        allowed.write_text(
            "# Teste\n\nVeja [indice](index.md) para mais detalhes.\n",
            encoding="utf-8",
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertNotIn("_teste_link_ok", result.stdout)
        finally:
            allowed.unlink()

    def test_validator_catches_block_page_missing_sections(self):
        offender = DOCS / "modulo-1-fundamentos" / "bloco-teste-incompleto.md"
        offender.write_text(
            "# Bloco teste\n\nConceito sem as secoes nomeadas.\n", encoding="utf-8"
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertEqual(1, result.returncode)
            self.assertIn("falta a secao", result.stdout)
        finally:
            offender.unlink()

    def test_validator_allows_block_page_with_all_sections_in_order(self):
        allowed = DOCS / "modulo-1-fundamentos" / "bloco-teste-completo.md"
        allowed.write_text(
            "# Bloco teste\n\n"
            "## Antes de começar\n\nTexto.\n\n"
            "## Conceito\n\nTexto.\n\n"
            "## Uso pelo arquiteto\n\nTexto.\n\n"
            "## Exercício 1\n\nTexto.\n\n"
            "## Fontes\n\nTexto.\n",
            encoding="utf-8",
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertNotIn("bloco-teste-completo", result.stdout)
        finally:
            allowed.unlink()

    def test_validator_catches_block_page_sections_out_of_order(self):
        offender = DOCS / "modulo-1-fundamentos" / "bloco-teste-fora-de-ordem.md"
        offender.write_text(
            "# Bloco teste\n\n"
            "## Conceito\n\nTexto.\n\n"
            "## Antes de começar\n\nTexto.\n\n"
            "## Uso pelo arquiteto\n\nTexto.\n\n"
            "## Exercício 1\n\nTexto.\n\n"
            "## Fontes\n\nTexto.\n",
            encoding="utf-8",
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertEqual(1, result.returncode)
            self.assertIn("fora da ordem", result.stdout)
        finally:
            offender.unlink()

    def test_validator_catches_nonexistent_anchor(self):
        offender = ROOT / "docs" / "_teste_ancora_quebrada.md"
        offender.write_text(
            "# Teste\n\n"
            "Veja [atributo](referencia/glossario.md#ancora-que-nao-existe) para mais detalhes.\n",
            encoding="utf-8",
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertEqual(1, result.returncode)
            self.assertIn("ancora inexistente", result.stdout)
        finally:
            offender.unlink()

    def test_validator_allows_existing_anchor(self):
        allowed = ROOT / "docs" / "_teste_ancora_ok.md"
        allowed.write_text(
            "# Teste\n\n"
            "Veja [atributo](referencia/glossario.md#atributo-de-qualidade) para mais detalhes.\n",
            encoding="utf-8",
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertNotIn("_teste_ancora_ok", result.stdout)
            self.assertNotIn("ancora inexistente", result.stdout)
        finally:
            allowed.unlink()

    def test_validator_catches_missing_module_index(self):
        index_path = DOCS / "modulo-6-lacunas-e-governanca" / "index.md"
        backup_path = index_path.with_name("index.md.bak")
        index_path.rename(backup_path)
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertEqual(1, result.returncode)
            self.assertIn(
                "docs/modulo-6-lacunas-e-governanca/index.md ausente", result.stdout
            )
        finally:
            backup_path.rename(index_path)

    def test_validator_catches_exercise_heading_without_number(self):
        offender = DOCS / "modulo-1-fundamentos" / "bloco-9-teste-sem-numero.md"
        offender.write_text(
            "# Bloco teste\n\n"
            "## Antes de começar\n\nTexto.\n\n"
            "## Conceito\n\nTexto.\n\n"
            "## Uso pelo arquiteto\n\nTexto.\n\n"
            "## Exercício\n\nTexto.\n\n"
            "## Fontes\n\nTexto.\n",
            encoding="utf-8",
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertEqual(1, result.returncode)
            self.assertIn("falta a secao Exercício", result.stdout)
        finally:
            offender.unlink()

    def test_validator_allows_exercise_heading_with_number(self):
        allowed = DOCS / "modulo-1-fundamentos" / "bloco-9-teste-com-numero.md"
        allowed.write_text(
            "# Bloco teste\n\n"
            "## Antes de começar\n\nTexto.\n\n"
            "## Conceito\n\nTexto.\n\n"
            "## Uso pelo arquiteto\n\nTexto.\n\n"
            "## Exercício 7\n\nTexto.\n\n"
            "## Fontes\n\nTexto.\n",
            encoding="utf-8",
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertNotIn("bloco-9-teste-com-numero", result.stdout)
        finally:
            allowed.unlink()

    def test_validator_catches_forbidden_word_prosa(self):
        offender = ROOT / "docs" / "_teste_palavra_prosa.md"
        offender.write_text(
            "# Teste\n\nResponda em prosa, sem usar bullets.\n", encoding="utf-8"
        )
        try:
            result = subprocess.run(
                ["python3", "scripts/validate_content.py"],
                cwd=ROOT, text=True, capture_output=True,
            )
            self.assertEqual(1, result.returncode)
            self.assertIn("palavra prosa proibida", result.stdout)
        finally:
            offender.unlink()


if __name__ == "__main__":
    unittest.main()
