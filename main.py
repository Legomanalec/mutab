from mido import MidiFile
import numpy as np
import tensorflow as tf

#pip3 install --upgrade https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.0-py3-none-any.whl

#read in midi
mid = MidiFile('TAKEFIVE.mid', clip=True)
print(mid)


#base guitar
guitar = np.array([[40], [45], [50], [55], [59], [64]])
for x in range(22):
    guitar = [np.append(a, a[0]+x+1) for a in guitar]
        

#extract notes from midi into numpy array
arr = np.array([])
for msg in mid.tracks[0][:50]:
    if msg.type == 'note_on':
        arr = np.append(arr, msg.note)
print(arr)



#Setup new fretboard
minNote = arr.min()

def getGuitarPosition(min):
    return np.where(guitar[int((minNote - 50)) // 5] == min)[0]

min_offset = getGuitarPosition(minNote)
guitarMod = np.array([[40+min_offset], [45+min_offset], [50+min_offset], [55+min_offset], [59+min_offset], [64+min_offset]])
for x in range(4):
    guitarMod = [np.append(a, a[0]+x+1) for a in guitarMod]
for x in guitarMod:
    print(x) 


#Make tab array and print
tab = np.full((6, arr.size), '---')


def getIndex(note):
    for i in range(6):
        for j in range(5):
            if guitarMod[i][j] == note:
                return (j, i)

k = 0
for i in arr:
    x_y_tup = getIndex(i)
    x = x_y_tup[0] + 7
    y = x_y_tup[1]
    if(x < 10):
        tab[y][k] = str(x) + '--'
    else:
        tab[y][k] = str(x) + '-'

    k+=1


for x in range(6):
    for y in range(arr.size):
        print(tab[5-x][y], end='')
    print()



