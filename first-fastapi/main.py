from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bismillah!"}

@app.get("/about")
def about():
    return {"message": "This is my first FastAPI application."}

@app.get("/block")
def block():
    return {"message": "This is a block endpoint."}

@app.get("/owner")
def owner():
    return {"message": "This application is made by Mushfikur Rahman."}