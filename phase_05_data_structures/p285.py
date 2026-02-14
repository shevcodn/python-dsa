def compress(s):
    if not s:
        return ""
    
    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i-1] + (str(count) if count > 1 else ""))
            count = 1
    compressed.append(s[-1] + (str(count) if count > 1 else ""))

    return ''.join(compressed)

print(compress("aabcccdddd"))
print(compress("abc"))
print(compress("aaaa"))