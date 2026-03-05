def max_water(height):
    left = 0
    right = len(height) - 1
    max_vol = 0

    while left < right:
        h = min(height[left], height[right])
        width = right - left
        max_vol = max(max_vol, h * width)

        if height[left] < height[right]:
            left = left + 1
        else:
            right = right - 1

    return max_vol

print(max_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(max_water([1, 1]))
print(max_water([4, 3, 2, 1, 4]))
print(max_water([1, 2, 1]))