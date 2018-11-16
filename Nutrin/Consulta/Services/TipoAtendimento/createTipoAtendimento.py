def createTipoAtendimento(nome, preco, qtdRetorno):
    nome = nome.upper()
    from Nutrin.Consulta.Model.TipoAtendimento import TipoAtendimento
    tipo_atendimento = TipoAtendimento(nome, preco, qtdRetorno)
    from Nutrin.Consulta.Services.TipoAtendimento.validarNome import validarNome
    if validarNome(nome):
        from Nutrin import db
        db.session.add(tipo_atendimento)
        db.session.commit()
        return True, "tipo atendimento cadastrado com sucesso"
    return False, "tipo atendimento ja cadastrado"
