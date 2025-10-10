def f(n:int)->None:
    #base case
    if n == 0:
        return
    
    # recursive case
    print(n)

n = int(input().strip())
f(n)