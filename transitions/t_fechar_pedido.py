# transition
    # bloqueia o estado atual na instancia.
    # cria um novo estado
    # atualiza estado atual no Instance e libera o bloqueio
    # atualiza o history_entry (monitor passa a linha do history)
    # Inserir o novo estado nas filas
# from database import *
from database.Associations import wedState_wedTrigger
from database.Interruption import Interruption
from database.History_entry import History_entry
from database.Instance import Instance
from database.WED_attribute import WED_attribute
from database.WED_condition import WED_condition
from database.WED_flow import WED_flow 
from database.WED_transition import WED_transition
from database.WED_trigger import WED_trigger
from database.Readxml import Readxml
from database.WED_state import WED_state
import datetime
import copy


from database.db_session import *
class t_fechar_pedido():
    def run(instance_id, history_entry_id):
        session = Session()
        instance = session.query(Instance).with_for_update().filter_by(id = instance_id).first()
        
        history_entry = session.query(History_entry).filter_by(id = history_entry_id).first()
        state_atual = session.query(WED_state).with_for_update().filter_by(id = instance.state_id).first()
        
        state = WED_state(
            id_cliente = state_atual.id_cliente,
            cliente = 'validado6',
            pontos = state_atual.pontos,
            id_pedido = state_atual.id_pedido,
            pedido = 'concluido',
            id_produto = state_atual.id_produto,
            produto= state_atual.produto,
            pagamento=state_atual.pagamento,
            instance_id = instance.id,
            )


        session.add(state)
        session.flush()
        instance.state = state
        session.commit()
        # DESBLOQUEIA o state_atual

        history_entry.completed_at = datetime.datetime.now()
        history_entry.current_state_id = state_atual.id
        history_entry.final_state_id = state.id
        
        wed_trigger = session.query(WED_trigger).all()
        for i in wed_trigger:
            wedState_wedTrigger(wed_state=state, status='started', wed_trigger=i)
        
        session.commit()
        session.close()
