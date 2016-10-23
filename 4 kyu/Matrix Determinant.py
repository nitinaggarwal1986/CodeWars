def determinant(matrix):
    
    firstRow = matrix[0]
    n = len(firstRow)
    
    if n == 1:
        return matrix[0][0]
    
    deter = 0
    
    for i in range(n):
        deter = deter + (-1) ** i * firstRow[i] * determinant([[x[j] for j in range(len(x)) if j != i] for x in matrix[1:]])
    
    return deter