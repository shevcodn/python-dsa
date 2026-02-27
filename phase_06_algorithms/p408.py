def is_valid(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    return len(stack) == 0

def min_remove_to_valid(s):
    stack = []
    to_remove = set()
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                to_remove.add(i)
    to_remove |= set(stack)
    return ''.join(c for i, c in enumerate(s) if i not in to_remove)

def validate_json_structure(s):
    stack = []
    pairs = {'}': '{', ']': '['}
    for char in s:
        if char in '{[':
            stack.append(char)
        elif char in '}]':
            if not stack or stack[-1] != pairs[char]:
                return False, f"Unexpected '{char}'"
            stack.pop()
    if stack:
        return False, f"Unclosed '{stack[-1]}'"
    return True, "Valid"

print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("([)]"))
print(is_valid("{[]}"))

print(min_remove_to_valid("lee(t(c)o)de)"))
print(min_remove_to_valid("a)b(c)d"))
print(min_remove_to_valid("))(("))

api_responses = [
    '{"status": "ok", "data": [1, 2, 3]}',
    '{"status": "error", "code": 400',
    '[{"id": 1}, {"id": 2}]',
]

for resp in api_responses:
    brackets_only = ''.join(c for c in resp if c in '{}[]')
    valid, msg = validate_json_structure(brackets_only)
    print(f"  {msg}: {resp[:40]}")
