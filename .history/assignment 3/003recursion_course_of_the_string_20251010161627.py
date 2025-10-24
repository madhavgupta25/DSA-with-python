def get_codes(s):
    # Base Case: empty string
    if len(s) == 0:
        return [""]

    # Base Case: single digit
    if len(s) == 1:
        if s[0] == "0":  # '0' has no mapping
            return []
        return [chr(int(s[0]) + 96)]  # '1' -> 'a', '2' -> 'b' ...

    result = []

    # --- Choice 1: take one digit ---
    if s[0] != "0":
        first_char = chr(int(s[0]) + 96)
        for code in get_codes(s[1:]):
            result.append(first_char + code)

    # --- Choice 2: take two digits ---
    two_digit = int(s[:2])
    if 10 <= two_digit <= 26:
        second_char = chr(two_digit + 96)
        for code in get_codes(s[2:]):
            result.append(second_char + code)

    return result


# ----- Driver Code -----
s = input().strip()
ans = get_codes(s)
print(ans)
