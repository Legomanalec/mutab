import argparse
import tensorflow.compat.v1 as tf
import ctc_utils
import cv2
import numpy as np
from mido import Message, MidiFile, MidiTrack


parser = argparse.ArgumentParser(description='Decode a music score image with a trained model (CTC).')
parser.add_argument('-image',  dest='image', type=str, required=True, help='Path to the input image.')
parser.add_argument('-model', dest='model', type=str, required=True, help='Path to the trained model.')
parser.add_argument('-vocabulary', dest='voc_file', type=str, required=True, help='Path to the vocabulary file.')
args = parser.parse_args()

tf.reset_default_graph()
sess = tf.InteractiveSession()

# Read the dictionary
dict_file = open(args.voc_file,'r')
dict_list = dict_file.read().splitlines()
int2word = dict()
for word in dict_list:
    word_idx = len(int2word)
    int2word[word_idx] = word
dict_file.close()

# Restore weights
saver = tf.train.import_meta_graph(args.model)
saver.restore(sess,args.model[:-5])

graph = tf.get_default_graph()

input = graph.get_tensor_by_name("model_input:0")
seq_len = graph.get_tensor_by_name("seq_lengths:0")
rnn_keep_prob = graph.get_tensor_by_name("keep_prob:0")
height_tensor = graph.get_tensor_by_name("input_height:0")
width_reduction_tensor = graph.get_tensor_by_name("width_reduction:0")
logits = tf.get_collection("logits")[0]

# Constants that are saved inside the model itself
WIDTH_REDUCTION, HEIGHT = sess.run([width_reduction_tensor, height_tensor])

decoded, _ = tf.nn.ctc_greedy_decoder(logits, seq_len)

image = cv2.imread(args.image,0)
image = ctc_utils.resize(image, HEIGHT)
image = ctc_utils.normalize(image)
image = np.asarray(image).reshape(1,image.shape[0],image.shape[1],1)

seq_lengths = [ image.shape[2] / WIDTH_REDUCTION ]

prediction = sess.run(decoded,
                      feed_dict={
                          input: image,
                          seq_len: seq_lengths,
                          rnn_keep_prob: 1.0,
                      })

str_predictions = ctc_utils.sparse_tensor_to_strs(prediction)

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)


midi_note_dic = {
    "C" : 0,
    "C#": 1,
    "Db": 1,
    "D" : 2,
    "Eb": 3,
    "E" : 4,
    "F" : 5,
    "Gb": 6,
    "G" : 7,
    "G#": 8,
    "Ab": 8,
    "A" : 9,
    "Bb": 10,
    "B" : 11,
    "Cb" :11
}

for w in str_predictions[0]:

    half = int2word[w].split('-', 1)
    note = ""
    if(half[0] == "note"):
        note = half[1].split('_', 1)[0]

        value = ""
        octave = 0
        if(len(note) > 2):
            value = note[0:2]
            octave = note[2:3]
        else:
            value = note[0:1]
            octave = note[1:2]
        midiVal = midi_note_dic.get(value) + (12 * (int(octave) + 1))
        print (int2word[w])
        print(midiVal)

        track.append(Message('program_change', program=12, time=0))
        track.append(Message('note_on', note=midiVal, velocity=64, time=32))
        track.append(Message('note_off', note=midiVal, velocity=127, time=32))
        #print(midi_note_dic.get(value))
        print ('\t'),


mid.save('../../new_song.mid')

#python ctc_predict.py -image ../../mutabdata/Data/Example/000051652-1_2_1.png -model ../../mutabdata/Semantic-Model/semantic_model.meta -vocabulary Data/vocabulary_semantic.txt


