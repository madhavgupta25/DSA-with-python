m , n , k ,s = map(int, input().split())
park = [[None] * n for _ in range(m)]
check =0
for i in range(0,n):
    row=[]
    row = input().split()
    park.append(row)

for i in range(0,n):
    for j in range(0,m):
        if park[i][j]=='.':
            s-=2
        if park[i][j]=='*':
            s+=5
        if (park[i][j]=='#' or j==m-1):
            break
        s-=1
        if (s<k):
            check = 1
if check ==0:
    print("Yes")
    print(s)
else:
    print("No")
        
