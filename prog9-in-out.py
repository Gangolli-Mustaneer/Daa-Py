n = int(input("Enter the number of vertices: "))

adj_matrix = []

print("Enter the adjacency matrix row by row (1 for edge, 0 for no edge):")
for i in range(n):
    row = list(map(int, input(f"Vertex {i + 1}: ").split()))
    adj_matrix.append(row)

in_degrees = [sum(row) for row in zip(*adj_matrix)]
out_degrees = [sum(row) for row in adj_matrix]

for i in range(n):
    print(f"Vertex {i + 1}: In-degree {in_degrees[i]}, Out-degree {out_degrees[i]}")

print("Adjacency matrix:")
for row in adj_matrix:
    print(*row)