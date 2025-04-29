def floyd_warshall(vertices, graph):
    dist = {v: {u: float('inf') for u in vertices} for v in vertices}

    for v in vertices:
        dist[v][v] = 0

    for u, v, weight in graph:
        dist[u][v] = weight

    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# test
edges = [
    ('A', 'B', 1),
    ('B', 'C', 2),
    ('A', 'C', 4),
    ('C', 'D', 1),
    ('B', 'D', 5)
]
vertices = ['A', 'B', 'C', 'D']

result = floyd_warshall(vertices, edges)
for from_node in vertices:
    for to_node in vertices:
        print(f"Shortest path from {from_node} to {to_node} is {result[from_node][to_node]}")
