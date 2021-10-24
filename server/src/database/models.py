"""
Do not forget
https://stackoverflow.com/questions/710551/use-import-module-or-from-module-import
"""

import database


class FieldOfStudy(database.db.Model):
    id = database.db.Column(database.db.Integer, primary_key=True)
    name = database.db.Column(database.db.String)
