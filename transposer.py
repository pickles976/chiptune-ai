import music21

def transpose_notes(notes, new_key):
    midi_stream = music21.stream.Stream(notes)
    key = midi_stream.analyze('key')
    print(key,key.correlationCoefficient)
    interval = music21.interval.Interval(key.tonic, new_key.tonic)
    new_stream = midi_stream.transpose(interval)
    return new_stream.notes

the_key = music21.key.Key("C") # C Major

# midi = music21.converter.parseFile("mariotheme.mid")
fp = "mariotheme.mid"
midi = music21.midi.MidiFile()
midi.open(fp)
midi.read()
midi.close()

for track in midi.tracks:
    print(track)

print("file loaded")

# midi to stream
stream = music21.midi.translate.midiFileToStream(midi)

# transpose notes in midi file
new_stream = transpose_notes(stream, the_key)

# stream to midifile
mf = music21.midi.translate.streamToMidiFile(new_stream)

for track in mf.tracks:
    print(track)

mf.open("newmidi.mid","wb")
mf.write()
mf.close()

# print(new_notes)
