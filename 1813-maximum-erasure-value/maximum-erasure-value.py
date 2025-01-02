class Solution:
    def maximumUniqueSubarray(self, nums: list[int]) -> int:
        left = max_sum = curr_sum = 0
        nums_set = set()
        nums_len = len(nums)

        for right in range(nums_len):
            if nums[right] not in nums_set:
                nums_set.add(nums[right])
                curr_sum += nums[right]
                max_sum = max(max_sum, curr_sum)
            else:
                while nums[right] in nums_set:
                    nums_set.remove(nums[left])
                    curr_sum -= nums[left]
                    left += 1
                nums_set.add(nums[right])
                curr_sum += nums[right]
        return max_sum
