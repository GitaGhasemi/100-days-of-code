nums = list(map(int, input().split())) 
operation = input() 
value = None 

if operation in ["add", "remove"]:
    try:
        value = int(input())
    except:
        print("Error")
        exit()

if operation == "add":
    nums.append(value)
    print(" ".join(map(str, nums)))

elif operation == "remove":
    if value in nums:
        nums.remove(value)
        if nums:
            print(" ".join(map(str, nums)))
        else:
            print("")  # If the list is empty, print Error
    else:
        print("Error")
elif operation == "max":
    if nums:
        print(max(nums))
    else:
        print("Error")
elif operation == "min":
    if nums:
        print(min(nums))
    else:
        print("Error")
elif operation == "average":
    if nums:
        print("%.1f" % (sum(nums) / len(nums)))
    else:
        print("Error")
else:
    print("Invalid operation")
