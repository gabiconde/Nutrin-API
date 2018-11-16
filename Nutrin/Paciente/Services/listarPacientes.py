from Nutrin.Paciente.Model.Paciente import Paciente

def listarPacientes(f=False):
    pacientes = Paciente.query.all()
    if f:
        return pacientes
    pacientes_dic = []
    for p in pacientes:
        pacientes_dic.append({
            'id':p.id,
            'username': p.user.username,
            'password' : p.user.password,
            'nome': p.user.nome,
            'email': p.user.email,
            'celular': p.user.celular,
            'tipo': p.user.tipo,
            'ativo':p.user.ativo,
            'dataNascimento': p.dataNascimento,
            'sexo': p.sexo,
            'cidade': p.cidade,
            'profissao': p.profissao,
            'altura': p.altura,
            'objetivo': p.objetivo
        })
    return pacientes_dic