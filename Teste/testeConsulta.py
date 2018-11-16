import requests as Req

url_basica = 'http://127.0.0.1:5000'

def testeConsultaCreate(paciente_id, tipoAtendimento_id, horaI, horaF,data, tipoEstado_id):
    url = url_basica + '/consulta/cadastrar'
    consulta = {
        'paciente_id': paciente_id,
        'tipoAtendimento_id': tipoAtendimento_id,
        'data': data,
        'horaI': horaI,
        'horaF': horaF,
        'tipoEstado_id': tipoEstado_id
    }
    dados = Req.api.post(url, json=consulta).json()
    return dados

def testeListConsultas():
    url = url_basica + '/consultas'
    dados = Req.api.get(url).json()
    return dados

def testeListConsultasPacientes(id_paciente):
    url = url_basica + '/consultas/paciente/' + id_paciente
    dados = Req.api.get(url).json()
    return dados

def testeListConsultaHorarios(id_horario):
    url = url_basica + '/consultas/horario/' + id_horario
    dados = Req.api.get(url).json()
    return dados

def testeAlterarConsulta(consulta_id,paciente_id,tipoAtendimento_id,tipoEstado_id,pagamento):
    url = url_basica + '/consultas/alterar'
    consulta = {
        'consulta_id':consulta_id,
        'paciente_id': paciente_id,
        'tipoAtendimento_id': tipoAtendimento_id,
        'tipoEstado_id': tipoEstado_id,
        'pagamento':pagamento      
    }
    dados = Req.api.put(url, json=consulta).json()
    return dados

def testeAlterarHorarioConsulta(consulta_id, horario_id,data,horaI,horaF):
    url = url_basica + '/consultas/alterarHorario'
    consulta = {
        'consulta_id':consulta_id,
        'horario_id': horario_id,
        'data': data,
        'horaI': horaI,
        'horaF':horaF      
    }
    dados = Req.api.put(url, json=consulta).json()
    #dia , hi, hf
    return dados

def testeDesmarcarConsulta(id_consulta, column, id_column):
    url = url_basica + '/consultas/alterarId'
    consulta = {
        'id_consulta':id_consulta,
        'column' : column,
        'id_column' : id_column
    }
    dados = Req.api.put(url, json=consulta).json()
    return dados

def testeAdcAntropometria(id_consulta, column, id_column):
    url = url_basica + '/consultas/alterarId'
    consulta = {
        'id_consulta':id_consulta,
        'column' : column,
        'id_column' : id_column
    }
    dados = Req.api.put(url, json=consulta).json()
    return dados

def testeAdcDieta(id_consulta, column, id_column):
    url = url_basica + '/consultas/alterarId'
    consulta = {
        'id_consulta':id_consulta,
        'column' : column,
        'id_column' : id_column
    }
    dados = Req.api.put(url, json=consulta).json()
    return dados

def testeAdcPagamento(id_consulta, column, id_column):
    url = url_basica + '/consultas/alterarId'
    consulta = {
        'id_consulta':id_consulta,
        'column' : column,
        'id_column' : id_column
    }
    dados = Req.api.put(url, json=consulta).json()
    return dados

def testeDeleteConsulta(id_consulta):
    url = url_basica + '/consultas/delete/' + id_consulta
    dados = Req.api.delete(url).json()
    return dados



def main():
    # print(testeConsultaCreate("2", "1", "17:00","18:00", "2018-11-01", "1"))
     print(testeListConsultas())
    # print(testeListConsultasPacientes('2'))
    # print(testeListConsultaHorarios('2018-11-01'))
    # print(testeAlterarConsulta('3','2','1','1',True))
    # print(testeAlterarHorarioConsulta('3','3','2018-11-01','13:00','14:00'))
    # print(testeDesmarcarConsulta('2','tipoEstado_id','3'))
    # print(testeAdcAntropometria('2','antropometria_id','1'))
    # print(testeAdcDieta('1','dieta','../Users/gabic/Documents'))
    # print(testeAdcPagamento('2','pagamento', True))
    # print(testeDeleteConsulta('6'))
main()

 #[{'id': 1, 'horaI': '11:00', 'horaF': '12:00'}, {'id': 2, 'horaI': '11:00', 'horaF': '12:00'}, {'id': 3, 'horaI': '11:00', 'horaF': '12:00'}, {'id': 4, 'horaI': '11:00', 'horaF': '12:00'}, {'id': 5, 'horaI': '11:00', 'horaF': '12:00'}, {'id': 6, 'horaI': '12:00', 'horaF': '13:00'}]