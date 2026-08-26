class Solution:
    def isHappy(self, n: int) -> bool:
        slow=n
        fast=n
        def sqrsumm(n):
            summ=0
            while(n>0):
                d=n%10
                n=n//10
                summ=summ+d*d
            return summ
        while(fast!=1):
            slow=sqrsumm(slow)
            fast=sqrsumm(fast)
            fast=sqrsumm(fast) # writitng two times as fast moves doubles
            if slow==fast and slow!=1:# slow and fast should meet but only at one
                return False
        return True         