def add_matrix(matrix1, matrix2):
    """Add two matrices of the same size."""
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices must be of the same size."
    result = []
    for i in range(len(matrix1)):
        row=[]
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

mat1 = [
    [12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]   
    
]
mat2 = [
    [5, 8, 1],
    [6, 7, 3],
    [4, 2, 0]
]
result_matrix = add_matrix(mat1, mat2)
print("Resultant Matrix:")
for row in result_matrix:
    print(row)
    