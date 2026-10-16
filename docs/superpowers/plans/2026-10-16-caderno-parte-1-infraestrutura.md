# Caderno arquitetural, parte 1: auditoria e infraestrutura Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Entregar a matriz de auditoria do conteúdo e a infraestrutura do caderno arquitetural (fonte única, gerador de template, mapa e gabaritos, navegação, validador e testes), sem alterar o texto dos módulos 1 a 5.

**Architecture:** O texto do caderno vive em `caderno-fonte/`, fora de `docs/`, um arquivo por seção, com marcadores HTML que separam orientação, campos e gabarito de cada exercício. O script `scripts/gerar_caderno.py` lê a fonte e grava `docs/caderno/template.md`, `docs/caderno/mapa.md`, `docs/gabaritos/index.md` e uma página `docs/gabaritos/gabarito-exercicio-NN.md` por exercício que tenha trecho de gabarito. O modo `--check` compara essa saída com o disco e termina com código 1 quando alguma página diverge da fonte.

**Tech Stack:** Python 3 (biblioteca padrão, `unittest`), MkDocs Material 9.7.6, validador `scripts/validate_content.py`.

**Spec:** `docs/superpowers/specs/2026-10-16-caderno-arquitetural-design.md`. A tarefa 12 registra três emendas à spec, descobertas durante o planejamento: a fonte fica em `caderno-fonte/`, na raiz do repositório, porque o validador resolve links relativos a partir da pasta do arquivo e o MkDocs publicaria qualquer fonte colocada em `docs/`. O exercício 4 preenche a seção 1. As seções 0 e 10 têm modo de substituição, que mostra só a versão mais recente com exercício menor ou igual ao do gabarito.

## Global Constraints

- A suíte atual passa com 171 testes (`python3 -m unittest discover -s tests`) e o validador retorna 0 violações (`python3 scripts/validate_content.py`). Os dois permanecem verdes ao fim de cada tarefa.
- Regras do validador, que valem também para as páginas geradas: sem ponto-e-vírgula em prosa, no máximo um travessão por parágrafo (tabelas e `## Fontes` são isentas), sem a palavra "prosa", sem os marcadores em caixa alta TODO, TBD, PLACEHOLDER e PREENCHER, títulos que não abrem com "Por que" nem trazem subtítulo após travessão, links relativos e âncoras existentes.
- Texto em português brasileiro com acentuação completa, voz impessoal, sem neologismos e sem "Lovatt" ou "livro-texto" fora das Fontes (`tests/test_modulo_4_contract.py`, `SelfContainedTextTest`).
- Nenhum parágrafo fecha com frase de efeito, e o último período de cada parágrafo carrega dado.
- Mensagens de commit em ASCII, no padrão `tipo(escopo): descricao`, terminadas por `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`.
- A pasta `docs/superpowers/` não é publicada (`exclude_docs` em `mkdocs.yml`) nem validada.
- Remoção de página ou de conteúdo só ocorre depois da aprovação do professor sobre a matriz (tarefa 2). As tarefas 3 a 10 não removem nada.

## Review Focus

Entradas e condições que a spec implica e que nenhum teste de tarefa exercitaria por padrão. Cada linha tem o teste na tarefa dona do código.

1. Marcador `<!--ex` sem fechamento, ou fonte sem orientação: o gerador deve falhar com mensagem que cita o arquivo, sem gerar página vazia (tarefa 4, `test_carregar_rejeita_marcador_sem_fechamento` e `test_carregar_exige_orientacao`).
2. Gabarito com título de nível 1 a 3 no corpo: quebraria a numeração e o sumário da página, e o gerador deve rejeitá-lo (tarefa 4, `test_carregar_rejeita_titulo_no_gabarito`).
3. Edição manual de página gerada: `--check` deve falhar e apontar o arquivo, inclusive quando sobra um gabarito de exercício sem fonte (tarefa 4, `test_divergencias_detecta_edicao_manual_e_sobra`).
4. Exercício sem trecho de gabarito: nenhuma página de gabarito é criada, e o mapa mostra "A publicar", sem link quebrado (tarefa 4, `test_exercicio_sem_gabarito_aparece_como_a_publicar`).
5. Seção de substituição com duas versões do mesmo exercício, ou com versão fora dos exercícios 4, 8, 12, 16, 20 e 24: deve ser rejeitada (tarefa 4, `test_carregar_rejeita_numero_repetido`, e tarefa 9, `test_fragmentos_respeitam_o_plano`).

---

### Task 1: Inventário da auditoria

**Files:**
- Create: `scripts/inventario_auditoria.py`
- Create: `tests/test_inventario_auditoria.py`
- Create: `docs/superpowers/auditoria/2026-10-16-matriz-caderno.md` (gerado)

**Interfaces:**
- Produces: `inventariar(docs: Path) -> list[tuple[str, str, str]]`, com tuplas `(tipo, local, rotulo)`, e `renderizar(linhas) -> str`. Os tipos são `página`, `exercício`, `item`, `termo` e `síntese`.

- [ ] **Step 1: Escrever o teste**

```python
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
        self.assertEqual(20, len(exercicios))
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
```

- [ ] **Step 2: Rodar o teste e conferir a falha**

Run: `python3 -m unittest tests.test_inventario_auditoria -v`
Expected: FAIL com `FileNotFoundError` ou `ModuleNotFoundError`, porque o script não existe.

- [ ] **Step 3: Implementar**

```python
"""Gera o inventário de auditoria do conteúdo do curso para a matriz do caderno.

Uso: python3 scripts/inventario_auditoria.py [--escrever]
Sem --escrever, imprime a tabela. Com --escrever, grava a matriz em
docs/superpowers/auditoria/ e se recusa a sobrescrever matriz já preenchida.
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
MATRIZ = DOCS / "superpowers" / "auditoria" / "2026-10-16-matriz-caderno.md"
IGNORADAS = ("superpowers", "caderno", "gabaritos")


def _slug(titulo: str) -> str:
    spec = importlib.util.spec_from_file_location(
        "validate_content", ROOT / "scripts" / "validate_content.py"
    )
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo._slugify_heading(titulo)


def _primeiro_titulo(texto: str) -> str:
    achado = re.search(r"^# (.+)$", texto, re.MULTILINE)
    return achado.group(1) if achado else ""


def _secao(texto: str, titulo_regex: str) -> str:
    achado = re.search(rf"^## {titulo_regex}.*$", texto, re.MULTILINE)
    if achado is None:
        return ""
    resto = texto[achado.end():]
    proximo = re.search(r"^## ", resto, re.MULTILINE)
    return resto[: proximo.start()] if proximo else resto


def inventariar(docs: Path = DOCS) -> list[tuple[str, str, str]]:
    linhas: list[tuple[str, str, str]] = []
    for caminho in sorted(docs.rglob("*.md")):
        relativo = caminho.relative_to(docs)
        if relativo.parts[0] in IGNORADAS:
            continue
        texto = caminho.read_text(encoding="utf-8")
        linhas.append(("página", str(relativo), _primeiro_titulo(texto)))
        if caminho.name == "glossario.md":
            for achado in re.finditer(r"^## (.+)$", texto, re.MULTILINE):
                linhas.append(("termo", f"{relativo}#{_slug(achado.group(1))}", achado.group(1)))
        if caminho.name == "sintese.md":
            bloco = _secao(texto, "Checklist")
            for item in re.finditer(r"^- (.+)$", bloco, re.MULTILINE):
                resumo = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", item.group(1))
                linhas.append(("síntese", f"{relativo}#checklist", resumo[:90]))
        exercicio = re.search(r"^## (Exercício \d+)\s*$", texto, re.MULTILINE)
        if exercicio:
            ancora = _slug(exercicio.group(1))
            linhas.append(("exercício", f"{relativo}#{ancora}", exercicio.group(1)))
            for item in re.finditer(r"^### (Item \d+: .+)$", _secao(texto, "Exercício \\d+"), re.MULTILINE):
                linhas.append(("item", f"{relativo}#{ancora}", item.group(1)))
    return linhas


def renderizar(linhas: list[tuple[str, str, str]]) -> str:
    cabecalho = [
        "| Tipo | Local | Rótulo | Seção do caderno | Decisão | Justificativa |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    corpo = [f"| {tipo} | {local} | {rotulo.replace('|', '/')} |  |  |  |" for tipo, local, rotulo in linhas]
    return "\n".join(cabecalho + corpo) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Inventário de auditoria do caderno")
    parser.add_argument("--escrever", action="store_true")
    args = parser.parse_args()
    tabela = renderizar(inventariar())
    if not args.escrever:
        print(tabela)
        return 0
    if MATRIZ.exists():
        print(f"{MATRIZ.relative_to(ROOT)} já existe e não será sobrescrita", file=sys.stderr)
        return 1
    MATRIZ.parent.mkdir(parents=True, exist_ok=True)
    cabecalho = (
        "# Matriz de auditoria do conteúdo à luz do caderno arquitetural\n\n"
        "**Data:** 16/10/2026\n\n**Estado:** inventário gerado, decisões pendentes\n\n"
        "Decisões possíveis: mantém, altera, move, remove. Seção do caderno é o número da "
        "seção em `caderno-fonte/`, ou `apoio` para conceito sem seção própria que sustenta "
        "conceito que a tem.\n\n"
    )
    MATRIZ.write_text(cabecalho + tabela, encoding="utf-8")
    print(f"gravado {MATRIZ.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Rodar o teste e conferir a aprovação**

Run: `python3 -m unittest tests.test_inventario_auditoria -v`
Expected: PASS nos cinco testes. Se `test_item_de_exercicio_e_item_de_sintese_tem_local_com_ancora` falhar por contagem, rodar `python3 scripts/inventario_auditoria.py | grep -c "| item |"` e `| síntese |`, conferir se os exercícios usam `### Item N:` e se as sínteses usam `## Checklist do que precisa permanecer`, e corrigir o limite do teste para o valor real menos 10% (o limite de 40 é uma estimativa).

