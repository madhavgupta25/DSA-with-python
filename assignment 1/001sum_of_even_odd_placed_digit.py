n = int(input().strip())
sum_even = 0
sum_odd = 0
for i in range(len(str(n))):
    digit = n%10
    if i%2 == 0:
        sum_even += digit
    else:
        sum_odd += digit
    n = n//10
print(sum_even)
print(sum_odd)