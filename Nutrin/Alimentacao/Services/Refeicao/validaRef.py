from Nutrin.Alimentacao.Services.Refeicao.readRefeicao import readRefeicao

def validaRef(id_anamnese, id_tipoRef):
    refs = readRefeicao(True)
    for i in refs:
        if i.anamnese_id == id_anamnese and i.tipoRefeicao_id == id_tipoRef:
            return False
    return True

