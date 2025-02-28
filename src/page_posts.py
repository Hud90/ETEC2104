import mako.template
import os.path
import data
import random

#location of this file
srcdir = os.path.dirname(__file__)

def get():
    shuffled_images = random.sample(data.image_list, len(data.image_list))  # Shuffle images
    shuffled_age = random.sample(data.post_age, len(data.post_age))
    shuffled_views = random.sample(data.views, len(data.views))
    T = mako.template.Template(filename=f"{srcdir}/posts.html")
    return T.render(image_list=shuffled_images, post_age=shuffled_age, views=shuffled_views)
    
