from Nutrin import db 

class Antropometria(db.Model):
    __tablename__ = "antropometrias"

    id = db.Column(db.Integer, primary_key=True)
    peso = db.Column(db.Float)
    braco = db.Column(db.Float)
    torax = db.Column(db.Float)
    cintura = db.Column(db.Float)
    abdomen = db.Column(db.Float)
    quadril = db.Column(db.Float)
    coxa = db.Column(db.Float)
    biceps = db.Column(db.Float)
    triceps = db.Column(db.Float)
    peito = db.Column(db.Float)
    subsCap = db.Column(db.Float)
    axilar = db.Column(db.Float)
    gorduraPerc = db.Column(db.Float)
    aguaPerc = db.Column(db.Float)
    pesoMagro = db.Column(db.Float)

    def __init__(self, peso, braco, torax, cintura, abdomen, quadril, coxa, biceps, triceps, peito, subsCap, axilar, gorduraPerc, aguaPerc, pesoMagro):
        self.peso = peso
        self.braco = braco
        self.torax = torax
        self.cintura = cintura
        self.abdomen = abdomen
        self.quadril = quadril
        self.coxa = coxa
        self.biceps = biceps
        self.triceps = triceps
        self.peito = peito
        self.subsCap = subsCap
        self.axilar = axilar
        self.gorduraPerc = gorduraPerc
        self.aguaPerc = aguaPerc
        self.pesoMagro = pesoMagro

