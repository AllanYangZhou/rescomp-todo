from flask import Flask, render_template
import os
import sqlite3
app = Flask(__name__, static_url_path="/static")

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
    db = get_db()
    cur = db.execute('INSERT INTO ')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)

@app.route('/read', methods=['GET'])
def read():
    pass


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

@app.route('/update', methods=['POST'])
def update():
    pass

@app.route('/delete', methods=['DELETE'])
def delete():
    pass
