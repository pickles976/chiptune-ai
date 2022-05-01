import subprocess
import requests
from random import randint
import json
import os
import subprocess
from music21 import converter
from mido import MidiFile
import sys
from aitextgen import aitextgen

def requestMidi(seed):

    PATH = "/tmp/"
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

    tokenizer = "./model/aitextgen.tokenizer.json"
    model_folder = "./model/MIDI_15"
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
    return midi

if __name__ == "__main__":
    args=sys.argv
    globals()[args[1]](*args[2:])