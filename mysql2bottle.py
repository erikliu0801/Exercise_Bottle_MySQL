import bottle
from bottle import route, run, template, app, HTTPError

@route('/')
def hello():
    return "Hello World!"

#connect db
import MySQLdb
db = MySQLdb.connect(host='localhost',user='root',passwd='',db='dbname')
cursor = db.cursor()
cursor.execute('SELECT * FROM dbTablename')
results = cursor.fetchall()

#api dev
from bottle import get
@get('/get')
def getData():
    import json
    results_json = json.dumps(results)
    return (results_json)

from bottle import error
@error(404)
def error404(error):
    return 'Nothing here, error404'

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)