from flask import Flask,redirect,request,send_file
from flask_cors import CORS, cross_origin
from requester import requestMidi,requestMidi2
app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/getMidi",methods=["GET"])
@cross_origin()
def getMidi():

    # midi = requestMidi()
    midi = requestMidi2()
    return send_file(midi,mimetype='audio/mid')

    # return send_file("2281.mid",mimetype='audio/mid')

if __name__ == '__main__':
   app.run(debug = True,host="0.0.0.0",port=5000)