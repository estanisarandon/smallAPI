"""
Mini Flask API main file
"""

import os
import json
from dotenv import load_dotenv
from flask import Flask, Response
from models import User

load_dotenv()
MONGODB_URI = os.environ.get('MONGODB_URI')


def create_app():
    """
    Factory function for flask application
    :return: app object
    """
    app = Flask(__name__)

    @app.get('/api/v1.0/first')
    def first_get():
        data = {
            'name': 'Jane',
            'age': 34
        }

        return Response(json.dumps(data), 200, content_type='application/json')

    @app.get('/api/v1.0/second')
    def second_get():
        users = [user.to_dict() for user in User.all()]

        return Response(json.dumps(users), 200, content_type='application/json')

    @app.get('/api/v1.0/third')
    def third_get():
        data = {
            'name': 'Anna',
            'age': 37
        }

        return Response(json.dumps(data), 200, content_type='application/json')


    @app.get('/api/v1.0/forth')
    def forth_get():
        data = {
            'name': 'Joakim',
            'age': 24
        }

        return Response(json.dumps(data), 200, content_type='application/json')

    return app


if __name__ == '__main__':
    create_app().run()
