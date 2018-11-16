from Nutrin import db


class TipoEstado(db.Model):
    __tablename__ = "tipoEstados"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30), unique=True)
    #consultas = db.relationship('Consulta', backref='estado')

    # c1 = Consulta(..., tipo=nomeTipo)

    def __init__(self, nome):
        self.nome = nome

    
    def __repr__(self):
        return "<TipoEstado {0}>".format(self.nome)
