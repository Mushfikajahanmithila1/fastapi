from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoanRequest(BaseModel):
    age: int
    income: float
    loan_amount: float
    working_years: int

@app.post("/predict")
def predict(loan_request: LoanRequest):
    if loan_request.working_years < 18 or loan_request.income < 20000:
        decision = "Loan approved"
    else:
        decision = "Loan rejected"
    return {"age": loan_request.age, "decision": decision}