import os
from mido import MidiFile

INDIR = "./NES_MIDI"
files = os.listdir(INDIR)

# loop through all files
for f in files:

    fullpath = os.path.join(INDIR,f)

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