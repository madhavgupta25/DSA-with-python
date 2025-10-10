def f(n:int)->None:
    #base case
    if n == 0:
        return ""
    
    # recursive case
    return f(n//2) + str ( n%2 )
        

n = int(input())
print(f(n))