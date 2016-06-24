from DAO import *
from Readxml import *
import settings

dao = DAO()
readxml = Readxml('../xml/B1.xml')
readxml.set_dao(dao)
dao.set_readxml(readxml)

dao.drop_tables()
dao.create_tables()
dao.insert()