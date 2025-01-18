class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        nums.sort()
        l = ans = 0
        r = len(nums) - 1

        while l <= r:
            if nums[r] + nums[l] > target:
                r -= 1
            else:
                ans += pow(2, r - l, pow(10, 9) + 7)
                l += 1
        return ans % (pow(10, 9) + 7)