from Nutrin.User.Services.listarUser import listarUser
def login(username, password):
    users = listarUser()
    user = False
    for u in users:
        if username == u["username"]:
            user = u
            break
    if user and user["password"] == password:
        return True
    else:
        return False