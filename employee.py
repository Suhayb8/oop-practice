from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,name, id):
        self.name = name
        self.id = id
    @abstractmethod
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self, name, id, monthly_salary):
        super().__init__(name, id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, id, hourly_rate, hours_worked):
        super().__init__(name, id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        total = self.hourly_rate * self.hours_worked
        return total

employees = [
    FullTimeEmployee("Alice", 1,3000),
    PartTimeEmployee("wes", 6, 20, 80)
]

for employee in employees:
    print(f"ID {employee.id} -||- Employee: {employee.name} -||-  Salary: {employee.calculate_salary()} €.")

