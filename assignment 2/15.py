def isToeplitz(matrix, M, N):
    for i in range(M - 1):
        for j in range(N - 1):
            if matrix[i][j] != matrix[i + 1][j + 1]:
                return False
    return True

M, N = map(int, input().split())
    
    # Read the matrix
matrix = []
for _ in range(M):
    row = list(map(int, input().split()))
    matrix.append(row)

    # Check and print result
print("true" if isToeplitz(matrix, M, N) else "false")
