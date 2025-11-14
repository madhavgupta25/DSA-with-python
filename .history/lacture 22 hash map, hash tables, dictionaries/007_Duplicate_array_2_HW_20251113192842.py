# brute force apprach O(n2)
# def duplicate_found_near(arr:list[int],k:int)->bool: 
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if i!= j and arr[i] == arr[j]:
#                 if abs( i - j ) <= k:
#                     return True
#     return False

#using dictionary approach 
def duplicate_found_near(arr: list[int], k: int) -> bool:
    last_index = {}
    for i, num in enumerate(arr):
        if num in last_index and i - last_index[num] <= k:
            return True
        last_index[num] = i
    return False



arr = list(map(int,input().split()))
k = int(input())
print(duplicate_found_near(arr,k))