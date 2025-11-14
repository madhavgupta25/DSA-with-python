def array_intersection(arr1:list[int],arr2:list[int])->list[int]:
    intersection = []
    for i in arr1:
        # if i in arr2 and i in intersection:
        #     intersection.append(i) 
        if i in arr2:
            intersection.append(i) 
    
    intersection.sort
    return intersection


n = int(input("Enter the size of both arrays: "))
arr1 = [int(input()) for _ in range(n)]
arr2 = [int(input()) for _ in range(n)]
print(array_intersection(arr1,arr2))