"""Gerador do caderno: leitura da fonte, template, mapa e gabaritos cumulativos."""

import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SEC_RESUMO = """---
secao: 0
titulo: A solução em uma página
modo: substitui
---
<!--orientacao-->
Orientação do resumo.
<!--/orientacao-->

<!--ex n=4 titulo="Resumo da Aula 1"-->
<!--gabarito-->
Resumo versão quatro.
<!--/gabarito-->
<!--/ex-->

<!--ex n=8 titulo="Resumo da Aula 2"-->
<!--gabarito-->
Resumo versão oito.
<!--/gabarito-->
<!--/ex-->
"""

SEC_REQ = """---
secao: 3
titulo: Requisitos
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| O que vai | Catálogo de requisitos |
<!--/orientacao-->

<!--ex n=5 titulo="Direcionadores"-->
<!--campos-->
- Direcionadores classificados
<!--/campos-->
<!--gabarito-->
Texto do gabarito cinco.
<!--/gabarito-->
<!--/ex-->

<!--ex n=6 titulo="Catálogo"-->
<!--campos-->
- Requisitos classificados
<!--/campos-->
<!--gabarito-->
Texto do gabarito seis.
<!--/gabarito-->
<!--/ex-->

<!--ex n=7 titulo="Cenários"-->
<!--campos-->
- Cenários com seis elementos
<!--/campos-->
<!--/ex-->
"""

SEC_ROTEIRO = """---
secao: 9
titulo: Roteiro e governança
modo: acumula
---
<!--orientacao-->
Orientação do roteiro.
<!--/orientacao-->
"""


def carregar_gerador():
    spec = importlib.util.spec_from_file_location(
        "gerar_caderno", ROOT / "scripts" / "gerar_caderno.py"
    )
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


