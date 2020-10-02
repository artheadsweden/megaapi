from mongoengine import Document, StringField, IntField, EmbeddedDocumentField, EmbeddedDocument, DictField


class Message(EmbeddedDocument):
    status_text = StringField()
    reason = StringField()


class Endpoints(Document):
    endpoint = StringField(required=True)
    method = StringField()
    response_ok = IntField()
    response_ok_message = EmbeddedDocumentField(Message)
    response_error = IntField()
    response_error_message = EmbeddedDocumentField(Message)
    body = DictField()

