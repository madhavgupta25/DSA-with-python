x = 2
n = 10
def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)
print(power(x, n))