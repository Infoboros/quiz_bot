from peewee import *

from db.conf import db
from db.permissions import User
from db.quiz import Question, Tag, Test

'''
from db.init import *
InitDB().init()
'''

class InitDB:
    def __init__(self, models_list: [Model] = None):
        self.models_list = models_list or [
            User,
            Tag,
            Question,
            Test,
            Test.questions.get_through_model()
        ]

    def init(self):
        self.create_tables()
        self.init_data()

    def create_tables(self):
        db.create_tables(self.models_list)

    def init_data(self):
        user, _ = User.get_or_create(telegram_id=0)
        Test.get_or_create(
            name='Простой тест для теста',
            owner = user,
        )
