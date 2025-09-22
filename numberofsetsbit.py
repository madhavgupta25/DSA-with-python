# this is the hone work for how to find the number of set bits in a number;
n = int(input("Enter the number: "))
count = 0
while n>0:
    if (n&1) :
        count += 1
    n = n >> 1
print(count)
# --- IGNORE ---    