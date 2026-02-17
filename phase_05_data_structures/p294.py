def max_water(height):
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        max_area = max(max_area, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

print(max_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(max_water([1, 1]))
print(max_water([4, 3, 2, 1, 4]))