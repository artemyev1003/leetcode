class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p1, p2 = 0, 0
        end = len(nums) - 1

        while p1 <= end:
            if nums[p1] == 0:
                p1 += 1
                continue
            if nums[p2] != 0 and p2 < end:
                p2 += 1
                continue
            if p1 > p2:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 += 1
            p1 += 1