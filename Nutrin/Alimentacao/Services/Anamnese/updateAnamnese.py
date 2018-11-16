# -*- coding: utf-8 -*-
from Nutrin import db

def updateAnamnese(id_anamnese, qtdAtividadeFisica, tipoExercicio, horaAcorda,padraoRefeicao,deficienciaAlimentacaoDiaria,necessitaSuplementoAlimentar,retencaoLiquido,alergiaRemedio,alergiaSuplemento,intoleranciaAlimentar,problemaSaude,problemaSaudeFamilia,medicacao,suplementacao):
    from Nutrin.Alimentacao.Services.Anamnese.readAnamnese import readAnamneseById
    ana = readAnamneseById(id_anamnese)
    if ana:
        from Nutrin.Controle.converter_data import stringToTime
        hora = stringToTime(horaAcorda)
        ana.qtdAtividadeFisica = qtdAtividadeFisica
        ana.tipoExercicio = tipoExercicio
        ana.horaAcorda = hora
        ana.padraoRefeicao = padraoRefeicao
        ana.deficienciaAlimentacaoDiaria = deficienciaAlimentacaoDiaria
        ana.necessitaSuplementoAlimentar = necessitaSuplementoAlimentar
        ana.retencaoLiquido = retencaoLiquido
        ana.alergiaRemedio = alergiaRemedio
        ana.alergiaSuplemento = alergiaSuplemento
        ana.intoleranciaAlimentar = intoleranciaAlimentar
        ana.problemaSaude = problemaSaude
        ana.problemaSaudeFamilia = problemaSaudeFamilia
        ana.medicacao = medicacao
        ana.suplementacao = suplementacao
        db.session.commit()
        return True, "Anamnese atualizada com sucesso"
    return False, "Anamnese não encontrada"
