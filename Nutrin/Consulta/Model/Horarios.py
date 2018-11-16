from Nutrin import db

class Horarios(db.Model):
    __tablename__ = "horarios"
    __table_args__ = (
        db.UniqueConstraint('data', 'horaInicio', 'horaFim', name='periodo unico'),
    )

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10))
    horaInicio = db.Column(db.String(5))
    horaFim = db.Column(db.String(5))

    def __init__(self, data, horaInicio, horaFim):
        self.data = data
        self.horaInicio = horaInicio
        self.horaFim = horaFim

    # def __repr__(self):
    #     return "<Período disponível: {} - {} - {}".format(self.data, self.horaInicio, self.horaFim)

