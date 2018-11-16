import requests as Req

url_padrao = 'http://127.0.0.1:5000'

def testeCadastrarUser(nome):
    url = url_padrao + "/tipo-estado/cadastrar"
    tipoEstado = {
        "nome" : nome
    }
    Dados = Req.api.post(url, json=tipoEstado).json()
    return Dados

def testeReadTipoEstado():
    url = url_padrao + "/tipo-estado"
    Dados = Req.api.get(url).json()
    return Dados

def testeAlterarUser(id, nome):
    url = url_padrao + "/tipo-estado/alterar"
    dados = {
        "id" : id,
        "nome_novo" : nome
    }
    Dados = Req.api.post(url, json=dados).json()
    return Dados

def main():
    print(testeCadastrarUser('agendado'))
    #print(testeReadTipoEstado())
    #print(testeAlterarUser(1, "Solicitado"))

main()



