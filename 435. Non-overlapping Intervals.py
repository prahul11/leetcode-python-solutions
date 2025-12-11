intervals = [[1,2],[2,3],[3,4],[1,3]]

def jlhc(intervals):
    intervals.sort()
    res =0
    current = intervals[0][1]
    for i,j in intervals[1:]:
        if i >= current:
            current = j
        else:
            res+=1
            current = min(current, j)
    return res


def khf(intervals):
    intervals.sort(key = lambda x : x[0])
    res =0
    prevEnd = intervals[0][1]
    for start, end in intervals[1:]:
        if start >= prevEnd:
            prevEnd = end
        else:
            res+=1
            prevEnd = min(prevEnd, end)
    return res