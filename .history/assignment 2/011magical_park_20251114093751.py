n , m , k , s = map(int,input().split())

park = [input().split() for _ in range(n)]

# park = [[None ]*n for _ in range(n)]
# for i in range(0,n):
#     rows = []
#     rows = input().split()
#     park.append(rows)
check = 0
for i in range(0,n):
    for j in range(0,m):
        cell = park[i][j]
        if cell == '#':
            break
        if j != m-1:
            s-=1
            if s<k:
                check = 1
                break
        
        if cell == '.':
            s-=2
            
        elif cell == '*':
            s+=5
        if s<k:
            check = 1
            break
    if check == 1:
        break
    
if check ==0:
    print("Yes")
    print(s)
else:
    print("No")