from flask import jsonify, request
from Nutrin import app, response


# Tipo Estado

@app.route("/tipo-estado/cadastrar", methods=["POST"])
def CreateTipoEstadoRoute():
    from Nutrin.Consulta.Services.TipoEstado.createTipoEstado import createTipoEstado
    dados = request.get_json(force=True)
    nome = dados["nome"]
    status, mensagem = createTipoEstado(nome)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route("/tipo-estado", methods=["GET"])
def ReadTipoEstadoRoute():
    from Nutrin.Consulta.Services.TipoEstado.readTipoEstado import readTipoEstado
    response['Status'] = "Sucesso"
    response['Dados'] = readTipoEstado()
    response['Mensagem'] = "Tipos de estado listado com sucesso"
    return jsonify(response)

@app.route("/tipo-estado/alterar", methods=["POST"])
def UpdateTipoEstadoRoute():
    from Nutrin.Consulta.Services.TipoEstado.updateTipoEstado import updateTipoEstado
    dados = request.get_json()
    id_estado = dados["id"]
    nome_novo = dados["nome_novo"]
    status, mensagem = updateTipoEstado(id_estado, nome_novo)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)
    

# Tipo Atendimento

@app.route('/tipo-atendimento/cadastrar', methods=["POST"])
def CreateTipoAtendimentoRoute():
    from Nutrin.Consulta.Services.TipoAtendimento.createTipoAtendimento import createTipoAtendimento
    dados = request.get_json()
    nome = dados["nome"]
    preco = dados["preco"]
    qtdRetorno = dados["qtdRetorno"]
    status, mensagem = createTipoAtendimento(nome, preco, qtdRetorno)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)
  
  
@app.route('/tipo-atendimento', methods=["GET"])
def BuscarTipoAtendimentoRoute():
    from Nutrin.Consulta.Services.TipoAtendimento.readTipoAtendimento import readTipoAtendimento
    status, dados = readTipoAtendimento()
    response["Status"] = "Erro"
    response["Dados"] = dados
    response["Mensagem"] = ""
    return jsonify(response)
        
@app.route('/tipo-atendimento/alterar', methods=["POST"])
def UpdateTipoAtendimentoRoute():
    from Nutrin.Consulta.Services.TipoAtendimento.updateTipoAtendimento import updateTipoAtendimento
    dados = request.get_json()
    id_atendiemnto = dados["id_atendiemnto"]
    nome = dados["nome"]
    preco = dados["preco"]
    qtdRetorno = dados["qtdRetorno"]
    status, mensagem = updateTipoAtendimento(id_atendiemnto, nome, preco, qtdRetorno)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)
  
# Antropometria

@app.route('/antropometria/cadastrar', methods=["POST"])
def createAntropometriaRoute():
    from Nutrin.Consulta.Services.Antropometria.createAntropometria import createAntropometria
    dados = request.get_json()
    peso = dados["peso"]
    braco = dados["braco"]
    torax = dados["torax"]
    cintura = dados["cintura"]
    abdomen = dados["abdomen"]
    quadril = dados["quadril"]
    coxa = dados["coxa"]
    biceps = dados["biceps"]
    triceps = dados["triceps"]
    peito = dados["peito"]
    subsCap = dados["subsCap"]
    axilar = dados["axilar"]
    gorduraPerc = dados["gorduraPerc"]
    aguaPerc = dados["aguaPerc"]
    pesoMagro = dados["pesoMagro"]
    status, mensagem = createAntropometria(peso, braco, torax, cintura, abdomen, quadril, coxa, biceps, triceps, peito, subsCap, axilar, gorduraPerc, aguaPerc, pesoMagro)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = mensagem[1]
        response["Mensagem"] = mensagem[0]
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = mensagem[1]
    response["Mensagem"] = mensagem[0]
    return jsonify(response)
        

