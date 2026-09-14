"""Shortest-path algorithms for weighted directed graphs."""

import sys

from .heapq import heappop, heappush


def dijkstra(graph, source):
    """Return shortest distances and path prefixes from ``source``.

    ``graph`` must be a mapping in the form ``{vertex: {neighbor: weight}}``.
    Edge weights must be nonnegative. The returned ``path`` mapping follows
    the assignment format: each destination maps to the vertices visited
    before that destination.
    """
    vertices = set(graph)
    for neighbors in graph.values():
        vertices.update(neighbors)

    if source not in vertices:
        raise ValueError("source vertex is not present in the graph")

    dist = {node: sys.maxsize for node in vertices}
    dist[source] = 0
    path = {source: []}
    heap = [(0, source)]

    while heap:
        current_distance, u = heappop(heap)

        if current_distance != dist[u]:
            continue

        for v, weight in graph.get(u, {}).items():
            if weight < 0:
                raise ValueError("Dijkstra's algorithm requires nonnegative weights")

            candidate = current_distance + weight
            if candidate < dist[v]:
                dist[v] = candidate
                path[v] = path[u] + [u]
                heappush(heap, (candidate, v))

    return dist, path
