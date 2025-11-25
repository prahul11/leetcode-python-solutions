"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        if not intervals: return True
        intervals.sort(key = lambda x:x.start)
        l2= intervals[0].end
        for i in range(1, len(intervals)):
            if intervals[i].start >= l2:
                l2=intervals[i].end
            else:
                return False
        return True


# Actual
class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        if not intervals : return True
        intervals.sort(key = lambda x: x.start)
        for i in range(1, len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]
            if i1.end > i2.start:
                return False
        return True