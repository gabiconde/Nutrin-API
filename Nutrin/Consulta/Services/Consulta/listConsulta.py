from Nutrin.Consulta.Services.Consulta.readConsulta import readConsulta
from Nutrin.Consulta.Model.Consulta import Consulta
#listar todas as consultas == read
def listConsultas():
    status, dado = readConsulta()
    return dado

def listByColumn(column,id_column):
    lista = listConsultas()
    #print('listinha formosa {} {}'.format(column,id_column))
    consultas = []
    for c in lista:   
        if int(c[column]) == int(id_column):
            consultas.append(c)
    return consultas

#listar por tipo estado
#listar por pagamento
#listar por horarios
'''
def listOcupadoConsulta(id_ocupado):
    lista = listConsultas()
    consultas = []
    for c in lista:
        if c['horario_id'] == id_ocupado:
            consultas.append(c)
    return consultas

#listar por pacientes
def listPacienteConsulta(id_paciente):
    #lista = Consulta.query.filter_by(paciente_id='1')
    lista = listConsultas()
    print(lista)
    consultas = []
    for c in lista:
        if c['paciente_id'] == id_paciente:
            consultas.append(c)
    return consultas
'''

#listar tipoAtendimento