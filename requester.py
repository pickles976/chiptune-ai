import subprocess
import requests
from random import randint
import json
import os
import subprocess
from music21 import converter
from mido import MidiFile

def requestMidi():

    URL = "https://api.openai.com/v1/completions"
    TOKEN = "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"

    songname = f"{randint(0,9999):04d}"

    KEY_FILE = "keys.json"
    REQ_FILE = "request.json"
    OUTDIR = "./"
    key_dict = {}
    request = {}

    try:

        # get keys
        with open(KEY_FILE,"r") as f:
            key_dict = json.load(f)

        # load request file
        with open(REQ_FILE,"r") as f:
            request = json.load(f)

        # add key to request
        request["prompt"] = key_dict[str(randint(0,23))]

        print("Sending Request to Server")

        r = requests.post(url=URL,json=request,headers={'Authorization': 'Bearer {}'.format(TOKEN)})

        print(f"Response: {r.status_code}")

        # load response into abc file format
        music = """X:1
        T:Music21 Fragment
        C:Music21\n"""

        data = r.json()["choices"][0]["text"].split("\\n")

        for line in data:
            music += line + "\n"

        abcfile = songname + ".abc"

        with open(abcfile,"w") as f:
            f.write(music)

        # xml to midi pipeline
        xmlout = songname + ".xml"
        midiout = songname + ".mid"

        print(f"Converting {abcfile} to {xmlout}")
        command = ["python","abc2xml.py",abcfile,"-o",OUTDIR]
        process = subprocess.run(command)

        print("Converting xml to midi")
        midi = converter.parseFile(xmlout).write("midi",fp=midiout)
        return midi

    except:
        print("Failed!")

def requestMidi2():

    URL = "https://api.openai.com/v1/completions"
    TOKEN = "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"

    songname = f"{randint(0,9999):04d}"

    REQ_FILE = "request2.json"
    OUTDIR = "./"
    request = {}

    try:

        # load request file
        with open(REQ_FILE,"r") as f:
            request = json.load(f)

        # add key to request
        request["prompt"] = f"{randint(0,23)} ->"

        print("Sending Request to Server")

        r = requests.post(url=URL,json=request,headers={'Authorization': 'Bearer {}'.format(TOKEN)})

        print(f"Response: {r.status_code}")

        # load response into abc file format
        music = """X:1
        T:Music21 Fragment
        C:Music21\n"""

        data = r.json()["choices"][0]["text"].split("\\n")

        for line in data:
            music += line + "\n"

        abcfile = songname + ".abc"

        with open(abcfile,"w") as f:
            f.write(music)

        # xml to midi pipeline
        xmlout = songname + ".xml"
        midiout = songname + ".mid"

        print(f"Converting {abcfile} to {xmlout}")
        command = ["python","abc2xml.py",abcfile,"-o",OUTDIR]
        process = subprocess.run(command)

        print("Converting xml to midi")
        midi = converter.parseFile(xmlout).write("midi",fp=midiout)
        return midi

    except:
        print("Failed!")