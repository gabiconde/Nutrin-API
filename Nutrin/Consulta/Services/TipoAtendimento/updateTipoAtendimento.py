def updateTipoAtendimento(id_atendiemnto, nome, preco, qtdRetorno):
    from Nutrin.Consulta.Services.TipoAtendimento.readTipoAtendimento import readTipoAtendimento
    status, tipo_atendimento = readTipoAtendimento(True, id_atendiemnto)
    nome = nome.upper()
    if tipo_atendimento.nome != nome:
        from Nutrin.Consulta.Services.TipoAtendimento.validarNome import validarNome
        if not validarNome(nome):
            return False, "Nome do tipo atendimento já existe"
    tipo_atendimento.nome = nome
    tipo_atendimento.preco = preco
    tipo_atendimento.qtdRetorno = qtdRetorno
    from Nutrin import db
    db.session.commit()
    return True, "Tipo atendimento alterado com sucesso"


    
