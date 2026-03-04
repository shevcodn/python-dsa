import heapq
def k_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return sorted(heap, reverse=True)

print(k_largest([3, 1, 5, 12, 2, 11], 3))
print(k_largest([7, 10, 4, 3, 20, 15], 2))