# Exercise 3
# Recap – What is a float? What is the difference between an integer and a float?
# Earlier, we tried to create a sequence of floats. Did it work?
# Can you think of another way of generating a sequence of floats?
# Create a list containing the sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 without hard-coding the sequence.

# 1//
# a float is essentially a number with decimals while an integer is a whole number

# 2//
# yes it works, you can have floats in sequences because floats are just a differnt types of data
# 3 and 4
l=[]
for i in range(0,20):
    i+= 0.5
    l.append(i)
print(l)
