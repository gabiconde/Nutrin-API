# -*- coding: utf-8 -*-
from Nutrin.Alimentacao.Model.Anamnese import Anamnese
from Nutrin.Paciente.Services.pesquisarPaciente import pesquisarPacienteById
from Nutrin.Controle.converter_data import timeToString
from Nutrin.Alimentacao.Services.Refeicao.readRefeicao import readRefeicaoAnamnese

def readAnamnese(f=False):
    anamnese = Anamnese.query.all()
    print(type(anamnese))
    if f:    
        return anamnese
    anamnese_dic = []
    for t in anamnese:
        paciente = pesquisarPacienteById(t.paciente_id)
        hora = timeToString(t.horaAcorda)
        refeicoes = readRefeicaoAnamnese(t.id)
        anamnese_dic.append({
            'id': t.id,
            'paciente': paciente,
            'qtdAtividadeFisica':t.qtdAtividadeFisica,
            'tipoExercicio': t.tipoExercicio,
            'horaAcorda':hora,
            'padraoRefeicao':t.padraoRefeicao,
            'defAlimentacaoDiaria':t.deficienciaAlimentacaoDiaria,
            'necessitaSuplementoAlimentar':t.necessitaSuplementoAlimentar,
            'retencaoLiquido':t.retencaoLiquido,
            'alergiaRemedio':t.alergiaRemedio,
            'alergiaSuplemento':t.alergiaSuplemento,
            'intoleranciaAlimentar':t.intoleranciaAlimentar,
            'problemaSaude':t.problemaSaude,
            'problemaSaudeFamilia':t.problemaSaudeFamilia,
            'medicacao':t.medicacao,
            'suplementacao':t.suplementacao,
            'refeicoes': refeicoes
        })
    return anamnese_dic

def readAnamneseById(id_anam):
    return Anamnese.query.get(id_anam)


