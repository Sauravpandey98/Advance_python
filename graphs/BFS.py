from collections import deque
from typing import Dict, List, Any, Union, Tuple

# from graphs.graph_representations import to_adjacency_list


### traversal###
def bfs(graph: List[List[int]], vertices: int):
    # good even for non connected components
    """
    complexity: O(V+E)
    space: O(V)
    """
    if not graph:
        return

    q = deque()
    visited = set()

    for v in range(vertices):
        print("\n")
        if v in visited:
            continue
        q.append(v)
        while q:
            current_node = q.popleft()

            if current_node in visited:
                continue

            print(current_node, end="->")

            visited.add(current_node)
            for node in graph[current_node]:
                if node not in visited:
                    q.append(node)


def shortest_path(graph: List[List[int]], nodes: int, s: int, d: int) -> List[int]:
    """
    space complexity: O(V+E)
    time complexity: O(V^2)
    """
    if not graph or s < 0 or d < 0 or s >= nodes or d >= nodes:
        return []

    q = deque([(s, [s])])
    visited = set()

    while q:
        current_node, path = q.popleft()

        if current_node in visited:
            continue

        if current_node == d:
            return path

        visited.add(current_node)

        for node in graph[current_node]:
            if node not in visited:
                q.append((node, path + [node]))

    return []


def shortest_path2(graph: List[List[int]], nodes: int, s: int, d: int) -> List[int]:
    """
    space complexity: O(V+E)
    time complexity: O(V)
    """
    if not graph or s < 0 or d < 0 or s >= nodes or d >= nodes:
        return []

    q = deque([s])
    parent = {s: -1}
    visited = set()

    while q:
        current_node = q.popleft()

        if current_node in visited:
            continue

        visited.add(current_node)

        for node in graph[current_node]:
            if node not in visited:
                parent[node] = current_node
                q.append(node)

                if node == d:
                    path = []
                    node = d
                    while node != -1:
                        path.append(node)
                        node = parent[node]
                    return path[::-1]  # reversing the path
    return []


def shortest_path_length(graph: List[List[int]], nodes: int, s: int, d: int) -> int:
    # here lenght mean minimum number of edges you need to traverse to go from source to node
    # the lenght is basically the depth of graph where the required d is present
    if not graph or s < 0 or d < 0 or s >= nodes or d >= nodes:
        return []

    q = deque([(s, 0)])
    visited = set()

    while q:
        current_node, level = q.popleft()

        if current_node in visited:
            continue

        if current_node == d:
            return level

        visited.add(current_node)

        for node in graph[current_node]:
            if node not in visited:
                q.append((node, level + 1))
    return -1


def all_shortest_paths(
    graph: List[List[int]], nodes: int, s: int, d: int
) -> List[List[int]]:
    # NOTE: Still need answers of some question here:
    # 1. Why do we need to do level order traversal.Why do not normal traversal give that result.
    if not graph or s < 0 or d < 0 or s >= nodes or d >= nodes:
        return []

    q = deque([(s, [s])])
    visited = set()
    current_level_visited = set()
    found = False
    shortest_paths = []

    while q or not found:
        current_level_visited.clear()
        for _ in range(len(q)):
            current_node, path = q.popleft()

            if current_node == d:
                shortest_paths.append(path)
                found = True
                continue

            current_level_visited.add(current_node)
            for node in graph[current_node]:
                if node not in visited:
                    q.append((current_node, path + [node]))

        visited.update(current_level_visited)
    return shortest_paths


def topological_sort(graph: List[List[int]], nodes: int):
    index_tracker = [0] * nodes

    for i in range(nodes):
        nghbrs = graph[i]
        for nghbr in nghbrs:
            index_tracker[nghbr] += 1

    q = deque(i for i in range(nodes) if index_tracker[i] == 0)

    while q:
        current_node = q.popleft()

        print(current_node, end="->")

        for node in graph[current_node]:
            index_tracker[node] -= 1
            if index_tracker[node] == 0:
                q.append(node)


def main():
    nodes = 4
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]

    def to_adjacency_list(nodes: int, edges: List[Tuple[int, int]]) -> List[List[int]]:
        # considering the graph is unweighted
        graph = [[] for _ in range(nodes)]

        for node1, node2 in edges:
            graph[node1].append(node2)

        return graph

    graph = to_adjacency_list(nodes=nodes, edges=edges)
    topological_sort(graph=graph, nodes=nodes)


if __name__ == "__main__":
    main()
