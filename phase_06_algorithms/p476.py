from collections import Counter

def top_k_frequent(nums, k):
    count = Counter(nums)


    return [item for item, freq in count.most_common(k)]

def top_k_frequent_v2(nums, k):
    count = {}
    for n in nums:
        count[n] = count.get(n, 0) + 1

    
    sorted_items = sorted(count, key=lambda x: count[x], reverse=True)
    return sorted_items[:k]

print(top_k_frequent([1,1,1,2,2,3], 2))
print(top_k_frequent([1], 1))
print(top_k_frequent([1,2,3,4,5,6,7], 2))

print(top_k_frequent_v2([1,1,1,2,2,3], 2))
print(top_k_frequent_v2([4,4,4,6,6,7], 2))