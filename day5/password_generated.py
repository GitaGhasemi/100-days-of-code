#  This programm generates random passwords in two different ways
#  from 3 lists of letters, numbers, and symbols
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '(', ')', '*', '+']

print("Welcome to password generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))

#Easy level
# In this level passwords are generated in a sequence. for example:
# fgH&*34

password = ""
for char in range(0, nr_letters):
    random_char = random.choice(letters)
    password += random_char

for sym in range(0,nr_symbols):
    random_sym = random.choice(symbols) 
    password += random_sym
      
for num in range(0, nr_numbers):
    random_num = random.choice(numbers)
    password += random_num
print(f"Your password is: {password}")


# Hard level
#  In this level there is no sequence.
# so we add them to a list to shuffel them
# Then we convert our list to a char string, using a for loop.
# f4H&g3&

password_list = []
for char in range(0, nr_letters):
    random_char = random.choice(letters)
    password_list += random_char

for sym in range(0,nr_symbols):
    random_sym = random.choice(symbols) 
    password_list += random_sym   

for num in range(0, nr_numbers):
    random_num = random.choice(numbers)
    password_list += random_num
# print(password_list)

# We shouldnt assign it to a var!
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")
