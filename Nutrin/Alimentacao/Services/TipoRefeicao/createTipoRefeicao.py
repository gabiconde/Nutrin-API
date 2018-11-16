# -*- coding: utf-8 -*-
from Nutrin.Alimentacao.Model.TipoRefeicao import TipoRefeicao
from Nutrin.Alimentacao.Services.TipoRefeicao.validarNome import validarNome


def createTipoRefeicao(nome):
    nome = nome.upper()
    if validarNome(nome):
        tipoRef = TipoRefeicao(nome)
        from Nutrin import db
        db.session.add(tipoRef)
        db.session.commit()
        return True, "Tipo Refeição cadastrado"
    return False, "Tipo já cadastrado"
