class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        prevEnd = intervals[0][1]
        removals = 0
        for start, end in intervals[1:]:
            if start < prevEnd:
                removals += 1
            else:
                prevEnd = end
        return removals

            