################################################################
# Attention: This code was written for REEBORG'S WORLD... 
# ...Hurdle 4 challenge.
# And will NOT run without its library. -Git;)
################################################################

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_step():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

count = 0    
    
while not at_goal():
    if front_is_clear():
        if count > 0:
            move()
            turn_right()
            while count > 0:
                move()                
            
    else:
        while wall_in_front():
            turn_left()
            move()
            turn_right()
            count += 1


################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
