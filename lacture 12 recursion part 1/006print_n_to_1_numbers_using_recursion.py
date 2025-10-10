def f(n:int)->None:
    #base case
    if n == 0:
        return
    
    # recursive case
    print(n, end=" ")
    f(n-1)

n = int(input().strip())
f(n)