import configparser
from dataclasses import dataclass
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Message(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer)
    message_id = Column(Integer)
    user_id = Column(Integer)
    chat_type = Column(String)
    text = Column(String)
    timestamp = Column(String)

class MessageController():
    def __init__(self, config):
        self.mm = "MMMMM"
        url = 'postgres+psycopg2://arthurlin:1234@localhost:5432/telegram'
        self.engine = create_engine(url, echo=True)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    # TODO: cahce message and bulk commit at once.
    def get_message(self, update, context):
        message = Message(
            chat_id = update.message.chat.id,
            message_id = update.message.message_id,
            user_id = update.message.from_user.id,
            chat_type = update.message.chat.type,
            text = update.message.text,
            timestamp = update.message.date,
        )

        # TODO: try cache and close at finalliy
        print(message)
        session = self.Session()
        self.save_message(message, session)
        session.commit()
        session.close()

    def search_message(self, update, context):
        key = ' '.join(update.message.text.split()[1:])
        session = self.Session()
        result = self.query_message(key, session)
        for row in result:
            print(row.text)
            result = context.bot.send_message(
                chat_id = row.chat_id,
                reply_to_message_id =row.message_id,
                text=f"Search for {row.text}"
            )

        session.commit()
        session.close()

    def save_message(self, message, session):
        session.add(message)
    
    def query_message(self, key, session):
        return session.query(Message).filter(Message.text.like(f'%{key}%'))

def search_message():
    return None

def search(update, context):
    text = update.message.text.split()[1:]
    chat_id = update.message.chat.id
    message_id = update.message.message_id 

    result = context.bot.send_message(chat_id=chat_id, reply_to_message_id=1, text=f"Search for {text}")
    print(result)

def main():
    # Load data from config.ini file
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Create database and Session
    msg_ctl = MessageController("")

    # Create Updater object and attach dispatcher to it
    updater = Updater(config['TELEGRAM']['ACCESS_TOKEN'], use_context=True)
    dispatcher = updater.dispatcher
    print("Bot started")

    # Add command handler to dispatcher
    search_handler = CommandHandler('search', msg_ctl.search_message)
    message_handler = MessageHandler(Filters.text, msg_ctl.get_message)

    dispatcher.add_handler(search_handler)
    dispatcher.add_handler(message_handler)

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

def develop():
    print("DEVELOP")
    message_ctl = MessageController("HOHOHO")
    print(message_ctl.get_message())


if __name__ == '__main__':
    main()
    # develop()
