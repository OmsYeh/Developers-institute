# Exercise 4
# 1. a float has a decimal place and a integer is a whole number

# 2. by using a function that i can create

# 3.  
import decimal

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

print(list(float_range(1, 20.5, '0.5')))