from mongoengine import Document, StringField, IntField


class Persons(Document):
    name = StringField()
    age = IntField()