def conversion_any_to_any(b1:int,b2:int,n:int)->int:
    dec_val = 0
    power = 0
    while n > 0:
        d = n % 10
        dec_val = dec_val+(d * (b1**power))
        n //=10
        power+=1
    print (dec_val)
    result = ""
    while dec_val > 0:
        rem = dec_val % b2
        result = str(rem) + result
        dec_val //= b2
        
    return result if result != "" else "0"            
    
    

b1 = int(input("Enter the input number base : ").strip())
b2 = int(input("Enter the output number base : ").strip())
n = int(input("input the number : ").strip())

print(conversion_any_to_any(b1,b2,n))