@app.route('/antropometria/alterar', methods=["POST"])
def updateAntropometriaRoute():
    from Nutrin.Consulta.Services.Antropometria.updateAntropometria import updateAntropometria
    dados = request.get_json()
    antropometria_id = dados["id"]
    peso = dados["peso"]
    braco = dados["braco"]
    torax = dados["torax"]
    cintura = dados["cintura"]
    abdomen = dados["abdomen"]
    quadril = dados["quadril"]
    coxa = dados["coxa"]
    biceps = dados["biceps"]
    triceps = dados["triceps"]
    peito = dados["peito"]
    subsCap = dados["subsCap"]
    axilar = dados["axilar"]
    gorduraPerc = dados["gorduraPerc"]
    aguaPerc = dados["aguaPerc"]
    pesoMagro = dados["pesoMagro"]
    status, mensagem = updateAntropometria(antropometria_id, peso, braco, torax, cintura, abdomen, quadril, coxa, biceps, triceps, peito, subsCap, axilar, gorduraPerc, aguaPerc, pesoMagro)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('/antropometria/buscar/<ID>', methods=["GET"])
def readAntropometriaRoute(ID):
    id_antro = int(ID)
    from Nutrin.Consulta.Services.Antropometria.readAntropometria import readAntropometria
    status, mensagem = readAntropometria(id_antro)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)
  

@app.route('/antropometria/deletar/<ID>', methods=["GET"])
def deleteAntropometriaRoute(ID):
    from Nutrin.Consulta.Services.Antropometria.deleteAntropometria import deleteAntropometria
    status, mensagem = deleteAntropometria(ID)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)


#Horarios

@app.route('/horario/cadastrar', methods=['POST'])
def createHorarioRoute():
    dados = request.get_json()
    from Nutrin.Consulta.Services.Horarios.createHorario import createHorario
    status, mensagem = createHorario(dados['data'],dados['horaI'],dados['horaF'])
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('/horario/alterar', methods=['PUT'])
def updateHorarioRoute():
    dados = request.get_json()
    from Nutrin.Consulta.Services.Horarios.updateHorario import updateHorario
    status, mensagem = updateHorario(dados['id'],dados['horaI'],dados['horaF'])
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('/horario/deletar/<id>', methods=['GET'])
def deleteHorarioRoute(id):
    from Nutrin.Consulta.Services.Horarios.deleteHorario import deleteHorario
    status, mensagem = deleteHorario(id)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

    
@app.route('/horarios', methods=['GET'])
def listHorarioRoute():
    from Nutrin.Consulta.Services.Horarios.listHorario import listHorario
    response["Status"] = "Sucesso"
    response["Dados"] = listHorario()
    response["Mensagem"] = ""
    return jsonify(response)
    
@app.route('/horarios/<dia>', methods=['GET'])
def readHorarioRoute(dia):
    from Nutrin.Consulta.Services.Horarios.listHorario import listHorarioData
    status, mensagem = listHorarioData(dia)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = mensagem
        response["Mensagem"] = ""
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = []
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('/horarios/listaDisp', methods=['GET'])
def listHorarioDispRoute():
    from Nutrin.Consulta.Services.Horarios.listHorario import listDisponiveis
    mensagem = listDisponiveis()
    response["Status"] = "Sucesso"
    response["Dados"] = mensagem
    response["Mensagem"] = ''
    return jsonify(response)

#Horarios ocupados

# @app.route('/ocupado/cadastrar', methods=['POST'])
# def createOcupadoRoute():
#     dados = request.get_json()
#     from Nutrin.Consulta.Services.Ocupado.createOcupado import createOcupado
#     status, mensagem = createOcupado(dados['horario_id'],dados['horaI'],dados['horaF'])
#     if status:
#         response["Status"] = "Sucesso"
#         response["Dados"] = ""
#         response["Mensagem"] = mensagem
#         return jsonify(response)
#     response["Status"] = "Erro"
#     response["Dados"] = ""
#     response["Mensagem"] = mensagem
#     return jsonify(response)

@app.route('/ocupado/alterar', methods=['PUT'])
def updateOcupadoRoute():
    dados = request.get_json()
    from Nutrin.Consulta.Services.Ocupado.updateOcupado import updateOcupado
    status, mensagem = updateOcupado(dados['id'],dados['horaI'],dados['horaF'])
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

# @app.route('/ocupado/deletar/<id>', methods=['DELETE'])
# def deleteOcupadoRoute(id):
#     from Nutrin.Consulta.Services.Ocupado.deleteOcupado import deleteOcupado
#     status, mensagem = deleteOcupado(id)
#     if status:
#         response["Status"] = "Sucesso"
#         response["Dados"] = ""
#         response["Mensagem"] = mensagem
#         return jsonify(response)
#     response["Status"] = "Erro"
#     response["Dados"] = ""
#     response["Mensagem"] = mensagem
#     return jsonify(response)
    
