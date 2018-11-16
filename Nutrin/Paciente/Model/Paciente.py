from Nutrin import db
from Nutrin.User.Model.User import User


class Paciente(db.Model):
    __tablename__ = "pacientes"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    dataNascimento = db.Column(db.DateTime)
    sexo = db.Column(db.String(1))
    cidade = db.Column(db.String(50))
    profissao = db.Column(db.String(50))
    objetivo = db.Column(db.String(50))
    altura = db.Column(db.Float, nullable=False)

    #consultas = db.relationship('Consulta', backref='consultas')
    #anamneses = db.relationship('Anamnese', backref='anamneses')
    user = db.relationship('User', foreign_keys=user_id)

    
    def __init__(self, id_user, dataNascimento, sexo, cidade, profissao, objetivo,altura):
        self.user_id = id_user 
        self.dataNascimento = dataNascimento
        self.sexo = sexo
        self.cidade = cidade
        self.profissao = profissao
        self.objetivo = objetivo
        self.altura = altura
    
    def __repr__(self):
        return "<Paciente {0}>".format(self.user.username)