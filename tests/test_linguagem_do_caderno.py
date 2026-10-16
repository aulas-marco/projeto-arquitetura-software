"""Linguagem do caderno: sem códigos genéricos, sem fórmulas vazias, sem depender de memória."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Códigos com "n" no lugar do número, como D1 a Dn, que só quem já conhece o caderno decifra.
PLACEHOLDER = re.compile(r"\b(?:ADR|CQ|DD|DL|FA|PR|RD|RT|CP|[A-Z])n{1,3}\b")

# Fórmulas que parecem informar e não informam, apontadas na revisão de 16/10/2026.
FORMULAS_VAZIAS = (
    "uma linha pelo",
    "e o motivo",
    "do requisito em análise",
    "critério de seção completa",
    "artefatos e códigos",
    "preenchida em",
    "de que cada uma depende",
    "campos a preencher",
    "o que a decisão muda",
    "o que a tarefa muda",
    "seções que os exercícios seguintes preenchem",
)


def arquivos():
    paginas = []
    paginas += sorted((ROOT / "caderno-fonte").glob("*.md"))
    paginas += sorted((ROOT / "docs" / "caderno").glob("*.md"))
    paginas += sorted((ROOT / "docs" / "gabaritos").glob("*.md"))
    paginas += sorted((ROOT / "docs" / "modulo-1-fundamentos").glob("*.md"))
    paginas.append(ROOT / "docs" / "index.md")
    paginas.append(ROOT / "scripts" / "gerar_caderno.py")
    return paginas


class LinguagemDoCadernoTest(unittest.TestCase):
    def test_nenhum_codigo_generico_com_n_no_lugar_do_numero(self):
        for caminho in arquivos():
            texto = caminho.read_text(encoding="utf-8")
            achados = PLACEHOLDER.findall(texto)
            with self.subTest(arquivo=str(caminho.relative_to(ROOT))):
                self.assertEqual([], achados)

    def test_nenhuma_formula_vazia(self):
        for caminho in arquivos():
            texto = caminho.read_text(encoding="utf-8").casefold()
            with self.subTest(arquivo=str(caminho.relative_to(ROOT))):
                for formula in FORMULAS_VAZIAS:
                    self.assertNotIn(formula, texto, formula)

    def test_celula_de_orientacao_e_frase_com_verbo_ou_pergunta(self):
        """A linha 'O que você escreve' de cada seção explica o que se escreve, com ao menos 12 palavras."""
        for caminho in sorted((ROOT / "caderno-fonte").glob("*.md")):
            texto = caminho.read_text(encoding="utf-8")
            linha = next(
                (l for l in texto.splitlines() if l.startswith("| O que você escreve |")), None
            )
            with self.subTest(arquivo=caminho.name):
                self.assertIsNotNone(linha)
                conteudo = linha.split("|")[2]
                self.assertGreaterEqual(len(conteudo.split()), 12)
