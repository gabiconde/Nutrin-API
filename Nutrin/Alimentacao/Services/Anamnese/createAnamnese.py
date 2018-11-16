# -*- coding: utf-8 -*-
from Nutrin.Alimentacao.Model.Anamnese import Anamnese
from Nutrin.Alimentacao.Services.Anamnese.validaPaciente import validaPaciente

def createAnamnese(paciente_id, qtdAtividadeFisica, tipoExercicio, horaAcorda,padraoRefeicao,deficienciaAlimentacaoDiaria,necessitaSuplementoAlimentar,retencaoLiquido,alergiaRemedio,alergiaSuplemento,intoleranciaAlimentar,problemaSaude,problemaSaudeFamilia,medicacao,suplementacao):
    if validaPaciente(paciente_id):  
        from Nutrin.Controle.converter_data import stringToTime
        hora = stringToTime(horaAcorda)
        print(hora)
        anamnese = Anamnese(paciente_id, qtdAtividadeFisica, tipoExercicio, hora,padraoRefeicao,deficienciaAlimentacaoDiaria,necessitaSuplementoAlimentar,retencaoLiquido,alergiaRemedio,alergiaSuplemento,intoleranciaAlimentar,problemaSaude,problemaSaudeFamilia,medicacao,suplementacao)
        from Nutrin import db
        db.session.add(anamnese)
        db.session.commit()
        return True, "Anamnese cadastrada" 
    return False, "O paciente já possui uma anamnese"
