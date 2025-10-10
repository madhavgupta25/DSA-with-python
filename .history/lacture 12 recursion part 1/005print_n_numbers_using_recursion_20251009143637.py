def f(n:int)->None:
    #base case
    if n == 0:
        return
    
    f(n-1)
    
    print(n , end=" ")
    
    

n = int(input().strip())
print(f(n))