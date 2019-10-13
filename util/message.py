from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

class MessageController():
    def __init__(self, config):
        url = 'postgres+psycopg2://arthurlin:1234@localhost:5432/telegram'
        self.engine = create_engine(url, echo=True)
        self.message = message
        Base.metadata.create_all(engine)

    def search_message(self, search_key):
        return None
    
    def store_message(self, message):
        message = User(
            name = 'ed2', 
            fullname = 'Ed Jones 2', 
            nickname = 'edsnickname'
        )

