class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] == val:
                if nums[right] != val:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                else:
                    right -= 1
            else:
                left += 1
        return left