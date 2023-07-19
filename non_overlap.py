class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda interval: interval[1]) 
        end = intervals[0][1]
        count = len(intervals) - 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:
                count -= 1
                end = intervals[i][1]  # Update the end point

        return count

nonoverlap = Solution()
intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(nonoverlap.eraseOverlapIntervals(intervals))
