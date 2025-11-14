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
    
print(capital_map.grt("italy", 0))

print(capital_map)

print("italy" in capital_map)

