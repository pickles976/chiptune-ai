from requester import requestMidi3
from flask import Flask,redirect,request,send_file
from flask_cors import CORS, cross_origin
import io
import os
import base64

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

def base64toString(b):
    return base64.b64encode(b).decode("utf-8")

@app.route("/getMidi",methods=["GET"])
@cross_origin()
def getMidi():

    app.logger.info("request received")

    midi,songname = requestMidi3()

    midiData = None

    with open(midi,"rb") as f:
        midiData = f.read()

    os.remove(songname + ".abc")
    os.remove(songname + ".xml")
    os.remove(songname + ".mid")

    return base64toString(midiData)

    # info needed for lambda
    # return {
    #     'statusCode': 200,
    #     'headers': {
    #         'Content-Type': 'application/json',
    #         'Access-Control-Allow-Headers': 'Content-Type',
    #         'Access-Control-Allow-Origin': '*',
    #         'Access-Control-Allow-Methods': 'OPTIONS,POST,GET' 
    #     },
    #     'body': base64toString(midiData)
    # }

if __name__ == '__main__':
   app.run(debug = True,host="0.0.0.0",port=5000)
