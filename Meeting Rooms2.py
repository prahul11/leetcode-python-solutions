"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

intervals=[(1,5),(5,10),(10,15),(15,20)]

# mera solution
# class Solution:
def minMeetingRooms( intervals) -> int:
    # l = [(s.start, "s") for s in intervals] + [(s.end, "e") for s in intervals]
    l = [(s[0], "s") for s in intervals] + [(s[1], "e") for s in intervals]
    l.sort()
    print(l)
    cnt = 0
    res = 0
    for i in l:
        if i[1] == "s":
            cnt += 1
            res = max(cnt, res)
        else:
            cnt -= 1
    return  res 

# print(minMeetingRooms(intervals))


class Solution:
    def minMeetingRooms(self, intervals) -> int:
        start = sorted([ i.start for i in intervals])
        end = sorted([ i.end for i in intervals])
        res, cnt =0,0
        s,e = 0,0
        while s < len(intervals):
            if start[s] < end[e]:
                cnt += 1
                s += 1
            else:
                cnt -= 1
                e+=1
            res = max(res, cnt)
        return res


class Solution:
    def minMeetingRooms(self, intervals) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        result , count =0,0
        s,e=0,0

        while s< len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                count -= 1
                e += 1
            result = max(count, result)
        return result
