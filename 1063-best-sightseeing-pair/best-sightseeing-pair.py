class Solution:
    def maxScoreSightseeingPair(self, values: int | list) -> int:
        i = ans = 0
        j = 1

        while j < len(values):
            if (curr := values[i] + values[j] + i - j) > ans:
                ans = curr

            if values[j] > values[i] + i - j:
                i, j = j, j + 1
            else:
                j += 1
        return ans