graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

visited = []
queue = [] #borda
goal = 'F' #estado final

def breadth(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0) #first in first out (retira o primeiro elemento e retorna ele)
        print(s, end=' ')
        if s == goal:
            break
        for neighboor in graph[s]: #expansão do nó s
            if neighboor not in visited:
                visited.append(neighboor)
                queue.append(neighboor)
                if goal in visited:
                    break

breadth(visited, graph, 'A')