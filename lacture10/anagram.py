#anagram : anagram is the string formed by rearranging the letters of another, such as cinema, formed from iceman and listen from silent.
# n steps to build fmap_s +n steps to build fmap_s2 + 26 steps to compare both the frequency maps
# overall time complexity : (2n + 26)  O(n)
# space complexity : (26 + 26) O(1) as we are using constant space of 26 length array

def are_anagrams(s1:str,s2:str) -> bool:
    fmap_s1 =[0]*26
    for ch in s1:
        idx = ord(ch) - ord('a')
        fmap_s1[idx]+=1
    print(fmap_s1)

    fmap_s2 =[0]*26
    for ch in s2:
        idx = ord(ch) - ord('a')
        fmap_s2[idx]+=1
    print(fmap_s2)
    
    for i in range(26):
        if fmap_s1[i] != fmap_s2[i]:
            return False # when as soon as we find a mismatch then we direct return False dont need to check further
        
    return True
    # return fmap_s1 == fmap_s2


s1=input("Enter first string: ")
s2=input("Enter second string: ")
print(are_anagrams(s1,s2))