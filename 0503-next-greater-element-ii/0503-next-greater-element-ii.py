class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        st = []

        for i in range(2 * n - 1, -1, -1):
            idx = i % n

            while st and st[-1] <= nums[idx]:
                st.pop()

            if i < n:
                if st:
                    res[idx] = st[-1]

            st.append(nums[idx])

        return res