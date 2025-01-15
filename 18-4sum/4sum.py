class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ans = []
        nums.sort()

        len_nums = len(nums)

        for a in range(len_nums):

            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a + 1, len_nums):

                if b - a > 1 and nums[b] == nums[b - 1]:
                    continue

                c, d = b + 1, len_nums - 1

                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]
                    if total < target:
                        c += 1
                    elif total > target:
                        d -= 1
                    else:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])

                        c += 1
                        while nums[c] == nums[c - 1] and c < d:
                            c += 1
        return ans