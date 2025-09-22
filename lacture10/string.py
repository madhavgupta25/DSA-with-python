s = "Hi how are you"
print(s.split())
l=s.split()
print(type(l))
for word in l:
    print(word)
sport="cricket,football,tennis,hockey"
print(sport.split(","))
len = sport.split(",")
for w in len:
    print(w)

fruits="mango, orange, banana, apple"
print(fruits.split(", "))
nums = {"10","20","30","40","50"}
s = "-".join(nums)
print(s)
country = "India"
year = 1947
print(country + " is indenpendent in the " + str(year)+ ".")
print(f"{country} is independent in the {year}.")
