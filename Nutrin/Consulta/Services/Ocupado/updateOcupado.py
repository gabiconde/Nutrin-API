from Nutrin import db
from Nutrin.Consulta.Services.Ocupado.readOcupado import readOcupado, readOcupadoNoPeriodo
from Nutrin.Consulta.Services.Horarios.listHorario import listHorarioData

def validaNovoOcupado(data, hI, hF):
    status, dado = listHorarioData(data)
    if status:
        pode = False
        for disp in dado:
            if disp['horaInicio'] >= hI and hF >= disp['horaFim']:
                pode = True
                id_periodo = disp['hora_id']
            else:
                pode = False
        if pode:
            statusOcup, dadoOcup = readOcupadoNoPeriodo(id_periodo)
            if statusOcup:
                lista = []
                pode = False
                for ocup in dadoOcup:
                    if ocup['horaI'] > hI and hF > ocup['horaF']:
                        pode = True
                    else:
                        pode = False
                return pode, id_periodo
            return False, dadoOcup
        return False, "Horário escolhido não está disponível no dia"
    return False, dado  



def updateOcupado(id,data,hI,hF):
    status, dado = readOcupado(id, True)
    if status:
        statusNew, dadoNew = validaNovoOcupado(data, hI, hF)
        if statusNew:
            dado.horario_id = dadoNew
            dado.horaI = hI
            dado.horaF = hF
            db.session.commit()
            return True, "Horário consulta alterado"
        return statusNew, dadoNew
    return status, dado


