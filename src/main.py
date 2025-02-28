import cherrypy
import os.path
import mako.template
import PIL.Image
import io

#we have modules for each page we're displaying 
import page_index
import page_signup
import page_posts

#the location where the main.py file is stored: The src folder
srcdir = os.path.dirname(__file__)

cherrypy.config.update({'tools.sessions.on': True, 'tools.sessions.storage_type': 'ram'})

def checkImage( data ):
        try:
            MAXSIZE=4096
            tmp = io.BytesIO(data)
            with PIL.Image.open(tmp, formats=["JPEG","PNG"]) as img:
                if img.width > MAXSIZE or img.height > MAXSIZE:
                    return False
            return True
        except PIL.UnidentifiedImageError:
            return False
        except PIL.DecompressionBombError:
            return False

class App:
    @cherrypy.expose
    def index(self):
        # Retrieve the most recent post from the session
        recent_post = cherrypy.session.get('recent_post')
        
        # If no recent post exists, provide fallback title and image
        if recent_post:
            title = recent_post['title']
            image_src = "/mostrecent"
        else:
            title = "No Post Available"
            image_src = "/mostrecent"  # Placeholder image

        # Pass the data to the index_page for rendering
        return page_index.get(title, image_src)
    
    @cherrypy.expose
    def signup(self):
        return page_signup.get()
    @cherrypy.expose
    def posts(self):
        return page_posts.get()

    @cherrypy.expose
    def makepost(self):
        with open(f"{srcdir}/../html/makepost.html") as fp:
            return fp.read()
        
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def make_post(self, name, pic): # Need to check why params, sessions, worked!!!!!!
        # Get the name and picture from the form data
        name = cherrypy.request.params.get('name')
        pic = cherrypy.request.params.get('pic')  # This is where the file is stored
        
        # Check if a title was provided
        if not name or len(name.strip()) == 0:
            return {"ok": False, "reason": "Title is required"}

        if not pic:
            return {"ok": False, "reason": "No file uploaded"}
        
        # Read image data
        img_data = pic.file.read()
        
        # Validate image (check if it's a valid image and within size limits)
        if not checkImage(img_data):
            return {"ok": False, "reason": "Invalid image"}
        
        # Store the data in the session
        cherrypy.session['recent_post'] = {'title': name, 'image_data': img_data}
        
        return {"ok": True}


    @cherrypy.expose
    def mostrecent(self):
        # Retrieve the most recent post from the session
        recent_post = cherrypy.session.get('recent_post')
        
        if not recent_post:
            cherrypy.response.status = 404
            return "No recent post available."

        # Get the raw binary image data
        image_data = recent_post['image_data']
        cherrypy.response.headers["Content-Type"] = "image/jpeg"  # Adjust the content type for your image
        return image_data

app = App()
cherrypy.quickstart(
    app,
    '/',
    {
        "/html": {
            "tools.staticdir.on": True,
            "tools.staticdir.dir": os.path.abspath(f"{srcdir}/../html")
        }
    }
)
