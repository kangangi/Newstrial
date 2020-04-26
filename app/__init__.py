from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap 



#initializing flask application
app = Flask(__name__,instance_path='/mnt/c/Users/User/Documents/moringa-school-core/Flask/NewAPI/app',instance_relative_config= True)

#setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

#Initializing Flask Extension
#bootstrap = Bootstrap(app)
from app import views

