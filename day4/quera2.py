nums = list(map(int, input().split()))  # Read list of integers
operation = input().strip()  # Read operation type

if operation == "count":
    value = int(input())  # Read extra input for "count"
    count = 0
    for num in nums:
        if num == value:
            count += 1
    result = count

elif operation == "reverse":
    nums.reverse()
    result = " ".join(map(str, nums))

elif operation == "even":
    even_numbers = []
    for num in nums:
        if num % 2 == 0:
            even_numbers.append(num)
    result = " ".join(map(str, even_numbers))

elif operation == "odd":
    odd_numbers = []
    for num in nums:
        if num % 2 != 0:
            odd_numbers.append(num)
    result =  " ".join(map(str, odd_numbers))

elif operation == "sum":
    total = 0
    for num in nums:
        total += num
    result = total


print(result)