class GeradorTest(unittest.TestCase):
    def setUp(self):
        self.ger = carregar_gerador()
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.fonte = Path(self.tmp.name) / "fonte"
        self.docs = Path(self.tmp.name) / "docs"
        self.fonte.mkdir()
        self.docs.mkdir()
        (self.fonte / "00-resumo.md").write_text(SEC_RESUMO, encoding="utf-8")
        (self.fonte / "03-requisitos.md").write_text(SEC_REQ, encoding="utf-8")
        (self.fonte / "09-roteiro.md").write_text(SEC_ROTEIRO, encoding="utf-8")
        self.secoes = self.ger.carregar(self.fonte)

    def test_carregar_le_as_secoes_em_ordem(self):
        self.assertEqual([0, 3, 9], [s.numero for s in self.secoes])
        self.assertEqual("substitui", self.secoes[0].modo)
        self.assertEqual(3, len(self.secoes[1].fragmentos))

    def test_template_traz_orientacao_e_campos_sem_gabarito(self):
        texto = self.ger.render_template(self.secoes)
        self.assertIn("## A solução em uma página", texto)
        self.assertIn("## 3. Requisitos", texto)
        self.assertIn("| O que vai | Catálogo de requisitos |", texto)
        self.assertIn("### 3.1 Direcionadores", texto)
        self.assertIn("- Direcionadores classificados", texto)
        self.assertNotIn("Texto do gabarito cinco", texto)
        self.assertIn("{{folha:3}}", texto)
        self.assertIn("{{trilha:todas}}", texto)

    def test_gabarito_cinco_nao_traz_o_seis(self):
        texto = self.ger.render_gabarito(self.secoes, 5, self.docs)
        self.assertIn("Texto do gabarito cinco.", texto)
        self.assertNotIn("Texto do gabarito seis.", texto)

    def test_gabarito_seis_contem_o_cinco_e_destaca_so_o_seis(self):
        texto = self.ger.render_gabarito(self.secoes, 6, self.docs)
        self.assertIn("Texto do gabarito cinco.", texto)
        self.assertIn("{{novo}}\n\nTexto do gabarito seis.", texto)
        self.assertNotIn("{{novo}}\n\nTexto do gabarito cinco", texto)
        self.assertIn("{{progresso:6}}", texto)

    def test_cumulativo_a_versao_n_contem_a_anterior_nas_secoes_que_acumulam(self):
        anterior = self.ger.render_gabarito(self.secoes, 5, self.docs)
        seguinte = self.ger.render_gabarito(self.secoes, 6, self.docs)
        self.assertIn("### 3.1 Direcionadores", seguinte)
        self.assertIn("Texto do gabarito cinco.", seguinte)
        self.assertLess(len(anterior), len(seguinte))

    def test_secao_que_substitui_mostra_so_a_versao_mais_recente(self):
        no_seis = self.ger.render_gabarito(self.secoes, 6, self.docs)
        no_oito = self.ger.render_gabarito(self.secoes, 8, self.docs)
        self.assertIn("Resumo versão quatro.", no_seis)
        self.assertNotIn("Resumo versão oito.", no_seis)
        self.assertIn("Resumo versão oito.", no_oito)
        self.assertNotIn("Resumo versão quatro.", no_oito)

    def test_secoes_sem_trecho_visivel_ficam_em_pendentes(self):
        texto = self.ger.render_gabarito(self.secoes, 5, self.docs)
        self.assertIn("Seções que os exercícios seguintes preenchem: 9. Roteiro e governança", texto)

    def test_exercicio_sem_gabarito_aparece_como_a_publicar(self):
        saidas = self.ger.saidas(self.secoes, self.docs)
        self.assertNotIn(self.docs / "gabaritos" / "gabarito-exercicio-07.md", saidas)
        mapa = saidas[self.docs / "caderno" / "mapa.md"]
        self.assertRegex(mapa, r"Exercício 7 \| A publicar")

    def test_saidas_gera_um_gabarito_por_exercicio_com_trecho(self):
        saidas = self.ger.saidas(self.secoes, self.docs)
        gerados = sorted(p.name for p in saidas if p.name.startswith("gabarito-exercicio-"))
        self.assertEqual(
            ["gabarito-exercicio-04.md", "gabarito-exercicio-05.md",
             "gabarito-exercicio-06.md", "gabarito-exercicio-08.md"],
            gerados,
        )

    def test_divergencias_detecta_edicao_manual_e_sobra(self):
        saidas = self.ger.saidas(self.secoes, self.docs)
        for caminho, texto in saidas.items():
            caminho.parent.mkdir(parents=True, exist_ok=True)
            caminho.write_text(texto, encoding="utf-8")
        self.assertEqual([], self.ger.divergencias(saidas, self.docs))
        editado = self.docs / "caderno" / "template.md"
        editado.write_text(editado.read_text(encoding="utf-8") + "\nedição manual\n", encoding="utf-8")
        (self.docs / "gabaritos" / "gabarito-exercicio-99.md").write_text("sobra", encoding="utf-8")
        problemas = self.ger.divergencias(saidas, self.docs)
        self.assertTrue(any("template.md" in p for p in problemas))
        self.assertTrue(any("gabarito-exercicio-99.md" in p for p in problemas))

    def test_carregar_rejeita_marcador_sem_fechamento(self):
        (self.fonte / "03-requisitos.md").write_text(
            SEC_REQ.replace("<!--/ex-->", "", 1), encoding="utf-8"
        )
        with self.assertRaisesRegex(ValueError, "03-requisitos.md.*sem fechamento"):
            self.ger.carregar(self.fonte)

    def test_carregar_exige_orientacao(self):
        (self.fonte / "09-roteiro.md").write_text(
            "---\nsecao: 9\ntitulo: Roteiro e governança\n---\nsem marcador\n", encoding="utf-8"
        )
        with self.assertRaisesRegex(ValueError, "09-roteiro.md.*orientação"):
            self.ger.carregar(self.fonte)

    def test_carregar_rejeita_titulo_no_gabarito(self):
        (self.fonte / "03-requisitos.md").write_text(
            SEC_REQ.replace("Texto do gabarito cinco.", "### Título solto\n\nTexto."), encoding="utf-8"
        )
        with self.assertRaisesRegex(ValueError, "título de nível 1 a 3"):
            self.ger.carregar(self.fonte)

    def test_carregar_rejeita_numero_repetido(self):
        (self.fonte / "00-resumo.md").write_text(
            SEC_RESUMO.replace("n=8", "n=4"), encoding="utf-8"
        )
        with self.assertRaisesRegex(ValueError, "exercício 4 repetido"):
            self.ger.carregar(self.fonte)

    def test_carregar_rejeita_fragmento_mal_formado(self):
        (self.fonte / "03-requisitos.md").write_text(
            SEC_REQ.replace('titulo="Direcionadores"', "titulo='Direcionadores'"), encoding="utf-8"
        )
        with self.assertRaisesRegex(ValueError, "03-requisitos.md.*mal formado"):
            self.ger.carregar(self.fonte)

    def test_carregar_rejeita_gabarito_sem_fechamento(self):
        (self.fonte / "03-requisitos.md").write_text(
            SEC_REQ.replace("<!--/gabarito-->", "", 1), encoding="utf-8"
        )
        with self.assertRaisesRegex(ValueError, "03-requisitos.md.*gabarito.*sem fechamento"):
            self.ger.carregar(self.fonte)

    def test_carregar_aceita_espaco_depois_do_marcador(self):
        (self.fonte / "03-requisitos.md").write_text(
            SEC_REQ.replace("<!--gabarito-->\n", "<!--gabarito--> \n", 1), encoding="utf-8"
        )
        secoes = self.ger.carregar(self.fonte)
        self.assertEqual("Texto do gabarito cinco.", secoes[1].fragmentos[0].gabarito)

    def test_carregar_aceita_comentario_dentro_de_cerca_de_codigo(self):
        corpo = "Antes.\n\n```bash\n# comentário do shell\nls\n```\n\n~~~\n# outro\n~~~"
        (self.fonte / "03-requisitos.md").write_text(
            SEC_REQ.replace("Texto do gabarito cinco.", corpo), encoding="utf-8"
        )
        secoes = self.ger.carregar(self.fonte)
        self.assertIn("# comentário do shell", secoes[1].fragmentos[0].gabarito)
