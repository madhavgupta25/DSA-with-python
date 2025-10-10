def f (n:int,src:str,hlp:str,des:str)->None:
    #base case
    
    #recursive case
    f(n-1,src,dst,hlp)
    
    print(f"move disk from {src} to {dst}")
    
    f(n-1)
    
n = map(int, input())
f(n, A , B , C)