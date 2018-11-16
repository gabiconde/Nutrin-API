from Nutrin.Consulta.Services.Consulta.listConsulta import listOcupadoConsulta
'''
def deleteOcupado(id_ocupado):
    consulta = listOcupadoConsulta(id_ocupado)
    if not consulta:
        from Nutrin.Consulta.Services.Ocupado.readOcupado import readOcupado
        status, ocup = readOcupado(id_ocupado, True)
        if status:
            from Nutrin import db
            db.session.delete(ocup)
            db.session.commit()
            return True, "Horário não esta mais ocupado"
        return status, ocup
    return False, ""

'''