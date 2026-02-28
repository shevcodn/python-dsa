def word_break(s, word_dict):
    word_set = set(word_dict)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    return dp[len(s)]

def word_break_all(s, word_dict):
    word_set = set(word_dict)
    memo = {}
    def dp(start):
        if start == len(s):
            return [[]]
        if start in memo:
            return memo[start]
        result = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in word_set:
                for rest in dp(end):
                    result.append([word] + rest)
        memo[start] = result
        return result
    return [' '.join(words) for words in dp(0)]
        
    
print(word_break("leetcode", ["leet", "code"]))
print(word_break("applepenapple", ["apple", "pen"]))
print(word_break("catsandog", ["cats", "dog", "sand", "and", "cat"]))

print(word_break_all("catsanddog", ["cat", "cats", "and", "sand", "dog"]))