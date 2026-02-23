from collections import Counter

def longest_palindrome(s):
    count = Counter(s)
    odd_count = sum(1 for freq in count.values() if freq % 2 != 0)
    return len(s) - odd_count + (1 if odd_count > 0 else 0)

print(longest_palindrome("abccccdd"))
print(longest_palindrome("a"))
print(longest_palindrome("bb"))