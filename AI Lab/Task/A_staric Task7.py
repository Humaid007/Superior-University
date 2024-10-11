class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  
        self.h = 0 
        self.f = 0  

    def __eq__(self, other):
        return self.position == other.position

def astar(start, goal, grid):
    open_set = [Node(start)]
    closed_set = []

    while open_set:
        current_node = min(open_set, key=lambda node: node.f)

        if current_node == Node(goal):
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return reversed path

        open_set.remove(current_node)
        closed_set.append(current_node)

        for neighbor_pos in get_neighbors(current_node.position, grid):
            neighbor = Node(neighbor_pos, current_node)
            if neighbor in closed_set:
                continue

            neighbor.g = current_node.g + 1
            neighbor.h = heuristic(neighbor.position, goal)
            neighbor.f = neighbor.g + neighbor.h

            if neighbor not in open_set or neighbor.g < open_set[open_set.index(neighbor)].g:
                if neighbor not in open_set:
                  open_set.append(neighbor)
                else:
                  open_set[open_set.index(neighbor)] = neighbor
    return None  

def get_neighbors(position, grid):
    x, y = position
    neighbors = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != 1:
            neighbors.append((nx, ny))
    return neighbors

def heuristic(pos1, pos2):
    # Manhattan distance
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

grid = [[0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0]]

start = (0, 0)
goal = (4, 4)

path = astar(start, goal, grid)
if path:
    print("Path found:", path)
else:
    print("No path found.")