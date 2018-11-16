import requests as Req

url_padrao ="http://127.0.0.1:5000"

def testeCadastrarAnamnese():
    url = url_padrao + "/anamnese/cadastrar"
    anamnese = {
   "paciente_id" :  1,
   "qtdAtividadeFisica" :  5,
   "tipoExercicio" :"musculação e muay thai",
   "horaAcorda" :"05:30",
   "padraoRefeicao" :"Não sei o que vai nesse campo",
   "deficienciaAlimentacaoDiaria" :  None,
   "necessitaSuplementoAlimentar" :"Precisa de whey protein, bcaa e glutamina",
   "retencaoLiquido" :  False,
   "alergiaRemedio" :  None,
   "alergiaSuplemento" :  None,
   "intoleranciaAlimentar" :"Não gotsa de coco, amendoim, castanhas nem palmito",
   "problemaSaude" :  None,
   "problemaSaudeFamilia" :  None,
   "medicacao" :"Toma anti",
   "suplementacao" :"Faz uso de whey iso e bcaa no pre e pos treino"
    }

    anamnese2 = {
   "paciente_id" :  2,
   "qtdAtividadeFisica" :  0,
   "tipoExercicio" :"levantamento de garfo",
   "horaAcorda" :"10:30",
   "padraoRefeicao" :"Não sei o que vai nesse campo",
   "deficienciaAlimentacaoDiaria" :  "Come porra nenhuma",
   "necessitaSuplementoAlimentar" :"Precisa de vitaminas",
   "retencaoLiquido" :  True,
   "alergiaRemedio" :  None,
   "alergiaSuplemento" :  None,
   "intoleranciaAlimentar" :"Intolerante a gluten",
   "problemaSaude" :  None,
   "problemaSaudeFamilia" : "cardio",
   "medicacao" :None,
   "suplementacao" :"Não utiliza"
    }
    Dados = Req.api.post(url, json=anamnese).json()
    return Dados

def testeReadAnamnese():
    url = url_padrao + "/anamnese"
    Dados = Req.api.get(url).json()
    return Dados

def testeAlterarAnamnese():
#def testeAlterarAnamnese(id_anamnese, qtdAtividadeFisica, tipoExercicio, horaAcorda,padraoRefeicao,deficienciaAlimentacaoDiaria,necessitaSuplementoAlimentar,retencaoLiquido,alergiaRemedio,alergiaSuplemento,intoleranciaAlimentar,problemaSaude,problemaSaudeFamilia,medicacao,suplementacao):
    url = url_padrao + "/anamnese/alterar"
    dados = {
   "anamnese_id" :  1,
   "qtdAtividadeFisica" :  6,
   "tipoExercicio" :"musculação, muay thai, yoga",
   "horaAcorda" :"05:30",
   "padraoRefeicao" :"Não sei o que vai nesse campo",
   "deficienciaAlimentacaoDiaria" :  None,
   "necessitaSuplementoAlimentar" :"Precisa de whey protein, bcaa e glutamina",
   "retencaoLiquido" :  False,
   "alergiaRemedio" :  None,
   "alergiaSuplemento" :  None,
   "intoleranciaAlimentar" :"Não gotsa de coco, amendoim, castanhas nem palmito",
   "problemaSaude" :  None,
   "problemaSaudeFamilia" :  None,
   "medicacao" :"Toma anti",
   "suplementacao" :"Faz uso de whey iso e bcaa no pre e pos treino"
    }
    Dados = Req.api.post(url, json=dados).json()
    return Dados

def testeDeleteAnamnese(id_anamnese):
    url = url_padrao + "/anamnese/excluir/" + id_anamnese
    Dados = Req.api.delete(url).json()
    return Dados

def main():
    print(testeCadastrarAnamnese())
    #print(testeReadAnamnese())
    #print(testeAlterarAnamnese())
    #print(testeDeleteAnamnese('2'))

main()



