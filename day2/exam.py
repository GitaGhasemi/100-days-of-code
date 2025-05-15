try:
    # Input reading
    N = int(input())
    X = float(input())
    P = float(input())

    # Input validation
    if N <= 0:
        raise ValueError("The number of people must be greater than zero.")
    if X < 0:
        raise ValueError("The total bill amount cannot be negative.")
    if P < 0:
        raise ValueError("The tip percentage cannot be negative.")

    # Calculate the total amount including the tip
    total = (P / 100 * X) + X
    # Calculate the amount each person should pay
    each_person = total / N
    # Print the result rounded to two decimal places
    print(f"Each person should pay: ${each_person:.2f}")

except ValueError as e:
    print(f"Invalid input: {e}")
except ZeroDivisionError:
    print("The number of people must be greater than zero to split the bill.")
