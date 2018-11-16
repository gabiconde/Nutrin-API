# -*- coding: utf-8 -*-
def deleteAnamnese(id_anamnese):
    from Nutrin.Alimentacao.Services.Anamnese.readAnamnese import readRefeicaoAnamnese, readAnamneseById
    refeicoes = readRefeicaoAnamnese(id_anamnese)
    if not refeicoes:
        ana = readAnamneseById(id_anamnese)
        if ana:
            from Nutrin import db
            db.session.delete(ana)
            db.session.commit()
            return True, "Anamnese deletada com sucesso"
        return False, "Anamnese não existe"
    return False, "Há refeições atreladas a esta Anamnese"
    
    