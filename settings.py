import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# define sqlite database file path 
db_dir = os.path.abspath('data.sqlite')

# app settings 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config["DEBUG"] = True
# Database connecting for Linux 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+db_dir+'?check_same_thread=False'

# Database connecting for Windows
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+db_dir
db = SQLAlchemy(app)
