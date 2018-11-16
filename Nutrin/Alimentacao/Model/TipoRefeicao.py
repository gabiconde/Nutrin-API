from Nutrin import db


class TipoRefeicao(db.Model):
    __tablename__ = "tipoRefeicoes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(30),nullable=False)
    #refeicoes = db.relationship('Refeicao', backref='tipo')

    def __init__(self, nome):
        self.nome = nome
    
    def __repr__(self):
        return "<TipoRefeicao {0}>".format(self.nome)
