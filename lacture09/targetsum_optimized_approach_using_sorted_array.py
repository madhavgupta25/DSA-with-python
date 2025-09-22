def target_sum(arr:list[int],n:int,t:int)->int:
    count = 0
    i , j=0 , n-1
    while i<j:
        pair_sum=arr[i]+arr[j]
        if pair_sum == t:
            count+=1
            i+=1
            j-=1
        elif pair_sum > t:
            j-=1

        else:
            i+=1 # pair_sum <t
    return count


arr=[10,20,30,40,50]
n=len(arr)
t = 60
print(target_sum(arr,n,t))