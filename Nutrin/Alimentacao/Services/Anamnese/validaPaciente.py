def validaPaciente(id_paciente):
    from Nutrin.Alimentacao.Services.Anamnese.readAnamnese import readAnamnese
    anamneses = readAnamnese(True)
    for a in anamneses:
        if a.paciente_id == id_paciente:
            return False
    return True