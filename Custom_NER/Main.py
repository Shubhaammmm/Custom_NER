import spacy
from spacy.tokens import DocBin
from tqdm import tqdm
import warnings
warnings.filterwarnings("ignore")

nlp = spacy.blank("en") 
db = DocBin() 


import json
"""
f = open('training_input.json')
TRAIN_DATA = json.load(f)

#to convert json file to .spacy file
for text, annot in tqdm(TRAIN_DATA['annotations']): 
    doc = nlp.make_doc(text) 
    ents = []
    for start, end, label in annot["entities"]:
        span = doc.char_span(start, end, label=label, alignment_mode="contract")
        if span is None:
            print("Skipping entity")
        else:
            ents.append(span)
    doc.ents = ents 
    db.add(doc)

db.to_disk("./traindata.spacy")# save .spacy file 
"""
