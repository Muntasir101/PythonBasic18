employees = [
    {"name": "Smith", "salary": 5000},
    {"name": "kevin", "salary": 10000},
    {"name": "Green", "salary": 50000},
    {"name": "David", "salary": 20000},
]
total_salary = 0

for employee in employees:
    #total_salary += employee['salary']
    total_salary = total_salary + employee['salary']

print("Total salary: $" + str(total_salary))
