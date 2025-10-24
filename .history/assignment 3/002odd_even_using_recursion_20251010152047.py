def odd(n:int):
    # base case
    if n == 0:
        return
    if n%2 == 1:
        print(n)
    odd(n-1)
    
def even(n,i=2):
    #base case
    if i > n:
        return
    print
    even(n-1)
    
n = int(input())
odd(n)
even(n)
