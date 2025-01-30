import mako.template
import os.path
import data
import random

#location of this file
srcdir = os.path.dirname(__file__)

def get():
    shuffled_images = random.sample(data.image_list, len(data.image_list))  # Shuffle images
    T = mako.template.Template(filename=f"{srcdir}/posts.html")
    return T.render(image_list=shuffled_images)
    
