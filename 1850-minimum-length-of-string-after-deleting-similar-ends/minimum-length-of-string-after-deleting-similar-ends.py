class Solution:
    def minimumLength(self, s: str) -> int:
        ans = len(s)
        l = 0
        r = ans - 1
        while l < r:
            curr_l = s[l]
            curr_r = s[r]
            if s[l] != s[r]:
                return ans
            while s[l] == curr_r and l < r:
                l += 1
                ans -= 1
            while s[r] == curr_l and r >= l:
                r -= 1 
                ans -= 1
        return ans
