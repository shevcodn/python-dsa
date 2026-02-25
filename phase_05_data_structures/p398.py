def can_attend(intervals):
    if not intervals:
        return True
    
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True

print(can_attend([[0,30],[5,10],[15,20]]))
print(can_attend([[7,10],[2,4]]))
print(can_attend([[1,5],[5,10]]))