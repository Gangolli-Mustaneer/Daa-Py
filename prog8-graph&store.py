def create_adjacency_matrix(vertices, edges):
    matrix = [[0] * vertices for _ in range(vertices)]
    for u, v in edges:
        if 0 <= u < vertices and 0 <= v < vertices:
            matrix[u][v] = matrix[v][u] = 1
    return matrix

vertices = int(input("Enter number of vertices: "))
edges = [tuple(map(int, input("Enter an edge (u v): ").split())) for _ in range(int(input("Enter number of edges: ")))]
matrix = create_adjacency_matrix(vertices, edges)

for row in matrix:
    print(" ".join(map(str, row)))