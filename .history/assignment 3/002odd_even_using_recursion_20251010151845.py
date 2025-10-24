def odd(n:int):
    # base case
    if n == 0:
        return
    if n%2 == 1:
        print(n)
    odd(n-1)
    
def even(n):
    #base case
    if n == 0:
        return
    if n%2 == 0:
        print(n)
    even(n-1)
    
n = int(input())

