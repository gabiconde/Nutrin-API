from Nutrin import db
from Nutrin.User.Services.buscarUser import buscarUser

def alterarUser(username_atual, username, nome, email, celular, tipo):
    u = buscarUser(username_atual, True)
    if u:
        if u.username != username:
            from Nutrin.User.Services.validar import validar_username
            if not validar_username(username):
                return False, "Username já cadastrado"
        if u.email != email:
            from Nutrin.User.Services.validar import validar_email
            if not validar_email(email):
                return False, "Email já cadastrado"
        u.username = username
        u.nome = nome
        u.email = email
        u.celular = celular
        u.tipo = tipo
        db.session.commit()
        return True, "Usuario alterado com sucesso"
    return False, "Usuario não encontrado"