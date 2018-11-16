from Nutrin import db
from Nutrin.Consulta.Model.TipoAtendimento import TipoAtendimento
from Nutrin.Consulta.Model.Antropometria import Antropometria
from Nutrin.Consulta.Model.TipoEstado import TipoEstado
from Nutrin.Paciente.Model.Paciente import Paciente
from Nutrin.Consulta.Model.Ocupado import Ocupado

class Consulta(db.Model):
    __tablename__ = "consultas"

    id = db.Column(db.Integer, primary_key=True)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    tipoAtendimento_id = db.Column(db.Integer, db.ForeignKey('tipoAtendimentos.id'), nullable=False)
    horario_id = db.Column(db.Integer, db.ForeignKey('ocupados.id'), nullable=True)
    tipoEstado_id = db.Column(db.Integer, db.ForeignKey('tipoEstados.id'), nullable=False)
    antropometria_id = db.Column(db.Integer, db.ForeignKey('antropometrias.id'))
    dieta = db.Column(db.LargeBinary)
    pagamento = db.Column(db.Boolean, default=False)

    def __init__(self, paciente_id, tipoAtendimento_id, horario_id, tipoEstado_id):
        self.paciente_id = paciente_id
        self.tipoAtendimento_id = tipoAtendimento_id
        self.horario_id = horario_id
        self.tipoEstado_id = tipoEstado_id
    
    def __repr__(self):
        return "<Consulta {}".format(self.tipoEstado_id)

    # @id_column.setter
    # def id_column(self, x, id_set):
    #     if x == 'tipoEstado_id':
    #         self.__x = id_set




    
