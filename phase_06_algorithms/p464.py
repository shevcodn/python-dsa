from collections import Counter
import heapq

def top_k_frequent(nums, k):
    count = Counter(nums)
    heap = []

    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]

print(top_k_frequent([1, 1, 1, 2, 2, 3], 2))
print(top_k_frequent([1, 2, 2, 3, 3, 3], 1))

    

