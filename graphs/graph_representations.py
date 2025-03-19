"""function to convert a graph in the two representaions:
1. Adjacency List
2. Adjacency Matrix
"""

from typing import List, Tuple


def to_adjacency_matrix(nodes: int, edges: List[Tuple[int, int]]) -> List[List[int]]:
    # considering the graph is unweighted
    graph = [[0] * nodes for _ in range(nodes)]
    for i, j in graph:
        graph[i][j] = 1
    return graph


def to_adjacency_list(nodes: int, edges: List[Tuple[int, int]]) -> List[List[int]]:
    # considering the graph is unweighted
    graph = [[] for _ in range(nodes)]

    for node1, node2 in edges:
        graph[node1].append(node2)

    return graph
