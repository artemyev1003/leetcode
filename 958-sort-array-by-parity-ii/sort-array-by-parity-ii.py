class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        even = 0
        odd = 1
        ans = [None for _ in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                ans[even] = nums[i]
                even += 2
            if nums[i] % 2 != 0:
                ans[odd] = nums[i]
                odd += 2

        return ans
