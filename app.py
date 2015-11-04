from flask import Flask, render_template, request, jsonify, Response
import os, sys
import sqlite3

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
    conn = sqlite3.connect('todo.db')
    try:
        description = info['description']
        c = conn.cursor()
        c.execute("INSERT INTO todos ('description') VALUES (?)", (description,))
        c.execute("SELECT created_date FROM todos WHERE id=last_insert_rowid()")
        conn.commit()
        created = c.fetchone()[0]
    except:
        return Response(response="db error", status=500)
    return jsonify({'created' : created})

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
            return jsonify(items=items)
        except:
            return Response(response="db error", status=500)

@app.route('/update', methods=['POST'])
def update():
    info = request.json
    conn = sqlite3.connect('todo.db')
    try:
        status = info['status']
        id = info['id']
        c = conn.cursor()
        c.execute("UPDATE todos SET status=? WHERE id=?", (status,id))
        conn.commit()
    except:
        return Response(response="db error", status=500)

    return Response(response="ok", status=200)

@app.route('/delete', methods=['DELETE'])
def delete():
    with sqlite3.connect('todo.db') as conn:
        try:
            c = conn.cursor()
            c.execute('DELETE FROM todos WHERE id = ?', (request.json['id'],))
            return Response(response='ok', status=200)
        except:
            return Response(response='db error', status=500)

if __name__ == "__main__":
    restart = False
    if len(sys.argv) > 1:
        if sys.argv[1] == 'restart':
            restart = True
    # Create todo.db if non-existent or if args provided
    if not os.path.exists(app.root_path + '/todo.db') or restart:
        conn = sqlite3.connect('todo.db')
        with open('schema.sql', 'rt') as f:
            schema = f.read()
        conn.executescript(schema)
        print("created todo.db")

    # Run the app
    app.run(debug=True)
