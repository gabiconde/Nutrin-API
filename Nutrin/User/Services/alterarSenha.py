from Nutrin import db
from Nutrin.User.Services.buscarUser import buscarUser

def alterarSenha(username,senha_atual,senha_nova):
    u = buscarUser(username, True)
    if u:
        if u.password == senha_atual:
            u.password = senha_nova
            db.session.commit()
            return True, "Senha alterada com sucesso"
        return False, 'Digite a senha atual valida'
    return False, 'Usuario não encontrado'
    
    
    
