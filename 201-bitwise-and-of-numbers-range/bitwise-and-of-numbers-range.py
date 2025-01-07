class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        right_bin = bin(right)[2:]
        left_bin = bin(left)[2:]
        len_right = len(right_bin)
        left_bin = "0" * (len_right - len(left_bin)) + bin(left)[2:]

        ans_bin = ""

        for i in range(len_right):
            if left_bin[i] == right_bin[i]:
                ans_bin += left_bin[i]
            else:
                ans_bin += "0" * (len_right - i)
                break
        return int(ans_bin, 2)
