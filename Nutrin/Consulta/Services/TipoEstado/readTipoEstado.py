from Nutrin.Consulta.Model.TipoEstado import TipoEstado

def readTipoEstado(f=False):
    tipos_estado = TipoEstado.query.all()
    print(type(tipos_estado))
    if f:    
        return tipos_estado
    tipos_estado_dic = []
    for t in tipos_estado:
        tipos_estado_dic.append({
            'id': t.id,
            'nome': t.nome
        })
    return tipos_estado_dic

def readEstadoById(id_estado):
    return TipoEstado.query.get(id_estado)
     
