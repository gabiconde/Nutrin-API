# -*- coding: utf-8 -*-
from Nutrin import db

def updateRefeicao(id_refeicao,horario, refeicao):
    from Nutrin.Alimentacao.Services.Refeicao.readRefeicao import readRefeicaoById
    ref = readRefeicaoById(id_refeicao)
    if ref:
        from Nutrin.Controle.converter_data import stringToTime
        hora = stringToTime(horario)
        ref.horario = hora
        ref.refeicao = refeicao
        db.session.commit()
        return True, "Refeição alterada com sucesso"
    return False , "Refeição não encontrada"
