import subprocess
import requests
from random import randint
import json
import os
import subprocess
from music21 import converter
from mido import MidiFile
from abc2xmlinmem import translateABC # translation without filesystem

def requestMidi3():

    URL = "https://api.openai.com/v1/completions"
    TOKEN = "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"

    songname = f"{randint(0,9999):04d}"

    REQ_FILE = "request2.json"
    OUTDIR = "./"
    request = {}


    # load request file
    with open(REQ_FILE,"r") as f:
        request = json.load(f)

    # add key to request
    request["prompt"] = f"{randint(0,23)} ->"

    print("Sending Request to Server")

    r = requests.post(url=URL,json=request,headers={'Authorization': 'Bearer {}'.format(TOKEN)})

    print(f"Response: {r.status_code}")

    # load response into abc file format
    abc = """X:1
    T:Music21 Fragment
    C:Music21\n"""

    data = r.json()["choices"][0]["text"].split("\\n")

    for line in data:
        abc += line + "\n"

    # xml to midi pipeline
    midiout = songname + ".mid"

    print(f"Converting abc to xml")
    translateABC(abc,songname)

    print("Converting xml to midi")
    midi = converter.parseFile(xmlout).write("midi",fp=midiout)
    # midi = converter.parseFile(xmlout)
    return midi


if __name__ == '__main__':
    requestMidi3()
