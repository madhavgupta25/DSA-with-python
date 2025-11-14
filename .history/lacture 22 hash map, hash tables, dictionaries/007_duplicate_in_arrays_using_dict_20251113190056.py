# approach1: 
# step1:sort the array (nlogn)
# step2: scan the array (n) 

#approach2:
# step1:build a frequency map
# step2: look for the element whose frequency is >1

from collections import defaultdict

def is_duplicate_present(arr:list[int])->bool:
    freq_map = defaultdict(int)
    for item in arr:
        freq_map[item] +=1
    print(freq_map)


arr = [1,2,3,4,1,2,1]
print(is_duplicate_persent(arr))