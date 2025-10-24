def f(x:list, n:int, i:int)-> bool:
    #base case
    if i == n-1:
        return True

    # recursive case

    #f(i) = it is fn that checks if x[i...n-1] is sorted or not
    return x[i]< x[i+1] and f(x, n , i+1)



n = int(input("Enter the size of array: "))
arr = list(map(int, input("Enter the elements of array: ").split()))
print(f(arr ,n , 0))