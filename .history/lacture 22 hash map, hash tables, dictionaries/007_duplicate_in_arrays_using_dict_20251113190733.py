# approach1: 
# step1:sort the array (nlogn)
# step2: scan the array (n) 

#approach2:
# step1:build a frequency map
# step2: look for the element whose frequency is >1

from collections import defaultdict,Counter

def is_duplicate_present(arr:list[int])->bool:
    freq_map = defaultdict(int)
    for item in arr:
        freq_map[item] +=1
    # print(freq_map)
        if freq_map[item] > 1:
            return True #you find duplicate

    return False #you dont find any duplicate

def is_duplicate_present_using_counter(arr)


arr = [1,2,3,4]
# print(Counter(arr))
print(is_duplicate_present(arr))