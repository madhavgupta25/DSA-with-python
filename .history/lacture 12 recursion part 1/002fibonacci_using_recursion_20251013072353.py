def fibo(n:int)->int:
    #base case
    if n == 0 or n== 1:
        return n
    
    # recurrsive case
    a = fibo(n-1)
    n = fibo (n-2)
    return a+n
8


n = int(input("Enter the number : "))
#fib_list = []

arr = ''.join.append(n)
print("The Fibonaci of ",n," is ", fibo(n))