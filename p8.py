from collections import deque


vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
edge = ['A-B', 'A-C', 'B-D', 'C-D', 'C-E', 'D-F', 'E-H', 'E-G', 'G-H']


adjList = {v: [] for v in vertex}
for e in edge:
    v1, v2 = e.split('-')
    adjList[v1].append(v2)
    adjList[v2].append(v1)


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in sorted(graph[start]):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        current = queue.popleft()
        print(current, end=' ')
        for neighbor in sorted(graph[current]):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


def find_connected_components(graph):
    visited = set()
    components = []

    for vertex in graph:
        if vertex not in visited:
            component = []
            queue = deque([vertex])
            visited.add(vertex)

            while queue:
                current = queue.popleft()
                component.append(current)
                for neighbor in sorted(graph[current]):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            components.append(component)

    return components


def spanning_tree(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbor in sorted(graph[start]):
        if neighbor not in visited:
            print(f"({start}, {neighbor})", end=' ')
            spanning_tree(graph, neighbor, visited)

#테스트 프로그램
if __name__ == "__main__":
    print("DFS: ", end="")
    dfs(adjList, 'A')
    print()

    print("BFS: ", end="")
    bfs(adjList, 'A')
    print()

    components = find_connected_components(adjList)
    print(f"Connected Components: {components}")

    print("Spanning Tree: ", end="")
    spanning_tree(adjList, 'A')
    print()
