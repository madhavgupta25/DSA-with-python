# this is the assignment que 1 of python with DSA
nums=input("Enter the numbers in list: ").split()
sum_even=0
sum_odd=0
for i in nums:
    if int(i)%2==0:
        sum_even+=nums(i)
    else:
        sum_odd+=nums(i)
print("Sum of even numbers is: ",sum_even)
print("Sum of odd numbers is: ",sum_odd)