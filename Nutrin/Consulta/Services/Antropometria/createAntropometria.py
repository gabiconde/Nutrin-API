from Nutrin.Consulta.Model.Antropometria import Antropometria
from Nutrin import db

def createAntropometria(peso, braco, torax, cintura, abdomen, quadril, coxa, biceps, triceps, peito, subsCap, axilar, gorduraPerc, aguaPerc, pesoMagro):
    a = Antropometria(peso, braco, torax, cintura, abdomen, quadril, coxa, biceps, triceps, peito, subsCap, axilar, gorduraPerc, aguaPerc, pesoMagro)
    db.session.add(a)
    db.session.commit()
    return True, ['Antropometria cadastrada com sucesso!', a.id]

