import spacy
from spacy import displacy
from pydantic import BaseModel
from fastapi import FastAPI

en_core_web_sm = spacy.load("en_core_web_sm")

app = FastAPI()

class Input(BaseModel):
    sentence: str

class Result(BaseModel):
    start_char: int
    end_char: int
    label_: str
    text: str

@app.post("/")
def result(input: Input):
    global html
    doc = en_core_web_sm(input.sentence)
    html = displacy.render(doc, style = "ent", minify=True)

    result = []
    for entity in doc.ents:
      comp = {}
      comp["start_char"] = entity.start_char
      comp["end_char"] = entity.end_char
      comp["label_"] = entity.label_
      comp["text"] = entity.text
      result.append(comp)

    return {"result": result, "html": html}

@app.get("/")
def hello():
    return {"Hello"}