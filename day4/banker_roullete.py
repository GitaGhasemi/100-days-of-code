# this program choose a person name randomly from a list
import random

names_string = input("Write everybody's names, seperated by a coma.")
names = names_string.split(", ")

size_of_list = len(names)

# important to note that indexing starts from 0 but len starts at 1
random_choice = random.randint(0,size_of_list - 1)
person_who_will_pay = names[random_choice]

# or simply using choice() function:
# person_who_will_pay = random.choice(names)

print(person_who_will_pay + " is going to buy the meal today!")
