from peewee import *

from db.conf import db
from db.permissions import User
from db.quiz import Answer, PassingAnswer, PassingTest, Question, Tag, Test

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
            Question.tags.get_through_model(),
            Answer,

            Test,
            Test.questions.get_through_model(),

            PassingTest,
            PassingAnswer
        ]

    def init(self):
        self.create_tables()
        self.init_data()

    def create_tables(self):
        db.create_tables(self.models_list)

    def init_test(self, test: Test, question: str, answers: [(str, bool)]):
        question, _ = Question.get_or_create(
            question=question
        )
        for (answer, is_correct) in answers:
            Answer.get_or_create(
                question=question,
                answer=answer,
                is_correct=is_correct
            )

        test.questions.add(question)

    def init_data(self):
        user, _ = User.get_or_create(telegram_id=0)
        test, _ = Test.get_or_create(
            name='Простой тест для теста',
            owner=user,
        )
        self.init_test(
            test,
            "2+2=",
            [
                ("3", False),
                ("25", False),
                ("4", True),
            ]
        )

        self.init_test(
            test,
            "КБ это",
            [
                ("Красное Белое", True),
                ("Компьютерная безопасноть", True),
                ("Конструкторское бюро", True),
            ]
        )
