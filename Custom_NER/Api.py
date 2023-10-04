from fastapi import FastAPI
from pydantic import BaseModel
import spacy
app=FastAPI()
nlp_ner= spacy.load("model-best")

class TextInput(BaseModel):
    text:str


@app.post("/ner")
async def perform_ner(text_input:TextInput):
    doc=nlp_ner(text_input.text)
    entities =[{"text":ent.text,"labels":ent.label_} for ent in doc.ents]
    return {"entities":entities}    