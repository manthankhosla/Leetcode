class Solution:
    def findMaxLength(self, a):
        n = len(a)

        zero = 0
        one = 0
        res = 0

        freq = {}

        for i in range(n):

            if a[i] == 0:
                zero += 1
            else:
                one += 1

            diff = zero - one

            # If equal number of 0s and 1s from index 0 to i
            if diff == 0:
                res = max(res, i + 1)
                continue

            # First time seeing this diff
            if diff not in freq:
                freq[diff] = i

            # Diff was seen before
            else:
                idx = freq[diff]
                length = i - idx
                res = max(res, length)

        return res