import os
from abc import ABC
from dotenv import load_dotenv
from pymongo import MongoClient

# Loading the connection string from env
load_dotenv()
M_URI = os.environ.get('M_URI')

DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
#DB_HOST = os.environ.get('DB_HOST')
#DB_PORT = os.environ.get('DB_PORT')
#DB_DATABASE = os.environ.get('DB_DATABASE')#

#client = MongoClient(f'mongodb://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}')

#db = client[DB_DATABASE]

client = MongoClient("mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.6xum5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test


class ResultList(list):
    def first_or_none(self):
        return self[0] if len(self) > 0 else None

    def last_or_none(self):
        return self[-1] if len(self) > 0 else None


class Document(ABC):
    collection = None

    def __init__(self, data):
        self.__dict__ = data

    def __repr__(self):
        return '\n'.join(f'{k} = {v}' for k, v in self.__dict__.items())

    def to_dict(self):
        d = self.__dict__
        d['_id'] = str(d['_id'])
        return d

    def save(self):
        if '_id' not in self.__dict__:
            self.collection.insert_one(self.__dict__)
        else:
            self.collection.replace_one({'_id': self._id}, self.__dict__)

    def delete(self):
        self.collection.delete_one(self.__dict__)

    def delete_field(self, field):
        self.collection.update_one({'_id': self._id}, {"$unset": {field: ""}})

    @classmethod
    def all(cls):
        return [cls(item) for item in cls.collection.find()]

    @classmethod
    def insert_many(cls, items):
        for item in items:
            cls(item).save()

    @classmethod
    def delete_many(cls, **kwargs):
        cls.collection.delete_many(kwargs)

    @classmethod
    def find(cls, **kwargs):
        return ResultList(cls(item) for item in cls.collection.find(kwargs))