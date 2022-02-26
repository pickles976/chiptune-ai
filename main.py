from requester import requestMidi,requestMidi2
import io
import os
app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


@app.route("/getMidi",methods=["GET"])
@cross_origin()
def getMidi():

    # midi = requestMidi()

    midi,songname = requestMidi2()

    midiData = None

    with open(midi,"rb") as f:
        midiData = f.read()

    os.remove(songname + ".abc")
    os.remove(songname + ".xml")
    os.remove(songname + ".mid")

    # return send_file(midi,mimetype='audio/mid',download_name=songname+".mid")
    return 

    # return send_file("7294.mid",mimetype='audio/mid')

if __name__ == '__main__':
   app.run(debug = True,host="0.0.0.0",port=5000)