from collections import Counter

def four_sum_count(nums1, nums2, nums3, nums4):
    count = Counter()
    for a in nums1:
        for b in nums2:
            count[a + b] += 1

    result = 0
    for c in nums3:
        for d in nums4:
            result += count[-(c + d)]

    return result

print(four_sum_count([1,2], [-2,-1], [-1,2], [0,2]))
print(four_sum_count([0], [0], [0], [0]))