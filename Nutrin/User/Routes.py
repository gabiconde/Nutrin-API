from flask import jsonify, request
from Nutrin import app, response

@app.route("/login", methods=["POST"])
def LoginRoute():
    from Nutrin.User.Services.login import login
    dados = request.get_json()
    username = dados["username"]
    password = dados["password"]
    l = login(username, password)
    if l:
        response["Status"] = "Sucesso"
        response["Dados"] = l
        response["Mensagem"] = "Login feito com sucesso"
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = l
    response["Mensagem"] = "O usuario ou a senha estão errados"
    return jsonify(response)

@app.route("/usuarios", methods=["GET"])
def ListarUserRoute():
    from Nutrin.User.Services.listarUser import listarUser
    response["Status"] = "Sucesso"
    response["Dados"] = listarUser()
    response["Mensagem"] = "Usuarios listado com sucesso"
    return jsonify(response)

@app.route("/usuarios/cadastrar", methods=["POST"])
def CadastarUserRoute():
    from Nutrin.User.Services.cadastrarUser import cadastrarUser
    dados = request.get_json(force=True)
    username = dados["username"]
    password = dados["password"]
    nome = dados["nome"]
    email = dados["email"]
    celular = dados["celular"]
    tipo = dados["tipo"]
    status, mensagem = cadastrarUser(username, password, nome, email, celular, tipo)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route("/usuario/<username>", methods=["GET"])
def BuscarUserRoute(username):
    from Nutrin.User.Services.buscarUser import buscarUser
    user = buscarUser(username)
    if user:
        response["Status"] = "Sucesso"
        response["Dados"] = user
        response["Mensagem"] = "Usuario encontrado com sucesso"
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = user
    response["Mensagem"] = "Usuario não encontrado"
    return jsonify(response)

@app.route("/usuario/alterar-senha", methods=["PUT"])
def AlterarSenhaRoute():
    from Nutrin.User.Services.alterarSenha import alterarSenha
    dados = request.get_json()
    username = dados["username"]
    senha_atual = dados["password_atual"]
    senha_nova = dados['password_nova']
    status, mensagem = alterarSenha(username,senha_atual,senha_nova)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route("/usuario/alterar-user", methods=['PUT'])
def AlterarUserRoute():
    from Nutrin.User.Services.alterarUser import alterarUser
    dados = request.get_json()
    username_atual = dados['username_atual']
    username = dados['username']
    nome = dados['nome']
    email = dados['email']
    celular = dados['celular']
    tipo = dados["tipo"]
    status, mensagem = alterarUser(username_atual, username, nome, email, celular, tipo)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route("/usuario/desativar/<username>", methods=["GET"])
def DeletarUserRoute(username):
    from Nutrin.User.Services.excluirUser import excluirUser
    if excluirUser(username):
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = "Usuário desativado"
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = "Usuário não existe"
    return jsonify(response)

@app.route("/usuario/ativar/<username>", methods=["GET"])
def AtivarUserRoute(username):
    from Nutrin.User.Services.excluirUser import ativarUser
    if ativarUser(username):
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = "Usuário ativado"
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = "Usuário não existe"
    return jsonify(response)
