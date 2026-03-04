def reverse_string(s):
    left, right = 0, len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]
        left = left + 1
        right = right - 1

    return s

print(reverse_string(["h", "e", "l", "l", "o"]))
print(reverse_string(["A", "b", "C"]))