- [ ] **Step 5: Gerar a matriz e commitar**

```bash
python3 scripts/inventario_auditoria.py --escrever
python3 -m unittest discover -s tests 2>&1 | tail -3
git add scripts/inventario_auditoria.py tests/test_inventario_auditoria.py docs/superpowers/auditoria/2026-10-16-matriz-caderno.md
git commit -m "feat(caderno): inventario de auditoria do conteudo

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
```

---

### Task 2: Preenchimento da matriz e portão de aprovação

**Files:**
- Modify: `docs/superpowers/auditoria/2026-10-16-matriz-caderno.md`

**Interfaces:**
- Consumes: a tabela da tarefa 1 e os rótulos de seção da tarefa 3 (`TITULOS_SECAO`). A tarefa 3 pode rodar em paralelo, e o preenchimento usa os números de seção da spec, seção 4.1.
- Produces: matriz com a coluna Decisão preenchida em todas as linhas e uma seção final `## Achados`, que a tarefa 11 lê.

Esta tarefa é de julgamento e não tem teste de unidade. O critério de término é verificável pelo comando do passo 5.

- [ ] **Step 1: Ler as fontes de referência**

Ler `docs/superpowers/specs/2026-10-16-caderno-arquitetural-design.md` (seções 4, 5 e 7) e o caderno pocket em `~/pka/projects/aulas/iec-ead-2026-projeto-arquitetura-solucao/4-caderno/pocket/caderno-pocket-acme.md`. A tabela da spec, seção 4.1, dá a seção do caderno de cada exercício.

- [ ] **Step 2: Preencher as linhas por módulo**

O trabalho se divide por módulo, das aulas 1 a 5, e pelas páginas `caso-acme/`, `referencia/` e `cronograma.md`, e cada divisão pode ser delegada a um subagente com este roteiro. Cada linha recebe a `Seção do caderno`, a `Decisão` e uma `Justificativa` de uma linha, segundo os critérios da tabela abaixo.

| Decisão | Critério |
| --- | --- |
| mantém | O conceito, o exercício ou o termo alimenta uma seção do caderno sem mudança de conteúdo |
| altera | Há seção do caderno, mas o texto tem código, dado, ordem ou formulação diferente do caderno, ou o exercício precisa pedir o preenchimento de um campo |
| move | O conteúdo pertence a outra aula ou a outra seção |
| remove | Não tem seção do caderno e não sustenta conceito que tenha |

Linhas de exemplo, que valem como padrão de redação:

```
| exercício | modulo-2-requisitos-e-partes-interessadas/bloco-2-qualidade-e-tipos-de-requisito.md#exercicio-6 | Exercício 6 | 3 | altera | Passa a pedir a coluna Tipo e a medida do catálogo de requisitos da seção 3 |
| termo | referencia/glossario.md#stride | STRIDE | 8 | mantém | Subseção de segurança da seção 8 usa as seis categorias |
| item | modulo-1-fundamentos/bloco-3-papel-do-arquiteto-de-solucao.md#exercicio-3 | Item 1: Tarefas por nível | 1 | altera | Reformular como preenchimento da subseção de papéis, a pedido da spec, seção 5.2 |
```

- [ ] **Step 3: Rodar as cinco verificações obrigatórias da spec, seção 7**

Registrar o resultado de cada uma, com `arquivo:linha`, na seção `## Achados` ao fim da matriz.

1. Conceito sem seção e seção sem bloco. Montar a lista dos termos com seção `apoio` ou vazia e a lista das seções 0 a 10 sem nenhum bloco que as ensine.
2. Códigos e números iguais entre o site e o caderno completo:

```bash
EAD=~/pka/projects/aulas/iec-ead-2026-projeto-arquitetura-solucao/4-caderno/caderno-arquitetural-acme.md
for n in "38.400" "214.000" "15,83" "5.800" "2.300" "34 dias" "30/09/2027" "31/12/2028" "R\$ 6,2" "R\$ 11,0"; do
  site=$(grep -rF -- "$n" docs --include='*.md' --exclude-dir=superpowers | wc -l | tr -d ' ')
  ead=$(grep -cF -- "$n" "$EAD")
  echo "$n site=$site caderno=$ead"
done
grep -nE "^\| R[0-9]+ " docs/caso-acme/index.md | cut -c1-90
grep -nE "^\| R[0-9]+ " "$EAD" | cut -c1-90
```

Qualquer número presente num lado e ausente no outro, e qualquer requisito com texto diferente, entra nos achados.
3. Ordem das seções contra a ordem das aulas, com a diferença da análise de lacunas (capítulo 8 do caderno completo, Aula 6 do curso) registrada.
4. Capítulos do caderno completo sem aula correspondente, como IA no processo de arquitetura (capítulo 19) e interoperabilidade: listá-los e marcá-los como fora do template.
5. Páginas que a seção 5 da spec manda alterar: confirmar que `caso-acme/artefatos.md` está coberta pelo mapa, e classificar cada síntese.

- [ ] **Step 4: Atualizar o estado da matriz**

Trocar a linha `**Estado:** inventário gerado, decisões pendentes` por `**Estado:** preenchida, aguarda aprovação do professor`.

- [ ] **Step 5: Verificar completude**

Run:
```bash
grep -E "^\| (página|exercício|item|termo|síntese) " docs/superpowers/auditoria/2026-10-16-matriz-caderno.md \
  | awk -F'|' '{ if ($6 !~ /(mantém|altera|move|remove)/) print "sem decisão:", $3 }' | head
```
Expected: nenhuma linha impressa. Cada linha com decisão `altera`, `move` ou `remove` precisa de justificativa não vazia:
```bash
grep -E "^\| .*\| (altera|move|remove) *\|  *\|$" docs/superpowers/auditoria/2026-10-16-matriz-caderno.md | head
```
Expected: nenhuma linha impressa.

- [ ] **Step 6: Commitar e parar para aprovação**

```bash
git add docs/superpowers/auditoria/2026-10-16-matriz-caderno.md
git commit -m "docs(caderno): matriz de auditoria preenchida, aguardando aprovacao

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
```

Apresentar ao professor a contagem de linhas por decisão (`awk -F'|' '{print $6}' ... | sort | uniq -c`) e os achados, e **parar** até que ele responda. As tarefas 3 a 10 não dependem dessa aprovação e podem seguir em paralelo, mas a tarefa 11 só começa depois da aprovação, linha a linha.

---

### Task 3: Registro de dados do caderno

**Files:**
- Create: `scripts/caderno_registro.py`
- Create: `tests/test_caderno_registro.py`

**Interfaces:**
- Produces: `TITULOS_SECAO: dict[int, str]`, `SUBSTITUI: dict[int, tuple[int, ...]]`, `PLANO: dict[int, tuple[int, ...]]`, `EXERCICIOS: dict[int, tuple[int, str, str]]` com `(aula, arquivo relativo a docs/, título do bloco)`, e `CODIGOS: tuple[str, ...]`.

- [ ] **Step 1: Escrever o teste**

```python
"""O registro fixa seções, exercícios e códigos do caderno."""

import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


def carregar():
    spec = importlib.util.spec_from_file_location(
        "caderno_registro", ROOT / "scripts" / "caderno_registro.py"
    )
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


class RegistroTest(unittest.TestCase):
    def setUp(self):
        self.reg = carregar()

    def test_onze_secoes_numeradas_de_zero_a_dez(self):
        self.assertEqual(list(range(11)), sorted(self.reg.TITULOS_SECAO))

    def test_vinte_e_quatro_exercicios_com_plano(self):
        self.assertEqual(list(range(1, 25)), sorted(self.reg.EXERCICIOS))
        self.assertEqual(sorted(self.reg.EXERCICIOS), sorted(self.reg.PLANO))

    def test_plano_so_usa_secoes_que_acumulam(self):
        for n, secoes in self.reg.PLANO.items():
            for secao in secoes:
                with self.subTest(exercicio=n, secao=secao):
                    self.assertIn(secao, self.reg.TITULOS_SECAO)
                    self.assertNotIn(secao, self.reg.SUBSTITUI)

    def test_secoes_que_substituem_so_aceitam_o_fim_de_cada_aula(self):
        for secao, exercicios in self.reg.SUBSTITUI.items():
            self.assertEqual((4, 8, 12, 16, 20, 24), exercicios, secao)

    def test_os_vinte_primeiros_exercicios_apontam_para_blocos_existentes(self):
        for n in range(1, 21):
            _, arquivo, _ = self.reg.EXERCICIOS[n]
            with self.subTest(exercicio=n):
                texto = (DOCS / arquivo).read_text(encoding="utf-8")
                self.assertRegex(texto, rf"(?m)^## Exerc[ií]cio {n}\s*$")

    def test_codigos_de_artefato(self):
        self.assertEqual(
            ("D", "PR", "RT", "R", "RD", "CQ", "L", "P", "DD", "DL", "B", "I", "ADR", "C", "LG", "FA"),
            self.reg.CODIGOS,
        )
```

- [ ] **Step 2: Rodar e conferir a falha**

Run: `python3 -m unittest tests.test_caderno_registro -v`
Expected: FAIL, `scripts/caderno_registro.py` não existe.

- [ ] **Step 3: Implementar**

