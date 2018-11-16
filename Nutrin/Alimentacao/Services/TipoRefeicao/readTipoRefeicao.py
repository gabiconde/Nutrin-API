# -*- coding: utf-8 -*-
from Nutrin.Alimentacao.Model.TipoRefeicao import TipoRefeicao

def readTipoRefeicao(f=False):
    tipos_ref = TipoRefeicao.query.all()
    print(type(tipos_ref))
    if f:    
        return tipos_ref
    tipos_ref_dic = []
    for t in tipos_ref:
        tipos_ref_dic.append({
            'id': t.id,
            'nome': t.nome
        })
    return tipos_ref_dic

def readTipoRefeicaoById(id_tipoRef):
    return TipoRefeicao.query.get(id_tipoRef)
     
