from DAO import *
import settings

dao = DAO()
dao.drop_tables()
dao.create_tables()
dao.insert()