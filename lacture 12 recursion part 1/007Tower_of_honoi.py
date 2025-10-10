def f (n:int,src:str,hlp:str,dst:str)->None:
    #base case
    if n == 0:
        return
    
    #recursive case
    f(n-1,src,dst,hlp)
    
    print(f"move disk from {src} to {dst}")
    
    f(n-1,hlp,src,dst)
    
n = int(input())
f(n, 'A' , 'B' , 'C')