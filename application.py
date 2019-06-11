from flask import Flask, request,  url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import urllib.parse
from sqlalchemy import create_engine
import logging
app = Flask(__name__)

from sqlalchemy.engine import create_engine
engine = create_engine('postgres://%s:Amcompose2019@testamcompose.postgres.database.azure.com/mypgsqldb' % urllib.parse.quote('newuser@testamcompose'))

@app.route("/")
def hello():
    return "Hello A!"
@app.route("/submitResponse",methods=['POST','GET'])
def submitResponse():
    #sys.stdout = open('\home\LogFiles\app.log','w')
    #print(request.data)
    choice = request.data
    logging.debug(type(choice))
    choice = choice.decode("utf-8") 
    engine.execute("INSERT INTO test (name) VALUES (%s)",(choice))
    return "Hello {}!".format(choice)
