from Nutrin import db
from Nutrin.Consulta.Services.Horarios.readHorario import readHorarioById
from Nutrin.Consulta.Services.Ocupado.readOcupado import readOcupadoNoPeriodo

def deleteHorario(id):
    status, dado = readOcupadoNoPeriodo(id)
    if status:
        return False, "Não é possivel excluir. Há um paciente utilizando o horário"
    else:
        statusObj, dadoObj = readHorarioById(id,True)
        if statusObj:
            db.session.delete(dadoObj)
            db.session.commit()
            return True, "Periodo excluido"
        return statusObj, dadoObj
    