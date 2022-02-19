from mido import MidiFile
import os
from music21 import converter
import xml2abc
from multiprocessing import Process
import subprocess

INDIR = "./NES_MIDI"
OUTDIR = "./NES_ABC"

files = os.listdir(INDIR)
outfiles = os.listdir(OUTDIR)

for songfile in files:

    songname = songfile.split(".")[0]
    fullpath = os.path.join(INDIR,songfile)
    abcname = songname + ".abc"

    if abcname not in outfiles:

        try:

            print(f"Converting {abcname}")

            xmlname = songname + ".musicxml"
            xmlout = os.path.join(OUTDIR,xmlname)

            # convert midi to xml temporarily
            songxml = converter.parseFile(fullpath).write("musicxml",fp=xmlout)

            command = ["python","xml2abc.py",xmlout,"-u","-o",OUTDIR]

            process = subprocess.Popen(command)

        except:
            print("Conversion failed!")
            os.remove(fullpath)