class Solution:
    def intervalIntersection(self, a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0

        while i < len(a) and j < len(b):
            s = max(a[i][0], b[j][0])
            e = min(a[i][1], b[j][1])

            if s <= e:
                res.append([s, e])

            if a[i][1] <= b[j][1]:
                i += 1
            else:
                j += 1

        return res