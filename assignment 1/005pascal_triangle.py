def pt(n : int)->int:
    for i in range(0,n):
        print(" "*(n-i),end=" ")
        val = 1
        for j in range(i+1):
            print(val,end=" ")
            val = val * (i-j) // (j+1)
        print()
    
n = int(input("Enter the size of triangle : ").strip())
print(pt(n))