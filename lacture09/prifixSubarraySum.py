import sys
# time complexity O(n^2)
# space complexity O(n)
# this is the prefix sum approach
def prefix_subarray_sum(arr:list[int],n:int)->int:
    psum=[None]*n # prefix sum array
    psum[0]=arr[0]
    for i in range(1,n):
        psum[i]=psum[i-1]+arr[i]
    max_so_far= -sys.maxsize-1
    for i in range(n):
        for j in range(i,n):
            s = psum[j] if i== 0 else psum[j]-psum[i-1]
            max_so_far=max(max_so_far,s)
    return max_so_far
arr=[-2,1,-3,4,-1,2,1,-5,4]
n=len(arr)
print(prefix_subarray_sum(arr,n))


