from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'postgres+psycopg2://arthurlin:1234@localhost:5432/telegram'

engine = create_engine(DATABASE_URI, echo=True)

Base = declarative_base()
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

print(User.__table__)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()
ed_user = User(name='ed2', fullname='Ed Jones 2', nickname='edsnickname')
session.add(ed_user)
session.commit()
session.close()

session = Session()
ed_user = User(name='ed3', fullname='Ed Jones 3', nickname='edsnickname')
session.add(ed_user)
session.commit()
session.close()

# conn = engine.connect(
# conn.execute("CREATE TABLE chat_messages( \
#    id serial PRIMARY KEY, \
#    chat_id INTEGER, \
#    message_id INTEGER, \
#    from_user_id INTEGER, \
#    type VARCHAR (30), \
#    text VARCHAR (255), \
#    create_at TIMESTAMP \
# );")

# engine.close()

# try:
#     connection = psycopg2.connect(user = "arthurlin",
#                                   password = "1234",
#                                   host = "127.0.0.1",
#                                   port = "5432",
#                                   database = "postgres")

#     cursor = connection.cursor()
#     # Print PostgreSQL Connection properties
#     print ( connection.get_dsn_parameters(),"\n")

#     # Print PostgreSQL version
#     cursor.execute("SELECT * FROM student")
#     record = cursor.fetchone()
#     print("You are connected to - ", record,"\n")

# except (Exception, psycopg2.Error) as error :
#     print ("Error while connecting to PostgreSQL", error)
# finally:
#     #closing database connection.
#         if(connection):
#             cursor.close()
#             connection.close()
#             print("PostgreSQL connection is closed")
