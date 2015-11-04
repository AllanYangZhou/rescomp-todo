import os

from flask import Flask, render_template, request

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
    db = get_db()
    cur = db.execute('INSERT INTO ')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)

@app.route('/read', methods=['GET'])
def read():
    pass

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

if __name__ == '__main__':
    #if (!os.path.exists('/this/is/a/dir'))
    #con = sqlite3.connect('sqlite.db')
    #with open('dump.sql', 'w') as f:
    #    for line in con.iterdump():
    #        f.write('%s\n' % line)
    app.run(debug=True)
