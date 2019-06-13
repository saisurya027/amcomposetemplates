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

from sqlalchemy.engine import create_engine

engine = create_engine(
    'postgres://%s:Amcompose2019@testamcompose.postgres.database.azure.com/mypgsqldb' % urllib.parse.quote(
        'newuser@testamcompose'))


@app.route("/")
def hello():
    return "Hello A!"


@app.route("/submitResponse", methods=['POST', 'GET'])
def submitResponse():
    choice = request.data

    choice = choice.decode("utf-8")
    #print(choice, file=sys.stderr)
    lt = choice.split('#')
    response = lt[0]
    qid=lt[1]
    engine.execute("INSERT INTO responsetemp (qid,response) VALUES (%s,%s)", (qid,response))
    payload = "{\"$schema\": \"https://adaptivecards.io/schemas/adaptive-card.json\",\n\"type\": \"AdaptiveCard\",\"version\": \"1.0\",\n\"body\": [\n{\n\"type\": \"TextBlock\",\n\"text\":\"Succesfully Submitted\",\n\"wrap\": true\n}\n]\n}"
    resp = Response(payload)
    resp.headers['CARD-UPDATE-IN-BODY'] = True
    resp.headers['Content-Type'] = 'application/json'
    return resp
