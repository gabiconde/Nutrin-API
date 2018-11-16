# -*- coding: utf-8 -*-
from Nutrin import db

def updateTipoRefeicao(id_tipo_ref, novo_nome):
    from Nutrin.Alimentacao.Services.TipoRefeicao.readTipoRefeicao import readTipoRefeicao
    from Nutrin.Alimentacao.Services.TipoRefeicao.validarNome import validarNome
    novo_nome = novo_nome.upper()
    tipos_ref = readTipoRefeicao(True)
    if validarNome(novo_nome):
        for t in tipos_ref:
            if t.id == id_tipo_ref:
                t.nome = novo_nome
                db.session.commit()
                return True, "Tipo refeição alterado com sucesso"
        return False , "Tipo refeição não encontrado"
    return False, "Nome do tipo refeição ja existe"