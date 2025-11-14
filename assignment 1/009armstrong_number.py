def is_armstrong(n:int)->bool:
    s=str(n)
    power = len(str(n))
    sum = 0
    for i in s:
        sum=sum+int(i)**power
    return n == sum
    
n = int(input("Enter the number to check armstrong : ").strip())
print(is_armstrong(n))