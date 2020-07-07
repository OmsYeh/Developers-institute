# Exercise 1

my_fav_numbers = set([7,9,23,46,82])
friend_fav_numbers = set([6,7,8,9,0])
print(friend_fav_numbers)

print(my_fav_numbers)
my_fav_numbers.add(54)
print(my_fav_numbers)
my_fav_numbers.add(72)
print(my_fav_numbers)
my_fav_numbers.remove(72)
print(my_fav_numbers)

our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)
