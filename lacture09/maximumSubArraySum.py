import sys
# time complexity O(n^3)
# space complexity O(1)
# this is the brute force approach
def maximum_subarray_sum(arr:list[int],n:int)->int:
    max_so_far= -sys.maxsize-1
    for i in range(n):
        for j in range(i,n):
            s =0
            for k in range (i, j+1):
                s += arr[k]
            max_so_far=max(max_so_far,s)
    return max_so_far

arr=[-2,1,-3,4,-1,2,1,-5,4]
n=len(arr)
print(maximum_subarray_sum(arr,n))