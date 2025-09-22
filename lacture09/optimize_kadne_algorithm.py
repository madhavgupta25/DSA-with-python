import sys
# time complexity O(n)
# space complexity O(1)
# this is the prefix sum approach

def maximum_subarray_sum(arr: list[int], n: int) -> int:
    x= [None]*n
    x=arr[0]
    max_so_far=x

    for i in range(1,n):
        x = max(x+arr[i] , arr[i])
        max_so_far=max(max_so_far,x)

    return max_so_far
# arr = [-2,1,-3,4,-1,2,1,-5,4]
arr = [-3 , 2 , -1 , 4 , -5]
n=len(arr)
print(maximum_subarray_sum(arr,n))