from database import *

if __name__ == '__main__':
    dao = DAO()
    readxml = Readxml('xml/B3.xml')

    lista = readxml.data_wed_attributes()
    
    for i in range(1):
    	dao.insert_wed_state(lista)


    


