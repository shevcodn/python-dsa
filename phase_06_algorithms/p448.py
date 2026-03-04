def longest_consecutive(nums):
    num_set = set(nums)

    max_len = 0

    for num in num_set:
        if num - 1 not in nums:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            max_len = max(length, max_len)

    return max_len

print(longest_consecutive([100, 4, 200, 1, 3, 2]))
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
print(longest_consecutive([1]))