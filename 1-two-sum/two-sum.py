class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_map: dict = {}

        for i in range(len(nums)):
            if (diff := target - nums[i]) in nums_map:
                return [i, nums_map[diff]]
            else:
                nums_map[nums[i]] = i
