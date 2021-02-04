# Exercise 9

found_nums = []

for i in range(1500,2700):
	if (i%7 == 0) and (i%5 ==0):
		found_nums.append(i)

print(found_nums)