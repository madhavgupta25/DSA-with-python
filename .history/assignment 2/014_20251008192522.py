def count_negatives(matrix:list[list[int]], m:int, n:int)->int:
    count = 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j]>0:
                break
            else:
                count+=1
    return count


m, n=map(int,input().split())
# matrix = [list(map(int,input().split())) for _ in range(m)] # wrong
matrix = [[0]*n for _ in range(m)]
for i in range(m):
    matrix[i] = list(map(int,input().split()))
     
# matrix.sort() it understend we have to input sort matrix buit if not then we sort it👍👍
print("The number of negative number is : " , count_negatives(matrix,m,n))

     