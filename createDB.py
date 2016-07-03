from database.DAO import *
from database.Readxml import *

dao = DAO()
readxml = Readxml('xml/B1.xml')
readxml.set_dao(dao)
dao.set_readxml(readxml)

dao.drop_tables()
dao.create_tables()
#insere estado inicial no wed_state


dao.insert()