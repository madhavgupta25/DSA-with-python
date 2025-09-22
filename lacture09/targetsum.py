def target_sum_pairs(arr: list[int], n:int , t:int)->int:
    count=0
    for i in range(0,n-1):
        for j in range(i+1,n):
            pair_sum=arr[i]+arr[j]
            if pair_sum==t:
                count+=1

    return count          # print((arr[i],arr[j]),end=" ")

arr = [10,20,30,40,50]
n=len(arr)
t=60
print(target_sum_pairs(arr,n,t))