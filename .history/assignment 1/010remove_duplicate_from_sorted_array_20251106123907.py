
n = int(input("Enter the size of array : ").strip())
arr = list(map(int, input().split()))
arr= list(map(int,input.sp))

result=[]
for i in range(n):
    if arr[i] not in result:
        result.append(arr[i])
print(len(result))
print(*result)
        