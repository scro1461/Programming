from tinydb import TinyDB, Query
from bottle import route, run, template

@route('/test')
def test(name='It works'):
    return template('index', name = name)

run()
















