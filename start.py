from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello from FastAPI!"}

@app.get("/hello/{name}")
def hello_someone(name: str):
    return {"message": f"Hello, {name}!"}