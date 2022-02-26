from flask import Flask,redirect,request,send_file
from flask_cors import CORS, cross_origin
from requester import requestMidi,requestMidi2
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

    # midi = requestMidi()

    # midi = requestMidi2()

    midi = "4620.mid"
    songname = midi.split(".")[0]
    midiData = None

    with open(midi,"rb") as f:
        midiData = f.read()

    # os.remove(songname + ".abc")
    # os.remove(songname + ".xml")
    # os.remove(songname + ".mid")
    # print(base64toString(midiData))

    return base64toString(midiData)

    # return send_file(midi,mimetype='audio/mid',download_name=songname+".mid")

    # return send_file("7294.mid",mimetype='audio/mid')

if __name__ == '__main__':
   app.run(debug = True,host="0.0.0.0",port=5000)