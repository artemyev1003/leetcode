class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        ans = [n if char != c else 0 for char in s]

        for i in range(1, n):
            ans[i] = min(ans[i], ans[i-1] + 1)

        for i in range(n - 2, -1, -1):
            ans[i] = min(ans[i], ans[i+1] + 1)

        return ans
