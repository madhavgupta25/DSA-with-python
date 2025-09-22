def maze(maze:list[list[str]], path:list[list[str]], m:int, n:int, i:int, j:int):
    if i == m or j== n:
        return
    
    if maze[i][j] == 'X':
        return
    
    if i == 



maze = [['0', '0', '0', '0'],
        ['0', '0', 'X', '0'],
        ['0', '0', '0', 'X'],
        ['0', 'X', '0', '0']]

m = len(maze)
n = len(maze[0])

path = [['0']*n for in range(m)]
