from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

@app.get("/analyze/") #TODO
def analyze():
    return {"TODO": "TODO"}

@app.get("/health")
def health_check(response: Response):
    return {"status": f"Ok"}