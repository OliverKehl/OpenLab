import web,json
from azurecli import *
from rest_server import *
urls = ('/(.*)', 'index')
class index:
    def GET(self,tag):
        #do some thingi 
        web.input(tag=None)
        if tag=='python':
            vm_list = get_
            get_virtual_machine_status()
            pyDict = {'hostname':'khost','username':'kangjihua','password':'opentech','port':'8080'}
            web.header('Content-Type', 'application/json')
            return json.dumps(pyDict)
        else:
            return 'Hello world'


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()