```python
"""Dados fixos do caderno arquitetural, compartilhados pelo gerador e pelos testes."""

TITULOS_SECAO = {
    0: "A solução em uma página",
    1: "Contexto",
    2: "Partes interessadas",
    3: "Requisitos",
    4: "Linha de base e lacunas",
    5: "Contexto do sistema (C4, nível 1)",
    6: "Princípios",
    7: "Decisões",
    8: "Tecnologia e plataforma",
    9: "Roteiro e governança",
    10: "O que ainda falta decidir",
}

# Seções que mostram só a versão mais recente, revista ao fim de cada aula.
SUBSTITUI = {
    0: (4, 8, 12, 16, 20, 24),
    10: (4, 8, 12, 16, 20, 24),
}

# Exercício -> seções do caderno que ele preenche, em ordem de importância.
PLANO = {
    1: (1,), 2: (1,), 3: (1,), 4: (1,),
    5: (3,), 6: (3,), 7: (3, 4), 8: (2,),
    9: (6,), 10: (7,), 11: (7,), 12: (7,),
    13: (7,), 14: (7,), 15: (5,), 16: (7,),
    17: (8,), 18: (8,), 19: (8,), 20: (8,),
    21: (4,), 22: (9,), 23: (9,), 24: (10,),
}

# Exercício -> (aula, página do bloco relativa a docs/, título do bloco).
# Os arquivos da Aula 6 ainda não existem, e o gerador só cria link para arquivo existente.
EXERCICIOS = {
    1: (1, "modulo-1-fundamentos/bloco-1-arquitetura-de-solucoes-e-de-software.md", "Arquitetura de soluções e arquitetura de software"),
    2: (1, "modulo-1-fundamentos/bloco-2-a-solucao-como-sistema.md", "A solução como sistema e seus componentes"),
    3: (1, "modulo-1-fundamentos/bloco-3-papel-do-arquiteto-de-solucao.md", "O papel do arquiteto de solução"),
    4: (1, "modulo-1-fundamentos/bloco-4-processo-de-definicao-da-arquitetura.md", "O processo de definição da arquitetura"),
    5: (2, "modulo-2-requisitos-e-partes-interessadas/bloco-1-direcionadores-de-mudanca.md", "Direcionadores de mudança"),
    6: (2, "modulo-2-requisitos-e-partes-interessadas/bloco-2-qualidade-e-tipos-de-requisito.md", "Qualidade e tipos de requisito"),
    7: (2, "modulo-2-requisitos-e-partes-interessadas/bloco-3-cenarios-linha-de-base-e-restricoes.md", "Cenários de qualidade, linha de base e restrições"),
    8: (2, "modulo-2-requisitos-e-partes-interessadas/bloco-4-partes-interessadas-e-pontos-de-vista.md", "Partes interessadas, pontos de vista e escopo"),
    9: (3, "modulo-3-design-e-padroes/bloco-1-principios-de-design.md", "Princípios de design da solução"),
    10: (3, "modulo-3-design-e-padroes/bloco-2-estilos-arquiteturais.md", "Estilos arquiteturais"),
    11: (3, "modulo-3-design-e-padroes/bloco-3-padroes-arquiteturais-e-de-design.md", "Padrões arquiteturais e de design"),
    12: (3, "modulo-3-design-e-padroes/bloco-4-registro-de-decisao-arquitetural.md", "Registro de decisão arquitetural"),
    13: (4, "modulo-4-dominios-da-solucao/bloco-1-arquitetura-de-negocio.md", "Arquitetura de negócio"),
    14: (4, "modulo-4-dominios-da-solucao/bloco-2-arquitetura-de-dados.md", "Arquitetura de dados"),
    15: (4, "modulo-4-dominios-da-solucao/bloco-3-arquitetura-de-aplicacoes-e-integracao.md", "Arquitetura de aplicações e integração"),
    16: (4, "modulo-4-dominios-da-solucao/bloco-4-arquitetura-de-infraestrutura.md", "Arquitetura de infraestrutura"),
    17: (5, "modulo-5-frameworks-e-tecnologias/bloco-1-definicao-tecnologica-e-trm.md", "Definição tecnológica e modelo técnico de referência"),
    18: (5, "modulo-5-frameworks-e-tecnologias/bloco-2-plataforma-arquitetural.md", "Plataforma arquitetural"),
    19: (5, "modulo-5-frameworks-e-tecnologias/bloco-3-seguranca-fim-a-fim.md", "Segurança fim a fim"),
    20: (5, "modulo-5-frameworks-e-tecnologias/bloco-4-adr-de-plataforma.md", "ADR de plataforma e lacunas"),
    21: (6, "modulo-6-lacunas-e-governanca/bloco-1-analise-de-lacunas.md", "Análise de lacunas"),
    22: (6, "modulo-6-lacunas-e-governanca/bloco-2-roteiro-de-entrega.md", "Roteiro de entrega"),
    23: (6, "modulo-6-lacunas-e-governanca/bloco-3-governanca.md", "Governança"),
    24: (6, "modulo-6-lacunas-e-governanca/bloco-4-inovacao-e-tendencias.md", "Inovação e tendências"),
}

CODIGOS = ("D", "PR", "RT", "R", "RD", "CQ", "L", "P", "DD", "DL", "B", "I", "ADR", "C", "LG", "FA")
```

- [ ] **Step 4: Rodar e conferir a aprovação**

Run: `python3 -m unittest tests.test_caderno_registro -v`
Expected: PASS nos seis testes.

- [ ] **Step 5: Commit**

```bash
git add scripts/caderno_registro.py tests/test_caderno_registro.py
git commit -m "feat(caderno): registro de secoes, exercicios e codigos

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
```

---

### Task 4: Gerador do template, do mapa e dos gabaritos

**Files:**
- Create: `scripts/gerar_caderno.py`
- Create: `tests/test_caderno_gerador.py`

**Interfaces:**
- Consumes: `caderno_registro` (tarefa 3).
- Produces: `Fragmento(n, titulo, campos, gabarito)`, `Secao(numero, titulo, modo, orientacao, fragmentos)`, `carregar(fonte: Path) -> list[Secao]`, `render_template(secoes) -> str`, `render_gabarito(secoes, n, docs) -> str`, `render_mapa(secoes, existentes, docs) -> str`, `render_indice(existentes) -> str`, `saidas(secoes, docs) -> dict[Path, str]`, `divergencias(saidas_, docs) -> list[str]`.

Formato da fonte, um arquivo `NN-nome.md` por seção:

```
---
secao: 3
titulo: Requisitos
modo: acumula
---
<!--orientacao-->
(tabela de orientação em Markdown)
<!--/orientacao-->

<!--ex n=5 titulo="Direcionadores de mudança"-->
<!--campos-->
- campo que o aluno preenche
<!--/campos-->
<!--gabarito-->
Texto do gabarito, sem títulos de nível 1 a 3.
<!--/gabarito-->
<!--/ex-->
```

- [ ] **Step 1: Escrever o teste**

```python
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

    def test_gabarito_cinco_nao_traz_o_seis(self):
        texto = self.ger.render_gabarito(self.secoes, 5, self.docs)
        self.assertIn("Texto do gabarito cinco.", texto)
        self.assertNotIn("Texto do gabarito seis.", texto)

    def test_gabarito_seis_contem_o_cinco_e_destaca_so_o_seis(self):
        texto = self.ger.render_gabarito(self.secoes, 6, self.docs)
        self.assertIn("Texto do gabarito cinco.", texto)
        self.assertIn('<div class="caderno-novo" markdown="1">\n\nTexto do gabarito seis.', texto)
        self.assertNotIn('markdown="1">\n\nTexto do gabarito cinco', texto)

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
```

- [ ] **Step 2: Rodar e conferir a falha**

Run: `python3 -m unittest tests.test_caderno_gerador -v`
Expected: FAIL, `scripts/gerar_caderno.py` não existe.

- [ ] **Step 3: Implementar**

