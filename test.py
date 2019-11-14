import os
import bottle
import bottle_mongo
from bottle import route, run ,template
import bottle_mysql
from bottle import Bottle ,redirect
from bottle.ext.mongo import MongoPlugin
from bson.json_util import dumps

index_html = "My first web app! By <strong>{{ author}}</strong>."
app = bottle.Bottle()
plugin = bottle_mysql.Plugin(dbuser = 'root', dbpass='1234')
app.install(plugin)

@route('/')
def index():
	return template(index_html, author = 'Erik')

@route('/name/<name>')
def name(name):
    return template(index_html, author=name)


# @route('/show/:<tem>')
# def show(item, db):
# 	db.execute('SELECT * from items where name="%s"',(item,))
# 	row = db.fetchone()
# 	if row:
# 		return template('showitem',page=row)
# 	return HTTPError(404, "Page not found")

# app = Bottle()
# plugin = MongoPlugin(uri="mongodb://127.0.0.1",db="mydb",json_mongo=True)
# app.install(plugin)

# @app.route('/',method='GET')
# def index(mongodb):
# 	return dumps(mongodb['collection_name'].find())

# @app.route('/',method='POST')
# def create(mongodb):
# 	mongodbb['collection_name'].instert({'key1':int, 'key2':int})
# 	redirect("/")

if __name__ == '__main__':
	port = int(os.environ.get('PORT',8080))
	run(host='0.0.0.0',port=port,debug = True)
