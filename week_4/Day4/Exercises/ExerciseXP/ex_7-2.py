# Exercise 7.2

def four_x(x):
    str_x = str(x)
    double_x = str_x * 2
    triple_x = str_x * 3
    quad_x = double_x * 2
    total = x + int(double_x) + int(triple_x) + int(quad_x)
    return total
