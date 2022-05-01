from requester import modifyMidi
import io
import os
import base64

PATH = "/tmp/"

def base64toString(b):
    return base64.b64encode(b).decode("utf-8")

def lambda_handler(event,context):

    seed = int(event["seed"])
    midiString = event["midi"].split(",")[1] # remove prefixes
    tracks = int(event["tracks"])

    newSong = "new.mid"

    # write midi bytes to file
    with open(newSong,"wb") as f:
        f.write(stringtoBase64(midiString))

    midi = modifyMidi(seed,tracks,newSong)
    songname = midi.split(".")[0]
    midiData = None

    with open(midi,"rb") as f:
        midiData = f.read()

    # remove the songs
    try:
        os.remove(os.path.join(PATH,songname + ".mid"))
        os.remove(os.path.join(PATH,songname + ".xml"))
        os.remove(os.path.join(PATH,songname + ".abc"))
    except:
        print("Song files were not present!")

    message = {
   'message': 'Execution started successfully!'
    }
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET' 
        },
        'body': base64toString(midiData)
    }