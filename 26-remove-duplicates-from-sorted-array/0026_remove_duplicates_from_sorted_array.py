class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        p1, p2 = 0, 1
        k, l = 1, len(nums) - 1

        while p2 <= l:
            if nums[p1] == nums[p2]:
                p2 += 1
            else:
                k += 1
                nums[k-1] = nums[p2]
                p1 = p2
                p2 += 1
        return k
