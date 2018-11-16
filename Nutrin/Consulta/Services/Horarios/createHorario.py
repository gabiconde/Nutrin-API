from Nutrin.Consulta.Model.Horarios import Horarios
from Nutrin.Consulta.Services.Horarios.readHorario import readHorario
from Nutrin.Consulta.Services.Horarios.listHorario import listHorarioData, listHorario
from Nutrin import db

# def validaCadastro(data, hI,hF):
#     status, periodos = listHorariu7oData(data)
#     print('-----------------------------------' + periodos)
#     permissao = None
#     for pe in periodos:
#         for p in pe:
#             print(p)
#         # if hF[0:1] > p['horaInicio'][0:1] and hI[0:1] < p['horaFim'][0:1]:
#         #     permissao = True
#         # else:
#         #     return False
#     return permissao

def createHorario(data, horaInicio, horaFim):
    from Nutrin.Consulta.Services.Horarios.listHorario import listHorarioData
    status, mensagem = listHorarioData(data)
    if status:
        print(status, mensagem)
        # if validaCadastro(data, horaInicio,horaFim):       
        #     horario = Horarios(data, horaInicio, horaFim)
        #     db.session.add(horario)
        #     db.session.commit()
        #     return True, "Período cadastrado com sucesso!"
        return False, "Já existe um periodo nesta data"
    else:
        horario = Horarios(data, horaInicio, horaFim)
        db.session.add(horario)
        db.session.commit()
        return True, "Período cadastrado com sucesso!"

    

    

        