from database import *
import schedule
from datetime import datetime
import copy
import time
import _thread
import threading


# transition
    # bloqueia o estado atual na instancia.
    # cria um novo estado
    # atualiza estado atual no Instance e libera o bloqueio
    # atualiza o history_entry (monitor passa a linha do history)
    # Inserir o novo estado nas filas

def avalia_trigger(condition, state, dao):
    
    predicate = condition.predicates;

    results = list()

    list1 = predicate.split(',')
    for p in list1:

        list2 = p.split(' ')
        print('list2: ', list2)
        print('state: ', state.id)
        attr1 = getattr(state, list2[0])
        print('attr1: ' , attr1 , '\nattr2', list2[2])
        if attr1 == list2[2]:
            results.append(True)
        else:
            results.append(False)


    expressions = condition.expression

    print('len: ' , len(results))
    print('result: ' , results)
    if len(results) == 1:
        print('iff')
        return results[0]
    else:
        listExpression = expressions.split(' ')
        if listExpression[2] == "and" and results[0] == True and results[1] == True:
            return True
        elif listExpression[2] == "and":
            return False
        elif listExpression[2] == "or" and (results[0] == True or results[1] == True):
            return True
        else:
            return False 

    #lll.insert(0,True)
    #del lll[0]

def make_func(trigger):
    def _function():
        '''
            recuper a fila da trigger X
            Para cada wed_state da fila avalia a condition da trigger
            se true: dispara a transition
        '''
        dao = DAO()
        fila_wedStates_wedTriggers = dao.select_fila(trigger.id)
        print("..............INICIO.................", trigger.id)

        # update status para processando (feito)
        for i in fila_wedStates_wedTriggers:
            i.status = "processing"
        dao.session.commit()

        for i in fila_wedStates_wedTriggers:
            result = avalia_trigger(trigger.wed_condition, dao.select_state(i.wed_state_id)[0], dao)
            
            if(result == True):
                # Criar a entrada no history_entry
                print(i.wed_state_id)
                print(dao.select_state(i.wed_state_id)[0].id)
                bla = dao.select_state(i.wed_state_id)[0]
                print(bla)
                instance = dao.select_instance(bla.instance_id)[0]
                
                
                history_entry = History_entry(create_at = datetime.now(), instance_id = instance.id, \
                    initial_state_id = i.wed_state_id, wed_transition_id = i.wed_trigger.wed_transition_id) # FALTA O INTERRUPTION
                
                dao.session.add(history_entry)
                dao.session.commit()
                
                transition = i.wed_trigger.wed_transition
                print('name t: ' , transition.name)
                # Carrega a classe da transition
                package = __import__("transitions")
                
                module = getattr(package, transition.name)
                class_ = getattr(module, transition.name)

                # cria e inicia a thread da transition
                try:
                    print("aaa " , transition.name)
                    _thread.start_new_thread(class_.run, (instance.id, history_entry.id))
                   # _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
                except:
                   print ("Error: unable to start thread")


        # update para processado (finish)
        for i in fila_wedStates_wedTriggers:
            i.status = "finish"
        dao.session.commit()
        
        print("....................FIM.................", trigger.id)


    return _function




def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

if __name__ == '__main__':
    dao = DAO()
    result = dao.select_trigger()
    for i in result:
        job = make_func(i)
        schedule.every(i.period).seconds.do(run_threaded, job)

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)

        except KeyboardInterrupt:
            schedule.clear()
            print("\nBye")
            exit(0)
