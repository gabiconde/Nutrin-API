import requests as Req

url_padrao = 'http://127.0.0.1:5000'

def testeCadastrarTipoRef(nome):
    url = url_padrao + "/tipo-refeicao/cadastrar"
    tipoEstado = {
        "nome" : nome
    }
    Dados = Req.api.post(url, json=tipoEstado).json()
    return Dados

def testeReadTipoRefeicao():
    url = url_padrao + "/tipo-refeicao"
    Dados = Req.api.get(url).json()
    return Dados

def testeAlterarTipoRefeicao(id, nome):
    url = url_padrao + "/tipo-refeicao/alterar"
    dados = {
        "id" : id,
        "nome_novo" : nome
    }
    Dados = Req.api.post(url, json=dados).json()
    return Dados

def main():
    #print(testeCadastrarTipoRef('Lanche manhã'))
    #print(testeReadTipoRefeicao())
    #print(testeAlterarTipoRefeicao(2, "Almoço"))

main()



