def array_intersection(arr1:list[int],arr2:list[int])->list[int]:
    intersection = []
    for i in arr1:
        # if i in arr2 and i in intersection:
        #     intersection.append(i) 
        if i in arr2:
            intersection.append(i) 
    
    intersection.sort()
    return intersection


n = int(input("Enter the size of both arrays: "))
arr1 = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
print(array_intersection(arr1,arr2))