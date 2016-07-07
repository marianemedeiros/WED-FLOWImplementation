from database import *

if __name__ == '__main__':
    dao = DAO()
    readxml = Readxml('xml/sequencial.xml')

    lista = readxml.data_wed_attributes()
    

    for i in range(50):
    	print(i)
    	dao.insert_wed_state(lita)


    



# from database import *
# import threading

# def inser_fila():
#     dao = DAO()
#     readxml = Readxml('xml/B3.xml')
#     lista = readxml.data_wed_attributes()

#     # dao.insert_wed_state(lista)

# def run_threaded(job_func):
#     job_thread = threading.Thread(target=job_func)
#     job_thread.start()

# if __name__ == '__main__':
#     # dao = DAO()
#     # readxml = Readxml('xml/B3.xml')

#     # lista = readxml.data_wed_attributes()
    
#     for i in range(50):
#         run_threaded(inser_fila)
#         # dao.insert_wed_state(lista)


    


