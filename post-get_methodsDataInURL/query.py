from fastapi import FastAPI
app = FastAPI()
all_customers = [
    {"customer_id": 1, "name": "John Doe", "risk": 'high', "city": "newyork"},
    {"customer_id": 2, "name": "Jane Smith", "risk": 'medium', "city": "losangeles"},
    {"customer_id": 3, "name": "Alice Johnson", "risk": 'low', "city": "chicago"},
    {"customer_id": 4, "name": "Bob Brown", "risk": 'high', "city": "newyork"},
]

@app.get('/customers')
def get_customers(risk: str = None, city: str = None):
    filtered = [
        c for c in all_customers
        if c['risk'] == risk and c['city'] == city
    ] 
    return{
        "city": city,
        "risk": risk,
        "count": len(filtered),
        'results': filtered
    }