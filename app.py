import json

from flask import Flask, request
from mongoengine import ValidationError

from data.Endpoints import Endpoints
from data.Persons import Persons

app = Flask(__name__)


@app.route('/', methods=['POST'])
def root():
    data = json.loads(request.data)
    allowed_types = ['String', 'Int']
    for key, value in data['body'].items():
        if value not in allowed_types:
            return f"{value} is not an allowed type", 400
    endpoint = Endpoints(**data)
    try:
        endpoint.save()
    except ValidationError as e:
        return e.message, 400
    else:
        return f"Created with id {endpoint.id}", 201


if __name__ == '__main__':
    app.run()
