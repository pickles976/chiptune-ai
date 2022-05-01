import subprocess
import requests
from random import randint
import json
import os
import subprocess
from music21 import converter
from mido import MidiFile
import sys

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
    PATH = "/tmp/"

    songname = f"{randint(0,9999):04d}"

    OUTDIR = "."
    request = {
        "prompt": "",
        "temperature": 0.95,
        "max_tokens": 2046,
        "model": "curie:ft-personal-2022-02-22-03-23-51",
        "top_p": 1,
        "frequency_penalty": 0,
        "presence_penalty": 0,
        "stop": "[END]"
        }

    try:

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

        abcfile = os.path.join(PATH,songname + ".abc")

        print("Save the .abc file")
        with open(abcfile,"w") as f:
            f.write(music)

        # xml to midi pipeline
        xmlout = os.path.join(PATH,songname + ".xml")
        midiout = os.path.join(PATH,songname + ".mid")

        print(f"Converting {abcfile} to {xmlout}")
        command = ["python","abc2xml.py",abcfile,"-o",PATH]
        process = subprocess.run(command)

        print(os.listdir())
        print(os.listdir(PATH))

        print("Converting xml to midi")
        midi = converter.parseFile(xmlout).write("midi",fp=midiout)
        print(midi)
        return midi

    except:
        print("Failed!")

if __name__ == "__main__":
    args=sys.argv
    globals()[args[1]](*args[2:])