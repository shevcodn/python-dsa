def largest_rectangle(heights):
    stack = []
    max_area = 0
    heights = heights + [0]

    for i, h in enumerate(heights):
        start = i
        while stack and heights[stack[-1]] > h:
            idx = stack.pop()
            width = i - stack[-1] - 1 if stack else i
            height = heights[idx]
            max_area = max(max_area, width * height)
            start = idx
        stack.append(start)

    return max_area

print(largest_rectangle([2, 1, 5, 6, 2, 3]))
print(largest_rectangle([2, 4]))
print(largest_rectangle([1]))
print(largest_rectangle([1, 2, 3, 4, 5]))