import numpy as np
from environment import Environment
from astar import astar

if __name__ == '__main__':
    
    path = None
    while path is None:
        # Generate random map
        size = 50
        # Generate walls
        map = np.ones((size, size))
        for i in range(40):
            map[i][10] = 0
            map[i][30] = 0

        for i in range(10, 50):
            map[i][20] = 0
            map[i][40] = 0
        # Start and End points
        map[0][0] = map[-1][-1] = 1
        # Create environment
        environment = Environment(map)
        # Find path
        path = astar(map, [0, 0], [size - 1, size - 1], environment)

    while True:
        environment.show([], [], path)
