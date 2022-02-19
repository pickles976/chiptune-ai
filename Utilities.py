import re
import requests
import os
import sys
from mido import MidiFile
import music21
from music21 import converter
import json
import xml2abc
from multiprocessing import Process
import subprocess
from random import randint

# helper function for downloadMidis
def download_file(outdir,url):
        songname = url.split('/')[-1]
        local_filename = os.path.join(outdir,songname)
        files = os.listdir(outdir)
        if songname not in files:

            print(f"Downloading item #{len(files)}")
            
            # NOTE the stream=True parameter below
            with requests.get(url, stream=True) as r:
                r.raise_for_status()
                with open(local_filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192): 
                        # If you have chunk encoded response uncomment if
                        # and set chunk_size parameter to None.
                        #if chunk: 
                        f.write(chunk)
            return local_filename

def getUrls(baseurl,inputfile,outputfile):
    """ Gets the URLs from an HTML webpage

        baseurl (str): The base URL of the page
            - "https://www.vgmusic.com/music/console/nintendo/nes/"
        inputfile (str): Format of the input file
            - "nes.txt"
        outputfile (str): format of the output file
            - "NES_URL.txt"
    """

    results = []
    href = "<a[^>]+href=\"(.*?)\"[^>]*>(.*)?</a>"

    # open webpage
    with open(inputfile,"r") as myFile:

        # loop through the HTML 
        for line in myFile:
            text = re.findall(href,line) # extract all lines with href
            if len(text) > 0 and len(text[0]) > 1: # extract and check for midi files
                mid = text[0][0]
                spl = mid.split(".")
                if len(spl) > 1 and spl[1] == "mid":
                    results.append(mid)

    with open(outputfile,"w") as out:

        for url in results:
            out.write(baseurl + url + "\n")

def downloadMidis(outdir,urlfile):
    """ Downloads the MIDI files from the url file


        outdir (str) output directory
            - "./NES_MIDI"
        urlfile (str): file containing the URL data
            - "NES_URL.txt"
    """
    with open(urlfile,"r") as myFile:

        for line in myFile:
            download_file(outdir,line.replace("\n",""))

    print("Downloads complete!")

def normalizeTracks(indir):
    """ Removes duplicate MIDI tracks
        indir (str): input directory
            - "./NES_MIDI"
    """
    files = os.listdir(indir)

    # loop through all files
    for f in files:

        fullpath = os.path.join(indir,f)

        # try to remove redundant tracks
        try:
            
            print(f"Flattening {f}")

            midi = MidiFile(fullpath, clip=True)

            # remove duplicates
            message_numbers = []
            duplicates = []

            for track in midi.tracks:
                if len(track) in message_numbers:
                    duplicates.append(track)
                else:
                    message_numbers.append(len(track))

            for track in duplicates:
                midi.tracks.remove(track)

            # keep files with proper amount of tracks
            if len(midi.tracks) <= 5 and len(midi.tracks) > 3:
                midi.save(fullpath)
            else:
                os.remove(fullpath)

        except:
            os.remove(fullpath)
            print("Failed to open file!")

def extractKeys(indir,outdir):
    """ Extract the keys and save off to a json file w/ corresponding abc values
        indir (str): input directory
            - "./NES_MIDI"
        outdir (str): output directory
            - "./NES_ABC"
    """

    files = os.listdir(indir)
    d = {}
    count = 0

    for f in files:

        fullpath = os.path.join(indir,f)

        songname = f.split(".")[0]
        abcname = songname + ".abc"

        count += 1
        print(f"{count}/{len(files)} completed")

        try:
            midi = music21.converter.parseFile(fullpath)
            midi_stream = music21.stream.Stream(midi)
            key = midi_stream.analyze("key")

            # remove low-confidence songs
            if key.correlationCoefficient > 0.75:
                sig = str(key)
                print(sig)
                if sig in d:
                    d[sig].append(abcname)
                else:
                    d[sig] = [abcname]
            else:
                os.remove(fullpath)

        except:
            print("Failed to analyze!")
            os.remove(fullpath)

    # write to json
    fn = os.path.join(outdir,"signatures.json")
    with open(fn,"w") as f:
        json.dump(d,f)

def midi2abc(indir,outdir):
    """ Converts all midi files to xml, then abc
        indir (str): input directory 
            - "./NES_MIDI"
        outdir (str): output directory
            - "./NES_ABC"
    """

    files = os.listdir(indir)
    outfiles = os.listdir(outdir)

    for songfile in files:

        songname = songfile.split(".")[0]
        fullpath = os.path.join(indir,songfile)
        abcname = songname + ".abc"

        if abcname not in outfiles:

            try:

                print(f"Converting {abcname}")

                xmlname = songname + ".musicxml"
                xmlout = os.path.join(outdir,xmlname)

                # convert midi to xml temporarily
                converter.parseFile(fullpath).write("musicxml",fp=xmlout)
                command = ["python","xml2abc.py",xmlout,"-u","-o",outdir]
                subprocess.Popen(command)

            except:
                print("Conversion failed!")
                os.remove(fullpath)

def purgeXML(outdir):
    """ Remove all the xml artifacts
            outdir (str): 
                - "./NES_ABC"
    """

    for f in os.listdir(outdir):
        if f.split(".")[1] == "musicxml":
            print(f"Removing file: {f}")
            os.remove(os.path.join(outdir,f))

def jsonl(indir,outfile):
    """ Write out all .abc files to a jsonl for processing

        indir (str): the input directory of the abc files
            - "./NES_ABC"
        keysjson (str): the key signatures json file
            - "signatures.json"
        outfile (str): output file for completions
            - "NES_completions.jsonl"
    """

    files = os.listdir(indir)

    completions = ""
    songnum = 0

    # offset removing boilerplate
    offset = 33

    for song in files:

        fn = os.path.join(indir,song)

        try:

            with open(fn,"r") as songfile:

                data = songfile.read()

                tokens = data.split(" ")
                numtokens = len(tokens)

                # make sure our songs are of a decent length
                if numtokens < 2048 and numtokens > 256:

                    entry = {"prompt" : f"{randint(0,99):02d}",
                        "completion" : " " + data[offset:]} # whitespace character helps training

                    completions += json.dumps(entry) + "\n"
                    songnum += 1

        except:
            print("Song could not be found!")

    print(f"Completions file contains {songnum} songs!")

    with open(outfile,"w") as f:
        f.write(completions)

if __name__ == "__main__":
    args=sys.argv
    globals()[args[1]](*args[2:])