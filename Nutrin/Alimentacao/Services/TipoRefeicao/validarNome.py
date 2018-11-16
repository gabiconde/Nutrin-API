# -*- coding: utf-8 -*-
def validarNome(nome):
    from Nutrin.Alimentacao.Services.TipoRefeicao.readTipoRefeicao import readTipoRefeicao
    tipos_ref = readTipoRefeicao(True)
    for t in tipos_ref:
        if t.nome == nome:
            return False
    return True