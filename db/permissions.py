from peewee import *

from db.conf import db


class User(Model):
    telegram_id = BigIntegerField()


    class Meta:
        database = db