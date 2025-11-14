
def duplicate_found_near(arr:list[int],k:int)->bool:
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                if abs( i - j ) <= k:
                    return True
    return False
                
    


arr = list(map(int,input().split()))
k = int(input())
print(duplicate_found_near(arr,k))