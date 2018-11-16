import requests as Req

url_padrao = 'http://127.0.0.1:5000'

def testeCadastrarRef():
    url = url_padrao + "/refeicao/cadastrar"
    Refeicao = {
        "anamnese_id" : 2,
        "tipoRefeicao_id": 1,
        "horario":"06:00",
        "refeicao": "Tapioca com queijo branco e rodelas de tomate"
    }
    Refeicao2 = {
        "anamnese_id" : 1,
        "tipoRefeicao_id": 2,
        "horario":"09:00",
        "refeicao": "Frango com batata doce"
    }
    Dados = Req.api.post(url, json=Refeicao).json()
    return Dados

def testeReadRefeicao():
    url = url_padrao + "/refeicao"
    Dados = Req.api.get(url).json()
    return Dados

def testeAlterarRefeicao(id_refeicao,horario, refeicao):
    url = url_padrao + "/refeicao/alterar"
    dados = {
        "id_refeicao" : id_refeicao,
        "horario" : horario,
        "refeicao":refeicao
    }
    Dados = Req.api.post(url, json=dados).json()
    return Dados

def testeDeleteRefeicao(id_ref):
    url = url_padrao + "/refeicao/excluir/" + id_ref
    Dados = Req.api.delete(url).json()
    return Dados

def main():
    #print(testeCadastrarRef())
    #print(testeReadRefeicao())
    #print(testeAlterarRefeicao(1,"06:00","Tapioca com queijo branco e whey"))
    print(testeDeleteRefeicao('4'))

main()



