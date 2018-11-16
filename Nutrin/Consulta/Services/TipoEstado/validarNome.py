def validarNome(nome):
    from Nutrin.Consulta.Services.TipoEstado.readTipoEstado import readTipoEstado
    tipos_estado = readTipoEstado(True)
    for t in tipos_estado:
        if t.nome == nome:
            return False
    return True