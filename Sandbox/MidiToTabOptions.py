
def generate_tab_midi_pairs():
    tab_dict = {}
    strings = ['E', 'A', 'D', 'G', 'B', 'e']
    base_midi = [40, 45, 50, 55, 59, 64]
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

        
print(generate_tab_midi_pairs())    
