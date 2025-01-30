import mako.template
import os.path
import random
import data

#location of this file
srcdir = os.path.dirname(__file__)

def get():
    name = random.choice(data.names)
    T = mako.template.Template(filename=f"{srcdir}/index.html")
    return T.render(NAME=name)
    
