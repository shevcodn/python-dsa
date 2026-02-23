from collections import Counter

def k_most_frequent(nums, k):
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]

print(k_most_frequent([1,1,1,2,2,3], 2))
print(k_most_frequent([1], 1))
    