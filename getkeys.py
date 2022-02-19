import os
import music21
from mido import MidiFile
import json

INDIR = "./NES_MIDI"
files = os.listdir(INDIR)
d = {}
count = 0

for f in files:

    fullpath = os.path.join(INDIR,f)

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

# write to jsoni
with open("signatures.json","w") as f:
    json.dump(d,f)