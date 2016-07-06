from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

from sqlalchemy.orm import scoped_session
import database.settings
engine = create_engine(URL(**database.settings.DATABASE), echo=False)
Session = scoped_session(sessionmaker(bind=engine))
