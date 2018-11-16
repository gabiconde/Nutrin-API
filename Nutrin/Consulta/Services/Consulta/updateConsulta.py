
def updateConsulta(id_consulta, paciente_id, tipoAtendimento_id, tipoEstado_id, pagamento ):
    from Nutrin.Consulta.Services.Consulta.readConsulta import readConsultaId
    status, c = readConsultaId(id_consulta,True)
    if status:
        c.paciente_id = paciente_id
        c.tipoAtendimento_id = tipoAtendimento_id
        c.tipoEstado_id = tipoEstado_id
        c.pagamento = pagamento
        from Nutrin import db
        db.session.commit()
        return True, "Consulta alterada com sucesso"
    return False, "Consulta não encontrada"

def updateHorarioConsulta(id_consulta, horario_id, data, hI, hF):
    from Nutrin.Consulta.Services.Consulta.readConsulta import readConsultaId
    status, c = readConsultaId(id_consulta,True)
    if status:
            from Nutrin.Consulta.Services.Horarios.listHorario import listHorarioData
            statusHora, periodo = listHorarioData(data)
            if statusHora:
                periodo_id = periodo[0]['hora_id']
                from Nutrin.Consulta.Services.Ocupado.createOcupado import createOcupado
                statusOcup, msg = createOcupado(periodo_id, hI, hF)
                if statusOcup:
                    from Nutrin.Consulta.Services.Ocupado.readOcupado import readOcupadoNoPeriodo
                    statusHid, msgHora = readOcupadoNoPeriodo(periodo_id)
                    if statusHid:
                        for o in msgHora:
                            if o['horaI'] == hI and o['horaF'] == hF:
                                c.horario_id = o['id']
                                from Nutrin import db
                                db.session.commit()
                                from Nutrin.Consulta.Services.Ocupado.readOcupado import readOcupado
                                ocupStatus, ocup = readOcupado(horario_id, True)
                                if ocupStatus:
                                    db.session.delete(ocup)
                                    db.session.commit()
                                return True, "Consulta alterada com sucesso"
                    return statusHid, msgHora
                return statusOcup, msg
            return statusHora, periodo
    return False, "Consulta não encontrada"

def updateAntropometriaConsulta(id_consulta, paciente_id, tipoAtendimento_id, horario_id, tipoEstado_id, pagamento ):
    from Nutrin.Consulta.Services.Consulta.readConsulta import readConsultaId
    status, c = readConsultaId(id_consulta,True)
    if status:
        c.paciente_id = paciente_id
        c.tipoAtendimento_id = tipoAtendimento_id
        c.horario_id = horario_id
        c.tipoEstado_id = tipoEstado_id
        c.pagamento = pagamento
        from Nutrin import db
        db.session.commit()
        return True, "Consulta alterada con sucesso"
    return False, "Consulta não encontrada"

# def updateDietaConsulta(id_consulta, paciente_id, tipoAtendimento_id, horario_id, tipoEstado_id, pagamento ):
#     from Nutrin.Consulta.Services.Consulta.readConsulta import readConsultaId
#     status, c = readConsultaId(id_consulta,True)
#     if status:
#         c.paciente_id = paciente_id
#         c.tipoAtendimento_id = tipoAtendimento_id
#         c.horario_id = horario_id
#         c.tipoEstado_id = tipoEstado_id
#         c.pagamento = pagamento
#         from Nutrin import db
#         db.session.commit()
#         return True, "Consulta alterada con sucesso"
#     return False, "Consulta não encontrada"

def updateUmConsulta(id_consulta, column, id_column):
    from Nutrin.Consulta.Services.Consulta.readConsulta import readConsultaId
    status, c = readConsultaId(id_consulta,True)
    if status:
        if column == 'tipoEstado_id':
            c.tipoEstado_id = id_column
        elif column == 'antropometria_id':
            c.antropometria_id = id_column
        elif column == 'dieta':
            from Nutrin.Controle.converter_data import stringToBinary
            value = stringToBinary(id_column)
            c.dieta = value
        elif column == 'pagamento':
            c.pagamento = id_column
        else:
            return False, "Opção não válida"
        from Nutrin import db
        db.session.commit()
        return True, '{} alterado com sucesso'.format(column)
    return False, 'Consulta não encontrada'











