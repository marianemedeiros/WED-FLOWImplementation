# transition
    # bloqueia o estado atual na instancia.
    # cria um novo estado
    # atualiza estado atual no Instance e libera o bloqueio
    # atualiza o history_entry (monitor passa a linha do history)
    # Inserir o novo estado nas filas

class t_validar_dados():
    def run(dao, instance, history_entry):
        wed_flow_id = dao.session.query(WED_flow).all()[0].id
        # BLOQUEIA O state_atual
        state_atual = dao.session.query(WED_state).filter_by(id=instance.state_id)
        state = WED_state(cliente='validado', pontos=state_atual.pontos,pedido='validado', instance_id=instance.id, produto=state_atual.produto, pedido=state_atual.pedido, pagamento=state_atual.pagamento)

        dao.session.add(state)
        dao.session.commit()
        instance.state = state
        dao.session.commit()
        # DESBLOQUEIA o state_atual

        history_entry.completed_at = datetime.datetime.now()
        history_entry.current_state_id = state_atual.id
        history_entry.final_state_id = state.id
        dao.session.commit()        