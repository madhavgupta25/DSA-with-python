def is_prime(n)->bool :
    i = 2
    while i<=(int(n**0.5)):
        if n%i==0:
            return False
        i+=1
    return True
def series_of_prime_number(n : int) -> list[int] :
    ans = []
    for i in range(2,n+1):
        if is_prime(i):
            ans.append(i)
    return ans
n = int(input("Enter the number: "))
print(series_of_prime_number(n))
