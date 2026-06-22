from fastapi import FastAPI
import pandas as pd

#pd.read_cvs()

app = FastAPI()
@app.get("/")
def read_root():
    return "hello"

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}