from Nutrin.Consulta.Model.Antropometria import Antropometria
from Nutrin import db

def readAntropometria(antropometria_id, f = False):
    a = db.session.query(Antropometria).filter_by(id = antropometria_id).first()
    if a:
        if f:
            return True, a
        else:
            antropometria = {
            'peso' : a.peso,
            'braco' : a.braco,
            'torax' : a.torax,
            'cintura' : a.cintura,
            'abdomen' : a.abdomen,
            'quadril' : a.quadril,
            'coxa' : a.coxa,
            'biceps' : a.biceps,
            'triceps' : a.triceps,
            'peito' : a.peito,
            'subsCap' : a.subsCap,
            'axilar' : a.axilar,
            'gorduraPerc' : a.gorduraPerc,
            'aguaPerc' : a.aguaPerc,
            'pesoMagro' : a.pesoMagro
            }
            return True, antropometria
    return False, "Antropometria não encontrada"


