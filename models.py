from mongo_document import db, Document


class User(Document):
    collection = db.users
