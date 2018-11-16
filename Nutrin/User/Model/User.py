from Nutrin import db

class User(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    nome = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    celular = db.Column(db.String(11))
    tipo = db.Column(db.String(1))
    ativo = db.Column(db.Boolean, default=True)

    #tipo: N - nutricionista, P - paciente, A - admin  

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)

    def __init__(self, username, password, nome, email, celular, tipo):
        self.username = username
        self.password = password
        self.nome = nome
        self.email = email
        self.celular = celular
        self.tipo = tipo
    
    def __repr__(self):
        return "<User {0}>".format(self.username)