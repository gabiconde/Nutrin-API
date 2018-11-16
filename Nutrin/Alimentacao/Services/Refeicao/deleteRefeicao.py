# -*- coding: utf-8 -*-
def deleteRefeicao(id_refeicao):
    from Nutrin.Alimentacao.Services.Refeicao.readRefeicao import readRefeicaoById
    refeicao = readRefeicaoById(id_refeicao)
    if refeicao:
        from Nutrin import db
        db.session.delete(refeicao)
        db.session.commit()
        return True, "Refeição deletada com sucesso"
    return False, "Refeição não existe"

    