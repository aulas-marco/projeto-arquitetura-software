"""Os quatro blocos do módulo 1 preenchem a seção 1 do caderno arquitetural."""

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "docs" / "modulo-1-fundamentos"

BLOCOS = {
    "bloco-1-arquitetura-de-solucoes-e-de-software.md": 1,
    "bloco-2-a-solucao-como-sistema.md": 2,
    "bloco-3-papel-do-arquiteto-de-solucao.md": 3,
    "bloco-4-processo-de-definicao-da-arquitetura.md": 4,
}


def texto(nome):
    return (MODULE / nome).read_text(encoding="utf-8")


def itens(pagina):
    """Devolve (titulo, corpo) de cada item do exercício."""
    inicio = re.search(r"(?m)^## Exerc[ií]cio \d+\s*$", pagina).end()
    fim = pagina.index("\n## Fontes")
    partes = re.split(r"(?m)^### (Item \d+: .+)$", pagina[inicio:fim])
    return list(zip(partes[1::2], partes[2::2]))


class ModuloUmCadernoTest(unittest.TestCase):
    def test_secao_no_caderno_fica_entre_uso_e_exercicio(self):
        for nome, n in BLOCOS.items():
            pagina = texto(nome)
            with self.subTest(bloco=nome):
                uso = pagina.index("## Uso pelo arquiteto")
                caderno = pagina.index("## No caderno arquitetural")
                exercicio = re.search(rf"(?m)^## Exerc[ií]cio {n}\s*$", pagina).start()
                self.assertLess(uso, caderno)
                self.assertLess(caderno, exercicio)

    def test_ficha_da_secao_1_aberta_e_fechada_com_links_nos_dois_sentidos(self):
        for nome, n in BLOCOS.items():
            pagina = texto(nome)
            with self.subTest(bloco=nome):
                self.assertIn("{{ficha:1}}", pagina)
                self.assertIn("{{/ficha}}", pagina)
                self.assertIn(f"../gabaritos/gabarito-exercicio-{n:02d}.md", pagina)
                self.assertIn("../caderno/template.md#1-contexto", pagina)
                self.assertGreaterEqual(pagina.count("{ .caderno-botao }"), 2)

    def test_cada_item_diz_qual_campo_do_caderno_a_resposta_preenche(self):
        for nome in BLOCOS:
            for titulo, corpo in itens(texto(nome)):
                with self.subTest(bloco=nome, item=titulo):
                    self.assertRegex(corpo, r"(A resposta preenche|As (duas )?respostas preenchem)")
                    self.assertIn("caderno", corpo)

    def test_componentes_do_exercicio_2_usam_codigo_cp(self):
        pagina = texto("bloco-2-a-solucao-como-sistema.md")
        exercicio = pagina[pagina.index("## Exercício 2"):]
        for numero in range(1, 11):
            with self.subTest(codigo=f"CP{numero}"):
                self.assertRegex(exercicio, rf"\| CP{numero} \|")
        self.assertNotRegex(exercicio, r"\| C(10|[1-9]) \|")

    def test_item_3_do_exercicio_3_vira_campo_da_tabela_de_papeis(self):
        pagina = texto("bloco-3-papel-do-arquiteto-de-solucao.md")
        item = [corpo for titulo, corpo in itens(pagina) if titulo.startswith("Item 3")][0]
        self.assertIn("campo Benefício da tarefa T10", item)

    def test_exercicio_4_associa_artefato_a_secao_e_registra_a_pendencia(self):
        pagina = texto("bloco-4-processo-de-definicao-da-arquitetura.md")
        item1 = [corpo for titulo, corpo in itens(pagina) if titulo.startswith("Item 1")][0]
        item2 = [corpo for titulo, corpo in itens(pagina) if titulo.startswith("Item 2")][0]
        self.assertIn("seção do caderno", item1)
        self.assertIn("seção 10", item2)

    def test_bloco_4_apresenta_o_caderno_no_conceito(self):
        pagina = texto("bloco-4-processo-de-definicao-da-arquitetura.md")
        conceito = pagina.index("### O caderno arquitetural")
        self.assertLess(conceito, pagina.index("## Uso pelo arquiteto"))
        self.assertGreater(conceito, pagina.index("### Adaptação do processo"))
        self.assertIn("{{trilha:todas}}", pagina)
        self.assertIn("../referencia/glossario.md#caderno-arquitetural", pagina)

    def test_indice_e_sintese_apontam_para_o_caderno_e_para_os_gabaritos(self):
        indice = texto("index.md")
        sintese = texto("sintese.md")
        self.assertIn("../caderno/template.md", indice)
        self.assertIn("{{trilha:1}}", indice)
        self.assertNotIn("sem gabarito público", sintese)
        self.assertIn("../gabaritos/index.md", sintese)
