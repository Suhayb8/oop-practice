from fastapi import FastAPI
from bank import BankAccount

app = FastAPI()

account = BankAccount(2000) # Starting with 2000 balance

@app.get("/")
def home():
    return {"message": "🏦 Welcome to the Bank API!"}


@app.get("/deposit/{amount}")
def deposit(amount: float):
    return {"message": account.deposit(amount)}

@app.get("/withdraw/{amount}")
def withdraw(amount: float):
    return {"message": account.withdraw(amount)}

@app.get("/show_balance")
def show_balance():
    return {"message": account.show_balance()}


