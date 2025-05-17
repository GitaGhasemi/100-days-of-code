gate = input().strip().upper()
    
if gate not in {"AND", "OR", "NOT", "XOR", "NAND"}:
    print("Error: Invalid logical gate. Choose from AND, OR, NOT, XOR, or NAND.")   
input1 = input().strip().capitalize()

if input1 not in {"True", "False"}:
    print("Error: Invalid boolean input.")
input1 = input1 == "True"
    
input2 = None
if gate != "NOT":
    input2 = input().strip().capitalize()
    if input2 not in {"True", "False"}:
        print("Error: Invalid boolean input.")
    input2 = input2 == "True"


if gate == "AND":
        result = input1 and input2
elif gate == "OR":
        result = input1 or input2
elif gate == "XOR":
        result = input1 != input2
elif gate == "NAND":
        result = not (input1 and input2)
elif gate == "NOT":
        result = not input1
    
print(result)
