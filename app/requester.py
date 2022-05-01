import subprocess
import requests
from random import randint
import json
import os
import subprocess
from music21 import converter
from mido import MidiFile
from aitextgen import aitextgen

channelMap = {0: "V:0", 1: "V:1", 2: "V:2", 3: "V:3",4: "V:4"}

def requestMidi(seed):

    PATH = "."
    songname = f"{randint(0,9999):04d}"
    OUTDIR = "."

    prompt=f"""X:1
    T:Music21 Fragment
    C:Music21
    %%score 1 2 3 4
    L:1/8
    Q:1/4=180
    M:4/4
    I:linebreak $
    K:none
    V:1 treble nm="Brass" snm="Brs"
    V:2 treble nm="Brass" snm="Brs"
    V:3 bass nm="Fretless Bass" snm="Gtr"
    V:4 bass nm="Percussion" snm="Perc"
    """

    tokenizer = "/model/aitextgen.tokenizer.json"
    model_folder = "/model/MIDI_15"
    ai = aitextgen(model_folder=model_folder,tokenizer_file=tokenizer)

    text = ai.generate_one(prompt=prompt,max_length=2048,temperature=0.9,seed=seed)

    print(text,flush=True)

    abcfile = os.path.join(PATH,songname + ".abc")

    print("Save the .abc file")
    with open(abcfile,"w") as f:
        f.write(text)

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
    return midi,songname

# the previous midi track is used as the new prompy
def modifyMidi(seed,tracks,oldMidi):

    PATH = "."
    songname = f"{randint(0,9999):04d}"
    OUTDIR = "."

    tokenizer = "/model/aitextgen.tokenizer.json"
    model_folder = "/model/MIDI_15"


    songname = oldMidi.split(".")[0]
    xmlname = songname + ".musicxml"
    xmlout = os.path.join(OUTDIR,xmlname)

    # convert midi to xml to abc
    converter.parseFile(oldMidi).write("musicxml",fp=xmlout)
    command = ["python","xml2abc.py",xmlout,"-u","-o",OUTDIR]
    subprocess.run(command)

    abcname = songname + ".abc"
    prompt = ""
    marked = False

    # read in the abc file
    with open(abcname,"r") as f:
        for line in f:
            first = line.split(" ")[0][0:3]
            if first == channelMap[tracks+1]:

                # stop the prompt at the specified channel
                if marked:
                    prompt += first
                    break
                marked = True
            prompt += line

    # print(prompt,flush=True)

    ai = aitextgen(model_folder=model_folder,tokenizer_file=tokenizer)
    text = ai.generate_one(prompt=prompt,max_length=2048,temperature=0.9,seed=seed)

    # print(text,flush=True)

    abcfile = os.path.join(PATH,songname + ".abc")

    # write the completions text to an abc file
    with open(abcfile,"w") as f:
        f.write(text)

    # xml to midi pipeline
    xmlout = os.path.join(PATH,songname + ".xml")
    midiout = os.path.join(PATH,songname + ".mid")
    command = ["python","abc2xml.py",abcfile,"-o",PATH]
    process = subprocess.run(command)

    print("Converting xml to midi")
    midi = converter.parseFile(xmlout).write("midi",fp=midiout)
    print(midi)
    return midi,songname