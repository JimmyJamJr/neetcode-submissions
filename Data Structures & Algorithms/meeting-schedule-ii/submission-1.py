"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])

        a, b = 0, 0
        jobs = 0
        peak = 0
        while a < len(intervals) and b < len(intervals):
            start, end = starts[a], ends[b]
            if start < end:
                jobs += 1
                a += 1
            else:
                jobs -= 1
                b += 1
            peak = max(peak, jobs)
        return peak