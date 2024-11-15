from random import choice

class RandomWalk():
    """class to generate random walk"""

    def __init__(self, num_points=5000):
        """initialize atributes of a walk"""
        self.num_points = num_points

        #walk start at (0,0)
        self.x_values = [0]
        self.y_values = [0]
    
    def fill_walk(self):
        """calculate all walk points"""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            #no point if not moving
            if x_step == 0 and y_step == 0:
                continue
            
            #new point
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            self.x_values.append(x)
            self.y_values.append(y)

    
    def get_step(self):
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = distance * direction
        return step
            