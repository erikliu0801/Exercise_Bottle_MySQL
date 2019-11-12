import bottle
import bottle_mysql
import MySQLdb

app = bottle.Bottle()
# dbhost is optional, default is localhost
plugin = bottle_mysql.Plugin(dbuser='root', dbpass='1234', dbname='opendata')
app.install(plugin)

@app.route('/show/<item>')
def show(item, db):
    db.execute('SELECT * from items where name="%s"', (item,))
    row = db.fetchone()
    if row:
        return template('showitem', page=row)
    return HTTPError(404, "Page not found")