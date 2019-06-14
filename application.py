from flask import Flask, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import urllib.parse
from sqlalchemy import create_engine
from flask import Response
import responses
import json

app = Flask(__name__)

from sqlalchemy.engine import create_engine

engine = create_engine(
    'postgres://%s:Amcompose2019@testamcompose.postgres.database.azure.com/mypgsqldb' % urllib.parse.quote(
        'newuser@testamcompose'))


@app.route("/")
def hello():
    return "Hello A!"


@app.route("/submitResponse", methods=['POST','GET'])
def submitResponse():
    temp=request.data
    temp=temp.decode("utf-8")
    lt = temp.split('#')
    response = lt[0]
    qid=lt[1]
    engine.execute("INSERT INTO responsetemp (qid,response) VALUES (%s,%s)", (qid,response))
    payload = "{\"$schema\": \"https://adaptivecards.io/schemas/adaptive-card.json\",\n\"type\": \"AdaptiveCard\",\"version\": \"1.0\",\n\"body\": [\n{\n\"type\": \"TextBlock\",\n\"text\":\"Succesfully Submitted\",\n\"wrap\": true\n}\n]\n}"
    resp = Response(payload)
    resp.headers['CARD-UPDATE-IN-BODY'] = True
    resp.headers['Content-Type'] = 'application/json'
    return resp
@app.route("/getResponses",methods=['POST'])
def getResponses():
    qid = request.data
    qid = qid.decode("utf-8")
    r=""
    queryChoice = engine.execute("SELECT choice FROM question WHERE qid = %s",qid)
    name = queryChoice.fetchall()
    choices=str(name[0]).split(',')
    choices[0]=choices[0][2:]
    choices[len(choices)-2]=choices[len(choices)-2][:len(choices[len(choices)-2])-1]
    for i in range(len(choices)-1):
        result = engine.execute("SELECT * FROM responsetemp WHERE qid = %s and response= %s", (qid,choices[i]))
        r=r+choices[i]+"= "+ str(result.rowcount)
        r=r+"\n"
    #print(result.rowcount, file=sys.stdout)
    return r
