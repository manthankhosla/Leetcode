class Solution:
    def subarraysDivByK(self, a, k):
        n = len(a)
        sum = 0
        res = 0

        freq = {0: 1}

        for i in range(n):
            sum += a[i]

            rem = sum % k

            if rem in freq:
                res += freq[rem]

            freq[rem] = freq.get(rem, 0) + 1

        return res