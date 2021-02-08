# Exercise 7

def get_age(year, month, day):
    current_year = 2020
    current_month = 7
    current_day = 8
    age = current_year - year
    if current_month > month:
        current_month -= 1
    elif current_month == month:
        if current_day > day:
            age -= 1
    return age


get_age(1997, 2, 28)


sex = input("what is your gender?")


def can_retire(gender, age):
    retire = False
    if gender == "p" and age > 67:
        retire = True
    elif gender == "v" and age > 62:
        retire = True
    return retire


print(can_retire(sex, get_age(1930, 2, 28)))
