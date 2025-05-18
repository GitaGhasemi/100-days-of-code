row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# -1 to get the index
# in this line we find the proper row from map
which_element_of_map = (int(position) % 10) - 1

# -1 to get the index
# in this line we find the proper element from the proper row
which_element_of_rows = (int(position) // 10) - 1

map[which_element_of_map][which_element_of_rows] = "X"

print(f"{row1}\n{row2}\n{row3}")
