import cherrypy
import mako.template
import os.path

PYPATH = os.path.dirname(__file__)

class App:
    @cherrypy.expose
    def index(self):
        return "I like pie!"

    @cherrypy.expose
    def test(self):
        t = mako.template.Template(filename=f"{PYPATH}/../html/test.html")
        return t.render(foobar=42)

app = App()
cherrypy.quickstart(app)