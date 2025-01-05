from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        complement = 0

        for i, j in zip_longest(a[::-1], b[::-1], fillvalue="0"):
            if i == "1" and j == "1":
                if complement == 1:
                    ans = "1" + ans
                    complement = 1
                else:
                    ans = "0" + ans
                    complement = 1
            elif i == "1" or j == "1":
                if complement == 1:
                    ans = "0" + ans
                    complement = 1
                else:
                    ans = "1" + ans
            else:
                if complement == 1:
                    ans = "1" + ans
                    complement = 0
                else:
                    ans = "0" + ans

        if complement:
            ans = "1" + ans
        return ans