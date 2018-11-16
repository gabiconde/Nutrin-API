import requests as Req

url_basica = 'http://127.0.0.1:5000'

def testeCadastroAntropometria():
    url = url_basica + '/antropometria/cadastrar'
    antropometria = {
    "peso" : 75.3,
    "braco" :29,
    "torax" :99,
    "cintura" :91,
    "abdomen" :92,
    "quadril" :0,
    "coxa" :58,
    "biceps" :9,
    "triceps" :17,
    "peito" :14,
    "subsCap" :28,
    "axilar" :22,
    "gorduraPerc" :25,
    "aguaPerc" :20.41,
    "pesoMagro" :76.47
    }
    Dados = Req.api.post(url, json=antropometria).json()
    return Dados

def testeAlterarAntropometria(antropometria_id, peso, braco, torax, cintura, abdomen, quadril, coxa, biceps, triceps, peito, subsCap, axilar, gorduraPerc, aguaPerc, pesoMagro):
    url = url_basica + '/antropometria/alterar'
    antropometria = {
    'id':antropometria_id,
    'peso' : peso,
    'braco' :braco,
    'torax' :torax,
    'cintura' :cintura,
    'abdomen' :abdomen,
    'quadril' :quadril,
    'coxa' :coxa,
    'biceps' :biceps,
    'triceps' :triceps,
    'peito' :peito,
    'subsCap' :subsCap,
    'axilar' :axilar,
    'gorduraPerc' :gorduraPerc,
    'aguaPerc' :aguaPerc,
    'pesoMagro' :pesoMagro}
    print(antropometria)
    Dados = Req.api.post(url, json=antropometria).json()
    return Dados

def testeBuscarAntropometria(id_busca):
    url = url_basica + '/antropometria/buscar/' + id_busca
    dados = Req.api.get(url).json()
    return dados

def testeDeletarAntropometria(id):
    url = url_basica + '/antropometria/deletar/' + id
    dados = Req.api.get(url).json()
    return dados



def main():
    print(testeCadastroAntropometria())
    #print(testeAlterarAntropometria(1, 53.4, 27,79,66,74,95,56,9,15,6,10,16,18.33,49.55,71.53))
    #print(testeBuscarAntropometria('2'))
    #print(testeDeletarAntropometria('2'))

main()