import re

from midiutil.MidiFile import MIDIFile
import os




def midiToTab(tab, name, data_name):
    string_array = ['e', 'B', 'G', 'D', 'A', 'E']
    tab_array = []

    for string in string_array:
        tab_reg = re.finditer(string + r'\|(.)*\n', tab, re.MULTILINE)

        fullline = ''
        for matchNum, match in enumerate(tab_reg, start=1):
            fullline = fullline + match.group()
        tab_array.append(fullline)



    #Put in new file
    mf = MIDIFile(1)     
    track = 0   
    time = 0    
    mf.addTrackName(track, time, name)
    mf.addTempo(track, time, 120)
    channel = 0
    volume = 100

    string_midi_offset = [64, 59, 55, 50, 45, 40]

    time = 0

    for i in range(len(min(tab_array, key=len))):
        note = False
        for j in range(0, 6):
            if(tab_array[j][i].isnumeric()):
                if(tab_array[j][i+1].isnumeric()):
                    note = string_midi_offset[j]+(int(tab_array[j][i])*10 + int(tab_array[j][i+1]))
                    mf.addNote(track, channel, note, time, 0.5, volume)
                elif(tab_array[j][i-1].isnumeric()):
                    continue
                else:
                    mf.addNote(track, channel, string_midi_offset[j]+int(tab_array[j][i]), time, 0.5, volume)
                note = True
        if(note):
            time+=0.5

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../data/' + str(data_name))
    os.mkdir(filename)

    with open("data/" + str(data_name) + "/" + str(name) + ".mid", 'wb') as outf:
        mf.writeFile(outf)
    with open("data/" + str(data_name) + "/" + str(name) + ".txt", 'w', encoding="utf-8") as outf:
        outf.write(tab)
