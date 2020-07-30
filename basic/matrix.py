matrix = [
    [1, 2, 3],
    [11, 12, 13],
    [5, 7, 9]
]
print(matrix)
matrix[0][1] = 4
print(matrix[0][1])
print(matrix)
for row in matrix:
    for item in row:
        print(item)
