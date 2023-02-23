from mido import MidiFile

def MidiToArray():
    midi_array = []
    mid = MidiFile(r'C:\Users\alecr\desktop\mutab\data\0\Stairway To Heaven.mid', clip=True)

    for msg in mid.tracks[1]:
        if msg.type == 'note_on':
            midi_array.append(msg.note)
    return midi_array
