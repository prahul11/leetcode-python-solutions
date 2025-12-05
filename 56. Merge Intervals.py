intervals = [[1,3],[2,6],[8,10],[15,18]]


def gljk(intervals):
    intervals.sort(key = lambda x:x[0])
    f = [intervals[0]]
    for i, j in intervals[1:]:
        if i > f[-1][-1] :
            f.append([i,j])
        else:
            start = min(f[-1][0], i)
            end = max(f[-1][-1], j)
            f[-1]=[start,end]
    return f

def nhhgfjh(intervals):
    intervals.sort(key = lambda x: x[0])
    output = [intervals[0]]
    for start, end in intervals[1:]:
        le = output[-1][1]
        if start <= le:
            output[-1][1]= max(end, le)
        else:
            output.append([start, end])
    return output