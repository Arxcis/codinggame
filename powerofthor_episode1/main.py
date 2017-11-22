import sys
import math

class Vector2:
    def __init__(self, x, y):
        self.x, self.y = x,y

    def __sub__(self, other): 
        return Vector2(self.x-other.x,self.y-other.y)

    def __add__(self, other): 
        return Vector2(self.x+other.x,self.y+other.y)

    def angle(self):          
        return int((math.atan2(self.y, self.x) / (2*math.pi))*360)

direction = {
    180: {'string': 'W',  'vector': Vector2( -1, 0)},
    135: {'string': 'SW', 'vector': Vector2( -1, 1)},
     90:  {'string': 'S',  'vector': Vector2( 0, 1)},
     45:  {'string': 'SE', 'vector': Vector2( 1, 1)},
      0:  {'string': 'E',  'vector': Vector2( 1, 0)},
    -45:  {'string': 'NE', 'vector': Vector2( 1,-1)},
    -90:  {'string': 'N',  'vector': Vector2( 0,-1)},
    -135:  {'string': 'NW', 'vector': Vector2(-1,-1)},
    -180:  {'string': 'W',  'vector': Vector2(-1, 0)}
}
    
def closest_8way_angle(vector):
    angle = vector.angle() 
    modulo = angle % 45

    if modulo < 27.5:
        return angle - modulo
    return angle + (45 - modulo)


# init
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
light_vector = Vector2(light_x, light_y)
thor_vector = Vector2(initial_tx, initial_ty)

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.    
    
    # Find optimal angle
    direction_vector = light_vector - thor_vector
    angle = closest_8way_angle(direction_vector)

    # Move Thor
    thor_vector = thor_vector + direction[angle]['vector']
    print(direction[angle]['string'])

