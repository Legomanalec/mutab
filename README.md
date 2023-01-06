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