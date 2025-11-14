capital_map = {
    "India": "New Delhi",
    "USA": "Washington, D.C.",
    "France": "Paris",
    "Germany": "Berlin",
    "Japan": "Tokyo", 
    "Australia": "Canberra"
}

print(capital_map["India"])  # Output: New Delhi
print(capital_map["USA"])    # Output: Washington, D.C.

if "italy" in capital_map:
    print("Italy is present in the map")
else:
    print("Italy is not present in the map")
    
if "India" in capital_map:
    print("India is present in the map")
    print(capital_map["India"])
else:
    print("India is not present in the map")
    
print(capital_map.get("italy", 0))

print(capital_map)

capital_map["italy"] = "Rome"
print("italy" in capital_map)
print(capital_map["italy"])

del capital_map["France"]
print(capital_map)

# del capital_map["Spain"] #this give an key error because spain is not present in capital_map