from collections import Counter

def least_bricks(wall):
    count = Counter()
    for row in wall:
        edge_sum = 0
        for brick in row[:-1]:
            edge_sum += brick
            count[edge_sum] += 1
    if count:
        return len(wall) - max(count.values())
    return len(wall)

wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
print(least_bricks(wall))