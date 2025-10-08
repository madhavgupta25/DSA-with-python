def sum(m:int, n:int, arr1:list[int], arr2:list[int])->list[int]:
    i = m-1
    j = n-1
    carry = 0
    result =[]
    while i>=0 or j >= 0 or carry:
        x = arr1[i] if i>=0 else 0
        y = arr2[j] if j>=0 else 0
        
        s = x+y+carry
        
        result.append(s%10)
        carry = carry // 10
        
        i-=1
        j-=1
        
    return result[::-1]
        
        
    
m = int(input().strip())
arr1 = list(map(int, input().split()))

n = int(input().strip())
arr2 = list(map(int, input().split()))

ans = sum(m,n,arr1,arr2)
print(", ".join(map(str,ans)),", END", sep ="")


