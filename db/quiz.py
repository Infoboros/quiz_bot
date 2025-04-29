from peewee import *

from db.conf import db
from db.permissions import User


class Tag(Model):
    name = CharField(unique=True)

    class Meta:
        database = db

    def __str__(self):
        return self.name


class Question(Model):
    owner = ForeignKeyField(User, backref='personal_questions', null=True)
    tags = ManyToManyField(Tag, backref='questions')

    question = TextField()

    class Meta:
        database = db


class Answer(Model):
    question = ForeignKeyField(Question, backref='answers')
    answer = TextField()
    is_correct = BooleanField()

    class Meta:
        database = db


class Test(Model):
    name = CharField(max_length=128)

    owner = ForeignKeyField(User, backref='owner_tests')

    questions = ManyToManyField(Question, backref='tests')

    class Meta:
        database = db


class PassingTest(Model):
    test = ForeignKeyField(Test, backref='passing')
    respondent = ForeignKeyField(User, backref='passing')

    class Meta:
        database = db


class PassingAnswer(Model):
    passing = ForeignKeyField(PassingTest, backref='passing_answers')
    question = ForeignKeyField(Question, backref='passing_answers')

    current_answer = ForeignKeyField(Answer, backref='passing_answers')

    class Meta:
        database = db
