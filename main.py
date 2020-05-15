import numpy as np
from environment import Environment
from astar import astar

if __name__ == '__main__':
    path = None
    while path is None:
        # Generate random map
        size = 50
        map = np.random.randint(2, size=(size, size))
        map[0][0] = map[-1][-1] = 1
        # Create environment
        environment = Environment(map)
        # Find path
        path = astar(map, [0, 0], [size - 1, size - 1], environment)

    while True:
        environment.show([], [], path)
