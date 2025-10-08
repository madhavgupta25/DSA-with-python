def is_toeplitz(arr:list[list[int]],m:int,n:int)->bool:
    for i in range(1,m):
        for j in range(1,n):
                if arr[i][j]!=arr[i-1][j-1]:
                    return False
    return True

m,n = map(int, input("Enter the value of m & n : ").split())
arr = [list(map(int, input().split())) for _ in range(m)]
# arr = [[None]*n for _ in range(m)]
# for i in range(m):
#     arr[i] = list(map(int,input().split()))
    
print(is_toeplitz(arr,m,n))
