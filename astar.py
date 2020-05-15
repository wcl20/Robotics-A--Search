import numpy as np

class Node:
    def __init__(self, position, parent):
        self.position = position
        self.parent = parent
        # F cost
        self.f = 0
        # G cost
        self.g = 0
        # H cost
        self.h = 0

    def __eq__(self, other):
        # Nodes are the same if they have same position
        return (self.position == other.position).all()

    def __lt__(self, other):
        # Return node with smaller F cost
        return self.f < other.f

    def __hash__(self):
        return hash(str(self.position))

def astar(map, start, end, environment):
    # Queue of nodes to be evaluated
    queue = []
    # Set of visited nodes
    visited = set()
    # Create start node
    start = Node(np.array(start), parent=None)
    # Create end node
    end = Node(np.array(end), parent=None)
    # Add start node to queue
    queue.append(start)
    # While queue is not empty
    while queue:
        environment.show(queue, visited)
        # Get node with smallest F cost
        queue.sort()
        current = queue.pop(0)
        # Add node to set of visited nodes
        visited.add(current)
        # If current node is end node ...
        if current == end:
            # Create path
            path = []
            while current is not None:
                path.append(current)
                current = current.parent
            return path[::-1]
        # Iterate each neighbour
        for step in [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]:
            # Create neighbour node
            neighbour = Node(current.position + np.array(step), parent=current)
            x, y = neighbour.position
            # Check neighbour is within range
            if x < 0 or x >= map.shape[1] or y < 0 or y >= map.shape[0]:
               continue
            # Check neighbour is traversable
            if map[y][x] == 0:
                continue
            # Check neighbour is not visited
            if neighbour in visited:
                continue
            # Compute G cost (Distance from start node)
            neighbour.g = current.g + 1
            # Compute H cost (Distance from end node)
            neighbour.h = (x - end.position[0]) ** 2 + (y - end.position[1]) ** 2
            # Compute F cost
            neighbour.f = neighbour.g + neighbour.h
            # If neighbour is already in queue
            if neighbour in queue:
                # Update neighbour with smaller G cost
                index = queue.index(neighbour)
                if queue[index].g > neighbour.g:
                    queue[index] = neighbour
            else:
                queue.append(neighbour)
    return None
