def longest_k_distincts(s, k):
    char_count = {}
    left = 0
    max_len = 0

    for right in range(len(s)):
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

print(longest_k_distincts("eceba", 2))
print(longest_k_distincts("aa", 1))
print(longest_k_distincts("abcadcacacaca", 3))
print(longest_k_distincts("a", 0))
