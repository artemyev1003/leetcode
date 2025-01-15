class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        ans = []
        len_nums = len(nums)
        nums.sort()

        for i in range(len_nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, len_nums - 1

            while j < k:
                local_sum = nums[i] + nums[j] + nums[k]
                if local_sum > 0:
                    k -= 1
                elif local_sum < 0:
                    j += 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return ans
