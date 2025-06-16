################################################################
# Attention: This code was written for REEBORG'S WORLD... 
# ...Hurdle 4 challenge.
# And will NOT run without its library. -Git;)
################################################################

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()    
  
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
  
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
