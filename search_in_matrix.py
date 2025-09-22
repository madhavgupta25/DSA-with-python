def searchMatrix(matrix, target: int) -> bool:
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        for j in range(n):
            if target == matrix[i][j]:
                return True
    return False
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
print(searchMatrix(matrix, target))
# print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))