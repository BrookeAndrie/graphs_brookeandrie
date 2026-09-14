"""Graph traversal algorithms."""

from collections import deque


def breadth_first_search(graph, source):
    """Return vertices in breadth-first order starting at ``source``."""
    vertices = set(graph)
    for neighbors in graph.values():
        vertices.update(neighbors)

    if source not in vertices:
        raise ValueError("source vertex is not present in the graph")

    visited = {source}
    queue = deque([source])
    order = []

    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        for neighbor in graph.get(vertex, {}):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order
