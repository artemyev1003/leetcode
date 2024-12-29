class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        length = len(nums) - 1
        l, r = 0, length

        med = (l + r) // 2
        while l + 1 < r:
            if nums[med] == target:
                return med
            elif nums[med] > target:
                r = med
            else:
                l = med
            med = (l + r) // 2

        if nums[l] < target <= nums[r]:
            return l + 1

        if target > nums[r]:
            return r + 1

        return l