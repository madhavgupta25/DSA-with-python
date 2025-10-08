m , n = map(int,input().split())
arr = list(map(int, input().split()))

mat = []
idx = 0
for i in range(m):
    row = []
    for j in range(n):
        row.append(arr[idx])
        idx += 1
    mat.append(row)

result = []
# for d in range(m+n-1):
#     for i in range(m):
#         for j in range(n):
#             if i + j == d:
#                 result.append(mat[i][j])
                
for s in range(m + n - 1):
    start_row = max(0, s - (n - 1))
    end_row = min(m - 1, s)
    temp = []
    for r in range(start_row, end_row + 1):
        c = s - r
        temp.append(mat[r][c])
    if s % 2 == 0:
        temp.reverse()
    result.extend(temp)
                
print(result)