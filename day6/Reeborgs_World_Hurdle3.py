################################################################
# Attention: This code was written for REEBORG'S WORLD... 
# ...Hurdle 3 challenge.
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

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        turn_step()        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
