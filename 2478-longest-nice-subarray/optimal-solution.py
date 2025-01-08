class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        left = mask = ans = 0

        for right in range(len(nums)):
            while mask & nums[right]:
                mask ^= nums[left]
                left += 1
            mask |= nums[right]
            ans = max(ans, right - left + 1)
        return ans
