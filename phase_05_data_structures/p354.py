from collections import Counter

def top_kth_frequent(nums, k):
    count = Counter(nums)
    most_common = count.most_common(k)
    return [num for num, freq in most_common]

print(top_kth_frequent(["i", "love", "leetcode", "i", "love", "coding"], 2))
print(top_kth_frequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))
    