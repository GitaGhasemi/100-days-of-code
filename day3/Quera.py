logical_gate = input().strip().upper()

if logical_gate not in {"AND", "OR", "NOT", "XOR", "NAND"}:
    print("Error: Invalid logical gate. Choose from AND, OR, NOT, XOR, or NAND.")

elif logical_gate == "AND":
    op1 = input().strip().capitalize()
    op2 = input().strip().capitalize()

    if op1 not in {"True", "False"}:
        print("Error: Invalid boolean input.")
    op1 = op1 == "True"    

    if op2 not in {"True", "False"}:
        print("Error: Invalid boolean input.")
    op2 = op2 == "True"    
    
    if op1 == "True" and op2 == "True":
        print(True)
    else:
        print(False)

elif logical_gate == "OR":
    op1 = input().strip().capitalize()
    op2 = input().strip().capitalize()

    if op1 not in {"True", "False"}:
        print("Error: Invalid boolean input.")
    op1 = op1 == "True"    

    if op2 not in {"True", "False"}:
        print("Error: Invalid boolean input.")
    op2 = op2 == "True"    

    if op1== "True" or op2 == "True":
        print(True)
    else:
        print(False)

elif logical_gate == "XOR":
    op1 = input().strip().capitalize()
    op2 = input().strip().capitalize()

    if op1 not in {"True", "False"}:
        print("Error: Invalid boolean input.")
    op1 = op1 == "True"    

    if op2 not in {"True", "False"}:
        print("Error: Invalid boolean input.")
    op2 = op2 == "True"    
  
    if (op1 == "True" and op2 == "True"):
        print(False)
    elif (op1 == "False" and op2 == "False"):
        print(False)        
    else:
        print(True)
      
elif logical_gate == "NAND":
    op1 = input().strip().capitalize()
    op2 = input().strip().capitalize() 

    if op1 not in {"True", "False"}:
        print("Error: Invalid boolean input.")
    op1 = op1 == "True"    

    if op2 not in {"True", "False"}:
        print("Error: Invalid boolean input.")
    op2 = op2 == "True"    

    answer = not (op1 and op2)
    print(answer)

elif logical_gate == "NOT":
    op1 = input().strip().capitalize()
    
    if op1 not in {"True", "False"}:
        print("Error: Invalid boolean input.")
    op1 = op1 == "True"    
        
    answer = not op1
    print(answer)

