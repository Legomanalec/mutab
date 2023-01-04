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