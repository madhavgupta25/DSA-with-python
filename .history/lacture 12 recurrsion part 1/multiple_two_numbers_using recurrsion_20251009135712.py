def f(x:int,y:int)->int:
    # base case
    if y == 0:
        return 1
    
    # recursion case
    A = f(x,y-1)
    return A

x , y = map(int, input().split())
print(f(x,y))