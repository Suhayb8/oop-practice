from fastapi import FastAPI
from PaymentSystem  import CreditCardPayment, PayPalPayment

app = FastAPI()

@app.get("/")
def home_payment():
    return {"message": "Welcome to the Payment API!"}

@app.get("/credit/{amount}")
def credit_method(amount: float):
    credit = CreditCardPayment()
    message = credit.process_payment(amount)
    return {"status": message}

@app.get("/paypal/{amount}")
def paypal_method(amount: float):
    paypal = PayPalPayment()
    message = paypal.process_payment(amount)
    return {"status": message}

