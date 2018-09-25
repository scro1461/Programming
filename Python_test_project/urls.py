from tinydb import TinyDB, Query
from bottle import route, run, template, static_file

#Login Page - Login_screen Template
@route('/')
def home():
    return template('login_screen')

@route('/<filename:path>')
def server_static(filepath):
    return static_file(filepath, root='/.Views/static_files/')









run(reloader=True,debug=True)

# lsof -i tcp: PORT NUMBER
# kill -9 <PID>i















