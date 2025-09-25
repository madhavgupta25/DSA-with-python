from collections import defaultdict

contact_map = defaultdict(list)

contact_map["nitin"].append("1234567890")
contact_map["nitin"].append("9876543210")

print(contact_map)

contact_map["hitesh"].append("0000000000")
contact_map["hitesh"].append("1111111111")

print(contact_map)

for key in contact_map:
    print(key)
print()