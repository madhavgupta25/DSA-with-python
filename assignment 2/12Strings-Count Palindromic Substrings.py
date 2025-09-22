s = input().strip()
n = len(s)

def is_palindrome(st):
    left, right = 0, len(st) - 1
    while left < right:
        if st[left] != st[right]:
            return False
        left += 1
        right -= 1
    return True

count = 0
for i in range(n):
    for j in range(i+1, n+1):
        if is_palindrome(s[i:j]):
            count += 1

print(count)
