def array_target_sum_triplets(n:int,arr:list[int],target:int)->list[int]:
    arr.sort()
    triplets = set()
    for i in range(n):
        left = i+1
        right = n-1
        while left < right:
            s = arr[i]+arr[left]+arr[right]
            if target == s:
                triplets.add((arr[i],arr[left],arr[right]))
                left+=1
                right-=1
            elif s < target:
                left+=1
            else:
                right-=1
        
    for a , b , c in sorted(triplets):
        print(f"{a} , {b} and {c}")
        

n = int(input("Enter the size of array : ").strip())
arr = list(map(int, input().split()))
target = int(input("enter the target : ").strip())

array_target_sum_triplets(n,arr,target)