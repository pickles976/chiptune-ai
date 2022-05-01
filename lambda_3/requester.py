import subprocess
import requests
from random import randint
import json
import os
import subprocess
from music21 import converter
from mido import MidiFile
import sys

# the previous midi track is used as the new prompy
def modifyMidi(seed,tracks,oldMidi):

    PATH = "/tmp/"
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

    ai = aitextgen(model_folder=model_folder,tokenizer_file=tokenizer,seed=seed)
    text = ai.generate_one(prompt=prompt,max_length=2048,temperature=0.9)

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

if __name__ == "__main__":
    args=sys.argv
    globals()[args[1]](*args[2:])