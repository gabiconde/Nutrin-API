def deleteConsulta(id_consulta):
    from Nutrin.Consulta.Services.Consulta.readConsulta import readConsultaId
    status, consulta = readConsultaId(id_consulta, True)
    if status:
        from Nutrin import db
        db.session.delete(consulta)
        db.session.commit()
        return True, "Periodo excluido"
    return status, consulta



