s = "1??0?101"
count = s.count('?')
for i in range(2 ** count):
    bits = f"{i:0{count}b}"   # convert to binary with padding
    res = ""
    bit_idx = 0
    for ch in s:
        if ch == '?':
            res += bits[bit_idx]
            bit_idx += 1
        else:
            res += ch
    print(res, end=" ")
