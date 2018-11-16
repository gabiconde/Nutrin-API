from Nutrin.User.Services.buscarUser import buscarUser

def excluirUser(username):
    user = buscarUser(username, True)
    if user:
        user.ativo = False
        from Nutrin import db
        db.session.commit()
        return True
    return False

def ativarUser(username):
    user = buscarUser(username, True)
    if user:
        user.ativo = True
        from Nutrin import db
        db.session.commit()
        return True
    return False