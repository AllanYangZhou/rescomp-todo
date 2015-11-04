import os
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, static_url_path='/static')

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'todo.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    db = get_db()
    cur = db.execute('INSERT INTO ')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)

@app.route('/list', methods=['GET'])
def list():
    pass

@app.route('/read', methods=['GET'])
def read():
    item = TodoItem(117, 'John', False, datetime.now())
    return item.to_json()

@app.route('/update', methods=['POST'])
def update():
    pass

@app.route('/delete', methods=['GET'])
def delete():
    try:
        id = request.args['id']
        return id
    except:
        return 'Illegal arguments.'

if __name__ == "__main__":
    # Create todo.db if non-existent
    if not os.path.exists(app.root_path + '/todo.db'):
        conn = sqlite3.connect('todo.db')
        with open('schema.sql', 'rt') as f:
            schema = f.read()
        print schema
        conn.executescript(schema)
        print("created todo.db")

    # Run the app
    app.run(debug=True)
