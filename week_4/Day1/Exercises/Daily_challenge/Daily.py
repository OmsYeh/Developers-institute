import random #alternativley can do //from random import shuffle//

num = input("enter a sentence or word thats 10 characters long")

if len(num) !=10:
    num = input("sorry thats not 10 characters long")
else:
    print(f'Your first character is {num[0]}')
    print(f'Your last character is {num[-1]}')
for i in range(len(num)+1):
    print(num[:i])

shuffled = list(num)
random.shuffle(shuffled)
shuffled = ''.join(shuffled)
print(shuffled)