@app.route('/ocupados', methods=['GET'])
def listOcupadoRoute():
    from Nutrin.Consulta.Services.Ocupado.readOcupado import readAllOcupado
    status, mensagem = readAllOcupado()
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = mensagem
        response["Mensagem"] = ""
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = []
    response["Mensagem"] = mensagem
    return jsonify(response)

# Consultas

@app.route('/consulta/cadastrar', methods=["POST"])
def CreateConsultaRoute():
    from Nutrin.Consulta.Services.Consulta.createConsulta import createConsulta
    dados = request.get_json()
    paciente_id = dados["paciente_id"]
    tipoAtendimento_id = dados["tipoAtendimento_id"]
    data = dados["data"]
    horaI = dados["horaI"]
    horaF = dados["horaF"]
    tipoEstado_id = dados["tipoEstado_id"]
    status, mensagem = createConsulta(paciente_id, tipoAtendimento_id, data, horaI, horaF, tipoEstado_id)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('/consultas', methods=["GET"])
def listConsultasRoute():
    from Nutrin.Consulta.Services.Consulta.listConsulta import listConsultas
    response["Status"] = "Sucesso"
    response["Dados"] = listConsultas()
    response["Mensagem"] = 'Consultas agendadas'
    return jsonify(response)

@app.route('/consultas/paciente/<id_paciente>', methods=["GET"])
def listConsultasPacientesRoute(id_paciente):
    from Nutrin.Consulta.Services.Consulta.listConsulta import listByColumn
    response["Status"] = "Sucesso"
    response["Dados"] = listByColumn('paciente_id',id_paciente)
    response["Mensagem"] = 'Consultas agendadas para o paciente'
    return jsonify(response)

@app.route('/consultas/horario/<id_horario>', methods=["GET"])
def listConsultasHorariosRoute(id_horario):
    from Nutrin.Consulta.Services.Consulta.listConsulta import listByColumn
    response["Status"] = "Sucesso"
    response["Dados"] = listByColumn('horario_id',id_horario)
    response["Mensagem"] = 'Consultas agendadas no dia desejado'
    return jsonify(response)

@app.route('/consultas/alterar', methods=['PUT'])
def updateConsultaRoute():
    dados = request.get_json()
    from Nutrin.Consulta.Services.Consulta.updateConsulta import updateConsulta
    consulta_id = dados["consulta_id"]
    paciente_id = dados["paciente_id"]
    tipoAtendimento_id = dados["tipoAtendimento_id"]
    tipoEstado_id = dados["tipoEstado_id"]
    pagamento = dados["pagamento"]
    status, mensagem = updateConsulta(consulta_id,paciente_id,tipoAtendimento_id,tipoEstado_id,pagamento)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('/consultas/alterarHorario', methods=['PUT'])
def updateHorarioConsultaRoute():
    dados = request.get_json()
    from Nutrin.Consulta.Services.Consulta.updateConsulta import updateHorarioConsulta
    consulta_id = dados["consulta_id"]
    horario_id = dados["horario_id"]
    data = dados["data"]
    horaI = dados["horaI"]
    horaF = dados["horaF"]
    status, msg = updateHorarioConsulta(consulta_id, horario_id,data,horaI,horaF)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = msg
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = msg
    return jsonify(response)

@app.route('/consultas/alterarId', methods=['PUT'])
def demarcarConsultaRoute():
    dados = request.get_json()
    id_consulta = dados['id_consulta']
    column = dados['column']
    id_column = dados['id_column']
    from Nutrin.Consulta.Services.Consulta.updateConsulta import updateUmConsulta
    status, msg = updateUmConsulta(id_consulta, column, id_column)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = msg
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = msg
    return jsonify(response)

@app.route('/consultas/delete/<id_consulta>', methods=['delete'])
def deletarConsultaRoute(id_consulta):
    from Nutrin.Consulta.Services.Consulta.deleteConsulta import deleteConsulta
    status, msg = deleteConsulta(id_consulta)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = msg
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = msg
    return jsonify(response)

  
    
    





