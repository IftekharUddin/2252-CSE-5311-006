class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX == rootY:
            return False

        if self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        elif self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1

        return True

class RobotGrid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0] * cols for _ in range(rows)]
        self.dsu = DSU(rows * cols)
        self.cluster_count = 0
        self.active = set()

    def add_robot(self, r, c):
        if self.grid[r][c] == 1:
            return

        self.grid[r][c] = 1
        index = r * self.cols + c
        self.active.add(index)
        self.cluster_count += 1

        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols and self.grid[nr][nc] == 1:
                neighbor_index = nr * self.cols + nc
                if self.dsu.union(index, neighbor_index):
                    self.cluster_count -= 1

    def get_cluster_count(self):
        return self.cluster_count


import random
import time

def benchmark_dsu_grid(rows, cols, num_robots):
    grid = RobotGrid(rows, cols)
    positions = [(r, c) for r in range(rows) for c in range(cols)]
    random.shuffle(positions)
    positions = positions[:num_robots]

    times = []
    cluster_counts = []

    for r, c in positions:
        start = time.time()
        grid.add_robot(r, c)
        end = time.time()
        times.append(end - start)
        cluster_counts.append(grid.get_cluster_count())

    return times, cluster_counts

dsu_times, dsu_cluster_counts = benchmark_dsu_grid(100, 100, 1000)


from collections import deque

class RobotGridBFS:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[0] * cols for _ in range(rows)]
        self.visited = [[False] * cols for _ in range(rows)]

    def add_robot(self, r, c):
        self.grid[r][c] = 1

    def count_clusters(self):
        def bfs(start_r, start_c):
            queue = deque()
            queue.append((start_r, start_c))
            self.visited[start_r][start_c] = True
            while queue:
                r, c = queue.popleft()
                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.cols:
                        if self.grid[nr][nc] == 1 and not self.visited[nr][nc]:
                            self.visited[nr][nc] = True
                            queue.append((nr, nc))

        self.visited = [[False] * self.cols for _ in range(self.rows)]
        cluster_count = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == 1 and not self.visited[r][c]:
                    bfs(r, c)
                    cluster_count += 1
        return cluster_count


def benchmark_bfs(grid_size, num_robots):
    grid = RobotGridBFS(grid_size, grid_size)
    positions = [(r, c) for r in range(grid_size) for c in range(grid_size)]
    random.shuffle(positions)
    positions = positions[:num_robots]

    times = []
    cluster_counts = []

    for r, c in positions:
        grid.add_robot(r, c)
        start = time.time()
        cluster_count = grid.count_clusters()
        end = time.time()
        times.append(end - start)
        cluster_counts.append(cluster_count)

    return times, cluster_counts

bfs_times, bfs_cluster_counts = benchmark_bfs(100, 1000)



import matplotlib.pyplot as plt

steps = list(range(1, len(dsu_times) + 1))

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(steps, dsu_times, label='DSU', color='blue')
plt.plot(steps, bfs_times, label='BFS', color='red')
plt.xlabel('Insertion Step')
plt.ylabel('Time (seconds)')
plt.title('Time per Robot Addition')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(steps, dsu_cluster_counts, label='DSU Clusters', color='green')
plt.plot(steps, bfs_cluster_counts, label='BFS Clusters', color='orange')
plt.xlabel('Insertion Step')
plt.ylabel('Cluster Count')
plt.title('Cluster Count Over Time')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()