def gcd(a:int,b:int)->int:
    while b != 0:
        a,b = b,a%b
    return a

def lcm(a:int,b:int)->int:
    return (a *b) // gcd(a,b)

n1 = int(input().strip())
n2 = int(input().strip())

print(lcm(n1 , n2))
print(5%)