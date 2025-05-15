# Input reading
num_people = int(input())
total_bill = float(input())
per_tip = float(input())

# Input validation
if num_people > 0 and total_bill >= 0 and per_tip >= 0:
    # Calculate the total amount including the tip
    total = (per_tip / 100 * total_bill) + total_bill
    # Calculate the amount each person should pay
    each_person = total / num_people
    # Print the result rounded to two decimal places
    #answer = "{:.2f}".format(each_person)
    print(f"Each person should pay: ${each_person:.2f}")
