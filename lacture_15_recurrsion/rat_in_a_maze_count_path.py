def f(maze:list[list[str]], m:int, n:int, i:int, j:int)->bool:
    
    #base case
    if  i == m or j==n:
        return 0
    
        
    if maze[i][j] == 'X':
        return 0
    if i == m-1 and j == n-1:
        return 1
    
    # recursive case
     
    #f(i,j) = it is fn that checks if there is a path from i,jth cell

    if i == m-1:
        return f(maze, m, n, i, j+1)
    if j == n-1:
        return f(maze, m, n, i+1, j)
    
    return f(maze, m,n,i+1,j) + f(maze, m, n, i, j+1)


maze = [['0', '0', '0', '0'],
        ['0', '0', 'X', '0'],
        ['0', '0', '0', 'X'],
        ['0', 'X', '0', '0']]

m = len(maze)
n = len(maze[0])
print(f(maze, m, n, 0 ,0))