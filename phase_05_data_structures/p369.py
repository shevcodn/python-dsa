import heapq

def kth_smallest(matrix, k):
    min_heap = []
    for i in range(min(k, len(matrix))):
        heapq.heappush(min_heap, (matrix[i][0], i, 0))
    
    for _ in range(k - 1):
        value, row, col = heapq.heappop(min_heap)
        if col + 1 < len(matrix[0]):
            heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
    return min_heap[0][0]


matrix = [[1,5,9],[10,11,13],[12,13,15]]
print(kth_smallest(matrix, 8))

matrix2 = [[1,2],[1,3]]
print(kth_smallest(matrix2, 2))