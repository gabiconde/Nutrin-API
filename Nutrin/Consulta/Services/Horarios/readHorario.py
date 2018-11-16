from Nutrin.Consulta.Model.Horarios import Horarios
from Nutrin import db
from Nutrin.Controle.converter_data import *

def readHorario(data, horaInicio, horaFim, f =False):
    h = db.session.query(Horarios).filter(data==data,horaInicio==horaInicio,horaFim==horaFim)
    print(h)
    if h != None:
        if f:
            return True, h
        else:
            hora = {
                'hora_id' : h.id,
                'data' : h.data,
                'horaInicio' : h.horaInicio,
                'horaFim' : h.horaFim
            }
        return True, hora
    return False, "Período não cadastrado"

def readHorarioById(horaraio_id, f= False):
    h = Horarios.query.all()
    #User.query.get(1)
    print(horaraio_id) 
    if h:
        if f:
            for i in h:
                a = i.id
                if int(a) == int(horaraio_id):
                    return True, i
            return False, "Período não cadastrado"
        else:
            hora = {
                'hora_id' : h.id,
                'data' : h.data,
                'horaInicio' : h.horaInicio,
                'horaFim' : h.horaFim
            }
        
        return True, hora
    return False, "Período não cadastrado"

