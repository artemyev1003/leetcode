from collections import deque


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans = deque()
        l = 0
        r = len(nums) - 1

        while l <= r:
            if abs(nums[l]) < abs(nums[r]):
                ans.appendleft(nums[r] ** 2)
                r -= 1
            else:
                ans.appendleft(nums[l] ** 2)
                l += 1
        return list(ans)
