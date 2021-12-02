import csv

FILENAME = "employees.csv"
EMPLOYEES = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]

with open(FILENAME, 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "job"], delimiter=';')
    writer.writeheader()
    writer.writerows(EMPLOYEES)