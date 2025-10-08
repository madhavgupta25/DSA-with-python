m , n , k , s = map(int,input().split())
# print(m,n,k,s)
park = [None for _ in range(m)]
check = 0
for i in range (0,m):
    park[i] = list(map(str, input().split()))
for i in range(0,n):
    for j in range(m):
        if park[i][j] == '.':
            s-=2
        if park[i][j] == '*':
            s+=5
        if (park[i][j] == '#' or j == m-1):
            break
        s-=1
        if ( s<k):
            check = 1
if check == 0:
    print("Yes")
    print(s)
else:
    print("No")
    
        
                