from flask import jsonify

class TodoItem:
    def __init__(self, id, description, status, created_date):
        self.id = id
        self.description = description
        self.status = status
        self.created_date = created_date

    def to_json(self):
        return jsonify(
                id=self.id,
                description=self.description,
                status=self.status,
                created_date=self.created_date)
