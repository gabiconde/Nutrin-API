from Nutrin import db
from Nutrin.Alimentacao.Model.TipoRefeicao import TipoRefeicao
from Nutrin.Alimentacao.Model.Anamnese import Anamnese

class Refeicao(db.Model):
    __tablename__ = "refeicoes"

    id = db.Column(db.Integer, primary_key=True)
    anamnese_id = db.Column(db.Integer, db.ForeignKey('anamneses.id'), nullable=False)
    tipoRefeicao_id = db.Column(db.Integer, db.ForeignKey('tipoRefeicoes.id'), nullable=False)
    horario = db.Column(db.TIME,nullable=False)
    refeicao = db.Column(db.Text,nullable=False)

    def __init__(self,anamnese_id, tipoRefeicao_id, horario, refeicao):
        self.anamnese_id = anamnese_id
        self.tipoRefeicao_id = tipoRefeicao_id
        self.horario = horario
        self.refeicao = refeicao
    
    def __repr__(self):
        return "<Refeição {} - {}>".format(self.tipoRefeicao_id, self.refeicao)

    #def __str__(self):