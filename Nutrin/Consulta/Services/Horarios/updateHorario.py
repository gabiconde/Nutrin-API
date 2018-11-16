from Nutrin import db
from Nutrin.Consulta.Services.Horarios.readHorario import readHorarioById
from Nutrin.Consulta.Services.Ocupado.readOcupado import readOcupadoNoPeriodo

def updateHorario(horario_id, hI, hF):
    status, dado = readOcupadoNoPeriodo(horario_id)
    if status:
        return False, "Não é possivel alterar. Há um paciente utilizando o horário"
    else:
        statusObj, dadoObj = readHorarioById(horario_id,True)
        if statusObj:
            dadoObj.horaInicio = hI
            dadoObj.horaFim = hF
            db.session.commit()
            return True, "Periodo alterado"
        return statusObj, dadoObj
    
    
'''
    status, dado = validaHorario(data, hora)
    if status:
        if verdade:
            return False, "Horário já está sendo utilizado"
        else:
            dado.utilizado = verdade
            db.session.commit()
            return True, "Horário foi liberado"
    elif status == False:
        if verdade:
            dado.utilizado = verdade
            db.session.commit()
            return True, "Horário foi ocupado"
        return False, "Horario já esta liberado"
    return False, dado

'''



