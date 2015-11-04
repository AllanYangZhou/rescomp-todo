from flask import Flask, render_template, json, request, Response
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
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("INSERT INTO todos ('description', 'status') VALUES (?, ?)",
                (description, status))
    try:
        c.commit()
    except Exception e:
        c.close()
        return Response(response="db error", status=500)
    c.close()
    return Response(response="success", status=200)


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
