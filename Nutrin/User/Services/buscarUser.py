def buscarUser(username, f = False):
    from Nutrin.User.Model.User import User
    from Nutrin import db
    u = db.session.query(User).filter_by(username = username).first()
    if u:
        if f:
            return u
        else:
            user = {
                'id': u.id,
                'username': u.username,
                'password' : u.password,
                'nome': u.nome,
                'email': u.email,
                'celular': u.celular,
                'tipo': u.tipo
            }
            return user
    return False