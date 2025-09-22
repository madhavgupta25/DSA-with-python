def is_prime(n : int) -> bool:
    i=2
    while i<=(int(n**0.5)):
        if n%i==0:
            return False
        i+=1
    return True
n = int(input("Enter the number:"))
print(is_prime(n))
    