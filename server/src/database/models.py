import enum
import sqlalchemy
import server.src.database.database as db


class FieldOfStudy(db.db.Model):
    id = db.db.Column(db.db.Integer, primary_key=True)
    name = db.db.Column(db.db.String)
    print('hi')
