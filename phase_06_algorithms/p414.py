def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def is_palindrome_alphanumeric(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def longest_palindromic_substring(s):
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    result = ""
    for i in range(len(s)):
        result = max(result, expand(i, i), expand(i, i + 1), key=len)
    return result

def is_almost_palindrome(s):
    def valid(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return valid(s, left + 1, right) or valid(s, left, right - 1)
        left += 1
        right -= 1
    return True

print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("abcba"))
print(is_palindrome("a"))

print(is_palindrome_alphanumeric("A man, a plan, a canal: Panama"))
print(is_palindrome_alphanumeric("race a car"))

print(longest_palindromic_substring("babad"))
print(longest_palindromic_substring("cbbd"))
print(longest_palindromic_substring("racecar"))

account_ids = ["ABA12321ABA", "ACC789987CCX", "TXN456654NXT"]
for acc_id in account_ids:
    alphanum = ''.join(c for c in acc_id if c.isalnum())
    print(f"{acc_id}: palindrome={is_almost_palindrome(alphanum)}")
