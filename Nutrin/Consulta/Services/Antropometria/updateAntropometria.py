from Nutrin.Consulta.Services.Antropometria.readAntropometria import readAntropometria
from Nutrin import db

def updateAntropometria(antropometria_id,peso, braco, torax, cintura, abdomen, quadril, coxa, biceps, triceps, peito, subsCap, axilar, gorduraPerc, aguaPerc, pesoMagro):
    status, a = readAntropometria(antropometria_id, True)
    if status:
        a.peso = peso
        a.braco = braco
        a.torax = torax
        a.cintura = cintura
        a.abdomen = abdomen
        a.quadril = quadril
        a.coxa = coxa
        a.biceps = biceps
        a.triceps = triceps
        a.peito = peito
        a.subsCap = subsCap
        a.axilar = axilar
        a.gorduraPerc = gorduraPerc
        a.aguaPerc = aguaPerc
        a.pesoMagro =pesoMagro
        db.session.commit()
        return True, "Antropometria alterada com sucesso"
    return False, "Antropometria não encontrada"