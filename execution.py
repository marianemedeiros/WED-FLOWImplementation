from database import *
import schedule
from datetime import datetime
import time


# transition
    # bloqueia o estado atual na instancia.
    # cria um novo estado
    # atualiza estado atual no Instance e libera o bloqueio
    # atualiza o history_entry (monitor passa a linha do history)
    # Inserir o novo estado nas filas

def avalia_trigger(condition, state, dao):
    print("aaaaaa")
    print(dao.select_condition(condition.id))

    

def make_func(t, dao):
    def _function():
        '''
        recuper a fila da trigger X
        Para cada wed_state da fila avalia a condition da trigger
        se true: dispara a transition
        '''

        fila = dao.select_fila(t.id)
        # update status para processando
        for i in fila:
            r = avalia_trigger(t.condition, dao.select_state(fila.wed_state_id), dao)
            if(r == True):
                pass
                # Criar a entrada no history_entry
                # dispara transition (a transition atualiza o history_entry)

            # update para processado (finish)
        print('t_'+str(t.id) + ': Funcionou')
    return _function


    # status = Column(String(50))
    # create_at = Column (DateTime)
    # finalized_at =  Column (DateTime)
    # wed_flow_id = Column(Integer, ForeignKey('wed_flow.id'))
if __name__ == '__main__':
    dao = DAO()
    # wedflow = dao.select_wedflow2(1)
    # ins = Instance(status = 'started', create_at = datetime.now(), wed_flow_id = wedflow[0])
    # dao.session.add(ins)
    # dao.session.commit()

    result = dao.select_trigger()
    for i in result:
        job = make_func(i, dao)
        schedule.every(i.id).seconds.do(job)


    while True:
        schedule.run_pending()
        time.sleep(1)

