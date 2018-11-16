from Nutrin import db
from Nutrin.Consulta.Services.Ocupado.readOcupado import readOcupadoNoPeriodo
from Nutrin.Consulta.Model.Ocupado import Ocupado


def createOcupado(periodo_id,hI,hF):
    #print(readOcupadoNoPeriodo(periodo_id))
    status, dado = readOcupadoNoPeriodo(periodo_id)
    #print('aquiiiiii --- {} {}'.format(status, dado))
    if status:
        for ocup in dado:
            #int(p['horaFim'][:2]) - int(p['horaInicio'][:2]
            #if int(hF[:2]) >= int(ocup['horaI'][:2]) and int(hI[:2]) <= int(ocup['horaF'][:2]) and int(hI[:2]) != int(ocup['horaI'][:2]):
            if int(hI[:2]) != int(ocup['horaI'][:2]):
                permissao = True
            else:
                return False, "Horário esta ocupado"
        if permissao:
            o = Ocupado(periodo_id, hI, hF)
            db.session.add(o)
            db.session.commit()
            return True, "Horário foi preenchido com sucesso"
    else:
        #print('aqui03')
        o = Ocupado(periodo_id, hI, hF)
        db.session.add(o)
        db.session.commit()
        return True, "Horário foi preenchido com sucesso"


