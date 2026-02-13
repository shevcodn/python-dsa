def is_palindrome(s):
    if len(s) == 0:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])
    
print(is_palindrome("racecar"))
print(is_palindrome("hello"))
print(is_palindrome("a"))
print(is_palindrome(""))