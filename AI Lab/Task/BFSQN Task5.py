def breadth_first_search(graph, start):
    visited = set()
    queue = [start]

    while queue:
        current = queue.pop(0)  

        if current not in visited:
            visited.add(current)
            print(current)

            for neighbor in graph[current]:
                if neighbor not in visited:
                    queue.append(neighbor)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
breadth_first_search(graph, start_node)