class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        have = {}
        need = {}

        for i in range(len(ransomNote)):
            need[ransomNote[i]] = need.get(ransomNote[i], 0) + 1

        for i in range(len(magazine)):
            have[magazine[i]] = have.get(magazine[i], 0) + 1

        for c in need:
            freq = need[c] #tells freq of c from need, c loops to each char of need
            fhave = have.get(c, 0)

            if fhave < freq:
                return False

        return True