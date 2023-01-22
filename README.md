<h1>1 Overview</h1>
The goal of this project is to allow a mobile app user the ability to take a picture of an excerpt of musican notation and recieve the corresponding guitar tablature 

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

<h2>4 Resources</h2>

LSTM RNN in Keras: Examples of One-to-Many, Many-to-One & Many-to-Many: https://wandb.ai/ayush-thakur/dl-question-bank/reports/LSTM-RNN-in-Keras-Examples-of-One-to-Many-Many-to-One-Many-to-Many---VmlldzoyMDIzOTM#what-are-many-to-one-sequence-problems?
 
<h1>X Brainstorming</h1>
My plan:
    1. Create a web scraper to grab thousands of guitar tablatures from Ultimate Guitar Tabs
    2. Convert each of these tablatures to midi 
    3. save these tablature/midi pairs for training
    4. feed the model midi data and have it return tablature

The reason this is not a trivial problem and warrants a solution using supervised learning is 
because mapping midi to tablature is not one-to-one, it is one-to-many. When it comes to midi,
each value is mapped to a single note, one-to-one. Guitar tablature maps many-to-one because
a single note can be represented in many different positions on a guitar neck. Therefore, mapping
midi to guitar tablature will be a one-to-many solution. 

The reason I feel a machine learning model is neccesary is because when a human converts 
midi to tablature the need a deep understanding of how a guitar fretboard is structured, and
they need advanced intuition on which mappings are most viable for a guitarist. So, feeding the
model thousands of many-to-one mappings will hopefully allow me to predict a viable one-to-many mapping



UPDATE: 1/6/2023
It would make more sense to convert the tab to an easier encoding for the computer to read (e.g. [(E, A, D2, G, B, e1), (E, A, D, G, B2, e3),...,(E0, A2, D2, G1, B0, e1)] ). 
Along with this new encoding there would be no need for the midi, even though it was fun to do. It would make more sense to instead convert the tab to a computer readable form as well 
(e.g. [(52, 65, 0, 0, 0, 0), (61, 66, 0, 0, 0, 0),...,(40, 47, 52, 56, 59, 65)]). The reason for arrays of 6 is because only 6 notes can be played at a time. A 0 would signify no note being played
and each value is a note(s) being played.

[(E, A, D2, G, B, e1), (E, A, D, G, B2, e3),...,(E0, A2, D2, G1, B0, e1)]
[(52, 65, 0, 0, 0, 0), (61, 66, 0, 0, 0, 0),...,(40, 47, 52, 56, 59, 65)]



UPDATE 1/6/2023
This is more of a timeseries problem. It would make sense to divide each note into an equally spaced time interval and predict based on the notes context. I am not familar with timeseries learning
so I will need to do some reading, but the idea appears pretty simple. I believe the ideal dataset would look like so:

|Time|Tab                     |Midi                    |
|----|------------------------|------------------------|
|0001|(E, A, D2, G, B, e1)    |(52, 65, 0, 0, 0, 0)    |
|0002|(E, A, D, G, B2, e3)    |(61, 66, 0, 0, 0, 0)    |
|... |...                     |...                     |
|0168|(E0, A2, D2, G1, B0, e1)|(40, 47, 52, 56, 59, 65)|

It might also make sense to make a dataset like:
|Time|TabE|TabA|TabD|TabG|TabB|Tabe|Midi0|Midi1|Midi2|Midi3|Midi4|Midi5|
|----|----|----|----|----|----|----|-----|-----|-----|-----|-----|-----|
|0001|-1  |-1  |2   |-1  |-1  |1   |52   |65   |0    |0    |0    |0    |
|0002|-1  |-1  |-1  |-1  |2   |3   |61   |66   |0    |0    |0    |0    |
|... |... |... |... |... |... |... |...  |...  |...  |...  |...  |...  |
|0168|0   |2   |2   |1   |0   |1   |40   |47   |52   |56   |59   |65   |

This would probably be easier to work with but would require multi-prediction as we would be predicting all 6 Tab columns at a time. 


Take the first row for example:
|Time|TabE|TabA|TabD|TabG|TabB|Tabe|Midi0|Midi1|Midi2|Midi3|Midi4|Midi5|
|----|----|----|----|----|----|----|-----|-----|-----|-----|-----|-----|
|0001|-1  |-1  |2   |-1  |-1  |1   |52   |65   |0    |0    |0    |0    |

I want to give the machine the inputs (52, 65, 0, 0, 0, 0) which correspond to an E3 and an F4 being played at the same time. The model will then think "Oh, when an E3 and F4 are being played at the same time, 
based on all the samples I have seen, it would make most sense to write the tab as D2/e1"

UPDATE: 1/7/2023
It wouldnt make much sense to structure the databse like mentioned previously because we have anywhere from 20 to 20000 samples per song so we would need a new database for each tab. Could look at encoding each measure
between tab and midi or 2 measure. 

UPDATE 1/21/2023
I was getting way too ahead of myself by trying to plan out the data format for training when I had no idea how I was going to train anything...

After doing more research, I believe this is an RNN problem, similar to predictive text. Instead of predicting the rest of a word based on its first character, I will be predicting the next tablature note based on the current one. There are only a max of 6 possible locations a note can be on the neck so there are at most 6 options to choose from next as the note needed will be known.
