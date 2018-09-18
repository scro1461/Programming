from tinydb import TinyDB, Query
from bottle import route, run

to_do_listDB = TinyDB('to_do.json')

to_do_listDB.insert({'Name':'Jamie'})
to_do_listDB.insert({'Name':'Aimee'})

def printDB(a):
    for item in a:
        print(item)

@route('/todo')
def todo():
    return str(printDB(to_do_listDB))
run()
















