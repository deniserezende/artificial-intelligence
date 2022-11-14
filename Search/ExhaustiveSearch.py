import logging
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def breadth_first_search(graph, root, goal, visited=None):
    logging.info(msg=f'breadth_first_search ')
    # FIFO - First in first out
    # https://www.programiz.com/dsa/graph-bfs
    if visited is None:
        visited = []
    visited.append(root)
    queue = [root]

    while queue:
        vertex = queue.pop(0)  # FIFO
        logging.info(msg=f'{vertex} ')
        if vertex == goal:
            break
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                if goal in visited:
                    break
    return visited


def depth_first_search(graph, root, goal, visited=None):
    logging.info(msg=f'depth_first_search ')
    # https://www.programiz.com/dsa/graph-dfs
    if visited is None:
        visited = []
    visited.append(root)
    stack = [root]

    while stack:
        vertex = stack.pop(0)
        visited.append(vertex)
        logging.info(msg=f'{vertex} ')
        if vertex == goal:
            break
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                stack.insert(0, neighbour)
    return visited


graph_example_1 = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

graph_example_2 = {
    '0': ['1', '2'],
    '1': ['0', '3', '4'],
    '2': ['0'],
    '3': ['1'],
    '4': ['2', '3'],
}

graph_example_3 = {
    '0': ['1', '2', '3'],
    '1': ['2'],
    '2': ['4'],
    '3': ['5'],
    '4': [],
    '5': []
}
