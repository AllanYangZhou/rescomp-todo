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

@app.route('/add', methods=['POST'])
def create():
    info = request.json
    try:
        description = info['description']
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("INSERT INTO todos ('description') VALUES (?)",
                (description,))
    
        c.commit()
    except:
        c.close()
        return Response(response="db error", status=500)
    c.close()
    return Response(response="ok", status=200)

@app.route('/list', methods=['GET'])
def list():
    with sqlite3.connect('todo.db') as conn:
        try:
            c = conn.cursor()
            c.execute('SELECT id, description, status, created_date FROM todos')
            items = [{ 'id':           id,
                       'description':  description,
                       'status':       status,
                       'created_date': created_date }
                     for id, description, status, created_date in c.fetchall()]
            result = jsonify(items=items)
        except Exception as e:
            result = Response(response="db error", status=500)

    return result

@app.route('/update', methods=['POST'])
def update():
    info = request.json
    try:
        status = info['status']
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()
        c.execute("UPDATE todos SET status=1 WHERE id=?",
                    (id,))
        c.commit()
    except:
        c.close()
        return Response(response="db error", status=500)
    c.close()
    return Response(response="success", status=200)

@app.route('/delete', methods=['DELETE'])
def delete():
    with sqlite3.connect('todo.db') as conn:
        try:
            c = conn.cursor()
            c.execute('DELETE FROM todos WHERE id = ?', (request.json['id'],))
            result = Response(response='ok', status=200)
        except:
            result = Response(response='db error', status=500)

    return result

if __name__ == "__main__":
    # Create todo.db if non-existent
    if not os.path.exists(app.root_path + '/todo.db'):
        conn = sqlite3.connect('todo.db')
        with open('schema.sql', 'rt') as f:
            schema = f.read()
        conn.executescript(schema)
        print("created todo.db")

    # Run the app
    app.run(debug=True)
