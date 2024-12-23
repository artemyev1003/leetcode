from functools import reduce


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        rows = ["" for _ in range(numRows)]
        i = 0
        down_flag = True
        for char in s:
            rows[i] += char
            if down_flag:
                i += 1
            else:
                i -= 1

            if i == numRows - 1:
                down_flag = False
            if i == 0:
                down_flag = True

        return reduce(lambda x, y: x + y, rows)