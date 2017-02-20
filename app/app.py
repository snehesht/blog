from flask import Flask
from config import *

# Initilize Flask App
app = Flask(__name__,static_folder='static', static_url_path='')

# Import views after the app is initilized
from views import *

# @app.after_request
# def add_header(response):
#     response.cache_control.max_age = 360000
#     response.cache_control.no_store = True
#     return response

if __name__=="__main__":
    app.run(debug=DEBUG_STATUS,host=HOST,port=PORT)
