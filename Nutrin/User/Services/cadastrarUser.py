from Nutrin.User.Model.User import User
from Nutrin.User.Services.validar import validar_email, validar_username
from Nutrin import db

def cadastrarUser(username, password, nome, email, celular, tipo):
    if not validar_email(email):
        return False, 'Email já cadastrado'
    elif not validar_username(username):
        return False, 'Username já cadastrado'
    u = User(username, password, nome, email, celular, tipo)
    db.session.add(u)
    db.session.commit()
    return True, 'Cadastro feito com sucesso'