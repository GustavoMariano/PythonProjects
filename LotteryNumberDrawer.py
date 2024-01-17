import random

numbers = []
count = 0

while count < 6:
    number = random.randint(1, 60)
    if number not in numbers:
        numbers.append(number)
        count += 1

print('Drawn numbers:', numbers)
numbers.sort()
print('Numbers in ascending order:', numbers)