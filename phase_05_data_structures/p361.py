from collections import Counter

def least_interval(tasks, n):
    count = Counter(tasks)
    max_freq = max(count.values())
    max_count = sum(1 for freq in count.values() if freq == max_freq)

    return max(len(tasks), (max_freq - 1) * (n + 1) + max_count)

print(least_interval(["A", "A", "A", "B", "B", "B"], 2))
print(least_interval(["A", "A", "A", "B", "B", "B"], 0))