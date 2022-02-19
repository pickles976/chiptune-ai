from music21 import converter, interval, pitch, midi

filenameList = ["tetris.mid"]

for fn in filenameList:
    s = converter.parse(fn)
    k = s.analyze('key')
    print(k)
    print(k.correlationCoefficient)
    if k.correlationCoefficient > 0.75:
        i = interval.Interval(k.tonic, pitch.Pitch('C'))
        sNew = s.transpose(i)
        print(sNew.analyze('key'))
        sNew.write("midi","new.mid")