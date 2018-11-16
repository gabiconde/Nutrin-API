# -*- coding: utf-8 -*-
from flask import jsonify, request
from Nutrin import app
from Nutrin import response

@app.route('/paciente/cadastrar', methods=["POST"])
def CadastrarPacienteRoute():
    from Nutrin.Paciente.Services.cadastrarPaciente import cadastrarPaciente
    dados = request.get_json()
    username = dados['username']
    password = dados['password']
    nome = dados['nome']
    email = dados['email']
    celular = dados['celular']
    dataNascimento = dados['dataNascimento']
    sexo = dados['sexo']
    cidade = dados['cidade']
    profissao = dados['profissao']
    objetivo = dados['objetivo']
    altura = dados['altura']
    status, mensagem = cadastrarPaciente(username, password, nome, email, celular, dataNascimento, sexo, cidade, profissao, objetivo, altura)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('/pacientes', methods=["GET"])
def ListarPacientesRoute():
    from Nutrin.Paciente.Services.listarPacientes import listarPacientes
    response['Status'] = "Sucesso"
    response['Dados'] = listarPacientes()
    response['Mensagem'] = "Pacientes listado com sucesso"
    return jsonify(response)

@app.route('/paciente/consultar/<username>', methods=["GET"])
def PesquisarPacienteRoute(username):
    from Nutrin.Paciente.Services.pesquisarPaciente import pesquisarPaciente
    status, retorno = pesquisarPaciente(username)
    if status:
        response["Status"] = "Sucesso"
        response['Dados'] = retorno
        response['Mensagem'] = "Paciente encontrado"
        return jsonify(response)
    response["Status"] = "Erro"
    response['Dados'] = ""
    response['Mensagem'] = retorno
    return jsonify(response)

@app.route('/paciente/alterar-paciente', methods=['PUT'])
def AlterarPacienteRoute():
    from Nutrin.Paciente.Services.alterarPacinete import alterarPaciente
    dados = request.get_json()
    username_atual = dados['username_atual']
    username = dados['username']
    nome = dados['nome']
    email = dados['email']
    celular = dados['celular']
    tipo = dados['tipo']
    dataNascimento = dados['dataNascimento']
    sexo = dados['sexo']
    cidade = dados['cidade']
    profissao = dados['profissao']
    objetivo = dados['objetivo']
    altura = dados['altura']
    status, mensagem = alterarPaciente(username_atual, username, nome, email, celular, tipo, dataNascimento, sexo, cidade, profissao, objetivo, altura)
    if status:
        response["Status"] = "Sucesso"
        response["Dados"] = ""
        response["Mensagem"] = mensagem
        return jsonify(response)
    response["Status"] = "Erro"
    response["Dados"] = ""
    response["Mensagem"] = mensagem
    return jsonify(response)

@app.route('/paciente/desativar/<username>', methods=["GET"])
def DesativarPacienteRoute(username):
    from Nutrin.Paciente.Services.excluirPaciente import desativarPaciente
    if desativarPaciente(username):
        response["Status"] = "Sucesso"
        response['Dados'] = ''
        response['Mensagem'] = "Paciente foi desativado"
        return jsonify(response)
    response["Status"] = "Erro"
    response['Dados'] = ''
    response['Mensagem'] = "Falaha ao desativar o paciente"
    return jsonify(response)

@app.route('/paciente/ativar/<username>', methods=["GET"])
def AtivarPacienteRoute(username):
    from Nutrin.Paciente.Services.excluirPaciente import ativarPaciente
    if ativarPaciente(username):
        response["Status"] = "Sucesso"
        response['Dados'] = ''
        response['Mensagem'] = "Paciente foi ativado"
        return jsonify(response)
    response["Status"] = "Erro"
    response['Dados'] = ''
    response['Mensagem'] = "Falaha ao ativar o paciente"
    return jsonify(response)