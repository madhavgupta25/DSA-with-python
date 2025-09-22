#total operation = n(push) + n(pop) + 1(push) = 2n + 1
#time = O(n)
#space = O(n) 
def insert_at_bottom(s, val):
    #base case
    if len(s) == 0:
        s.append(val)
        return
    
    #recursive case
    
    x = s.pop()
    insert_at_bottom(s,val)
    s.append(x)

s=[]

s.append(10)
s.append(20)
s.append(30)
s.append(40)
s.append(50)

print(s)

insert_at_bottom(s,0)

print(s)