from peewee import *

from db.conf import db
from db.permissions import User


class Tag(Model):
    name = CharField(unique=True)

    class Meta:
        database = db

class Question(Model):
    owner = ForeignKeyField(User, backref='personal_questions', null=True)
    tags = ManyToManyField(Tag, backref='questions')

    question = TextField()
    answer = TextField()

    class Meta:
        database = db


class Test(Model):
    name = CharField(max_length=128)

    owner = ForeignKeyField(User, backref='owner_tests')
    respondent = ManyToManyField(User, backref='respondent_tests')

    questions = ManyToManyField(Question, backref='tests')

    class Meta:
        database = db
