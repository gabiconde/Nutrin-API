from Nutrin import db
from Nutrin.Consulta.Model.Horarios import Horarios

def listHorario(hoje=False):
    horarios = Horarios.query.all()
    lista = []
    for h in horarios:
        lista.append({
        'hora_id': h.id,
        'data': h.data,
        'horaInicio': h.horaInicio,
        'horaFim':h.horaFim})
    return lista

def listHorarioData(data):
    horarios = Horarios.query.filter(data==data)
    lista = []
    if horarios != None:
        for h in horarios:
            print(h.data == data)
            if h.data == data:        
                lista.append({
                'hora_id' : h.id,
                'data' : h.data,
                'horaInicio' : h.horaInicio,
                'horaFim' : h.horaFim})
        if not lista:
            return False, "Não há periodos nessa data"
        return True, lista
    

def listHorarioDisp():
    from Nutrin.Consulta.Services.Ocupado.readOcupado import readOcupadoNoPeriodo
    horarios = Horarios.query.all()
    if horarios != None:
        disponiveis = []
        parcial = []
        for h in horarios:
            status, dado = readOcupadoNoPeriodo(h.id)
            if status:
                parcial.append(h)
            else:
                disponiveis.append(h)
        lista = [disponiveis,parcial]
        return True, lista
    return False, 'Não há horários cadastrados'


def listDisponiveis():
    from Nutrin.Consulta.Services.Ocupado.readOcupado import readOcupadoNoPeriodo
    diaHoras = {}
    periodos = listHorario()
    #print(periodos)
    for p in periodos:  
        qtdHoras = int(p['horaFim'][:2]) - int(p['horaInicio'][:2])
        diaHoras[p['data']] = []
        for i in range(0, qtdHoras):
            diaHoras[p['data']].append(int(p['horaInicio'][:2])+i)
        #print(diaHoras)
        statusOcup, dadoOcup = readOcupadoNoPeriodo(p['hora_id'])
        #print(statusOcup, dadoOcup)
        if statusOcup:
            print(statusOcup, dadoOcup)
            for o in dadoOcup:
                if int(o['horaI'][:2]) in diaHoras[p['data']]:
                    diaHoras[p['data']].remove(int(o['horaI'][:2]))
    horasDisp = []
    for dia, horas in diaHoras.items():
        horasDisp.append({"dia":dia,"horas":horas}) 
    return horasDisp

     






'''
listaTodos = listHorario()
    horarios = []
    for p in listaTodos:
        if data == p.data:
            horarios.append(p)
    
'''