```python
"""Gera o template, o mapa e os gabaritos cumulativos do caderno arquitetural.

A fonte fica em caderno-fonte/. Uso:
    python3 scripts/gerar_caderno.py          grava as páginas em docs/
    python3 scripts/gerar_caderno.py --check  falha se alguma página diverge da fonte
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from caderno_registro import EXERCICIOS, PLANO, SUBSTITUI, TITULOS_SECAO  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
FONTE = ROOT / "caderno-fonte"

FRONT = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
ORIENTACAO = re.compile(r"<!--orientacao-->\n(.*?)<!--/orientacao-->", re.DOTALL)
FRAGMENTO = re.compile(r'<!--ex n=(\d+) titulo="([^"]+)"-->\n(.*?)<!--/ex-->', re.DOTALL)
CAMPOS = re.compile(r"<!--campos-->\n(.*?)<!--/campos-->", re.DOTALL)
GABARITO = re.compile(r"<!--gabarito-->\n(.*?)<!--/gabarito-->", re.DOTALL)

INTRO_TEMPLATE = (
    "O caderno arquitetural é o documento de arquitetura da solução da ACME. Ele reúne, em dez "
    "seções, as decisões que o curso ensina a tomar, cada uma ligada ao requisito que a motivou. "
    "A tabela de cada seção indica o que vai nela, a pergunta que responde, os artefatos que a "
    "compõem, a entrada de que depende e o exercício que a preenche. As "
    "[convenções](convencoes.md) definem os códigos dos artefatos, e o [mapa](mapa.md) relaciona "
    "seção, bloco e exercício."
)


@dataclass(frozen=True)
class Fragmento:
    n: int
    titulo: str
    campos: str
    gabarito: str


@dataclass(frozen=True)
class Secao:
    numero: int
    titulo: str
    modo: str
    orientacao: str
    fragmentos: tuple[Fragmento, ...]


def _extrair(padrao: re.Pattern, texto: str) -> str:
    achado = padrao.search(texto)
    return achado.group(1) if achado else ""


def carregar(fonte: Path = FONTE) -> list[Secao]:
    secoes: list[Secao] = []
    for caminho in sorted(fonte.glob("[0-9][0-9]-*.md")):
        texto = caminho.read_text(encoding="utf-8")
        front = FRONT.match(texto)
        if front is None:
            raise ValueError(f"{caminho.name}: falta o cabeçalho de metadados")
        meta = dict(linha.split(": ", 1) for linha in front.group(1).splitlines())
        if "secao" not in meta or "titulo" not in meta:
            raise ValueError(f"{caminho.name}: o cabeçalho precisa de secao e titulo")
        corpo = texto[front.end():]
        if corpo.count("<!--ex ") != corpo.count("<!--/ex-->"):
            raise ValueError(f"{caminho.name}: marcador ex sem fechamento")
        orientacao = _extrair(ORIENTACAO, corpo).strip()
        if not orientacao:
            raise ValueError(f"{caminho.name}: falta a orientação da seção")
        fragmentos: list[Fragmento] = []
        vistos: set[int] = set()
        for achado in FRAGMENTO.finditer(corpo):
            n = int(achado.group(1))
            if n in vistos:
                raise ValueError(f"{caminho.name}: exercício {n} repetido na seção")
            vistos.add(n)
            gabarito = _extrair(GABARITO, achado.group(3)).strip()
            # O gabarito usa títulos de nível 4 ou maior. Bloco de código com
            # comentário iniciado por # deve usar a cerca ```, que o teste não distingue.
            for linha in gabarito.splitlines():
                if re.match(r"#{1,3}\s", linha):
                    raise ValueError(
                        f"{caminho.name}: título de nível 1 a 3 no gabarito do exercício {n}"
                    )
            fragmentos.append(
                Fragmento(n, achado.group(2), _extrair(CAMPOS, achado.group(3)).strip(), gabarito)
            )
        secoes.append(
            Secao(int(meta["secao"]), meta["titulo"], meta.get("modo", "acumula"),
                  orientacao, tuple(fragmentos))
        )
    return sorted(secoes, key=lambda s: s.numero)


def _rotulo(numero: int) -> str:
    return TITULOS_SECAO[numero] if numero == 0 else f"{numero}. {TITULOS_SECAO[numero]}"


def _cabecalho(secao: Secao) -> str:
    return f"## {_rotulo(secao.numero)}"


def _visiveis(secao: Secao, n: int) -> list[Fragmento]:
    visiveis = [f for f in secao.fragmentos if f.gabarito and f.n <= n]
    if secao.modo == "substitui" and visiveis:
        ultimo = max(f.n for f in visiveis)
        visiveis = [f for f in visiveis if f.n == ultimo]
    return visiveis


def _pagina(n: int, docs: Path) -> str | None:
    arquivo = EXERCICIOS[n][1]
    return arquivo if (docs / arquivo).exists() else None


def render_template(secoes: list[Secao]) -> str:
    partes = ["# Template do caderno arquitetural", "", INTRO_TEMPLATE, ""]
    for secao in secoes:
        partes += [_cabecalho(secao), "", secao.orientacao, ""]
        if secao.modo != "acumula":
            continue
        for i, fragmento in enumerate(secao.fragmentos, start=1):
            partes += [f"### {secao.numero}.{i} {fragmento.titulo}", "",
                       f"Preenchida no exercício {fragmento.n}.", ""]
            if fragmento.campos:
                partes += ["Campos a preencher:", "", fragmento.campos, ""]
    return "\n".join(partes).rstrip() + "\n"


def render_gabarito(secoes: list[Secao], n: int, docs: Path = DOCS) -> str:
    partes = [f"# Gabarito do exercício {n}", ""]
    intro = (
        f"O caderno abaixo reúne o resultado dos exercícios 1 a {n}, e o trecho em destaque é o "
        f"que o exercício {n} preenche."
    )
    pagina = _pagina(n, docs)
    if pagina:
        intro += f" O [enunciado do exercício {n}](../{pagina}#exercicio-{n}) está na página do bloco."
    partes += [intro, ""]
    pendentes: list[str] = []
    for secao in secoes:
        visiveis = _visiveis(secao, n)
        if not visiveis:
            pendentes.append(_rotulo(secao.numero))
            continue
        partes += [_cabecalho(secao), ""]
        for i, fragmento in enumerate(secao.fragmentos, start=1):
            if fragmento not in visiveis:
                continue
            if secao.modo == "acumula":
                partes += [f"### {secao.numero}.{i} {fragmento.titulo}", ""]
            if fragmento.n == n:
                partes += ['<div class="caderno-novo" markdown="1">', "", fragmento.gabarito, "", "</div>", ""]
            else:
                partes += [fragmento.gabarito, ""]
    if pendentes:
        partes += ["Seções que os exercícios seguintes preenchem: " + ", ".join(pendentes), ""]
    return "\n".join(partes).rstrip() + "\n"


def _com_gabarito(secoes: list[Secao]) -> set[int]:
    return {f.n for s in secoes for f in s.fragmentos if f.gabarito}


def render_mapa(secoes: list[Secao], existentes: set[int], docs: Path = DOCS) -> str:
    linhas = [
        "# Mapa do caderno arquitetural",
        "",
        "A tabela relaciona cada seção do caderno ao bloco que a ensina, ao exercício que a "
        "preenche e ao gabarito em que o resultado aparece. As seções 0 e 10 são revistas ao fim "
        "de cada aula, nos exercícios 4, 8, 12, 16, 20 e 24.",
        "",
        "| Seção | Aula | Bloco | Exercício | Gabarito |",
        "| --- | --- | --- | --- | --- |",
    ]
    pares = {(s, n) for n, ss in PLANO.items() for s in ss}
    pares |= {(s, n) for s, ns in SUBSTITUI.items() for n in ns}
    for secao, n in sorted(pares):
        aula, arquivo, titulo = EXERCICIOS[n]
        numero_bloco = re.search(r"bloco-(\d)", arquivo).group(1)
        existe = (docs / arquivo).exists()
        bloco = f"[Bloco {numero_bloco}, {titulo}](../{arquivo})" if existe else f"Bloco {numero_bloco}, {titulo}"
        exercicio = f"[Exercício {n}](../{arquivo}#exercicio-{n})" if existe else f"Exercício {n}"
        gabarito = (
            f"[Gabarito {n}](../gabaritos/gabarito-exercicio-{n:02d}.md)" if n in existentes else "A publicar"
        )
        linhas.append(f"| {_rotulo(secao)} | Aula {aula} | {bloco} | {exercicio} | {gabarito} |")
    return "\n".join(linhas) + "\n"


def render_indice(existentes: set[int]) -> str:
    partes = [
        "# Gabaritos",
        "",
        "Cada gabarito é o caderno arquitetural da ACME com o resultado dos exercícios até aquele "
        "ponto, e o trecho que o exercício preenche aparece em destaque. O "
        "[template](../caderno/template.md) mostra o caderno vazio, e o "
        "[mapa](../caderno/mapa.md) relaciona seção, bloco e exercício.",
        "",
    ]
    if not existentes:
        partes.append("Nenhum gabarito foi publicado até o momento.")
    else:
        partes += ["| Exercício | Gabarito |", "| --- | --- |"]
        for n in sorted(existentes):
            partes.append(f"| Exercício {n}, {EXERCICIOS[n][2]} | [Gabarito {n}](gabarito-exercicio-{n:02d}.md) |")
    return "\n".join(partes).rstrip() + "\n"


def saidas(secoes: list[Secao], docs: Path = DOCS) -> dict[Path, str]:
    existentes = _com_gabarito(secoes)
    resultado = {
        docs / "caderno" / "template.md": render_template(secoes),
        docs / "caderno" / "mapa.md": render_mapa(secoes, existentes, docs),
        docs / "gabaritos" / "index.md": render_indice(existentes),
    }
    for n in sorted(existentes):
        resultado[docs / "gabaritos" / f"gabarito-exercicio-{n:02d}.md"] = render_gabarito(secoes, n, docs)
    return resultado


