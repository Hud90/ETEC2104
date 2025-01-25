import cherrypy
import os.path
import mako.template

#we have modules for each page we're displaying 
import page_index
import page_signup
import page_posts

class App:
    @cherrypy.expose
    def index(self):
         return page_index.get()
    @cherrypy.expose
    def signup(self):
        return page_signup.get()
    @cherrypy.expose
    def posts(self):
        return page_posts.get()

        
#the location where the main.py file is stored: The src folder
srcdir = os.path.dirname(__file__)

app = App()
cherrypy.quickstart(
    app,
    '/',
    {
        "/html": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": f"{srcdir}/../html"
        }
    }
)
