from flask import Flask
from config import *

# Initilize Flask App
app = Flask(__name__)

from views import *

if __name__=="__main__":
	app.run(debug=DEBUG_STATUS,host=HOST,port=PORT)
