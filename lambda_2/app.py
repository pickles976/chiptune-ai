from requester import requestMidi,requestMidi2
import io
import os
import base64

PATH = "/tmp/"

def base64toString(b):
    return base64.b64encode(b).decode("utf-8")

def lambda_handler(event,context):

    midi = generateMidi()
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