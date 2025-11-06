num = input("Enter a binary number: ").strip()
dec = 0
for i in num: #here i shows each charcter 
    dec = dec * 2 + int(i)
print(dec)