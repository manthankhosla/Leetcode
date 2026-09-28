class Solution:
    def subarraySum(self, nums, k):
        sum = 0
        res = 0

        freq = {0: 1}

        for i in range(len(nums)):
            sum += nums[i]

            q = sum - k

            if q in freq:
                res += freq[q]

            if sum in freq:
                freq[sum] += 1
            else:
                freq[sum] = 1

        return res