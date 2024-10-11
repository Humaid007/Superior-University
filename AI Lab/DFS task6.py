class Node:
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.neighbors = []

def dfs(start_node):
    stack = [start_node] 
    
    while stack:
        node = stack.pop() 
        
        if not node.visited:
            node.visited = True
            print(node.data, end=" ")  

            for neighbor in node.neighbors:
                if not neighbor.visited:
                    stack.append(neighbor) 

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node1.neighbors = [node2, node3]
node2.neighbors = [node4, node5]
node3.neighbors = [node5]
node4.neighbors = [node1] 

dfs(node1)  


