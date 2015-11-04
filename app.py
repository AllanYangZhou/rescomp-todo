from flask import Flask, render_template, request, jsonify, Response
import os
import sqlite3
from datetime import datetime

from models import TodoItem

app = Flask(__name__, static_url_path='/static')

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'todo.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute('INSERT INTO todos (description, status) VALUES (?, ?)',
            (description, status))
    try:
        c.commit()
    except:
        c.close()
        return Response(response="db error", status=500)
    c.close()
    return Response(response="success", status=200)

@app.route('/list', methods=['GET'])
def list():
    with sqlite3.connect('todo.db') as conn:
        try:
            c = conn.cursor()
            c.execute('SELECT description, status, created_date FROM todos')
            items = [{'description': description, 'status': status, 'created_date': created_date}
                     for description, status, created_date in c.fetchall()]
            result = jsonify(items=items)
        except Exception as e:
            result = Response(response="db error", status=500)
        finally:
            c.close()
    return result

@app.route('/update', methods=['POST'])
def update():
    pass

@app.route('/delete', methods=['GET'])
def delete():
    try:
        id = request.args['id']
        return id
    except:
        return 'bad arguments'

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
