# adding even numbers from 0 to 100

total = 0
for number in range(2, 101, 2):
    total += number
print(total)


total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)
