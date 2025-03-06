from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel
from typing import List, Annotated
import models
from db import engine,SessionLocal
from sqlalchemy.orm import Session
from src.model_architechture import NeuralNet
from src.preprocessing import tokenize, bag_of_words
import torch
import random
import json

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class QueriesText(BaseModel):
    text : str

#connection to database
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]

with open('src/train_datasets/train_data_M1.json', 'r') as json_data:
    intents = json.load(json_data)

# Load trained model
FILE = "deep_models/pava-m1.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Pava"

@app.post("/chat")
async def chat(queries:QueriesText,db:db_dependency):
    sentence = queries.text
    sentence = tokenize(sentence)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)
    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return {"bot": random.choice(intent['responses'])}
    else:
        return {"bot": "I do not understand..."}
        db_query = models.Queries(query_text=queries.text)
        db.add(db_query)
        db.commit()
        db.refresh(db_query)



