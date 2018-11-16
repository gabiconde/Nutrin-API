from Nutrin import db

class TipoAtendimento(db.Model):
    __tablename__ = "tipoAtendimentos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(300), unique=True)
    preco = db.Column(db.Float)
    qtdRetorno = db.Column(db.Integer)
    #consultas = db.relationship('Consulta', backref='tipo')
    # c1 = Consulta(..., tipo=nomeTipo)

    def __init__(self, nome, preco, qtdRetorno):
        self.nome = nome
        self.preco = preco
        self.qtdRetorno = qtdRetorno
  
    
    def __repr__(self):
        return "<TipoAtendimento {0}>".format(self.nome)
