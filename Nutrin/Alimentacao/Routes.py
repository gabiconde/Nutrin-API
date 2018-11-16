# -*- coding: utf-8 -*-
from flask import jsonify, request
from Nutrin import app
from Nutrin import response


#Tipo Refeição

@app.route('/tipo-refeicao/cadastrar', methods=['POST'])
def cadastrarTipoRefeicao():
    from Nutrin.Alimentacao.Services.TipoRefeicao.createTipoRefeicao import createTipoRefeicao 
    dados = request.get_json()
    nome = dados["nome"]
    status, mensagem = createTipoRefeicao(nome)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('/tipo-refeicao', methods=['GET'])
def buscarTipoRefeicao():
    from Nutrin.Alimentacao.Services.TipoRefeicao.readTipoRefeicao import readTipoRefeicao 
    response["Status"] = "Sucesso"
    response["Dados"] = readTipoRefeicao()
    response["Mensagem"] = "Tipos de refeição"
    return jsonify(response)

@app.route('/tipo-refeicao/alterar', methods=['POST'])
def alterarTipoRefeicao():
    from Nutrin.Alimentacao.Services.TipoRefeicao.updateTipoRefeicao import updateTipoRefeicao 
    dados = request.get_json()
    id_tipoRef = dados['id']
    nome = dados["nome_novo"]
    status, mensagem = updateTipoRefeicao(id_tipoRef,nome)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

# Refeições

@app.route('/refeicao/cadastrar', methods=['POST'])
def cadastrarRefeicao():
    from Nutrin.Alimentacao.Services.Refeicao.createRefeicao import createRefeicao 
    dados = request.get_json()
    anamnese_id = dados["anamnese_id"]
    tipoRefeicao_id = dados["tipoRefeicao_id"]
    horario = dados["horario"]
    refeicao = dados['refeicao']
    status, mensagem = createRefeicao(anamnese_id, tipoRefeicao_id, horario, refeicao)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('/refeicao', methods=['GET'])
def buscarRefeicao():
    from Nutrin.Alimentacao.Services.Refeicao.readRefeicao import readRefeicao 
    response["Status"] = "Sucesso"
    response["Dados"] = readRefeicao()
    response["Mensagem"] = "Lista refeições cadastradas"
    return jsonify(response)

@app.route('/refeicao/alterar', methods=['POST'])
def alterarRefeicao():
    from Nutrin.Alimentacao.Services.Refeicao.updateRefeicao import updateRefeicao 
    dados = request.get_json()
    id_refeicao = dados["id_refeicao"]
    horario = dados["horario"]
    refeicao = dados['refeicao']
    status, mensagem = updateRefeicao(id_refeicao,horario, refeicao)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('/refeicao/excluir/<id_refeicao>', methods=['DELETE'])
def excluirRefeicao(id_refeicao):
    from Nutrin.Alimentacao.Services.Refeicao.deleteRefeicao import deleteRefeicao 
    status, mensagem = deleteRefeicao(id_refeicao)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

#Anamnese

@app.route('/anamnese/cadastrar', methods=['POST'])
def cadastrarAnamnese():
    from Nutrin.Alimentacao.Services.Anamnese.createAnamnese import createAnamnese 
    dados = request.get_json()
    paciente_id = dados["paciente_id"]
    qtdAtividadeFisica = dados["qtdAtividadeFisica"]
    tipoExercicio = dados["tipoExercicio"]
    horaAcorda = dados['horaAcorda']
    padraoRefeicao = dados["padraoRefeicao"]
    deficienciaAlimentacaoDiaria = dados["deficienciaAlimentacaoDiaria"]
    necessitaSuplementoAlimentar = dados["necessitaSuplementoAlimentar"]
    retencaoLiquido = dados['retencaoLiquido']
    alergiaRemedio = dados["alergiaRemedio"]
    alergiaSuplemento = dados["alergiaSuplemento"]
    intoleranciaAlimentar = dados["intoleranciaAlimentar"]
    problemaSaude = dados['problemaSaude']
    problemaSaudeFamilia = dados["problemaSaudeFamilia"]
    medicacao = dados["medicacao"]
    suplementacao = dados['suplementacao']

    status, mensagem = createAnamnese(paciente_id, qtdAtividadeFisica, tipoExercicio, horaAcorda,padraoRefeicao,deficienciaAlimentacaoDiaria,necessitaSuplementoAlimentar,retencaoLiquido,alergiaRemedio,alergiaSuplemento,intoleranciaAlimentar,problemaSaude,problemaSaudeFamilia,medicacao,suplementacao)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('/anamnese', methods=['GET'])
def buscarAnamnese():
    from Nutrin.Alimentacao.Services.Anamnese.readAnamnese import readAnamnese 
    response["Status"] = "Sucesso"
    response["Dados"] = readAnamnese()
    response["Mensagem"] = "Listagem anamneses"
    return jsonify(response)

@app.route('/anamnese/alterar', methods=['POST'])
def alterarAnamnese():
    from Nutrin.Alimentacao.Services.Anamnese.updateAnamnese import updateAnamnese
    dados = request.get_json()
    id_anamnese = dados["anamnese_id"]
    qtdAtividadeFisica = dados["qtdAtividadeFisica"]
    tipoExercicio = dados["tipoExercicio"]
    horaAcorda = dados['horaAcorda']
    padraoRefeicao = dados["padraoRefeicao"]
    deficienciaAlimentacaoDiaria = dados["deficienciaAlimentacaoDiaria"]
    necessitaSuplementoAlimentar = dados["necessitaSuplementoAlimentar"]
    retencaoLiquido = dados['retencaoLiquido']
    alergiaRemedio = dados["alergiaRemedio"]
    alergiaSuplemento = dados["alergiaSuplemento"]
    intoleranciaAlimentar = dados["intoleranciaAlimentar"]
    problemaSaude = dados['problemaSaude']
    problemaSaudeFamilia = dados["problemaSaudeFamilia"]
    medicacao = dados["medicacao"]
    suplementacao = dados['suplementacao']
    status, mensagem = updateAnamnese(id_anamnese, qtdAtividadeFisica, tipoExercicio, horaAcorda,padraoRefeicao,deficienciaAlimentacaoDiaria,necessitaSuplementoAlimentar,retencaoLiquido,alergiaRemedio,alergiaSuplemento,intoleranciaAlimentar,problemaSaude,problemaSaudeFamilia,medicacao,suplementacao)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('/anamnese/excluir/<id_anamnese>', methods=['DELETE'])
def excluirAnamnese(id_anamnese):
    from Nutrin.Alimentacao.Services.Anamnese.deleteAnamnese import deleteAnamnese 
    status, mensagem = deleteAnamnese(id_anamnese)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)


# @app.route("/tipo-estado/cadastrar", methods=["POST"])
# def CreateTipoEstadoRoute():
#     from Nutrin.Consulta.Services9.TipoEstado.createTipoEstado import createTipoEstado
#     dados = request.get_json(force=True)
#     nome = dados["nome"]
#     status, mensagem = createTipoEstado(nome)
#     if status:
#         response["Status"] = "Sucesso"
#         response["Dados"] = ""
#         response["Mensagem"] = mensagem
#         return jsonify(response)
#     response["Status"] = "Erro"
#     response["Dados"] = ""
#     response["Mensagem"] = mensagem
#     return jsonify(response)
