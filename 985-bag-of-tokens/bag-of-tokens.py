class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        l = 0
        r = len(tokens) - 1
        ans = 0
        while l <= r:
            if power - tokens[l] >= 0:
                power -= tokens[l]
                l += 1
                ans += 1
            else:
                if (ans > 0) and (tokens[r] >= tokens[l]) and (r != l):
                    power += tokens[r]
                    r -= 1
                    ans -= 1
                else:
                    return ans
        return ans 
