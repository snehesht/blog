from flask import Flask
from config import *
import os

# Initilize Flask App
app = Flask(__name__,static_folder='static', static_url_path='')

# Import views after the app is initilized
from views import *

ENV = 'production'
DEBUG_STATUS = False
if ('ENV' in os.environ):
    if (os.environ['ENV'] == 'dev'):
        DEBUG_STATUS = True

print(ENV)

@app.after_request
def add_header(response):
    if (DEBUG_STATUS):
        response.cache_control.no_store = True
        response.cache_control.no_cache = True
    else:
        response.cache_control.max_age = 360000
    return response

if __name__=="__main__":
    app.run(debug=DEBUG_STATUS,host=HOST,port=PORT)
