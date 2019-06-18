from flask import Flask, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
import urllib.parse
from sqlalchemy import create_engine
from flask import Response
import logging
import responses
import json
import sys
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
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
@app.route("/sendEmail",methods=['POST'])
def sendEmail():
    qid = request.args.get('qid')
    me = "meganb@M365x814387.onmicrosoft.com"
    you = "meganb@M365x814387.onmicrosoft.com"

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Link"
    msg['From'] = me
    msg['To'] = you

    # Create the body of the message (a plain-text and an HTML version).
    text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
    html = """\
    <html>
    <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
      <script type="application/adaptivecard+json">{
        "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
        "originator": "863402fa-7924-43fa-a7e1-47293462aaf4",
        "type": "AdaptiveCard",
        "version": "1.0",
        "body": [
            {
                "type": "TextBlock",
                "spacing": "none",
                "isSubtle": true,
                "text": "Results will be displayed Soon..."
            }
        ],
        "autoInvokeAction": {
            "type": "Action.Http",
            "method": "POST",
            "hideCardOnInvoke": false,
            "url": "https://amcompose.azurewebsites.net/fetchLatestResponses",
            "body":"""+qid+"""
        }
    }
      </script>
    </head>
    <body>
    Visit the <a href="https://docs.microsoft.com/outlook/actionable-messages">Outlook Dev Portal</a> to learn more about Actionable Messages.
    </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.office365.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('meganb@M365x814387.onmicrosoft.com', 'mahgarg@2642')
    mail.sendmail(me, you, msg.as_string())
    mail.quit()
    return "HELLO"
