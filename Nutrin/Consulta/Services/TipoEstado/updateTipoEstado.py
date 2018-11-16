from Nutrin import db

def updateTipoEstado(id_tipo_estado, novo_nome):
    from Nutrin.Consulta.Services.TipoEstado.readTipoEstado import readTipoEstado
    from Nutrin.Consulta.Services.TipoEstado.validarNome import validarNome
    novo_nome = novo_nome.upper()
    tipos_estados = readTipoEstado(True)
    if validarNome(novo_nome):
        for t in tipos_estados:
            if t.id == id_tipo_estado:
                t.nome = novo_nome
                db.session.commit()
                return True, "Tipo estado alterado com sucesso"
        return False , "Tipo estado não encontrado"
    return False, "Nome do tipo estado ja existe"