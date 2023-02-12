


def generate_tab_midi_pairs():
    tab_dict = {}    
    base_midi = [40, 45, 50, 55, 59, 64]
    strings = ['E', 'A', 'D', 'G', 'B', 'e']
    frets = 25
    for string in range(len(strings)):
        for fret in range(frets):
            midi = base_midi[string] + fret
            tab = strings[string] + str(fret)
            if midi in tab_dict:
                tab_dict[midi].append(tab)
            else:
                tab_dict[midi] = [tab]
    return tab_dict

#Cnverts a tab array to a readable tablature format        
def convert_array_to_tab(tab_array): 
    strings = ['e', 'B', 'G', 'D', 'A', 'E']
    tab_string = ''
    for string in strings:
        tab_string += string + '|'
        for i in range(len(tab_array)):
            if string in tab_array[i]:
                tab_string += tab_array[i][1:] + '-' if int(tab_array[i][1:]) > 9 else tab_array[i][1:] + '--'
            else:
                tab_string += '---'
        tab_string += '\n'
    return tab_string

