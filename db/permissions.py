from peewee import *

from db.conf import db


class User(Model):
    telegram_id = BigIntegerField()
    name = TextField(default='Нет данных')


    class Meta:
        database = db