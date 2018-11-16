import requests as Req

url_padrao = "http://127.0.0.1:5000"

def TesteCreateTipoAtendimento(nome, preco, qtdRetorno):
    url = url_padrao + "/tipo-atendimento/cadastrar"
    tipoAtendimento = {
        "nome" : nome,
        "preco" : preco,
        "qtdRetorno" : qtdRetorno
        }
    Dados = Req.api.post(url, json=tipoAtendimento).json()
    return Dados

def TestebuscarTipoAtendimento():
    url = url_padrao + "/tipo-atendimento"
    dados = {
        "id_atual": id_atual
    }
    Dados = Req.api.get(url).json()
    return Dados

def TesteupdateTipoAtendimento(id_atendiemnto, nome, preco, qtdRetorno):
    url = url_padrao + "/tipo-atendimento/alterar"
    tipoAtendimento = {
        "id_atendiemnto" : id_atendiemnto,
        "nome" : nome,
        "preco" : preco,
        "qtdRetorno" : qtdRetorno
        }
    Dados = Req.api.post(url, json=tipoAtendimento).json()
    return Dados


def main():
    print(TesteCreateTipoAtendimento('Sala alugada', 250, 2))
    #print(TestebuscarTipoAtendimento())
    #print(TesteupdateTipoAtendimento(2, 'Residencial', 150, 1))
main() 


