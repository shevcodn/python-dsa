def generate_parentheses(n):
    result = []
    def backtrack(current, open, close):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open < n:
            backtrack(current + '(', open + 1, close)
        if close < open:
            backtrack(current + ')', open, close + 1)
    backtrack('', 0, 0)
    return result

print(generate_parentheses(1))
print(generate_parentheses(2))
print(generate_parentheses(3))