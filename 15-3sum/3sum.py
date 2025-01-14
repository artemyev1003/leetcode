class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        visited = set()
        nums.sort()

        if set(nums) == {0}:
            return [[0, 0, 0]]

        for k in range(2, len(nums)):
            i = 0
            j = k - 1

            while i < j:
                local_sum = nums[i] + nums[j]
                if local_sum == -nums[k]:
                    h = f"{nums[i]}_{nums[j]}_{nums[k]}"
                    if h not in visited:
                        ans.append([nums[i], nums[j], nums[k]])
                        visited.add(h)
                    j -= 1
                elif local_sum < -nums[k]:
                    i += 1
                else:
                    j -= 1
        return ans