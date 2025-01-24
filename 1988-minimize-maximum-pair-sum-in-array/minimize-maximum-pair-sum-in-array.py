class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        l = ans = 0
        r = len(nums) - 1

        while l < r:
            ans = max(ans, nums[l] + nums[r])
            l += 1
            r -= 1
        return ans
        