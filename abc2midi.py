import subprocess
from music21 import converter
from mido import MidiFile

infile = "4.abc"
song = infile.split(".")[0]
xml = song + ".xml"
midiout = song + ".mid"
OUTDIR = "./"

command = ["python","abc2xml.py",infile,"-o",OUTDIR]
process = subprocess.run(command)

midi = converter.parseFile(xml).write("midi",fp=midiout)
