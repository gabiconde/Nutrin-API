def validar_username(username):
    from Nutrin.User.Services.listarUser import listarUser
    users = listarUser()
    for u in users:
        if username == u['username']:
            return False
    return True

def validar_email(email):
    from Nutrin.User.Services.listarUser import listarUser
    users = listarUser()
    for u in users:
        if email == u['email']:
            return False
    return True