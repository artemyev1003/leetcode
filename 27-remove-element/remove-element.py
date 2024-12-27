class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        count = len(nums)
        i = 0
        j = count - 1

        while i <= j:
            if nums[i] == val:
                if nums[j] != val:
                    nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                count -= 1
            else:
                i += 1

        return count