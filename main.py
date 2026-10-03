from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Assalamu Alaikum. Welcome to the FastAPI application!"}

@app.get("/customer")
def customer(customer_id: int):
    return {"customer_id": customer_id, "message": f"Customer ID {customer_id} details retrieved successfully."}