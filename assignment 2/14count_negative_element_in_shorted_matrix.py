def count_neg_element(arr:list, m:int , n:int)->int:
    
    m , n = int(input()) , int(input())
    nums = [[None] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            nums[i][j] = int(input())