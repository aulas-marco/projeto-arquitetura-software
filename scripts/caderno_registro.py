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
# As seções que substituem (0 e 10) vêm de SUBSTITUI, e o exercício 24 só as preenche.
PLANO = {
    1: (1,), 2: (1,), 3: (1,), 4: (1,),
    5: (3,), 6: (3,), 7: (3, 4), 8: (2,),
    9: (6,), 10: (7,), 11: (7,), 12: (7,),
    13: (7,), 14: (7,), 15: (5,), 16: (7,),
    17: (8,), 18: (8,), 19: (8,), 20: (8,),
    21: (4,), 22: (9,), 23: (9,), 24: (),
}

# Exercício -> (aula, página do bloco relativa a docs/, título do bloco).
# Os arquivos da Aula 6 ainda não existem, e o gerador só cria link para arquivo existente.
EXERCICIOS = {
    1: (1, "modulo-1-fundamentos/bloco-1-arquitetura-de-solucoes-e-de-software.md", "Arquitetura de soluções e arquitetura de software"),
    2: (1, "modulo-1-fundamentos/bloco-2-a-solucao-como-sistema.md", "A solução como sistema e seus componentes (pessoas, áreas, processos, informação e tecnologia)"),
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

CODIGOS = ("D", "PR", "RT", "R", "RD", "CQ", "L", "P", "DD", "DL", "B", "I", "ADR", "C", "LG", "FA", "CP", "N", "T", "A")

ROTULOS_CURTOS = {
    0: "Resumo", 1: "Contexto", 2: "Partes", 3: "Requisitos", 4: "Linha de base",
    5: "Contexto C4", 6: "Princípios", 7: "Decisões", 8: "Tecnologia",
    9: "Roteiro", 10: "Pendências",
}

# Parte do caderno a que cada seção pertence: I enquadrar, II desenhar, III concretizar.
PARTES = {
    0: "I", 1: "I", 2: "I", 3: "I", 4: "I",
    5: "II", 6: "II", 7: "II",
    8: "III", 9: "III", 10: "III",
}
