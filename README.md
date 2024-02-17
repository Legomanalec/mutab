<h1>1 Overview</h1>
The goal of this project is to allow a mobile app user the ability to take a picture of an excerpt of musican notation and recieve the corresponding guitar tablature 

<h2>1.1 Scope</h2>
The scope of this project is to take in music data from a format such as midi or music xml and return a guitar tablature representation. 

<h1>2 Background</h1>
<h2>2.1 Sheet Music</h2>

<h2>2.2 Optical Music Recognition</h2>
Optical Music Recognition or OMR is a machine learning journey that many researchers have taken on. The goal of this research is to have a machine learning model take an image of sheet music as an input and receieve an encoding of the music as an output. 
<h2>2.1 Guitar Tablature</h2>
Guitar tablature is the most common notation used for guitar music. The was guitar tablature works is by mapping out the neck of the guitar with all 6 strings like so:

e-----|\
B-----|\
G-----|\
D-----|\
A-----|\
E-----|

To represent a note in this notation you simply add the fret number to the desired string like so:

e-5---|\
B-----|\
G-----|\
D-----|\
A-----|\
E-----|

This would mean you are playing an A note as that is that is the note on the 5th fret of the e string. 

<h1>3 Sheet Music to Guitar Tablature</h1>
The ultimate goal of this project is to reliably convert sheet music to guitar tablature using a machine learning model. The reason this problem requires machine learning is because to convert sheet music to guitar tablature is a one-to-many mapping with only a few select viable mappings. When humans translate sheet music to guitar tablature, their own intuition is used to determine if a mapping is viable. 

Guitar tablature to sheet music is a trivial problem to solve. every note on the guitar corresponds to a single note in sheet music notation. However, every note in sheet music notion corresponds to multiple notes in guitar tablature. Using machine learning, the model will be able to determine which one-to-many mapping is closest to how a guitarist would map it using their own intuition.


<h2>3.1 Web Scraping</h2>


<h1>4 How It Works</h1>
Using a recurrent neural network we are able to solve this problem. The network trains on over 500,000 tablature notes in sequence in a textfile. The resulting output is very similar to a text generation model except the output text is contrained to a possible tablature position. This happens by running the model along side the musical note array to sort of guide it in its prediction. For example, if we have a midi note marked as 57 the corresponding tablature notes will be: [G2, D7, A12, E17] the networks job is to determine, based on the previous notes played, which of these tablature options makes the most sense. 

Take this musical excerpt:

![The Lickt](https://b.thumbs.redditmedia.com/w1V7Zqnl2mmeuzw-1S6VaTAlGHlB5BQX1vf57279wpA.png)

The Musical column in this table represents the 7 (transposed) notes from the excerpt above, in order.

| Musical | Midi | Tablature Options       | Pred 1 | Pred 2 | Pred 3 | Pred 4 |
|---------|------|-------------------------|--------|--------|--------|--------|
| A3      | 57   | [G2, D7, A12, E17]      | D7     | A12    | G2     | E17    |
| B3      | 59   | [B0, G4, D9, A14, E19]  | G4     | D9     | B0     | A14    |
| C4      | 60   | [B1, G5, D10, A15, E20] | G5     | D10    | B1     | A15    |
| D4      | 62   | [B3, G7, D12, A17, E22] | G7     | D12    | B3     | A17    |
| B3      | 59   | [B0, G4, D9, A14, E19]  | G4     | D9     | B0     | A14    |
| G3      | 55   | [G0, D5, A10, E15]      | D5     | A10    | G0     | E15    |
| A3      | 57   | [G2, D7, A12, E17]      | D7     | A12    | G2     | E17    |

The next 2 columns are conversions to other notations.

The four prediction columns are feasible tablature options

<h2>5 Resources</h2>

LSTM RNN in Keras: Examples of One-to-Many, Many-to-One & Many-to-Many: https://wandb.ai/ayush-thakur/dl-question-bank/reports/LSTM-RNN-in-Keras-Examples-of-One-to-Many-Many-to-One-Many-to-Many---VmlldzoyMDIzOTM#what-are-many-to-one-sequence-problems?
 
