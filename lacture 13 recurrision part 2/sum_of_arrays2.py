def f(x:list, n:int , i:int)-> int:
    #base case
    if i == n:
        return 0
    #recursive case

    # f(i) = find the sum of x[i.... n-1]

    # ask your friend to find the sum of X[i+1... n-1]
    A = f(x, n , i+1)
    return x[i]+A
    
n = int(input("Enter the size of array: "))
arr = list(map(int, input("Enter the elements of array: ").split()))
print("The sum of the given array is : ", f(arr , n , 0))