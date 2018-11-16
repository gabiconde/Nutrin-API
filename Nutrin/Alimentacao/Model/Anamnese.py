from Nutrin import db
from Nutrin.Paciente.Model.Paciente import Paciente


class Anamnese(db.Model):
    __tablename__ = "anamneses"

    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'))
    qtdAtividadeFisica = db.Column(db.Integer)
    tipoExercicio = db.Column(db.String(150))
    horaAcorda = db.Column(db.TIME)
    padraoRefeicao = db.Column(db.String(150))
    deficienciaAlimentacaoDiaria = db.Column(db.String(250))
    necessitaSuplementoAlimentar = db.Column(db.String(150))
    retencaoLiquido = db.Column(db.Boolean)
    alergiaRemedio = db.Column(db.String(150))
    alergiaSuplemento = db.Column(db.String(150))
    intoleranciaAlimentar = db.Column(db.String(150))
    problemaSaude = db.Column(db.String(150))
    problemaSaudeFamilia = db.Column(db.String(150))
    medicacao = db.Column(db.String(150))
    suplementacao = db.Column(db.String(150))
    #refeicoes = db.relationship('Refeicao', backref='anamneseOwner')

    def __init__(self,paciente_id, qtdAtividadeFisica, tipoExercicio, horaAcorda, padraoRefeicao, deficienciaAlimentacaoDiaria, necessitaSuplementoAlimentar, retencaoLiquido, alergiaRemedio, alergiaSuplemento, intoleranciaAlimentar, problemaSaude, problemaSaudeFamilia, medicacao, suplementacao):
        self.paciente_id = paciente_id
        self.qtdAtividadeFisica = qtdAtividadeFisica
        self.tipoExercicio = tipoExercicio
        self.horaAcorda = horaAcorda
        self.padraoRefeicao = padraoRefeicao
        self.deficienciaAlimentacaoDiaria= deficienciaAlimentacaoDiaria
        self.necessitaSuplementoAlimentar =necessitaSuplementoAlimentar
        self.retencaoLiquido = retencaoLiquido
        self.alergiaRemedio = alergiaRemedio
        self.alergiaSuplemento = alergiaSuplemento
        self.intoleranciaAlimentar = intoleranciaAlimentar
        self.problemaSaude = problemaSaude
        self.problemaSaudeFamilia = problemaSaudeFamilia
        self.medicacao = medicacao
        self.suplementacao = suplementacao

    def __repr__(self):
        return "<Anamnese {} - {}>".format(self.qtdAtividadeFisica, self.horaAcorda)



    

