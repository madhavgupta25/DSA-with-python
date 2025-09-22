def generate_subarray(arr:list[int],n:int,count:int)->None:
    # iterate over the arrray
    for i in range(n):
        for j in range(i, n):
            a = []
            for k in range(i, j + 1):
                a.append(arr[k])
            print(a)
            count += 1
    print("Total number of subarrays are:",count)
arr=[1,2,3,4]
n=len(arr)
count=0
generate_subarray(arr,n,count)