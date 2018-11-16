def alterarPaciente(username_atual, username, nome, email, celular, tipo, dataNascimento, sexo, cidade, profissao, objetivo, altura):
    from Nutrin import db
    from Nutrin.Paciente.Services.pesquisarPaciente import pesquisarPaciente
    from Nutrin.User.Services.alterarUser import alterarUser
    from Nutrin.Controle.converter_data import stringToDate

    status_paciente, p = pesquisarPaciente(username_atual, True)
    if status_paciente:
        status_user, mensagem = alterarUser(username_atual, username, nome, email, celular, tipo)
        if status_user:
            data_convertida = stringToDate(dataNascimento)
            sexo = sexo.upper()
            p.dataNascimento = data_convertida
            p.sexo = sexo
            p.cidade = cidade
            p.profissao = profissao
            p.objetivo = objetivo
            p.altura = altura
            db.session.commit()
            return True, "Paciente alterado com sucesso"
        return status_user, mensagem
    return False, "Paciente não encontrado"