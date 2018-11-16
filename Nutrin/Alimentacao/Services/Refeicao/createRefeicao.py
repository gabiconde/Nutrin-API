# -*- coding: utf-8 -*-
from Nutrin.Alimentacao.Model.Refeicao import Refeicao
from Nutrin.Alimentacao.Services.Refeicao.validaRef import validaRef


def createRefeicao(anamnese_id, tipoRefeicao_id, horario, refeicao):
    valida = validaRef(anamnese_id, tipoRefeicao_id)
    if valida:
        from Nutrin.Controle.converter_data import stringToTime
        hora = stringToTime(horario)
        refeicao = Refeicao(anamnese_id, tipoRefeicao_id, hora, refeicao)
        from Nutrin import db
        db.session.add(refeicao)
        db.session.commit()
        return True, "Refeição cadastrada"
    return False, "Refeição já está cadastrada"
