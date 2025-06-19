import numpy as np

def floyd_warshall(edges, vertecies):
    dist = np.full((vertecies, vertecies), np.inf, dtype=np.float32)
    np.fill_diagonal(dist, 0)

    for edge in edges:
        u, v, w = int(edge[0]), int(edge[1]), edge[2]
        dist[u, v] = w

    for k in range(vertecies):
        for i in range(vertecies):
            for j in range(vertecies):
                if dist[i, k] + dist[k, j] < dist[i, j]:
                    dist[i, j] = dist[i, k] + dist[k, j]

    return dist

def print_nicely(dist):
    for i in range(vertecies):
      for j in range(vertecies):
        if i != j and not np.isinf(dist[i, j]):
            print(f"{i} -> {j}: {dist[i, j]}")

if __name__ == "__main__":
    vertecies = 6
    edges = np.array([
        [0, 1, 3],
        [0, 5, 10],
        [1, 2, 3],
        [2, 3, 1],
        [2, 4, 4],
        [3, 4, 4],
        [5, 4, 2],
        [5, 2, 8]
    ], dtype=np.float)
    dist = floyd_warshall(edges, vertices)
    print(dist)
    print_nicely(dist)
