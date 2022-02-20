from flask import Flask,redirect,request,send_file
from flask_cors import CORS, cross_origin
from requester import requestMidi
app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/getMidi",methods=["GET"])
@cross_origin()
def getMidi():

    midi = requestMidi()

    return send_file(midi)

if __name__ == '__main__':
   app.run(debug = True)