def divergencias(saidas_: dict[Path, str], docs: Path = DOCS) -> list[str]:
    problemas = []
    for caminho, texto in saidas_.items():
        if not caminho.exists() or caminho.read_text(encoding="utf-8") != texto:
            problemas.append(f"{caminho.name} diverge da fonte")
    for caminho in sorted((docs / "gabaritos").glob("gabarito-exercicio-*.md")):
        if caminho not in saidas_:
            problemas.append(f"{caminho.name} sobra, sem trecho na fonte")
    return problemas


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera as páginas do caderno arquitetural")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    gerado = saidas(carregar())
    if args.check:
        problemas = divergencias(gerado)
        for problema in problemas:
            print(problema)
        print(f"\nResumo: {len(problemas)} divergência(s).")
        return 1 if problemas else 0
    for caminho, texto in gerado.items():
        caminho.parent.mkdir(parents=True, exist_ok=True)
        caminho.write_text(texto, encoding="utf-8")
    for caminho in (DOCS / "gabaritos").glob("gabarito-exercicio-*.md"):
        if caminho not in gerado:
            caminho.unlink()
    print(f"gravadas {len(gerado)} páginas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Rodar e conferir a aprovação**

Run: `python3 -m unittest tests.test_caderno_gerador -v`
Expected: PASS nos 14 testes. Se `test_exercicio_sem_gabarito_aparece_como_a_publicar` falhar no `assertRegex`, imprimir `mapa` e conferir o formato da linha do exercício 7: sem arquivo de bloco na pasta temporária, a célula é `Exercício 7`, seguida de ` | A publicar |`.

- [ ] **Step 5: Commit**

```bash
git add scripts/gerar_caderno.py tests/test_caderno_gerador.py
git commit -m "feat(caderno): gerador de template, mapa e gabaritos cumulativos

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
```

---

### Task 5: Fonte do caderno, orientação das onze seções

**Files:**
- Create: `caderno-fonte/00-resumo.md`, `01-contexto.md`, `02-partes-interessadas.md`, `03-requisitos.md`, `04-linha-de-base-e-lacunas.md`, `05-contexto-c4.md`, `06-principios.md`, `07-decisoes.md`, `08-tecnologia-e-plataforma.md`, `09-roteiro-e-governanca.md`, `10-pendencias.md`

**Interfaces:**
- Consumes: formato da fonte (tarefa 4).
- Produces: orientação das seções 0 a 10. Os trechos de gabarito (`<!--ex ...-->`) entram nas partes 2 a 7 da decomposição, e esta tarefa não cria nenhum.

Cada arquivo tem o cabeçalho de metadados, o marcador de orientação e uma tabela de cinco linhas. Os arquivos não levam ponto-e-vírgula nem travessão.

- [ ] **Step 1: Criar `caderno-fonte/00-resumo.md`**

```
---
secao: 0
titulo: A solução em uma página
modo: substitui
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| O que vai | O problema, a pergunta, a decisão central, o requisito que guia o desenho, o que a organização aceita em troca e o estado das decisões |
| Pergunta que responde | O que um leitor que lesse só esta página precisaria saber para apoiar ou questionar o projeto |
| Artefatos | Cinco parágrafos curtos, um para cada item acima, e uma linha de estado que diz o que está proposto e o que depende de prova |
| Entrada | Todas as seções seguintes, porque o resumo só repete o que elas já registram |
| Preenchida em | Revista ao fim de cada aula, nos exercícios 4, 8, 12, 16, 20 e 24, e fechada no exercício 24 |
<!--/orientacao-->
```

- [ ] **Step 2: Criar `01-contexto.md`**

```
---
secao: 1
titulo: Contexto
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| O que vai | A instituição e os números do problema, as restrições que chegam fechadas, as respostas já excluídas, as decisões classificadas por nível de arquitetura, os componentes da solução nos cinco tipos e os papéis de quem decide |
| Pergunta que responde | Que organização é esta, que problema ela precisa resolver e quem decide cada parte |
| Artefatos e códigos | Tabela de porte, tabela de restrições com origem e efeito, decisões D1 a Dn pelo nível que cada uma toma, premissas PR1 a PRn |
| Entrada | O dossiê do caso ACME, em particular a página inicial do caso e os dados operacionais |
| Preenchida em | Aula 1, exercícios 1 a 4 |
<!--/orientacao-->
```

- [ ] **Step 3: Criar `02-partes-interessadas.md`**

```
---
secao: 2
titulo: Partes interessadas
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| O que vai | Os papéis envolvidos, o que cada um quer e teme, o tratamento dado a cada um, os conflitos de expectativa, os pontos de vista e a declaração de escopo do primeiro ciclo |
| Pergunta que responde | Quem precisa ser envolvido nas decisões e onde as expectativas se chocam |
| Artefatos e códigos | Matriz de partes interessadas com tratamento (envolver, consultar, manter informado), pontos de vista, declaração de escopo com o que muda, o que permanece e a origem de cada exclusão |
| Entrada | Seção 1, em particular as restrições fechadas e o mapa de atores |
| Preenchida em | Aula 2, exercício 8 |
<!--/orientacao-->
```

- [ ] **Step 4: Criar `03-requisitos.md`**

```
---
secao: 3
titulo: Requisitos
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| O que vai | Os direcionadores de mudança classificados, o catálogo de requisitos com tipo, medida e prioridade, os requisitos vagos reescritos de forma mensurável, os cenários de qualidade e os requisitos derivados |
| Pergunta que responde | O que a solução precisa entregar e com que medida se verifica que entregou |
| Artefatos e códigos | Direcionadores com evidência, catálogo R1 a Rn, requisitos derivados RD1 a RDn, cenários CQ com seis elementos (fonte, estímulo, ambiente, artefato, resposta, medida) |
| Entrada | Seções 1 e 2, porque restrição e parte interessada delimitam o que é requisito |
| Preenchida em | Aula 2, exercícios 5, 6 e 7 |
<!--/orientacao-->
```

- [ ] **Step 5: Criar `04-linha-de-base-e-lacunas.md`**

```
---
secao: 4
titulo: Linha de base e lacunas
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| O que vai | A descrição da arquitetura atual, com camadas, integrações, incidentes e dívida técnica, e a lista das lacunas entre a linha de base e a arquitetura alvo |
| Pergunta que responde | Como o sistema é hoje, onde ele é frágil e o que falta para chegar ao alvo |
| Artefatos e códigos | Descrição da linha de base, tabela de incidentes com causa e impacto, relatório de lacunas L1 a Ln com domínio, forma de fechamento e onda |
| Entrada | Seção 3 para a linha de base, e as seções 5 a 8 para a arquitetura alvo com que a linha de base é comparada |
| Preenchida em | Linha de base na Aula 2, exercício 7, e lacunas na Aula 6, exercício 21 |
<!--/orientacao-->
```

- [ ] **Step 6: Criar `05-contexto-c4.md`**

```
---
secao: 5
titulo: Contexto do sistema (C4, nível 1)
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| O que vai | O diagrama de contexto do sistema, com a fronteira da solução, os perfis de usuário e os sistemas externos, e a razão de cada elemento ficar dentro ou fora da fronteira |
| Pergunta que responde | O que está dentro da solução, o que fica fora e com quem ela se relaciona |
| Artefatos e códigos | Diagrama C4 de nível 1 com legenda e um parágrafo que justifica a fronteira |
| Entrada | Seções 2 e 4, porque as partes interessadas e a linha de base definem usuários e sistemas externos |
| Preenchida em | Aula 4, exercício 15 |
<!--/orientacao-->
```

- [ ] **Step 7: Criar `06-principios.md`**

```
---
secao: 6
titulo: Princípios
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| O que vai | As regras que orientam todas as decisões de design, cada uma com o que ela proíbe e com o requisito ou a restrição que a motiva |
| Pergunta que responde | Que regras o desenho precisa respeitar, de modo que uma decisão possa ser recusada por violá-las |
| Artefatos e códigos | Tabela de princípios P1 a Pn, com a proibição correspondente e a rastreabilidade ao requisito |
| Entrada | Seções 1 e 3, porque os princípios derivam de restrições e de requisitos |
| Preenchida em | Aula 3, exercício 9 |
<!--/orientacao-->
```

- [ ] **Step 8: Criar `07-decisoes.md`**

```
---
secao: 7
titulo: Decisões
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| O que vai | As decisões de desenho, de padrões, de negócio, de dados, de aplicações e integração e de infraestrutura, cada uma com a escolha, o requisito a que responde e o registro de decisão arquitetural que a formaliza |
| Pergunta que responde | Que decisões estruturais foram tomadas, com que compromisso e como se confirma que valeram |
| Artefatos e códigos | Decisões de design DD1 a DDn, decisões de legado e dados DL1 a DLn, blocos B1 a Bn, interfaces I1 a In, registros ADR 001 a ADR nnn |
| Entrada | Seções 3 e 6, porque cada decisão responde a requisito e obedece a princípio |
| Preenchida em | Aulas 3 e 4, exercícios 10, 11, 12, 13, 14 e 16 |
<!--/orientacao-->
```

- [ ] **Step 9: Criar `08-tecnologia-e-plataforma.md`**

```
---
secao: 8
titulo: Tecnologia e plataforma
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| O que vai | O modelo técnico de referência em cinco colunas, a matriz de seleção, a plataforma e a zona de pouso escolhidas, a avaliação de segurança fim a fim, o registro de decisão da plataforma e as lacunas de provisão |
| Pergunta que responde | Com que tecnologia a solução pode ser construída, sobre que plataforma ela executa e como se protege |
| Artefatos e códigos | Modelo técnico de referência com classificação verde, âmbar e vermelho, matriz dos seis critérios, quadro comparativo de plataformas, ativos classificados, grade de permissões, ameaças por categoria STRIDE, controles C1 a Cn, ADR de plataforma |
| Entrada | Seções 5 e 7, porque os contêineres e as decisões estruturais definem o que a tecnologia precisa realizar |
| Preenchida em | Aula 5, exercícios 17, 18, 19 e 20 |
<!--/orientacao-->
```

- [ ] **Step 10: Criar `09-roteiro-e-governanca.md`**

```
---
secao: 9
titulo: Roteiro e governança
modo: acumula
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| O que vai | A ordem em que a mudança acontece, em ondas com entregas, valor e critério de conclusão, e o modo como a arquitetura é governada durante e depois da execução |
| Pergunta que responde | Em que ordem as lacunas se fecham e como se impede que a arquitetura derive depois de aprovada |
| Artefatos e códigos | Tabela de ondas, conselho de revisão com periodicidade, funções de aptidão FA1 a FAn, registro de dívida técnica, níveis de serviço |
| Entrada | Seção 4, porque as lacunas confirmadas são a matéria das ondas |
| Preenchida em | Aula 6, exercícios 22 e 23 |
<!--/orientacao-->
```

- [ ] **Step 11: Criar `10-pendencias.md`**

```
---
secao: 10
titulo: O que ainda falta decidir
modo: substitui
---
<!--orientacao-->
| Campo | Conteúdo |
| --- | --- |
| O que vai | As pendências que impedem fechar uma decisão e a pessoa ou o grupo com autoridade para resolvê-las |
| Pergunta que responde | O que ainda depende de decisão ou de verificação e quem decide |
| Artefatos e códigos | Tabela de pendência e responsável, com a tendência tecnológica avaliada no encerramento |
| Entrada | Todas as seções anteriores, porque cada premissa não confirmada gera uma pendência |
| Preenchida em | Revista ao fim de cada aula, nos exercícios 4, 8, 12, 16, 20 e 24, e fechada no exercício 24 |
<!--/orientacao-->
```

- [ ] **Step 12: Conferir que a fonte carrega e gerar as páginas**

Run:
```bash
python3 -c "
import importlib.util
s = importlib.util.spec_from_file_location('g', 'scripts/gerar_caderno.py'); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
print([x.numero for x in m.carregar()])"
```
Expected: `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`.

- [ ] **Step 13: Commit**

```bash
git add caderno-fonte
git commit -m "feat(caderno): fonte com a orientacao das onze secoes

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
```

---

### Task 6: Página de convenções

**Files:**
- Create: `docs/caderno/convencoes.md`

**Interfaces:**
- Consumes: `CODIGOS` (tarefa 3). A tarefa 9 testa que cada código aparece na primeira coluna da tabela.

- [ ] **Step 1: Escrever o teste, em `tests/test_caderno_convencoes.py`**

```python
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
```

- [ ] **Step 2: Rodar e conferir a falha**

Run: `python3 -m unittest tests.test_caderno_convencoes -v`
Expected: FAIL, `FileNotFoundError` para `convencoes.md`.

- [ ] **Step 3: Criar `docs/caderno/convencoes.md`**

```markdown
# Convenções do caderno arquitetural

O caderno usa códigos curtos para que uma decisão, um requisito e uma lacuna possam ser citados de qualquer seção sem ambiguidade. Esta página define os códigos, os marcadores de estado e a regra de rastreabilidade que liga uma decisão ao requisito que a motivou.

## Códigos de artefato

Cada código é a inicial do artefato seguida de um número sequencial dentro do caderno, como R6 para o sexto requisito declarado.

| Código | Artefato | Seção |
| --- | --- | --- |
| D | Decisão classificada por nível de arquitetura | 1 |
| PR | Premissa adotada na ausência de dado | 1 |
| RT | Restrição que chega fechada | 1 |
| R | Requisito declarado pelas partes interessadas | 3 |
| RD | Requisito derivado de outro requisito ou de uma restrição | 3 |
| CQ | Cenário de atributo de qualidade | 3 |
| L | Lacuna entre a linha de base e a arquitetura alvo | 4 |
| P | Princípio de design | 6 |
| DD | Decisão de design | 7 |
| DL | Decisão de legado e de dados | 7 |
| B | Bloco de construção da solução | 7 |
| I | Interface entre blocos | 7 |
| ADR | Registro de decisão arquitetural | 7 e 8 |
| C | Controle de segurança | 8 |
| LG | Ligação entre contêineres, com protocolo e contrato | 7 |
| FA | Função de aptidão que verifica uma decisão na esteira | 9 |

## Marcadores de estado

Uma decisão ou um artefato que ainda depende de validação com as partes interessadas recebe o marcador **proposto**. Um valor que o caso não registra recebe o marcador **a definir**, com a pessoa que o fornece. Os dois marcadores saem quando a validação ocorre, e a seção 10 do caderno lista tudo o que ainda os carrega.

## Rastreabilidade

Toda decisão das seções 6 a 8 cita o requisito ou a restrição que a motivou, e todo requisito da seção 3 aponta a decisão que o atende e a medida que verifica o atendimento. A leitura de uma decisão sem requisito de origem indica decisão sem justificativa, e a leitura de um requisito sem decisão indica lacuna a registrar na seção 4.
```

- [ ] **Step 4: Rodar teste e validador**

Run:
```bash
python3 -m unittest tests.test_caderno_convencoes -v
python3 scripts/validate_content.py | tail -3
```
Expected: PASS, e `Resumo: 0 violacao(oes).`

- [ ] **Step 5: Commit**

```bash
git add docs/caderno/convencoes.md tests/test_caderno_convencoes.py
git commit -m "docs(caderno): convencoes de codigos, marcadores e rastreabilidade

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
```

---

### Task 7: Páginas geradas, navegação, estilo e página inicial

**Files:**
- Create (gerados): `docs/caderno/template.md`, `docs/caderno/mapa.md`, `docs/gabaritos/index.md`
- Modify: `mkdocs.yml` (nav e versão do CSS)
- Modify: `docs/assets/stylesheets/extra.css`
- Modify: `docs/index.md`
- Create: `tests/test_caderno_site.py`

- [ ] **Step 1: Escrever o teste**

```python
"""Páginas do caderno e dos gabaritos entram no site e coincidem com a fonte."""

import importlib.util
import re
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
        self.assertIn(".caderno-novo", css)
        self.assertIn("extra.css?v=20261016-1", (ROOT / "mkdocs.yml").read_text(encoding="utf-8"))

    def test_pagina_inicial_apresenta_o_caderno(self):
        texto = (DOCS / "index.md").read_text(encoding="utf-8")
        self.assertIn("## O caderno arquitetural", texto)
        self.assertIn("caderno/template.md", texto)
```

- [ ] **Step 2: Rodar e conferir a falha**

Run: `python3 -m unittest tests.test_caderno_site -v`
Expected: FAIL (páginas geradas ainda não existem, nav sem entradas, CSS sem estilo).

- [ ] **Step 3: Gerar as páginas**

Run: `python3 scripts/gerar_caderno.py`
Expected: `gravadas 3 páginas`.

- [ ] **Step 4: Editar `mkdocs.yml`**

Trocar a linha `  - assets/stylesheets/extra.css?v=20261003-3` por `  - assets/stylesheets/extra.css?v=20261016-1`, e inserir, entre `Caso ACME` e `Referência` no `nav`:

```yaml
  - Caderno arquitetural:
      - Template: caderno/template.md
      - Convenções: caderno/convencoes.md
      - Mapa: caderno/mapa.md
  - Gabaritos:
      - Visão geral: gabaritos/index.md
```

- [ ] **Step 5: Acrescentar o estilo ao fim de `docs/assets/stylesheets/extra.css`**

```css

.md-typeset .caderno-novo {
  border-left: 0.25rem solid var(--course-cobalt);
  background: #EEF4FA;
  padding: 0.1rem 1rem;
  margin: 1rem 0;
}
```

- [ ] **Step 6: Acrescentar a seção à página inicial**

Inserir em `docs/index.md`, antes de `## Avaliação`:

```markdown
## O caderno arquitetural

O curso produz, exercício a exercício, o caderno arquitetural da ACME, documento de arquitetura da solução com dez seções. O [template](caderno/template.md) apresenta o caderno vazio, com o que vai em cada seção, e o [mapa](caderno/mapa.md) relaciona seção, bloco e exercício. A seção Gabaritos traz, para cada exercício, o caderno preenchido até aquele ponto.
```

- [ ] **Step 7: Rodar testes, validador e compilação estrita**

Run:
```bash
python3 -m unittest discover -s tests 2>&1 | tail -3
python3 scripts/validate_content.py | tail -3
.venv/bin/mkdocs build --strict 2>&1 | tail -5
```
Expected: todos os testes passam, `Resumo: 0 violacao(oes).` e `mkdocs` termina sem `WARNING`. Se o validador acusar link quebrado em `mapa.md`, conferir a coluna Exercício da linha citada contra `## Exercício N` na página do bloco.

- [ ] **Step 8: Commit**

```bash
git add docs/caderno docs/gabaritos docs/index.md docs/assets/stylesheets/extra.css mkdocs.yml tests/test_caderno_site.py
git commit -m "feat(caderno): template, mapa e indice de gabaritos no site

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
```

---

### Task 8: Validador, anatomia de oito seções por adesão

**Files:**
- Modify: `scripts/validate_content.py` (constantes e `check_block_anatomy`, `--module`)
- Create: `tests/test_validador_caderno.py`

**Interfaces:**
- Produces: `CADERNO_SECTION = "No caderno arquitetural"` e `CADERNO_BLOCKS: set[str]`, conjunto de nomes de arquivo de bloco que já exigem a seção. As partes 2 a 6 acrescentam os arquivos de cada módulo. Bloco fora do conjunto não é obrigado a ter a seção, mas, se a tiver, ela precisa estar entre `Uso pelo arquiteto` e `Exercício`.

- [ ] **Step 1: Escrever o teste**

```python
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
        self.addCleanup(setattr, self.v, "CADERNO_BLOCKS", set())

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
```

- [ ] **Step 2: Rodar e conferir a falha**

Run: `python3 -m unittest tests.test_validador_caderno -v`
Expected: FAIL, `AttributeError: ... CADERNO_BLOCKS`.

- [ ] **Step 3: Alterar o validador**

Em `scripts/validate_content.py`, trocar:

```python
EXTRA_SECTIONS = ("caso-acme", "referencia")
```
por
```python
EXTRA_SECTIONS = ("caso-acme", "referencia", "caderno", "gabaritos")
```

Depois de `BLOCK_SECTIONS = (...)`, acrescentar:

```python
# Seção que liga o bloco ao caderno arquitetural. Os blocos listados em
# CADERNO_BLOCKS já a exigem, e as partes 2 a 6 da migração acrescentam os
# arquivos de cada módulo. Em qualquer bloco, quando existe, a seção precisa
# estar entre "Uso pelo arquiteto" e "Exercício".
CADERNO_SECTION = "No caderno arquitetural"
CADERNO_BLOCKS: set[str] = set()
```

Em `check_block_anatomy`, substituir o corpo, a partir de `sections = BLOCK_SECTIONS`, por:

```python
    sections = BLOCK_SECTIONS
    if path.name.startswith("bloco-0-"):
        sections = tuple(s for s in BLOCK_SECTIONS if s != "Exercício")
    tem_caderno = re.search(rf"^##\s+{re.escape(CADERNO_SECTION)}\s*$", text, re.MULTILINE)
    if path.name in CADERNO_BLOCKS or tem_caderno:
        if not path.name.startswith("bloco-0-"):
            indice = sections.index("Exercício")
            sections = sections[:indice] + (CADERNO_SECTION,) + sections[indice:]
    positions = []
    for section in sections:
        if section == "Exercício":
            match = re.search(r"^##\s+Exerc[ií]cio\s+\d+\s*$", text, re.MULTILINE)
        elif section == CONCEPT_SECTION:
            match = _find_concept_section(text)
        else:
            match = re.search(rf"^##\s+{re.escape(section)}", text, re.MULTILINE)
        if match is None:
            return [f"{path.relative_to(ROOT)}: falta a secao {section}"]
        positions.append(match.start())
    if positions != sorted(positions):
        return [f"{path.relative_to(ROOT)}: secoes fora da ordem definida"]
    return []
```

Atenção: `_find_concept_section` devolve `None` se a primeira seção depois de `Antes de começar` for uma das nomeadas, e `No caderno arquitetural` não está em `nomeadas`. Ela só vira a seção de conceito se vier antes de `Uso pelo arquiteto`, o que o teste de ordem já cobre. Para evitar que `## No caderno arquitetural` colocada antes de `Conceito` seja tomada como conceito, acrescentar `CADERNO_SECTION` à tupla `nomeadas` dentro de `_find_concept_section`:

```python
    nomeadas = ("Uso pelo arquiteto", "Exercício", "Exercicio", "Fontes", CADERNO_SECTION)
```

- [ ] **Step 4: Rodar tudo**

Run:
```bash
python3 -m unittest tests.test_validador_caderno -v
python3 -m unittest discover -s tests 2>&1 | tail -3
python3 scripts/validate_content.py | tail -2
```
Expected: PASS nos cinco testes novos, suíte inteira verde, 0 violações. O teste `test_secao_fora_de_ordem_e_rejeitada_mesmo_fora_do_conjunto` depende de `_find_concept_section`: com a seção do caderno antes de `Uso pelo arquiteto` e sem `Conceito` entre elas, o erro esperado seria `falta a secao Conceito`. Por isso o texto do teste mantém `## Conceito` e a seção do caderno é inserida logo antes de `## Uso pelo arquiteto`, depois do conceito, o que dá o erro de ordem. Se o erro obtido for outro, imprimir `erros` e ajustar o teste ao comportamento descrito aqui.

- [ ] **Step 5: Commit**

```bash
git add scripts/validate_content.py tests/test_validador_caderno.py
git commit -m "feat(validador): secao No caderno arquitetural por adesao e novas secoes de site

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
```

---

### Task 9: Contrato da fonte e dos gabaritos

**Files:**
- Create: `tests/test_caderno_contrato.py`

**Interfaces:**
- Consumes: `carregar`, `PLANO`, `SUBSTITUI`, `TITULOS_SECAO`, `EXERCICIOS`.
- Produces: testes que protegem as partes 2 a 7, ativos desde já com a fonte só de orientação.

- [ ] **Step 1: Escrever o teste**

```python
"""Contrato da fonte do caderno e dos gabaritos publicados."""

import importlib.util
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CAMPOS_DA_TABELA = ("O que vai", "Pergunta que responde", "Artefatos", "Entrada", "Preenchida em")


def carregar(nome):
    spec = importlib.util.spec_from_file_location(nome, ROOT / "scripts" / f"{nome}.py")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


class ContratoDoCadernoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ger = carregar("gerar_caderno")
        cls.reg = carregar("caderno_registro")
        cls.secoes = cls.ger.carregar()

    def test_fonte_tem_as_onze_secoes_com_o_titulo_do_registro(self):
        self.assertEqual(sorted(self.reg.TITULOS_SECAO), [s.numero for s in self.secoes])
        for secao in self.secoes:
            with self.subTest(secao=secao.numero):
                self.assertEqual(self.reg.TITULOS_SECAO[secao.numero], secao.titulo)

    def test_secoes_que_substituem_sao_as_do_registro(self):
        for secao in self.secoes:
            esperado = "substitui" if secao.numero in self.reg.SUBSTITUI else "acumula"
            with self.subTest(secao=secao.numero):
                self.assertEqual(esperado, secao.modo)

    def test_orientacao_traz_as_cinco_linhas_da_tabela(self):
        for secao in self.secoes:
            for campo in CAMPOS_DA_TABELA:
                with self.subTest(secao=secao.numero, campo=campo):
                    self.assertRegex(secao.orientacao, rf"(?m)^\| {re.escape(campo)}")

    def test_fragmentos_respeitam_o_plano(self):
        for secao in self.secoes:
            for fragmento in secao.fragmentos:
                with self.subTest(secao=secao.numero, exercicio=fragmento.n):
                    if secao.modo == "substitui":
                        self.assertIn(fragmento.n, self.reg.SUBSTITUI[secao.numero])
                    else:
                        self.assertIn(secao.numero, self.reg.PLANO[fragmento.n])

    def test_cada_gabarito_publicado_tem_enunciado_que_aponta_de_volta(self):
        for caminho in sorted((DOCS / "gabaritos").glob("gabarito-exercicio-*.md")):
            n = int(re.search(r"(\d+)\.md$", caminho.name).group(1))
            _, arquivo, _ = self.reg.EXERCICIOS[n]
            with self.subTest(exercicio=n):
                pagina = (DOCS / arquivo).read_text(encoding="utf-8")
                self.assertIn(f"gabaritos/{caminho.name}", pagina)

    def test_gabaritos_cumulativos_a_versao_n_contem_os_trechos_anteriores(self):
        existentes = sorted({f.n for s in self.secoes for f in s.fragmentos if f.gabarito})
        for anterior, seguinte in zip(existentes, existentes[1:]):
            texto_n = self.ger.render_gabarito(self.secoes, seguinte, DOCS)
            for secao in self.secoes:
                if secao.modo != "acumula":
                    continue
                for fragmento in secao.fragmentos:
                    if fragmento.gabarito and fragmento.n <= anterior:
                        with self.subTest(de=anterior, para=seguinte, secao=secao.numero):
                            self.assertIn(fragmento.gabarito, texto_n)
```

- [ ] **Step 2: Rodar**

Run: `python3 -m unittest tests.test_caderno_contrato -v`
Expected: PASS em todos os testes. Enquanto a fonte não tiver trechos de gabarito, os testes `test_cada_gabarito_publicado_...` e `..._cumulativos_...` não têm itens e passam vazios, e a proteção passa a valer na parte 2, quando entra o primeiro trecho. Se algum teste falhar por título de fonte diferente do registro, o arquivo da fonte é o que se corrige.

- [ ] **Step 3: Commit**

```bash
git add tests/test_caderno_contrato.py
git commit -m "test(caderno): contrato da fonte, do plano e dos gabaritos cumulativos

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
```

---

### Task 10: Glossário

**Files:**
- Modify: `docs/referencia/glossario.md` (acrescentar ao fim)
- Create: `tests/test_caderno_glossario.py`

- [ ] **Step 1: Escrever o teste**

```python
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
```

- [ ] **Step 2: Rodar e conferir a falha**

Run: `python3 -m unittest tests.test_caderno_glossario -v`
Expected: FAIL em `test_termos_do_caderno_estao_no_glossario`.

- [ ] **Step 3: Acrescentar ao fim de `docs/referencia/glossario.md`**

```markdown

## Descrição de arquitetura

Produto de trabalho que expressa a arquitetura de um sistema num determinado estado, como uma organização, uma aplicação ou uma solução. Cada descrição compõe-se de ao menos um entregável. A arquitetura de linha de base e a arquitetura alvo de uma solução têm descrições distintas, e a análise de lacunas compara as duas.

## Entregável de arquitetura

Documento ou relatório composto, produzido por uma equipe de arquitetura por solicitação ou como parte do ciclo de vida, para uma descrição de arquitetura específica. Reúne informação estruturada, em artefatos, e informação não estruturada, em comentário e análise. São exemplos a declaração de requisitos, o caso de negócio, o esboço da solução, o desenho lógico e o relatório de impacto.

## Artefato de arquitetura

Catálogo, mapa, tabela, diagrama ou modelo que trata de um aspecto específico da arquitetura de um sistema e mostra a relação entre entidades ou outros componentes. A visão é um tipo de artefato, produzido a partir de um ponto de vista. O mesmo artefato pode compor vários entregáveis, e são exemplos o catálogo de interfaces, o diagrama de contexto e o modelo de dados.

## Entidade de arquitetura

Elemento discreto que faz parte da arquitetura de um sistema e interessa a quem analisa e projeta, como um requisito, uma interface ou um componente. Uma entidade pode aparecer em mais de um artefato e relacionar-se com outras por abstração, que a generaliza em categoria, ou por composição, que a forma a partir de várias.

## Caderno arquitetural

Documento de arquitetura da solução do caso ACME, construído ao longo do curso em dez seções, do contexto ao roteiro e à governança. Funciona como a descrição de arquitetura da solução alvo, e cada exercício preenche uma seção. O [template](../caderno/template.md) mostra o caderno vazio, e a seção Gabaritos traz o caderno preenchido a cada exercício.
```

- [ ] **Step 4: Rodar tudo**

Run:
```bash
python3 -m unittest tests.test_caderno_glossario -v
python3 -m unittest discover -s tests 2>&1 | tail -3
python3 scripts/validate_content.py | tail -2
```
Expected: PASS, suíte verde, 0 violações. Se o validador acusar o link do glossário para `../caderno/template.md`, conferir que `docs/caderno/template.md` existe (tarefa 7).

- [ ] **Step 5: Commit**

```bash
git add docs/referencia/glossario.md tests/test_caderno_glossario.py
git commit -m "docs(glossario): termos de descricao de arquitetura e do caderno arquitetural

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
```

---

### Task 11: Aplicar as decisões aprovadas da matriz que pertencem à parte 1

**Pré-condição:** o professor aprovou a matriz da tarefa 2, linha a linha, ou indicou as linhas que não aprova. Sem essa aprovação, **não executar esta tarefa**.

**Files:**
- Modify ou delete: apenas as páginas que a matriz aprovada classifica como `remove` ou `altera` e que não pertencem a um módulo de aula. Candidatas já conhecidas: `docs/caso-acme/artefatos.md`, que o mapa substitui, e as referências a ela em `mkdocs.yml`.
- Modify: `mkdocs.yml` (nav e `redirect_maps`)

**Interfaces:**
- Consumes: matriz aprovada (tarefa 2). Alterações de blocos, exercícios e sínteses dos módulos 1 a 5 pertencem às partes 2 a 6 e **não** são feitas aqui.

- [ ] **Step 1: Listar as linhas da matriz que tocam páginas fora dos módulos de aula**

Run:
```bash
grep -E "^\| página \| (caso-acme|referencia|cronograma|index)" docs/superpowers/auditoria/2026-10-16-matriz-caderno.md
```
Expected: as linhas de `caso-acme/*`, `referencia/*`, `cronograma.md` e `index.md`, cada uma com decisão aprovada.

- [ ] **Step 2: Para `caso-acme/artefatos.md`, se a decisão aprovada for `remove`**

Substituir o item de nav `Artefatos por aula` por nada e adicionar o redirecionamento ao bloco `redirect_maps` de `mkdocs.yml`:

```yaml
        caso-acme/artefatos.md: caderno/mapa.md
```

Em seguida:
```bash
git rm docs/caso-acme/artefatos.md
grep -rn "artefatos.md" docs mkdocs.yml README.md tests
```
Para cada ocorrência restante, trocar o link por `../caderno/mapa.md` (ou `caderno/mapa.md` a partir da raiz de `docs/`) e conferir a âncora.

- [ ] **Step 3: Aplicar as demais linhas aprovadas desta tarefa**

Para cada linha `altera` de `caso-acme/`, `referencia/`, `cronograma.md` ou `index.md`, abrir o arquivo na linha indicada pela coluna Local e aplicar a alteração descrita na justificativa. Cada alteração entra num commit próprio.

- [ ] **Step 4: Rodar tudo**

Run:
```bash
python3 -m unittest discover -s tests 2>&1 | tail -3
python3 scripts/validate_content.py | tail -2
.venv/bin/mkdocs build --strict 2>&1 | tail -5
```
Expected: suíte verde, 0 violações, compilação sem `WARNING`. Se um teste de contrato de módulo citar `artefatos.md` ou o texto removido, atualizar o teste para o novo texto na mesma tarefa.

- [ ] **Step 5: Commit**

```bash
git add -A docs mkdocs.yml tests
git commit -m "docs(caderno): aplica as decisoes aprovadas da matriz fora dos modulos

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
```

---

### Task 12: Emendas à spec, README e verificação final

**Files:**
- Modify: `docs/superpowers/specs/2026-10-16-caderno-arquitetural-design.md`
- Modify: `docs/superpowers/specs/2026-09-19-estrutura-do-curso-design.md`
- Modify: `README.md`

- [ ] **Step 1: Emendar a spec do caderno**

Em `2026-10-16-caderno-arquitetural-design.md`:

1. Seção 4.1, tabela, linha `1. Contexto`: trocar `1, 2, 3` por `1, 2, 3, 4`, e acrescentar à coluna Conteúdo ` e o mapa das seções do caderno nas fases do processo`.
2. Seção 6.1, primeiro item: trocar `` `docs/caderno/fonte/` `` por `` `caderno-fonte/` `` e acrescentar a frase `A fonte fica fora de docs/ porque o MkDocs a publicaria e o validador resolveria os links relativos a partir da pasta errada.`
3. Seção 6.1, acrescentar o item: `As seções 0 e 10 têm modo de substituição, e a página de gabarito N mostra só a versão mais recente com exercício menor ou igual a N. As demais acumulam.`
4. Seção 5.1: acrescentar ao fim a frase `O validador exige a seção apenas nos blocos listados em CADERNO_BLOCKS, que cada parte da decomposição amplia, e rejeita a seção fora de ordem em qualquer bloco.`

- [ ] **Step 2: Registrar as revogações na spec antiga**

Em `2026-09-19-estrutura-do-curso-design.md`, logo abaixo dos títulos `### 12.1 ...` e `### 12.2 ...`, inserir respectivamente:

```markdown
> **Revisto em 16/10/2026** por `2026-10-16-caderno-arquitetural-design.md`: a anatomia passa a oito seções, com `## No caderno arquitetural`, à medida que cada módulo migra.
```
```markdown
> **Revogado em 16/10/2026** por `2026-10-16-caderno-arquitetural-design.md`: os gabaritos voltam ao site, na seção Gabaritos, abertos desde a publicação.
```

- [ ] **Step 3: Atualizar o README**

Na tabela de `README.md`, acrescentar as linhas:

```markdown
| `caderno-fonte/` | Fonte do caderno arquitetural, uma seção por arquivo, com orientação e trechos de gabarito |
| `scripts/gerar_caderno.py` | Gera `docs/caderno/` e `docs/gabaritos/` a partir da fonte, e com `--check` falha se alguma página diverge |
```

- [ ] **Step 4: Verificação final**

Run:
```bash
python3 scripts/gerar_caderno.py --check
python3 -m unittest discover -s tests 2>&1 | tail -3
python3 scripts/validate_content.py | tail -2
.venv/bin/mkdocs build --strict 2>&1 | tail -5
git status --short
```
Expected: `Resumo: 0 divergência(s).`, suíte verde (171 testes anteriores mais os novos), `Resumo: 0 violacao(oes).`, compilação sem `WARNING` e árvore limpa.

- [ ] **Step 5: Atualizar o fluxo de publicação**

Em `.github/workflows/publicar-site.yml`, acrescentar, antes do passo `Validar o conteúdo do curso`:

```yaml
      - name: Conferir as páginas geradas do caderno
        run: python scripts/gerar_caderno.py --check
```

- [ ] **Step 6: Commit**

```bash
git add docs/superpowers/specs README.md .github/workflows/publicar-site.yml
git commit -m "docs(caderno): emendas a spec, README e conferencia das paginas geradas no fluxo

Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>"
```

---

## Self-review

**Cobertura da spec.** As três páginas da seção 4.2 saem das tarefas 6 e 7, com o template e o mapa gerados e as convenções escritas à mão, e a seção 4.3, sobre o módulo 1, pertence à parte 2 e fica fora deste plano. A anatomia de oito seções da seção 5.1 entra no validador na tarefa 8, com adesão por bloco, e o glossário da seção 5.3 entra na tarefa 10, enquanto os exercícios, as sínteses e os índices das seções 5.2 e 5.3 pertencem às partes 2 a 6. A fonte única, a origem do texto e os testes da seção 6 correspondem às tarefas 4, 5 e 9, e a origem do texto só se exerce nas partes 2 a 7, quando os trechos de gabarito são escritos. A auditoria da seção 7 corresponde às tarefas 1 e 2, com portão de aprovação, e as revogações da seção 9 estão na tarefa 12 para as duas specs, ficando as sínteses e os testes de contrato por módulo nas partes 2 a 6.

**Varredura de marcadores.** O plano não contém marcador pendente em nenhuma tarefa, e a tarefa 2, que é de julgamento, traz critérios, exemplos e comandos de verificação, enquanto a tarefa 11 depende de aprovação e descreve o que fazer para cada tipo de decisão da matriz.

**Consistência de tipos.** `carregar`, `render_template`, `render_gabarito(secoes, n, docs)`, `render_mapa(secoes, existentes, docs)`, `render_indice(existentes)`, `saidas(secoes, docs)` e `divergencias(saidas_, docs)` têm as mesmas assinaturas na tarefa 4, nos testes das tarefas 4, 7 e 9 e na descrição de `Interfaces`. `CADERNO_BLOCKS` e `CADERNO_SECTION` são definidos na tarefa 8 e citados na tarefa 12 com o mesmo nome. A decisão `remove` da tarefa 11 usa o mesmo vocabulário da tarefa 2.

**Pontos de atenção na execução.**
- A contagem mínima de 40 itens de exercício e de 40 itens de síntese, na tarefa 1, é estimativa, e o passo 4 da tarefa 1 diz como ajustá-la ao valor real.
- Os nomes dos blocos da Aula 6 no registro (tarefa 3) são provisórios. A parte 7 os confirma ou os renomeia, e o gerador só cria link para arquivo existente.
- A colocação do diagrama de contêineres (exercício 16) na seção 7 segue a spec e pode mudar na auditoria.
