# graphs_brookeandrie

`graphs_brookeandrie` is a Python library for working with graphs. It includes
Dijkstra's algorithm for finding the shortest paths from one source vertex to
all reachable vertices in a weighted graph. As an additional graph algorithm,
the package also includes breadth-first search (BFS).

GitHub repository: https://github.com/brookeandrie/graphs_brookeandrie

## Requirements

- Python 3.9 or newer
- `pip`

The library has no third-party runtime dependencies.

## Installation

Clone this repository, open a terminal in its root directory, and install it:

```powershell
py -m pip install .
```

For editable installation during development, use:

```powershell
py -m pip install -e .
```

## Dijkstra's shortest-path algorithm

A graph connects vertices with edges. In a weighted graph, every edge has a
cost called its weight. Dijkstra's algorithm finds the lowest total weight
needed to travel from a selected source vertex to every reachable vertex.

The graph is represented as a nested dictionary. Each outer key is a vertex,
and its value maps neighboring vertices to nonnegative edge weights:

```python
graph = {
    0: {1: 4, 2: 1},
    1: {3: 1},
    2: {1: 2, 3: 5},
    3: {},
}
```

Use the algorithm like this:

```python
from graphs_brookeandrie import sp

distances, paths = sp.dijkstra(graph, 0)

print(distances)
print(paths)
```

`distances` contains the minimum cost from the source to each vertex. `paths`
contains the vertices visited before each reachable destination. Unreachable
vertices have a distance of `sys.maxsize` and do not appear in `paths`.
Dijkstra's algorithm requires nonnegative edge weights.

## Running the included example

After installation, pass one of the graph data files to the test program:

```powershell
py test.py data/example1.txt
```

Each line of an input file contains a source vertex, destination vertex, and
edge weight separated by spaces.

## Breadth-first search

The bonus BFS implementation visits vertices one level at a time:

```python
from graphs_brookeandrie import traversal

order = traversal.breadth_first_search(graph, 0)
print(order)
```

## Project structure

```text
src/
└── graphs_brookeandrie/
    ├── __init__.py
    ├── heapq.py
    ├── sp.py
    └── traversal.py
data/
test.py
README.md
pyproject.toml
```

## Development

Development work should be committed to the `dev` branch. Completed changes
can then be merged into the protected `main` branch through a pull request.
