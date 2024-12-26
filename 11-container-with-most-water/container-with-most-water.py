class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0

        while l != r:
            if height[l] > height[r]:
                curr = height[r] * (r - l)
                r -= 1
            else:
                curr = height[l] * (r - l)
                l += 1
            if curr > ans:
                ans = curr

        return ans
