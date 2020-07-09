#Args

def my_sum(*args):
    print(args)
    return sum(args)


print(my_sum(1, 2, 4, 78, 99, 9))


#Kwargs


def myinfo(**kwargs):
    return kwargs


myKeys = myinfo(first_name="Yair", middle_name="George", last_name="Hochner")

print(myKeys)
