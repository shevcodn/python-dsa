def min_eating_speed(piles, h):
    left, right = 1, max(piles)
    while left < right:
        mid = left + (right - left) // 2
        hours_needed = sum((pile + mid - 1) // mid for pile in piles)
        if hours_needed > h:
            left = mid + 1
        else:
            right = mid
    return left

print(min_eating_speed([3,6,7,11], 8))
print(min_eating_speed([30,11,23,4,20], 5))
print(min_eating_speed([30,11,23,4,20], 6))