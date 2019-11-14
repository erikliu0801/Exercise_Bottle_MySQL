import bottle
from bottle import route, run, template, app, HTTPError
from bottle import request, response
from bottle import post, get, put, delete

testAPI = [{
    "objectID" : "001",
    "device" : "container",
    "Info" : {
        "price" : "NT100" ,
        "productionTime" : "2015"
    }
},
{
    "objectID" : "002",
    "device" : "container",
    "Info" : {
        "price" : "NT100" ,
        "productionTime" : "2015"
    }
},
{
    "objectID" : "003",
    "device" : "container",
    "Info" : {
        "price" : "NT100" ,
        "productionTime" : "2015"
    }
}
]

#
@get('/get') #ok
def getAll():
    return {'testAPI':testAPI}

@get('/get/<objectID>') #ok
def getOne(objectID):
    for i in testAPI:
        if i['objectID'] == str(objectID):
            return i

@post('/post') #ok
def addOne():
    new_object = {'objectID': request.json.get('objectID'),'device': request.json.get('device'),'Info': request.json.get('Info')}
    testAPI.append(new_object)
    return {'testAPI':testAPI}

@delete('/remove/<objectID>') #ok
def removeOne(objectID):
    for i in testAPI:
        if i['objectID'] == str(objectID):
            testAPI.remove(i)
    return {'testAPI':testAPI}
    
from bottle import error
@error(404)
def error404(error):
    return 'Nothing here, error404'

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)



