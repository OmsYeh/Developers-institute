# make a function that returns all even numbers from a list

l = [1, 2, 3, 4]


def is_even(num):
    return num % 2 == 0


def even_num(l):
    evens = [num for num in l if is_even(num)]
    return evens


print(even_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

