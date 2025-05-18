nums = input().strip()
if nums:
    nums = list(map(int, nums.split()))
else:
    nums = []

operation = input().strip()
value = None

if operation in ["add", "remove"]:
    value = int(input())

if operation == "add":
    nums.append(value)
    print(" ".join(map(str, nums)))

elif operation == "remove":
    if value in nums:
        nums.remove(value)
        print(" ".join(map(str, nums)))
    else:
        print("Error")

elif operation == "max":
    print(max(nums))

elif operation == "min":
    print(min(nums))

elif operation == "average":
    print("%.1f" % (sum(nums) / len(nums)))  # Ensures one decimal place

else:
    print("Invalid operation")
