from Nutrin.Consulta.Services.Antropometria.readAntropometria import readAntropometria
from Nutrin import db

def deleteAntropometria(id_antropometria):
    status, a = readAntropometria(id_antropometria,True)
    if status:
        db.session.delete(a)
        db.session.commit()
        return True, "Deletado com sucesso"
    return False, a