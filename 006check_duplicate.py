from collections import defaultdict

def is_duplicate_present(arr:"list(int)")->bool:
    freq_map = defaultdict(int)
    for item in arr:
        freq_map[item] +=1
        if freq_map[item] >= 1:
            return True
        
    return False
    # print(freq_map)
    
arr = [1,2,3,4]
print(is_duplicate_present(arr))