from sqlalchemy import create_engine, Integer, Column, ForeignKey, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class History_entry(Base):
    __tablename__ = 'history_entry'
    id = Column(Integer, primary_key = True)
    status = Column(String(50))
    consistent = Column(String(50))
    create_at = Column (DateTime)
    completed_at =  Column (DateTime)

# Initialize the database :: Connection & Metadata retrieval
engine = create_engine("mysql://root@localhost/wedflowdatabase")

# SqlAlchemy :: Session setup
Session = sessionmaker()
session.configure(bind=engine)
#Create all tables that do not already exist
Base.metadata.create_all(engine)
# SqlAlchemy :: Starts a session
