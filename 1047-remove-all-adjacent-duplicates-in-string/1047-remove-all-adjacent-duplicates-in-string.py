class Solution:
    def removeDuplicates(self, s: str) -> str:
        st = []
        n = len(s)

        for i in range(n):
            if not st:
                st.append(s[i])
                continue

            if st[-1] == s[i]:
                st.pop()
                continue

            st.append(s[i])

        res = ""

        while st:
            res += st[-1]
            st.pop()

        return res[::-1]