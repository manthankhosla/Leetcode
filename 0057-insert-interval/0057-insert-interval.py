class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):

            # Current interval is completely before newInterval
            if intervals[i][1] < newInterval[0]:
                res.append(intervals[i])

            # Current interval starts after newInterval
            elif intervals[i][0] > newInterval[1]:#note this..line
                res.append(newInterval)
                res.extend(intervals[i:])
                return res

            # Overlap
            else:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])

        res.append(newInterval)
        return res