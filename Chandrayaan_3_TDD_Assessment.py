"""
inputs :
starting position (x,y,z)
init direction anyone(N,S,E,W,U,P)
commands 

outputs :
final position and 
final direction
"""
def control_lunar_space_craft(start_pos : tuple, init_direc : str, commands_lst : list):
    Direction = {"N":{"f":"N", "b":"N", "l":"W", "r":"E", "u":"U", "d":"D"}, 
             "S":{"f":"S", "b":"S", "l":"E", "r":"W", "u":"U", "d":"D"}, 
             "W":{"f":"W", "b":"W", "l":"S", "r":"N", "u":"U", "d":"D"}, 
             "E":{"f":"E", "b":"E", "l":"N", "r":"S", "u":"U", "d":"D"}, 
             "U":{"f":"U", "b":"U", "l":"W", "r":"E", "u":"U", "d":"D"}, 
             "D":{"f":"D", "b":"D", "l":"E", "r":"W", "u":"U", "d":"D"}}

    Position = {"f":1, "b":1, "l":0, "r":0, "u":0, "d":0}

    final_pos = (1,1,1)
    final_dir = "S"
    return final_pos,final_dir
