arr = [5, 3, 6, 7, 2, 1, 4]
n=len(arr)

stk= []
ans= []

for i in range(n-1 , -1, -1):
    # find the greatest element on the right side of arr[i]
    while len(stk) != 0 and stk[-1] <= arr[i]:
        stk.pop()
        
    if len(stk) == 0:
        ans.append(-1)
        
    else:
        ans.append(stk[-1])
        
    stk.append(arr[-1])
    
ans = ans[::-1]
print(ans)