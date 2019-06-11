from flask import Flask, request,  url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import urllib.parse
from sqlalchemy import create_engine
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
    engine.execute("INSERT INTO test (name) VALUES ('JJI')")
    choice = request.args.get("Poll","")
    return "Hello {}!".format(choice)
