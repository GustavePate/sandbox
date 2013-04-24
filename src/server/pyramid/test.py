from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response 



"""
//commentaire
//
//comment
"""
#@decorator
def hello_world(request): 
        return Response('Hello %(name)s!' % request.matchdict) 

def func():
        i=1
        print 'ok'
        print "tg"
        lst=[]
        lst.append(['a',789])
        lst.append('ok')
        lst.
        lst.append('ok')

if __name__ == '__main__': 
    
    config = Configurator() 
    config.add_route('hello', '/hello/{name}') 
    config.add_view(hello_world, route_name='hello') 
    app = config.make_wsgi_app() 
    server = make_server('0.0.0.0', 8080, app) 
    server.serve_forever()
    lst=['a']
    lst.pop()
    print "ok"

