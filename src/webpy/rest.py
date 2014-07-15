import web,json

urls = ('/(.*)', 'index')
class index:
    def GET(self,tag):
        #do some thingi 
        web.input(tag=None)
        if tag=='python':
            pyDict = {'hostname':'khost','username':'kangjihua','password':'opentech','port':'8080'}
            web.header('Content-Type', 'application/json')
            return json.dumps(pyDict)
        else:
            return 'Hello world'
        

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()