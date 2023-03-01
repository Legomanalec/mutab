from mido import MidiFile

def MidiToArray(input_midi):
    midi_array = []
    mid = MidiFile(input_midi, clip=True)

    for msg in mid.tracks[1]:
        if msg.type == 'note_on':
            midi_array.append(msg.note)
    return midi_array

print(MidiToArray(r"C:\Users\alecr\desktop\mutab\Sandbox\samples\sample.mid"))