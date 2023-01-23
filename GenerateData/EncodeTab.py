import re

import os


def encodeTab(tab, name, data_name):
    string_array = ['e', 'B', 'G', 'D', 'A', 'E']
    tab_array = []

    for string in string_array:
        tab_reg = re.finditer(string + r'\|(.)*\n', tab, re.MULTILINE)

        fullline = ''
        for matchNum, match in enumerate(tab_reg, start=1):
            fullline = fullline + match.group()
        tab_array.append(fullline)


    string_midi_offset = [64, 59, 55, 50, 45, 40]
        
    encoded_tab_string = ""
    midi_array = []
    for i in range(len(min(tab_array, key=len))):
        for j in range(0, 6):
            if(tab_array[j][i].isnumeric()):
                note = 0
                encoded = 0
                if(tab_array[j][i+1].isnumeric()):
                    note = int(tab_array[j][i])*10 + int(tab_array[j][i+1])
                    encoded = string_array[j] + str(note)
                    midi = string_midi_offset[j]+ note

                elif(tab_array[j][i-1].isnumeric()):
                    continue
                else:
                    note = int(tab_array[j][i])
                    encoded = string_array[j] + str(note)
                    midi = string_midi_offset[j]+note

                encoded_tab_string += encoded + " "
                midi_array.append(midi)

    with open("data/full_tab_string.txt", 'a', encoding="utf-8") as outf:
        outf.write(str(encoded_tab_string))


   

#NEED TO MAKE THE INPUT TO THE RNN AN ARRAY NOT A STRING GOING ONE INDEX AT A TIME
    

