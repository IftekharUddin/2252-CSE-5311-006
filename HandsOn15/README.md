**Shortest Path Algorithms: Detailed Explanation and Code Walkthrough**

---

# 1. Dijkstra's Algorithm

- using a min heap we're keeping track as we go along 


## The Code
```python
heap = [(0, start)]
```
- The heap stores (current distance, node).

```python
distances = {node: float('inf') for node in graph}
distances[start] = 0
```
- Initialize all distances to infinity except the start node.

```python
current_distance, current_node = heapq.heappop(heap)
```
- Always process the node with the smallest known distance.

```python
for neighbor, weight in graph[current_node]:
```
- Relax each neighbor: check if the path through the current node is better.

```python
if distance < distances[neighbor]:
    distances[neighbor] = distance
    heapq.heappush(heap, (distance, neighbor))
```
- If a better path is found, update and push to the heap.

---

# 2. Bellman-Ford Algorithm

## Purpose
Find the shortest paths from a single source node to all other nodes even if **negative edge weights** exist. Can also detect **negative weight cycles**.

## How It Works
- Initialize distances.
- For (V-1) times, where V = number of vertices:
  - Go through each edge and relax it.
- After V-1 iterations, if any edge can still be relaxed, a negative cycle exists.

## Our Code Walkthrough
```python
distances = {v: float('inf') for v in vertices}
distances[start] = 0
```
- Initialize distances.

```python
for _ in range(len(vertices) - 1):
    for u, v, weight in graph:
```
- Repeat V-1 times. Each iteration relaxes all edges.

```python
if distances[u] + weight < distances[v]:
    distances[v] = distances[u] + weight
```
- If the new path is shorter, update the distance.

```python
for u, v, weight in graph:
    if distances[u] + weight < distances[v]:
        raise Exception("Graph contains a negative-weight cycle")
```
- Final check for negative-weight cycles.

---

# 3. Floyd-Warshall Algorithm

## Purpose
Find the shortest paths **between every pair of nodes**.

## How It Works
- Create a distance matrix where `dist[i][j]` holds the current shortest known distance from i to j.
- Initially, set direct edge weights and 0 for self-loops, infinity otherwise.
- For each node k (acting as an intermediate node):
  - For each pair (i, j), update `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])`

## Our Code Walkthrough
```python
dist = {v: {u: float('inf') for u in vertices} for v in vertices}
```
- Initialize all distances to infinity.

```python
for v in vertices:
    dist[v][v] = 0
```
- Set distance to self as 0.

```python
for u, v, weight in graph:
    dist[u][v] = weight
```
- Populate direct edges.

```python
for k in vertices:
    for i in vertices:
        for j in vertices:
```
- For every intermediate node k, try to improve paths.

```python
if dist[i][j] > dist[i][k] + dist[k][j]:
    dist[i][j] = dist[i][k] + dist[k][j]
```
- Update the shortest distance if going through k is better.

---

# Summary
| Algorithm | Best for | Handles Negative Weights | Handles All-Pairs |
|:---------:|:--------:|:------------------------:|:-----------------:|
| Dijkstra  | Single source, non-negative edges | No | No |
| Bellman-Ford | Single source, negative edges allowed | Yes | No |
| Floyd-Warshall | All pairs shortest paths | Yes | Yes |

Each algorithm serves a different use case depending on the graph's properties!

