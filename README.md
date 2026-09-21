# Projeto e Inovação em Arquitetura de Soluções

Material da disciplina de pós-graduação **Projeto e Inovação em Arquitetura de Soluções**, do IEC/PUC Minas, conduzida em seis aulas síncronas.

O site publicado está em <https://aulas-marco.github.io/projeto-arquitetura-software/>.

## Organização do repositório

| Caminho | Conteúdo |
| --- | --- |
| `docs/` | Páginas do site, uma pasta por aula, mais o caso ACME e a seção de referência |
| `overrides/` | Ajustes do tema, entre eles a página de erro própria |
| `scripts/validate_content.py` | Validador das regras editoriais do curso |
| `tests/` | Contrato de conteúdo, executado na publicação |
| `mkdocs.yml` | Configuração do site, navegação e redirecionamentos |

## Publicação

A publicação é automática. Cada envio para a `main` dispara o workflow `publicar-site.yml`, que roda os testes, o validador e a compilação em modo estrito antes de publicar no GitHub Pages.

Para trabalhar localmente:

```bash
pip install -r requirements.txt
mkdocs serve
```

## Material de origem

Os guias de arquitetura de software escritos pelo professor, usados como fonte de parte do conteúdo, ficam no repositório <https://github.com/marco-mendes/projeto-arquitetura-software> e no site <https://marco-mendes.github.io/arquitetura-software/>. Eles não são mais mantidos aqui, para que este repositório contenha apenas o material da disciplina.

O livro-texto da disciplina é LOVATT, Mark. *Solution architecture foundations*. BCS, The Chartered Institute for IT, 2021. A bibliografia completa está na [seção de referência](https://aulas-marco.github.io/projeto-arquitetura-software/referencia/bibliografia/) do site.
