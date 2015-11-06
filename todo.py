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
    """ LOOK AT THIS EXAMPLE """
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
    """ FILL IN THIS FUNCTION """
    pass

@app.route('/update', methods=['POST'])
def update():
    """ FILL IN THIS FUNCTION """
    pass

@app.route('/delete', methods=['DELETE'])
def delete():
    """ FILL IN THIS FUNCTION """
    pass

if __name__ == "__main__":
    # "python app.py restart" to delete db
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
