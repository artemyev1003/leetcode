class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        _max = len(s)
        _min = 0
        ans = []
        for char in s:
            if char == "D":
                ans.append(_max)
                _max -= 1
            else:
                ans.append(_min)
                _min += 1
        ans.append(_min)
        return ans
