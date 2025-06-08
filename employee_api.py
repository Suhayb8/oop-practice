from fastapi import FastAPI
from employee import FullTimeEmployee, PartTimeEmployee

app = FastAPI()

@app.get("/")
def employee_home():
    return {"message": "🙌Welcome to my employee system"}

@app.get("/full_time_employee/{name}/{id}/{monthly_salary}")
def full_time_employee(name: str, id: int, monthly_salary: float):
    full_time = FullTimeEmployee(name, id, monthly_salary)
    return {
        "employee": name,
        "id": id,
        "salary": full_time.calculate_salary()
    }

@app.get("/part_time_employee/{name}/{id}/{hourly_rate}/{hours_worked}")
def part_time_employee(name: str, id: int, hourly_rate: float, hours_worked:int):
    part_time = PartTimeEmployee(name, id, hourly_rate, hours_worked)
    return {
        "employee": name,
        "id": id,
        "salary": part_time.calculate_salary()
    }

