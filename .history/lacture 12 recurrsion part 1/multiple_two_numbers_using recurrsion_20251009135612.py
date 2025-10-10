def f(x:int,y:int)->int:
    # base case
    if y == 0:
        return 1
    
    # recursion case
    

x , y = map(int, input().split())
print(f(x,y))