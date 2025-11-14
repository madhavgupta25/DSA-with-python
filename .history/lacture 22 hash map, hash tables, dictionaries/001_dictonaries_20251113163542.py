capitalMap = {
    "India" : "New Delhi",
    "USA" : "Washington DC",
    "Russia": "Moscow",
    "Japan": "Tokyo"
}
print(capitalMap)
print(capitalMap.keys())
print(capitalMap.values())
print(capitalMap.items())

key_val_list = [("India","New Delhi"),("USA","Washington DC"),("Russia","Moscow"),("Japan","Tokyo")]
capitalMap2 = dict(key_val_list)