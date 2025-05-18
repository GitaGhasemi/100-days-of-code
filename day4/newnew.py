import sys

nums = input().strip()
if nums:
    nums = list(map(int, nums.split()))
else:
    nums = []

operation = input().strip()
value = None

if operation in ["add", "remove"]:
    try:
        value = int(input().strip())
    except:
        print("Error")
        sys.exit()

if operation == "add":
    nums.append(value)
    print(" ".join(map(str, nums)))

elif operation == "remove":
    if value in nums:
        nums.remove(value)
        print(" ".join(map(str, nums)) if nums else "")  # Empty list should print nothing
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
