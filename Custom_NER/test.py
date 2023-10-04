import spacy

nlp_ner = spacy.load("model-best") 

doc=nlp_ner(" Elon Musk will buy iphone 13 on December 20 at 6:30 PM")
for ent in doc.ents:
    print(ent.text, ent.label_)
