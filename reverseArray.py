# this code is use to reverse an array
def reverse_array(nums:list[int])->None:
     i=0
     j= len(nums) - 1
     while i<j:
          nums[i], nums[j] = nums[j],nums[i]
          i+=1
          j-+1

n= int(input("Enter the number of elements: "))
nums = [int(input("Enter the numbers in list: ")) for  _ in range(n)]
print(nums)
reverse_array(nums)
print(nums)
