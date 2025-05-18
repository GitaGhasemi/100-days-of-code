student_heights = input("Input a list of heights ").split()

for n in range (0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)    

# we have a function called sum() for doing it
sum = 0
count = 0
for height in student_heights:
    sum += height
    count +=1

average = sum / count
print(average)
print(round(average))

