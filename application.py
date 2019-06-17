from flask import Flask, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import urllib.parse
from sqlalchemy import create_engine
from flask import Response
import logging
import responses
import json
import sys

app = Flask(__name__)
c=0
from sqlalchemy.engine import create_engine

engine = create_engine(
    'postgres://%s:Amcompose2019@testamcompose.postgres.database.azure.com/postgres' % urllib.parse.quote(
        'newuser@testamcompose'))


@app.route("/")
def hello():
    return "Hello A!"


@app.route("/submitResponse", methods=['POST'])
def submitResponse():
    temp=request.data
    temp=temp.decode("utf-8")
    #return "Hi"
    lt = temp.split('#')
    response = lt[0]
    qid=lt[1]
    engine.execute("INSERT INTO responses (qid,response) VALUES (%s,%s)", (qid,response))
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
    #for i in range(len(choices)):
    #print(choices[0],file=sys.stdout)
    #print(choices[1], file=sys.stdout)
    for i in range(len(choices)-1):
        result = engine.execute("SELECT * FROM responses WHERE qid = %s and response= %s", (qid,choices[i]))
        r=r+choices[i]+"= "+ str(result.rowcount)
        r=r+"\n"
    #print(result.rowcount, file=sys.stdout)
    return r
@app.route("/fetchLatestResponses",methods=['POST','GET'])
def fetchLatestResponses():
    qid = request.data
    qid=qid.decode("utf-8")
    r = []
    queryChoice = engine.execute("SELECT choice FROM question WHERE qid = %s", qid)
    name = queryChoice.fetchall()
    choices = str(name[0]).split(',')
    choices[0] = choices[0][2:]
    choices[len(choices) - 2] = choices[len(choices) - 2][:len(choices[len(choices) - 2]) - 1]
    for i in range(len(choices)-1):
        result = engine.execute("SELECT * FROM responses WHERE qid = %s and response= %s", (qid,choices[i]))
        #r=r+choices[i]+"= "+ str(result.rowcount)
        r.append(result.rowcount)
    payload = "{\n\"$schema\": \"http://adaptivecards.io/schemas/adaptive-card.json\",\n\"originator\": \"863402fa-7924-43fa-a7e1-47293462aaf4\",\n\"type\": \"AdaptiveCard\",\n\"version\": \"1.0\",\n\"body\": [\n"
    for i in range(len(r)):
        if i==len(r)-1:
            payload=payload+"{\n\"type\": \"TextBlock\",\n\"spacing\": \"none\",\n\"text\": \""+choices[i]+"-->"+str(r[i])+"\"\n}\n],\n"
        else :
            payload=payload+"{\n\"type\": \"TextBlock\",\n\"spacing\": \"none\",\n\"text\": \""+choices[i]+"-->"+str(r[i])+"\"\n},\n"
    payload=payload+"\"autoInvokeAction\": {\n\"type\": \"Action.Http\",\n\"method\": \"POST\",\n\"hideCardOnInvoke\": false,\n\"url\": \"https://amcomposetemplate.azurewebsites.net/fetchLatestResponses\",\n\"body\": \""+qid+"\"\n}\n}"
    resp = Response(payload)
    resp.headers['CARD-UPDATE-IN-BODY'] = True
    resp.headers['Content-Type'] = 'application/json'
    return resp
@app.route("/test",methods=['POST'])
def test():
    t="{\n\"$schema\": \"http://adaptivecards.io/schemas/adaptive-card.json\",\n\"originator\": \"863402fa-7924-43fa-a7e1-47293462aaf4\",\n\"type\": \"AdaptiveCard\",\n\"version\": \"1.0\",\n\"body\": [\n{\n\"type\": \"TextBlock\",\n\"spacing\": \"none\",\n\"isSubtle\": true,\n\"text\": \"lala\""
    t=t+"\n}\n],\n\"autoInvokeAction\": {\n\"type\": \"Action.Http\",\n\"method\": \"POST\",\n\"hideCardOnInvoke\": false,\n\"url\": \"https://amcomposetemplate.azurewebsites.net/test\",\n\"body\": \"{}\"\n}\n}"
    resp = Response(t)

    resp.headers['Content-Type'] = 'application/json'
    return resp
