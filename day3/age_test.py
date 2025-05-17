print("Welcome to the rollercoaster!")
height = int(input("Enter your height in cm:\n"))
bill = 0

if height >= 120:
    print("You can buy a ticket!")
    age = int(input("Enter your age:\n"))
    
    if age < 12:
        bill = 5
        print(f"Child tickets are {bill}$.")
    elif age >= 12 and age <= 18:
        bill = 7
        print(f"Youth tickets are {bill}$.")
    else:
        bill = 12
        print(f"Adult tickets are {bill}$.") 

    # anyone can have a photo taken of them.
    wants_photo = input("Do you also want a photo? Y or N.")  
    if wants_photo == "Y":
        bill += 3
    
    print(f"You have to pay {bill}$")

else:
    print("Sorry! You have to grow taller before you can ride.")

