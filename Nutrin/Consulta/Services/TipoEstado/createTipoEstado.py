from Nutrin.Consulta.Model.TipoEstado import TipoEstado
from Nutrin.Consulta.Services.TipoEstado.validarNome import validarNome
from Nutrin import db

def createTipoEstado(nome):
    nome = nome.upper()
    if validarNome(nome):
        tipo_estado = TipoEstado(nome)
        db.session.add(tipo_estado)
        db.session.commit()
        return True, "Tipo estado cadastrado com sucesso"
    return False, "Tipo estado já cadastrado"
