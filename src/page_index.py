import mako.template
import os.path
import random
import data

#location of this file
srcdir = os.path.dirname(__file__)

def get(title, image_src):
    T = mako.template.Template(filename=f"{srcdir}/index.html")
    return T.render(title=title, image_src=image_src)
    
