from typing import Any, Set, List, Dict


def dfs(graph: List[List[int]], current_node: int, visited: Set = None):

    if not graph:
        return

    if visited is None:
        visited = set()

    print(current_node, end="->")
    visited.add(current_node)
    for node in graph[current_node]:
        if node not in visited:
            dfs(graph=graph, current_node=node, visited=visited)


def dfs_with_non_connected_component(graph: List[List[int]], vertices: int):

    visited = set()

    for v in range(vertices):
        if v in visited:
            continue
        print("")
        dfs(graph=graph, current_node=v, visited=visited)


def check_bipartite_graph(graph: List[List[int]], nodes: int):
    colors = [-1] * nodes

    def dfs(current_node: int, color: int):
        colors[current_node] = color
        for node in graph[current_node]:
            if colors[node] == -1:
                if not dfs(current_node=node, color=1 - colors[current_node]):
                    return False
            else:
                if colors[node] == colors[current_node]:
                    return False
        return True

    for start in range(nodes):
        if colors[start] == -1:
            if not dfs(current_node=start, color=0):
                return False
    return True


def dfs_iterative(graph: List[List[int]]):
    stack = []
    visited = set()

    stack.append(0)

    while stack:
        current_node = stack.pop()
        visited.add(current_node)
        for node in graph[current_node]:
            if node not in visited:
                stack.append(node)


def topological_sort(dep_graph: List[List[int]], target: int, nodes: int):
    visiting = [False] * nodes
    visited = set()
    dep_order = []
    is_cyclic = False

    def dfs(node: int):
        nonlocal is_cyclic
        if visiting[node] == True:
            is_cyclic = True
            return

        visiting[node] = True
        for dep in dep_graph[node]:
            if dep not in visited:
                dfs(dep)

        visiting[node] = False
        dep_order.append(node)

    dfs(node=target)
    if is_cyclic:
        return []
    else:
        return dep_order[::-1]


def main():
    graph_with_cycle = {
        0: [1],
        1: [2],
        2: [0],  # This edge creates a cycle (0 -> 1 -> 2 -> 0)
        3: [],
    }
    graph_without_cycle = {0: [1], 1: [2], 2: [], 3: []}
    print(topological_sort(dep_graph=graph_without_cycle, target=0, nodes=4))
    print(topological_sort(dep_graph=graph_with_cycle, target=0, nodes=4))


if __name__ == "__main__":
    main()
