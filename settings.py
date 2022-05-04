#from pickle import FALSE
from flask import Flask, request, Response, jsonify
from flask_sqlalchemy import SQLAlchemy

#creating instance flask
app = Flask(__name__)


#database   sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


