from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]

print(top_k_frequent([1,1,1,2,2,3], 2))
print(top_k_frequent([1], 1))
print(top_k_frequent([1,2,2,3,3,3], 2))
