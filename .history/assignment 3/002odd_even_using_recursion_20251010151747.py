def odd(n:int):
    # base case
    if n == 0:
        return 0
    if n%2 == 1:
        print(n)
    odd(n-1)
n = int(input())
