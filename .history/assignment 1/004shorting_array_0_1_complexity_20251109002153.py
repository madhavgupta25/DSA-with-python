n = int(input("Enter the size of array : "))
arr = [int(input().strip()) for _ in range(n)]
    

zeros = 0
for num in arr:
    if num == 0:
        zeros+=1
        
sorted_array = [0] * zeros + [1] *(n-zeros)
print datatype(sorted_array)
print (*sorted_array) 
    