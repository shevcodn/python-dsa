import heapq

def merge_k_list(lists):
    min_heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))

    merged = []
    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        merged.append(value)
        if element_index + 1 < len(lists[list_index]):
            next_tuple = (lists[list_index][element_index + 1], list_index, element_index + 1)
            heapq.heappush(min_heap, next_tuple)

    return merged

print(merge_k_list([[1,4,5],[1,3,4],[2,6]]))
print(merge_k_list([]))
print(merge_k_list([[],[1]]))
