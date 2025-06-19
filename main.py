def floyd_warshall(vertices: int, edges: list[(int, int, int)], source: int) -> list[int]:
    dist = [[float('inf')] * vertices for _ in range(vertices)]

    for i in range(vertices):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = w

    for k in range(vertices):
        for i in range(vertices):
            for j in range(vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist[source]

if __name__ == "__main__":
    vertices = 6
    edges = [
        (0, 1, 3),
        (0, 5, 10),
        (1, 2, 3),
        (2, 3, 1),
        (2, 4, 4),
        (3, 4, 4),
        (5, 4, 2),
        (5, 2, 8)
    ]
    print(floyd_warshall(vertices, edges, 0))
