import cherrypy
import os
import redis
import ast
import threading
from threading import Thread
from scrapper import worker
#import pusher
'''
pusher.app_id = app_id
pusher.key = appkey
p = pusher.Pusher()
'''

def getRedisData():
	r = redis.StrictRedis(host='localhost', port=6379, db=0)
	result = r.lrange('nifty_data',0, -1)[0].decode()
	result = ast.literal_eval(result)
	return result

def getTable(data):
    to_show = ['ltp','netPrice','series','openPrice','previousPrice','highPrice','radedQuantity','turnoverInLakhs','lowPrice']
    table = "<table ><thead><tr><th colspan=2>"+data['symbol']+"</th></tr></thead>"
    for key in to_show:
        try:
            table+= "<tr> <td>"+key+" </td><td>"+data[key]+"</td></tr>"
        except:
            pass
    table+= "</table>"
    return table

class Root:
    @cherrypy.expose
    def update(self):
        data = list(getRedisData())
        body=""
        i = 0
        for comp in data:
            if i == 3:
                body+="</div>"
                i =0
            if i==0:
                body+= "<div class='row'>"
            body+="<div class='col s4 '><div class='card blue-grey darken-1 hoverable'><div class='card-content white-text'>"
            body+= getTable(comp)
            body+="</div></div></div>"
            i+=1
        body+="</div>"
        return body

    @cherrypy.expose
    def index(self):
        data = list(getRedisData())
        body=file('info.html').read()
        return body


def cherry():
    configfile = os.path.join(os.path.dirname(__file__),'server.conf')
    cherrypy.quickstart(Root(),config =configfile )

if __name__ == '__main__':
    Thread(target = worker).start()
    Thread(target = cherry).start()