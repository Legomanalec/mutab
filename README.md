<h1>1 Overview</h1>
The goal of this project is to allow a mobile app user the ability to take a picture of an excerpt of musican notation and recieve the corresponding guitar tablature 

<h1>2 Background</h1>
<h2>2.1 Sheet Music</h2>

<h2>2.2 Optical Music Recognition</h2>

<h2>2.1 Guitar Tablature</h2>

<h1>3 Sheet Music to Guitar Tablature</h1>
<h2>3.1 Web Scraping</h2>


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
