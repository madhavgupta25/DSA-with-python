num = input("Enter a binary number: ").strip()
dec = 0
for i in num: 
    dec = dec * 2 + int(i)
print(dec)