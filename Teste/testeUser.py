import requests as Req

url_padrao = "http://127.0.0.1:5000"

def testeCadastrarUser():
    url = url_padrao + "/usuarios/cadastrar"
    user2 = {
        "username":'admin',
        "password":"0123456",
        'nome':'Monkey D. Luffy',
        'email':'luffy@gmail.com',
        'celular':'11955554662',
        'tipo':'A'
        }
    user = {
        "username":'Aline',
        "password":"aline.nutri",
        'nome':'Aline nutri',
        'email':'lady@gmail.com',
        'celular':'11986532415',
        'tipo':'N'
        }
    Dados = Req.api.post(url, json=user2).json()
    return Dados

def testeAlterarSenha():
    url = url_padrao + "/usuario/alterar-senha"
    user = {
        "username": 'admin',
        "password_atual": '0123456',
        "password_nova": '12345'
        }
    Dados = Req.api.put(url, json=user).json()
    return Dados

def testeAlterarUser():
    url = url_padrao + "/usuario/alterar-user"
    user = {
        "username_atual":"gabi",
        "username":'gabiconde',
        'nome':'Gabi Conde',
        'email':'gabiconde@gmail.com',
        'celular':'11955554662',
        'tipo':'A'
        }
    Dados = Req.api.put(url, json=user).json()
    return Dados

def testeListarUser():
    url = url_padrao + "/usuarios"
    Dados = Req.api.get(url).json()
    return Dados

def testeBuscarUser(username):
    url = url_padrao + "/usuario/" + username
    Dados = Req.api.get(url).json()
    return Dados

def testeExcluirUser(username):
    url = url_padrao + "/usuario/desativar/" + username
    Dados = Req.api.get(url).json()
    return Dados 

def testeAtivarUser(username):
    url = url_padrao + "/usuario/ativar/" + username
    Dados = Req.api.get(url).json()
    return Dados

def main():
    print(testeCadastrarUser())
    #print(testeListarUser())
    #print(testeBuscarUser('Aline'))
    #print(testeAlterarUser())
    #print(testeAlterarSenha())
    #print(testeExcluirUser('Aline'))
    #print(testeAtivarUser('Aline'))
main()