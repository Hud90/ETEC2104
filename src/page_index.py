import mako.template
import os.path

#location of this file
srcdir = os.path.dirname(__file__)

def get():
    T = mako.template.Template(filename=f"{srcdir}/index.html")
    return T.render()
    
