class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        ans = 1
        l = 0
        nice_sum = nums[0]

        for r in range(1, n):
            if nice_sum ^ nums[r] != nice_sum + nums[r]:
                if (curr := r - l) > ans:
                    ans = curr
                while nice_sum ^ nums[r] != nice_sum + nums[r]:
                    nice_sum -= nums[l]
                    l += 1
            nice_sum += nums[r]
        ans = max(r - l + 1, ans)
        return ans