from Nutrin.Consulta.Services.Ocupado.createOcupado import createOcupado
from Nutrin.Consulta.Services.Ocupado.readOcupado import readOcupadoNoPeriodo
from Nutrin.Consulta.Services.Horarios.listHorario import listHorarioData

def createConsulta(paciente_id, tipoAtendimento_id, data, hI, hF, tipoEstado_id):
    statusHora, periodo = listHorarioData(data)
    if statusHora:
        periodo_id = periodo[0]['hora_id']
        status, msg = createOcupado(periodo_id, hI, hF)
        #print('bel deus ------- {} - {}'.format(status, msg))
        if status:
            statusHid, msgHora = readOcupadoNoPeriodo(periodo_id)
            #print('bel deus022 ------- {} - {}'.format(statusHid, msgHora))
            if statusHid:
                for o in msgHora:
                    if  hF == o['horaF'] and hI == o['horaI']:
                        from Nutrin.Consulta.Model.Consulta import Consulta
                        consulta = Consulta(paciente_id, tipoAtendimento_id, o['id'] , tipoEstado_id)
                        from Nutrin import db
                        db.session.add(consulta)
                        db.session.commit()
                        return True, "Consulta cadastrada com sucesso"
                return False, 'ID Ocupado não encontrado'
            return statusHid, msgHora
        return status, msg
    return statusHora, periodo

