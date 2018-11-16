from Nutrin.Consulta.Services.TipoEstado.readTipoEstado import readEstadoById
from Nutrin.Consulta.Services.TipoAtendimento.readTipoAtendimento import readAtendimentoById
from Nutrin.Consulta.Services.Ocupado.readOcupado import readOcupadoById
from Nutrin.Paciente.Services.pesquisarPaciente import pesquisarPacienteById
from Nutrin.Controle.converter_data import binaryToString

def readConsulta(f=False):
    from Nutrin.Consulta.Model.Consulta import Consulta
    consultas = Consulta.query.all()
    if consultas != None:
        if f:
            return True, consultas
        consulas_dic = []
        for c in consultas:
            tipoEstado = readEstadoById(c.tipoEstado_id)
            tipoAtendimento = readAtendimentoById(c.tipoAtendimento_id)
            horario = readOcupadoById(c.horario_id)
            paciente = pesquisarPacienteById(c.paciente_id)
            dieta = binaryToString(c.dieta)
            consulas_dic.append({
                'id': c.id,
                'paciente_id': paciente,
                'tipoAtendimento_id': tipoAtendimento.nome,
                'horario_id': horario,
                'tipoEstado_id':tipoEstado.nome,
                'antropometria_id': c.antropometria_id,
                'dieta': dieta,
                'pagamento': c.pagamento
            })
        return True, consulas_dic
    return False, 'Nenhuma Consulta cadastrada'


def readConsultaId(id_consulta,f=False):
    from Nutrin.Consulta.Model.Consulta import Consulta
    #consultas = Consulta.query().filter(id==id_consulta)
    consultas = Consulta.query.get(id_consulta)
    print(consultas)
    if consultas != None:
        if f:
            return True, consultas
        consultas_dic = []
        for c in consultas:    
            tipoEstado = readEstadoById(c.tipoEstado_id)
            tipoAtendimento = readAtendimentoById(c.tipoAtendimento_id)
            horario = readOcupadoById(c.horario_id)
            paciente = pesquisarPacienteById(c.paciente_id)
            dieta = binaryToString(c.dieta)
            consultas_dic.append({
                'id': c.id,
                'paciente_id': paciente,
                'tipoAtendimento_id': tipoAtendimento,
                'horario_id': horario,
                'tipoEstado_id': tipoEstado,
                'antropometria_id': c.antropometria_id,
                'dieta': dieta,
                'pagamento': c.pagamento
            })
        return True, consultas_dic
    return False, 'Nenhuma consulta com este id'

