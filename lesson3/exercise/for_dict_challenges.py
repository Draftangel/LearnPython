print("# Задание 1")
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
dict_students = {}
for student in students:
    dict_students[student["first_name"]] = dict_students.get(student["first_name"], 0) + 1

for student in dict_students:
    print(f"{student}: {dict_students[student]}")


print("# Задание 2")
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]


def get_popular_name(persons):
    dict_persons = {}
    popular_name = {}

    for person in persons:
        name = person["first_name"]
        dict_persons[name] = dict_persons.get(name, 0) + 1

        if popular_name.get("name", "") != name and popular_name.get("count", 0) < dict_persons[name]:
            popular_name["name"] = name
            popular_name["count"] = dict_persons[name]

    return popular_name["name"]


print(f"Самое частое имя среди учеников: {get_popular_name(students)}")


print("# Задание 3")
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for index, class_students in enumerate(school_students, 1):
    print(f"Самое частое имя в классе {index}: {get_popular_name(class_students)}")


print("# Задание 4")
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}


def get_gender_count(persons):
    counts = {
        "male": 0,
        "female": 0
    }

    for person in persons:
        counts["male" if is_male[person["first_name"]] else "female"] += 1

    return counts


for group in school:
    genders = get_gender_count(group["students"])
    print(f"Класс {group['class']}: девочки {genders['female']}, мальчики {genders['male']}")

print("# Задание 5")
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

most_male = {}
most_female = {}

for group in school:
    genders = get_gender_count(group["students"])

    if most_male.get("class", "") != group["class"] and most_male.get("count", 0) < genders["male"]:
        most_male["class"] = group["class"]
        most_male["count"] = genders["male"]

    if most_female.get("class", "") != group["class"] and most_female.get("count", 0) < genders["female"]:
        most_female["class"] = group["class"]
        most_female["count"] = genders["female"]

print(f"Больше всего мальчиков в классе {most_male['class']}")
print(f"Больше всего девочек в классе {most_female['class']}")
