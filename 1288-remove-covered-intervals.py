class Solution:
    """
    起点正向排序，终点逆向大到小排序，最终只要终点大于前一个的就是可以被覆盖的
    """
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort by start point.
        # If two intervals share the same start point
        # put the longer one to be the first.
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0

        prev_end = 0
        for _, end in intervals:
            # if current interval is not covered
            # by the previous one
            if end > prev_end:
                count += 1
                prev_end = end

        return count
