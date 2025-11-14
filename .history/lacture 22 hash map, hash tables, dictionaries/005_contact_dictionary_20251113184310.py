# Here we are making contact default dictionary

from collections import defaultdict

contactMap = defaultdict(list)

print(contactMap["nitin"])

contactMap["nitin"].append("1234")
contactMap["nitin"].append("0000")
contactMap["neha"].append("124")
contactMap["neha"].append("1111")
contactMap["manisha"].append("1254")

print(contactMap)

for key in contactMap:
    print(key)
    
for val in contactMap.values():
    print(val)
    
for key,val