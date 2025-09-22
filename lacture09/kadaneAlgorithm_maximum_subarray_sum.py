import sys
# time complexity O(n)
# space complexity O(n)
def maximum_subarray_sum(arr: list[int], n: int) -> int:
    x= [None]*n
    x[0]=arr[0]
    max_so_far=arr[0]

    for i in range(1,n):
        x[i]=max(x[i-1]+arr[i] , arr[i])
        max_so_far=max(max_so_far,x[i])

    return max_so_far
# arr = [-2,1,-3,4,-1,2,1,-5,4]
arr = [-3 , 2 , -1 , 4 , -5]
n=len(arr)
print(maximum_subarray_sum(arr,n))