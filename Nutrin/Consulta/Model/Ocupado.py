from Nutrin import db
from Nutrin.Consulta.Model.Horarios import Horarios

class Ocupado(db.Model):
    __tablename__ = "ocupados"

    id = db.Column(db.Integer, primary_key=True)
    horario_id = db.Column(db.Integer, db.ForeignKey('horarios.id'), nullable=False)
    horaI = db.Column(db.String(5), nullable=False)
    horaF = db.Column(db.String(5), nullable=False)

    def __init__(self, horario_id, horaI, horaF):
        self.horario_id = horario_id
        self.horaI = horaI
        self.horaF = horaF

    # def __repr__(self):
    #     return "<Horário ocupado: \nid: {}\nHora Inicio: {}\nHora Fim: {}>".format(self.horario_id,self.horaI,self.horaF)



