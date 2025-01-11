class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while True:
            m = (l + r) // 2
            if m ** 2 <= x < (m + 1) ** 2:
                return m
            elif m ** 2 < x:
                l = m + 1
            else:
                r = m - 1
