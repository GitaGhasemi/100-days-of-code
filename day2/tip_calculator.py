print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
per_tip = int(input("What percentage tip would you like to gove? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

total = (per_tip / 100 * total_bill) + total_bill
each_person = round((total / num_people), 2)
#answer = "{:.2f}".format(each_person)

print(f"Each person should pay {each_person}")
