from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.adjacent = []

def breadth_first_search(start_node):
    queue = deque([start_node])
    visited = set()

    while queue:
        current_node = queue.popleft()

        if current_node not in visited:
            visited.add(current_node)
            print(current_node.data)

            for neighbor in current_node.adjacent:
                if neighbor not in visited:
                    queue.append(neighbor)


node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")

node1.adjacent = [node2, node3]
node2.adjacent = [node1, node4]
node3.adjacent = [node1, node5]
node4.adjacent = [node2]
node5.adjacent = [node3]

breadth_first_search(node1)