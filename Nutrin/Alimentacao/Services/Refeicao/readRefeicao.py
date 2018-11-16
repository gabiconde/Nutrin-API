# -*- coding: utf-8 -*-
from Nutrin.Alimentacao.Model.Refeicao import Refeicao
from Nutrin.Alimentacao.Model.TipoRefeicao import TipoRefeicao
from Nutrin.Controle.converter_data import timeToString
from Nutrin.Alimentacao.Services.TipoRefeicao.readTipoRefeicao import readTipoRefeicaoById
def readRefeicao(f=False):
    refeicao = Refeicao.query.all()
    #print(type(refeicao))
    if f:    
        return refeicao
    refeicao_dic = []
    for t in refeicao:
        tipoRef = readTipoRefeicaoById(t.tipoRefeicao_id)
        hora = timeToString(t.horario)
        refeicao_dic.append({
            'id': t.id,
            'anamnese_id': t.anamnese_id,
            'tipoRefeicao':tipoRef.nome,
            'horario':hora,
            'refeicao':t.refeicao
        })
    return refeicao_dic

def readRefeicaoById(id_Ref):
    return Refeicao.query.get(id_Ref)

def readRefeicaoAnamnese(id_anamnese):
    lista = readRefeicao()
    refs =[]
    for r in lista:
        print(type(r["anamnese_id"]))
        print(type(id_anamnese))
        if r["anamnese_id"] == int(id_anamnese):
            refs.append(r)
    return refs




