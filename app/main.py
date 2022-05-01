from requester import requestMidi, modifyMidi
from flask import Flask,redirect,request,send_file
from flask_cors import CORS, cross_origin
import io
import os
import base64
from aitextgen import aitextgen

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

# pre-load model
tokenizer = "/model/aitextgen.tokenizer.json"
model_folder = "/model/GPT_NEO"
ai = aitextgen(model_folder=model_folder,tokenizer_file=tokenizer,to_gpu=True)

# remove forking
os.environ["TOKENIZERS_PARALLELISM"] = "false"

def base64toString(b):
    return base64.b64encode(b).decode("utf-8")

def stringtoBase64(s):
    return base64.decodebytes(s.encode("utf-8"))

@app.route("/getMidi",methods=["POST"])
@cross_origin()
def getMidi():

    seed = int(request.form["seed"])

    app.logger.info(f"request received; seed: {seed}")

    midi,songname = requestMidi(ai,seed)

    midiData = None

    with open(midi,"rb") as f:
        midiData = f.read()

    os.remove(songname + ".abc")
    os.remove(songname + ".xml")
    os.remove(songname + ".mid")

    return base64toString(midiData)

@app.route("/shuffleMidi",methods=["POST"])
@cross_origin()
def shuffleMidi():

    seed = int(request.form["seed"])
    midiString = request.form["midi"].split(",")[1] # remove prefixes
    tracks = int(request.form["tracks"])

    app.logger.info(f"request received; seed: {seed}, tracks: {tracks}")
    # app.logger.info(midiString)

    newSong = "new.mid"

    # write midi bytes to file
    with open(newSong,"wb") as f:
        f.write(stringtoBase64(midiString))

    # use midi file to generate completions
    midi,songname = modifyMidi(ai,seed,tracks,newSong)

    # load midi file into memory
    with open(newSong,"rb") as f:
        midiData = f.read()

    return base64toString(midiData)

if __name__ == '__main__':
   app.run(debug = True,host="0.0.0.0",port=5000)
